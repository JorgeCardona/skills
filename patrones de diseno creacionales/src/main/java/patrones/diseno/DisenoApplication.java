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

		MessageFactory mf = new MessageFactory();

		InterfaceMessageFactory mfv = mf.create(null);
		mfv.message();

		InterfaceMessageFactory mf1 = mf.create("uno");
		mf1.message();

		InterfaceMessageFactory mf2 = mf.create("Dos");
		mf2.message();

		InterfaceMessageFactory mf3 = mf.create("TRES");
		mf3.message();

		InterfaceMessageFactory mfn = mf.create("---");
		mfn.message();
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

	public static void prototypeTest(){

		ClaseClonable cc = new ClaseClonable();
		cc.setX(1);
		cc.setY(2);

		System.out.println(cc);

		ClaseClonable cc2 = (ClaseClonable) cc.clonar();
		System.out.println(cc2);

		boolean equalObjects = cc==cc2 ? true : false;

		System.out.println(cc.hashCode());
		System.out.println(cc2.hashCode());
		System.out.println(equalObjects);
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
		//factoryMessagesTest();
		//abstractFactoryTest();
		//prototypeTest();
		builderTest();
	}

}
