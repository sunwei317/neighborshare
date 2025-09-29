# admin.py
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('neighborhood_db.py')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/admin')
def admin_dashboard():
    conn = get_db_connection()
    
    # 获取统计数据
    donators_count = conn.execute('SELECT COUNT(*) FROM donator').fetchone()[0]
    volunteers_count = conn.execute('SELECT COUNT(*) FROM volunteer').fetchone()[0]
    
    # 获取最新记录
    recent_donators = conn.execute('SELECT * FROM donator ORDER BY submission_date DESC LIMIT 5').fetchall()
    recent_volunteers = conn.execute('SELECT * FROM volunteer ORDER BY submission_date DESC LIMIT 5').fetchall()
    
    conn.close()
    
    return render_template('admin.html', 
                         donators_count=donators_count,
                         volunteers_count=volunteers_count,
                         recent_donators=recent_donators,
                         recent_volunteers=recent_volunteers)

if __name__ == '__main__':
    app.run(debug=True, port=5001)