from pro_filer.actions.main_actions import show_disk_usage  # NOQA
# import os
import pytest


@pytest.fixture
def create_temp_files(tmp_path):
    # Cria arquivos temporários para os testes
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    file3 = tmp_path / "file3.txt"

    # Escreve dados nos arquivos temporários
    file1.write_text("Test file 1")
    file2.write_text("Test file 2")
    file3.write_text("Test file 3")

    return [str(file1), str(file2), str(file3)]


def test_show_disk_usage(create_temp_files, capfd):
    # Obter a lista de arquivos temporários criados
    all_files = create_temp_files

    # Chamando a função show_disk_usage para os arquivos temporários
    context = {
        "all_files": all_files
    }
    show_disk_usage(context)
    captured_output = capfd.readouterr().out

    # Verificar a saída capturada
    assert "file1.txt" in captured_output
    assert "file2.txt" in captured_output
    assert "file3.txt" in captured_output
    assert "Total size: 33" in captured_output


def test_show_disk_usage_empty_files(capfd):
    # Chamando a função show_disk_usage sem arquivos
    context = {
        "all_files": []
    }
    show_disk_usage(context)
    captured_output = capfd.readouterr().out

    # Verificar a saída capturada
    assert "Total size: 0" in captured_output


def test_show_disk_usage_file_order(create_temp_files, capfd):
    # Obter a lista de arquivos temporários criados
    all_files = create_temp_files

    # Alterar a ordem dos arquivos
    all_files = [all_files[1], all_files[0], all_files[2]]

    # Chamando a função show_disk_usage para os arquivos
    # temporários com ordem alterada
    context = {
        "all_files": all_files
    }
    show_disk_usage(context)
    output = capfd.readouterr().out

    # Verificar a saída capturada
    assert output.index("file2.txt") < output.index("file1.txt")
    assert output.index("file1.txt") < output.index("file3.txt")
    assert "Total size: 33" in output
