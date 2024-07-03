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
        
        $praia = $_POST["praia"];

        if($praia == "barra"){
            echo "<h1>Barra do Cunhaú</h1>";
            echo "<p><img src='barra.jpg' alt='Imagem da praia de Barra do Cunhaú' /></p>";
        } else {
            if($praia == "baia"){
                echo "<h1>Baía Formosa</h1>";
                echo "<p><img src='baia.jpg' alt='Imagem da praia de Baía Formisa' /></p>"; 
            } else {
                if($praia == "pipa"){
                    echo "<h1>Pipa</h1>";
                    echo "<p><img src='pipa.jpg' alt='Imagem da praia de Pipa' /></p>";
                }
            }
        }
        
    ?>
</body>
</html>