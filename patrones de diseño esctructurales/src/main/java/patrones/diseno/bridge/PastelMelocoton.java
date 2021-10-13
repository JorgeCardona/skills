package patrones.diseno.bridge;

public class PastelMelocoton extends AbstractTipoPastel {

    public PastelMelocoton(AbstractPastel pastel) {
        super(pastel);
    }

    @Override
    public void ordenarPastel() {
        melocoton();
    }
}
