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

        $sql="select count(*) as num from timeinfo;";
        $result = mysqli_query($link,$sql);
        $data = mysqli_fetch_assoc($result);
        print "<body>";
        print "<p><h3> Time Info table (Currently " . $data['num'] . " datas in database)</h3></p>";
        print "</body>";
    ?>

    <table class = "table table-striped">
		<tr>
			<th>Date</th>
			<th>Test</th>
			<th>Negative</th>
			<th>Confirmed</th>
			<th>Released</th>
			<th>Deceased</th>
		</tr>

		<?php
			$sql="select * from timeinfo;";
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