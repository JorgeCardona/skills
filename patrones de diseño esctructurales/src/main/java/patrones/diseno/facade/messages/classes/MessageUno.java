package patrones.diseno.facade.messages.classes;

import patrones.diseno.facade.messages.interfaces.InterfaceMessage;

public class MessageUno implements InterfaceMessage {

    @Override
    public void message() {
        System.out.println("Clase Uno");
    }

    public MessageUno() {
    }
}
