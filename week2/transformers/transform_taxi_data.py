if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    data = data[(data['passenger_count'] != 0) & (data['trip_distance'] != 0)]
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    data.rename(columns={'VendorID': 'vendor_id', 'RatecodeID':'ratecode_id', 'PULocationID': 'pu_location_id', 'DOLocationID':'do_location_id'}, inplace=True)
    # q4
    # print(data['vendor_id'].unique())
    return data

@test
def test_output(output, *args) -> None:
    assert 'vendor_id' in output.columns, 'vendor_id is not in df columns'
    assert output['passenger_count'].isin([0]).sum() == 0, 'Passenger count > 0'
    assert output['trip_distance'].isin([0]).sum() == 0, 'Trip distance > 0'