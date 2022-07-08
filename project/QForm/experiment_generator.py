import experiment as exp
from configs import experiment_conf as conf
from project import global_conf as global_project_conf


def run_create_experiments_set(dataset):
    exp.launch_QForm()

    results_experiments = {
        "tool_1_PZ": [],
        "tool_2_PY": [],
        "tool_3_PX": [],
        "mean_stress_equal": []
    }

    for experiment in dataset:
        path_geometry = global_project_conf.path_save__ + "\\" + dataset["name_model"]

        res = exp.create_experiment(results_experiments, path_geometry, dataset["VX"], dataset["VY"])

    print(conf.success_QForm_work)

    return results_experiments
