# BasketItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID associated with the product. | [optional] 
**description** | **str** | A name or short description of the product. | [optional] 
**sub_total** | **float** | Subtotal amount. | [optional] 
**value_added_tax** | **float** | Value added tax amount. | [optional] 
**local_tax** | **float** | Local tax amount. | [optional] 
**delivery_amount** | **float** | Delivery amount. | [optional] 
**charge_total** | **float** | Charge Total amount. | [optional] 
**currency** | **str** | The currency of the original transaction. | [optional] 
**quantity** | **int** | The unit in which the product is sold (e.g. litre, kilogram, etc). Leave empty if the product is sold as a complete unit. | [optional] 
**category** | **str** | Category of the product. | [optional] 
**detailed_category** | **str** | Detailed Category of the product. | [optional] 
**options** | [**list[Option]**](Option.md) | Option details | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


