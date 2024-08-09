
public class TesteContaBanco {
    public static void main(String[] args) {
        ContaBanco conta1 = new ContaBanco(156);
        conta1.depositar(100);
        conta1.depositar(50);
        System.out.println(conta1.getSaldo());
        conta1.sacar(30);
        System.out.println(conta1.getSaldo());
        conta1.sacar(15);
        System.out.println(conta1.getSaldo());
    }
}
