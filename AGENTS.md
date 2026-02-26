# challenge-assignment-plugin-server-python

An Extend Override app for the **challenge assignment function** written in Python. AGS calls this gRPC server to execute custom challenge goal assignment logic instead of the default behavior.

This is a template project — clone it, replace the sample logic in the service implementation, and deploy.

## Build & Test

```bash
make build                           # Build the project
docker compose up --build            # Run locally with Docker
make proto                           # Regenerate proto code
```

## Architecture

AGS invokes this app's gRPC methods instead of its default logic:

```
Game Client → AGS → [gRPC] → This App → Response → AGS
```

The sample implementation randomly selects one goal from the list of active goals and assigns it to the requesting user.

### Key Files

| Path | Purpose |
|---|---|
| `src/accelbyte_grpc_plugin/app.py` | Entry point — starts gRPC server, wires interceptors and observability |
| `src/app/services/challenge_assignment.py` | **Service implementation** — your custom logic goes here |
| `proto/assignment_function.proto` | gRPC service definition (AccelByte-provided, do not modify) |
| `src/accelbyte_grpc_plugin/interceptors/` | Auth interceptor, tracing, logging utilities |
| `docker-compose.yaml` | Local development setup |
| `.env.template` | Environment variable template |

## Rules

See `.agents/rules/` for coding conventions, commit standards, and proto file policies.

## Environment

Copy `.env.template` to `.env` and fill in your credentials.

| Variable | Description |
|---|---|
| `AB_BASE_URL` | AccelByte base URL (e.g. `https://test.accelbyte.io`) |
| `AB_CLIENT_ID` | OAuth client ID |
| `AB_CLIENT_SECRET` | OAuth client secret |
| `AB_NAMESPACE` | Target namespace |
| `PLUGIN_GRPC_SERVER_AUTH_ENABLED` | Enable gRPC auth (`true` by default) |

## Dependencies

- [AccelByte Python SDK](https://github.com/AccelByte/accelbyte-python-sdk) (`accelbyte-py-sdk`) — AGS platform SDK and gRPC plugin utilities
