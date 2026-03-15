from engine.firewall import Firewall
from models.enums import Action
from parser.rules_parser import load_rules
from parser.packets_parser import load_packets


def main():
    rules = load_rules("data/rules.json")
    packets = load_packets("data/packets.json")

    firewall = Firewall(rules=rules, default_action=Action.BLOCK)

    for packet in packets:
        result = firewall.process_packet(packet)
        print(
            f"{packet.protocol.value} "
            f"{packet.source_ip} -> {packet.destination_ip}:{packet.port} "
            f"=> {result.value}"
        )


if __name__ == "__main__":
    main()