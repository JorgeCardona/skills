package patrones.diseno.facade.messages.classes;

import patrones.diseno.facade.messages.interfaces.InterfaceMessage;

public class MessageVacio implements InterfaceMessage {


    @Override
    public void message() {
        System.out.println("Mensaje Vacio o Null");
    }
}
