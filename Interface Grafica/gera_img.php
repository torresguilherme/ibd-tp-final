<?
//CONECTA
AO MYSQL 
$conn = mysqli_connect("localhost", "root",
"vertrigo", "tpfinalibd");

$cod = $_GET["codigo"];
//EXIBE
$sql = "SELECT foto FROM usuario WHERE idusuario = ".$cod."";
$query = mysql_query($sql) or die("Impossível executar a query");
$row = mysql_fetch_array($query);

header("Content-type: image/png", true);
echo $row["foto"];

?>