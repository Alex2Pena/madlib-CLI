# @pytest.mark.skip("testing")
from madlib_cli.madlib import read_template, parsed_madlib, merged_template

# Create and test a read_template function that takes in a path to text file and returns a stripped string of the file’s contents.
def test_read_template():
    actual = read_template('./madlib_cli/assets/test_text_template.txt')
    expected = "I am a {adjective} {adjective} test text file!"
    assert actual == expected

# Create and test a parse function that takes in a template string and returns a string with language parts removed and a separate list of those language parts.
def test_parsed_madlib2():
    actual_stripped, actual_parts = parsed_madlib("a {noun} and {verb} and an {adjective}")
    expected_stripped = "a {} and {} and an {}"
    expected_parts = ["noun", "verb", "adjective"]
    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts 

# Create and test a merge function that takes in a “bare” template and a list of user entered language parts, and returns a string with the language parts inserted into the template.
def test_merge_madlib():
    actual = merged_template("A {} and {} {}.", ["dark", "stormy", "night"])
    expected = "A dark and stormy night."
    assert actual == expected
    







