from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from geekSchoolApp.models import FAQ
from .serializers import FAQSerializer
from rest_framework.permissions import IsAuthenticated


# View for listing all FAQs
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllFAQs(request):
    faqs = FAQ.objects.all()
    serializer = FAQSerializer(faqs, many=True)
    return Response({
        "status": True,
        "data": serializer.data
        })

# View for getting FAQ by id
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getFAQById(request, id):
    try:
        faq = FAQ.objects.get(id=id)
    except FAQ.DoesNotExist:
        return Response({"error": "FAQ not found"}, status=404)

    serializer = FAQSerializer(faq)
    return Response(serializer.data)

# View for adding a new issue
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addFAQ(request):
    serializer = FAQSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateFAQ(request, id):
    try:
        faq = FAQ.objects.get(id=id)
        serializer = FAQSerializer(faq, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    except FAQ.DoesNotExist:
        return Response({"error": "FAQ not found"}, status=404)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteFAQ(request, id):
    try:
        faq = FAQ.objects.get(id=id)
    except FAQ.DoesNotExist:
        return Response({"error": "FAQ not found"}, status=404)

    faq.delete()
    return Response({"message": "FAQ deleted successfully"})
