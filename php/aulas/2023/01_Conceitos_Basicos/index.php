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
        echo "<p>Olá Mundo</p>";

        // Comentário em 1 linha

        /*
        Comentário em 
        várias linhas
        */

        /* VARIÁVEIS 
        - PHP é fracamente tipado, ou seja,
        não é preciso informar o tipo
        da variável (o tipo de dado que
        será armazenado);
        - É necessário utilizar o $ antes
        do nome da variável.
        */
        $idade = 30;
        $nota = 8.5;
        $instituto = "Canguaretama";
        $aprovado = TRUE;

        echo "<p>";
        echo $idade;
        echo "</p>";

        echo "<p>".$idade."</p>";

        echo "<p> $idade </p>";

        /*
        OPERADORES ARITMÉTICOS
        + soma
        - subtração
        * multiplicação
        / divisão
        */ 

        $nota1 = 80;
        $nota2 = 70;
        $media = ($nota1+$nota2)/2;
        echo "<p>A média é $media</p>";

        /* 
        OPERADORES CONDICIONAIS/COMPARAÇÃO
        > maior que
        >= maior ou igual a
        < menor que
        <= menor ou igual a
        == igual a
        != diferente de
        */

        echo "<p>".(10 > 1)."</p>";
        echo "<p>".(5 >= 10)."</p>";
        echo "<p>".(5 != 10)."</p>";

        /*
        OPERADORES LÓGICOS

        && e
        || ou
        ! não
        */

        echo "<p>".((10>5)&&(5<4))."</p>";
        echo "<p>".((10>5)||(5<4))."</p>";
        echo "<p>".(!(10>5))."</p>";

    ?>
</body>
</html>