"""
Example usage for Cutaneous Corneometry Stratum Corneum Hydration Skill.
"""

from client import CorneometryHydrationClient


def main():
    client = CorneometryHydrationClient()

    print("--- Case 1: Healthy Hydrated Stratum Corneum ---")
    healthy_case = client.evaluate_hydration(
        capacitance_samples_au=[46.5, 45.2, 47.1, 46.0],
        anatomical_site="Cheek",
        patient_age_years=28
    )
    print("Mean Hydration:", healthy_case["corneometry_metrics"]["mean_hydration_au"], "AU")
    print("Heterogeneity (CV%):", healthy_case["corneometry_metrics"]["coefficient_of_variation_cv_pct"], "%")
    print("Xerosis Status:", healthy_case["dermatological_assessment"]["xerosis_status"])
    print("Barrier Uniformity:", healthy_case["dermatological_assessment"]["barrier_uniformity"])
    print("Pathophysiology:", healthy_case["dermatological_assessment"]["pathophysiology_summary"])
    print()

    print("--- Case 2: Atopic Dermatitis Severe Barrier Xerosis ---")
    atopic_case = client.evaluate_hydration(
        capacitance_samples_au=[22.4, 18.5, 26.2, 19.8],
        anatomical_site="Antecubital Fossa",
        patient_age_years=16
    )
    print("Mean Hydration:", atopic_case["corneometry_metrics"]["mean_hydration_au"], "AU")
    print("Heterogeneity (CV%):", atopic_case["corneometry_metrics"]["coefficient_of_variation_cv_pct"], "%")
    print("Xerosis Status:", atopic_case["dermatological_assessment"]["xerosis_status"])
    print("Barrier Uniformity:", atopic_case["dermatological_assessment"]["barrier_uniformity"])
    print("Pathophysiology:", atopic_case["dermatological_assessment"]["pathophysiology_summary"])
    print()

    print("--- Case 3: Subclinical Winter Xerosis (Mildly Dry Skin) ---")
    dry_case = client.evaluate_hydration(
        capacitance_samples_au=[34.2, 35.8, 33.5, 36.1],
        anatomical_site="Pretibial Leg",
        patient_age_years=65
    )
    print("Mean Hydration:", dry_case["corneometry_metrics"]["mean_hydration_au"], "AU")
    print("Xerosis Status:", dry_case["dermatological_assessment"]["xerosis_status"])


if __name__ == "__main__":
    main()
