from socket import *

def smtp_client(port=1025, server='127.0.0.1'):
    message = "\r\n Hello, this is my email message."
    end_message = "\r\n.\r\n"

    # Set up socket and connect to server
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((server, port))

    response = s.recv(1024).decode()
    if response[:3] != '220':
        print('Did not get 220 on connection')

    # Say hello to server
    s.send('HELO student\r\n'.encode())
    response = s.recv(1024).decode()
    if response[:3] != '250':
        print('HELO failed')

    # Tell server who the email is from
    s.send('MAIL FROM:<aj2494@nyu.edu>\r\n'.encode())
    response = s.recv(1024).decode()
    if response[:3] != '250':
        print('MAIL FROM rejected')

    # Tell server who the email is to
    s.send('RCPT TO:<anikajishan18@gmail.com>\r\n'.encode())
    response = s.recv(1024).decode()
    if response[:3] != '250':
        print('RCPT TO rejected')

    # Start data section
    s.send('DATA\r\n'.encode())
    response = s.recv(1024).decode()
    if response[:3] != '354':
        print('DATA command not accepted')

    # Send the message itself
    s.send(message.encode())
    s.send(end_message.encode())

    response = s.recv(1024).decode()
    if response[:3] != '250':
        print('Message not accepted')

    # Close the connection politely
    s.send('QUIT\r\n'.encode())
    response = s.recv(1024).decode()
    if response[:3] != '221':
        print('QUIT failed')

    s.close()

if __name__ == '__main__':
    smtp_client()
