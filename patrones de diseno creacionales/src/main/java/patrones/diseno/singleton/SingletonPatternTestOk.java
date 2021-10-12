package patrones.diseno.singleton;

public class SingletonPatternTestOk {

    private static SingletonPatternTestOk objetoInstanciado;

    private SingletonPatternTestOk() {
    }

    public static SingletonPatternTestOk data(){

        if(objetoInstanciado == null){
            objetoInstanciado = new SingletonPatternTestOk();
        }

        return objetoInstanciado;

    }
}
