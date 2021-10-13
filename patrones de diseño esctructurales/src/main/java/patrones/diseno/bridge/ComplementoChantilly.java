package patrones.diseno.bridge;

public class ComplementoChantilly extends AbstractPastel {

    @Override
    protected void fresa(){

        System.out.println("Ordenado Pastel de Fresa con Chantilly");
    };

    @Override
    protected void melocoton(){

        System.out.println("Ordenado Pastel de Melocoton con Chantilly");
    };
}
