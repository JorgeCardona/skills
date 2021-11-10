package patrones.diseno.strategy;

public class Multiplicar implements InterfaceStrategy{

    @Override
    public int calcular (int x, int y) {
        return x * y;
    }
}
