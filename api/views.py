from django.http import JsonResponse
from api.models import Currency
from rest_framework.parsers import JSONParser
from api.serializers import CurrencySerializer
import requests
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def currencies(request):
    if request.method == "PUT":
        # Update database with latest currencies
        try:
            rates = requests.get("https://api.exchangeratesapi.io/latest?base=ZAR").json()['rates']
            print(rates)
            Currency.objects.all().delete()
            for name, value in rates.items():
                print(name)
                print(value)
                Currency(name=name, value=value).save()
        except requests.exceptions.RequestException as e:
            # Show error if failed to connect to api
            return JsonResponse({"code": 200, "message": "Connection Error, Currencies May Not Be The Latest"})
        return JsonResponse({"code": 200, "message": "Updated Currencies"})

    if request.method == "GET":
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)
        return JsonResponse(dict(currencies=list(serializer.data)))

    if request.method == "POST":
        try:
            value1 = Currency.objects.get(name=request.POST['currency'])
            print(value1)
        except Currency.DoesNotExist:
            return JsonResponse({"code": 404, "message": "Currency Does Not Exist"})
        value = CurrencySerializer(value1).data['value']
        print(value)
        return JsonResponse({"result" : float(request.POST['value'])/value})