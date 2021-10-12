package patrones.diseno.builder;

import lombok.Data;

@Data
public class BaseBuilder {

    private String potencia;
    private String raiz;
    private String absoluto;
    private String logaritmo;
    private String combinatoria;

    public BaseBuilder potencia(String potencia) {
        this.potencia = potencia;
        return this;
    }

    public BaseBuilder raiz(String raiz) {
        this.raiz = raiz;
        return this;
    }

    public BaseBuilder combinatoria(String combinatoria, String logaritmo, String absoluto) {
        this.absoluto = absoluto;
        this.logaritmo = logaritmo;
        this.combinatoria = combinatoria;
        return this;
    }

    public Base buildObject(){
        return new Base(this);
    }
}