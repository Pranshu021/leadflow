# 🚀 LeadFlow

LeadFlow is a **Python FastAPI application** that demonstrates how to integrate **AI with traditional applications using the Model Context Protocol (MCP)**.

The project exposes REST APIs through FastAPI while simultaneously providing an MCP server that AI assistants such as Claude Desktop or Claude Code can connect to. This allows an LLM to interact with your application's business logic without requiring custom integrations.

The application uses **SQLite** as its database and includes scripts to generate mock data and seed the database for quick local development.

---

## ✨ Features

- ⚡ FastAPI REST API
- 🤖 Local MCP Server with FastMCP Framework
- 🗄️ SQLite Database
- 🌱 Database Seeding
- 📊 Mock Data Generation
- 📂 Modular Project Structure
- 🔌 Ready for AI Integration

---

## 📁 Project Structure

```
backend/
│
├── routers/                  # API Routes
├── services/                 # Business Logic
│
├── database.py               # Database Connection
├── models.py                 # Database Models
├── main.py                   # FastAPI Application
├── mcp_server.py             # MCP Server
├── seed.py                   # Database Seeder
├── mock_data_generation.py   # Mock Data Generator
│
├── requirements.txt
└── app.db (generated locally)
```

---

# 🛠️ Prerequisites

- Python 3.11+
- pip
- Git

---

# 📥 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/leadflow.git

cd leadflow/backend
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Generate the Database

If you're starting from scratch, generate the SQLite database:

```bash
cd src
python seed.py
```

If you wish to populate it with additional demo data:

```bash
python mock_data_generation.py
```

---

# ▶️ Running the FastAPI Server

```bash
uvicorn main:app --reload
```

FastAPI will be available at:

```
http://localhost:8000
```

Interactive API documentation:

```
http://localhost:8000/docs
```

---

# 🤖 Testing the MCP Server file

You can test the local MCP server:

```bash
python mcp_server.py
```

If no errors and server runs successfully, You can configure and connect the server to MCP-compatible AI clients such as:

- Claude Desktop
- Claude Code
- Other MCP-enabled AI applications

---

# 📡 API Endpoints

The application exposes REST APIs through FastAPI.

Example:

```
GET /...
POST /...
```

Refer to the Swagger documentation at:

```
http://localhost:8000/docs
```

for the complete list of available endpoints.

---

# 💻 Technologies Used

- Python
- FastAPI
- MCP (Model Context Protocol)
- SQLite
- Pydantic
- Uvicorn

---

# 🧠 What is MCP?

The **Model Context Protocol (MCP)** is an open protocol that enables AI models to securely interact with external applications, tools, and data sources.

Instead of hardcoding integrations for every AI application, MCP provides a standardized interface that allows AI assistants to invoke tools, retrieve information, and execute business logic from your application.

LeadFlow demonstrates how a traditional backend application can expose its functionality through MCP, making it instantly usable by AI-powered clients.

---

# 📌 Notes

The SQLite database (`app.db`) is intentionally **excluded** from version control.

Generate it locally using:

```bash
python seed.py
```

---

# 🤝 Contributing

Contributions, improvements, and suggestions are always welcome!

Feel free to fork the repository, submit issues, or open pull requests.

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!

It helps others discover the project and supports future development.