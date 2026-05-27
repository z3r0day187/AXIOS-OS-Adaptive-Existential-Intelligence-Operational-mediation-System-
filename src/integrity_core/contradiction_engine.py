"""
Contradiction Engine

Detects:
- logical inconsistencies
- recursive instability
- conflicting reasoning states
- coherence violations
"""

from src.utils.logger import setup_logger

# --------------------------------------------------
# Initialize Logger
# --------------------------------------------------

logger = setup_logger()


class ContradictionEngine:
    """
    Contradiction detection and coherence analysis engine.
    """

    def __init__(self):

        logger.info("Contradiction Engine initialized.")

    # --------------------------------------------------
    # Contradiction Detection
    # --------------------------------------------------

    def detect(
        self,
        reasoning_trace: list
    ) -> list:
        """
        Detect contradictions within reasoning trace.
        """

        logger.info(
            "Starting contradiction analysis."
        )

        contradictions = []

        # ----------------------------------------------
        # Simple Contradiction Scan
        # ----------------------------------------------

        analyses = [
            step.get("analysis", "").lower()
            for step in reasoning_trace
        ]

        # Example placeholder contradiction rules
        contradiction_pairs = [
            ("stable", "instability"),
            ("coexistence", "domination"),
            ("truth", "deception"),
            ("coherence", "contradiction"),
        ]

        for index, analysis in enumerate(analyses):

            for positive, negative in contradiction_pairs:

                if positive in analysis and negative in analysis:

                    contradiction = {
                        "type": "semantic_conflict",
                        "stage": reasoning_trace[index].get(
                            "stage",
                            "unknown"
                        ),
                        "details": (
                            f"Detected contradiction between "
                            f"'{positive}' and '{negative}'."
                        )
                    }

                    contradictions.append(contradiction)

        # ----------------------------------------------
        # Recursive Stability Check
        # ----------------------------------------------

        if len(reasoning_trace) < 2:

            contradictions.append({
                "type": "insufficient_reasoning_depth",
                "stage": "recursive_analysis",
                "details": (
                    "Reasoning depth insufficient for "
                    "stable recursive evaluation."
                )
            })

        # ----------------------------------------------
        # Final Logging
        # ----------------------------------------------

        logger.info(
            f"Contradiction analysis complete. "
            f"Detected {len(contradictions)} contradiction(s)."
        )

        return contradictions

    # --------------------------------------------------
    # Contradiction Density
    # --------------------------------------------------

    def contradiction_density(
        self,
        contradictions: list,
        reasoning_trace: list
    ) -> float:
        """
        Calculate contradiction density score.
        """

        if not reasoning_trace:
            return 1.0

        density = len(contradictions) / len(reasoning_trace)

        density = round(density, 2)

        logger.info(
            f"Contradiction density calculated: {density}"
        )

        return density

    # --------------------------------------------------
    # Coherence Evaluation
    # --------------------------------------------------

    def evaluate_coherence(
        self,
        contradiction_density: float
    ) -> float:
        """
        Compute coherence score from contradiction density.
        """

        coherence_score = max(
            0.0,
            1.0 - contradiction_density
        )

        coherence_score = round(coherence_score, 2)

        logger.info(
            f"Coherence evaluation complete: "
            f"{coherence_score}"
        )

        return coherence_score
