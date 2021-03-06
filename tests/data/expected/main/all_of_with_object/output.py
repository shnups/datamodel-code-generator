# generated by datamodel-codegen:
#   filename:  all_of_with_object.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class Home(BaseModel):
    address: Optional[str] = None
    zip: Optional[str] = None


class Kind(BaseModel):
    description: Optional[str] = None


class Id(BaseModel):
    id: Optional[int] = None


class Pet(Home, Kind, Id):
    name: Optional[str] = None
    age: Optional[int] = None
