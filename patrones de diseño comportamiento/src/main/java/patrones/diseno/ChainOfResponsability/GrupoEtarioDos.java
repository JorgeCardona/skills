package patrones.diseno.ChainOfResponsability;

public class GrupoEtarioDos implements InterfaceLimite {

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

        if(x>=21 && x < 41){
            System.out.println("Queda asignado al grupo Etario 2");
        } else {
            next.calcularGrupo(x);
        }
    }
}
