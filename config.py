"""
company_tags
Specifies the keywords that the algorithm uses to detect whether a particular piece of text is a company name
"""
company_tags = ["limited", "limited.", "ltd", "ltd."]

"""
countries
Specifies the countries that the OCR engine should look out for
"""
countries = ["singapore", "japan", "hk", "hong kong"]


"""
tax_labels
Specifies the keywords that the algorithm uses to detect whether a particular piece of text is related to tax
"""
tax_labels = ["gst", "tax", "vat"]

"""
specific_currencies
Specifies the currencies which are recognised by the OCR engine as denoting a specific currency
"""
specific_currencies = [
    "SGD",
    "HKD",
    "JPY",
    "USD",
    "US$",
    "SG$",
    "$SG",
    "$US",
    "S$",
    "SINGAPORE DOLLAR",
]

"""
currencies
Specifies the currencies which are recognised by the OCR engine as denoting a currency value
"""
currencies = [
    "SGD",
    "HKD",
    "JPY",
    "USD",
    "US$",
    "SG$",
    "$SG",
    "$US",
    "S$",
    "SINGAPORE DOLLAR",
    "$",
    "dollar",
    "¥",
]

"""
category_mappings
Converts between classifier categories and human readable categories.
If the categories that needs to be predicted changes, this variable should be edited
"""
category_mappings = {
    "Others": 0,
    "Account number": 1,
    "Consumption period": 2,
    "Country of consumption": 3,
    "Currency of invoice": 4,
    "Date of invoice": 5,
    "Invoice number": 6,
    "Name of provider": 7,
    "PO Number": 8,
    "Tax": 9,
    "Total amount": 10,
    0: "Others",
    1: "Account number",
    2: "Consumption period",
    3: "Country of consumption",
    4: "Currency of invoice",
    5: "Date of invoice",
    6: "Invoice number",
    7: "Name of provider",
    8: "PO Number",
    9: "Tax",
    10: "Total amount",
}

"""
features_to_use
Used to select features that are used in the training of the classifier and the prediction of tokens.
Features which are not commented out will be used in the training and prediction of tokens 
"""
features_to_use = [
    # "char_count",
    # "word_count",
    # "height",
    # "width",
    "rel_dist_top",
    # "rel_dist_left",
    # "dist_bottom",
    # "dist_right",
    # "dist_top_outer",
    # "dist_left_outer",
    # "dist_bottom_outer",
    # "dist_right_outer",
    # "rel_size_page_x",
    # "rel_size_page_y",
    # "average_dist_neighbours_pixel",
    # "average_dist_neighbours_rel",
    # "average_dist_N_nearest_neighbours_pixel",
    # "average_dist_N_nearest_neighbours_rel",
    # "percentile_width",
    # "percentile_height",
    "contains_date",
    "contains_currency",
    "contains_specific_currency",
    "contains_date_range",
    "contains_address",
    # "contains_num_label", #
    # "contains_total_label", #
    # "contains_amount_label", #
    # "contains_date_label", #
    # "contains_date_of_invoice_label", #
    "contains_digit",
    "contains_company",
    # "contains_tax_label",
    # "vert_align_to_cell_w_date",
    "vert_align_to_cell_w_currency",
    # "vert_align_to_cell_w_address",
    "vert_align_to_cell_w_datelabel",
    "vert_align_to_cell_w_dateofinvoicelabel",
    # "vert_align_to_cell_w_numlabel",
    "vert_align_to_cell_w_totallabel",
    "vert_align_to_cell_w_amountlabel",
    # "vert_align_to_cell_w_digit",
    "vert_align_to_cell_w_invoicenum_label",
    "vert_align_to_cell_w_accountnum_label",
    "vert_align_to_cell_w_ponum_label",
    "vert_align_to_cell_w_tax_label",
    # "hori_align_to_cell_w_date",
    "hori_align_to_cell_w_currency",
    # "hori_align_to_cell_w_address",
    "hori_align_to_cell_w_datelabel",
    "hori_align_to_cell_w_dateofinvoicelabel",
    # "hori_align_to_cell_w_numlabel",
    "hori_align_to_cell_w_totallabel",
    "hori_align_to_cell_w_amountlabel",
    # "hori_align_to_cell_w_digit",
    "hori_align_to_cell_w_invoicenum_label",
    "hori_align_to_cell_w_accountnum_label",
    "hori_align_to_cell_w_ponum_label",
    "hori_align_to_cell_w_tax_label",
    # "rel_dist_nearest_cell_w_date",
    "rel_dist_nearest_cell_w_currency",
    # "rel_dist_nearest_cell_w_address",
    "rel_dist_nearest_cell_w_datelabel",
    "rel_dist_nearest_cell_w_invoicedatelabel",
    # "rel_dist_nearest_cell_w_numlabel",
    "rel_dist_nearest_cell_w_invoicenumlabel",
    "rel_dist_nearest_cell_w_accnumlabel",
    "rel_dist_nearest_cell_w_ponumlabel",
    "rel_dist_nearest_cell_w_totallabel",
    "rel_dist_nearest_cell_w_amountlabel",
    # "rel_dist_nearest_cell_w_digit",
    "rel_dist_nearest_cell_w_tax_label",
]
