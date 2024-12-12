from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from geekSchoolApp.models import Event
from .serializers import EventSerializer
from rest_framework.permissions import IsAuthenticated


# View for listing all events
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllEvents(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response({
        "status": True,
        "data": serializer.data
        })

# View for getting event by id
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getEventById(request, id):
    try:
        event = Event.objects.get(id=id)
    except Event.DoesNotExist:
        return Response({"error": "Event not found"}, status=404)

    serializer = EventSerializer(event)
    return Response(serializer.data)

# View for adding a new issue
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addEvent(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateEvent(request, id):
    try:
        event = Event.objects.get(id=id)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    except Event.DoesNotExist:
        return Response({"error": "Event not found"}, status=404)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteEvent(request, id):
    try:
        event = Event.objects.get(id=id)
    except Event.DoesNotExist:
        return Response({"error": "Event not found"}, status=404)

    event.delete()
    return Response({"message": "Event deleted successfully"})
