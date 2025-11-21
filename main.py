# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from anthropic import Anthropic
import os
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Allow requests from your website

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Simple counter file (in production, use a database)
COUNTER_FILE = 'rejection_counter.json'

def get_counter():
    try:
        with open(COUNTER_FILE, 'r') as f:
            data = json.load(f)
            return data.get('count', 0)
    except FileNotFoundError:
        return 0

def increment_counter():
    count = get_counter() + 1
    with open(COUNTER_FILE, 'w') as f:
        json.dump({'count': count, 'last_updated': datetime.now().isoformat()}, f)
    return count

@app.route('/api/counter', methods=['GET'])
def counter():
    """Get current rejection count"""
    return jsonify({'count': get_counter()})

@app.route('/api/generate', methods=['POST'])
def generate_rejection():
    """Generate rejection letter"""
    try:
        data = request.json
        company = data.get('company', 'TechCorp')
        role = data.get('role', 'Product Manager')
        email = data.get('email', None)
        
        # Increment counter
        new_count = increment_counter()
        
        # Generate rejection letter
        prompt = f"""Generate a satirical rejection letter from {company} for the role of {role}.

Make it:
- Absurdly corporate with buzzwords, OR brutally honest, OR overly emotional
- Clever and funny but not mean-spirited
- Around 150-200 words
- Include a formal sign-off

Pick whichever style feels most appropriate for {company}."""

        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        rejection_text = message.content[0].text
        
        # If email provided, send it (you'll need to add email sending)
        # For now, we'll just return it
        
        return jsonify({
            'success': True,
            'rejection_letter': rejection_text,
            'count': new_count,
            'company': company,
            'role': role
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

