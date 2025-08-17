# API Reference

# `GET /hello`

**Operation ID:** `hello`  

**Summary:** Returns a friendly greeting.

**Description**  
This endpoint returns a simple greeting message. It does not require any request parameters or authentication.

---

## Request

```
GET /hello HTTP/1.1
Host: <your-api-host>
Accept: application/json
```

### Headers

| Name   | Type   | Required | Description                |
|--------|--------|----------|----------------------------|
| Accept | string | No       | Desired response format, e.g., `application/json` |

### Query Parameters

*None*

### Request Body

*None*

---

## Responses

| Code | Description            | Content-Type | Schema |
|------|------------------------|--------------|--------|
| 200  | Successful greeting    | `application/json` | `{ "message": "Hello, World!" }` |
| 400  | Bad request            | `application/json` | `{ "error": "Bad Request" }` |
| 500  | Internal server error  | `application/json` | `{ "error": "Internal Server Error" }` |

---

## Example Curl

```bash
curl -X GET "https://api.example.com/hello" \
     -H "Accept: application/json"
```

**Expected response**

```json
{
  "message": "Hello, World!"
}
```

---

## Swagger (OpenAPI 3.0) Snippet

```yaml
paths:
  /hello:
    get:
      operationId: hello
      summary: Returns a friendly greeting
      description: |
        This endpoint returns a simple greeting message. No parameters or
        authentication are required.
      responses:
        '200':
          description: Successful greeting
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Hello, World!
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
```

---

## `POST /echo` – Echo Service  

**Operation ID:** `echo`  
**Tags:** `Utility`  

### Description
Accepts a JSON payload and returns the same payload unchanged.  
Useful for testing connectivity, request/response formatting, or as a simple health‑check that verifies the request body is received correctly.

---

### Request

| Parameter | Type | In | Required | Description |
|-----------|------|----|----------|-------------|
| body      | object | body | **Yes** | Any valid JSON object. The service will return this exact object in the response. |

**Content-Type:** `application/json`

**Schema (example)**  

```json
{
  "message": "Hello, world!",
  "timestamp": "2025-08-06T12:34:56Z"
}
```

---

### Responses

| Code | Description | Schema |
|------|-------------|--------|
| **200** | Successful echo – the payload you sent is returned verbatim. | Same as request body (any JSON object). |
| **400** | Invalid JSON or malformed request. | `{ "error": "Invalid JSON payload." }` |
| **415** | Unsupported Media Type – only `application/json` is accepted. | `{ "error": "Content-Type must be application/json." }` |

---

### Example cURL

```bash
curl -X POST "https://api.example.com/echo" \
     -H "Content-Type: application/json" \
     -d '{
           "message": "Hello, world!",
           "timestamp": "2025-08-06T12:34:56Z"
         }'
```

**Expected response (200)**

```json
{
  "message": "Hello, world!",
  "timestamp": "2025-08-06T12:34:56Z"
}
```

---  

### Swagger (OpenAPI) Snippet (YAML)

```yaml
paths:
  /echo:
    post:
      operationId: echo
      summary: Echo back the supplied JSON payload
      description: |
        Returns the exact JSON object received in the request body.
      tags:
        - Utility
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              additionalProperties: true   # any JSON object
      responses:
        '200':
          description: Echoed payload
          content:
            application/json:
              schema:
                type: object
                additionalProperties: true
        '400':
          description: Invalid request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
        '415':
          description: Unsupported Media Type
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
```

---

