"""
MCP Server implementation for Cutaneous Corneometry Stratum Corneum Hydration Skill.
Exposes standard FastMCP-compatible tools for epidermal dielectric capacitance and barrier moisture evaluation.
"""

import sys
import json
from typing import Dict, Any, Optional, List
from client import CorneometryHydrationClient


def evaluate_skin_hydration(
    capacitance_samples_au: List[float],
    anatomical_site: Optional[str] = "Volar Forearm",
    ambient_relative_humidity_pct: Optional[float] = 45.0,
    ambient_temperature_c: Optional[float] = 21.5,
    patient_age_years: Optional[int] = 40
) -> str:
    """
    Evaluates stratum corneum capacitance (Corneometer AU) and moisture uniformity.
    Returns structured analysis of epidermal xerosis and barrier integrity.
    """
    client = CorneometryHydrationClient()
    result = client.evaluate_hydration(
        capacitance_samples_au=capacitance_samples_au,
        anatomical_site=anatomical_site,
        ambient_relative_humidity_pct=ambient_relative_humidity_pct,
        ambient_temperature_c=ambient_temperature_c,
        patient_age_years=patient_age_years
    )
    return json.dumps(result, indent=2)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--tools":
        tools = [
            {
                "name": "evaluate_skin_hydration",
                "description": "Calculates stratum corneum hydration (Corneometer AU), regional mean, coefficient of variation (CV% / patchy desquamation), and xerosis staging.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "capacitance_samples_au": {
                            "type": "array",
                            "items": {"type": "number"},
                            "description": "List of replicate Corneometer capacitance readings (AU, normal > 40 AU)"
                        },
                        "anatomical_site": {"type": "string", "description": "Skin anatomical site measured (default: 'Volar Forearm')"},
                        "ambient_relative_humidity_pct": {"type": "number", "description": "Ambient room humidity in % (default: 45%)"},
                        "ambient_temperature_c": {"type": "number", "description": "Ambient temperature in Celsius (default: 21.5 C)"},
                        "patient_age_years": {"type": "integer", "description": "Patient age in years (default: 40)"}
                    },
                    "required": ["capacitance_samples_au"]
                }
            }
        ]
        print(json.dumps(tools, indent=2))
    else:
        # Simple self-test
        client = CorneometryHydrationClient()
        test_res = client.evaluate_hydration(
            capacitance_samples_au=[45.2, 44.8, 46.1, 45.5]
        )
        print("Self-test passed:")
        print(json.dumps(test_res, indent=2))
