# Flask REST API – User Management

This is a simple REST API built using Python and Flask. It allows you to manage user data with basic CRUD operations using in-memory storage (a dictionary).

---

## 🚀 Features

- `GET /users` – Retrieve all users  
- `GET /users/<user_id>` – Retrieve a specific user  
- `POST /users` – Add a new user  
- `PUT /users/<user_id>` – Update an existing user  
- `DELETE /users/<user_id>` – Delete a user

---

## 🛠️ Tools Used

- Python
- Flask
- VS Code
- Postman / curl (for testing)

---

## 📦 Installation

1. **Clone the repository** (or download the files)
2. **Navigate to the project folder**

```bash
cd flask_api_project
3. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
4. Install dependencies
pip install flask
▶️ Running the App
python app.py
Visit http://127.0.0.1:5000 in your browser or test using Postman/curl.
.

🧪 Sample API Calls
1. Get all users

bash
Copy
Edit
GET http://localhost:5000/users
2. Add a user

bash
Copy
Edit
POST http://localhost:5000/users
Content-Type: application/json

{
  "name": "Charlie",
  "email": "charlie@example.com"
}
3. Update a user

bash
Copy
Edit
PUT http://localhost:5000/users/1
Content-Type: application/json

{
  "email": "newemail@example.com"
}
4. Delete a user

bash
Copy
Edit
DELETE http://localhost:5000/users/2
📂 Project Structure
bash
Copy
Edit
flask_api_project/
│
├── app.py          # Main Flask app
├── venv/           # Virtual environment
└── README.md       # Project documentation
📌 Notes
This API uses in-memory storage (dictionary), which means data is lost on restart.

Ideal for learning and small prototypes.


