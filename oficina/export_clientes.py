import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lere.settings")

from decouple import config 
from datetime import datetime
from supabase import create_client
import csv
import io 

SUPABASE_URL = config("SUPABASE_URL")
SUPABASE_SERVICE_KEY = config("SUPABASE_SERVICE_KEY")
BUCKET_NAME = config("BUCKET_NAME")

def export_supabase():
    supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)
    
    # Busca dados pela API REST do Supabase (sem precisar de conexão direta ao banco)
    response = supabase.table("oficina_cliente").select(
        "nome, carro, placa, telefone, servicos, Data_entrada"
    ).execute()
    
    clientes = response.data
    
    buffer = io.StringIO()
    writer = csv.writer(buffer, delimiter=";")
    writer.writerow(["nome", "carro", "placa", "telefone", "servicos", "Data_entrada"])
    
    for cliente in clientes:
        writer.writerow([
            cliente.get("nome", ""),
            cliente.get("carro", ""),
            cliente.get("placa", ""),
            cliente.get("telefone", ""),
            cliente.get("servicos", ""),
            cliente.get("Data_entrada", ""),
        ])
            
    csv_bytes = buffer.getvalue().encode("utf-8")
    
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
