# ByteBlog

ByteBlog is a secure RESTful blogging API built with FastAPI.
It provides backend services for managing users and journals with authentication and protected routes.

The project emphasizes clean architecture, JWT-based authentication, modular code structure, and API documentation using Swagger (OpenAPI).

# 🚀 Features

User Registration & Login

JWT-based Authentication

Password Hashing

Protected Routes

Journal CRUD Operations

User-specific journal access

Input validation using Pydantic

Interactive Swagger API documentation

Clean modular architecture

# 🛠 Tech Stack

Framework: FastAPI

ORM: SQLAlchemy

Database: SQLite

Authentication: JWT (JSON Web Tokens)

API Documentation: Swagger (OpenAPI)

Language: Python

# 📌 API Documentation

The API is fully documented using Swagger UI.

After running the server:

http://127.0.0.1:8000/docs
Swagger API Preview:

<img width="1226" height="681" alt="Screenshot 2026-02-22 at 2 36 22 AM" src="https://github.com/user-attachments/assets/93c788f6-b454-4bc2-b19d-4b60c0335fc3" />

# ▶️ How to Run the Project

Clone the repository

Create a virtual environment

Install dependencies

pip install -r requirements.txt

Run the server

uvicorn main:app --reload

# 🎯 Project Objective

This project was built to strengthen:

RESTful API design

Authentication & Authorization mechanisms

Secure password handling

Database relationships

Clean and maintainable backend architecture
