from project.configs import main as global_conf


def visibility():
    mode = InteractionMode.Solid

    ViewHelper.SetViewMode(mode, None)


def center_coordinate(edge_length):
    return PointUV.Create(edge_length / 2, edge_length / 2)


def save_model(name, path=global_conf.path_save):
    options = ExportOptions.Create()
    DocumentSave.Execute(path + "\\" + name + ".stp", options)


def remove_model():
    selection = BodySelection.Create(GetRootPart().Bodies[0])
    result = Delete.Execute(selection)
