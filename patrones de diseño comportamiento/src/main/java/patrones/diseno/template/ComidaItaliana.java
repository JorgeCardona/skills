package patrones.diseno.template;

public class ComidaItaliana extends AbstractTemplate {

    @Override
    protected void pedirLacarta() {
        System.out.println("Carta Italiana");
    }

    @Override
    protected void ordenar() {

        System.out.println("Pizza");
    }

    @Override
    protected void comer() {

        System.out.println("Comer Pizza Napolitana");
    }
}
