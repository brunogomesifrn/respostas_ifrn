<?php
//https://www.w3schools.com/php/php_mysql_connect.asp

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "aula_01";
//$port = 3306

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

//echo "Connected successfully";


//$conn->close(); 
?> 