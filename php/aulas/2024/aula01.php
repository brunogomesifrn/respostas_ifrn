<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        // echo serve para imprimir
        echo "<p>Olá Mundo</p>";

        /*
        Linguagens do lado do
        servidor sempre geram
        código HTML! Não esqueçam :D
        */

        /*
        VARIÁVEL
        - Armazenamento temporário
        de dados
        - PHP é fracamente tipada, 
        ou seja, não é necessário
        informar o tipo do dado que
        será armazenado
        - Utiliza $ no nome da variável
        */

        $idade = 30;
        $nota = 8.5;
        $nome = "IFRN";
        $valor = true;
        
        echo "<h1>";
        echo $nome;
        echo "</h1>";
        
        // O operador de concatenação é .
        echo "<p>A idade é:".$idade."</p>";
        /*
        Utilizando o operador echo
        não é necessário concatenar
        variáveis com texto, ele 
        reconhece a variável mesmo
        que esteja dentro das aspas.
        */
        echo "<p>A nota é $nota </p>";

        /*
        OPERADORES ARITMÉTICOS
        + soma
        - subtração
        * multiplicação
        / divisão
        % resto da divisão

        Obs.: SEMPRE RETORNAM VALOR NUMÉRICO
        */

        /*
        Armazene um valor inteiro qualquer
        em uma variável. Logo após imprima
        o dobro deste número armazenado!
        */
        //possibilidade 1
        $numero = 10;
        echo "<p>".($numero*2)."</p>";

        //possibilidade 2
        echo "<p>O dobro de $numero é".($numero*2)."</p>";

        //possibilidade 3
        $dobro = $numero*2;
        echo "<p>O dobro de $numero é $dobro </p>";



    ?>
</body>
</html>