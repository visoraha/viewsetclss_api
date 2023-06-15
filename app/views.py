from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from app.models import *
from app.serializers import *
from rest_framework.response import Response

class ProductCrudVS(ViewSet):
    def list(self, request):
        PQS=Products.objects.all()
        PSD=ProductSerializers(PQS,many=True)
        return Response(PSD.data)

    def create(self,request):
        SD=ProductSerializers(data=request.data)
        if SD.is_valid():
            SD.save()
            return Response({'Success':'Product is Created'})
        else:
            return Response({'Failed':'Product is not created'})
    
    def retrieve(self,request,pk):
        SPO=Products.objects.get(pk=pk)
        SPD=ProductSerializers(SPO)
        return Response(SPD.data)
    
    def update(self,request,pk):
        SPO=Products.objects.get(pk=pk)
        SPD=ProductSerializers(SPO,data=request.data)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Product is updated'})
        else:
            return Response({'Failed':'Prodct is Not Updated'})
    
    def partial_update(self,request,pk):
        SPO=Products.objects.get(pk=pk)
        SPD=ProductSerializers(SPO,data=request.data,partial=True)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Product is updated'})
        else:
            return Response({'Failed':'Prodct is Not Updated'})
    def destroy(self,request,pk):
        Products.objects.get(pk=pk).delete()
        return Response({'Deleted':'Product is deleted'})
    





                            









        

    
















