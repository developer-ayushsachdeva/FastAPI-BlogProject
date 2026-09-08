# FastAPI Blog API

A RESTful Blog API built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **JWT authentication**.

This project was built as a learning project to understand backend API development, database integration, authentication, and protected API endpoints using FastAPI.

## 🚀 Features

* Create, read, update, and delete blog posts
* PostgreSQL database integration
* SQLAlchemy ORM
* JWT-based authentication
* Protected Create and Update blog endpoints
* Swagger UI for API testing
* Pydantic request/response validation
* Automatic API documentation

## 🛠️ Tech Stack

* **Python**
* **FastAPI**
* **Uvicorn**
* **SQLAlchemy**
* **PostgreSQL**
* **Pydantic**
* **JWT / python-jose**

## 📁 Project Structure

```text
FastAPI-BlogProject/
│
├── main.py          # FastAPI application and API routes
├── model.py         # SQLAlchemy database models
├── Schemas.py       # Pydantic schemas
├── database.py      # Database connection and session
├── auth.py          # JWT authentication
├── requirements.txt # Project dependencies
├── .gitignore       # Ignored files and folders
└── README.md        # Project documentation
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/developer-ayushsachdeva/FastAPI-BlogProject.git
cd FastAPI-BlogProject
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🗄️ Database Setup

This project uses **PostgreSQL**.

Create a PostgreSQL database named:

```text
blogdb
```

Configure your database connection before running the application.

> **Important:** Never commit your PostgreSQL password or JWT secret directly to GitHub. Use environment variables or a `.env` file for sensitive credentials.

## ▶️ Run the Application

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## 📚 API Documentation

FastAPI automatically provides interactive Swagger documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can test the API directly from Swagger UI.

Alternative ReDoc documentation:

```text
http://127.0.0.1:8000/redoc
```

## 🔐 Authentication

The project uses **JWT tokens** to protect certain endpoints.

### Login

```http
POST /login
```

Example request:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

Successful login returns an access token:

```json
{
  "access_token": "your_jwt_token",
  "token_type": "bearer"
}
```

Use this token to access protected endpoints.

In Swagger, click **Authorize** and provide your bearer token.

## 📝 Blog Endpoints

| Method | Endpoint           | Authentication |
| ------ | ------------------ | -------------- |
| GET    | `/`                | ❌              |
| POST   | `/login`           | ❌              |
| POST   | `/blogs`           | ✅              |
| GET    | `/blogs`           | ❌              |
| GET    | `/blogs/{blog_id}` | ❌              |
| PUT    | `/blogs/{blog_id}` | ✅              |
| DELETE | `/blogs/{blog_id}` | ❌              |

### Create Blog

```http
POST /blogs
```

Request:

```json
{
  "title": "My First Blog",
  "body": "This is my first blog post."
}
```

Requires a valid JWT bearer token.

### Get All Blogs

```http
GET /blogs
```

Returns all blog posts.

### Get One Blog

```http
GET /blogs/{blog_id}
```

Example:

```text
GET /blogs/1
```

### Update Blog

```http
PUT /blogs/{blog_id}
```

Example request:

```json
{
  "title": "Updated Blog",
  "body": "Updated blog content."
}
```

Requires authentication.

### Delete Blog

```http
DELETE /blogs/{blog_id}
```

Deletes the specified blog post.

## 🔑 JWT Authentication Flow

The authentication flow works like this:

```text
Client
   │
   │ POST /login
   ▼
FastAPI
   │
   │ Verify username/password
   ▼
JWT Token
   │
   │ Bearer Token
   ▼
Protected Endpoint
   │
   │ Verify JWT
   ▼
Access Granted
```

## 🎯 What I Learned

Through this project, I practiced:

* Building REST APIs with FastAPI
* Creating API routes and dependencies
* Using Pydantic schemas
* Connecting FastAPI with PostgreSQL
* Working with SQLAlchemy ORM
* Creating database models
* Implementing JWT authentication
* Protecting API endpoints
* Using dependency injection with `Depends()`
* Testing APIs with Swagger UI
* Managing a project with Git and GitHub

## 🔮 Future Improvements

Some improvements planned for future versions:

* Password hashing with bcrypt/pwdlib
* User registration endpoint
* User-specific blog ownership
* Protect the delete endpoint
* Better JWT configuration using environment variables
* `.env` configuration
* Database migrations with Alembic
* Pagination for blogs
* Better error handling
* Automated tests with Pytest

## 👨‍💻 Author

**Ayush Sachdeva**

GitHub: [@developer-ayushsachdeva](https://github.com/developer-ayushsachdeva)

---

⭐ If you found this project useful, feel free to star the repository!
