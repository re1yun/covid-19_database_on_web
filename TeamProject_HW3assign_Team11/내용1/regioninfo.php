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

        $sql="select count(*) as num from region;";
        $result = mysqli_query($link,$sql);
        $data = mysqli_fetch_assoc($result);
        print "<body>";
        print "<p><h3> Region table (Currently " . $data['num'] . " regions in database)</h3></p>";
        print "</body>";
    ?>

    <table class = "table table-striped">
		<tr>
			<th>Region_code</th>
			<th>Province</th>
			<th>City</th>
			<th>Latitude</th>
			<th>Longitude</th>
			<th>Elementry_school_count</th>
			<th>Kindergarten_count</th>
			<th>University_count</th>
			<th>Academy_ratio</th>
			<th>Elderly_population_ratio</th>
			<th>Elderly_alone_ratio</th>
			<th>Nursing_home_count</th>
		</tr>

		<?php
			$sql="select * from region;";
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