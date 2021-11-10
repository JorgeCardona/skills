package patrones.diseno.ChainOfResponsability;

public interface InterfaceLimite {

    public void setNext(InterfaceLimite interfaceLimite);
    InterfaceLimite getNext();
    public void calcularGrupo(int x);
}
