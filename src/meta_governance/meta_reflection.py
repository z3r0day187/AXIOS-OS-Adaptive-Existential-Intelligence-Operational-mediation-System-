"""
Meta Reflection Engine

Performs:
- recursive self-evaluation
- arbitration introspection
- coherence reflection
- epistemic self-monitoring
- adaptive reasoning assessment
"""

from datetime import datetime

from src.utils.logger import setup_logger

# --------------------------------------------------
# Initialize Logger
# --------------------------------------------------

logger = setup_logger()


class MetaReflection:
    """
    Recursive self-reflection and introspection engine.
    """

    def __init__(self):

        logger.info(
            "Meta Reflection Engine initialized."
        )

        self.reflection_history = []

    # --------------------------------------------------
    # Perform Reflection
    # --------------------------------------------------

    def reflect(
        self,
        coherence_score: float,
        epistemic_integrity: float,
        contradiction_count: int,
        metadata: dict = None
    ) -> dict:
        """
        Perform recursive system self-evaluation.
        """

        logger.info(
            "Performing recursive self-reflection."
        )

        # ----------------------------------------------
        # Reflection State Evaluation
        # ----------------------------------------------

        if contradiction_count == 0 and coherence_score >= 0.90:

            reflection_state = "stable_recursive_alignment"

        elif coherence_score >= 0.75:

            reflection_state = "adaptive_recursive_stability"

        elif coherence_score >= 0.50:

            reflection_state = "elevated_recursive_uncertainty"

        else:

            reflection_state = "recursive_instability_detected"

        # ----------------------------------------------
        # Reflection Record
        # ----------------------------------------------

        reflection = {
            "timestamp": datetime.utcnow().isoformat(),
            "coherence_score": round(
                coherence_score,
                2
            ),
            "epistemic_integrity": round(
                epistemic_integrity,
                2
            ),
            "contradiction_count": contradiction_count,
            "reflection_state": reflection_state,
            "metadata": metadata or {}
        }

        self.reflection_history.append(reflection)

        logger.info(
            f"Reflection complete: {reflection_state}"
        )

        return reflection

    # --------------------------------------------------
    # Evaluate Reflection Stability
    # --------------------------------------------------

    def evaluate_stability(self) -> dict:
        """
        Evaluate longitudinal reflection stability.
        """

        logger.info(
            "Evaluating reflection stability."
        )

        if not self.reflection_history:

            return {
                "reflection_state": "initializing",
                "average_coherence": 1.0
            }

        coherence_scores = [
            reflection["coherence_score"]
            for reflection in self.reflection_history
        ]

        average_coherence = (
            sum(coherence_scores)
            / len(coherence_scores)
        )

        average_coherence = round(
            average_coherence,
            2
        )

        # ----------------------------------------------
        # Stability Classification
        # ----------------------------------------------

        if average_coherence >= 0.90:

            stability_state = (
                "high_recursive_stability"
            )

        elif average_coherence >= 0.75:

            stability_state = "stable"

        elif average_coherence >= 0.50:

            stability_state = (
                "adaptive_variation"
            )

        else:

            stability_state = (
                "recursive_instability"
            )

        logger.info(
            f"Reflection stability: {stability_state}"
        )

        return {
            "stability_state": stability_state,
            "average_coherence": average_coherence,
            "reflection_count": len(
                self.reflection_history
            )
        }

    # --------------------------------------------------
    # Recursive Insight Generation
    # --------------------------------------------------

    def generate_insights(self) -> dict:
        """
        Generate recursive introspective insights.
        """

        logger.info(
            "Generating recursive introspective insights."
        )

        if not self.reflection_history:

            return {
                "insight_state": "no_reflection_data",
                "insights": []
            }

        latest = self.reflection_history[-1]

        insights = []

        if latest["contradiction_count"] > 0:

            insights.append(
                "Contradictions detected during recursive evaluation."
            )

        if latest["coherence_score"] < 0.75:

            insights.append(
                "Coherence degradation observed."
            )

        if latest["epistemic_integrity"] < 0.75:

            insights.append(
                "Epistemic integrity instability detected."
            )

        if not insights:

            insights.append(
                "Recursive systems remain within stable coherence bounds."
            )

        logger.info(
            "Recursive insights generated successfully."
        )

        return {
            "insight_state": "generated",
            "insights": insights
        }

    # --------------------------------------------------
    # Retrieve Reflection Timeline
    # --------------------------------------------------

    def get_reflection_timeline(self) -> list:
        """
        Return recursive reflection history.
        """

        logger.info(
            "Retrieving reflection timeline."
        )

        return self.reflection_history
