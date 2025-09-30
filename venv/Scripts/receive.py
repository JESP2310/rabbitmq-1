import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
        # Mensagem ainda não confirmada
        input("Press ENTER to acknowledge the message and remove it from the queue...")
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(" [x] Message acknowledged!")

    # auto_ack=False mantém a mensagem na fila até você confirmar
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=False)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

if __name__ == '__main__':
    main()
