package patrones.diseno.proxy;

public class Articles implements InterfaceProxy {

    public Articles(){
        otherMethod();
    }

    @Override
    public void generate() {
        System.out.println("Usando el proxy en la clase Articles");
    }

    public void otherMethod(){

        System.out.println("Usando el metodo other Method de la clase Articles por intermedio del proxy");
    }
}
