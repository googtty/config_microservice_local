from os import path, listdir

from fastapi import APIRouter, HTTPException

from utils import Source, load_data
from variables import RESOURCES_ROOT

schema_router = APIRouter()


@schema_router.get('/{schema_type}')
async def get_schema_configurations_api(schema_type: str):
    try:
        item = get_schema_configurations(schema_type)
    except TypeError as e:
        raise HTTPException(status_code=404, detail=f'Unable to read configuration for schema: {schema_type}')

    return item


@schema_router.get('/{schema_type}/{schema_name}')
async def get_schema_configuration_api(schema_type: str, schema_name: str):
    try:
        item = get_schema_configurations(schema_type, schema_name)[0]
    except TypeError as e:
        raise HTTPException(status_code=404,
                            detail=f'Unable to read configuration for schema: {schema_type}/{schema_name}')

    return item


def get_schema_configurations(schema_type, schema_name=None, root_directory=RESOURCES_ROOT):
    schema_dir = path.join(root_directory, schema_type)

    if schema_name:
        file_names = [schema_name + '.txt']
    else:
        file_names = listdir(schema_dir)

    schema_list = []

    for file_name in file_names:
        source = Source(file_name, schema_dir)

        data = load_data(source)
        schema = {'name': source.name, 'content': data}
        schema_list.append(schema)

    return schema_list
