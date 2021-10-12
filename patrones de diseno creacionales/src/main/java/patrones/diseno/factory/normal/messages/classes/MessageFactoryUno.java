package patrones.diseno.factory.normal.messages.classes;

import patrones.diseno.factory.normal.messages.interfaces.InterfaceMessageFactory;

public class MessageFactoryUno implements InterfaceMessageFactory {

    @Override
    public void message() {
        System.out.println("Clase Uno");
    }

    public MessageFactoryUno() {
    }
}
