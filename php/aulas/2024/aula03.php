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

    /*
    ESTRUTURAS DE CONTROLE:
    - Estrutura Sequêncial
    - Estrutura de condição
    - Estrutura de repetição
    */

    /*
    ESTRUTURA DE CONDIÇÃO
    - if
    - if...else
    */

    $numero = 5;
    if($numero>0){
        echo "<p> Número Positivo </p>";
    }

    /*
    Se no bloco da estrutura possuir
    apenas uma instrução, as chaves
    são opcionais
    */

    if($numero>0)
        echo "<p> Número positivo </p>";
    

    if($numero>=0){
        echo "<p> Número positivo </p>";
    }else{
        echo "<p> Número negativo </p>";
    }

    /*
    Utilizando a estrutura if...else, 
    armazene um valor inteiro em uma
    variável. Logo em seguida, imprima
    na página em título de nível 2 se
    o número é POSITIVO, NEGATIVO ou NULO. 
    */

    // POSSIBILIDADE 1
    $num = 15;
    if($num>0){
        echo "<h2>Positivo</h2>";
    }
    if($num<0){
        echo "<h2>Negativo</h2>";
    }
    if($num==0){
        echo "<h2>Nulo</h2>";
    }

    // Possibilidade 2
    if($num>0){
        echo "<h2>Positivo</h2";
    }else{
        if($num<0){
            echo "<h2>Negativo</h2>";
        }else{
            if($num==0){
                echo "<h2>Nulo</h2>";
            }
        }
    }

    // Possibilidade 3
    if($num>0)
        echo "<h2>Positivo</h2";
    else if($num<0)
            echo "<h2>Negativo</h2>";
        else
                echo "<h2>Nulo</h2>";
    ?>
</body>
</html>