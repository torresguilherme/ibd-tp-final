<?php
$servername = "localhost";
$username = "root";
$password = "vertrigo";
$dbname = "tpfinalibd";

function getFieldName($field) {
	switch ($field) {
		case "nome":
			$field_name = "Nome";
			break;
		case "sobrenome":
			$field_name = "Sobrenome";
			break;
		case "idusuario":
			$field_name = "ID";
			break;
		case "idade":
			$field_name = "Idade";
			break;
		case "foto":
			$field_name = "Foto";
			break;
		case "pais":
			$field_name = "País";
			break;
		case "usoProfissional":
			$field_name = "Uso";
			break;
		case "genero":
			$field_name = "Gênero";
			break;
		case "distro":
			$field_name = "Distro";
			break;
		case "valor":
			$field_name = "Valor";
			break;
		case "desktop":
			$field_name = "Desktop";
			break;
		case "nomeDistro":
			$field_name = "Nome da Distro";
			break;
		case "arch":
			$field_name = "Arquitetura";
			break;
		case "pm":
			$field_name = "Package Manager";
			break;
		case "maintainer":
			$field_name = "Mantenedor";
			break;
		case "basedOn":
			$field_name = "Baseado em";
			break;
		case "tipo":
			$field_name = "Tipo";
			break;
		case "fm":
			$field_name = "File Manager";
			break;
		case "docViewer":
			$field_name = "Doc Viewer";
			break;
		case "imageViewer":
			$field_name = "Image Viewer";
			break;
		case "terminal":
			$field_name = "Terminal";
			break;
		default:
			$field_name = "";
	}

	return $field_name;
}

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
$conn->set_charset("utf8");

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$commands = array("create", "alter", "drop", "insert","update", "delete", "set", "show", "help", "grant", "revoke", "start", "transaction", "savepoint", "commit", "rollback");

$sql = $_POST['query'];

$matches = array();
$match_found = preg_match_all(
              	"/\b(" . implode($commands,"|") . ")\b/i", 
                $sql, 
                $matches
              );

if($match_found){
	echo "denied";
} else {

	$result = $conn->query($sql);
	
	
	if($result){
		if ($result->num_rows > 0) {
		
			$fields = array();
			while ($field_info = mysqli_fetch_field($result)){
				array_push($fields, getFieldName($field_info->name));
			}

			echo "<div class='col-lg-12 nova_consulta mostrar_todos'>
					<button type='button' id='nova_consulta' class='btn btn-primary'>
						<span>Realizar Nova Consulta</span>
					</button>
				</div>
				<table class='table table-striped consulta'>  
				<thead>  
					<tr>"; 
						for($index = 0; $index < mysqli_num_fields($result); $index++){
							echo "<th>" . $fields[$index] . "</th>";
						}

				  	echo "</tr>
				</thead>
				<tbody>
					<tr>";
						for($index = 0; $index < mysqli_num_fields($result); $index++){
							echo "<td><input class='form-control consulta_search' type='text' placeholder='" 
								. $fields[$index] . "'></td>";								
						}
					echo "</tr>";

			// output data of each row
			$index = 0;
			while($row = $result->fetch_array(MYSQLI_NUM)) {
				echo "<tr>";
			
				for($index = 0; $index < mysqli_num_fields($result); $index++){
					echo "<td>".$row[$index]."</td>";
				}
			
				echo "</tr>";
			}

		} else {
		    echo "no_results";
		}
	} else {
		echo "Erro: " . $conn->error;
	}
}

$conn->close();

?>
