from rest_framework.views import APIView
import logging
import paramiko

# TODO: Implement and test the Paramiko functions into the below Handler
class ParamikoSSHHandler():
    """
    Paramiko SSH connection handler.
    This class will be initialized in other VM API handlers for SSH connection.
    """
    # This is the test local connection of Paramiko
    def __init__(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.username = 'nieluming'
        self.password = '888777419036'
        self.client.connect('127.0.0.1', username=self.username, password=self.password)
        self.stdin, self.stdout, self.stderr = self.client.exec_command('ls -l')

    def print_message(self):
        print self.stdin, self.stdout, self.stderr


class WakeUpVMHandler(APIView):
    """
    Class based API for Wake Up virtual machine.
    """

    def post(self, request):
        """
        POST method for processing the Virtual Machine Wakeup request
        """
        try:
            logging.debug("Waking up the Virtual Machine with POST request.")
            # Call back end script to wake up virtual machine

        except Exception:
            logging.error("Failed to wake up the Virtual Machine.")


class VMStatusHandler(APIView):
    """
    APIs for getting Virtual Machine status.
    """

    def get(self, request):
        """
        GET method for processing the Virtual Machine Wakeup request
        """
        try:
            logging.debug("Getting Virtual Machine status with GET request.")
            # Call back end script to wake up virtual machine

        except Exception:
            logging.error("Failed to get the Virtual Machine Status.")