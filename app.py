from flask import Flask, render_template, jsonify
import random  # Mock data for now, replace with real API later

app = Flask(__name__)

# Mock data for matches
MATCHES = {
    '39': [  # Premier League
        {'home': 'Arsenal', 'away': 'Chelsea', 'score': '2-1', 'time': 'FT'},
        {'home': 'Liverpool', 'away': 'Man City', 'score': '1-1', 'time': '65\''}
    ],
    '140': [  # La Liga
        {'home': 'Real Madrid', 'away': 'Barcelona', 'score': '3-0', 'time': 'FT'}
    ]
}

@app.route('/')
def home():
    """Serve the main HTML page"""
    return render_template('index.html')

@app.route('/api/matches/<league_id>')
def get_matches(league_id):
    """API endpoint for JavaScript to fetch matches"""
    matches = MATCHES.get(league_id, [])
    return jsonify(matches)

if __name__ == '__main__':
    app.run(debug=True)