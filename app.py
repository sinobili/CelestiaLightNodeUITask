from flask import Flask, request
import json
import random
import subprocess

app = Flask(__name__)

# Render a form for the user to input the seed value
@app.route('/')
def index():
    return '''
        <h2>Submit Pay for Blob Transaction</h2>
        <form method="POST" action="/submit">
            <label for="seed">Enter a seed value:</label>
            <input type="text" id="seed" name="seed"><br>
            <br><br>
            <button type="submit">Submit Transaction</button>
        </form>
    '''

# Handle the submission of the form data
@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve the seed value from the submitted form data
    seed = request.form.get('seed')
    
    # Generate the namespace ID and data using the Go code
    namespace_id = subprocess.check_output(['go', 'run', 'generate_pfb.go', seed]).strip().decode()
    data = subprocess.check_output(['go', 'run', 'generate_pfb.go', seed]).strip().decode()
    
    # Create a JSON payload with the namespace ID, data, gas limit, and fee
    payload = {
        'namespace_id': namespace_id,
        'data': data,
        'gas_limit': 80000,
        'fee': 2000
    }
    
    # Send a POST request to the Celestia testnet using the curl command
    try:
        output = subprocess.check_output(['curl', '-X', 'POST', '-d', json.dumps(payload), 'http://localhost:26659/submit_pfb']).strip().decode()
        return f'Transaction submitted successfully!<br><br>{output}'
    except subprocess.CalledProcessError as e:
        return f'Transaction failed to submit:<br><br>{e}'