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
            Put Hospital_id.
         </legend>
            <input type = "text" name = "search" id = "search" value = "<?php echo isset($_POST['search']) ? $_POST['search'] : ''; ?>"/>
         <input type = "submit" value = "load"/>
      </form>


      <style>
         table{
            width: 100%;
            border: 1px solid #444444;
            border-collapse: collapse;
         }
         th {
            border: 1px solid #444444;
         }
         td {
            border: 1px solid #444444;
         }   
      </style>

      

      <?php
         $state = isset($_POST['search']) ? $_POST['search'] :'';
           $sql="select count(*) as num_patientinfo from patientinfo where hospital_id = \"" . $state . "\";";
           $result = mysqli_query($link,$sql);
           $data = mysqli_fetch_assoc($result);
           print "<p><h3> Hospital Info table (Currently " . $data['num_patientinfo'] . ") cases in database which hospital_id is 1 ~ 43</h3></p>";
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
                <th>Hospital_id
            </th>
         </tr>

         <?php
            $state = isset($_POST['search']) ? $_POST['search'] :'';
            $sql="select * from patientinfo where hospital_id = \"" . $state . "\";";
            $result = mysqli_query($link, $sql);
            while($row = mysqli_fetch_assoc($result)) {
               print "<tr>";
               foreach ($row as $key => $val){
                  if($key == 'hospital_id'){
                     print "<td onClick=\"window.open('map.php?h_id=$val','hospital','')\">" . $val . "</td>";
                  }
                  else{
                     print "<td>" . $val . "</td>";
                  }
               }
               print "</tr>";
            }
         ?>
      </table>
   </body>
</html>