package patrones.diseno.factory.normal.messages.classes;

import patrones.diseno.factory.normal.messages.interfaces.InterfaceMessageFactory;

public class MessageFactoryTres implements InterfaceMessageFactory {

    @Override
    public void message() {
        System.out.println("Clase Tres");
    }

    public MessageFactoryTres() {
    }
}
