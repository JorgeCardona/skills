from airflow.decorators import dag, task
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import random


def get_number():
    
    return random.randint(1, 1_000_000)

def get_duplicate_number(number):
    
    return number * 2

def get_len(number):
    return len(str(number))
    
@dag(
    dag_id="pasa_resultado_de_funcion_como_parametro",
    description='descripcion del dag creado',
    tags=['FUNCION_COMO_PARAMETRO'],
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
    def tarea_numero(ti=None):
        # guarda el valor de retorno de VALUE=mostrar(valor_aleatorio) en la key DESCARGAR_DATOS
        ti.xcom_push(key='OBTENER_NUMERO', value=get_number())
        
        # valor de retorno para la tarea
        return valor_aleatorio

    @task
    def tarea_duplicar(ti=None):
        
        # obtiene el valor que la tarea con id task_ids, "tarea_extraer" subio al xcom
        # lee el valor usando la task_ids y la key
        result = ti.xcom_pull(task_ids='tarea_extraer_usando_parametro_del_decorador', key='OBTENER_NUMERO')
        
        if result %2 ==0:
            result = 13
              
        ti.xcom_push(key='DUPLICAR_NUMERO', value=get_duplicate_number(result))
        
        return result
 
    @task
    def tarea_size(ti=None):
        
        result = ti.xcom_pull(task_ids='tarea_duplicar', key='DUPLICAR_NUMERO')
        
        return get_len(result)
    
    # tiene que llevar los parentesis de cada tarea sino, sale error ---> TypeError: unsupported operand type(s) for >>: '_TaskDecorator' and '_TaskDecorator'
    tarea_numero() >> tarea_duplicar() >> tarea_size()
    
ejemplo_rutina_llama_codigo()


@dag(
    dag_id="obtiene_valor_de_parametro_usando_xcom_pull",
    description='descripcion del dag creado',
    tags=['XCOM_PUSH XCOM_PULL'],
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
def taskflow():
    
    @task
    def number_task():
        return get_number()
    
    @task
    def duplicate_task(number):
        
        if number %2 == 0:
            return 13
        return get_duplicate_number(number)
    
    @task
    def len_task(number):
        return get_len(number)

    len_task(duplicate_task(number_task()))


dag = taskflow()

#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################

def get_number_ti(ti):
    
    number = get_number()
    ti.xcom_push(key='OBTENER_NUMERO', value=number)
    
    return number
    

def get_duplicate_number_ti(ti):
    
    result = ti.xcom_pull(task_ids='mumero_operator_task_id', key='OBTENER_NUMERO')
    
    if result %2 ==0:
        result = 13
            
    ti.xcom_push(key='DUPLICAR_NUMERO', value=get_duplicate_number(result))
    
    return result 

def get_len_ti(ti):
    
        number = ti.xcom_pull(task_ids='duplicado_operator_task_id', key='DUPLICAR_NUMERO')
        
        ti.xcom_push(key='DUPLICAR_NUMERO', value=number)
        
        result =  ti.xcom_pull(task_ids='largo_operator_task_id', key='DUPLICAR_NUMERO')
        
        return result

#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################

with DAG(
    "xcom_dag",
    tags=['PYTHON_OPERATOR - XCOM_PUSH XCOM_PULL'],
    start_date=datetime(2021, 1, 1),
    max_active_runs=2,
    schedule=timedelta(minutes=30),
    default_args={"retries": 1, "retry_delay": timedelta(minutes=5)},
    catchup=False,
) as dag:
    number_operator = PythonOperator(
        task_id="mumero_operator_task_id", python_callable=get_number_ti
    )

    duplicate_operator = PythonOperator(
        task_id="duplicado_operator_task_id", python_callable=get_duplicate_number_ti
    )

    len_operator = PythonOperator(
        task_id="largo_operator_task_id", python_callable=get_len_ti
    )
    
    number_operator >> duplicate_operator >> len_operator
