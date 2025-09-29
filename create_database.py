import sqlite3
import os

def create_database():
    # 删除已存在的数据库文件（如果存在）
    if os.path.exists('neighborhood.db'):
        os.remove('neighborhood.db')
    
    # 连接数据库（如果不存在会自动创建）
    conn = sqlite3.connect('neighborhood.db')
    cursor = conn.cursor()
    
    # 创建donator表
    cursor.execute('''
        CREATE TABLE donator (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            address TEXT NOT NULL,
            pickup_date TEXT NOT NULL,
            pickup_time TEXT NOT NULL,
            items TEXT NOT NULL,
            notes TEXT,
            submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # 创建volunteer表
    cursor.execute('''
        CREATE TABLE volunteer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            address TEXT NOT NULL,
            availability TEXT NOT NULL,
            frequency TEXT NOT NULL,
            roles TEXT NOT NULL,
            vehicle TEXT NOT NULL,
            experience TEXT,
            background_check BOOLEAN NOT NULL,
            terms_accepted BOOLEAN NOT NULL,
            submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # 提交更改并关闭连接
    conn.commit()
    conn.close()
    print("数据库创建成功！表 'donator' 和 'volunteer' 已创建。")

if __name__ == "__main__":
    create_database()