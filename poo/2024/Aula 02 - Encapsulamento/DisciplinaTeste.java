import java.util.Scanner;

public class DisciplinaTeste {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Disciplina disciplina = new Disciplina();
        String opcao = "0";
        do{
            System.out.println("PROGRAMA DE DISCIPLINA");
            System.out.println("MENU:");
            System.out.println("1 - Criar o objeto");
            System.out.println("2 - Exibir média");
            System.out.println("3 - Sair");
            opcao = sc.nextLine();
            switch(opcao){
                case "1":
                    System.out.println("Digite o nome da disciplina:");
                    disciplina.setNome(sc.nextLine());
                    System.out.println("Digite a matrícula do aluno:");
                    disciplina.setMatricula(sc.nextLine());
                    System.out.println("Digite a nota 1:");
                    disciplina.setNota1(Double.parseDouble(sc.nextLine()));
                    System.out.println("Digite a nota 2:");
                    disciplina.setNota2(Double.parseDouble(sc.nextLine()));
                    System.out.println("Valeu! Agora vamos acessar os dados do objeto:");
                    System.out.println("Nome da disciplina: "+disciplina.getNome());
                    System.out.println("Matrícula do aluno: "+disciplina.getMatricula());
                    System.out.println("Nota 1: "+disciplina.getNota1());
                    System.out.println("Nota 2: "+disciplina.getNota2());
                    break;
                case "2":
                    System.out.println("A média entre "+disciplina.getNota1()+" e "+disciplina.getNota2()+" é "+disciplina.media());
                    break;
            }
        }while(!opcao.equalsIgnoreCase("3"));
    }
}
