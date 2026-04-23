from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json.get('history', [])
    if not data:
        return jsonify({"message": "بيانات فارغة"}), 400
    
    avg = sum(data) / len(data)
    # احتمال الفوز عند هدف 2.0
    win_rate = (len([x for x in data if x >= 2.0]) / len(data)) * 100
    
    return jsonify({
        "average": round(avg, 2),
        "win_rate_2x": f"{round(win_rate, 2)}%",
        "status": "مخاطرة عالية" if avg < 1.8 else "فرصة جيدة"
    })
  
