package patrones.diseno.prototype;

import lombok.Data;

@Data
public class ClaseClonable implements InterfaceClonar {

    private int x;
    private int y;

    @Override
    public InterfaceClonar clonar() {

        InterfaceClonar obj = null;

        try{
            obj = (InterfaceClonar) super.clone();
        }catch(CloneNotSupportedException ex){
            System.out.println(" no se puede duplicar");
        }
        return obj;
    }

    @Override
    public String toString() {
        return "ClaseClonable{" +
                "x=" + x +
                ", y=" + y +
                '}';
    }
}
