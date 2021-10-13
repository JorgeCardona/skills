package patrones.diseno.decorator;

import patrones.diseno.facade.color.interfaces.InterfaceColors;

public class AddMethodAbstractColorDecorator extends AbstractColorDecorator {

    public AddMethodAbstractColorDecorator(InterfaceColors decorateInterface) {
        super(decorateInterface);
    }

    @Override
    public void color() {
        decorateInterface.color();
        newFunctionality(decorateInterface);
        newFunctionalityV2(decorateInterface);
    }

    private void newFunctionality(InterfaceColors decorateInterface){

        System.out.println("Adicionada nueva funcionalidad");
    }

    public void newFunctionalityV2(InterfaceColors decorateInterface){

        System.out.println("Accediendo a nueva funcionalidad de hash code " + decorateInterface.hashCode() );
    }
}
