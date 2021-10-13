package patrones.diseno.proxy;

public class ProxyProducer implements InterfaceProxy {

    private InterfaceProxy instance;


    public ProxyProducer(InterfaceProxy instance){
        this.instance = instance;
    }


    @Override
    public void generate() {

        System.out.println("Usando el proxy en la clase Proxy Producer");
        instance.generate();
    }
}
