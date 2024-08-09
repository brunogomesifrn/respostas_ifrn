public class Lampada {
    private int identificador;
    private String tipo;
    private String estado;
    
    // Construtores
    
    // Construtor Vazio
    public Lampada(){
        this.estado = "Apagada";
    }
    
    // Construtor Parametrizado
    public Lampada(int identificador, String tipo){
        this.identificador = identificador;
        this.tipo = tipo;
        this.estado = "Apagada";
    }
    
    
    
    public void acender(){
        this.estado = "Acender";
    }
    
    public void apagar(){
        this.estado = "Apagar";
    }
    
  
    // Encapsulamento - GET e SET
    
    public int getIdentificador(){
        return this.identificador;
    }
    
    public void setIdentificador(int identificador){
        this.identificador = identificador;
    }
    
    public String getTipo(){
        return this.tipo;
    }
    
    public void setTipo(String tipo){
        this.tipo = tipo;
    }
    
    public String getEstado(){
        return this.estado;
    }
    
    public void setEstado(String estado){
        this.estado = estado;
    }
    
    public String toString(){
        return "ID: "+this.identificador+" Tipo: "+this.tipo;
    }
    
}