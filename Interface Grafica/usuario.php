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
	$sql = "SELECT idusuario, nome, sobrenome, idade, pais, genero, foto FROM usuario LIMIT 20000";
} else {
	$sql = "SELECT idusuario, nome, sobrenome, idade, pais, genero, foto FROM usuario LIMIT 9";
}

$result = $conn->query($sql);

if ($result->num_rows > 0) {
	echo "<table class='table table-striped usuario'>  
		<thead>  
			<tr> 	
					<th>Foto</th>
		    		<th>Nome</th>  
			    	<th>Sobrenome</th>
					<th>Idade</th>
					<th>País</th>
					<th>Gênero</th>
					
		  	</tr>
		</thead>
		<tbody>
			<tr>
				<td></td>
				<td><input class='form-control usuario_search' type='text' placeholder='Nome'></td>
				<td><input class='form-control usuario_search' type='text' placeholder='Sobrenome'></td>
				<td><input class='form-control usuario_search' type='text' placeholder='Idade'></td>
				<td><input class='form-control usuario_search' type='text' placeholder='País'></td>
				<td><input class='form-control usuario_search' type='text' placeholder='Gênero'></td>
			</tr>";

			
	// output data of each row
	while($row = $result->fetch_assoc()) {
		echo "<tr>  
		<td><img src='data:image/png;base64,".base64_encode($row['foto'])."'></td>
		<td>".$row['nome']."</td>  
		<td>".$row['sobrenome']."</td>
		<td>".$row['idade']."</td>
		<td>".$row['pais']."</td>
		<td>".$row['genero']."</td>
		</tr>";
	}

	if ($_SERVER['REQUEST_METHOD'] === 'POST') {
		echo "</tbody>
		</table>
		<div class='mostrar_todos'>
			<button type='button' id='mostrar_menos_usuario' class='btn btn-primary'>
				<span>Mostrar menos</span>
			</button>
		</div>
		";
	} else {
		echo "</tbody>
		</table>
		<div class='mostrar_todos'>
			<button type='button' id='mostrar_usuario' class='btn btn-primary'>
				<span>Mostrar todos os resultados</span>
			</button>
		</div>
		";
	}

} else {
    echo "Consulta sem resultados.";
}

$conn->close();
?>
