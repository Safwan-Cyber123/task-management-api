#FastAPI Task Management System 🚀

A backend **Task Management System** built with FastAPI. It provides user registration, authentication, email notifications, and task management through REST APIs.

##✨ Features

- 👤 User Registration & Login
- 🔐 JWT-based Authentication
- 📧 Email notification after registration
- 📝 Create, Read, Update & Delete Tasks
- 🗄️ PostgreSQL Database
- 🧪 API Testing with Postman
- 📚 Interactive Swagger UI

##🛠️ Technologies

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- JWT
- FastAPI-Mail
- Uvicorn

##📂 Project Structure

├── user/
├── task/
├── util/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md

##🔐 Authentication

The project uses JWT authentication to protect task-related endpoints.

Users can register and log in to receive an access token, which is then used to access protected APIs.

Register → Email → Login → JWT Token → Task Management

##📧 Email

After registration, an email is sent to the user's registered email address using FastAPI-Mail.

##📚 API Testing

The API can be tested using Postman or FastAPI's built-in Swagger UI.

After running the project, open:

http://127.0.0.1:8000/docs

##⚙️ Installation

git clone <https://github.com/Safwan-Cyber123/task-management-api>
cd task-management-api
pip install -r requirements.txt
uvicorn main:app --reload

Create a ".env" file for your database, JWT, and email configuration.


##👨‍💻 Author
Muhammad Safwan

BS CSIT Student | Backend Development & Cyber Security Enthusiast
