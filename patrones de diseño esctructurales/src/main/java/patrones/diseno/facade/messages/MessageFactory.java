package patrones.diseno.facade.messages;

import patrones.diseno.facade.messages.classes.MessageDos;
import patrones.diseno.facade.messages.classes.MessageTres;
import patrones.diseno.facade.messages.classes.MessageUno;
import patrones.diseno.facade.messages.classes.MessageVacio;
import patrones.diseno.facade.messages.interfaces.InterfaceMessage;

public class MessageFactory {

    public InterfaceMessage create(String message) {

        if (message == null) {
            return new MessageVacio();

        } else if (message.equalsIgnoreCase("UNO")){
            return new MessageUno();

        } else  if(message.equalsIgnoreCase("DOS")){
            return new MessageDos();

        } else  if(message.equalsIgnoreCase("TRES")){
            return new MessageTres();

        } else {
            return new MessageVacio();
        }
    }
}
