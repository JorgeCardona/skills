package patrones.diseno.factory.normal.color.clases;

import patrones.diseno.factory.normal.color.interfaces.InterfaceColorsFactory;

public class ColorFactoryYellow implements InterfaceColorsFactory {


    @Override
    public void color() {
        System.out.println("Color Amarillo");
    }
}
