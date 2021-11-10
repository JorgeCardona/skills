package patrones.diseno.command;

public class EncenderAuto implements InterfaceCommand {

    private Auto auto;

    public EncenderAuto(Auto auto) {
        this.auto = auto;
    }

    @Override
    public void ejecutar() {

        auto.encender();
    }
}
