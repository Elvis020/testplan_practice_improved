import sys

from testplan import test_plan
from testplan.testing.multitest import MultiTest, testcase, testsuite

@testsuite
class CalculatorSuite(object):

    @testcase
    def basic_add(self, env, result):
        print("Client sent a GET request to /add")
        env.http_client.get(api="/add?a=100&b=45")
        response = env.http_client.receive().json()
        total = int(response["total"])
        result.equal(145, total, "Assert if addition total is working as it should.")

    @testcase
    def basic_subtract(self, env, result):
        print("Client sent a GET request to /subtract")
        env.http_client.get(api="/subtract?a=100&b=45")
        response = env.http_client.receive().json()
        difference = int(response["difference"])
        result.equal(55, difference, "Assert if subtraction endpoint is working well.")

    @testcase
    def basic_multiply(self, env, result):
        print("Client sent a GET request to /product")
        env.http_client.get(api="/multiply?a=100&b=45")
        response = env.http_client.receive().json()
        product = int(response["product"])
        result.equal(4500, product, "Assert if multiply endpoint is working well.")

    @testcase
    def basic_divide(self, env, result):
        print("Client sent a GET request to /divide")
        env.http_client.get(api="/divide?a=100&b=50")
        response = env.http_client.receive().json()
        product = int(response["factor"])
        result.equal(2, product, "Assert if division endpoint is working well.")


@test_plan(name='Calculation')
def main(plan):
    test = MultiTest(name='CalculationTest',
                     suites=[CalculatorSuite()])
    plan.add(test)


if __name__ == '__main__':
  sys.exit(not main())