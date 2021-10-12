package patrones.diseno.builder;

import lombok.Data;

@Data
public class Base {

    private String potencia;
    private String raiz;
    private String absoluto;
    private String logaritmo;
    private String combinatoria;

    private Base() {

    }

    Base (BaseBuilder builder){

        if (builder.getRaiz() == null){
            throw new IllegalArgumentException("Raiz es requerida");
        }
        this.potencia = builder.getPotencia();
        this.raiz = builder.getRaiz();
        this.absoluto = builder.getAbsoluto();
        this.logaritmo = builder.getLogaritmo();
        this.combinatoria = builder.getCombinatoria();
    }

    @Override
    public String toString() {
        return "Base{" +
                "potencia='" + potencia + '\'' +
                ", raiz='" + raiz + '\'' +
                ", absoluto='" + absoluto + '\'' +
                ", logaritmo='" + logaritmo + '\'' +
                ", combinatoria='" + combinatoria + '\'' +
                '}';
    }
}
