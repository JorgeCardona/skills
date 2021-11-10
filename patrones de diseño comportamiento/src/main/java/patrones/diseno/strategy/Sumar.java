package patrones.diseno.strategy;

public class Sumar implements InterfaceStrategy{

    @Override
    public int calcular (int x, int y) {
        return x + y;
    }
}
