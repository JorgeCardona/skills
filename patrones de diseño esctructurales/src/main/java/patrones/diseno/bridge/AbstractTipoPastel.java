package patrones.diseno.bridge;

public abstract class AbstractTipoPastel {

    AbstractPastel pastel;

    public abstract void ordenarPastel();

    public AbstractTipoPastel(AbstractPastel pastel){

        this.pastel = pastel;
    }

    protected void fresa(){

        pastel.fresa();
    };


    public void melocoton(){

        pastel.melocoton();
    };
}
