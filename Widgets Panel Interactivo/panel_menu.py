# INSTALAR LOS PAQUETES NECESARIOS
# pip install uvicorn panel

# INICIAR LA APLICACION
# uvicorn panel_menu:app --reload --port 5555

# ACCEDER A LA APLICACION
# http://127.0.0.1:7777

import panel as pn

def autocomplete_event_select_app():
    listado_opciones = ['Arco Iris','Amarillo','Azul','Rojo','Verde','Blanco','Rosado','Purpura','Agua Marina','Avellana','Ambar','Anaranjado']

    # panel de texto
    text = pn.widgets.StaticText()

    # panel de lista desplegable
    select = pn.widgets.Select(name='Select', options={'Biology': 'Biology is the number 1', 'Chemistry': 'Chemistry is the number 2'})

    # callback, funcion que se activa cuando se genera el evento de seleccion de una valor de la lista desplegable
    def update(event):
    # is dropdown select
        text.value = select.value.upper()

    # llama a la funcion y ejecuta su codigo al seleccionar cada  el valor del dropdown select
    select.param.watch(update, 'value')

    # panel de autocompletado
    autocomplete = pn.widgets.AutocompleteInput(
                                            name='Lista con ayuda de autocompletado', 
                                            options=listado_opciones,
                                            placeholder='digite su opcion aqui',
                                            case_sensitive=False,
                                            min_characters=1,
                                            restrict=True
                                            )
    # panel de barra desplegable
    int_slider = pn.widgets.IntSlider(name='Integer Slider', start=0, end=8, step=2, value=4)

    # layout, usa el widget de autocompletado, el widget del evento y el widget donde se muestra el contenido obtenido al procesar la funcion 
    panel = pn.Column(int_slider, autocomplete, select, text)

    return panel.servable()


def slider_select_app():

    listado_opciones = ['Amarillo','Azul','Rojo','Verde','Blanco','Rosado','Purpura','Agua Marina','Avellana','Ambar','Anaranjado']
    
    select = pn.widgets.Select(name='Colores', options=listado_opciones)

    int_slider = pn.widgets.IntSlider(name='Integer Slider', start=0, end=8, step=2, value=4)
    return pn.Row(int_slider, select).servable()


def markdown_app():
    return '# This is a Panel app'

def json_app():
    return pn.pane.JSON({'abc': 123})



# Variables de Configuracion
UBICACION_DE_LA_APLICACION = 'panel_menu:app'
HOST_APLICACION_SERVIDOR_QUE_INTERACCIONA_CON_PANELES = '127.0.0.1'
PUERTO_APLICACION_SERVIDOR_QUE_INTERACCIONA_CON_PANELES = 5555
URL_APLICACION_QUE_INTERACCIONA_CON_PANELES = f'{HOST_APLICACION_SERVIDOR_QUE_INTERACCIONA_CON_PANELES}:{PUERTO_APLICACION_SERVIDOR_QUE_INTERACCIONA_CON_PANELES}'

PUERTO_EXPONER_PANELES = 7777
HOST_EXPONER_PANELES = '127.0.0.1'
URL_EXPONER_PANELES = f'{HOST_EXPONER_PANELES}:{PUERTO_EXPONER_PANELES}'

# TODAS LAS APLICACIONES 'panels' QUE SE VAN A MOSTRAR EN LA PAGINA DE INICIO
app = pn.serve(
        panels={
                'Slider_Auto_Completado': autocomplete_event_select_app, # no se puede usar espacios en blanco, se debe usar el guion bajo, under score '_'
                'Select_Event_Text': slider_select_app,
                'markdown': markdown_app,
                'json': json_app
                },
        title={'Slider_Auto_Completado': 'A Markdown App', 'Select_Event_Text': 'A JSON App', 'markdown': 'A Markdown App', 'json': 'A JSON App'},
        port=PUERTO_EXPONER_PANELES,
        allow_websocket_origin=[# similar al cross origin
                                URL_APLICACION_QUE_INTERACCIONA_CON_PANELES, # donde se van a desplegar los paneles
                                URL_EXPONER_PANELES # donde se le esta haciendo las peticiones a los paneles
                                ],
        address=HOST_EXPONER_PANELES, 
        show=False
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(UBICACION_DE_LA_APLICACION,
                reload=True,
                host=HOST_APLICACION_SERVIDOR_QUE_INTERACCIONA_CON_PANELES,
                port=PUERTO_APLICACION_SERVIDOR_QUE_INTERACCIONA_CON_PANELES,
                log_level="INFO"
                )