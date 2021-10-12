package patrones.diseno.factory.normal.messages;

import patrones.diseno.factory.InterfaceAbstractFactory;
import patrones.diseno.factory.normal.messages.classes.MessageFactoryDos;
import patrones.diseno.factory.normal.messages.classes.MessageFactoryTres;
import patrones.diseno.factory.normal.messages.classes.MessageFactoryUno;
import patrones.diseno.factory.normal.messages.classes.MessageFactoryVacio;
import patrones.diseno.factory.normal.messages.interfaces.InterfaceMessageFactory;

public class MessageFactory  implements InterfaceAbstractFactory<InterfaceMessageFactory> {


    @Override
    public InterfaceMessageFactory create(String message) {
        if (message == null) {

            return new MessageFactoryVacio();
        } else if (message.equalsIgnoreCase("UNO")){

            return new MessageFactoryUno();
        } else  if(message.equalsIgnoreCase("DOS")){

            return new MessageFactoryDos();
        } else  if(message.equalsIgnoreCase("TRES")){

            return new MessageFactoryTres();
        } else {

            return new MessageFactoryVacio();
        }
    }
}
