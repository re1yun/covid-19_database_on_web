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
				wdate를 선택하세요.
			</legend>
			<select name = "search", id = "search">
				<?php
					$sql = "select distinct wdate from weather order by wdate asc;";
					$result = mysqli_query($link, $sql);
					while($row = mysqli_fetch_assoc($result)){
						if($_POST['search'] == $row['wdate']){
							echo '<option value ="' . $row['wdate'] . '" selected>' . $row['wdate'] . '</option>';
						}
						else{
							echo '<option value ="' . $row['wdate'] . '">' . $row['wdate'] . '</option>';	
						}
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
			$state = isset($_POST['search']) ? $_POST['search'] :'20000101';
        	$sql="select count(*) as num from weather where wdate = \"" . $state . "\";";
        	$result = mysqli_query($link,$sql);
        	$data = mysqli_fetch_assoc($result);
        	//print "<body>";
        	print "<p><h3> Weather Info table (Currently " . $data['num'] . " weather in database)</h3></p>";
        	//print "</body>";
    	?>

    	<table class = "table table-striped">
			<tr>
				<th>Region_code</th>
				<th>Province</th>
				<th>Date</th>
				<th>Avg_temp</th>
				<th>Min_temp</th>
				<th>Max_temp</th>
			</tr>

			<?php
				$state = isset($_POST['search']) ? $_POST['search'] :'20000101';
				$sql="select * from weather where wdate = \"" . $state . "\";";
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