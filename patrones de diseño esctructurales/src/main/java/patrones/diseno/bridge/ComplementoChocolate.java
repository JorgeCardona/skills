package patrones.diseno.bridge;

public class ComplementoChocolate extends AbstractPastel {

    @Override
    public void fresa(){

        System.out.println("Ordenado Pastel de Fresa con Chocolate");
    };

    @Override
    public void melocoton(){

        System.out.println("Ordenado Pastel de Melocoton con Chocolate");
    };
}
