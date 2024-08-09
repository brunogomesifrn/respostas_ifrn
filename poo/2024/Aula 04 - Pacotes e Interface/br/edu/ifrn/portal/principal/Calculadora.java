package br.edu.ifrn.portal.principal;

import br.edu.ifrn.portal.interfaces.CalculadoraInterface;

public class Calculadora implements CalculadoraInterface{
    
    @Override
    public int soma(int num1, int num2){
        return num1+num2;
    }
    
}
