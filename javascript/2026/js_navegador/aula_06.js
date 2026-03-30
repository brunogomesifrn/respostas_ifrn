/*
OBJETO EM JS
- É uma estrutura que possui
atributos/propriedades
- Semelhante a dicionário de dados
em outras linguagens
*/

let disciplina = {
    nome: "Des. Web. para Disp. Móveis",
    sigla: "DWDM",
    ch: 4,
    alunos: ["Aluno1", "Aluno2", "Aluno3"]
}
console.log(disciplina.nome);
console.log(disciplina.ch);
console.log(disciplina.alunos[1]);

let {nome, sigla, ch, alunos} = disciplina;
console.log(sigla);

/*
let nome = disciplina.nome;
let sigla = disciplina.sigla;

*/

