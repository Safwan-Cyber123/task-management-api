# FastAPI Task Management System 🚀

A backend **Task Management System** built with **FastAPI**. It provides user registration, authentication, email notifications, and task management through REST APIs.

## ✨ Features

* 👤 User Registration & Login
* 🔐 JWT-based Authentication
* 📧 Email notification after registration
* 📝 Create, Read, Update & Delete Tasks
* 🗄️ PostgreSQL Database
* 🧪 API Testing with Postman
* 📚 Interactive Swagger UI

## 🛠️ Technologies

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic
* JWT
* FastAPI-Mail
* Uvicorn

## 📂 Project Structure

```text
├── user/
├── task/
├── util/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔐 Authentication

The project uses **JWT authentication** to protect task-related endpoints.

Users can register and log in to receive an access token, which is then used to access protected APIs.

### Authentication Flow

**Register → Email → Login → JWT Token → Task Management**

## 📧 Email

After registration, an email is sent to the user's registered email address using **FastAPI-Mail**.

## 📚 API Testing

The API can be tested using **Postman** or FastAPI's built-in **Swagger UI**.

After running the project, open:

```text
http://127.0.0.1:8000/docs
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Safwan-Cyber123/task-management-api
cd task-managemnt-api
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
uvicorn main:app --reload
```



## 👨‍💻 Author

**Muhammad Safwan**
