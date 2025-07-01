import copy
from src.utils.data import symptoms, display_named_symptoms, diseases
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
le.fit_transform(diseases)

def encode_symptoms(symptom_list):
    """
    Encodes the symptoms into a list of integers.
    
    Args:
        symptom_list (list): List containing symptoms

    Returns:
        list: List of integers representing the encoded symptoms.
    """
    new_symptom_dict = copy.deepcopy(symptoms)
    for symptom in symptom_list:
        new_symptom_dict[symptom] = 1
    return list(new_symptom_dict.values())

def get_symptoms(symptom_list):
    """
    Returns the non display named symptoms from the given list.
    
    Args:
        symptom_list (list): List of symptoms.

    Returns:
        list: List of non display named symptoms.
    """
    non_display_symptoms = []
    for symptom in symptom_list:
        non_display_symptoms.append(display_named_symptoms[symptom])
    return non_display_symptoms


def inverse_encode_symptoms(encoded_symptoms):
    """
    Inverse encodes the symptoms from a list of integers to their original names.
    
    Args:
        encoded_symptoms (list): List of integers representing encoded symptoms.

    Returns:
        list: List of original symptom names.
    """
    return le.inverse_transform(encoded_symptoms)