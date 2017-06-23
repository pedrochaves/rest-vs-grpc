<?php
// GENERATED CODE -- DO NOT EDIT!

namespace Calculator {

  class CalculatorClient extends \Grpc\BaseStub {

     // @param string $hostname hostname
     // @param array $opts channel options
     // @param \Grpc\Channel $channel (optional) re-use channel object
    public function __construct($hostname, $opts, $channel = null) {
      parent::__construct($hostname, $opts, $channel);
    }

     // @param \Calculator\CalculateRequest $argument input argument
     // @param array $metadata metadata
     // @param array $options call options
    public function Add(\Calculator\CalculateRequest $argument,
      $metadata = [], $options = []) {
      return $this->_simpleRequest('/calculator.Calculator/Add',
      $argument,
      ['\Calculator\CalculateResponse', 'decode'],
      $metadata, $options);
    }

     // @param \Calculator\CalculateRequest $argument input argument
     // @param array $metadata metadata
     // @param array $options call options
    public function Subtract(\Calculator\CalculateRequest $argument,
      $metadata = [], $options = []) {
      return $this->_simpleRequest('/calculator.Calculator/Subtract',
      $argument,
      ['\Calculator\CalculateResponse', 'decode'],
      $metadata, $options);
    }

     // @param \Calculator\CalculateRequest $argument input argument
     // @param array $metadata metadata
     // @param array $options call options
    public function Multiply(\Calculator\CalculateRequest $argument,
      $metadata = [], $options = []) {
      return $this->_simpleRequest('/calculator.Calculator/Multiply',
      $argument,
      ['\Calculator\CalculateResponse', 'decode'],
      $metadata, $options);
    }

     // @param \Calculator\CalculateRequest $argument input argument
     // @param array $metadata metadata
     // @param array $options call options
    public function Divide(\Calculator\CalculateRequest $argument,
      $metadata = [], $options = []) {
      return $this->_simpleRequest('/calculator.Calculator/Divide',
      $argument,
      ['\Calculator\CalculateResponse', 'decode'],
      $metadata, $options);
    }

  }

}
