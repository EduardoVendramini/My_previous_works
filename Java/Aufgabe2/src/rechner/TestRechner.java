package rechner;

import static org.junit.Assert.*;

import org.junit.Test;


public class TestRechner {

	@Test
	public void testRechnungen() {
		double x = Calc.rechner(1.0, '+', 1.0);
		assertTrue(x==(float)2.0);
		x = Calc.rechner(1.0, '*', 1.0);
		assertTrue(x==(float)1.0);
		x = Calc.rechner(1.0, '-', 1.0);
		assertTrue(x==(float)0.0);
	}

}
