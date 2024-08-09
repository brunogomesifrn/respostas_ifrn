public class Estado {
    private int identificador;
    private String sigla;
    
    public Estado(){
        
    }
    
    public Estado(int identificador, String sigla){
        this.identificador = identificador;
        this.sigla = sigla;
    }
    
    public int getIdentificador(){
        return this.identificador;
    }
    
    public void setIdentificador(int identificador){
        this.identificador = identificador;
    }
    
    public String getSigla(){
        return this.sigla;
    }
    
    public void setSigla(String sigla){
        this.sigla = sigla;
    }

}
