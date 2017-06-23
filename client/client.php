<?php

require __DIR__ . '/vendor/autoload.php';

use Calculator\CalculateRequest;
use Calculator\CalculatorClient;
use Grpc\ChannelCredentials;

list($_, $n1, $operation, $n2) = $argv;

$request = new CalculateRequest();
$request->setFirstNumber($n1);
$request->setLastNumber($n2);

$client = new CalculatorClient('grpc-server:50051', [
    'credentials' => ChannelCredentials::createInsecure(),
]);

switch ($operation) {
    case '+':
        $operationName = 'Add';
        break;
    case '-':
        $operationName = 'Subtract';
        break;
    case '*':
        $operationName = 'Multiply';
        break;
    case '/':
        $operationName = 'Divide';
        break;
    default:
        throw new InvalidArgumentException('Invalid operation! Must be + - * /');
}

list($reply, $status) = $client->$operationName($request)->wait();
if ($reply === null) {
    echo sprintf('gRPC error[%d]: %s', $status->code, $status->details);
    exit(1);
}

echo 'The answer is ' . $reply->getAnswer();
