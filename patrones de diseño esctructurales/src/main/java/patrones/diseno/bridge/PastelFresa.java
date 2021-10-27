package patrones.diseno.bridge;

public class PastelFresa extends AbstractTipoPastel {

    public PastelFresa(AbstractPastel pastel) {
        super(pastel);
    }

    @Override
    public void ordenarPastel() {

        ordenarPastelFresa();
    }
}
