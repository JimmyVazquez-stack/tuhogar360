import os
import csv
import django

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hogar360.settings')  # Reemplaza 'tu_proyecto' con el nombre de tu proyecto
django.setup()

from catalogo.models import Sepomex  # Importa tu modelo después de configurar Django


def load_data_from_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='|')
        next(reader)  # Saltar la primera fila si contiene encabezados
        
        for row in reader:
            d_codigo, d_asenta, d_tipo_asenta, D_mnpio, d_estado, d_ciudad, d_CP, c_estado, c_oficina, c_CP, c_tipo_asenta, c_mnpio, id_asenta_cpcons, d_zona, c_cve_ciudad = row

            Sepomex.objects.create(
                d_codigo=d_codigo,
                d_asenta=d_asenta,
                d_tipo_asenta=d_tipo_asenta,
                D_mnpio=D_mnpio,
                d_estado=d_estado,
                d_ciudad=d_ciudad,
                d_CP=d_CP,
                c_estado=c_estado,
                c_oficina=c_oficina,
                c_CP=c_CP,
                c_tipo_asenta=c_tipo_asenta,
                c_mnpio=c_mnpio,
                id_asenta_cpcons=id_asenta_cpcons,
                d_zona=d_zona,
                c_cve_ciudad=c_cve_ciudad
            )

if __name__ == "__main__":
    file_path = 'sepomex_db.csv'  # Reemplaza con la ruta a tu archivo CSV
    load_data_from_csv(file_path)
