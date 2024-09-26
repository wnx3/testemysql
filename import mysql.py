import mysql.connector
import time

# Conexão com o banco de dados
conn = mysql.connector.connect(
    host='creator.mysql.uhserver.com',
    user='wnx3',
    password='@Rumo100k',
    database='creator'
)
cursor = conn.cursor()

def check_heartbeat():
    cursor.execute("""
        UPDATE controle_bot
        SET status = 'parado'
        WHERE id = 1 AND TIMESTAMPDIFF(SECOND, last_heartbeat, NOW()) > 15
    """)
    conn.commit()

while True:
    check_heartbeat()  # Verifica o status periodicamente
    time.sleep(15)  # Espera 15 segundos antes de verificar novamente
