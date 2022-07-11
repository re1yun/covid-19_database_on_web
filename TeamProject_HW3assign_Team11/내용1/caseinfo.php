<html>

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

	<h1 style="text-align:center;">
        <strong>
            Database TeamProject Team11
        </strong>
    </h1>

	<hr style = "width: 100%; border: 8px solid #81c147;">
	</hr>

	<?php  
        require_once 'dbconfig.php';

        $sql="select count(*) as num from caseinfo;";
        $result = mysqli_query($link,$sql);
        $data = mysqli_fetch_assoc($result);
        print "<body>";
        print "<p><h3> Case Info table (Currently " . $data['num'] . " cases in database)</h3></p>";
        print "</body>";
    ?>

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
			$sql="select * from caseinfo;";
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

</html>