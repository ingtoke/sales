import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import collections
import time


def preprocess():

    path = 'D:/'
    file_name = 'data.csv'

    start = time.time()

    # load data
    data = pd.read_csv(path + file_name)

    # drop rows with negative 'Order_Qty' value
    data = data[data.Order_Qty >= 0]

    # extract 'Order_Qty' column to be used as labels
    y = data['Order_Qty'].values
    # replace all non-zero values with one
    y[y > 0] = 1
    # drop 'Order_Qty' column
    data.drop('Order_Qty', axis=1, inplace=True)
    # total number of valid data sets
    data_size = len(y)
    dict_order_qty = dict(collections.Counter(y))
    keys_order_qty = list(dict_order_qty.keys())

    # extract 'Country' column
    countries = data['Country'].values
    # compute frequency of each country
    dict_country = dict(collections.Counter(countries))
    keys_country = list(dict_country.keys())
    top_3_countries = collections.Counter(countries).most_common(3)
    # print(top_3_countries)
    for i in range(0, len(countries)):
        country = countries[i]
        if country != 'US' and country != 'SA' and country != 'QA':
            countries[i] = 'other'
    # one-hot encode 'Country'
    le_country = LabelEncoder()
    labels_country = le_country.fit_transform(countries)
    country_b = np.zeros((len(countries), 4), dtype=int)
    country_b[np.arange(len(countries), dtype=int), labels_country] = 1
    # print(country_b)

    # extract 'Coverage' column
    coverage = data['Coverage'].values
    dict_coverage = dict(collections.Counter(coverage))
    keys_coverage = list(dict_coverage.keys())
    # one-hot encode 'Coverage'
    le_coverage = LabelEncoder()
    labels_coverage = le_coverage.fit_transform(coverage)
    coverage_b = np.zeros((len(coverage), 2), dtype=int)
    coverage_b[np.arange(len(coverage), dtype=int), labels_coverage] = 1
    # print(coverage_b)

    # extract 'SKU' column
    skus = [str(i) for i in data['SKU'].values]
    # compute frequency of each SKU
    dict_sku = dict(collections.Counter(skus))
    keys_sku = list(dict_sku.keys())
    top_5_skus = collections.Counter(skus).most_common(5)
    # print(top_5_skus)
    for i in range(0, len(skus)):
        sku = skus[i]
        if sku != '10070735' and sku != '10019577' and sku != '10108817' and sku != '10106342' and sku != '10064539':
            skus[i] = 'other'
    # one-hot encode 'SKU'
    le_sku = LabelEncoder()
    labels_sku = le_sku.fit_transform(skus)
    sku_b = np.zeros((len(skus), 6), dtype=int)
    sku_b[np.arange(len(skus), dtype=int), labels_sku] = 1
    # print(sku_b)

    # extract 'SKU_Category' column
    sku_categories = [str(i) for i in data['SKU_Category'].values]
    # compute frequency of each SKU category
    dict_sku_category = dict(collections.Counter(sku_categories))
    keys_sku_category = list(dict_sku_category.keys())
    top_5_sku_categories = collections.Counter(sku_categories).most_common(5)
    # print(top_5_sku_categories)
    for i in range(0, len(sku_categories)):
        sku_category = sku_categories[i]
        if sku_category != '33346' and sku_category != '10322' and sku_category != '14345' and sku_category != '10321' and sku_category != '14382':
            sku_categories[i] = 'other'
    # one-hot encode 'SKU_Category'
    le_sku_category = LabelEncoder()
    labels_sku_category = le_sku_category.fit_transform(sku_categories)
    sku_category_b = np.zeros((len(sku_categories), 6), dtype=int)
    sku_category_b[np.arange(len(sku_categories), dtype=int), labels_sku_category] = 1
    # print(sku_category_b)

    # extract 'EB_Flag' column
    eb_flag = data['EB_Flag'].values
    # compute frequency of each EB_Flag
    dict_eb_flag = dict(collections.Counter(eb_flag))
    keys_eb_flag = list(dict_eb_flag.keys())
    # one-hot encode 'EB_Flag'
    le_eb_flag = LabelEncoder()
    labels_eb_flag = le_eb_flag.fit_transform(eb_flag)
    eb_flag_b = np.zeros((len(eb_flag), 2), dtype=int)
    eb_flag_b[np.arange(len(eb_flag), dtype=int), labels_eb_flag] = 1
    # print(eb_flag_b)

    # extract 'RFQ_TYPE' column
    rfq_type = [str(i) for i in data['RFQ_TYPE'].values]
    # compute frequency of each RFQ_TYPE
    dict_rfq_type = dict(collections.Counter(rfq_type))
    keys_rfq_type = list(dict_rfq_type.keys())
    # One-hot encode RFQ_Type
    le_rfq_type = LabelEncoder()
    labels_rfq_type = le_rfq_type.fit_transform(rfq_type)
    rfq_type_b = np.zeros((len(rfq_type), 9), dtype=int)
    rfq_type_b[np.arange(len(rfq_type), dtype=int), labels_rfq_type] = 1

    # extract 'List_Price' column
    list_price = data['List_Price'].values
    # scale data to the [0, 1] range
    min_max_scaler = MinMaxScaler()
    list_price_n = np.array(min_max_scaler.fit_transform(np.array(list_price).reshape(-1, 1)))

    # extract 'RFQ_Price' column
    rfq_price = data['RFQ_Price'].values
    # scale data to the [0, 1] range
    min_max_scaler = MinMaxScaler()
    rfq_price_n = np.array(min_max_scaler.fit_transform(np.array(rfq_price).reshape(-1, 1)))
    # print(rfq_price_n)

    # extract 'List_Price*RFQ_Qty' column
    list_price_x_rfq_qty = data['List_Price*RFQ_Qty'].values
    # scale data to the [0, 1] range
    min_max_scaler = MinMaxScaler()
    list_price_x_rfq_qty_n = np.array(min_max_scaler.fit_transform(np.array(list_price_x_rfq_qty).reshape(-1, 1)))
    # print(list_price_x_rfq_qty_n)

    # extract 'RFQ_Price*Order_Qty' column
    rfq_price_x_order_qty = data['RFQ_Price*Order_Qty'].values
    # scale data to the [0, 1] range
    min_max_scaler = MinMaxScaler()
    rfq_price_x_order_qty_n = np.array(min_max_scaler.fit_transform(np.array(rfq_price_x_order_qty).reshape(-1, 1)))
    # print(rfq_price_x_order_qty_n)

    country_b = np.array(country_b)
    coverage_b = np.array(coverage_b)
    sku_b = np.array(sku_b)
    sku_category_b = np.array(sku_category_b)
    eb_flag_b = np.array(eb_flag_b)
    rfq_type_b = np.array(rfq_type_b)
    list_price_n = list_price_n
    rfq_price_n = rfq_price_n
    list_price_x_rfq_qty_n = list_price_x_rfq_qty_n
    rfq_price_x_order_qty_n = rfq_price_x_order_qty_n

    X = np.concatenate((country_b, coverage_b), axis=1)
    X = np.concatenate((X, sku_b), axis=1)
    X = np.concatenate((X, sku_category_b), axis=1)
    X = np.concatenate((X, eb_flag_b), axis=1)
    X = np.concatenate((X, rfq_type_b), axis=1)
    X = np.concatenate((X, list_price_n), axis=1)
    X = np.concatenate((X, rfq_price_n), axis=1)
    X = np.concatenate((X, list_price_x_rfq_qty_n), axis=1)
    X = np.concatenate((X, rfq_price_x_order_qty_n), axis=1)

    # # compute percentage of each key
    # for i in range(0, len(keys_order_qty)):
    #     key = keys_order_qty[i]
    #     dict_order_qty[key] = dict_order_qty.get(key) / data_size
    # for i in range(0, len(keys_country)):
    #     key = keys_country[i]
    #     dict_country[key] = dict_country.get(key) / data_size
    # for i in range(0, len(keys_sku)):
    #     key = keys_sku[i]
    #     dict_sku[key] = dict_sku.get(key) / data_size
    # for i in range(0, len(keys_sku_category)):
    #     key = keys_sku_category[i]
    #     dict_sku_category[key] = dict_sku_category.get(key) / data_size
    # for i in range(0, len(keys_eb_flag)):
    #     key = keys_eb_flag[i]
    #     dict_eb_flag[key] = dict_eb_flag.get(key) / data_size
    # for i in range(0, len(keys_rfq_type)):
    #     key = keys_rfq_type[i]
    #     dict_rfq_type[key] = dict_rfq_type.get(key) / data_size

    # # write result into a text file
    # file = open('result.txt', 'w')
    # file.write('Number of valid data sets: {}'.format(data_size))
    # file.write("\n\nCountry:")
    # file.write('\nKeys: {}'.format(keys_country))
    # file.write('\nNo. of keys: {}'.format(len(keys_country)))
    # file.write('\nFrequency of each category: {}'.format(dict_country))
    # file.write("\n\nCoverage:")
    # file.write('\nKeys: {}'.format(keys_coverage))
    # file.write('\nNo. of keys: {}'.format(len(keys_coverage)))
    # file.write('\nFrequency of each category: {}'.format(dict_coverage))
    # file.write("\n\nSKU:")
    # file.write('\nKeys: {}'.format(keys_sku))
    # file.write('\nNo. of keys: {}'.format(len(keys_sku)))
    # file.write('\nFrequency of each category: {}'.format(dict_sku))
    # file.write("\n\nSKU_Category:")
    # file.write('\nKeys: {}'.format(keys_sku_category))
    # file.write('\nNo. of keys: {}'.format(len(keys_sku_category)))
    # file.write('\nFrequency of each category: {}'.format(dict_sku_category))
    # file.write("\n\nEB_Flag:")
    # file.write('\nKeys: {}'.format(keys_eb_flag))
    # file.write('\nNo. of keys: {}'.format(len(keys_eb_flag)))
    # file.write('\nFrequency of each category: {}'.format(dict_eb_flag))
    # file.write("\n\nRFQ_Type:")
    # file.write('\nKeys: {}'.format(keys_rfq_type))
    # file.write('\nNo. of keys: {}'.format(len(keys_rfq_type)))
    # file.write('\nFrequency of each category: {}'.format(dict_rfq_type))
    # file.write("\n\nOrder_Qty:")
    # file.write('\nKeys: {}'.format(keys_order_qty))
    # file.write('\nNo. of keys: {}'.format(len(keys_order_qty)))
    # file.write('\nFrequency of each category: {}'.format(dict_order_qty))
    # file.close()

    end = time.time()

    print('\nPREPROCESSING COMPLETE\nTime elapsed: {:.2f} {}'.format((end - start), 'seconds'))

    return X, y

# preprocess()
