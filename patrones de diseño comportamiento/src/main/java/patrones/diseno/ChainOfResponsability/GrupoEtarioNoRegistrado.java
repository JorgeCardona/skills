package patrones.diseno.ChainOfResponsability;

public class GrupoEtarioNoRegistrado implements InterfaceLimite {

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

        if(x<0 || x>125){
            System.out.println("Grupo Etario No Clasificado");
        } else {
            next.calcularGrupo(x);
        }
    }
}
