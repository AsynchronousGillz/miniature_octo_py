#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
"""
"""

from pydantic import BaseModel
from typing import List, Type, Optional, Union


class Fixed(BaseModel):
    """ TODO """
    fixed_value: int


class SizeInBits(BaseModel):
    """ TODO """
    fixed: Optional[Fixed]


class Unit(BaseModel):
    """ TODO """
    description: Optional[str]
    text: Optional[str]


class Enumeration(BaseModel):
    """ TODO """
    value: Optional[str]
    label: Optional[str]


class DataEncoding(BaseModel):
    """ TODO """
    byte_order: str
    encoding: Optional[str]
    size_in_bits: Union[SizeInBits, int, None]


class ModelType(BaseModel):
    """ TODO """
    encoding: Type[DataEncoding]
    name: str
    long_description: Optional[str]
    short_description: Optional[str]
    tag: str
    unit_set: List[Unit] = []


class EnumeratedArgumentType(ModelType):
    """ TODO """
    enumeration_list: List[Enumeration]


class FloatArgumentType(ModelType):
    """ TODO """


class IntegerArgumentType(ModelType):
    """ TODO """
    size_in_bits: int
    signed: bool


class StringArgumentTpe(ModelType):
    """ TODO """
