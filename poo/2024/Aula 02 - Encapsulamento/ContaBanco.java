
public class ContaBanco {
    private int numero;
    private double saldo;
    
    public ContaBanco(int numero){
        this.numero = numero;
        this.saldo = 0;
    }
    
    public void sacar(double valor){
        this.saldo = this.saldo - valor;
    }
    
    public void depositar(double valor){
        this.saldo = this.saldo + valor;
    }
    
    public double getSaldo(){
        return this.saldo;
    }
    
}
