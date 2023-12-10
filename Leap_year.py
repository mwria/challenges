

## my code ##


def is_leap_year(year):
    y = year
    if y%100 == 0: 
        if y%400 == 0:
            return True
        else:
            return False
    elif  y%4 == 0:
            return True
    else:
        if y%100 != 0:
            return False
            
## given code ##            

@test.describe("Example tests")
def example_tests():
    
    @test.it("Year 2020 is a leap year")
    def test_year_2020():
        test.assert_equals(is_leap_year(2020), True, "Incorrect answer for year = 2020")
    
    @test.it("Year 2000 is a leap year")
    def test_year_2000():
        test.assert_equals(is_leap_year(2000), True, "Incorrect answer for year = 2000")

    @test.it("Year 2015 is not a leap year")
    def test_year_2015():
        test.assert_equals(is_leap_year(2015), False, "Incorrect answer for year = 2015")

    @test.it("Year 2100 is not a leap year")
    def test_year_2100():
        test.assert_equals(is_leap_year(2100), False, "Incorrect answer for year = 2100")

