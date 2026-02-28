import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lere.settings")
django.setup()

from oficina.models import Cliente
from decouple import config 
from datetime import datetime
from supabase import create_client, Client
import csv
import io 

SUPABASE_URL = config("SUPABASE_URL")
SUPABASE_SERVICE_KEY = config("SUPABASE_SERVICE_KEY")
BUCKET_NAME = config("BUCKET_NAME")

def export_supabase():
    clientes = Cliente.objects.all().values( 
        "nome", "carro", "placa", "telefone", "servicos", "Data_entrada"
    )
    
    buffer = io.StringIO()
    writer = csv.writer(buffer, delimiter=";")
    writer.writerow(["nome", "carro", "placa", "telefone", "servicos", "Data_entrada"])
    
    for cliente in clientes:  # loop duplicado removido
        writer.writerow([
            cliente["nome"],
            cliente["carro"],
            cliente["placa"],
            cliente["telefone"],
            cliente["servicos"],
            cliente["Data_entrada"].strftime("%Y-%m-%d") if cliente["Data_entrada"] else "",
        ])
            
    csv_bytes = buffer.getvalue().encode("utf-8")
    
    supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    file_name = f"clientes_{timestamp}.csv"
    
    supabase.storage.from_(BUCKET_NAME).upload(
        path=file_name,
        file=csv_bytes,
        file_options={"content-type": "text/csv", "upsert": "true"},
    )
    
    print(f"Arquivo {file_name} exportado com sucesso!")
    return file_name

if __name__ == "__main__":
    export_supabase()
