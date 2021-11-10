package patrones.diseno.command;

public class Lampara implements Acciones {

    @Override
    public void encender(){
        System.out.println("Lampara Encendida");
    }

    @Override
    public void apagar(){
        System.out.println("Lampara Apagada");
    }
}
