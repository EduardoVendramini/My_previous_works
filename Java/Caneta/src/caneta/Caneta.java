package caneta;

public class Caneta {
	String modelo;
	String cor;
	float ponta;
	int carga;
	private boolean tampada = false;
	
	void rabiscar() {
		
	}
	void tampar() {
		this.tampada = true;
	}
	void destampar() {
		this.tampada = false;
	}
	void status() {
		System.out.println("cor = " + this.cor);
		System.out.println("tampada? " + this.tampada);
	}
	
}
