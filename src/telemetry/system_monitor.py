"""
System Monitor

Tracks:
- recursive operational telemetry
- coherence metrics
- integrity stability
- ecosystem health
- longitudinal system diagnostics
"""

from datetime import datetime

from src.utils.logger import setup_logger

# --------------------------------------------------
# Initialize Logger
# --------------------------------------------------

logger = setup_logger()


class SystemMonitor:
    """
    Recursive telemetry and diagnostics monitor.
    """

    def __init__(self):

        logger.info(
            "System Monitor initialized."
        )

        self.telemetry_history = []

    # --------------------------------------------------
    # Record Telemetry Snapshot
    # --------------------------------------------------

    def record_snapshot(
        self,
        coherence_score: float,
        epistemic_integrity: float,
        contradiction_count: int,
        metadata: dict = None
    ) -> dict:
        """
        Record operational telemetry snapshot.
        """

        logger.info(
            "Recording telemetry snapshot."
        )

        snapshot = {
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
            "system_state": self.evaluate_system_state(
                coherence_score,
                epistemic_integrity,
                contradiction_count
            ),
            "metadata": metadata or {}
        }

        self.telemetry_history.append(snapshot)

        logger.info(
            "Telemetry snapshot recorded."
        )

        return snapshot

    # --------------------------------------------------
    # Evaluate System State
    # --------------------------------------------------

    def evaluate_system_state(
        self,
        coherence_score: float,
        epistemic_integrity: float,
        contradiction_count: int
    ) -> str:
        """
        Evaluate operational system state.
        """

        logger.info(
            "Evaluating system operational state."
        )

        if (
            coherence_score >= 0.90
            and epistemic_integrity >= 0.90
            and contradiction_count == 0
        ):

            return "optimal"

        elif (
            coherence_score >= 0.75
            and epistemic_integrity >= 0.75
        ):

            return "stable"

        elif (
            coherence_score >= 0.50
            and epistemic_integrity >= 0.50
        ):

            return "adaptive_variation"

        else:

            return "recursive_instability"

    # --------------------------------------------------
    # Retrieve Latest Snapshot
    # --------------------------------------------------

    def latest_snapshot(self) -> dict:
        """
        Retrieve latest telemetry snapshot.
        """

        logger.info(
            "Retrieving latest telemetry snapshot."
        )

        if not self.telemetry_history:

            return {
                "status": "no_telemetry_data"
            }

        return self.telemetry_history[-1]

    # --------------------------------------------------
    # Evaluate Longitudinal Stability
    # --------------------------------------------------

    def evaluate_longitudinal_stability(self) -> dict:
        """
        Evaluate long-term telemetry stability.
        """

        logger.info(
            "Evaluating longitudinal telemetry stability."
        )

        if not self.telemetry_history:

            return {
                "state": "initializing",
                "average_coherence": 1.0
            }

        coherence_scores = [
            snapshot["coherence_score"]
            for snapshot in self.telemetry_history
        ]

        average_coherence = (
            sum(coherence_scores)
            / len(coherence_scores)
        )

        average_coherence = round(
            average_coherence,
            2
        )

        if average_coherence >= 0.90:

            state = "high_stability"

        elif average_coherence >= 0.75:

            state = "stable"

        elif average_coherence >= 0.50:

            state = "adaptive_variation"

        else:

            state = "recursive_instability"

        logger.info(
            f"Telemetry stability evaluated: {state}"
        )

        return {
            "state": state,
            "average_coherence": average_coherence,
            "snapshot_count": len(
                self.telemetry_history
            )
        }

    # --------------------------------------------------
    # Generate Diagnostic Report
    # --------------------------------------------------

    def diagnostic_report(self) -> dict:
        """
        Generate operational diagnostic report.
        """

        logger.info(
            "Generating diagnostic report."
        )

        latest = self.latest_snapshot()

        longitudinal = (
            self.evaluate_longitudinal_stability()
        )

        return {
            "generated_at": (
                datetime.utcnow().isoformat()
            ),
            "latest_snapshot": latest,
            "longitudinal_stability": longitudinal,
            "telemetry_entries": len(
                self.telemetry_history
            )
        }
