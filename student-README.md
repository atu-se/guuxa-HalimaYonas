# Student README

## Questions

1. The client and server have different sized buffers.  Why does it still work?
THANKS TO THE TCP, 
 TCP is a stream oriented protocol and it does not keep message boundaries.
 
2. What happens if the buffer size on the client is changed to a value smaller than the initial `message_length`?
it will print something like that,
Received:
b'we'
b'lc'
b'om'
b'e '
b'to'

3. What happens if you run the client when the server is not running? 
error

4. What happens if you run the server while the server is already running?
it will restart  and it will wait for a connection from client 

5. What changes did you make to finish this assignment?
I removed the IF statement, while s.listen() I changed to s.listen(3), and I made socket.socket() like that to that IP version and TCP will be by default

6. What resources did you use to complete this assignemnt?  Make a Markdown list of web links below.
youtube, https://www.youtube.com/watch?v=u4kr7EFxAKk