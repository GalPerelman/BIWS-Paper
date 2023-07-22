import os
import json
import pandas as pd

import preprocess
import metrics
from greedy import Greedy
from exhaustive import ControlChecker
import utils

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option("display.precision", 2)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCES_DIR = os.path.join(BASE_DIR, 'resources')
OUTPUT_DIR = os.path.join(BASE_DIR, "output")


if __name__ == "__main__":
    # Command to search pump through all networks (years) - to run at the end
    # df = preprocess.iterate_all_pumps_combs(os.path.join(RESOURCES_DIR, 'networks', 'base'),
    #                                         os.path.join(OUTPUT_DIR, 'optimal_pumps.csv'))

    """ Run 1st year greedy """
    # The first year budget is only 550000 because of pumps replacements
    # output_path = os.path.join(OUTPUT_DIR, 'fcv', '1_greedy_output', time.strftime("%Y%m%d%H%M%S") + '_y1')
    # inp = os.path.join(RESOURCES_DIR, "networks", "1_Input-FCV",  "y1.inp")
    # greedy = Greedy(inp, output_dir=output_path, budget=550000, actions_ratio=0.3, hgl_threshold=0.003, n_leaks=1000,
    #                 reevaluate_ratio=0.03, total_run_time=24, hours_duration=168)
    # greedy.pipes.to_csv(os.path.join(output_path, 'pipes.csv'))
    # greedy.leaks.to_csv(os.path.join(output_path, 'leaks.csv'))
    # greedy.start()

    """ Prepare network for year 2 - change leaks emitter coefficients """
    # previous_year_file = os.path.join(OUTPUT_DIR, 'fcv', '1_greedy_output', '20230401103241_y1', 'y1-finalized.inp')  # The final inp from previous year
    # preprocess.change_leaks_coef(previous_year_file, 2, os.path.join(RESOURCES_DIR, 'networks', '1_input-FCV', 'y2.inp'))

    """ Run 2nd year greedy """
    # output_path = os.path.join(OUTPUT_DIR, 'fcv', '1_greedy_output', time.strftime("%Y%m%d%H%M%S") + '_y2')
    # inp = os.path.join(RESOURCES_DIR, "networks", "1_Input-FCV", "y2.inp")
    # previous_year_last_evaluations = os.path.join(RESOURCES_DIR, "networks", "1_Input-FCV", 'y2_init')
    # greedy = Greedy(inp, output_dir=output_path, budget=670000,
    #                 actions_ratio=0.3, hgl_threshold=0.003, n_leaks=1000, reevaluate_ratio=0.03,
    #                 total_run_time=24, hours_duration=168, load_init_path=previous_year_last_evaluations)
    # greedy.pipes.to_csv(os.path.join(output_path, 'pipes.csv'))
    # greedy.leaks.to_csv(os.path.join(output_path, 'leaks.csv'))
    # greedy.start()

    """ Prepare network for year 3 - change leaks emitter coefficients """
    # previous_year_file = os.path.join(OUTPUT_DIR, 'fcv', '1_greedy_output', '20230404100138_y2', 'y2-finalized.inp')  # The final inp from previous year
    # preprocess.change_leaks_coef(previous_year_file, 3, os.path.join(RESOURCES_DIR, 'networks', '1_input-FCV', 'y3.inp'))

    """ Run 3rd year greedy """
    # output_path = os.path.join(OUTPUT_DIR, 'fcv', '1_greedy_output', time.strftime("%Y%m%d%H%M%S") + '_y3')
    # inp = os.path.join(RESOURCES_DIR, "networks", "1_Input-FCV", "y3.inp")
    # previous_year_last_evaluations = os.path.join(RESOURCES_DIR, "networks", "1_Input-FCV", 'y3_init')
    # greedy = Greedy(inp, output_dir=output_path, budget=670000,
    #                 actions_ratio=0.3, hgl_threshold=0.003, n_leaks=1000, reevaluate_ratio=0.03,
    #                 total_run_time=24, hours_duration=168, load_init_path=previous_year_last_evaluations)
    # greedy.pipes.to_csv(os.path.join(output_path, 'pipes.csv'))
    # greedy.leaks.to_csv(os.path.join(output_path, 'leaks.csv'))
    # greedy.start()

    """ Prepare network for year 4 - change leaks emitter coefficients """
    # previous_year_file = os.path.join(OUTPUT_DIR, 'fcv', '1_greedy_output', '20230405094748_y3', 'y3-finalized.inp')  # The final inp from previous year
    # preprocess.change_leaks_coef(previous_year_file, 4, os.path.join(RESOURCES_DIR, 'networks', '1_input-FCV', 'y4.inp'))

    """ Run 4th year greedy """
    # output_path = os.path.join(OUTPUT_DIR, 'fcv', '1_greedy_output', time.strftime("%Y%m%d%H%M%S") + '_y4')
    # inp = os.path.join(RESOURCES_DIR, "networks", "1_Input-FCV", "y4.inp")
    # previous_year_last_evaluations = os.path.join(RESOURCES_DIR, "networks", "1_Input-FCV", 'y4_init')
    # greedy = Greedy(inp, output_dir=output_path, budget=670000,
    #                 actions_ratio=0.3, hgl_threshold=0.003, n_leaks=1000, reevaluate_ratio=0.03,
    #                 total_run_time=24, hours_duration=168, load_init_path=previous_year_last_evaluations)
    # greedy.pipes.to_csv(os.path.join(output_path, 'pipes.csv'))
    # greedy.leaks.to_csv(os.path.join(output_path, 'leaks.csv'))
    # greedy.start()

    """ Prepare network for year 5 - change leaks emitter coefficients """
    # previous_year_file = os.path.join(OUTPUT_DIR, 'fcv', '1_greedy_output', '20230406091741_y4', 'y4-finalized.inp')  # The final inp from previous year
    # preprocess.change_leaks_coef(previous_year_file, 5, os.path.join(RESOURCES_DIR, 'networks', '1_input-FCV', 'y5.inp'))

    """ Run 5th year greedy """
    # output_path = os.path.join(OUTPUT_DIR, 'fcv', '1_greedy_output', time.strftime("%Y%m%d%H%M%S") + '_y5')
    # inp = os.path.join(RESOURCES_DIR, "networks", "1_Input-FCV", "y5.inp")
    # previous_year_last_evaluations = os.path.join(RESOURCES_DIR, "networks", "1_Input-FCV", 'y5_init')
    # greedy = Greedy(inp, output_dir=output_path, budget=670000,
    #                 actions_ratio=0.3, hgl_threshold=0.003, n_leaks=1000, reevaluate_ratio=0.03,
    #                 total_run_time=24, hours_duration=168, load_init_path=previous_year_last_evaluations)
    # greedy.pipes.to_csv(os.path.join(output_path, 'pipes.csv'))
    # greedy.leaks.to_csv(os.path.join(output_path, 'leaks.csv'))
    # greedy.start()

    """ Run exhaustive controls search y1 """
    # inp_file_path = os.path.join(OUTPUT_DIR, 'fcv', 'controls', 'y1', 'y1-finalized-no-controls.inp')
    # elements_file_path = os.path.join(RESOURCES_DIR, 'valves.json')
    # output_path = os.path.join(OUTPUT_DIR, 'fcv', 'controls', 'y1')
    # with open(elements_file_path) as f:
    #     grouped_elements = json.load(f)
    #     for group, elements in grouped_elements.items():
    #         cc = ControlChecker(inp_file_path, group, elements, output_path)
    #         cc.evaluate_controls()

    """ Run exhaustive controls search y2 """
    # inp_file_path = os.path.join(OUTPUT_DIR, 'fcv', 'controls', 'y2', 'y2-finalized-no-controls.inp')
    # elements_file_path = os.path.join(RESOURCES_DIR, 'valves.json')
    # output_path = os.path.join(OUTPUT_DIR, 'fcv', 'controls', 'y2')
    # with open(elements_file_path) as f:
    #     grouped_elements = json.load(f)
    #     for group, elements in grouped_elements.items():
    #         cc = ControlChecker(inp_file_path, group, elements, output_path)
    #         cc.evaluate_controls()

    """ Run exhaustive controls search y3 """
    # inp_file_path = os.path.join(OUTPUT_DIR, 'fcv', 'controls', 'y3', 'y3-finalized-no-controls.inp')
    # elements_file_path = os.path.join(RESOURCES_DIR, 'valves.json')
    # output_path = os.path.join(OUTPUT_DIR, 'fcv', 'controls', 'y3')
    # with open(elements_file_path) as f:
    #     grouped_elements = json.load(f)
    #     for group, elements in grouped_elements.items():
    #         cc = ControlChecker(inp_file_path, group, elements, output_path)
    #         cc.evaluate_controls()

    """ Compare single year networks """
    # solution_path = "G:/My Drive/3_Academy/P.hd/2_Research/Projects/BIWS-Comp/Code/postprocess/v2/greedy/finalization/y5.inp"
    # score = metrics.evaluate_single_net(solution_path)
    # score = utils.round_dict(score, 3)
    # print('BIWS:', score)
    # #
    # solution_path = "output/fcv/final_networks/y5-finalized.inp"
    # score = metrics.evaluate_single_net(solution_path)
    # score = utils.round_dict(score, 3)
    # print('New:', score)

    # solution_path = "output/fcv/controls/y2/y2-finalized-with-controls.inp"
    # score = metrics.evaluate_single_net(solution_path)
    # score = utils.round_dict(score, 3)
    # print('New with controls:', score)

    # solution_path = "output/fcv/y5_test.inp"
    # score = metrics.evaluate_single_net(solution_path)
    # score = utils.round_dict(score, 3)
    # print('New with controls:', score)
    #
    # solution_path = "output/fcv/y5_test2.inp"
    # score = metrics.evaluate_single_net(solution_path)
    # score = utils.round_dict(score, 3)
    # print('New with controls:', score)


    # df = pd.read_csv(os.path.join(OUTPUT_DIR, "controls_classes_opt.csv"))
    # candidates = {}
    # for group in df['class'].unique():
    #     candidates[group] = df.loc[(df['year'] == 'y1') & (df['class'] == group), 'idx'].to_list()
    #
    # print(candidates)
    # combs = exhaustive.get_combinations(candidates)
    # print(combs)
    # exhaustive.multi_class_controls(combs)

    # comp_solution = "G:/My Drive/3_Academy/P.hd/2_Research/Projects/BIWS-Comp/Code/postprocess/v2/greedy/finalization"
    # comp_solution = "C:/Users/User/Desktop/New folder"
    # score = utils.round_dict(metrics.evaluate_scenario(comp_solution), 3)
    # print(f"Battle score: {score}")
    # print('===============================================================================================')

    paper_solution = "C:/Users/User/Documents/GitHub/BIWS-Paper/output/fcv/4_final_networks_controls"
    score = utils.round_dict(metrics.evaluate_scenario(paper_solution), 3)
    print(f"Paper score: {score}")
    print('===============================================================================================')