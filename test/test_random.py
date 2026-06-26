from dogceopy import DogCEO


def test_random_image():
    dog = DogCEO()

    image = dog.random.image()

    assert isinstance(image, str)
    assert image.startswith("https://")

    dog.close()


def test_random_images():
    dog = DogCEO()

    images = dog.random.images(5)

    assert isinstance(images, list)
    assert len(images) == 5

    for image in images:
        assert image.startswith("https://")

    dog.close()