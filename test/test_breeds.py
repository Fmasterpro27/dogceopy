from dogceopy import DogCEO


def test_list():
    dog = DogCEO()

    breeds = dog.breeds.list()

    assert isinstance(breeds, list)
    assert "husky" in breeds

    dog.close()


def test_list_all():
    dog = DogCEO()

    breeds = dog.breeds.list_all()

    assert isinstance(breeds, dict)
    assert "husky" in breeds

    dog.close()


def test_sub_breeds():
    dog = DogCEO()

    subs = dog.breeds.sub_breeds("bulldog")

    assert "english" in subs

    dog.close()


def test_exists():
    dog = DogCEO()

    assert dog.breeds.exists("husky")
    assert not dog.breeds.exists("dragon")

    dog.close()