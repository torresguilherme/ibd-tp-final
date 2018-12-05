<?php
$servername = "localhost";
$username = "root";
$password = "vertrigo";
$dbname = "tpfinalibd";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
$conn->set_charset("utf8");

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
	$sql = "SELECT nome, tipo, pm, maintainer, basedOn FROM distro";
} else {
	$sql = "SELECT  nome, tipo, pm, maintainer, basedOn FROM distro LIMIT 6";
}

$result = $conn->query($sql);

if ($result->num_rows > 0) {
	echo "<table class='table table-striped distro'>  
		<thead>  
			<tr> 
				<th>Nome</th>
		    	<th>Tipo</th>  
			    <th>Package Manager</th>
				<th>Mantenedor</th>
				<th>Baseado em</th>
		  	</tr>
		</thead>
		<tbody>
			<tr>
				<td><input class='form-control distro_search' type='text' placeholder='Nome'></td>
				<td><input class='form-control distro_search' type='text' placeholder='Tipo'></td>
				<td><input class='form-control distro_search' type='text' placeholder='Package Manager'></td>
				<td><input class='form-control distro_search' type='text' placeholder='Mantenedor'></td>
				<td><input class='form-control distro_search' type='text' placeholder='Baseado em'></td>
			</tr>";

    // output data of each row
    while($row = $result->fetch_assoc()) {
	echo "<tr>  
		<td>".$row['nome']."</td>  
		<td>".$row['tipo']."</td>  
        <td>".$row['pm']."</td>
        <td>".$row['maintainer']."</td>	
        <td>".$row['basedOn']."</td>
  	</tr>";
    }

	if ($_SERVER['REQUEST_METHOD'] === 'POST') {
		echo "</tbody>
		</table>
		<div class='mostrar_todos'>
			<button type='button' id='mostrar_menos_distro' class='btn btn-primary'>
				<span>Mostrar menos</span>
			</button>
		</div>
		";
	} else {
		echo "</tbody>
		</table>
		<div class='mostrar_todos'>
			<button type='button' id='mostrar_distro' class='btn btn-primary'>
				<span>Mostrar todos os resultados</span>
			</button>
		</div>";
	}

} else {
    echo "Consulta sem resultados.";
}

$conn->close();
?>
