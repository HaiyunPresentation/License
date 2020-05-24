# License
*This is Project 3 of CNI course in Department of Software Engineering, School of Infomatics, Xiamen University.*  
## Protocol
### Client
```
PURC:[username]:[password]:[userNum] # Purchase license from the server
HELO:[license]                       # Say hello to the server with license
CKAL:                                # Check ticket alive
RELS:[license]:[ticket]              # Release ticket
```
### Server
```
UKNW:[info]                          # Cannot recognize the request
PERM:[license]                       # Permit license request
FAIL:[info]                          # Fail to give a license
WELC:[ticket]                        # Give a ticket
RFUS:[info]                          # Refuse to give a ticket,
                                     # or to keep a client alive
GOOD:                                # Permit the alive check
WARN:[info]                          # Receive an unused ticket from a client
GBYE:[info]                          # Say goodbye to a client
```
