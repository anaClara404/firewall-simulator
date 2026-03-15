# Defines the Packet data class: a network packet with its source and destination IP addresses, port, and protocol.

from dataclasses import dataclass
from .enums import Protocol

@dataclass(frozen=True)
class Packet:
    source_ip: str
    destination_ip: str
    port: int
    protocol: Protocol