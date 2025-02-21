# Flask-PHP-Calculator-A-Web-Based-Arithmetic-Solver

🛠 Technologies Used
Frontend: PHP, HTML, cURL
Backend: Python, Flask
Communication: cURL (PHP -> Flask API)
⚙️ Setup & Installation
1️⃣ Install Flask (Python)
bash
Copy
Edit
pip install flask
2️⃣ Start the Flask Server
bash
Copy
Edit
cd py-server
python main_server.py
The Flask server will run at http://127.0.0.1:5000.
3️⃣ Start the PHP Server
bash
Copy
Edit
cd web-client
php -S 127.0.0.1:8000
Open http://127.0.0.1:8000/calc.php in your browser.
🖥️ How It Works
User Inputs: Two numbers and selects an arithmetic operation in the PHP web form.
PHP to Flask: PHP sends the data to Flask via cURL.
Flask Processing: Flask receives the request, performs the operation, and returns the result.
Result Display: The PHP page displays the result.
📝 Example API Request (Using cURL in Terminal)
bash
Copy
Edit
curl -X POST "http://127.0.0.1:5000/calculate" -H "Content-Type: application/json" -d '{"num1": 5, "num2": 3, "operation": "add"}'
Expected Response:
json
Copy
Edit
{"result": 8}
💡 Features
✔ Supports Addition, Subtraction, Multiplication, Division
✔ Handles division by zero error
✔ Uses Flask API for calculations
✔ PHP frontend communicates with Flask using cURL

🔧 Future Improvements
Add error handling for invalid inputs
Implement a better UI with CSS
Extend with more mathematical operations (e.g., square root, power, modulus)





Project Structure

calc-app/

├── py-server/

│   ├── main_server.py

│   ├── math_ops/

│   │   ├── __init__.py

│   │   ├── add.py

│   │   ├── sub.py

│   │   ├── mul.py

│   │   └── div.py

│   └── setup_env.py

└── web-client/

    ├── calc.php
    
    ├── client.py
