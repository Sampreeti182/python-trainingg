from flask import Flask,request,jsonify
app = Flask(__name__)
employees=[
    {"id":1,"name":"Sampreeti","role":"developer"},
    {"id":2,"name":"Tania","role":"developer"},
    {"id":3,"name":"John","role":"Designer"}
]
@app.route("/employees",methods=["GET"])
def get_employees():
    return jsonify(employees)


@app.route('/employees/<int:emp_id>', methods=['GET'])
def get_employee(emp_id):
    for emp in employees:
        if emp["id"] == emp_id:
            return jsonify(emp), 200
    return jsonify({"message": "Employee not found"}), 404


# POST - Add a new employee
@app.route('/employees', methods=['POST'])
def add_employee():
    new_emp = request.get_json()
    employees.append(new_emp)
    return jsonify({"message": "Employee added", "employee": new_emp}), 201

@app.route('/employees/<int:emp_id>', methods=['PUT'])
def update_employee(emp_id):
    updated_data = request.get_json()
    for emp in employees:
        if emp["id"] == emp_id:
            emp["name"] = updated_data.get("name", emp["name"])
            emp["role"] = updated_data.get("role", emp["role"])
            return jsonify({"message": "Employee updated", "employee": emp}), 200
    return jsonify({"message": "Employee not found"}), 404

@app.route('/employees/<int:emp_id>', methods=['DELETE'])
def delete_employee(emp_id):
    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            return jsonify({"message": "Employee deleted"}), 200
    return jsonify({"message": "Employee not found"}), 404


if __name__ == '__main__':
    app.run()