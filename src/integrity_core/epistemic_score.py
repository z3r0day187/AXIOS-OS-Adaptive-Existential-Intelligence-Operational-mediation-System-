"""
Epistemic Score Engine

Computes:
- overall epistemic integrity
- coherence confidence
- contradiction-adjusted trust
- recursive reasoning reliability
"""

from src.utils.logger import setup_logger

# --------------------------------------------------
# Initialize Logger
# --------------------------------------------------

logger = setup_logger()


class EpistemicScore:
    """
    Epistemic integrity scoring engine.
    """

    def __init__(self):

        logger.info("Epistemic Score Engine initialized.")

    # --------------------------------------------------
    # Compute Epistemic Integrity
    # --------------------------------------------------

    def compute(
        self,
        consistency_score: float,
        predictability_score: float,
        trust_score: float,
        contradiction_count: int
    ) -> dict:
        """
        Compute overall epistemic integrity score.
        """

        logger.info(
            "Computing epistemic integrity score."
        )

        # ----------------------------------------------
        # Contradiction Penalty
        # ----------------------------------------------

        contradiction_penalty = contradiction_count * 0.05

        # ----------------------------------------------
        # Composite Integrity Calculation
        # ----------------------------------------------

        epistemic_integrity = (
            (consistency_score * 0.40)
            + (predictability_score * 0.35)
            + (trust_score * 0.25)
        )

        epistemic_integrity -= contradiction_penalty

        epistemic_integrity = max(
            0.0,
            min(epistemic_integrity, 1.0)
        )

        epistemic_integrity = round(
            epistemic_integrity,
            2
        )

        # ----------------------------------------------
        # Integrity Classification
        # ----------------------------------------------

        if epistemic_integrity >= 0.90:

            integrity_state = "high_integrity"

        elif epistemic_integrity >= 0.75:

            integrity_state = "stable"

        elif epistemic_integrity >= 0.50:

            integrity_state = "uncertain"

        else:

            integrity_state = "critical_instability"

        logger.info(
            f"Epistemic integrity score: "
            f"{epistemic_integrity}"
        )

        return {
            "epistemic_integrity": epistemic_integrity,
            "integrity_state": integrity_state,
            "contradiction_penalty": contradiction_penalty
        }

    # --------------------------------------------------
    # Confidence Calibration
    # --------------------------------------------------

    def calibrate_confidence(
        self,
        epistemic_integrity: float
    ) -> dict:
        """
        Calibrate response confidence level.
        """

        logger.info(
            "Calibrating epistemic confidence."
        )

        if epistemic_integrity >= 0.90:

            confidence = "high"

        elif epistemic_integrity >= 0.75:

            confidence = "stable"

        elif epistemic_integrity >= 0.50:

            confidence = "moderate"

        else:

            confidence = "low"

        return {
            "confidence_level": confidence,
            "epistemic_integrity": epistemic_integrity
        }

    # --------------------------------------------------
    # Recursive Reliability Projection
    # --------------------------------------------------

    def project_reliability(
        self,
        epistemic_integrity: float
    ) -> dict:
        """
        Project long-term recursive reliability.
        """

        logger.info(
            "Projecting recursive reliability."
        )

        if epistemic_integrity >= 0.90:

            projection = "stable_recursive_integrity"

        elif epistemic_integrity >= 0.70:

            projection = "manageable_recursive_variation"

        elif epistemic_integrity >= 0.50:

            projection = "elevated_recursive_risk"

        else:

            projection = "recursive_integrity_failure_risk"

        return {
            "reliability_projection": projection,
            "integrity_score": epistemic_integrity
        }
