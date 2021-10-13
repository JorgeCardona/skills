package patrones.diseno.facade.color.clases;

import patrones.diseno.facade.color.interfaces.InterfaceColors;

public class ColorGreen implements InterfaceColors {


    @Override
    public void color() {
        System.out.println("Color Verde");
    }
}