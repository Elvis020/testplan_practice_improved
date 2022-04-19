import sys

from testplan import test_plan
from testplan.common.utils.context import context
from testplan.testing.multitest import MultiTest, testcase, testsuite
from testplan.testing.multitest.driver.http import (
    HTTPServer,
    HTTPClient,
)


@testsuite
class CalculatorSuite(object):

    @testcase
    def basic_add(self, env, result):
        print("Client sent a GET request to /add")
        env.http_client.get(api="/add?input_1=100&input_2=45")
        response = env.http_client.receive().json()
        total = int(response["total"])
        result.equal(145, total, "Assert if addition total is working as it should.")

    @testcase
    def basic_subtract(self, env, result):
        print("Client sent a GET request to /subtract")
        env.http_client.get(api="/subtract?input_1=100&input_2=5")
        response = env.http_client.receive().json()
        difference = int(response["difference"])
        result.equal(95, difference, "Assert if subtraction endpoint is working well.")

    @testcase
    def basic_multiply(self, env, result):
        print("Client sent a GET request to /product")
        env.http_client.get(api="/multiply?input_1=100&input_2=5")
        response = env.http_client.receive().json()
        product = int(response["product"])
        result.equal(500, product, "Assert if multiply endpoint is working well.")

    @testcase
    def basic_divide(self, env, result):
        print("Client sent a GET request to /divide")
        env.http_client.get(api="/divide?input_1=100&input_2=50")
        response = env.http_client.receive().json()
        product = int(response["factor"])
        result.equal(2.0, product, "Assert if division endpoint is working well.")

    @testcase
    def basic_divide_with_zero_denominator(self, env, result):
        print("Client sent a GET request to /divide when the denominator is 0")
        env.http_client.get(api="/divide?input_1=100&input_2=0")
        response = env.http_client.receive().json()
        product = response["factor"]
        result.equal("Not divisible by zero!", product, "Assert if division endpoint is working well, if the denominator is zero.")

    @testcase
    def basic_modulo(self, env, result):
        print("Client sent a GET request to /modulo")
        env.http_client.get(api="/modulo?input_1=7&input_2=2")
        response = env.http_client.receive().json()
        modulo = int(response["modulo"])
        result.equal(1, modulo, "Assert if modulo endpoint is working well.")

    @testcase
    def basic_exponent(self, env, result):
        print("Client sent a GET request to /math_exponent")
        env.http_client.get(api="/math_exponent?input_1=7&input_2=2")
        response = env.http_client.receive().json()
        exponent_result = int(response["math_exponent"])
        result.equal(49, exponent_result, "Assert if math_exponent endpoint is working well.")

    @testcase
    def basic_natural_log(self, env, result):
        print("Client sent a GET request to /natural_log")
        env.http_client.get(api="/natural_log?input_1=7&base=2")
        response = env.http_client.receive().json()
        log_result = int(response["natural_log_result"])
        result.equal(2, log_result, "Assert if natural_log endpoint is working well.")


@test_plan(name='Calculation')
def main(plan):
    test = MultiTest(name='CalculationTest',
                     suites=[CalculatorSuite()],
                     environment=[
                         HTTPServer(name="http_server"),
                         HTTPClient(
                             name="http_client",
                             host=context("http_server", "{{host}}"),
                             port=context("http_server", "5000"),
                         ),
                     ], )
    plan.add(test)


if __name__ == '__main__':
    sys.exit(not main())
