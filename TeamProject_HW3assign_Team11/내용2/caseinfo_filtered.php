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
			<fieldset style = "border: 0px;">
				<legend>
					province를 선택하세요.
				</legend>
				<select name = "search", id = "search">
					<?php
						$sql = "select distinct province from caseinfo order by province asc;";
						$result = mysqli_query($link, $sql);
						while($row = mysqli_fetch_assoc($result)){
							if($_POST['search'] == $row['province']){
								echo '<option value ="' . $row['province'] . '"selected = selected>' . $row['province'] . '</option>';
							}
							else{
								echo '<option value ="' . $row['province'] . '">' . $row['province'] . '</option>';	
							}
							//<option value = "\"". $row['id'] ."\""> "\"" . $row['state'] . "\"" </option>
						}
						?>
				</select>
				<input type = "submit" value = "submit1"/>
			</fieldset>

			<?php
			$state = isset($_POST['search']) ? $_POST['search'] :'';
        	$sql="select count(*) as num from caseinfo where province = \"" . $state . "\";";
        	$result = mysqli_query($link,$sql);
        	$data = mysqli_fetch_assoc($result);
        	//print "<body>";
        	print "<p><h3> Case Info table (Currently " . $data['num'] . " cases in database which province is " . $state . ")</h3></p>";
        	//print "</body>";
    		?>
			
			<fieldset style = "border: 0px;">
				<?php
					$state = isset($_POST['search']) ? $_POST['search'] :'';
					print "" . $state . "지역의 감염 케이스들 중 확진자 수를 알고싶은 케이스를 선택하세요.<br><br>";
				?>
				<select name = "search2", id = "search2">
					<?php
						$state = isset($_POST['search']) ? $_POST['search'] :'';
						$sql = "select distinct infection_case from caseinfo where province = \"" . $state . "\"order by infection_case asc;";
						$result = mysqli_query($link, $sql);
						while($row = mysqli_fetch_assoc($result)){
							if($_POST['search2'] == $row['infection_case']){
								echo '<option value ="' . $row['infection_case'] . '"selected = selected>' . $row['infection_case'] . '</option>';
							}
							else{
								echo '<option value ="' . $row['infection_case'] . '">' . $row['infection_case'] . '</option>';	
							}
						}
					?>
				</select>
				<input type = "submit" value = "submit2"/>
			</fieldset>

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
		
    	<table class = "table table-striped">
			<tr>
				<th>Case_id</th>
				<th>Province</th>
				<th>City</th>
				<th>Infection_group</th>
				<th>Infection_case</th>
				<th>Confirmed</th>
				<th>Latitude</th>
				<th>Longitude</th>
			</tr>

			<?php
				$state = isset($_POST['search']) ? $_POST['search'] :'';
				$state2 = isset($_POST['search2']) ? $_POST['search2'] :'';
				$sql="select * from caseinfo where province = \"" . $state . "\" and infection_case = \"" . $state2 . "\";";
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