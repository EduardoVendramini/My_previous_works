package caneta;

public class Main {
	public static void main(String[] args) {
		Caneta c1 = new Caneta();
		c1.cor = "azul";
		c1.carga = 90;
		c1.ponta = (float) 0.5;
		c1.status();
		c1.tampar();
		c1.status();

	}
}
