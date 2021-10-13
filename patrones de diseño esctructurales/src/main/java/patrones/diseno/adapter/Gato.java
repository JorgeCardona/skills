package patrones.diseno.adapter;

public class Gato implements InterfaceAnimal {

    @Override
    public void sonido() {
        System.out.println("Miau");
    }

    @Override
    public void alimento() {
        System.out.println("Concentrado");
    }

    @Override
    public void habitat() {
        System.out.println("Casa con Humanos");
    }
}
