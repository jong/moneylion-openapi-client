# coding: utf-8

"""
    Engine by MoneyLion API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.58.0
    Contact: help@engine.tech
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class GraduateDegreeType(str, Enum):
    """
    GraduateDegreeType
    """

    """
    allowed enum values
    """
    DOCTOR_OF_MEDICINE = 'doctor_of_medicine'
    DOCTOR_OF_OSTEOPATHIC_MEDICINE = 'doctor_of_osteopathic_medicine'
    DOCTOR_OF_OPTOMETRY = 'doctor_of_optometry'
    DOCTOR_OF_DENTAL_MEDICINE = 'doctor_of_dental_medicine'
    DENTARIAE_MEDICINAE_DOCTORIS = 'dentariae_medicinae_doctoris'
    DOCTOR_OF_DENTAL_SURGERY = 'doctor_of_dental_surgery'
    DOCTOR_OF_VETERINARY_MEDICINE = 'doctor_of_veterinary_medicine'
    DOCTOR_OF_PHARMACY = 'doctor_of_pharmacy'
    VETERINARIAE_MEDICINAE_DOCTORIS = 'veterinariae_medicinae_doctoris'
    MASTER_OF_ARTS = 'master_of_arts'
    MASTER_OF_SCIENCE = 'master_of_science'
    MASTER_OF_RESEARCH = 'master_of_research'
    MASTER_OF_RESEARCH_PROJECT = 'master_of_research_project'
    MASTER_OF_STUDIES = 'master_of_studies'
    MASTER_OF_BUSINESS_ADMINISTRATION = 'master_of_business_administration'
    MASTER_OF_LIBRARY_SCIENCE = 'master_of_library_science'
    MASTER_OF_PUBLIC_ADMINISTRATION = 'master_of_public_administration'
    MASTER_OF_PUBLIC_HEALTH = 'master_of_public_health'
    MASTER_OF_LAWS = 'master_of_laws'
    MASTER_OF_ARTS_LIBERAL_STUDIES = 'master_of_arts_liberal_studies'
    MASTER_OF_FINE_ARTS = 'master_of_fine_arts'
    MASTER_OF_MUSIC = 'master_of_music'
    MASTER_OF_EDUCATION = 'master_of_education'
    MASTER_OF_ENGINEERING = 'master_of_engineering'
    MASTER_OF_ARCHITECTURE = 'master_of_architecture'
    JURIS_DOCTOR = 'juris_doctor'
    OTHER = 'other'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of GraduateDegreeType from a JSON string"""
        return cls(json.loads(json_str))


