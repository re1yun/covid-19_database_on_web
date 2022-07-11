<!DOCTYPE html>
<html lang="ko">
<head>
<?php
    require_once 'dbconfig.php';
    $hospital = $_GET['h_id'];
    $sql = "select hospital_name, hospital_latitude, hospital_longitude, hospital_id from hospital where hospital_id = ". $hospital . ";";
   $result = mysqli_query($link, $sql);
    $row = mysqli_fetch_row($result);
    $name = $row[0];
    $lat = (float)$row[1];
    $lng = (float)$row[2];
?>
<title>병원 정보 출력</title>
<meta charset = 'utf-8'>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script type="text/javascript" src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
<script type="text/javascript" src="http://maps.google.com/maps/api/js?key=AIzaSyASC0ctZzu5GCyPC1YTwVh5zxnowx9saQc" >//키를 발급받아 사용하세요</script>
<style>
#map_ma {width:100%; height:400px; clear:both; border:solid 1px red;}
</style>
</head>
<body>

    
<div id="map_ma"></div>
<script type="text/javascript">
      $(document).ready(function() { 
   var Y_point         = <?= $lat?>;      // Y 좌표
   var X_point         = <?= $lng?>;      // X 좌표
   console.log(Y_point, X_point);
   var zoomLevel      = 18;            // 지도의 확대 레벨 : 숫자가 클수록 확대정도가 큼
   var markerTitle      = "<?= $name?>";      // 현재 위치 마커에 마우스를 오버을때 나타나는 정보
   var markerMaxWidth   = 300;            // 마커를 클릭했을때 나타나는 말풍선의 최대 크기
         var myLatlng = new google.maps.LatLng(Y_point, X_point); // 위치값 위도 경도

// 말풍선 내용
   var contentString   = '<div>' +
   '<h2><?= $name?></h2>'+
   '<p>.</p>' +
   '</div>';
   var myLatlng = new google.maps.LatLng(Y_point, X_point);
   var mapOptions = {
                  zoom: zoomLevel,
                  center: myLatlng,
                  mapTypeId: google.maps.MapTypeId.ROADMAP
               }
   var map = new google.maps.Map(document.getElementById('map_ma'), mapOptions);
   var marker = new google.maps.Marker({
                                 position: myLatlng,
                                 map: map,
                                 title: markerTitle
   });
   var infowindow = new google.maps.InfoWindow(
                                    {
                                       content: contentString,
                                       maxWizzzdth: markerMaxWidth
                                    }
         );
   google.maps.event.addListener(marker, 'click', function() {
      infowindow.open(map, marker);
   });
});
      </script>
</body>
</html>