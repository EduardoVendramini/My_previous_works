package rechner;

public class Calc {
	static double rechner(double x, char op, double y) {
		double result=0;
		if(op=='+')
			result = x + y;
		else if(op=='-')
			result = x - y;
		else if(op=='*')
			result = x * y;
		else
			System.out.print("Error");
		return result;
	}
}
