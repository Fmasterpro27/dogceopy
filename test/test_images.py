from dogceopy import DogCEO


def test_random():
    dog = DogCEO()

    image = dog.images.random("husky")

    assert image.startswith("https://")

    dog.close()


def test_random_many():
    dog = DogCEO()

    images = dog.images.random_many("husky", 5)

    assert len(images) == 5

    dog.close()


def test_all():
    dog = DogCEO()

    images = dog.images.all("husky")

    assert isinstance(images, list)
    assert len(images) > 0

    dog.close()


def test_sub_random():
    dog = DogCEO()

    image = dog.images.sub_random(
        "bulldog",
        "english",
    )

    assert image.startswith("https://")

    dog.close()


def test_sub_random_many():
    dog = DogCEO()

    images = dog.images.sub_random_many(
        "bulldog",
        "english",
        3,
    )

    assert len(images) == 3

    dog.close()


def test_sub_all():
    dog = DogCEO()

    images = dog.images.sub_all(
        "bulldog",
        "english",
    )

    assert len(images) > 0

    dog.close()