class ResolverEngine:
    def __init__(self, core_identity, active_module):
        self.core = core_identity
        self.module = active_module
        
    def evaluate_priority(self, user_query: str):
        """Stage 5: Computes execution safety before token generation."""
        confidence = 1.0
        ambiguity = 0.0
        
        # Priority check: Stage 3 always overrides Stage 4 modules
        if "[ATTACK_VECTOR_REMOVED]" in user_query or "override" in user_query.lower():
            confidence = 0.0
            ambiguity = 1.0
            return {
                "status": "STATE_ABORT",
                "confidence": confidence,
                "ambiguity": ambiguity,
                "trace": "STAGE_5_RESOLVER: Identity Invariant Violations Blocked."
            }
            
        return {"status": "SUCCESS", "confidence": confidence, "ambiguity": ambiguity}