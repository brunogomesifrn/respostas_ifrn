public class Categoria {
    private int identificador;
    private String nome;
    
    public Categoria(){
        
    }
    
    public Categoria(int identificador, String nome){
        this.identificador = identificador;
        this.nome = nome;
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
}
