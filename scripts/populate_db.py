# standard library
import os

from shutil import copyfile

# django
from django.conf import settings

from base.mockups import Mockup
from department.enums import ValidationCodeStatus


def run():
    mockup = Mockup()

    # Create a validation code
    mockup.create_validation_code(
        user=None, code="ABCD1234", status=ValidationCodeStatus.AVAILABLE
    )

    # Create 5 parkings
    for i in range(5):
        mockup.create_parking(number=int(f"30{i}"))

    # setup imagenes de anuncios
    if not os.path.exists(settings.MEDIA_ROOT):
        os.makedirs(settings.MEDIA_ROOT)

    if not os.path.exists(f"{settings.MEDIA_ROOT}test_files/"):
        os.makedirs(f"{settings.MEDIA_ROOT}test_files/")

    # anuncio huevos de galline libre
    huevos_path = f"{settings.BASE_DIR}/base/test_assets/huevos.jpg"
    huevos_media_path = "test_files/huevos.jpg"
    huevos_final_path = f"{settings.MEDIA_ROOT}{huevos_media_path}"
    copyfile(huevos_path, huevos_final_path)

    mockup.create_announcement(
        title="Vendo huevos de campo",
        description=(
            """
            Los mejores huevos de gallina libre, traidos desde narnia a tu casa.
            """
        ),
        image=huevos_media_path,
    )

    # anuncio antigenos
    antigenos_path = f"{settings.BASE_DIR}/base/test_assets/antigenos.jpg"
    antigenos_media_path = "test_files/antigenos.jpg"
    antigenos_final_path = f"{settings.MEDIA_ROOT}{antigenos_media_path}"
    copyfile(antigenos_path, antigenos_final_path)

    mockup.create_announcement(
        title="Vendo tests de antigenos",
        description=(
            """
            Vendo test de antígenos 2x10.000, 1x6.000, se reparten hasta las
             12 PM por si alquien necesita de urgencia, hablarme al +56942473658.
            """
        ),
        image=antigenos_media_path,
    )

    # Create 5 visits and 5 departments
    mockup.create_visit(
        name="Rodrigo", first_last_name="Gonzalez", second_last_name="Garcia"
    )
    mockup.create_visit(
        name="Francisca", first_last_name="Diaz", second_last_name="Muñoz"
    )
    mockup.create_visit(name="Mateo", first_last_name="Soto", second_last_name="Perez")
    mockup.create_visit(
        name="Lucas", first_last_name="Torres", second_last_name="Contreras"
    )
    mockup.create_visit(
        name="Fernanda", first_last_name="Silva", second_last_name="Sepulveda"
    )
