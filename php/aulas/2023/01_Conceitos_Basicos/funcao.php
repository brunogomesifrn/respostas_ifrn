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
    FUNÇÃO
    */

    function impressao(){
        echo "<h1>IFRN</h1>";
    }

    impressao();

    function nome(){
        return "<h1>Canguaretama</h1>";
    }

    echo nome();

    
    function instituto($nome){
        echo $nome;
    }

    instituto("<h2>IFPB</h2>");


    function soma($valor1, $valor2){
        return $valor1+$valor2;
    }

    echo "<p>".soma(5,3)."</p>";

    

    ?>
</body>
</html>