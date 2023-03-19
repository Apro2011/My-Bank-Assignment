import graphene
from graphene_django import DjangoObjectType
from myapp.models import BankDetails


class BankDetailsType(DjangoObjectType):
    class Meta:
        model = BankDetails


class Query(graphene.ObjectType):
    details = graphene.List(BankDetailsType)
    details_by_bank_branch = graphene.List(BankDetailsType, bank_branch=graphene.String())

    def resolve_details(root, info, **kwargs):
        return BankDetails.objects.all()
    
    def resolve_details_by_bank_branch(root, info, bank_branch):
        return BankDetails.objects.filter(branch=bank_branch)
    

schema = graphene.Schema(query=Query)