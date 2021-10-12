package patrones.diseno.factory.abstracta;

import patrones.diseno.factory.InterfaceAbstractFactory;
import patrones.diseno.factory.normal.color.ColorFactory;
import patrones.diseno.factory.normal.messages.MessageFactory;

public class ProduceAbstractFactory {

    public static InterfaceAbstractFactory getFactory (String interfaceInstance){

        if(interfaceInstance.equalsIgnoreCase("COLORS")){

            return new ColorFactory();
        } else {
            return  new MessageFactory();
        }
    }
}
