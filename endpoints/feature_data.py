from os import walk, path

from fastapi import APIRouter, HTTPException

from utils import Source, load_data
from variables import RESOURCES_ROOT

feature_data_router = APIRouter()


@feature_data_router.get('/{data_name}')
async def feature_data_api(data_name: str):
    try:
        item = get_feature_data(data_name)
    except TypeError as e:
        raise HTTPException(status_code=404, detail=f'Unable to read configuration for feature data: {data_name}')

    return item


def get_feature_data(data_name, root_directory=path.join(RESOURCES_ROOT, 'feature_data')):
    root, dir_names, file_names = next(walk(root_directory))

    for file_name in file_names:
        if file_name.split('.')[0] == data_name:
            source = Source(file_name, root_directory)

            data = load_data(source)
            feature = {'name': source.name, 'content': data, 'type': source.extension}
            return feature

    return {}
