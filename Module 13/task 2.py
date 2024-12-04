from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample Airport Database (in memory for simplicity)
airport_database = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    "EHDP": {"Name": "Dublin Airport", "Location": "Dublin"},
    # Add more airports here...
}

@app.route('/airport/<string:icao_code>', methods=['GET'])
def get_airport_info(icao_code):
    """Get airport information by ICAO code"""
    if icao_code in airport_database:
        return jsonify({"ICAO": icao_code, "Name": airport_database[icao_code]["Name"], "Location": airport_database[icao_code]["Location"]})
    else:
        return jsonify({"Error": f"Airport not found for ICAO code {icao_code}"}), 404

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
