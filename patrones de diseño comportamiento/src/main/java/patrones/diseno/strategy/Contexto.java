package patrones.diseno.strategy;

public class Contexto {

    InterfaceStrategy interfaceStrategy;

    public Contexto(InterfaceStrategy interfaceStrategy) {
        this.interfaceStrategy = interfaceStrategy;
    }

    public int ejecutarCalculo(int x, int y){

        return interfaceStrategy.calcular(x, y);
    }
}
