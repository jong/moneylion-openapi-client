# VehicleDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** | Year of the vehicle. | 
**make** | **str** | Make of the vehicle. | 
**model** | **str** | Model of the vehicle. | 
**trim** | **str** | Trim of the vehicle. | 
**uuid** | **str** | A unique identifier for this vehicle. | 
**ucg_vehicle_id** | **int** | NADA Used Card Guide vehicle id. | 

## Example

```python
from openapi_client.models.vehicle_details import VehicleDetails

# TODO update the JSON string below
json = "{}"
# create an instance of VehicleDetails from a JSON string
vehicle_details_instance = VehicleDetails.from_json(json)
# print the JSON string representation of the object
print(VehicleDetails.to_json())

# convert the object into a dict
vehicle_details_dict = vehicle_details_instance.to_dict()
# create an instance of VehicleDetails from a dict
vehicle_details_from_dict = VehicleDetails.from_dict(vehicle_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


