from airflow.decorators import dag, task
from datetime import datetime

# https://airflow.apache.org/docs/apache-airflow/stable/concepts/index.html
# https://airflow.apache.org/docs/apache-airflow/1.10.1/scheduler.html
# https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#parsing-processes    
# https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#worker-concurrency
# https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#max-active-runs-per-dag
# https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#max-active-tasks-per-dag
# https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#parallelism

import random
# dags con el mismo tag
@dag(tags=['Deportes'],
     schedule_interval='0 5 * * *', 
     concurrency=10,  
     max_active_runs=3, 
     start_date=datetime(2021, 1, 1), 
     catchup=False
     )
def ejemplo_rutina_restaurante_con_decorador():
    
    item = random.randint(1, 20)
    servicio = 'Lista de alimentos'
    
    @task()
    def solicitar_lista():
        return f"Por favor me trae la {servicio}"

    @task()
    def seleccionar_pedido():
        return f"Ya se, quiero el {item}"

    @task()
    def realizar_pedido():
        return f"Quisiera el item{item} por favor"

    @task()
    def disfrutar_del_pedido():
        return f"Excelente Seleccion, el item {item} estuvo fabuloso"
    
    solicitar_lista() >> seleccionar_pedido() >> realizar_pedido() >> disfrutar_del_pedido()
    
    solicitar_lista() >> realizar_pedido() >> disfrutar_del_pedido()

# dags que pasan valores entre tareas
from datetime import timedelta
@dag(
    dag_id="test_dag_rutina_deportes",
    description='descripcion del dag creado',
    tags=['Deportes'],
    schedule_interval='@hourly', # https://airflow.apache.org/docs/apache-airflow/1.10.1/scheduler.html#dag-runs
    concurrency=10,  
    max_active_runs=3, 
    start_date=datetime(2000, 1, 1), 
    end_date=datetime(2029, 12, 11), 
    catchup=False,
    default_args={
                "dag_owner": "https://hithub.com/jorgecardona",
                "owner": "Jorge Cardona",  # This defines the value of the "owner" column in the DAG view of the Airflow UI
                "retries": 2,  # If a task fails, it will retry 2 times.
                "retry_delay": timedelta(minutes=3, ) # datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
                }
    )
def ejemplo_rutina_deportes_con_decorador():
    
    item = random.randint(1, 20)
    servicio = 'Lista de Deportes'
    
    @task()
    def deporte_elegido(deporte):
        return f"Voy a iniciar con el deporte, {deporte}"

    @task()
    def seleccionar_pedido():
        return f"Ya se, quiero el {item}"

    @task()
    def resumen():
        pasos = {"Uno": seleccionar_pedido(), "Dos": deporte_elegido(seleccionar_pedido())}
        return f"El resultado del proceso es: {pasos}"
    
    resumen()

ejemplo_rutina_restaurante_con_decorador()
ejemplo_rutina_deportes_con_decorador()


# dags que pasan valores entre tareas y llama codigo python
def mostrar():
    return 'Hola, ud ha sido saludado'


@dag(
    dag_id="test_dag_rutina_llama_codigo",
    description='descripcion del dag creado',
    tags=['Deportes'],
    schedule_interval='@monthly', # https://airflow.apache.org/docs/apache-airflow/1.10.1/scheduler.html#dag-runs
    concurrency=10,  
    max_active_runs=3, 
    start_date=datetime(2000, 1, 1), 
    end_date=datetime(2029, 12, 11), 
    catchup=False,
    default_args={
                "dag_owner": "https://hithub.com/jorgecardona",
                "owner": "Jorge Cardona",  # This defines the value of the "owner" column in the DAG view of the Airflow UI
                "retries": 2,  # If a task fails, it will retry 2 times.
                "retry_delay": timedelta(minutes=3, ) # datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
                }
    )
def ejemplo_rutina_llama_codigo():
    
    item = random.randint(1, 20)
    servicio = 'Lista de Deportes'
    
    @task()
    def tarea_captura_codigo(ti=None):
        ti.xcom_push(key='descargar_datos', value=mostrar())


    @task()
    def resumen(ti=None):
        #pasos = {"Uno": seleccionar_pedido(), "Dos": deporte_elegido(seleccionar_pedido())}
        #return f"El resultado del proceso es: {pasos}"
        
        result = ti.xcom_pull(task_ids='tarea_captura_codigo',key='descargar_datos')
        
        return result*2
    
    tarea_captura_codigo() >> resumen()

ejemplo_rutina_llama_codigo()