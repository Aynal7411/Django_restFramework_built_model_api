# API Documentation

This project exposes a Django REST Framework API for working with core Django objects such as users, groups, permissions, sessions, content types, authentication tokens, and admin log entries.

## Base URL

When the development server is running, the API is available at:

- http://127.0.0.1:8000/

Additional useful routes:

- Admin panel: http://127.0.0.1:8000/admin/
- Browsable API login: http://127.0.0.1:8000/api-auth/login/

## Authentication

- The users and groups APIs require authentication.
- The log entries API is read-only and can be accessed for viewing admin activity.
- To access protected endpoints, log in through the browsable API or use basic authentication.

## Currently Exposed Endpoints

The router in the project currently registers the following endpoints:

| Endpoint | Method | Description |
|---|---|---|
| /users/ | GET, POST | List all users or create a new user |
| /users/{id}/ | GET, PUT, PATCH, DELETE | Retrieve, update, or delete a specific user |
| /groups/ | GET, POST | List all groups or create a new group |
| /groups/{id}/ | GET, PUT, PATCH, DELETE | Retrieve, update, or delete a specific group |
| /logentries/ | GET | List admin log entries |
| /logentries/{id}/ | GET | Retrieve a specific log entry |

## Serializer Overview

The project contains serializers for the following Django models:

- UserSerializer
- GroupSerializer
- LogEntrySerializer
- PermissionSerializer
- SessionSerializer
- ContentTypeSerializer
- TokenSerializer

These serializers are defined in the project and can be used for future API expansion. At the moment, only the user, group, and log entry resources are registered as API endpoints.

## 1. Users API

### Endpoint

- /users/
- /users/{id}/

### Description

Manages Django user accounts.

### Supported Fields

Each user response includes:

- url: hyperlink to the user resource
- username: username of the user
- email: user email address
- groups: list of linked group URLs

### Example Response

```json
{
  "url": "http://127.0.0.1:8000/users/1/",
  "username": "admin",
  "email": "admin@example.com",
  "groups": [
    "http://127.0.0.1:8000/groups/1/"
  ]
}
```

### Example Request

```bash
curl -u username:password http://127.0.0.1:8000/users/
```

## 2. Groups API

### Endpoint

- /groups/
- /groups/{id}/

### Description

Manages Django authentication groups.

### Supported Fields

Each group response includes:

- url: hyperlink to the group resource
- name: group name

### Example Response

```json
{
  "url": "http://127.0.0.1:8000/groups/1/",
  "name": "Admins"
}
```

### Example Request

```bash
curl -u username:password http://127.0.0.1:8000/groups/
```

## 3. Log Entries API

### Endpoint

- /logentries/
- /logentries/{id}/

### Description

Returns Django admin activity log entries.

### Supported Fields

Each log entry response includes:

- id: record identifier
- action_time: time of the action
- user: user who performed the action
- content_type: related model name
- object_repr: representation of the affected object
- action: human-readable action status such as Added, Changed, or Deleted
- change_message: change details, if available

### Example Response

```json
{
  "id": 1,
  "action_time": "2026-07-02T10:15:00Z",
  "user": "admin",
  "content_type": "user",
  "object_repr": "admin",
  "action": "Added",
  "change_message": ""
}
```

### Example Request

```bash
curl http://127.0.0.1:8000/logentries/
```

## 4. Additional Serializer Definitions

These serializers are present in the project but are not currently exposed through the main router:

### PermissionSerializer

Fields:

- id
- name
- content_type

### SessionSerializer

Fields:

- session_key
- expire_date
- decoded_data

### ContentTypeSerializer

Fields:

- id
- app_label
- model

### TokenSerializer

Fields:

- key
- user
- created

## Example Workflow

1. Start the server:

```bash
python manage.py runserver
```

2. Open the API in your browser:

```text
http://127.0.0.1:8000/
```

3. Log in through the API authentication page.

4. Use the endpoints to view or manage users, groups, and log entries.

## Notes

- This API is based on Django’s built-in authentication models and Django admin log entries.
- The current implementation is intentionally simple and suitable for basic administration and user management tasks.
- You can extend this project later by registering the additional serializers as new viewsets and endpoints.
