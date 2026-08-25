import os
import json
import boto3
import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)


def get_db_connection():
    client = boto3.client(
        "secretsmanager",
        region_name=os.getenv("AWS_REGION", "ap-south-1")
    )

    response = client.get_secret_value(
        SecretId=os.getenv("AWS_SECRET_NAME", "devops/rds/postgres")
    )

    secret = json.loads(response["SecretString"])

    return psycopg2.connect(
        host=secret["host"],
        database=secret["database"],
        user=secret["username"],
        password=secret["password"],
        port=int(secret["port"])
    )


@app.route("/")
def home():
    return "Version 2 deployed using CI/CD!"


@app.route("/health")
def health():
    return "Healthy"


@app.route("/employees", methods=["GET"])
def get_employees():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, name, email, role FROM employees ORDER BY id"
    )

    employees = cur.fetchall()

    cur.close()
    conn.close()

    result = []

    for employee in employees:
        result.append({
            "id": employee[0],
            "name": employee[1],
            "email": employee[2],
            "role": employee[3]
        })

    return jsonify(result)


@app.route("/employees", methods=["POST"])
def create_employee():
    data = request.get_json()

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO employees (name, email, role)
        VALUES (%s, %s, %s)
        RETURNING id
        """,
        (data["name"], data["email"], data["role"])
    )

    employee_id = cur.fetchone()[0]

    conn.commit()

    cur.close()
    conn.close()

    return jsonify({
        "message": "Employee created",
        "id": employee_id
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
