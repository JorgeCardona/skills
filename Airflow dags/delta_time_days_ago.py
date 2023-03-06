from datetime import datetime, timedelta
from airflow.decorators import dag, task

# con el parametro 'kwargs', se obtiene toda la informacion de la ejecucion del DAG
def success_message(kwargs):
    print(f'Task Completed Successfully -> parametros del DAG y TAREA {kwargs}')
# con el parametro 'kwargs', se obtiene toda la informacion de la ejecucion del DAG
def fail_message(kwargs):
    print(f'ERROR task Failed -> {kwargs}')
    
@dag(
    dag_id="delta",
    tags=['times'],
    schedule_interval= timedelta(minutes=5), # https://docs.python.org/es/3/library/datetime.html#timedelta-objects
    start_date=datetime(2023, 3, 5, 20, 39, 0), 
    end_date=datetime(2029, 12, 11),
    catchup=False, # backfilling process NO SE EJECUTA
    )
def delta():
    import random
    valor_aleatorio = random.randint(1, 20_000)
    
    @task(task_id='tarea_delta_time')
    def tarea_numero():
        return random.randint(1, 1_000_000)

    tarea_numero() 
    
delta()

@dag(
    dag_id="crontab",
    tags=['times'],
    schedule_interval='*/5 * * * *', # https://crontab.guru/#*/5_*_*_*_*
    start_date=datetime(2023, 3, 5, 20, 39, 0), 
    end_date=datetime(2029, 12, 11),
    # ponerse al dia
    catchup=True, # backfilling process ESTA POR DEFECTO en True Y SE EJECUTA
    max_active_runs=5 # es la maxima cantidad de DAGs corriendo cuando hay un backfilling, para no saturar la maquina y acabar con los recursos
    )
def cron():
    import random
    valor_aleatorio = random.randint(1, 20_000)
    
    @task(task_id='tarea_crontab')
    def tarea_numero():
        return random.randint(1, 1_000_000)

    tarea_numero() 
    
cron()


from airflow.utils.dates import days_ago

@dag(
    dag_id="days_ago",
    tags=['times'],
    schedule_interval='@daily', # https://docs.python.org/es/3/library/datetime.html#timedelta-objects
    start_date=days_ago(5), 
    end_date=datetime(2029, 12, 11),
    # especifique cuánto tiempo debe estar activo un DagRun antes de que se agote el tiempo de espera o falle, para que se puedan crear nuevos DagRun.
    # El tiempo de espera solo se aplica para DagRuns programados.
    dagrun_timeout = timedelta(minutes=5),
    concurrency=10, #define cuántas instancias al mismo tiempo RUNNING de tareas puede tener un DAG, más allá del cual las cosas se ponen en cola.
    max_active_tasks=5, # el número de instancias de tareas permitidas para ejecutarse simultáneamente
    max_active_runs=3, # define cuántas instancias RUNNING simultáneas de un DAG puede haber.
    #catchup=True, # backfilling process ESTA POR DEFECTO en True Y SE EJECUTA
    )
def days():
    import random
    valor_aleatorio = random.randint(1, 20_000)
    
    @task(task_id='tarea_days_ago',
          retries=3, # si la tarea falla cuantas veces va a reintentar la tarea para completar la tarea exitosamente
          retry_delay=timedelta(minutes=5), # cuanto tiempo espera entre cada reintento que la tarea falla
          on_success_callback=success_message, # accion que hace si la tarea se completa de manera exitosa
          on_failure_callback=fail_message, # accion que hace si la tarea FALLA
          # retries Y retry_delay son argumento que se pueden declarar en el DAG como argumentos por defecto y afecta todas los OPERATORS o tasks del DAG
          )
    def tarea_numero(uno='parametro 1',dos='parametro 2'):
        return random.randint(1, 1_000_000)

    tarea_numero() 
    
days()
