def hardcodedCredentialsExample():
    # 비밀번호를 코드에 하드코딩: 보안 취약점
    password = "my_secret_password"
    print(f"Password: {password}")  # 비밀번호가 출력되어 노출됨

hardcodedCredentialsExample()

import sqlite3

def sqlInjectionExample():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER, username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users (id, username, password) VALUES (1, 'user1', 'pass')")
    
    # 사용자 입력을 직접 SQL 쿼리에 삽입: SQL 인젝션 공격이 가능함
    username = "user1' OR '1'='1"
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    print(cursor.fetchall())

sqlInjectionExample()
