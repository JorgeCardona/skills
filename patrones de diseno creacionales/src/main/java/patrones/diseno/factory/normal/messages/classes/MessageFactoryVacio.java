package patrones.diseno.factory.normal.messages.classes;

import patrones.diseno.factory.normal.messages.interfaces.InterfaceMessageFactory;

public class MessageFactoryVacio implements InterfaceMessageFactory {


    @Override
    public void message() {
        System.out.println("Mensaje Vacio o Null");
    }
}
