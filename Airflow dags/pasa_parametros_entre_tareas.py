import random

def get_number():
    
    return random.randint(1, 1_000_000)

def get_duplicate_number(number):
    
    return number * 2

def get_len(number):
    return len(str(number))
    

########################################################################################################################################################################
############################################################# TASK DECORATOR FUNCION COMO PARAMETRO ####################################################################
########################################################################################################################################################################

from airflow.decorators import dag, task
from datetime import datetime, timedelta


url = "http://catfact.ninja/fact"

default_args = {"start_date": datetime(2021, 1, 1)}

@dag(
    dag_id="funcion_como_parametro",
    description='descripcion del dag creado',
    tags=['PASA_VALORES_ENTRE_TAREAS'],
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
    def tarea_numero():
        return get_number()

    @task
    def tarea_duplicar(number):
        
        if number %2 ==0:
            return 13
        
        return get_duplicate_number(number)

    @task
    def tarea_size(number):
        
        return get_len(number)
            
    # Invoke functions to create tasks and define dependencies
    tarea_size(tarea_duplicar(tarea_numero()))

taskflow()


########################################################################################################################################################################
############################################################## TASK DECORATOR XCOM_PUSH - XCOM_PULL ####################################################################
########################################################################################################################################################################

    
@dag(
    dag_id="resultado_como_parametro",
    description='descripcion del dag creado',
    tags=['PASA_VALORES_ENTRE_TAREAS'],
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

########################################################################################################################################################################
############################################################# PYTHON OPERATOR XCOM_PUSH - XCOM_PULL ####################################################################
########################################################################################################################################################################
from airflow import DAG
from airflow.operators.python import PythonOperator

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


    
with DAG(
    dag_id="python_operator_xcom_push_xcom_pull",
    tags=['PASA_VALORES_ENTRE_TAREAS'],
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
    

########################################################################################################################################################################
############################################################# ELIMINA CONTENIDO DE LAS KEY EN EL XCOM ##################################################################
########################################################################################################################################################################
import os
from airflow.models import XCom
from airflow.utils.db import provide_session

@provide_session
def limpiar_cache_variables_xcom(session=None):
    
    # captura ek nombre del dag ejecutado con la variable de AIRFLOW
    dag_ids = os.environ["AIRFLOW_CTX_DAG_ID"]
    session.query(XCom).filter(XCom.dag_id == dag_ids).delete()
    
########################################################################################################################################################################
############################################################# TASK DECORATOR FUNCION COMO PARAMETRO ####################################################################
########################################################################################################################################################################
from airflow.decorators import dag, task

# funciones que se llaman al terminar la tarea con exito o si falla la tarea
def task_failure_alert(context):
    print(f"LA TAREA {context['task']} HA FALLADO, {context['run_id']}, REVISE EL LOG PARA MAS DETALLES...")

def dag_success_alert(context):
    print('el contexto es', context)
    print(f"DAG HA COMPLETADO CON EXITO, run_id: {context['run_id']} Y LA TAREA: {context['task']}")
    
    
    
@dag(
    dag_id="funcion_como_parametro_elimina_xcom",
    description='descripcion del dag creado',
    tags=['ELIMINA_CONTENIDO_VARIABLES_XCOM'],
    schedule_interval='@monthly', # https://airflow.apache.org/docs/apache-airflow/1.10.1/scheduler.html#dag-runs
    concurrency=10,  
    max_active_runs=3, 
    start_date=datetime(2000, 1, 1), 
    end_date=datetime(2029, 12, 11), 
    catchup=False,
    default_args={
                "dag_owner": "https://hithub.com/jorgecardona",
                "owner": "Jorge Cardona",  # This defines the value of the "owner" column in the DAG view of the Airflow UI
                "retries": 0,  # If a task fails, it will retry 2 times.
                "retry_delay": timedelta(minutes=3, ), # datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
                "do_xcom_push":False,
                "do_xcom_pull":False
                }
    )
def taskflow():
    
    @task(on_success_callback=dag_success_alert, on_failure_callback=task_failure_alert)
    def tarea_numero():
        return get_number()

    @task(on_success_callback=dag_success_alert, on_failure_callback=task_failure_alert)
    def tarea_duplicar(number):
        
        if number %2 ==0:
            return 13
        
        return get_duplicate_number(number)

    @task(on_success_callback=dag_success_alert, on_failure_callback=task_failure_alert)
    def tarea_size(number):
        
        return get_len(number)

    @task(on_success_callback=dag_success_alert, on_failure_callback=task_failure_alert)
    def eliminar_variables_xcom():
        limpiar_cache_variables_xcom()
            
    # Invoke functions to create tasks and define dependencies
    tarea_size(tarea_duplicar(tarea_numero())) >> eliminar_variables_xcom()

taskflow()


########################################################################################################################################################################
############################################################## TASK DECORATOR XCOM_PUSH - XCOM_PULL ####################################################################
########################################################################################################################################################################

    
@dag(
    dag_id="resultado_como_parametro_elimina_xcom",
    description='descripcion del dag creado',
    tags=['ELIMINA_CONTENIDO_VARIABLES_XCOM'],
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
    
    @task(task_id='tarea_extraer_usando_parametro_del_decorador', on_success_callback=dag_success_alert, on_failure_callback=task_failure_alert)
    def tarea_numero(ti=None):
        # guarda el valor de retorno de VALUE=mostrar(valor_aleatorio) en la key DESCARGAR_DATOS
        ti.xcom_push(key='OBTENER_NUMERO', value=get_number())
        
        # valor de retorno para la tarea
        return valor_aleatorio

    @task(on_success_callback=dag_success_alert, on_failure_callback=task_failure_alert)
    def tarea_duplicar(ti=None):
        
        # obtiene el valor que la tarea con id task_ids, "tarea_extraer" subio al xcom
        # lee el valor usando la task_ids y la key
        result = ti.xcom_pull(task_ids='tarea_extraer_usando_parametro_del_decorador', key='OBTENER_NUMERO')
        
        if result %2 ==0:
            result = 13
              
        ti.xcom_push(key='DUPLICAR_NUMERO', value=get_duplicate_number(result))
        
        return result
 
    @task(on_success_callback=dag_success_alert, on_failure_callback=task_failure_alert)
    def tarea_size(ti=None):
        
        result = ti.xcom_pull(task_ids='tarea_duplicar', key='DUPLICAR_NUMERO')
        
        return get_len(result)
    
    @task(on_success_callback=dag_success_alert, on_failure_callback=task_failure_alert)
    def eliminar_variables_xcom():
        limpiar_cache_variables_xcom()

    # tiene que llevar los parentesis de cada tarea sino, sale error ---> TypeError: unsupported operand type(s) for >>: '_TaskDecorator' and '_TaskDecorator'
    tarea_numero() >> tarea_duplicar() >> tarea_size() >> eliminar_variables_xcom()
    
ejemplo_rutina_llama_codigo()

########################################################################################################################################################################
############################################################# PYTHON OPERATOR XCOM_PUSH - XCOM_PULL ####################################################################
########################################################################################################################################################################

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


    
with DAG(
    dag_id="python_operator_xcom_push_xcom_pull_elimina_xcom",
    tags=['ELIMINA_CONTENIDO_VARIABLES_XCOM'],
    start_date=datetime(2021, 1, 1),
    max_active_runs=2,
    schedule=timedelta(minutes=30),
    default_args={"retries": 1, "retry_delay": timedelta(minutes=5)},
    catchup=False,
) as dag:
    number_operator = PythonOperator(
        task_id="mumero_operator_task_id", 
        python_callable=get_number_ti, 
        on_success_callback=dag_success_alert, 
        on_failure_callback=task_failure_alert
    )

    duplicate_operator = PythonOperator(
        task_id="duplicado_operator_task_id", 
        python_callable=get_duplicate_number_ti, 
        on_success_callback=dag_success_alert, 
        on_failure_callback=task_failure_alert
    )

    len_operator = PythonOperator(
        task_id="largo_operator_task_id", 
        python_callable=get_len_ti, 
        on_success_callback=dag_success_alert, 
        on_failure_callback=task_failure_alert
    )

    delete_xcom = PythonOperator(
        task_id="delete_xcom",
        python_callable = limpiar_cache_variables_xcom, 
        on_success_callback=dag_success_alert,
        on_failure_callback=task_failure_alert,
        dag=dag
    )
	  
    number_operator >> duplicate_operator >> len_operator >> delete_xcom
