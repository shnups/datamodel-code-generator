# generated by datamodel-codegen:
#   filename:  modular.yaml
#   timestamp: 1985-10-26T08:21:00+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from .. import CustomId


class CustomTea(BaseModel):
    flavour: Optional[str] = None
    id: Optional[CustomId] = None


class CustomCocoa(BaseModel):
    quality: Optional[int] = None
