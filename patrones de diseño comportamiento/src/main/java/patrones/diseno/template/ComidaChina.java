package patrones.diseno.template;

public class ComidaChina extends AbstractTemplate {

    @Override
    protected void pedirLacarta() {
        System.out.println("Carta China");
    }

    @Override
    protected void ordenar() {

        System.out.println("Arroz");
    }

    @Override
    protected void comer() {

        System.out.println("Comer Arroz Chino");
    }
}
