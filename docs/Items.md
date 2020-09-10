# Items

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_type** | **str** | Defines the type of network associated with the device. | 
**ip** | **str** | The IPv4 or IPv6 address of the device if the network assigned one. | [optional] 
**phone_number** | **str** | The devices primary phone number. This value should be supplied directly without any transformation (e.g. removal of spaces, hyphens or parentheses). If this data is available in segregated fields, it should be concatenated using a blank space (\&quot; \&quot;) as a separator. | [optional] 
**carrier_name** | **str** | The network carrier name. | [optional] 
**mobile_country_code** | **str** | The Mobile Country Code (MCC) as described in the ITUs E.212 specification. | [optional] 
**mobile_network_code** | **str** | The Mobile Network Code (MNC) as described in the ITUs E.212 specification. | [optional] 
**subscription_identification_number** | **str** | The Mobile Subscription Identification Number code (MSIN) as described in the ITUs E.212 specification. | [optional] 
**location_area_code** | **str** | The Location Area Code (LAC) is a 16-bit identifier for a region that is covered by a set of network antennas. | [optional] 
**cell_id** | **str** | The Cell ID (CID) is identifier for a specific Base Transceiver Station (BTS) within a specific Location Area Code (LAC). | [optional] 
**standard** | **str** | An identifier of the network standard used. | [optional] 
**mac** | **str** | The MAC address of the device that is connected to the Wi-Fi network. | [optional] 
**ssid** | **str** | The Wi-Fi networks Service Set Identifier (SSID). | [optional] 
**bssid** | **str** | The Wi-Fi networks Basic Service Set Identifier (BSSID). | [optional] 
**user_defined** | [**object**](.md) | A JSON object that can carry any additional information about the network that might be helpful for fraud detection. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


