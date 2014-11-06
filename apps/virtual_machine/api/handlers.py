from rest_framework.views import APIView
import logging

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