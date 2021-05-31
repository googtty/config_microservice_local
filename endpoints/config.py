from typing import Optional

from fastapi import APIRouter, HTTPException
from ptrx_config import get_tenant_configuration
from pydantic import BaseModel

config_router = APIRouter()


class ConfigResponse(BaseModel):
    tenant: str
    config: dict


@config_router.get('/{tenant_name}/', response_model=ConfigResponse)
async def get_config(tenant_name: str, file_name: Optional[str] = None):
    try:
        config = get_tenant_configuration(tenant_name)
    except TypeError as e:
        raise HTTPException(status_code=404, detail=f'Unable to read configuration for tenant: {tenant_name}')

    if file_name:
        if file_name not in config:
            raise HTTPException(status_code=404, detail=f'Configuration not found: {file_name}')
        config = config[file_name]

    config_resp = ConfigResponse(tenant=tenant_name, config=config)
    return config_resp
