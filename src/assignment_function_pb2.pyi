import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssignmentRequest(_message.Message):
    __slots__ = ("namespace", "userId", "goals")
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    GOALS_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    userId: str
    goals: _containers.RepeatedCompositeFieldContainer[Goal]
    def __init__(self, namespace: _Optional[str] = ..., userId: _Optional[str] = ..., goals: _Optional[_Iterable[_Union[Goal, _Mapping]]] = ...) -> None: ...

class AssignmentResponse(_message.Message):
    __slots__ = ("namespace", "userId", "assignedGoals")
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEDGOALS_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    userId: str
    assignedGoals: _containers.RepeatedCompositeFieldContainer[Goal]
    def __init__(self, namespace: _Optional[str] = ..., userId: _Optional[str] = ..., assignedGoals: _Optional[_Iterable[_Union[Goal, _Mapping]]] = ...) -> None: ...

class Goal(_message.Message):
    __slots__ = ("code", "challengeCode", "name", "isActive", "tags", "requirements", "rewards", "createdAt", "updatedAt")
    CODE_FIELD_NUMBER: _ClassVar[int]
    CHALLENGECODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ISACTIVE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    code: str
    challengeCode: str
    name: str
    isActive: bool
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    requirements: _containers.RepeatedCompositeFieldContainer[Requirement]
    rewards: _containers.RepeatedCompositeFieldContainer[Reward]
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    def __init__(self, code: _Optional[str] = ..., challengeCode: _Optional[str] = ..., name: _Optional[str] = ..., isActive: bool = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., requirements: _Optional[_Iterable[_Union[Requirement, _Mapping]]] = ..., rewards: _Optional[_Iterable[_Union[Reward, _Mapping]]] = ..., createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Requirement(_message.Message):
    __slots__ = ("operator", "predicates")
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    PREDICATES_FIELD_NUMBER: _ClassVar[int]
    operator: str
    predicates: _containers.RepeatedCompositeFieldContainer[Predicate]
    def __init__(self, operator: _Optional[str] = ..., predicates: _Optional[_Iterable[_Union[Predicate, _Mapping]]] = ...) -> None: ...

class Predicate(_message.Message):
    __slots__ = ("parameterName", "parameterType", "matcher", "targetValue", "statCycleId", "id")
    PARAMETERNAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETERTYPE_FIELD_NUMBER: _ClassVar[int]
    MATCHER_FIELD_NUMBER: _ClassVar[int]
    TARGETVALUE_FIELD_NUMBER: _ClassVar[int]
    STATCYCLEID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    parameterName: str
    parameterType: str
    matcher: str
    targetValue: float
    statCycleId: str
    id: str
    def __init__(self, parameterName: _Optional[str] = ..., parameterType: _Optional[str] = ..., matcher: _Optional[str] = ..., targetValue: _Optional[float] = ..., statCycleId: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class Reward(_message.Message):
    __slots__ = ("type", "itemId", "itemName", "quantity")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    ITEMNAME_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    type: str
    itemId: str
    itemName: str
    quantity: float
    def __init__(self, type: _Optional[str] = ..., itemId: _Optional[str] = ..., itemName: _Optional[str] = ..., quantity: _Optional[float] = ...) -> None: ...

class Goals(_message.Message):
    __slots__ = ("goals",)
    GOALS_FIELD_NUMBER: _ClassVar[int]
    goals: _containers.RepeatedCompositeFieldContainer[Goal]
    def __init__(self, goals: _Optional[_Iterable[_Union[Goal, _Mapping]]] = ...) -> None: ...

class Tag(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
