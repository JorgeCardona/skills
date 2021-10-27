package patrones.diseno.bridge;

public abstract class AbstractTipoPastel {

    AbstractPastel pastel;

    public abstract void ordenarPastel();

    public AbstractTipoPastel(AbstractPastel pastel){

        this.pastel = pastel;
    }

    protected void ordenarPastelFresa(){

        pastel.fresa();
    };


    protected void ordenarPastelMelocoton(){

        pastel.melocoton();
    };
}
