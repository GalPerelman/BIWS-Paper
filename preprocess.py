import os
import numpy as np
import pandas as pd
import itertools
import glob
from tqdm import tqdm
import wntr
from wntr.network.io import write_inpfile
import warnings

from metrics import Evaluator
import utils


warnings.filterwarnings(action='ignore', module='wntr')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCES_DIR = os.path.join(BASE_DIR, 'resources')


class Preprocess:
    def __init__(self, inp_path, out_files_dir, out_inp_name):
        self.inp_path = inp_path
        self.out_files_dir = out_files_dir
        self.out_inp_path = os.path.join(self.out_files_dir, out_inp_name)
        self.wn = self.load_inp_with_wntr()

    def load_inp_with_wntr(self):
        return wntr.network.WaterNetworkModel(self.inp_path)

    def add_leak(self, pipe_id, length_from_start, coef, factor, leak_idx):
        try:
            old_pipe_id, j = pipe_id.split("_")
            new_pipe_id = old_pipe_id + "_" + str(int(j) + 1)

        except ValueError:
            new_pipe_id = pipe_id + '_1'

        pipe = self.wn.get_link(pipe_id)
        split_at_point = length_from_start / pipe.length

        self.wn = wntr.morph.split_pipe(self.wn, pipe_id, new_pipe_id, 'sp_' + str(leak_idx),
                                        add_pipe_at_end=True, split_at_point=split_at_point)

        split_node = self.wn.get_node('sp_' + str(leak_idx))
        split_elevation = split_node.elevation
        split_coords = split_node.coordinates

        self.wn.add_junction('Leak_' + str(leak_idx), elevation=split_elevation, coordinates=split_coords)
        leak_node = self.wn.get_node('Leak_' + str(leak_idx))
        leak_node.emitter_coefficient = factor * coef / 1000
        leak_node.pressure_exponent = 1

        self.wn.add_pipe('LeakPipe_'+str(leak_idx), split_node.name, leak_node.name, length=0.1, diameter=pipe.diameter,
                         roughness=pipe.roughness, check_valve=True)

    def add_all_leaks(self, year=0):
        """
            This function is only for adding the leaks junctions and splitting the pipes
            Emitter coefficients are set according to year zero
            Changing the emitter coefficients between years is done with the function: change_leaks_coef
        """
        df = pd.read_csv(os.path.join(RESOURCES_DIR, 'preprocess', 'leaks_preprocess.csv'))
        factor = np.exp(0.25 * year * 52 / 260)
        for i, row in tqdm(df.iterrows(), total=len(df)):
            self.add_leak(row['Link_id'], row['Length_'], row['Coef'], factor, i)

    def write_modified_inp(self):
        wntr.network.io.write_inpfile(self.wn, self.out_inp_path)


def change_leaks_coef(inp_path, year, export_path):
    """
    Function for modifying the leaks emitter coefficients between years
    :param inp_path:        path to input network - network with leaks nodes (str)
    :param year:            year number where initial network is 0 (int)
    :param export_path:     path to save modified network (str)
    """
    leaks_data = pd.read_csv(os.path.join(RESOURCES_DIR, 'preprocess', 'leaks_preprocess.csv'))
    net = wntr.network.WaterNetworkModel(inp_path)
    net_leaks = net.query_node_attribute('emitter_coefficient').dropna()
    net_leaks.name = 'current'

    df = pd.merge(leaks_data[['Leak_id', 'Coef']], net_leaks, left_on='Leak_id', right_index=True, how='inner')
    df['check'] = df['Coef'] * np.exp(0.25 * 52 / 260) / 1000
    df['year_' + str(year)] = df['Coef'] * np.exp(0.25 * year * 52 / 260) / 1000

    for i, row in df.iterrows():
        leak_node = net.get_node(row['Leak_id'])
        leak_node.emitter_coefficient = row['year_' + str(year)]
    net.write_inpfile(export_path)


def iterate_all_pumps_combs(networks_path: str):
    """ A function to evaluate pumps' models combinations

    :param networks_path:   path to dir with 6 networks (one for every year)
    :return:                csv file with objectives value for every pumps combination
    """

    df = pd.read_csv(os.path.join(RESOURCES_DIR, "pump_candidates.csv"))
    df['pump_model'] = df['pump_id'] + '-' + df['model']

    models = []
    groups = df.groupby(by='pump_id')
    for group, data in groups:
        models.append(data['pump_model'].tolist())

    combinations = (list(itertools.product(*models)))
    results = pd.DataFrame()
    for i, c in enumerate(combinations):
        indicators = replace_pumps_and_evaluate_solution(networks_path, df.loc[df['pump_model'].isin(c)], path=str(i)+'.inp')
        pumps = df.loc[df['pump_model'].isin(c)]
        pumps = dict(zip(pumps["pump_id"], pumps["model"]))
        results = pd.concat([results, pd.DataFrame.from_dict({**indicators, **pumps}, orient='index').T], axis=0)
    return results


def replace_pumps_and_evaluate_solution(networks_path, pumps_to_replace: pd.DataFrame, path):
    networks = []
    for file_path in glob.glob(os.path.join(networks_path, '*.inp')):
        net = wntr.network.WaterNetworkModel(file_path)
        for i, row in pumps_to_replace.iterrows():
            net = utils.replace_pumps(net, row["pump_id"], row["model"], row["psv_diameter"], row["psv_setting"])

        networks.append(net)
        write_inpfile(net, str(i) + '-' + path)
    sc = Evaluator(networks)
    indicators = sc.evaluate_scenario()

    return indicators


if __name__ == '__main__':
    base_net = os.path.join(RESOURCES_DIR, 'networks', 'BIWS.inp')
    output_path = os.path.join(RESOURCES_DIR, 'networks')
    p = Preprocess(base_net, output_path, 'BIWS_y0.inp')
    p.add_all_leaks()
    p.write_modified_inp()