package AtividadeProcesso.View;

import AtividadeProcesso.Controller.RedesController;

public class Main {
    public static void main(String[] args) {
        RedesController redesController = new RedesController();
        System.out.println(redesController.ip());
    }
}
