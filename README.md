# Flask-PHP-Calculator-A-Web-Based-Arithmetic-Solver

🛠 Technologies Used

Frontend: PHP, HTML, cURL

Backend: Python, Flask

Communication: cURL (PHP -> Flask API)

⚙️ Setup & Installation

1️⃣ Install Flask (Python)

pip install flask

2️⃣ Start the Flask Server


cd py-server

python main_server.py

The Flask server will run at http://127.0.0.1:5000.
3️⃣ Start the PHP Server

php -S 127.0.0.1:8000
Open http://127.0.0.1:8000/calc.php in your browser.





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
