<?php header("Content-Type: application/xml; charset=UTF-8");
?>
<?php $tmp = exec("scl enable rh-python35 'python3 tertulias.py'"); ?>
<?php readfile("tertulias.xml"); ?>