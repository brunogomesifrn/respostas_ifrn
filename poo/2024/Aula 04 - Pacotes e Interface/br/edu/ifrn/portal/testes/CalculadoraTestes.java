package br.edu.ifrn.portal.testes;

import br.edu.ifrn.portal.principal.Calculadora;

public class CalculadoraTestes {
    public static void main(String args[]){
        Calculadora calc = new Calculadora();
        System.out.println(calc.soma(10, 5));
    }
}
