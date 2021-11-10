package patrones.diseno.strategy;

public class Restar implements InterfaceStrategy{

    @Override
    public int calcular (int x, int y) {
        return x - y;
    }
}
