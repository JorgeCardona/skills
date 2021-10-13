package patrones.diseno.bridge;

public class ComplementoHelado extends AbstractPastel {

    @Override
    protected void fresa(){

        System.out.println("Ordenado Pastel de Fresa con Helado");
    };

    @Override
    protected void melocoton(){

        System.out.println("Ordenado Pastel de Melocoton con Helado");
    };
}
