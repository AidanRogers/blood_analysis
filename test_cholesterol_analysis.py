def test_HDL_analysis():
    from chol_analysis import HDL_analysis
    answer = HDL_analysis(80)
    expected = "Normal"
    assert answer == expected  # looks at whatever comes after it, if it's true
    # then it's happy, pytest will check this assert
    # errors


def test_HDL_analysis_bl():
    from chol_analysis import HDL_analysis
    answer = HDL_analysis(40)
    expected = "Borderline Low"
    assert answer == expected


def test_LDL_analysis():
    from chol_analysis import LDL_analysis
    answer = LDL_analysis(165)
    expected = "High"
    assert answer == expected


def test_fever_check():
    from chol_analysis import fever_check
    new_data = [96.0, 100.5, 105.1, 97]
    answer = fever_check(new_data)
    expected = True
    assert answer == expected
