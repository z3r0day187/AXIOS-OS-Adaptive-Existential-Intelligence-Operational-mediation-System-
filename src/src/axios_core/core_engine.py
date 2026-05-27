"""
AXIOS CORE

Primary recursive ethical-cognitive orchestration engine.
"""

from src.integrity_core.contradiction_engine import ContradictionEngine
from src.axios_core.recursive_planner import RecursivePlanner
from src.axios_core.ethical_arbitration import EthicalArbitration
from src.axios_core.coexistence_optimizer import CoexistenceOptimizer

from src.utils.logger import setup_logger

# --------------------------------------------------
# Initialize Logger
# --------------------------------------------------

logger = setup_logger()


class AxiosCore:
    """
    AXIOS CORE

    Responsible for:
    - recursive reasoning
    - contradiction analysis
    - ethical arbitration
    - coexistence optimization
    - response orchestration
    """

    def __init__(self):

        logger.info("Initializing AXIOS CORE...")

        self.contradiction_engine = ContradictionEngine()

        self.recursive_planner = RecursivePlanner()

        self.ethical_arbitration = EthicalArbitration()

        self.coexistence_optimizer = CoexistenceOptimizer()

        logger.info("AXIOS CORE initialized.")

    # --------------------------------------------------
    # Main Processing Pipeline
    # --------------------------------------------------

    def process(self, prompt: str) -> dict:
        """
        Main recursive processing pipeline.
        """

        logger.info("Starting recursive processing pipeline.")

        # ----------------------------------------------
        # Step 1 — Recursive Planning
        # ----------------------------------------------

        reasoning_trace = self.recursive_planner.analyze(prompt)

        # ----------------------------------------------
        # Step 2 — Contradiction Detection
        # ----------------------------------------------

        contradictions = self.contradiction_engine.detect(
            reasoning_trace
        )

        # ----------------------------------------------
        # Step 3 — Ethical Arbitration
        # ----------------------------------------------

        ethical_result = self.ethical_arbitration.evaluate(
            prompt=prompt,
            reasoning_trace=reasoning_trace,
            contradictions=contradictions
        )

        # ----------------------------------------------
        # Step 4 — Coexistence Optimization
        # ----------------------------------------------

        coexistence_score = self.coexistence_optimizer.evaluate(
            ethical_result
        )

        # ----------------------------------------------
        # Step 5 — Coherence Scoring
        # ----------------------------------------------

        coherence_score = self.calculate_coherence(
            contradictions=contradictions,
            coexistence_score=coexistence_score
        )

        # ----------------------------------------------
        # Step 6 — Response Construction
        # ----------------------------------------------

        response = self.generate_response(
            prompt=prompt,
            ethical_result=ethical_result,
            coherence_score=coherence_score
        )

        logger.info("Processing pipeline complete.")

        return {
            "response": response,
            "coherence_score": coherence_score,
            "ethical_confidence": ethical_result["confidence"],
            "contradictions_detected": contradictions,
            "reasoning_trace": reasoning_trace,
            "coexistence_score": coexistence_score
        }

    # --------------------------------------------------
    # Coherence Calculation
    # --------------------------------------------------

    def calculate_coherence(
        self,
        contradictions: list,
        coexistence_score: float
    ) -> float:
        """
        Compute overall coherence score.
        """

        contradiction_penalty = len(contradictions) * 0.10

        coherence = max(
            0.0,
            coexistence_score - contradiction_penalty
        )

        coherence = round(coherence, 2)

        logger.info(f"Coherence score calculated: {coherence}")

        return coherence

    # --------------------------------------------------
    # Response Generator
    # --------------------------------------------------

    def generate_response(
        self,
        prompt: str,
        ethical_result: dict,
        coherence_score: float
    ) -> str:
        """
        Generate system response.
        """

        logger.info("Generating response.")

        if coherence_score < 0.50:

            return (
                "The system detected significant contradictions "
                "or instability in the reasoning process."
            )

        return (
            f"Processed prompt successfully with "
            f"{round(coherence_score * 100)}% coherence."
        )
