from django.test.testcases import TestCase
import graphene
from mysite.schema import Query


class BankQueryTest(TestCase):
    def setUp(self):
        self.query = """
            query {
                detailsByBankBranch(bankBranch: "BHANDUP") {
                    ifsc
                    city
                    bankId
                    branch
                    bankName
                    state
                    district
                    address
                }
            }
        
        """
    def test_branch_details(self):
        schema = graphene.Schema(query=Query)
        result = schema.execute(self.query)
        self.assertIsNone(result.errors)