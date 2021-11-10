package patrones.diseno.command;

public class Auto implements Acciones {

    @Override
    public void encender(){
        System.out.println("Auto Encendido");
    }

    @Override
    public void apagar(){
        System.out.println("Auto Apagado");
    }
}
