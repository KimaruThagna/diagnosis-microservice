from ariadne.contrib.federation import FederatedObjectType

from diagnosis.models import Diagnosis

diagnosis_federated_object = FederatedObjectType("Diagnosis")
patient_federated_object = FederatedObjectType("Patient")
doctor_federated_object = FederatedObjectType("Doctor")

@diagnosis_federated_object.resolve_reference
def get_diagnosis_by_uid(representation):
    return Diagnosis.objects.get(id=representation.get("id"))


@diagnosis_federated_object.field("uid")
def resolve_id(obj, *_):
    return obj.uid


@diagnosis_federated_object.field("indexingId")
def resolve_indexing_id(obj, *_):
    return obj.indexing_id


@diagnosis_federated_object.field("diagnosis")
def resolve_diagnosis(obj, *_):
    return obj.diagnosis

@diagnosis_federated_object.field("consulting_doctor")
def resolve_consulting_doctor(obj, *_):
    return {"id":obj.consulting_doctor}

@diagnosis_federated_object.field("visiting_patient")
def resolve_visiting_patient(obj, *_):
    return {"id":obj.visiting_patient}

@doctor_federated_object.field("diagnosis")
def resolve_doctor_diagnosis(obj, *_):
    return Diagnosis.objects.filter(consulting_doctor__license_number=obj.diagnosis)

@patient_federated_object.field("diagnosis")
def resolve_patient_diagnosis(obj, *_):
    return Diagnosis.objects.filter(visiting_patient__patient_number=obj.visiting_patient)