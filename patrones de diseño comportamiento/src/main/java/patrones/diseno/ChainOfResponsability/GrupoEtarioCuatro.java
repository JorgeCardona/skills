package patrones.diseno.ChainOfResponsability;

public class GrupoEtarioCuatro implements InterfaceLimite {

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

        if(x>=60 && x<126){
            System.out.println("Queda asignado al grupo Etario 4");
        } else {
            next.calcularGrupo(x);
        }
    }
}
