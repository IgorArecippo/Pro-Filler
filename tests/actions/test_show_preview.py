from pro_filer.actions.main_actions import show_preview  # NOQA
import pytest

pytestmark = pytest.mark.dependency()


def test_show_preview_empty(capfd):
    context = {
        "all_files": [],
        "all_dirs": []
    }
    expected_output = "Found 0 files and 0 directories\n"

    show_preview(context)
    captured_output = capfd.readouterr().out

    assert captured_output.strip() == expected_output.strip()


# def test_show_preview_less_than_5_elements(capfd):
#     context = {
#         "all_files": ["file1.txt", "file2.txt"],
#         "all_dirs": ["dir1", "dir2"]
#     }
#     expected_output = "Found 2 files and 2 directories\n"
#     expected_output += "First 2 files: ['file1.txt', 'file2.txt']\n"
#     expected_output += "First 2 directories: ['dir1', 'dir2']"

#     show_preview(context)
#     captured_output = capfd.readouterr().out

#     assert captured_output.strip() == expected_output.strip()


def test_show_preview_more_than_5_elements(capfd):
    context = {
        "all_files": [
            "file1.txt",
            "file2.txt", "file3.txt", "file4.txt", "file5.txt", "file6.txt"],
        "all_dirs": ["dir1", "dir2", "dir3", "dir4", "dir5", "dir6"]
    }
    e = "Found 6 files and 6 directories\n"
    e += "First 5 files: ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt']\n"
    e += "First 5 directories: ['dir1', 'dir2', 'dir3', 'dir4', 'dir5']"

    show_preview(context)
    captured_output = capfd.readouterr().out

    assert captured_output.strip() == e.strip()


def test_show_preview_exactly_5_elements(capfd):
    context = {
        "all_files": [
            "file1.txt",
            "file2.txt",
            "file3.txt",
            "file4.txt", "file5.txt"],
        "all_dirs": ["dir1", "dir2", "dir3", "dir4", "dir5"]
    }
    expected_output = "Found 5 files and 5 directories\n"
    expected_output += "First 5 files: ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt']\n"
    expected_output += "First 5 directories: ['dir1', 'dir2', 'dir3', 'dir4', 'dir5']"

    show_preview(context)
    captured_output = capfd.readouterr().out

    assert captured_output.strip() == expected_output.strip()


@pytest.mark.dependency(
    depends=[
        "test_show_preview_empty",
        "test_show_preview_less_than_5_elements",
        "test_show_preview_more_than_5_elements",
        "test_show_preview_exactly_5_elements",
    ]
)
def test_final():
    pass
