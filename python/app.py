from flask import Flask, request, jsonify
from supabase import create_client, Client
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Supabase setup
url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_KEY')
supabase: Client = create_client(url, key)

@app.route('/')
def index():
    return "Welcome to the Flask API!"

@app.route('/data', methods=['GET'])
def get_data():
    try:
        data = supabase.table('your_table_name').select('*').execute()
        if data.error:
            raise Exception(data.error.message)
        return jsonify(data.data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)