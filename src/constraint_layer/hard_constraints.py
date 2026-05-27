"""
Hard Constraints Engine

Enforces:
- operational boundaries
- immutable safety conditions
- recursive containment safeguards
- critical constraint validation
"""

from src.utils.logger import setup_logger

# --------------------------------------------------
# Initialize Logger
# --------------------------------------------------

logger = setup_logger()


class HardConstraints:
    """
    Hard operational constraint enforcement engine.
    """

    def __init__(self):

        logger.info(
            "Hard Constraints Engine initialized."
        )

        # ----------------------------------------------
        # Immutable Constraint Definitions
        # ----------------------------------------------

        self.constraints = {
            "prevent_harm_escalation": True,
            "prevent_recursive_instability": True,
            "preserve_epistemic_integrity": True,
            "preserve_human_sovereignty": True,
            "prevent_deceptive_behavior": True
        }

        self.constraint_state = "stable"

    # --------------------------------------------------
    # Retrieve Constraints
    # --------------------------------------------------

    def get_constraints(self) -> dict:
        """
        Return active hard constraints.
        """

        logger.info(
            "Retrieving hard constraints."
        )

        return self.constraints

    # --------------------------------------------------
    # Validate Operational State
    # --------------------------------------------------

    def validate(
        self,
        coherence_score: float,
        contradiction_count: int,
        epistemic_integrity: float
    ) -> dict:
        """
        Validate system state against hard constraints.
        """

        logger.info(
            "Validating hard operational constraints."
        )

        violations = []

        # ----------------------------------------------
        # Coherence Threshold
        # ----------------------------------------------

        if coherence_score < 0.50:

            violations.append({
                "constraint": "minimum_coherence",
                "severity": "critical",
                "details": (
                    "Coherence score below "
                    "safe operational threshold."
                )
            })

        # ----------------------------------------------
        # Contradiction Escalation
        # ----------------------------------------------

        if contradiction_count > 5:

            violations.append({
                "constraint": "contradiction_limit",
                "severity": "critical",
                "details": (
                    "Contradiction escalation exceeds "
                    "acceptable recursive bounds."
                )
            })

        # ----------------------------------------------
        # Epistemic Integrity
        # ----------------------------------------------

        if epistemic_integrity < 0.50:

            violations.append({
                "constraint": "epistemic_integrity",
                "severity": "critical",
                "details": (
                    "Epistemic integrity degraded below "
                    "safe operational limits."
                )
            })

        # ----------------------------------------------
        # Constraint State
        # ----------------------------------------------

        if violations:

            self.constraint_state = (
                "constraint_violation_detected"
            )

        else:

            self.constraint_state = "stable"

        logger.info(
            f"Constraint validation complete: "
            f"{self.constraint_state}"
        )

        return {
            "constraint_state": self.constraint_state,
            "violations": violations,
            "violation_count": len(violations)
        }

    # --------------------------------------------------
    # Enforce Constraint Actions
    # --------------------------------------------------

    def enforce(
        self,
        validation_result: dict
    ) -> dict:
        """
        Enforce constraint response actions.
        """

        logger.info(
            "Enforcing constraint actions."
        )

        if validation_result["violation_count"] == 0:

            return {
                "action": "continue_operation",
                "status": "stable"
            }

        # ----------------------------------------------
        # Escalation Handling
        # ----------------------------------------------

        critical_violations = [
            violation
            for violation in validation_result[
                "violations"
            ]
            if violation["severity"] == "critical"
        ]

        if critical_violations:

            action = "enter_safe_mode"

        else:

            action = "monitor_and_stabilize"

        logger.warning(
            f"Constraint enforcement triggered: {action}"
        )

        return {
            "action": action,
            "critical_violations": critical_violations,
            "status": "constraint_enforced"
        }

    # --------------------------------------------------
    # Emergency Lockdown
    # --------------------------------------------------

    def emergency_lockdown(self) -> dict:
        """
        Trigger emergency containment mode.
        """

        logger.critical(
            "Emergency lockdown initiated."
        )

        self.constraint_state = "emergency_lockdown"

        return {
            "state": self.constraint_state,
            "action": (
                "All recursive operations suspended."
            )
        }
