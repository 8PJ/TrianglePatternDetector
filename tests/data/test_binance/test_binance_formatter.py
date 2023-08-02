from data.binance.binance_formatter import format_bincance

from datetime import datetime

def test_dataframe_has_correct_shape():
    json_data = [[1690966800000, '29489.54000000', '29501.43000000', '29419.80000000', '29453.52000000', '1694.81848000', 1690970399999, '49931674.71823270', 28880, '633.35104000', '18654916.65394930', '0'], [1690970400000, '29453.52000000', '29534.33000000', '29442.00000000', '29531.47000000', '866.64979000', 1690973999999, '25552651.79083950', 21174, '484.53428000', '14285650.57205770', '0'], [1690974000000, '29531.46000000', '29556.00000000', '29501.70000000', '29546.52000000', '713.23614000', 1690977599999, '21056329.55900010', 16843, '351.82863000', '10386843.97810530', '0']]

    price_data_df = format_bincance(json_data)

    assert price_data_df.shape == (3, 7)

def test_all_columns_are_present():
    json_data = [[1690966800000, '29489.54000000', '29501.43000000', '29419.80000000', '29453.52000000', '1694.81848000', 1690970399999, '49931674.71823270', 28880, '633.35104000', '18654916.65394930', '0'], [1690970400000, '29453.52000000', '29534.33000000', '29442.00000000', '29531.47000000', '866.64979000', 1690973999999, '25552651.79083950', 21174, '484.53428000', '14285650.57205770', '0'], [1690974000000, '29531.46000000', '29556.00000000', '29501.70000000', '29546.52000000', '713.23614000', 1690977599999, '21056329.55900010', 16843, '351.82863000', '10386843.97810530', '0']]

    price_data_df = format_bincance(json_data)

    # assert all columns are present
    assert 'open' in price_data_df.columns
    assert 'close' in price_data_df.columns
    assert 'high' in price_data_df.columns
    assert 'low' in price_data_df.columns
    assert 'volume' in price_data_df.columns
    assert 'number_transactions' in price_data_df.columns
    assert 'datetime' in price_data_df.columns

def test_time_correctly_converted():
    json_data = [[1690974000000, '29531.46000000', '29571.38000000', '29501.70000000', '29545.00000000', '805.19522000', 1690977599999, '23774085.37593960', 19198, '406.65353000', '12007138.10483550', '0']]

    price_data_df = format_bincance(json_data)

    assert price_data_df['datetime'][0] == str(datetime.fromtimestamp(1690974000000 / 1000))