from main.data.models import Dummy


# Test to ensure a new record can be created from the models imported
def test_new_dummy_record(new_dummy):
    """
    GIVEN a Dummy model
    WHEN a new Feed is created
    THEN check that a new id is generated
    """
    assert new_dummy.name == 'FancyName'
    assert new_dummy.comment == 'Some random comment'
    assert type(new_dummy.id) is int

