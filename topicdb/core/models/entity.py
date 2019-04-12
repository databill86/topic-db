"""
Entity class. Part of the StoryTechnologies project.

June 12, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import uuid
from typing import List, Optional

from slugify import slugify  # type: ignore

from topicdb.core.models.attribute import Attribute
from topicdb.core.store.topicstoreerror import TopicStoreError


class Entity:

    def __init__(self, identifier: str = '', instance_of: str = 'entity') -> None:
        if instance_of == '':
            raise TopicStoreError("Empty 'instance of' parameter")

        if identifier == '':
            self.__identifier = str(uuid.uuid4())
        elif identifier == '*':  # Universal Scope.
            self.__identifier = '*'
        else:
            self.__identifier = slugify(str(identifier))

        self.__instance_of = slugify(str(instance_of))
        self.__attributes: List[Attribute] = []

    @property
    def identifier(self) -> str:
        return self.__identifier

    @property
    def instance_of(self) -> str:
        return self.__instance_of

    @instance_of.setter
    def instance_of(self, value: str) -> None:
        if value == '':
            raise TopicStoreError("Empty 'value' parameter")
        self.__instance_of = slugify(str(value))

    @property
    def attributes(self) -> List[Attribute]:
        return self.__attributes

    def add_attribute(self, attribute: Attribute) -> None:
        self.__attributes.append(attribute)

    def add_attributes(self, attributes: List[Attribute]) -> None:
        for attribute in attributes:
            self.__attributes.append(attribute)

    def remove_attribute(self, identifier: str) -> None:
        self.__attributes[:] = [x for x in self.__attributes if x.identifier != identifier]

    def get_attribute(self, identifier: str) -> Optional[Attribute]:
        result = None
        for attribute in self.__attributes:
            if attribute.identifier == identifier:
                result = attribute
                break
        return result

    def get_attribute_by_name(self, name: str) -> Optional[Attribute]:
        result = None
        for attribute in self.__attributes:
            if attribute.name == name:
                result = attribute
                break
        return result

    def clear_attributes(self) -> None:
        del self.__attributes[:]
