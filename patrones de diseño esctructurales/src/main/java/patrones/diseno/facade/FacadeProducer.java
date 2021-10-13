package patrones.diseno.facade;

import patrones.diseno.facade.color.ColorFactory;
import patrones.diseno.facade.color.interfaces.InterfaceColors;
import patrones.diseno.facade.messages.MessageFactory;
import patrones.diseno.facade.messages.interfaces.InterfaceMessage;

public class FacadeProducer {

    private InterfaceColors iColor;
    private ColorFactory colorFactory;

    private InterfaceMessage iMessage;
    private MessageFactory messageFactory;

    public void getColor(String color){

        this.iColor = colorFactory.create(color);
        this.iColor.color();
    }

    public void getMessage(String message){

        this.iMessage = messageFactory.create(message);
        this.iMessage.message();
    }

    public FacadeProducer(){

        this.colorFactory = new ColorFactory();
        this.messageFactory = new MessageFactory();
    }

}
