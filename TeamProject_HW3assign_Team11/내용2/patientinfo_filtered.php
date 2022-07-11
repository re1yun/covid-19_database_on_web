<html>
	<head>
		<?php
			require_once 'dbconfig.php';
		?>

		<h1 style="text-align:center;">
        	<strong>
	            Database TeamProject Team11
        	</strong>
    	</h1>

		<hr style = "width: 100%; border: 8px solid #81c147;">
		</hr>
	</head>
	<body>



		<form method = "post">
			<legend>
				state를 선택하세요.
			</legend>
			<select name = "search", id = "search">
				<?php
					$sql = "select distinct state from patientinfo;";
					$result = mysqli_query($link, $sql);
					while($row = mysqli_fetch_assoc($result)){
						if($_POST['search'] == $row['state']){
							echo '<option value ="' . $row['state'] . '" selected>' . $row['state'] . '</option>';
						}
						else{
							echo '<option value ="' . $row['state'] . '">' . $row['state'] . '</option>';	
						}
						//<option value = "\"". $row['id'] ."\""> "\"" . $row['state'] . "\"" </option>
					}
					?>
			</select>
			<input type = "submit" value = "load"/>
		</form>


		<style>
			table{
				width: 100%;
				border: 1px solid #444444;
				border-collapse: collapse;
			}
			th, td {
				border: 1px solid #444444;
			}	
		</style>

		

		<?php
			$state = isset($_POST['search']) ? $_POST['search'] :'';
        	$sql="select count(*) as num_patientinfo from patientinfo where state = \"" . $state . "\";";
        	$result = mysqli_query($link,$sql);
        	$data = mysqli_fetch_assoc($result);
        	//print "<body>";
        	print "<p><h3> Patient Info table (Currently " . $data['num_patientinfo'] . " patients in database)</h3></p>";
        	//print "</body>";
    	?>

    	<table class = "table table-striped">
			<tr>
				<th>Patient_id</th>
				<th>Sex</th>
				<th>Age</th>
				<th>Country</th>
				<th>Province</th>
				<th>City</th>
				<th>Infection_case</th>
				<th>Infected_by</th>
				<th>Contact_number</th>
				<th>Symptom_onset_date</th>
				<th>Confirmed_date</th>
				<th>Released_date</th>
				<th>Deceased_date</th>
				<th>State</th>
			</tr>

			<?php
				$state = isset($_POST['search']) ? $_POST['search'] :'';
				$sql="select * from patientinfo where state = \"" . $state . "\";";
				$result = mysqli_query($link, $sql);
				while($row = mysqli_fetch_assoc($result)) {
					print "<tr>";
					foreach ($row as $key => $val){
						print "<td>" . $val . "</td>";
					}
					print "</tr>";
				}
			?>
		</table>
	</body>
</html>