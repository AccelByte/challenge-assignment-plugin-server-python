# Copyright (c) 2024 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

FROM --platform=$BUILDPLATFORM rvolosatovs/protoc:4.1.0 AS protoc
WORKDIR /build
COPY proto proto
COPY src src
RUN protoc  \
    --proto_path=proto/app \
    --grpc-python_out=src \
    --pyi_out=src \
    --python_out=src \
    assignment_function.proto


# Extend App
FROM ubuntu:22.04

RUN apt update && \
    apt install -y python3-pip python-is-python3 && \
    python -m pip install --no-cache-dir --upgrade pip && \
    apt upgrade -y && \
    apt dist-upgrade -y && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
WORKDIR /app
COPY requirements.txt requirements.txt
RUN python -m pip install --no-cache-dir --force-reinstall --requirement requirements.txt
COPY src .
COPY --from=protoc /build/src/assignment_function* .

# Plugin arch gRPC server port
EXPOSE 6565
# Prometheus /metrics web server port
EXPOSE 8080

ENTRYPOINT ["python", "-m", "app"]
