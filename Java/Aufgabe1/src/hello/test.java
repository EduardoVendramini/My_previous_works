package hello;

import static org.junit.Assert.*;

import org.junit.Test;

public class test {

	@Test
	public void testHello() {
		Hallo test = new Hallo();
		assertEquals("hello", test.printhello());
	}
}
