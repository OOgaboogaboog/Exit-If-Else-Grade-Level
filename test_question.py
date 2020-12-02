import pytest, question

@pytest.mark.parametrize(
  'num1, result',
  [
    (0, '0'),
    (5, '0'),
    (50, '1'),
    (62, '2'),
    (75, '3'),
    (80, '4'),
    (100, '4'),
    (101, 'Invalid input!'),
    (-1, 'Invalid input!')
  ]
)

def test_case(capsys, num1, result):
  
  input_values = [num1]
  
  def mock_input(s):
    return input_values.pop(0)
  question.input = mock_input
  
  question.main()
  out, err = capsys.readouterr()
  out = out.replace('\n', '')

  assert out == result, 'the output should be {} instead of {}'.format(result, out)
  assert err == ''