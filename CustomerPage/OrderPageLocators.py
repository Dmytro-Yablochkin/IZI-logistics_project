class OrderPageLocators:
    required_alert = 'css = p.Mui-error'
    order_saved_alert = 'css = div.Toastify__toast--success'
    # Customer data fields
    order_name_input = 'css = input[name="orderId"]'
    resp_person_dropdown = 'css = input[name="manager"]'
    templates_dropdown = 'css = input[name="template"]'

    # ------------Transportation(s)------------- #
    # Routes
    pickup_location_input = 'css = '
    pickup_warehouse_email_input = 'css = '
    pickup_date_calendar = 'css = '

    delivery_location_input = 'css = '
    delivery_warehouse_email = 'css = '
    delivery_date_calendar = 'css '

    # Cargo(es)
    full_truckload_checkbox = 'css = '
    less_than_truckload_checkbox = 'css = '
    cargo_id_input = 'css = '
    product_type_input = 'css = '
    tainted_code_input = 'css = '
    package_input = 'css = '
    pallet_type_input = 'css = '
    height_input = 'css = '
    volume_input = 'css = '
    amount_input = 'css = '

    weight_input = 'css = '
    weight_type_dropdown = 'css = '
    tonnes = 'css = '
    kilograms = 'css = '
    grams = 'css = '

    # ---------------Transport requirements-------------- #
    vehicle_type_input = 'css = '
    vehicle_type_dropdown = 'css = '
    loading_type = 'css = '

    # --------------Additional requirements-------------- #
    adr_checkbox = 'css = '
    corner_protect_checkbox = 'css = '
    anti_slip_mats_checkbox = 'css = '
    tent_checkbox = 'css = '
    gpm_checkbox = 'css = '

    straps_dropdown = 'css = '
    sideboards_input = 'css = '
    additional_requirements_input = 'css = '
    comment_for_cmr_input = 'css = '

    # -----------------Save order block-------------------- #
    order_expiration_date_input = 'css = '

    target_price_input = 'css = '
    price_dropdown = 'css = '
    usd = 'css = '
    eur = 'css = '
    rub = 'css = '

    create_order_btn = 'css = #btn-save-order'
