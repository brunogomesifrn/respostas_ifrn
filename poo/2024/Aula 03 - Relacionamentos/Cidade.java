
public class Cidade {
    private int identificador;
    private String nome;
    private Estado estado;
    
    public Cidade(){
        
    }
    
    public Cidade(int identificador, String nome, Estado estado){
        this.identificador = identificador;
        this.nome = nome;
        this.estado = estado;
    }
    
    public int getIdentificador(){
        return this.identificador;                
    }
    
    public void setIdentificador(int identificador){
        this.identificador = identificador;
    }
    
    public String getNome(){
        return this.nome;
    }
    
    public void setNome(String nome){
        this.nome = nome;
    }
    
    public Estado getEstado(){
        return this.estado;
    }
    
    public void setEstado(Estado estado){
        this.estado = estado;
    }
}
