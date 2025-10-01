RabbitMQ Producer e Consumer - Python

Dois scripts Python que demonstram envio e consumo de mensagens usando RabbitMQ.

Producer (send.py): envia "Hello World!" para a fila hello.
Consumer (receive.py): recebe mensagens da fila hello e só as remove após o usuário apertar ENTER (basic_ack).

Pré-requisitos: Python 3, RabbitMQ rodando localmente, biblioteca pika (pip install pika).

Uso:

Execute RabbitMQ.

Rode send.py para enviar mensagens.

Rode receive.py para consumir mensagens.

Resultado:

Mensagens aparecem na fila hello.

O consumer processa e confirma manualmente, mostrando o status no Management UI como Ready ou Unacknowledged.
