package patrones.diseno.decorator;

import patrones.diseno.facade.color.interfaces.InterfaceColors;

public abstract class AbstractColorDecorator implements InterfaceColors {

    protected InterfaceColors decorateInterface;

    public AbstractColorDecorator(InterfaceColors decorateInterface){

        this.decorateInterface = decorateInterface;
    }

    @Override
    public void color() {
        this.decorateInterface.color();
    }
}
