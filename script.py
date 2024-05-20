import pymysql
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes in the app

@app.route('/login', methods=['POST'])
def handle_login():
    try:
        data = request.json
        djnumber = int(data["djnumber"])
        password = data["password"]

        connection = pymysql.connect(
            host='sql12.freesqldatabase.com',
            user='sql12706927',
            password='nWzRF94cyw',
            database='sql12706927'
        )
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM register WHERE DJNO=%s AND PASSWORD=%s", (djnumber, password))
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        if result:
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"message": "Invalid DJ number or password"}), 401

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/script_', methods=['POST'])
def handle_script():
    try:
        data = request.json
        djnumber = data["key1"]
        date = data["key2"]
        intime = data.get("key3")
        outtime = data.get("key4")
        location = data["key5"]

        connection = pymysql.connect(
            host='sql12.freesqldatabase.com',
            user='sql12706927',
            password='nWzRF94cyw',
            database='sql12706927'
        )
        cursor = connection.cursor()

        cursor.execute("INSERT INTO attn (DJNO, DATE1, INTIME, OUTTIME, LOCATION) VALUES (%s, %s, %s, %s, %s)",
                       (djnumber, date, intime, outtime, location))
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({"message": "Data inserted successfully"}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
