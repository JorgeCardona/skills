package patrones.diseno;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import patrones.diseno.builder.Base;
import patrones.diseno.builder.BaseBuilder;
import patrones.diseno.factory.InterfaceAbstractFactory;
import patrones.diseno.factory.abstracta.ProduceAbstractFactory;
import patrones.diseno.factory.normal.color.interfaces.InterfaceColorsFactory;
import patrones.diseno.factory.normal.messages.MessageFactory;
import patrones.diseno.factory.normal.messages.interfaces.InterfaceMessageFactory;
import patrones.diseno.prototype.ClaseClonable;
import patrones.diseno.singleton.SingletonPatternTestFail;
import patrones.diseno.singleton.SingletonPatternTestOk;

import java.util.ArrayList;

@SpringBootApplication
public class DisenoApplication {

	// solo se cre un objeto en toda la aplicacion
	public static void singletonTest(){
		SingletonPatternTestOk tp1 = SingletonPatternTestOk.data();
		SingletonPatternTestOk tp2 = SingletonPatternTestOk.data();

		SingletonPatternTestFail tpf1 = new SingletonPatternTestFail();
		SingletonPatternTestFail tpf2 = new SingletonPatternTestFail();

		System.out.println("-----------------------");
		System.out.println("compara las dos instancias de los objetos SingletonPatternTestOk y son iguales " + tp1.equals(tp2));
		System.out.println(tp1 + " " + tp2);

		System.out.println("-----------------------");

		System.out.println("compara las dos instancias de los objetos SingletonPatternTestFail y son iguales " + tpf1.equals(tpf2));
		System.out.println(tpf1 + " " + tpf2);

		System.out.println(tp1.hashCode());
		System.out.println(tp2.hashCode());
	}

	// se crea el objeto dependiendo del identificador que se le envie
	public static void factoryMessagesTest(){

		MessageFactory messageFactory = new MessageFactory();

		ArrayList<String> values = new ArrayList<>();
		values.add(null);
		values.add("uno");
		values.add("Dos");
		values.add("TRES");
		values.add("---");

		for (String val: values) {
			InterfaceMessageFactory instanceMessageFactory = messageFactory.create(val);
			instanceMessageFactory.message();
		}
	}

	// se crea la fabrica dependiendo del identificador que se le envie
	// se crea el objeto dependiendo del identificador que se le envie
	public static void abstractFactoryTest(){

		InterfaceAbstractFactory afc;

		afc = ProduceAbstractFactory.getFactory("COLORS");

		InterfaceColorsFactory ifcv = (InterfaceColorsFactory) afc.create("GREEN");
		ifcv.color();

		InterfaceColorsFactory ifcb = (InterfaceColorsFactory) afc.create("BLUE");
		ifcb.color();

		afc = ProduceAbstractFactory.getFactory("----");
		InterfaceMessageFactory ifcu = (InterfaceMessageFactory) afc.create("UNO");
		ifcu.message();

		InterfaceMessageFactory ifcd = (InterfaceMessageFactory) afc.create("TRES");
		ifcd.message();

	}

	public static void validateObjects(Object original, Object clone){

		boolean equalObjects = original.equals(clone) ? true : false;
		System.out.println("OBJETO ORIGINAL " + original + " OBJETO CLONADO " + clone);
		System.out.println("HASHCODE ORIGINAL " + original.hashCode() + " HASHCODE CLONADO " + clone.hashCode());
		System.out.println("Instancia de ORIGINAL == Instancia de CLONADO " + equalObjects);
		System.out.println();

	}
	// crea una instancia con los valores clonados de otra instancia
	public static void prototypeTest(){

		ClaseClonable original = new ClaseClonable();
		original.setX(1);
		original.setY(2);

		ClaseClonable clone = (ClaseClonable) original.clonar();

		validateObjects(original, clone);

		clone.setX(7);
		validateObjects(original, clone);
	}

	public static void builderTest(){

		Base builder = new BaseBuilder()
				.potencia("Potencia")
				.raiz("Raiz")
				.combinatoria("combinatoria", "logaritmo", "absoluto")
				.buildObject();

		System.out.println(builder);
	}

	public static void main(String[] args) {
		SpringApplication.run(DisenoApplication.class, args);

		//singletonTest();
		//prototypeTest();
		//factoryMessagesTest();
		//abstractFactoryTest();
		builderTest();
	}

}
