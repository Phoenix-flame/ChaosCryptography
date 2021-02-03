# ChaosCryptography
Cryptography based on chaotic systems

![alt text](https://github.com/Phoenix-flame/ChaosCryptography/blob/main/images/xz.png?raw=true)

### File Structure
Lorenz system is implemented in 'LorenzSystem.py'. This Class solves lorenz map for predefined initial values and parameters.

This file also contains PRNG class that is used for generating random numbers.
This class has 'SetKey' member function that is used to set private key (including parameters and initial values).
When you set your private key, unique random number based on lorenz system's time series, can be generated using 'generate' member function.

'Server.py' is simple TCP/IP server that can be used either on localhost or actual server.
This server listens to socket and receives message from single client, this message is encryted, so using same private key as client, message can be decrypted.

'Client.py' is simple TCP/IP client that connects to server and send simple encrypted message.

'TestPRNG.py' contains NIST test that is used to test our PRNG.



