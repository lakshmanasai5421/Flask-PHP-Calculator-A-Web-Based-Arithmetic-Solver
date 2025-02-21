<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $num1 = (float)$_POST['num1'];
    $num2 = (float)$_POST['num2'];
    $operation = $_POST['operation'];
    
    $payload = json_encode([
        'operation' => $operation,
        'num1' => $num1,
        'num2' => $num2
    ]);
    
    $ch = curl_init('http://localhost:5000/calc');
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => $payload,
        CURLOPT_HTTPHEADER => [
            'Content-Type: application/json',
            'Content-Length: ' . strlen($payload)
        ]
    ]);
    
    $response = curl_exec($ch);
    $result = json_decode($response, true);
    curl_close($ch);
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Calculator</title>
</head>
<body>
    <form method="post">
        <input type="number" name="num1" step="any" required>
        <select name="operation" required>
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">×</option>
            <option value="divide">÷</option>
        </select>
        <input type="number" name="num2" step="any" required>
        <button type="submit">Calculate</button>
    </form>

    <?php if ($_SERVER['REQUEST_METHOD'] === 'POST'): ?>
        <div class="result">
            <?php if(isset($result['error'])): ?>
                <p style="color: red;">Error: <?= $result['error'] ?></p>
            <?php else: ?>
                <p>Result: <?= $result['result'] ?? 'Unknown' ?></p>
            <?php endif; ?>
        </div>
    <?php endif; ?>
</body>
</html>