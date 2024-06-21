from rest_framework import response, decorators as rest_decorators, permissions as rest_permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(
    method='post',
    operation_description="Make a payment for a subscription.",
    responses={
        200: openapi.Response(
            description="Payment successful",
            examples={
                'application/json': {
                    'msg': 'Success'
                }
            }
        ),
        400: "Bad request - Invalid data",
        401: "Unauthorized - User not authenticated",
        403: "Forbidden - User does not have permission",
        500: "Server error"
    }
)
@rest_decorators.api_view(["POST"])
@rest_decorators.permission_classes([rest_permissions.IsAuthenticated])
def paySubscription(request):
    return response.Response({"msg": "Success"}, 200)


@swagger_auto_schema(
    method='post',
    operation_description="List all subscriptions for the authenticated user.",
    request_body=None,
    responses={
        200: openapi.Response(
            description="Subscriptions listed successfully",
            examples={
                'application/json': {
                    'msg': 'Success'
                }
            }
        ),
        400: "Bad request - Invalid data",
        401: "Unauthorized - User not authenticated",
        403: "Forbidden - User does not have permission",
        500: "Server error"
    }
)
@rest_decorators.api_view(["POST"])
@rest_decorators.permission_classes([rest_permissions.IsAuthenticated])
def listSubscriptions(request):
    return response.Response({"msg": "Success"}, 200)
