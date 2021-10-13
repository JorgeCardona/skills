package patrones.diseno.decorator;

import patrones.diseno.facade.messages.interfaces.InterfaceMessage;

public abstract class AbstractMessageDecorator implements InterfaceMessage {

    protected InterfaceMessage decorateInterface;

    public AbstractMessageDecorator(InterfaceMessage decorateInterface){
        this.decorateInterface = decorateInterface;
    }

    @Override
    public void message() {
        this.decorateInterface.message();
    }
}
