package patrones.diseno.ChainOfResponsability;

public class GrupoEtarioTres implements InterfaceLimite {

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

        if(x>= 41 && x<60){
            System.out.println("Queda asignado al grupo Etario 3");
        } else {
            next.calcularGrupo(x);
        }
    }
}
