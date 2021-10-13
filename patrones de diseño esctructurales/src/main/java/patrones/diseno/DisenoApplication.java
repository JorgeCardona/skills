package patrones.diseno;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import patrones.diseno.adapter.*;
import patrones.diseno.bridge.*;
import patrones.diseno.decorator.AddMethodAbstractColorDecorator;
import patrones.diseno.decorator.AddMethodAbstractMessageDecorator;
import patrones.diseno.facade.FacadeProducer;
import patrones.diseno.facade.color.clases.ColorBlue;
import patrones.diseno.facade.color.interfaces.InterfaceColors;
import patrones.diseno.facade.messages.classes.MessageUno;
import patrones.diseno.facade.messages.interfaces.InterfaceMessage;
import patrones.diseno.proxy.Articles;
import patrones.diseno.proxy.InterfaceProxy;
import patrones.diseno.proxy.ProxyProducer;
import patrones.diseno.proxy.Stuffs;

import java.util.ArrayList;

@SpringBootApplication
public class DisenoApplication {


	// adiciona nuevo metodo al objeto sin cambiar la clase original
	public static void decoratorTest(){

		// colores
		InterfaceColors blue = new ColorBlue();

		InterfaceColors blueDecorated = new AddMethodAbstractColorDecorator(blue);

		System.out.println("Objeto normal");
		blue.color();

		System.out.println("Objeto con nueva funcionalidad");
		blueDecorated.color();

		System.out.println();

		// mensajes
		InterfaceMessage uno = new MessageUno();

		InterfaceMessage unoDecorated = new AddMethodAbstractMessageDecorator(uno);

		System.out.println("Objeto normal mensaje");
		uno.message();

		System.out.println("Objeto con nueva funcionalidad mensaje");
		unoDecorated.message();
	}

	// se obtiene la informacion del objeto sin concocer como instanciar ni nada del proceso
	public static void facadeTest(){

		FacadeProducer fp = new FacadeProducer();

		fp.getColor("Blue");
		fp.getColor("GREEN");
		fp.getColor("RED");
		fp.getColor("yelloW");

		fp.getMessage(null);
		fp.getMessage("UNo");
		fp.getMessage("dOs");
		fp.getMessage("TrEs");
		fp.getMessage("VACIO");

	}

	// usa un intermediador para el objeto que queremos trabajar
	public static void proxyTest(){

		System.out.println("---------------------------------------------------------");
		InterfaceProxy ip = new ProxyProducer(new Articles());
		System.out.println("accede a todos los metodos de la clase que esten inicializados en el constructor y la interface");
		ip.generate();

		System.out.println("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&");
		System.out.println("solo accede al metodo de la interface");
		ip.generate();

		System.out.println("---------------------------------------------------------");

		ip = new ProxyProducer(new Stuffs());
		System.out.println("accede a todos los metodos de la clase que esten inicializados en el constructor y la interface");
		ip.generate();
		System.out.println("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&");
		System.out.println("solo accede al metodo de la interface");
		ip.generate();
		System.out.println("---------------------------------------------------------");

	}

	// crea una interface que permite que se adapte a otra interface
	public static void adapterTest(){

		InterfaceAnimal gt = new Gato();
		System.out.println("Gato sonido");
		gt.sonido();

		InterfacePeluche ip = new GatoPeluche();
		System.out.println("Gato Peluche pitido");
		ip.pitido();

		InterfacePeluche ipa = new AdaptadorGato(gt);
		System.out.println("Gato Adaptador");
		ipa.pitido();

	}

	public static void bridgeTest(){


		AbstractTipoPastel fresaChan = new PastelFresa(new ComplementoChantilly());
		fresaChan.ordenarPastel();
		fresaChan.melocoton();// modificar a protected

		AbstractTipoPastel fresaCho = new PastelFresa(new ComplementoChocolate());
		fresaCho.ordenarPastel();

		AbstractTipoPastel fresaHel = new PastelFresa(new ComplementoHelado());
		fresaHel.ordenarPastel();

		AbstractTipoPastel meloChan = new PastelMelocoton(new ComplementoChantilly());
		meloChan.ordenarPastel();

		AbstractTipoPastel meloCho = new PastelMelocoton(new ComplementoChocolate());
		meloCho.ordenarPastel();

		AbstractTipoPastel meloHel = new PastelMelocoton(new ComplementoHelado());
		meloHel.ordenarPastel();

	}

	public static void main(String[] args) {
		SpringApplication.run(DisenoApplication.class, args);

		//facadeTest();
		//decoratorTest();
		//proxyTest();
		//adapterTest();
		bridgeTest();
	}

}
