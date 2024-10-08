# Copyright (c) 2024 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

import json
import random

from logging import Logger
from typing import Any, Optional

from google.protobuf.json_format import MessageToDict
from grpc import ServicerContext, StatusCode

from assignment_function_pb2 import (
    DESCRIPTOR,
    AssignmentRequest,
    AssignmentResponse,
)
from assignment_function_pb2_grpc import AssignmentFunctionServicer


class AsyncChallengeAssignmentService(AssignmentFunctionServicer):
    full_name: str = DESCRIPTOR.services_by_name["AssignmentFunction"].full_name

    def __init__(self, logger: Optional[Logger] = None) -> None:
        self.logger = logger

    async def Assign(
            self, request: AssignmentRequest, context: ServicerContext
    ) -> AssignmentResponse:
        self.log_payload(f"{self.Assign.__name__} request: %s", request)

        response = AssignmentResponse()

        if len(request.goals) == 0:
            code: StatusCode = StatusCode.INVALID_ARGUMENT
            details: str = "No active goals is available to be assigned."
            await context.abort(code=code, details=details)

        response.namespace = request.namespace
        response.userId = request.userId

        random_index = random.randint(0, len(request.goals) - 1)
        goal = request.goals[random_index]

        response.assignedGoals.append(goal)

        self.log_payload(f"{self.Assign.__name__} response: %s", response)

        return response

    # noinspection PyShadowingBuiltins
    def log_payload(self, format: str, payload: Any) -> None:
        if not self.logger:
            return

        payload_dict = MessageToDict(payload, preserving_proto_field_name=True)
        payload_json = json.dumps(payload_dict)

        self.logger.info(format % payload_json)