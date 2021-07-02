from os import path, listdir

from fastapi import APIRouter, HTTPException

from utils import Source, load_data
from variables import RESOURCES_ROOT

feature_data_router = APIRouter()


@feature_data_router.get('')
async def feature_datas_api():
    try:
        item = get_feature_data()
    except TypeError as e:
        raise HTTPException(status_code=404, detail=f'Unable to read configuration for feature data')

    return item


@feature_data_router.get('/{data_name}')
async def feature_data_api(data_name: str):
    try:
        item = get_feature_data(data_name)
    except TypeError as e:
        raise HTTPException(status_code=404, detail=f'Unable to read configuration for feature data: {data_name}')

    return item


def get_feature_data(data_name=None, root_directory=path.join(RESOURCES_ROOT, 'feature_data')):
    file_names = listdir(root_directory)
    feature_data = []

    for file_name in file_names:
        if not data_name or file_name.split('.')[0] == data_name:
            source = Source(file_name, root_directory)
            data = load_data(source)
            feature = {'name': source.name, 'content': data, 'extension': source.extension}
            if data_name:
                return feature
            feature_data.append(feature)

    return feature_data
