package patrones.diseno.facade.messages.classes;

import patrones.diseno.facade.messages.interfaces.InterfaceMessage;

public class MessageDos implements InterfaceMessage {

    @Override
    public void message() {
        System.out.println("Clase Dos");
    }

    public MessageDos() {
    }
}