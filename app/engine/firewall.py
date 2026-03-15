# Implements the Firewall class, which processes incoming network packets against a set of firewall rules and determines the appropriate action (allow or block) based on the first matching rule or a default action if no rules match.

from models.packet import Packet
from models.rule import Rule
from models.enums import Action
from engine.matcher import RuleMatcher

class Firewall:

    def __init__(self, rules: list[Rule], default_action: Action = Action.BLOCK):
        self.rules = rules
        self.default_action = default_action

    def process_packet(self, packet: Packet) -> Action:

        for rule in self.rules:
            if RuleMatcher.matches(packet, rule):
                return rule.action

        return self.default_action
