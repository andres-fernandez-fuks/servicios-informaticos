from project import db
from typing import Any, List
from marshmallow import ValidationError

from project.models.base_model import BaseModel, NullBaseModel


class InexistentBaseModelInstance(ValidationError):
    def __init__(self, obj_name: str, parameter: str, value: Any):
        message = {
            "error": f"inexistent_{obj_name}",
            "parameter": parameter,
            "value": value,
            "description": f"The given {parameter} is inexistent",
            "description_es": f"El parámetro {parameter} es inexistente",
        }
        super().__init__(message=[message])


class BaseController:
    """
    Base class for all controllers.
    Implements generic loads, saves and updates to all Model classes.
    """

    object_class = BaseModel
    null_object_class = NullBaseModel

    @classmethod
    def _verify_relations(cls, new_object: BaseModel) -> None:
        """
        Verify if FKs exist. In case they don't it should raise a ValidationError
        Will be call before dumping any new instance to the db
        """
        raise NotImplementedError

    @classmethod
    def save(cls, new_object: BaseModel) -> None:
        """
        Receives any Model object.
        Verifies relations and saves it into the database.
        """
        cls._verify_relations(new_object)
        db.session.add(new_object)
        db.session.commit()

    @classmethod
    def load_all(cls) -> List[BaseModel]:
        """
        Returns all Model objects, filtered by not deleted.
        """
        return cls.object_class.query.filter_by(is_deleted=False).all()

    @classmethod
    def load_by_id(cls, id: int) -> BaseModel:
        """
        Receives an id of a Model object and queries for it.
        Returns the object if found else its Null object.
        """
        # TODO: receive any parameter
        obj = cls.object_class.query.get(id)
        if obj:
            return obj
        if cls.null_object_class is None:
            return None
        return cls.null_object_class(id=id) if cls.null_object_class else None

    @classmethod
    def exists(cls, id: int) -> bool:
        """
        Receives an id of a Model object.
        Returns true if exists else false.
        """
        return bool(cls.load_by_id(id))

    @classmethod
    def _update(cls, obj: BaseModel, **kwargs) -> None:
        """
        Receives a Base model object and args.
        Updates the model with new args.
        """
        obj.update(**kwargs)

    @classmethod
    def load_updated(cls, id: int, **kwargs) -> BaseModel:
        """
        Receives an id of a Model object and args.
        Loads and updates the object with the args, then commits to the database.
        Returns the updated object.
        """
        obj = cls.load_by_id(id)
        if not obj:
            raise InexistentBaseModelInstance(
                obj_name=cls.object_class.name, parameter=f"{cls.object_class.name}_id", value=id
            )

        cls._update(obj, **kwargs)
        db.session.commit()

        return obj

    @classmethod
    def delete(cls, id: int) -> BaseModel:
        """
        Receives an id of a Model object and deletes it from the database.
        Deletion implies the is_deleted column for the object is marked as True.
        """
        obj = cls.load_by_id(id)
        if obj is None:
            return  # raise error?
        obj.delete()
        db.session.commit()
        return obj

class InexistentBaseModelInstance(ValidationError):
    def __init__(self, obj_name: str, parameter: str, value: Any):
        message = {
            "error": f"inexistent_{obj_name}",
            "parameter": parameter,
            "value": value,
            "description": f"The given {parameter} is inexistent",
            "description_es": f"El parámetro {parameter} es inexistente",
        }
        super().__init__(message=[message])