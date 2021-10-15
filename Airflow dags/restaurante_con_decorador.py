from airflow.decorators import dag, task
from datetime import datetime


@dag(schedule_interval=None, start_date=datetime(2021, 1, 1), catchup=False, tags=['Almuerzo'])
def ejemplo_rutina_restaurante_con_decorador():

    @task()
    def conocer_menu():
        return "Por favor me trae la Carta"

    @task()
    def seleccionar_plato():
        return "Ya se que quiero comer"

    @task()
    def realizar_pedido():
        return "Quisiera pollo al curry por favor"

    @task()
    def disfrutar_los_alimentos():
        return "Excelente Cena"
    
    conocer_menu() >> seleccionar_plato() >> realizar_pedido() >> disfrutar_los_alimentos()
    
    conocer_menu() >> realizar_pedido() >> disfrutar_los_alimentos()

dag = ejemplo_rutina_restaurante_con_decorador()
