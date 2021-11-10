package patrones.diseno;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import patrones.diseno.ChainOfResponsability.Asignador;
import patrones.diseno.command.*;
import patrones.diseno.strategy.Contexto;
import patrones.diseno.strategy.Multiplicar;
import patrones.diseno.strategy.Restar;
import patrones.diseno.strategy.Sumar;
import patrones.diseno.template.AbstractTemplate;
import patrones.diseno.template.ComidaChina;
import patrones.diseno.template.ComidaItaliana;

@SpringBootApplication
public class DisenoApplication {


	// crea una interface que permite que se adapte a otra interface
	public static void commandTest(){

		Lampara lampara = new Lampara();
		Auto auto = new Auto();
		InterfaceCommand objetoLampara;
		InterfaceCommand objetoAuto;
		Invocador invocador = new Invocador();

		for (int i = 0; i < 5; i++) {

			if(i%2 == 0){
				objetoLampara = new EncenderLampara(lampara);
				objetoAuto = new ApagarAuto(auto);
				invocador.createProccess(objetoLampara);
				invocador.createProccess(objetoAuto);
			} else {
				objetoAuto = new EncenderAuto(auto);
				objetoLampara = new ApagarLampara(lampara);
				invocador.createProccess(objetoLampara);
				invocador.createProccess(objetoAuto);
			}
		}
		invocador.commands();
	}

	// para usar diferentes algoritmos de logica de negocio
	public static void strategyTest(){

		Contexto contextoSumar = new Contexto(new Sumar());
		Contexto contextoRestar = new Contexto(new Restar());
		Contexto contextoMultiplicar = new Contexto(new Multiplicar());

		System.out.println("10 + 5 = " + contextoSumar.ejecutarCalculo(10, 5));
		System.out.println("20 - 7 = " + contextoRestar.ejecutarCalculo(20, 7));
		System.out.println("20 / 2 = " + contextoMultiplicar.ejecutarCalculo(20, 2));

	}

	public static void templateTest() {

		AbstractTemplate comidaChina = new ComidaChina();
		comidaChina.visitarRestaurante();
		System.out.println("-----------------------");
		AbstractTemplate comidaItaliana = new ComidaItaliana();
		comidaItaliana.visitarRestaurante();
	}

	public static void chainOfResponsabilityTest() {

		Asignador asignador = new Asignador();
		asignador.calcularGrupo(43);
		asignador.calcularGrupo(-1);
		asignador.calcularGrupo(0);
		asignador.calcularGrupo(126);
		asignador.calcularGrupo(67);
		asignador.calcularGrupo(28);

	}

	public static void main(String[] args) {
		SpringApplication.run(DisenoApplication.class, args);

		chainOfResponsabilityTest();
	}

}
