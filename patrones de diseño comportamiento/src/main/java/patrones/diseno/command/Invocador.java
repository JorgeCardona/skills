package patrones.diseno.command;

import java.util.ArrayList;

public class Invocador {

    private ArrayList<InterfaceCommand> interfaceCommandsList = new ArrayList<>();

    public void createProccess(InterfaceCommand interfaceCommands){

        interfaceCommandsList.add(interfaceCommands);
    }

    public void commands(){

        for (InterfaceCommand ifc : interfaceCommandsList) {
            ifc.ejecutar();
        }
        interfaceCommandsList.clear();
    }
}
