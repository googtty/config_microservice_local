from os import path

import yaml


class Source(object):
    def __init__(self, file_path, root='/'):
        split_name = path.basename(file_path).split('.')

        self.root = root
        self.file_path = file_path
        self.full_path = path.join(self.root, self.file_path)
        self.name = split_name[0]
        self.extension = split_name[-1]


def load_data(source):
    with open(source.full_path, 'rb') as f:
        data = f.read()
        if source.extension == "yaml":
            data = yaml.safe_load(data)
    return data
