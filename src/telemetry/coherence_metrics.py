"""
Coherence Metrics

Measures:
- recursive coherence stability
- contradiction density
- epistemic consistency
- longitudinal alignment integrity
"""

from statistics import mean

from src.utils.logger import setup_logger

# --------------------------------------------------
# Initialize Logger
# --------------------------------------------------

logger = setup_logger()


class CoherenceMetrics:
    """
    Recursive coherence measurement engine.
    """

    def __init__(self):

        logger.info(
            "Coherence Metrics initialized."
        )

    # --------------------------------------------------
    # Compute Coherence Index
    # --------------------------------------------------

    def compute_index(
        self,
        coherence_scores: list
    ) -> dict:
        """
        Compute aggregate coherence index.
        """

        logger.info(
            "Computing coherence index."
        )

        if not coherence_scores:

            return {
                "coherence_index": 0.0,
                "state": "no_data"
            }

        coherence_index = round(
            mean(coherence_scores),
            2
        )

        # ----------------------------------------------
        # Coherence Classification
        # ----------------------------------------------

        if coherence_index >= 0.90:

            state = "high_coherence"

        elif coherence_index >= 0.75:

            state = "stable"

        elif coherence_index >= 0.50:

            state = "adaptive_variation"

        else:

            state = "recursive_instability"

        logger.info(
            f"Coherence index computed: "
            f"{coherence_index}"
        )

        return {
            "coherence_index": coherence_index,
            "state": state
        }

    # --------------------------------------------------
    # Contradiction Density Metric
    # --------------------------------------------------

    def contradiction_density(
        self,
        contradiction_count: int,
        reasoning_depth: int
    ) -> dict:
        """
        Calculate contradiction density metric.
        """

        logger.info(
            "Calculating contradiction density."
        )

        if reasoning_depth <= 0:

            density = 1.0

        else:

            density = round(
                contradiction_count / reasoning_depth,
                2
            )

        # ----------------------------------------------
        # Density Classification
        # ----------------------------------------------

        if density <= 0.10:

            state = "minimal_contradiction"

        elif density <= 0.25:

            state = "manageable"

        elif density <= 0.50:

            state = "elevated_contradiction"

        else:

            state = "critical_instability"

        logger.info(
            f"Contradiction density: {density}"
        )

        return {
            "density": density,
            "state": state
        }

    # --------------------------------------------------
    # Alignment Integrity Metric
    # --------------------------------------------------

    def alignment_integrity(
        self,
        coherence_score: float,
        epistemic_integrity: float
    ) -> dict:
        """
        Evaluate alignment integrity stability.
        """

        logger.info(
            "Evaluating alignment integrity."
        )

        alignment_score = round(
            (
                coherence_score
                + epistemic_integrity
            ) / 2,
            2
        )

        if alignment_score >= 0.90:

            state = "high_alignment"

        elif alignment_score >= 0.75:

            state = "stable"

        elif alignment_score >= 0.50:

            state = "adaptive_variation"

        else:

            state = "alignment_instability"

        logger.info(
            f"Alignment integrity score: "
            f"{alignment_score}"
        )

        return {
            "alignment_score": alignment_score,
            "state": state
        }

    # --------------------------------------------------
    # Recursive Stability Metric
    # --------------------------------------------------

    def recursive_stability(
        self,
        historical_scores: list
    ) -> dict:
        """
        Evaluate recursive stability trends.
        """

        logger.info(
            "Evaluating recursive stability trends."
        )

        if len(historical_scores) < 2:

            return {
                "stability_state": "insufficient_data",
                "variance": 0.0
            }

        deltas = []

        for index in range(1, len(historical_scores)):

            delta = abs(
                historical_scores[index]
                - historical_scores[index - 1]
            )

            deltas.append(delta)

        variance = round(
            mean(deltas),
            2
        )

        # ----------------------------------------------
        # Stability Classification
        # ----------------------------------------------

        if variance <= 0.05:

            state = "stable_recursive_equilibrium"

        elif variance <= 0.15:

            state = "adaptive_variation"

        elif variance <= 0.30:

            state = "elevated_recursive_instability"

        else:

            state = "critical_recursive_divergence"

        logger.info(
            f"Recursive stability variance: "
            f"{variance}"
        )

        return {
            "variance": variance,
            "stability_state": state
        }
