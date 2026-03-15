import json

from models.packet import Packet
from models.enums import Protocol
from parser.validators import validate_ip, validate_port, validate_protocol


def load_packets(file_path: str) -> list[Packet]:
    with open(file_path, "r", encoding="utf-8") as file:
        raw_packets = json.load(file)

    packets = []

    for raw_packet in raw_packets:
        source_ip = raw_packet["source_ip"]
        destination_ip = raw_packet["destination_ip"]
        port = raw_packet["port"]
        protocol = raw_packet["protocol"]

        if not validate_ip(source_ip):
            raise ValueError(f"IP de origem inválido no pacote: {source_ip}")

        if not validate_ip(destination_ip):
            raise ValueError(f"IP de destino inválido no pacote: {destination_ip}")

        if not validate_port(port):
            raise ValueError(f"Porta inválida no pacote: {port}")

        if not validate_protocol(protocol):
            raise ValueError(f"Protocolo inválido no pacote: {protocol}")

        packets.append(
            Packet(
                source_ip=source_ip,
                destination_ip=destination_ip,
                port=port,
                protocol=Protocol(protocol),
            )
        )

    return packets