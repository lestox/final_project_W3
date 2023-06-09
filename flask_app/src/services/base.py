from db import db


def create_entity(entity: db.Model, data: dict, **kwargs):
    """
    Base to create entity

    :param data: json data
    :param entity: entity to create
    :param kwargs: values to check
    """
    if not data:
        return {'message': 'Missing parameters'}, 400
    if entity.get_by(**kwargs):
        return {'message': 'Entity already exists'}, 409
    try:
        entity_inst = entity(**data)
        entity_inst.create()
    except Exception as e:
        return {'error': str(e)}, 500
    return {'message': f'The {entity.__tablename__} created successfully'}, 200


def get_all_entities(entity: db.Model, **filters):
    """
    Base to get all entities

    :param entity: entity to get
    :param filters: filter to apply
    """
    try:
        entity_list = entity.get_all_by(**filters)
        if not entity_list:
            return {'message': "No entities found or it's empty"}, 404
        return {f"all_{entity.__tablename__}": entity_list}, 200
    except Exception as e:
        return {'error': str(e)}, 500


def search_entities(entity, search: str, *columns):
    """
    Base to search entities

    :param entity: entity to search
    :param search: search value
    :param columns: columns to search
    """
    try:
        entity_list = entity.get_entities_by_search_values(search, *columns)
        if not entity_list:
            return {'message': "No entities found or it's empty"}, 404
        return {f"all_{entity.__tablename__}": entity_list}, 200
    except Exception as e:
        return {'error': str(e)}, 500
