"""Handles the communication between the backend<->interface, as well
as the MPI communication between different backend processes."""
from ipc.zmqserver import ZmqServer
import socket
import mpi

_server = None
hostname = socket.gethostname()
port = None
uuid = None

def zmq():
    """Returns the ZmqServer for process.
    If it does not yet exist create one first."""
    global _server # pylint: disable=global-statement
    global port # pylint: disable=global-statement
    if(_server is None and mpi.is_zmqserver()):
        _server = ZmqServer(port)
    return _server

from ipc.broadcast import new_data, set_current_event # pylint: disable=unused-import
