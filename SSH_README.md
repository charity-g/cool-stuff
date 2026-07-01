
BASH

1) `ssh-keygen -t ed25519 -C "your_email@example.com"`
2) `eval "$(ssh-agent -s)"`
    - This starts the SSH authentication agent in the background.
    - `ssh-agent -s` launches the SSH agent and outputs environment variables like
    ```
    SSH_AUTH_SOCK=/tmp/ssh-xxxx/agent.1234;
    SSH_AGENT_PID=1234;
    export SSH_AUTH_SOCK;
    export SSH_AGENT_PID;
    ```

    - `$(...)` captures that output
    - `eval` executes the captured output in your current shell

3) `ssh-add ~/.ssh/id_ed25519`
    - This loads your SSH private key into the running SSH agent.
    - `ssh-add` adds a private key to the agent

4) `cat ~/.ssh/id_ed25519.pub`
    - copy output

5) Add output from 4) to `https://github.com/settings/keys`

6) optional `ssh -T git@github.com`