from os import path

from fastapi import APIRouter
from fastapi.responses import FileResponse

from utils import Source, load_data
from variables import MODELS_ROOT

models_router = APIRouter()


@models_router.get('/{model_name}/{file_name}/')
async def get_model_file_api(model_name: str, file_name: str):
    file_path = path.join(MODELS_ROOT, model_name, file_name)
    return FileResponse(file_path)


def get_model_file(model_name, file_name, root_directory=MODELS_ROOT):
    model_dir = path.join(root_directory, model_name)

    source = Source(file_name, model_dir)

    data = load_data(source)
    schema = {'name': source.name, 'content': data}

    return schema
