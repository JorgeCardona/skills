package patrones.diseno.command;

public class EncenderLampara implements InterfaceCommand {

    private Lampara lampara;

    public EncenderLampara(Lampara lampara) {
        this.lampara = lampara;
    }

    @Override
    public void ejecutar() {
        lampara.encender();
    }
}
