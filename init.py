import subprocess
# Comandos a serem executados em cada painel do tmux
commands = [
    "cd /data/data/com.termux/files/home/docker && ./jellyfin.sh",
    f"filebrowser -a 0.0.0.0 -p 7075 -r /data/data/com.termux/files/home",
    f"cd /data/data/com.termux/files/home/TermuxMonitor/ && ./Monitor.sh",
    "sshd && logcat -s 'sshd:*'"
]

#Sessão tmux com os painéis
tmux_script = f"""
tmux new-session -d -s my_session
tmux split-window -h
tmux split-window -v
tmux select-pane -t 0
tmux split-window -v
tmux select-pane -t 0
tmux send-keys '{commands[0]}' C-m
tmux select-pane -t 1
tmux send-keys '{commands[1]}' C-m
tmux select-pane -t 2
tmux send-keys '{commands[2]}' C-m
tmux select-pane -t 3
tmux send-keys '{commands[3]}' C-m
tmux attach-session -t my_session
"""

# Executa o script tmux
subprocess.run(tmux_script, shell=True, executable='/bin/bash')
