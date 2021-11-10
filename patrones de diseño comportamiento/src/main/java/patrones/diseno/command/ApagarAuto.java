package patrones.diseno.command;

public class ApagarAuto implements InterfaceCommand {

    private Auto auto;

    public ApagarAuto(Auto auto) {
        this.auto = auto;
    }

    @Override
    public void ejecutar() {

        auto.apagar();
    }
}
