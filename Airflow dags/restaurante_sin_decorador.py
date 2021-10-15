from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
        
def conocer_menu():
    return "Por favor me trae la Carta"

def seleccionar_plato(x: int):
    return "Ya se que quiero comer"
    
def realizar_pedido():
    return "Quisiera pollo al curry por favor"
    
def disfrutar_los_alimentos():
    return "Excelente Cena"
    
dag = DAG('ejemplo_rutina_restaurante_sin_decorador', description='restaurante_sin_decorador DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime(2017, 3, 20), catchup=False)

paso_uno = PythonOperator(task_id='conocer_menu', python_callable=conocer_menu, dag=dag)
paso_dos = PythonOperator(task_id='seleccionar_plato', python_callable=seleccionar_plato, dag=dag)
paso_tres = PythonOperator(task_id='realizar_pedido', python_callable=realizar_pedido, dag=dag)
paso_cuatro = PythonOperator(task_id='disfrutar_los_alimentos', python_callable=disfrutar_los_alimentos, dag=dag)


paso_uno >> paso_dos >> paso_tres >> paso_cuatro
