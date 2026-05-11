import pytest
from light import light_my_path

def test_path_inesistente():
    with pytest.raises(FileNotFoundError):
        light_my_path("/unknow/path.txt", "txt")


def test_tmp_folder(tmp_path):
    d = tmp_path / "test_pyTest"
    d.mkdir()

    expected_files = ["docs0.txt", "docs1.txt"]
    for i in range(2):
        f1 = d / f"docs{i}.txt"
        f1.write_text(f"test number: {i}")

    f2 = d / f"docs.jpeg"
    f2.write_text(f"test")

    file_list = light_my_path(str(d), ".txt")
    expected_set = set(expected_files)
    file_set = set(file_list)
    assert expected_set == file_set

    assert len(file_list) == len(expected_files)
    for ef in expected_files:
        found = False
        for file in file_list:
            if ef == file:
                found = True
                break
        assert found == True, f"non trovato file {ef}"


def test_list_camparison():
    file_list = ["tmb2", "tmb3", "tmb1", "tmb4"]
    expected_files = ["tmb1", "tmb2", "tmb3"]
    file_list.sort()
    expected_files.sort()
    assert file_list == expected_files


def test_set_camparison():
    file_list = ["tmb2", "tmb3", "tmb1", "tmb3"]
    file_set = set(file_list)
    expected_files = ["tmb1", "tmb2", "tmb3"]
    expected_set = set(expected_files)
    assert file_set == expected_set
