class Lampada{
    constructor(_identificador, _tipo){
        this.identificador = _identificador;
        this.tipo = _tipo;
        this.estado = false;
    }

    getIdentificador(){
        return this.identificador;
    }

    setIdentificador(_identificador){
        this.identificador = _identificador;
    }

    getTipo(){
        return this.tipo;
    }

    setTipo(_tipo){
        this.tipo = _tipo;
    }

    acender(){
        this.estado = true;
    }

    apagar(){
        this.estado = false;
    }

    verEstado(){
        return this.estado;
    }
}


let lamp = new Lampada(1, "Led");

console.log(lamp.verEstado());

lamp.acender();

console.log(lamp.verEstado());

lamp.apagar();

console.log(lamp.verEstado());

console.log(lamp.getIdentificador());

lamp.setIdentificador(5);

console.log(lamp.getIdentificador());

console.log(lamp.getTipo());

lamp.setTipo("Fluorescente");

console.log(lamp.getTipo());