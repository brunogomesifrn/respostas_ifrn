public class Disciplina {
    private String nome;
    private String matricula;
    private double nota1;
    private double nota2;
    
    public Disciplina(){
        
    }
    
    public Disciplina(String nome, String matricula, double nota1, double nota2){
        this.nome = nome;
        this.matricula = matricula;
        this.nota1 = nota1;
        this.nota2 = nota2;
    }
    
    public double media(){
        return ((this.nota1+this.nota2)/2);
    }
    
    public String getNome(){
        return this.nome;
    }
    
    public String getMatricula(){
        return this.matricula;
    }
    
    public double getNota1(){
        return this.nota1;
    }
    
    public double getNota2(){
        return this.nota2;
    }
    
    public void setNome(String nome){
        this.nome = nome;
    }
    
    public void setMatricula(String matricula){
        this.matricula = matricula;
    }
    
    public void setNota1(double nota1){
        this.nota1 = nota1;
    }
    
    public void setNota2(double nota2){
        this.nota2 = nota2;
    }
}
