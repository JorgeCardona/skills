package patrones.diseno.facade.color;

import patrones.diseno.facade.color.clases.ColorBlue;
import patrones.diseno.facade.color.clases.ColorGreen;
import patrones.diseno.facade.color.clases.ColorRed;
import patrones.diseno.facade.color.clases.ColorYellow;
import patrones.diseno.facade.color.interfaces.InterfaceColors;

public class ColorFactory {

    public InterfaceColors create(String color) {
        if (color == null) {

            return new ColorYellow();
        } else if (color.equalsIgnoreCase("BLUE")){

            return new ColorBlue();
        } else  if(color.equalsIgnoreCase("GREEN")){

            return new ColorGreen();
        } else  if(color.equalsIgnoreCase("RED")){

            return new ColorRed();
        } else {

            return new ColorYellow();
        }
    }
}
