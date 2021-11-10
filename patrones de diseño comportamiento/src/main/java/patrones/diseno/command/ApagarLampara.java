package patrones.diseno.command;

public class ApagarLampara implements InterfaceCommand {

    private Lampara lampara;

    public ApagarLampara(Lampara lampara) {
        this.lampara = lampara;
    }

    @Override
    public void ejecutar() {

        lampara.apagar();
    }
}
