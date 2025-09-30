# rabbitmq-1

RabbitMQ Producer e Consumer - Python

Este projeto contém dois scripts Python que demonstram como enviar e receber mensagens usando o RabbitMQ.

O primeiro script conecta ao RabbitMQ, cria uma fila chamada hello (caso não exista) e envia a mensagem "Hello World!" para essa fila.

O segundo script conecta ao mesmo RabbitMQ, declara a mesma fila hello e consome as mensagens que estão nela. Cada mensagem é exibida no terminal e só é removida da fila quando o usuário pressiona ENTER, permitindo que a mensagem seja processada com segurança antes de ser confirmada.

No RabbitMQ, a fila hello aparece no Management UI. As mensagens enviadas ficam na fila até serem consumidas e confirmadas pelo consumidor. Se uma mensagem ainda não for confirmada, ela aparece como unacknowledged no UI; após a confirmação, ela é removida da fila.

Esses scripts demonstram o funcionamento básico de envio e consumo de mensagens, mostrando como controlar manualmente a confirmação das mensagens para evitar perdas.
