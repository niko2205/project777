def test_predict_loan_amount():
    data = {
        'age': 30,
        'gender_Male': 1,
        'citizenship_Russia': 1,
        'income': 50000,
        'employment_status_Employed': 1,
        'marital_status_Married': 1,
        'children': 0
    }
    result = predict_loan_amount(pd.DataFrame([data]))
    assert result[0] == pytest.approx(250000, 1000)
