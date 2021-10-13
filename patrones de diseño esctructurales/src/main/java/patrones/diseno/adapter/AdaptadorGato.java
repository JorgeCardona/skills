package patrones.diseno.adapter;

public class AdaptadorGato implements InterfacePeluche {

    InterfaceAnimal ia;

    public AdaptadorGato(InterfaceAnimal ia){

        this.ia = ia;
    }

    @Override
    public void pitido() {

        ia.sonido();
    }
}
