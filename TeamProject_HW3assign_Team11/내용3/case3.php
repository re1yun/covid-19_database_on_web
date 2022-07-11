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
        $sql="select count(*) as num from case3;";
        $result = mysqli_query($link,$sql);
        $data = mysqli_fetch_assoc($result);
        print "<body>";
        print "<p><h3> Group_Affected_Twenties info table: (Currently " . $data['num'] . " group affected patients in database)</h3></p>";
        print "</body>";
    ?>
		
    	<table class = "table table-striped">
			<tr>
				<th>Province</th>
				<th>City</th>
				<th>Patient_id</th>
				<th>Age</th>
				<th>Infection_case</th>
				<th>University_count</th>
				<th>Infection_group</th>
			</tr>

			<?php
				$sql="select * from case3";
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