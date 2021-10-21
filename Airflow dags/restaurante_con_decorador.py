from airflow.decorators import dag, task
from datetime import datetime

# https://airflow.apache.org/docs/apache-airflow/stable/concepts/index.html
# https://airflow.apache.org/docs/apache-airflow/1.10.1/scheduler.html
# https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#parsing-processes    
# https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#worker-concurrency
# https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#max-active-runs-per-dag
# https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#max-active-tasks-per-dag
# https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#parallelism
@dag(schedule_interval='0 5 * * *', concurrency=10,  max_active_runs=3, start_date=datetime(2021, 1, 1), catchup=False, tags=['Almuerzo'])
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
