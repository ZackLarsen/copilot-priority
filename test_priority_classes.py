import unittest
from unittest.mock import MagicMock
from priority_classes import Hospital, Patient, RiskLevel

class TestHospital(unittest.TestCase):
    def setUp(self):
        self.hospital = Hospital()

    def test_triage_patient_high_acuity(self):
        patient = Patient(has_high_acuity=True)
        self.hospital.triage_patient(patient)
        self.assertEqual(patient.triaged_risk, RiskLevel.HIGH)
        self.assertTrue(patient.has_been_triaged)
        self.assertEqual(self.hospital.risk_change_count, 1)

    def test_triage_patient_moderate_acuity(self):
        patient = Patient(has_moderate_acuity=True)
        self.hospital.triage_patient(patient)
        self.assertEqual(patient.triaged_risk, RiskLevel.MODERATE)
        self.assertTrue(patient.has_been_triaged)
        self.assertEqual(self.hospital.risk_change_count, 1)

    def test_triage_patient_needs_stabilization(self):
        patient = Patient(needs_stabilization=True, current_clinical_risk="Moderate")
        self.hospital.triage_patient(patient)
        self.assertEqual(patient.triaged_risk, "Moderate")
        self.assertTrue(patient.has_been_triaged)
        self.assertEqual(self.hospital.risk_change_count, 0)

    def test_triage_patient_low_acuity(self):
        patient = Patient(current_clinical_risk="Low")
        self.hospital.triage_patient(patient)
        self.assertIsNone(patient.triaged_risk)
        self.assertFalse(patient.has_been_triaged)
        self.assertEqual(self.hospital.risk_change_count, 0)

if __name__ == '__main__':
    unittest.main()