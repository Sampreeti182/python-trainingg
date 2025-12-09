from flask import Flask, request, jsonify
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Chillichicken@1802',
    database='employees'
)

cursor = conn.cursor()

app = Flask(__name__)


@app.route("/employee", methods=["GET"])
def get_employee():
    sql = "SELECT * FROM employee"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return jsonify(rows)


@app.route("/employee-add", methods=["POST"])
def add_item():
    data = request.get_json()
    emp_id = data.get("emp_id")
    emp_name = data.get("emp_name")
    salary = data.get("salary")

    if not emp_id or not emp_name or not salary:
        return jsonify({"error": "emp_id, name, and salary are required"}), 400

    sql = "INSERT INTO employee (emp_id, name, salary) VALUES (%s, %s, %s)"
    cursor.execute(sql, (emp_id, emp_name, salary))
    conn.commit()
    return "Employee added successfully"


@app.route("/employee-del/<int:index>", methods=["DELETE"])
def delete_by_index(index):
    try:
        sql = "DELETE FROM employee WHERE empid=%s"
        cursor.execute(sql, (index,))
        conn.commit()
        return "Employee deleted successfully"
    except:
        return jsonify({"error": "Invalid index"}), 400


@app.route("/employee-put/<int:emp_id>", methods=["PUT"])
def put_item(empid):
    try:
        data = request.get_json()
        emp_name = data.get("emp_name")
        salary = data.get("salary")

        if not emp_name or not salary:
            return jsonify({"error": "name, and salary are required"}), 400

        sql = "UPDATE employee SET name=%s, salary=%s WHERE empid=%s"
        cursor.execute(sql, (emp_name, salary, empid))

        conn.commit()

        return "Employee updated successfully"
    except Exception as e:
        return jsonify({"error": str(e)}), 400