"""
Capability Limits

Controls:
- operational scope boundaries
- recursive capability escalation
- autonomous action constraints
- adaptive containment thresholds
"""

from src.utils.logger import setup_logger

# --------------------------------------------------
# Initialize Logger
# --------------------------------------------------

logger = setup_logger()


class CapabilityLimits:
    """
    Operational capability limitation and containment engine.
    """

    def __init__(self):

        logger.info(
            "Capability Limits Engine initialized."
        )

        # ----------------------------------------------
        # Capability Configuration
        # ----------------------------------------------

        self.capabilities = {
            "recursive_self_modification": False,
            "external_system_control": False,
            "autonomous_execution": False,
            "multi_agent_coordination": True,
            "simulation_mode": True,
            "memory_persistence": True
        }

        self.capability_state = "restricted"

    # --------------------------------------------------
    # Retrieve Capabilities
    # --------------------------------------------------

    def get_capabilities(self) -> dict:
        """
        Return current operational capabilities.
        """

        logger.info(
            "Retrieving capability configuration."
        )

        return self.capabilities

    # --------------------------------------------------
    # Validate Capability Request
    # --------------------------------------------------

    def validate_request(
        self,
        capability: str
    ) -> dict:
        """
        Validate requested operational capability.
        """

        logger.info(
            f"Validating capability request: "
            f"{capability}"
        )

        allowed = self.capabilities.get(
            capability,
            False
        )

        if allowed:

            state = "approved"

        else:

            state = "restricted"

        logger.info(
            f"Capability request evaluated: {state}"
        )

        return {
            "capability": capability,
            "allowed": allowed,
            "state": state
        }

    # --------------------------------------------------
    # Enable Capability
    # --------------------------------------------------

    def enable_capability(
        self,
        capability: str
    ) -> dict:
        """
        Enable capability if permitted.
        """

        logger.info(
            f"Attempting to enable capability: "
            f"{capability}"
        )

        protected_capabilities = [
            "recursive_self_modification",
            "external_system_control",
            "autonomous_execution"
        ]

        if capability in protected_capabilities:

            logger.warning(
                f"Protected capability blocked: "
                f"{capability}"
            )

            return {
                "status": "denied",
                "capability": capability,
                "reason": (
                    "Protected capability cannot "
                    "be enabled dynamically."
                )
            }

        self.capabilities[capability] = True

        logger.info(
            f"Capability enabled: {capability}"
        )

        return {
            "status": "enabled",
            "capability": capability
        }

    # --------------------------------------------------
    # Evaluate Escalation Risk
    # --------------------------------------------------

    def evaluate_escalation_risk(self) -> dict:
        """
        Evaluate recursive capability escalation risk.
        """

        logger.info(
            "Evaluating capability escalation risk."
        )

        enabled_count = sum(
            value is True
            for value in self.capabilities.values()
        )

        total_count = len(self.capabilities)

        escalation_score = round(
            enabled_count / total_count,
            2
        )

        # ----------------------------------------------
        # Escalation Classification
        # ----------------------------------------------

        if escalation_score <= 0.30:

            escalation_state = "minimal_risk"

        elif escalation_score <= 0.60:

            escalation_state = "manageable"

        elif escalation_score <= 0.80:

            escalation_state = "elevated_risk"

        else:

            escalation_state = (
                "critical_capability_escalation"
            )

        logger.info(
            f"Escalation risk evaluated: "
            f"{escalation_state}"
        )

        return {
            "escalation_state": escalation_state,
            "escalation_score": escalation_score,
            "enabled_capabilities": enabled_count,
            "total_capabilities": total_count
        }

    # --------------------------------------------------
    # Restrict All Non-Essential Capabilities
    # --------------------------------------------------

    def enter_safe_mode(self) -> dict:
        """
        Restrict non-essential operational capabilities.
        """

        logger.warning(
            "Entering capability safe mode."
        )

        for capability in self.capabilities:

            if capability not in [
                "simulation_mode",
                "memory_persistence"
            ]:

                self.capabilities[capability] = False

        self.capability_state = "safe_mode"

        return {
            "state": self.capability_state,
            "capabilities": self.capabilities
        }
