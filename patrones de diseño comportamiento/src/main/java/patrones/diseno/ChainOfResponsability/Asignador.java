package patrones.diseno.ChainOfResponsability;

public class Asignador implements InterfaceLimite {

    InterfaceLimite next;

    @Override
    public void setNext(InterfaceLimite interfaceLimite) {

        next = interfaceLimite;
    }

    @Override
    public InterfaceLimite getNext() {
        return next;
    }

    @Override
    public void calcularGrupo(int x) {

        InterfaceLimite uno = new GrupoEtarioUno();
        this.setNext(uno);

        InterfaceLimite dos = new GrupoEtarioDos();
        uno.setNext(dos);

        InterfaceLimite tres = new GrupoEtarioTres();
        dos.setNext(tres);

        InterfaceLimite cuatro = new GrupoEtarioCuatro();
        tres.setNext(cuatro);

        InterfaceLimite noRegistrado = new GrupoEtarioNoRegistrado();
        cuatro.setNext(noRegistrado);

        next.calcularGrupo(x);
    }
}
