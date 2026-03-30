/*
PROGRAMAÇÃO ORIENTADA A OBJETOS
- Paradigma de programação
- Utiliza o conceito da realidade
de Objetos (características e ações)
- A classe é a estrutura que se define
o objeto (atributos e funções)
- A partir da classe que os objetos
são criados/instanciados
*/

class Lampada{
    constructor(id, tipo){
        this.id = id;
        this.tipo = tipo;
        this.estado = false;
    }

    ligar(){
        this.estado = true;
    }

    desligar(){
        this.estado = false;
    }
}

let lamp_01 = new Lampada(1, 'LED');
console.log(lamp_01.id);
lamp_01.id = 5;
console.log(lamp_01.id);
console.log(lamp_01.tipo);
console.log(lamp_01.estado);

lamp_01.ligar();
console.log(lamp_01.estado);

lamp_01.desligar();
console.log(lamp_01.estado);