package patrones.diseno.template;

public abstract class AbstractTemplate {

    protected abstract void pedirLacarta();
    protected abstract void ordenar();
    protected abstract void comer();

    public void visitarRestaurante(){

        pedirLacarta();
        ordenar();
        comer();

    }

}