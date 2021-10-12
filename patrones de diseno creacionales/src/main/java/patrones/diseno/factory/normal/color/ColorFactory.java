package patrones.diseno.factory.normal.color;

import patrones.diseno.factory.normal.color.clases.ColorFactoryBlue;
import patrones.diseno.factory.normal.color.clases.ColorFactoryGreen;
import patrones.diseno.factory.normal.color.clases.ColorFactoryRed;
import patrones.diseno.factory.normal.color.clases.ColorFactoryYellow;
import patrones.diseno.factory.InterfaceAbstractFactory;
import patrones.diseno.factory.normal.color.interfaces.InterfaceColorsFactory;

public class ColorFactory implements InterfaceAbstractFactory<InterfaceColorsFactory> {

    @Override
    public InterfaceColorsFactory create(String color) {
        if (color == null) {

            return new ColorFactoryYellow();
        } else if (color.equalsIgnoreCase("BLUE")){

            return new ColorFactoryBlue();
        } else  if(color.equalsIgnoreCase("GREEN")){

            return new ColorFactoryGreen();
        } else  if(color.equalsIgnoreCase("RED")){

            return new ColorFactoryRed();
        } else {

            return new ColorFactoryYellow();
        }
    }
}
