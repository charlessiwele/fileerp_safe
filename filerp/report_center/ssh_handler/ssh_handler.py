import os
import paramiko
from filerp.settings import SSH_SERVER_ADDRESS


class SSHHandler:
    @staticmethod
    def run_ssh_file_send_local_file_to_server(local_path, remote_path, username, password):
        ssh = paramiko.SSHClient()
        ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
        server = SSH_SERVER_ADDRESS
        ssh.connect(server, username=username, password=password)
        with ssh.open_sftp() as ssh:
            with ssh.open_sftp() as sftp:
                sftp.put(local_path, remote_path)
