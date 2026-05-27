"""
Archive Manager

Coordinates:
- episodic memory
- semantic memory
- experience graph persistence
- longitudinal continuity archives
- recursive memory snapshots
"""

from datetime import datetime

from src.memory.episodic_memory import EpisodicMemory
from src.memory.semantic_memory import SemanticMemory
from src.memory.experience_graph import ExperienceGraph

from src.utils.logger import setup_logger

# --------------------------------------------------
# Initialize Logger
# --------------------------------------------------

logger = setup_logger()


class ArchiveManager:
    """
    Centralized memory and continuity archive manager.
    """

    def __init__(self):

        logger.info(
            "Archive Manager initialized."
        )

        # ----------------------------------------------
        # Initialize Memory Systems
        # ----------------------------------------------

        self.episodic_memory = EpisodicMemory()

        self.semantic_memory = SemanticMemory()

        self.experience_graph = ExperienceGraph()

    # --------------------------------------------------
    # Store Unified Archive Entry
    # --------------------------------------------------

    def store_interaction(
        self,
        prompt: str,
        response: str,
        coherence_score: float,
        metadata: dict = None
    ) -> dict:
        """
        Store unified interaction archive entry.
        """

        logger.info(
            "Storing unified archive interaction."
        )

        episode = self.episodic_memory.store_episode(
            prompt=prompt,
            response=response,
            coherence_score=coherence_score,
            metadata=metadata
        )

        return {
            "status": "interaction_archived",
            "episode": episode
        }

    # --------------------------------------------------
    # Store Semantic Concept
    # --------------------------------------------------

    def store_concept(
        self,
        concept: str,
        definition: str,
        metadata: dict = None
    ) -> dict:
        """
        Store semantic concept.
        """

        logger.info(
            f"Archiving semantic concept: {concept}"
        )

        return self.semantic_memory.store_knowledge(
            concept=concept,
            definition=definition,
            metadata=metadata
        )

    # --------------------------------------------------
    # Link Experiences
    # --------------------------------------------------

    def link_experiences(
        self,
        source_id: str,
        target_id: str,
        relationship: str
    ) -> dict:
        """
        Create relational experience linkage.
        """

        logger.info(
            f"Linking archived experiences: "
            f"{source_id} -> {target_id}"
        )

        return self.experience_graph.add_relationship(
            source_id=source_id,
            target_id=target_id,
            relationship=relationship
        )

    # --------------------------------------------------
    # Retrieve System Snapshot
    # --------------------------------------------------

    def snapshot(self) -> dict:
        """
        Generate full recursive archive snapshot.
        """

        logger.info(
            "Generating recursive archive snapshot."
        )

        episodic_snapshot = (
            self.episodic_memory.snapshot()
        )

        semantic_snapshot = (
            self.semantic_memory.snapshot()
        )

        graph_snapshot = (
            self.experience_graph.snapshot()
        )

        return {
            "timestamp": datetime.utcnow().isoformat(),
            "episodic_memory": episodic_snapshot,
            "semantic_memory": semantic_snapshot,
            "experience_graph": graph_snapshot
        }

    # --------------------------------------------------
    # Evaluate Archive Stability
    # --------------------------------------------------

    def evaluate_archive_stability(self) -> dict:
        """
        Evaluate total archive continuity stability.
        """

        logger.info(
            "Evaluating archive stability."
        )

        episodic_state = (
            self.episodic_memory.evaluate_stability()
        )

        semantic_state = (
            self.semantic_memory.evaluate_stability()
        )

        graph_state = (
            self.experience_graph.analyze_stability()
        )

        return {
            "episodic_state": episodic_state,
            "semantic_state": semantic_state,
            "graph_state": graph_state,
            "archive_status": "stable"
        }

    # --------------------------------------------------
    # Retrieve Recent Interactions
    # --------------------------------------------------

    def recent_interactions(
        self,
        limit: int = 10
    ) -> list:
        """
        Retrieve recent archived interactions.
        """

        logger.info(
            f"Retrieving recent archived interactions "
            f"(limit={limit})."
        )

        return self.episodic_memory.retrieve_recent(
            limit=limit
        )
