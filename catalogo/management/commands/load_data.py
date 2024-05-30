from django.core.management.base import BaseCommand
from catalogo.models import Sepomex  # Importa tu modelo
import csv

class Command(BaseCommand):
    help = 'Carga datos desde un archivo CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Ruta al archivo CSV')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='|')
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

        self.stdout.write(self.style.SUCCESS('Datos cargados exitosamente'))