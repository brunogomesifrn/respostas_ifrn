let nome = require("./mod_variavel");
console.log(nome);

let inst = require("./mod_funcao_01");
console.log(inst());

let sigla = require("./mod_funcao_02");
sigla();

let sum = require("./mod_funcao_03");
let resultado = sum(10, 5);
console.log(resultado);

let cidade = require("./mod_funcao_04");
console.log(cidade());

let campus = require("./mod_funcao_05");
console.log(campus());

let camp = require("./mod_funcao_06");
console.log(camp.nome());

let cursos = require("./mod_funcoes_01");
console.log(cursos.curso1());
console.log(cursos.curso2());
console.log(cursos.curso3());

let campi = require("./mod_funcoes_02");
console.log(campi.campus1());
console.log(campi.campus2());
console.log(campi.campus3());