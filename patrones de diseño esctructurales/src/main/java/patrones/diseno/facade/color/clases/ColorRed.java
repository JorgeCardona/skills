package patrones.diseno.facade.color.clases;

import patrones.diseno.facade.color.interfaces.InterfaceColors;

public class ColorRed implements InterfaceColors {


    @Override
    public void color() {
        System.out.println("Color Rojo");
    }
}