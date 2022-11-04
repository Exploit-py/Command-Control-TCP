
# Command&Control

This malware consists of simulating a command and control attack.
This code consists of a server in listen mode receiving connections ("victim.py") and a script that will make the connection.
("attacker.py").

The victim will receive commands from the attacker and these commands will be executed on your PC

This project was made with the intention of learning about how C&C malware works, the misuse of this code is categorized as a crime and I am not responsible for its actions.

## Authors

- [@exploit-py](https://www.github.com/exploit-py)


## Important Waring

Avoid terminating the program with "Ctrl + C" as it may cause a bug.
You can end the program with "Ctrl + Z" in linux or by closing the terminal!


## Screenshots

![App Screenshot](https://cdn.discordapp.com/attachments/1022921946641473567/1037980054040350720/image.png)

![App Screenshot](https://cdn.discordapp.com/attachments/1022921946641473567/1037973574654361640/image.png)

## Deploy



Linux            
```bash
  python3 victim.py
  python3 attacker.py
```

Windows            
```bash
  python victim.py
  python attacker.py
```

