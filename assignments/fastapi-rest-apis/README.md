```markdown
# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement a RESTful API using the FastAPI framework. Students will build a small API that exposes CRUD endpoints, uses Pydantic models for validation, and can be run locally with Uvicorn.

## 📝 Tasks

### 🛠️ Implement a Basic REST API

#### Description
Create a FastAPI application that manages a simple resource (for example, `notes` or `tasks`). Implement endpoints to create, read, update, and delete items using in-memory storage (a Python list or dict).

#### Requirements
Completed program should:

- Use FastAPI to define the application and route handlers
- Define request/response models using Pydantic
- Implement CRUD endpoints: `GET /items`, `GET /items/{id}`, `POST /items`, `PUT /items/{id}`, `DELETE /items/{id}`
- Validate incoming data and return appropriate HTTP status codes
- Run with Uvicorn (include run instructions)
- Keep data in-memory (no database required) and make helper functions modular for testing

#### Example run

Start the server and visit docs at `/docs` to interact with the API.

```bash
pip install -r requirements.txt
uvicorn starter_code:app --reload
```

### 🛠️ Optional Enhancements

#### Description
Improve the API with additional features or better developer experience.

#### Requirements

- Add pagination or filtering to `GET /items`
- Persist data to a lightweight file (JSON) between restarts
- Add authentication (token-based) for write endpoints
- Add automated tests using `pytest` and `httpx` or `requests`

---

**Skills practiced:** API design, FastAPI, Pydantic, HTTP status codes, basic testing

Place your solution in `starter_code.py`. Keep functions small and testable.

``` 
