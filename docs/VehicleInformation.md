# VehicleInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monthly_payment** | **float** | The lead&#39;s monthly auto loan payment | [optional] 
**estimated_mileage** | **float** | The vehicle&#39;s estimated number of miles driven | [optional] 
**vehicle_identification_number** | **str** | The vehicle identification number (VIN) of the financed vehicle | [optional] 
**vehicle_uuid** | **str** | A vehicle UUID that corresponds to a valid combination of vehicle year, make, model, and trim. See the [vehicle utility endpoints](https://engine.tech/docs/api-reference/#even-financial-api-ui-utils) | [optional] 

## Example

```python
from openapi_client.models.vehicle_information import VehicleInformation

# TODO update the JSON string below
json = "{}"
# create an instance of VehicleInformation from a JSON string
vehicle_information_instance = VehicleInformation.from_json(json)
# print the JSON string representation of the object
print(VehicleInformation.to_json())

# convert the object into a dict
vehicle_information_dict = vehicle_information_instance.to_dict()
# create an instance of VehicleInformation from a dict
vehicle_information_from_dict = VehicleInformation.from_dict(vehicle_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


