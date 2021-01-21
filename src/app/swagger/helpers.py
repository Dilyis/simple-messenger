from drf_yasg import openapi
from typing import Dict


def array(item: openapi.Schema, **kwargs) -> openapi.Schema:
    return openapi.Schema(type=openapi.TYPE_ARRAY, items=item, **kwargs)


def array_obj(obj_props, obj_kwargs=None, **kwargs) -> openapi.Schema:
    obj_kwargs = obj_kwargs or {}
    return array(obj(obj_props, **obj_kwargs), **kwargs)


def obj(props: Dict[str, openapi.Schema], **kwargs) -> openapi.Schema:
    return openapi.Schema(type=openapi.TYPE_OBJECT, properties=props, **kwargs)


def number(title=None, **kwargs) -> openapi.Schema:
    return openapi.Schema(type=openapi.TYPE_NUMBER, title=title, **kwargs)


def integer(title=None, **kwargs):
    return openapi.Schema(title=title, type=openapi.TYPE_INTEGER,  **kwargs)


def string(title=None, **kwargs):
    return openapi.Schema(title=title, type=openapi.TYPE_STRING,  **kwargs)


def boolean(**kwargs):
    return openapi.Schema(type=openapi.TYPE_BOOLEAN, **kwargs)


def date_time(title=None, **kwargs) -> openapi.Schema:
    return openapi.Schema(
        title=title,
        type=openapi.TYPE_STRING,
        format=openapi.FORMAT_DATETIME,
        **kwargs
    )


def date(title=None, **kwargs) -> openapi.Schema:
    return openapi.Schema(
        title=title,
        type=openapi.TYPE_STRING,
        format=openapi.FORMAT_DATE,
        **kwargs
    )
