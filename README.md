💡Code-Validator
A smart, interactive web & mobile app that lets users generate, validate, and fix programming code using AI-powered agents. 
Built with Flutter (frontend) and Flask (backend), this tool streamlines the process of writing error-free code in a developer-friendly interface.

📌 Features
🔠 Code Generator: Generate clean code based on user prompts using LLMs.

🧪 Code Validator: Detect syntax/logical issues and report detailed errors.

🔧 Fix Code: Automatically repair buggy code using AI.

✅ Real-time Code Checker in Flutter UI with feedback.


🛠️ Tech Stack
Layer	     Tech
Frontend	Flutter
Backend	    Flask + Python
AI Engine	Autogen based LLM agents
API	        REST(JSON-based POST requests)
Hosting	     Localhost / Render / Railway

📁 Project Structure

📦 AI-Powered-Code-Assistant
├── frontend_flutter/
│   └── lib/
│       └── main.dart (code validation UI)
├── backend_flask/
│   ├── app.py
│   ├── Code_tool.py
│   ├── config.json
│   └── requirements.txt
├── README.md

🚀 Getting Started
1️⃣ Backend Setup (Flask + AI Agents)
✅ Prerequisites
Python 3.8+

pip install -r requirements.txt

A config.json file with your LLM API credentials

🔧 Run Flask Server
cd backend_flask
python app.py
Server runs at: http://127.0.0.1:5000


📡 Available API Routes
Method	Route	         Description
POST	/generate_code	Generate code from prompt
POST	/validate_code	Validate code for errors
POST	/fix_code	    Fix broken code


2️⃣ Frontend Setup (Flutter)
✅ Prerequisites
Flutter SDK installed

Android Studio or VS Code
🛠️ Run Flutter App
cd frontend_flutter
flutter pub get
flutter run


🧠 Agent Logic
Codegenerator: LLM agent generating code from prompt.

Codevalidator: Validates syntax & semantics.

is_code_related(): Filters non-programming inputs.




















2️⃣ Frontend Setup (Flutter)
✅ Prerequisites
Flutter SDK installed

Android Studio or VS Code
