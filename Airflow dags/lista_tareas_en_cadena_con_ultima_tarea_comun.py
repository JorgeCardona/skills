import random
from datetime import datetime, timedelta

def get_number():
    
    return random.randint(1, 1_000_000)

def get_duplicate_number(number):
    
    return number * 2

def get_len(number):
    return len(str(number))
    


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
    
    mensaje_uno(context)
    mensaje_dos(context)
 
def mensaje_uno(context):
    print('OTRO MENSAJE 11111111111111111111')
       
def mensaje_dos(context):
    print('OTRO MENSAJE 22222222222222222222')
        
@dag(
    dag_id="flujo_tareas_en_cadena_con_tarea_final_en_comun",
    description='descripcion del dag creado',
    tags=['ELIMINA_CONTENIDO_VARIABLES_XCOM'],
    schedule_interval=None, # https://airflow.apache.org/docs/apache-airflow/1.10.1/scheduler.html#dag-runs
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
    from time import sleep
    
    @task(on_success_callback=dag_success_alert, on_failure_callback=task_failure_alert, trigger_rule='all_done')
    def eliminar_variables_xcom():
        limpiar_cache_variables_xcom()
            
    from airflow.models.baseoperator import chain
    
    lista_tarea_numero = list()   
    lista_tarea_duplicar = list()
    lista_tarea_size = list()
    
    lista = ['amarillo','azul','rojo','verde','rosado']
    
    lista_dags = []
    for index, value in enumerate(lista):
        
        indice = index + 1
        task_id_tarea_numero = f'tarea_{value}_numero'
        task_id_tarea_duplicar = f'tarea_{value}_duplicar'
        task_id_tarea_size = f'tarea_{value}_size'
        
                
        @task(task_id=task_id_tarea_numero, on_success_callback=eliminar_variables_xcom, on_failure_callback=task_failure_alert)
        def tarea_numero(ti=None, indice=0):
            
            # guarda el valor de retorno de VALUE=mostrar(valor_aleatorio) en la key DESCARGAR_DATOS
            ti.xcom_push(key=f'OBTENER_NUMERO_{indice}', value=get_number())
            
            return get_number()

        @task(task_id=task_id_tarea_duplicar, on_success_callback=eliminar_variables_xcom, on_failure_callback=task_failure_alert)
        def tarea_duplicar(ti=None, indice=0):
            
            # obtiene el valor que la tarea con id task_ids, "tarea_extraer" subio al xcom
            # lee el valor usando la task_ids y la key
            result = ti.xcom_pull(task_ids=task_id_tarea_numero, key=f'OBTENER_NUMERO_{indice}')
            
            print(F"RESULTADO DE OBTENER NUMERO {result}, indice{indice}")
            
            if result %2 ==0:
                
                0/0
                return 13
            
            ti.xcom_push(key=f'DUPLICAR_NUMERO_{indice}', value=get_duplicate_number(result))
            
            return get_duplicate_number(result)

        @task(task_id=task_id_tarea_size, on_success_callback=eliminar_variables_xcom, on_failure_callback=task_failure_alert)
        def tarea_size(ti=None, indice=0):
            
            result = ti.xcom_pull(task_ids=task_id_tarea_duplicar, key=f'DUPLICAR_NUMERO_{indice}')
            
            ti.xcom_push(key=f'TAMANO_NUMERO_{indice}', value=get_len(result))
            return get_len(result)

        # se unen las tareas por tipo para que se puedan predeceder una de otra
        lista_tarea_numero.append(tarea_numero(indice=indice))
        lista_tarea_duplicar.append(tarea_duplicar(indice=indice))
        lista_tarea_size.append(tarea_size(indice=indice))
        
    # genera el dag final con el flujo con la ultima tarea que se ejecuta incluso si alguna falla    
    chain(lista_tarea_numero, lista_tarea_duplicar, lista_tarea_size, eliminar_variables_xcom())

taskflow()
