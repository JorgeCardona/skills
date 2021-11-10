package patrones.diseno.ChainOfResponsability;

public class GrupoEtarioUno implements InterfaceLimite {

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

        if(x>=0 && x < 21){
            System.out.println("Queda asignado al grupo Etario 1");
        } else {
            next.calcularGrupo(x);
        }
    }
}
