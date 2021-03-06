# generated by datamodel-codegen:
#   filename:  modular.yaml
#   timestamp: 1985-10-26T08:21:00+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel

from .. import CustomId, CustomOptional


class CustomTea(BaseModel):
    flavour: Optional[str] = None
    id: Optional[CustomId] = None
    self: Optional[CustomTea] = None
    optional: Optional[List[CustomOptional]] = None


class CustomTeaClone(BaseModel):
    flavour: Optional[str] = None
    id: Optional[CustomId] = None
    self: Optional[CustomTea] = None
    optional: Optional[List[CustomOptional]] = None


class CustomList(BaseModel):
    __root__: List[CustomTea]


CustomTea.update_forward_refs()
