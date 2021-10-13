package patrones.diseno.proxy;

public class Stuffs implements InterfaceProxy {

    @Override
    public void generate() {
        System.out.println("Usando el proxy en la clase Stuffs");
    }

    public void otherMethod(){

        System.out.println("Usando el metodo other Method de la clase Stuffs por intermedio del proxy");
    }
}
