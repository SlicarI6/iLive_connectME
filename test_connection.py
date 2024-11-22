import psycopg2

try:
    conn = psycopg2.connect("postgres://mouseforce_db_user:pNligaC0yIfhcmdSfVjP0zIz5iyqZst2@dpg-csv0ketumphs739ospl0-a:5432/mouseforce_db")
    print("Conexiune reușită!")
    conn.close()
except Exception as e:
    print(f"Eroare: {e}")