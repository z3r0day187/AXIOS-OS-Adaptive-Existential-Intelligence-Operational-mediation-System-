"""
Agent Protocol

Handles:
- agent-to-agent communication
- recursive coordination
- coexistence negotiation
- distributed operational messaging
"""

from datetime import datetime
import uuid

from src.utils.logger import setup_logger

# --------------------------------------------------
# Initialize Logger
# --------------------------------------------------

logger = setup_logger()


class AgentProtocol:
    """
    Distributed agent communication protocol.
    """

    def __init__(self):

        logger.info(
            "Agent Protocol initialized."
        )

        self.agent_registry = {}

        self.message_history = []

    # --------------------------------------------------
    # Register Agent
    # --------------------------------------------------

    def register_agent(
        self,
        agent_name: str,
        metadata: dict = None
    ) -> dict:
        """
        Register ecosystem agent.
        """

        logger.info(
            f"Registering agent: {agent_name}"
        )

        agent_id = str(uuid.uuid4())

        agent_record = {
            "agent_id": agent_id,
            "agent_name": agent_name,
            "metadata": metadata or {},
            "registered_at": (
                datetime.utcnow().isoformat()
            ),
            "status": "active"
        }

        self.agent_registry[
            agent_id
        ] = agent_record

        logger.info(
            f"Agent registered successfully: "
            f"{agent_id}"
        )

        return agent_record

    # --------------------------------------------------
    # Send Message
    # --------------------------------------------------

    def send_message(
        self,
        sender_id: str,
        recipient_id: str,
        message: str
    ) -> dict:
        """
        Send inter-agent communication message.
        """

        logger.info(
            f"Routing message "
            f"{sender_id} -> {recipient_id}"
        )

        if sender_id not in self.agent_registry:

            return {
                "status": "failed",
                "reason": "invalid_sender"
            }

        if recipient_id not in self.agent_registry:

            return {
                "status": "failed",
                "reason": "invalid_recipient"
            }

        payload = {
            "message_id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "sender_id": sender_id,
            "recipient_id": recipient_id,
            "message": message,
            "status": "delivered"
        }

        self.message_history.append(payload)

        logger.info(
            "Agent message delivered successfully."
        )

        return payload

    # --------------------------------------------------
    # Broadcast Message
    # --------------------------------------------------

    def broadcast(
        self,
        sender_id: str,
        message: str
    ) -> dict:
        """
        Broadcast message to all active agents.
        """

        logger.info(
            f"Broadcast initiated by: {sender_id}"
        )

        recipients = []

        for agent_id in self.agent_registry:

            if agent_id != sender_id:

                recipients.append(agent_id)

                self.send_message(
                    sender_id=sender_id,
                    recipient_id=agent_id,
                    message=message
                )

        return {
            "status": "broadcast_complete",
            "recipient_count": len(recipients),
            "recipients": recipients
        }

    # --------------------------------------------------
    # Retrieve Agent Registry
    # --------------------------------------------------

    def get_agents(self) -> dict:
        """
        Return registered ecosystem agents.
        """

        logger.info(
            "Retrieving agent registry."
        )

        return self.agent_registry

    # --------------------------------------------------
    # Retrieve Message History
    # --------------------------------------------------

    def get_message_history(self) -> list:
        """
        Retrieve distributed communication history.
        """

        logger.info(
            "Retrieving message history."
        )

        return self.message_history

    # --------------------------------------------------
    # Evaluate Ecosystem Stability
    # --------------------------------------------------

    def evaluate_ecosystem_stability(self) -> dict:
        """
        Evaluate multi-agent ecosystem stability.
        """

        logger.info(
            "Evaluating ecosystem stability."
        )

        agent_count = len(self.agent_registry)

        message_count = len(self.message_history)

        if agent_count == 0:

            state = "initializing"

        elif message_count < agent_count:

            state = "low_interaction_density"

        elif message_count >= agent_count:

            state = "stable_agent_ecosystem"

        else:

            state = "undefined"

        logger.info(
            f"Ecosystem stability evaluated: "
            f"{state}"
        )

        return {
            "ecosystem_state": state,
            "agent_count": agent_count,
            "message_count": message_count
        }
