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
        // OPERADORES

        /*
        OPERADORES ARITMÉTICOS
        + soma
        - subtração
        * multiplicação
        / divisão
        % resto da divisão

        obs.: Sempre retorna número
        */

        /*
        Armazene um número qualquer em uma variável,
        posteriormente imprima na página HTML em
        título de nível 1 o dobro do número armazenado.
        */

        $numero = 30;
        echo "<h1>".($numero*2)."</h1>";

        $dobro = $numero*2;
        echo "<h1>".$dobro."</h1>";

        echo "<h1> $dobro </h1>";

        /*
        Armazene dois valores reais em duas variáveis.
        Posteriormente, imprima na página HTML em 
        parágrafo a média aritmética entre os dois 
        números armazenados.
        */

        $num1 = 9.5;
        $num2 = 5.6;
        $media = ($num1+$num2)/2;
        echo "<p> $media </p>";

        /*  
        OPERADORES CONDICIONAIS
        < menor que
        <= menor ou igual a
        > maior que
        >= maior ou igual a
        == igual (valor)
        === igual (valor e tipo)
        != diferente (valor)
        !== diferente (valor e tipo)

        Obs.: retornam valor booleano 
        True ou False
        */

        echo "<p>".(10>5)."</p>";
        echo "<p>".(10<5)."</p>";

        echo "<p>".(10>10)."</p>";
        echo "<p>".(10>=10)."</p>";

        echo "<p>".(10==10)."</p>";
        
        echo "<p>".(10==10.0)."</p>";
        echo "<p>".(10===10.0)."</p>";

        /*
        OPERADORES LÓGICOS

        || ou
        && e
        ! negação

        Obs.: retornam valor booleano
        */
        
        echo "<p>".((10==10) || (5>7))."</p>";
        
        echo "<p>".((10==10) && (5>7))."</p>";
        
        echo "<p>".(!(5>7))."</p>";
        
    ?>
</body>
</html>