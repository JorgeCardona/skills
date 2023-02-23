from airflow.decorators import dag, task
from datetime import datetime

# https://airflow.apache.org/docs/apache-airflow/stable/concepts/index.html
# https://airflow.apache.org/docs/apache-airflow/1.10.1/scheduler.html
# https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#parsing-processes    
# https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#worker-concurrency
# https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#max-active-runs-per-dag
# https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#max-active-tasks-per-dag
# https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#parallelism


# import the logging module
import logging

# get the airflow.task logger
task_logger = logging.getLogger('airflow.task')

import random

# dags que pasan valores entre tareas
from datetime import timedelta

def mostrar(valor_aleatorio):
    return valor_aleatorio

def triplicar(valores):
    
    return valores*3

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
                "retry_delay": timedelta(minutes=3, ), # datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
                "do_xcom_push":False,
                "do_xcom_pull":False
                }
    )
def ejemplo_rutina_llama_codigo():
    
    valor_aleatorio = random.randint(1, 20_000)
    
    @task(task_id='tarea_extraer_usando_parametro_del_decorador')
    def tarea_extraer(ti=None):
        # guarda el valor de retorno de VALUE=mostrar(valor_aleatorio) en la key DESCARGAR_DATOS
        ti.xcom_push(key='DESCARGAR_DATOS', value=mostrar(valor_aleatorio))
        
        # valor de retorno para la tarea
        return valor_aleatorio


    @task
    def tarea_transformar(ti=None):
        
        # obtiene el valor que la tarea con id task_ids, "tarea_extraer" subio al xcom
        # lee el valor usando la task_ids y la key
        result = ti.xcom_pull(task_ids='tarea_extraer_usando_parametro_del_decorador', key='DESCARGAR_DATOS')
        
        
        ti.xcom_push(key='TRANSFORMAR_DATOS', value=triplicar(result))
        
        return result
 
    @task
    def tarea_carga(ti=None):
        
        result = ti.xcom_pull(task_ids='tarea_transformar', key='TRANSFORMAR_DATOS')
        
        return result
      
    # tiene que llevar los parentesis de cada tarea sino, sale error ---> TypeError: unsupported operand type(s) for >>: '_TaskDecorator' and '_TaskDecorator'
    tarea_extraer() >> tarea_transformar() >> tarea_carga()

ejemplo_rutina_llama_codigo()