from flask import Flask, request, jsonify
from flask_cors import CORS
from Code_tool import codegenerator, codevalidator, is_code_related

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for frontend access

@app.route('/', methods=['GET'])
def home():
    return "✅ Backend is running."

@app.route('/generate_code', methods=['POST'])
def generate_code():
    data = request.get_json()
    user_prompt = data.get('prompt', '').strip()
    
    if not user_prompt:
        return jsonify({"error": "Prompt cannot be empty"}), 400
    
    code = codegenerator.generate_reply(messages=[{"role": "user", "content": user_prompt}])
    
    if not is_code_related(code):
        return jsonify({
            "status": "rejected",
            "message": "This is only a code related tool."
        })
    
    return jsonify({
        "status": "success",
        "code": code,
        "validation_required": True
    })

@app.route('/validate_code', methods=['POST'])
def validate_code():
    data = request.get_json()
    code = data.get('code', '').strip()
    
    if not code:
        return jsonify({"error": "Code cannot be empty"}), 400
    
    validation = codevalidator.generate_reply(messages=[{"role": "user", "content": code}]).strip()
    
    if validation.lower() == "no errors found.":
        return jsonify({
            "status": "valid",
            "message": validation,
            "code": code
        })
    else:
        return jsonify({
            "status": "invalid",
            "errors": validation,
            "code": code
        })

@app.route('/fix_code', methods=['POST'])
def fix_code():
    data = request.get_json()
    code = data.get('code', '').strip()
    errors = data.get('errors', '').strip()
    
    if not code or not errors:
        return jsonify({"error": "Both code and errors are required"}), 400
    
    fix_prompt = (
        f"The following errors were found in your code:\n{errors}\n"
        "Please fix these errors and return only the corrected code."
    )
    
    fixed_code = codegenerator.generate_reply(messages=[{"role": "user", "content": fix_prompt}])
    
    return jsonify({
        "status": "fixed",
        "code": fixed_code
    })

@app.before_request
def log_request():
    print(f"\n📥 Incoming request: {request.method} {request.url}")
    print(f"Headers: {dict(request.headers)}")
    print(f"Body: {request.get_data()}")

if __name__ == '__main__':
    app.run(debug=True)
