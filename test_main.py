import pytest
from light import light_my_path
def test_path_inesistente():
    with pytest.raises(FileNotFoundError):
        light_my_path("/unknow/path.txt", "txt")


def test_tmp_folder(tmp_path):
    d = tmp_path / "test_pyTest"
    d.mkdir()

    for i in range(10):
        f1 = d / f"docs{i}.txt"
        f1.write_text(f"test numeber: {i}")

    file_found, file_list = light_my_path(str(d), ".txt")
    assert file_found == 10, f"mi aspetto 10 file .txt, ne ho trovati solo {file_found}"

def test_file_exists():
    path = "/Users/marcovolpe/Downloads/"
    list_test = ['tmb.txt', 'tmb copia 4jpg.txt', 'tmb copia.txt', 'tmb copia 3.txt', 'tmb copia 2.txt', 'tmb copia 5.txt', 'tmb copia 5 2.txt', 'tmb copia 5 3.txt', 'tmb copia 5 4.txt', 'tmb copia 5.txt']
    file_found, file_list = light_my_path(path, ".txt")

    assert file_list == list_test, f"mi aspettavo questi file '{list_test}', ho ricevuto questi: {file_list}"



