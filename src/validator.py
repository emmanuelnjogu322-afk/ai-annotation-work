"""Small validation utilities for the Day One annotation portfolio."""

from collections import Counter

VALID_VISIBILITY = {"fully_visible", "partially_visible", "occluded"}


def validate_objects(objects):
    """Return validation errors for a list of annotation objects."""
    errors = []
    if not isinstance(objects, list):
        return ["objects must be a list"]
    instance_ids = [obj.get("instance_id") for obj in objects if isinstance(obj, dict)]
    if len(instance_ids) != len(set(instance_ids)):
        errors.append("duplicate instance_id detected")
    for index, obj in enumerate(objects):
        if not isinstance(obj, dict):
            errors.append(f"object {index}: expected an object")
            continue
        for field in ("class", "instance_id", "label", "visibility"):
            if not obj.get(field):
                errors.append(f"object {index}: missing {field}")
        if obj.get("visibility") not in VALID_VISIBILITY:
            errors.append(f"object {index}: invalid visibility")
    return errors


def count_instances(objects):
    """Count distinct annotation instances."""
    if not isinstance(objects, list):
        raise TypeError("objects must be a list")
    ids = [obj["instance_id"] for obj in objects]
    return len(set(ids))


def class_counts(objects):
    """Return the number of instances represented by each class."""
    return dict(Counter(obj["class"] for obj in objects))


if __name__ == "__main__":
    sample = [
        {"class": "vehicle", "instance_id": "vehicle_01", "label": "car", "visibility": "fully_visible"},
        {"class": "vehicle", "instance_id": "vehicle_02", "label": "car", "visibility": "partially_visible"},
        {"class": "vehicle", "instance_id": "vehicle_03", "label": "motorcycle", "visibility": "partially_visible"},
    ]
    print("Validation:", validate_objects(sample))
    print("Instance count:", count_instances(sample))
    print("Class counts:", class_counts(sample))
