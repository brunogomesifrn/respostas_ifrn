public class TesteLampada {
    public static void main(String args[]){
        Lampada lampada1 = new Lampada();
        
        lampada1.setIdentificador(2);
        lampada1.setTipo("Fluorescente");
        
        System.out.println(lampada1.getIdentificador());
        System.out.println(lampada1.getTipo());
        System.out.println(lampada1.getEstado());
        
        
        System.out.println(lampada1.getEstado());
        lampada1.acender();
        System.out.println(lampada1.getEstado());
        lampada1.apagar();
        System.out.println(lampada1.getEstado());
        
        Lampada lampada2 = new Lampada(1, "Led");
        
        Lampada lampada3 = new Lampada(3, "Led");
        lampada3.acender();
        System.out.println(lampada3.getIdentificador());
        System.out.println(lampada3.getTipo());
        System.out.println(lampada3.getEstado());
        
        Lampada lampada4 = new Lampada();
        lampada4.setIdentificador(4);
        lampada4.setTipo("Fluorescente");
        System.out.println(lampada4.getIdentificador());
        System.out.println(lampada4.getTipo());
        System.out.println(lampada4.getEstado());
        
        System.out.println(lampada4);
        
        
        /*
        
        
        */
        
        
        
    }
}