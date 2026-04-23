from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json.get('history', [])
        if not data:
            return jsonify({"error": "قائمة البيانات فارغة"}), 400
        
        avg = sum(data) / len(data)
        # حساب نسبة الفوز (أكبر من أو يساوي 2.0)
        win_count = len([x for x in data if x >= 2.0])
        win_rate = (win_count / len(data)) * 100
        
        return jsonify({
            "average": round(avg, 2),
            "win_rate_2x": f"{round(win_rate, 2)}%",
            "status": "مخاطرة عالية" if avg < 1.8 else "فرصة جيدة"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# السطر ده مهم جداً لـ Vercel
app.debug = True
