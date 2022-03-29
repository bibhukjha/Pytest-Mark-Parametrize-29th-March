import main
import pytest

@pytest.mark.parametrize("num,output",[(5,True),(2,False),(10,True),(7,False),(9,True)])
def test_divby5_1(num, output):
    out1 = main.divby5(num)
    assert out1 == output

@pytest.mark.parametrize("num2,output2",[(14,True),(20,False)])
def test_divby7_1(num2, output2):
    out1 = main.divby7(num2)
    assert out1 == output2

@pytest.mark.parametrize("num3, output3",[(17,False),(18,True)])
def test_divby9_1(num3, output3):
    out1 = main.divby9(num3)
    assert out1 == output3

@pytest.mark.parametrize("num4,output4",[(121, True),(34,False)])
def test_divby11_1(num4, output4):
    out1 = main.divby11(num4)
    assert out1 == output4
