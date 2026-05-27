"""
Reputation System

Evaluates:
- source reliability
- historical consistency
- epistemic trust weighting
- information integrity confidence
"""

from src.utils.logger import setup_logger

# --------------------------------------------------
# Initialize Logger
# --------------------------------------------------

logger = setup_logger()


class ReputationSystem:
    """
    Source reputation and trust evaluation engine.
    """

    def __init__(self):

        logger.info("Reputation System initialized.")

        # ----------------------------------------------
        # Placeholder Reputation Database
        # ----------------------------------------------

        self.source_registry = {
            "trusted": 0.95,
            "verified": 0.85,
            "unknown": 0.60,
            "unreliable": 0.30
        }

    # --------------------------------------------------
    # Source Evaluation
    # --------------------------------------------------

    def evaluate_source(
        self,
        source: str
    ) -> dict:
        """
        Evaluate source reputation score.
        """

        logger.info(
            f"Evaluating source reputation: {source}"
        )

        reputation_score = self.source_registry.get(
            source.lower(),
            0.50
        )

        reputation_score = round(
            reputation_score,
            2
        )

        # ----------------------------------------------
        # Reputation Classification
        # ----------------------------------------------

        if reputation_score >= 0.90:

            classification = "high_trust"

        elif reputation_score >= 0.75:

            classification = "trusted"

        elif reputation_score >= 0.50:

            classification = "uncertain"

        else:

            classification = "low_trust"

        logger.info(
            f"Source reputation evaluated: "
            f"{reputation_score}"
        )

        return {
            "source": source,
            "reputation_score": reputation_score,
            "classification": classification
        }

    # --------------------------------------------------
    # Historical Reliability
    # --------------------------------------------------

    def evaluate_historical_consistency(
        self,
        consistency_score: float,
        contradiction_count: int
    ) -> dict:
        """
        Evaluate longitudinal reliability trends.
        """

        logger.info(
            "Evaluating historical consistency."
        )

        penalty = contradiction_count * 0.05

        reliability_score = max(
            0.0,
            consistency_score - penalty
        )

        reliability_score = round(
            reliability_score,
            2
        )

        if reliability_score >= 0.90:

            state = "historically_stable"

        elif reliability_score >= 0.70:

            state = "moderately_stable"

        elif reliability_score >= 0.50:

            state = "elevated_uncertainty"

        else:

            state = "historical_instability"

        return {
            "reliability_score": reliability_score,
            "historical_state": state
        }

    # --------------------------------------------------
    # Composite Trust Evaluation
    # --------------------------------------------------

    def composite_trust_score(
        self,
        source_score: float,
        consistency_score: float,
        predictability_score: float
    ) -> dict:
        """
        Compute composite epistemic trust score.
        """

        logger.info(
            "Calculating composite trust score."
        )

        trust_score = (
            (source_score * 0.25)
            + (consistency_score * 0.40)
            + (predictability_score * 0.35)
        )

        trust_score = round(
            min(trust_score, 1.0),
            2
        )

        if trust_score >= 0.90:

            trust_state = "high_integrity"

        elif trust_score >= 0.75:

            trust_state = "stable"

        elif trust_score >= 0.50:

            trust_state = "uncertain"

        else:

            trust_state = "low_integrity"

        logger.info(
            f"Composite trust score: {trust_score}"
        )

        return {
            "trust_score": trust_score,
            "trust_state": trust_state
        }
