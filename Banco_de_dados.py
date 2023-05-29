import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()


class Banco:
    try:
        url = os.getenv("DATABASE_URL")
        connection = psycopg2.connect(url)
    except Exception as e:
        print(f"Erro ao conectar ao banco: {e}")

    def get_lista_de_plantas(self):
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id,plant_id,temperature,humidity,light,ph,last_time_watered FROM plant_info")
                dados = cursor.fetchall()
        lista_processada = {}
        index = 0
        for dado in dados:
            item = {"id": dado[0],
                    "plant_id": int(dado[1]),
                    "temperatura": float(dado[2]),
                    "humidadade": float(dado[3]),
                    "luz": float(dado[4]),
                    "ph": float(dado[5]),
                    "ultima_vez_regada": dado[6]}
            lista_processada.update({index: item})
            index += 1
        return lista_processada


banco = Banco()
print(banco.get_lista_de_plantas())