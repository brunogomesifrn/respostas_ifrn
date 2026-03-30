/*
POO RAIZ
*/

class Lampada{

    #id;
    #tipo;
    #estado;

    constructor(id, tipo){
        this.#id = id;
        this.#tipo = tipo;
        this.#estado = false;
    }

    get getId(){
        return this.#id;
    }

    set setId(id){
        this.#id = id;
    }
    
    get getTipo(){
        return this.#tipo;
    }

    ligar(){
        this.#estado = true;
    }

    desligar(){
        this.#estado = false;
    }

    get getEstado(){
        return this.#estado;
    }
}

let lamp_01 = new Lampada(1, "LED");
console.log(lamp_01.getId);
lamp_01.setId = 5;
console.log(lamp_01.getId);

lamp_01.id = 10; // NÃO FUNCIONA
console.log(lamp_01.id); // undefined
console.log(lamp_01.getId);

lamp_01.ligar();
console.log(lamp_01.estado); // undefined
console.log(lamp_01.getEstado);