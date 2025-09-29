from flask import Flask, request, jsonify
import sqlite3
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许跨域请求

def get_db_connection():
    conn = sqlite3.connect('neighborhood.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return "NeighborShare API Server is running!"

# 处理捐赠表单提交
@app.route('/api/donate', methods=['POST'])
def submit_donation():
    try:
        data = request.json
        print("收到捐赠数据:", data)
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # 将选中的物品转换为JSON字符串
        items_json = json.dumps(data.get('items', []))
        
        cursor.execute('''
            INSERT INTO donator (name, email, phone, address, pickup_date, pickup_time, items, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            data['name'],
            data['email'],
            data['phone'],
            data['address'],
            data['pickup_date'],
            data['pickup_time'],
            items_json,
            data.get('notes', '')
        ))
        
        conn.commit()
        donation_id = cursor.lastrowid
        conn.close()
        
        return jsonify({
            'success': True,
            'message': '捐赠信息提交成功！',
            'donation_id': donation_id
        }), 200
        
    except Exception as e:
        print("捐赠提交错误:", str(e))
        return jsonify({
            'success': False,
            'message': f'提交失败: {str(e)}'
        }), 500

# 处理志愿者表单提交
@app.route('/api/volunteer', methods=['POST'])
def submit_volunteer():
    try:
        data = request.json
        print("收到志愿者数据:", data)
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # 将选中的角色转换为JSON字符串
        roles_json = json.dumps(data.get('roles', []))
        
        cursor.execute('''
            INSERT INTO volunteer (name, email, phone, address, availability, frequency, roles, vehicle, experience, background_check, terms_accepted)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            data['name'],
            data['email'],
            data['phone'],
            data['address'],
            data['availability'],
            data['frequency'],
            roles_json,
            data['vehicle'],
            data.get('experience', ''),
            data.get('background_check', False),
            data.get('terms_accepted', False)
        ))
        
        conn.commit()
        volunteer_id = cursor.lastrowid
        conn.close()
        
        return jsonify({
            'success': True,
            'message': '志愿者申请提交成功！',
            'volunteer_id': volunteer_id
        }), 200
        
    except Exception as e:
        print("志愿者提交错误:", str(e))
        return jsonify({
            'success': False,
            'message': f'提交失败: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')