from pro_filer.actions.main_actions import show_disk_usage, _get_printable_file_path  # NOQA
# import pytest


# @pytest.fixture
# def create_temp_files(tmp_path):
#     # Cria arquivos temporários para os testes
#     file1 = tmp_path / "file1.txt"
#     file2 = tmp_path / "file2.txt"
#     file3 = tmp_path / "file3.txt"

#     # Escreve dados nos arquivos temporários
#     file1.write_text("Test file 1")
#     file2.write_text("Test file 2")
#     file3.write_text("Test file 3")

#     return [str(file1), str(file2), str(file3)]


# def test_show_disk_usage(create_temp_files, capfd):
#     # Obter a lista de arquivos temporários criados
#     all_files = create_temp_files

#     # Chamando a função show_disk_usage para os arquivos temporários
#     context = {
#         "all_files": all_files
#     }
#     show_disk_usage(context)
#     captured_output = capfd.readouterr().out

#     # Verificar a saída capturada
#     assert "file1.txt" in captured_output
#     assert "file2.txt" in captured_output
#     assert "file3.txt" in captured_output
#     assert "Total size: 33" in captured_output

def test_show_disk_usage_empty_files(capfd):
    # Chamando a função show_disk_usage sem arquivos
    context = {
        "all_files": []
    }
    show_disk_usage(context)
    captured_output = capfd.readouterr().out

    # Verificar a saída capturada
    assert "Total size: 0" in captured_output


def test_show_disk_usage_with_files(capsys, tmp_path):
    file_path = tmp_path / "test.py"
    file_path.touch()
    file_path.write_text("test")
    file_name = str(file_path)

    empty_file_path = tmp_path / "empty.py"
    empty_file_path.touch()
    empty_file_name = str(empty_file_path)

    context = {
        "all_files": [file_name, empty_file_name],
    }

    show_disk_usage(context)
    captured_output = capsys.readouterr().out

    file_output = f"'{_get_printable_file_path(file_name)}':".ljust(70)
    out = f"'{_get_printable_file_path(empty_file_name)}':".ljust(70)
    expected_output = f"{file_output} 4 (100%)\n{out} 0 (0%)\nTotal size: 4\n"
    assert captured_output == expected_output
