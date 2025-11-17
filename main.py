from flask import Flask
import psycopg2

app = Flask(__name__)

# ==========================
# KONEKSI KE DATABASE
# ==========================
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="mahasiswa",   # ganti
        user="postgres",
        password="Qwerty1357",        # ganti
        port="5432"
    )
    return conn


# ==========================
# ROUTES BIASA
# ==========================
@app.route("/get")
def hello_get():
    return "Hello, orang ganteng (GET)"

@app.route("/post")
def hello_post():
    return "Hello, orang ganteng (POST)"

@app.route("/delete")
def hello_delete():
    return "Hello, orang ganteng (DELETE)"

@app.route("/detail/<nama>")
def hello_detail(nama):
    return f"Halo {nama}, ini halaman detail kamu"


# ==========================
# ROUTE AMBIL DATA DARI DATABASE
# ==========================
@app.route("/getdata")
def get_data():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # GANTI TABEL SESUAI DATABASE LU
        cursor.execute("SELECT * FROM mahasiswa;")
        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        # tampilkan hasilnya sebagai teks
        return str(rows)

    except Exception as e:
        return f"Error: {e}"


# ==========================
# RUN APP
# ==========================
if __name__ == "__main__":
    app.run(debug=True)
