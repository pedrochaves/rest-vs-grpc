grpc:
	@docker-compose run --rm -e LD_LIBRARY_PATH=/usr/local/lib client protoc --proto_path=/protos --php_out=/app/app --grpc_out=/app/app --plugin=protoc-gen-grpc=/app/grpc/bins/opt/grpc_php_plugin /protos/calculator.proto
	@docker-compose run --rm server python -m grpc_tools.protoc -I/protos --python_out=/app/app/grpc --grpc_python_out=/app/app/grpc /protos/calculator.proto
