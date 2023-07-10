from pro_filer.actions.main_actions import show_details  # NOQA
import os
from datetime import date
import pytest

pytestmark = pytest.mark.dependency()


def test_show_details_existing_file(capfd):
    # Criando um arquivo temporário para o teste
    file_path = "temp_file.txt"
    file_name = "temp_file.txt"
    file_size = 9
    file_extension = ".txt"
    last_modified = date.today()

    # Escrevendo informações no arquivo temporário
    with open(file_path, "w") as file:
        file.write("Test file")

    # Chamando a função show_details para o arquivo temporário
    context = {
        "base_path": file_path
    }
    show_details(context)
    captured_output = capfd.readouterr().out

    # Verificando se as informações são exibidas corretamente
    assert file_name in captured_output
    assert str(file_size) in captured_output
    assert "file" in captured_output
    assert file_extension in captured_output
    assert str(last_modified) in captured_output

    # Removendo o arquivo temporário
    os.remove(file_path)


def test_show_details_existing_directory(capfd):
    # Criando um diretório temporário para o teste
    dir_path = "temp_dir"
    dir_name = "temp_dir"
    last_modified = date.today()

    # Criando o diretório temporário
    os.mkdir(dir_path)

    # Chamando a função show_details para o diretório temporário
    context = {
        "base_path": dir_path
    }
    show_details(context)
    captured_output = capfd.readouterr().out

    # Verificando se as informações são exibidas corretamente
    assert dir_name in captured_output
    assert "directory" in captured_output
    assert "[no extension]" in captured_output
    assert str(last_modified) in captured_output

    # Removendo o diretório temporário
    os.rmdir(dir_path)


def test_show_details_non_existing_file(capfd):
    # Chamando a função show_details para um arquivo que não existe
    context = {
        "base_path": "non_existing_file.txt"
    }
    show_details(context)
    captured_output = capfd.readouterr().out

    # Verificando se a mensagem de arquivo inexistente é exibida corretamente
    assert "File 'non_existing_file.txt' does not exist" in captured_output


def test_show_details_file_no_extension(capfd):
    # Criando um arquivo temporário sem extensão para o teste
    file_path = "temp_file"
    file_name = "temp_file"
    file_size = 9
    last_modified = date.today()

    # Criando o arquivo temporário
    with open(file_path, "w") as file:
        file.write("Test file")

    # Chamando a função show_details para o arquivo temporário sem extensão
    context = {
        "base_path": file_path
    }
    show_details(context)
    captured_output = capfd.readouterr().out

    # Verificando se as informações são exibidas corretamente
    assert file_name in captured_output
    assert str(file_size) in captured_output
    assert "file" in captured_output
    assert "[no extension]" in captured_output
    assert str(last_modified) in captured_output

    # Removendo o arquivo temporário
    os.remove(file_path)


@pytest.mark.dependency(
    depends=[
        "test_show_details_existing_file",
        "test_show_details_existing_directory",
        "test_show_details_non_existing_file",
        "test_show_details_file_no_extension",
    ]
)
def test_final():
    pass
