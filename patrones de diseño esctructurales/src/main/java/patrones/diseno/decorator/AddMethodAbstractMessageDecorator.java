package patrones.diseno.decorator;

import patrones.diseno.facade.messages.interfaces.InterfaceMessage;

public class AddMethodAbstractMessageDecorator extends AbstractMessageDecorator {

    public AddMethodAbstractMessageDecorator(InterfaceMessage decorateInterface) {
        super(decorateInterface);
    }

    @Override
    public void message() {

        decorateInterface.message();
        newFunctionality(decorateInterface);
    }

    private void newFunctionality(InterfaceMessage decorateInterface){

        System.out.println("Adicionada nueva funcionalidad en mensajes");
    }
}
