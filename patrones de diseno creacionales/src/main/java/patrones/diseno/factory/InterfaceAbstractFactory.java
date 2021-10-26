package patrones.diseno.factory;

//https://docs.oracle.com/javase/tutorial/java/generics/types.html
public interface InterfaceAbstractFactory<T> {

    T create(String objeto);
}
