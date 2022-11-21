import os

def parse_filename(filename: str):
    path_components = filename.split('/')

    return path_components[:-1], path_components[-1] # path_prefixes list, filename

def create_path_hierarchy(hierarchy_list: list, starting_path: str):
    # create all prefix directories if they do not exist
    for dir in hierarchy_list:
        dir_path = os.path.join(starting_path, dir)
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)

        # update current path
        starting_path = dir_path