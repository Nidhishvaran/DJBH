import pymysql
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes in the app

@app.route('/login.py', methods=['POST'])
def handle_login():
    try:
        data = request.json
        djnumber = int(data["djnumber"])  # Convert to integer
        password = data["password"]

        host = 'sql12.freesqldatabase.com'
        user = 'sql12706927'
        db_password = 'nWzRF94cyw'
        database = 'sql12706927'

        connection = pymysql.connect(
            host=host,
            user=user,
            password=db_password,
            database=database
        )
        cursor = connection.cursor()
        

        # Use parameterized query to avoid SQL injection
        # query = ("SELECT * FROM register WHERE DJNO=%d AND PASSWORD=%s")
        # cursor.execute(query, (djnumber, password))
        # Assuming you're using pymysql library
        cursor.execute("SELECT * FROM register WHERE DJNO=%s AND PASSWORD=%s", (djnumber, password))

        result = cursor.fetchone()

        cursor.close()
        connection.close()

        if result:
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"message": "Invalid DJ number or password"}), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
