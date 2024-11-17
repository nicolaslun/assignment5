<?php

$a = $_GET['a'] ?? null;
$b = $_GET['b'] ?? null;
$c = $_GET['c'] ?? null;
$d = $_GET['d'] ?? null;
$e = $_GET['e'] ?? null;

if (is_null($a) || is_null($b) || is_null($c) || is_null($d) || is_null($e)) {
    echo "<p>Error: Please provide all five numbers in the URL.</p>";
    exit;
}

$a = escapeshellarg($a);
$b = escapeshellarg($b);
$c = escapeshellarg($c);
$d = escapeshellarg($d);
$e = escapeshellarg($e);

echo "Python Execution" . "<br>";

$output = shell_exec("python3 data_management.py $a $b $c $d $e");
echo "<p>Result: " . nl2br($output) . "</p>";
?>
