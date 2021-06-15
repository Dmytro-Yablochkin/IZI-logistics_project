class OrderPageLocators:
    required_alert = 'css = p.Mui-error'
    order_saved_alert = 'css = div.Toastify__toast--success'
    # Customer data fields
    order_name_input = 'css = input[name="orderId"]'
    resp_person_dropdown = 'css = input[name="manager"]'
    templates_dropdown = 'css = input[name="template"]'

    # ------------Transportation(s)------------- #
    # Routes
    pickup_location_input = 'css = #mui-95487'
    pickup_warehouse_email_input = 'css = #mui-51095'
    pickup_date_field = 'css = .jss638 > div:nth-of-type(2) .MuiGrid-grid-lg-3'

    pickup_start_date = 'css = .jss638 > div:nth-of-type(2) div:nth-of-type(3) > div:nth-of-type(1) > ' \
                        'div:nth-of-type(1) > div:nth-of-type(1) input:nth-of-type(1) '
    pickup_end_date = 'css = .jss638 > div:nth-of-type(2) div:nth-of-type(3) div:nth-of-type(2) input:nth-of-type(1)'

    delivery_location_input = 'css = #mui-3684'
    delivery_warehouse_email = 'css = '
    delivery_date_calendar = 'css '

    delivery_start_date = 'css = .jss638 > div:nth-of-type(4) div:nth-of-type(3) > div:nth-of-type(1) > ' \
                          'div:nth-of-type(1) > div:nth-of-type(1) input:nth-of-type(1)'
    delivery_end_date = 'css = .jss638 > div:nth-of-type(4) div:nth-of-type(3) div:nth-of-type(2) input:nth-of-type(1)'

    # Cargo(es)
    full_truckload_checkbox = 'css = input[value="FullTrackLoad"]'
    less_than_truckload_checkbox = 'css = input[value="PTLTrackLoad"]'
    cargo_id_input = 'css = input[name="cargoId"]'
    product_type_input = 'css = input[name="productType"]'
    tainted_code_input = 'css = input[name="taintedCode"]'
    package_input = 'css = input[name="package"]'
    pallet_type_input = 'css = input[name="palletType"]'
    height_input = 'css = input[name="height"]'
    volume_input = 'css = input[name="volume"]'
    amount_input = 'css = input[name="amount"]'

    weight_input = 'css = input[name="weight"]'
    weight_type_dropdown = 'css = #mui-component-select-weightMeasure'
    tonnes = 'css = ul > li[data-value="t"]'
    kilograms = 'css = ul > li[data-value="kg"]'
    grams = 'css = ul > li[data-value="g"]'

    # ---------------Transport requirements-------------- #
    vehicle_type_input = 'css = input[name="vehicleType"]'
    loading_type = 'css = input[name="loadingType"]'

    # --------------Additional requirements-------------- #
    adr_checkbox = 'css = input[name="isADR"]'
    corner_protect_checkbox = 'css = input[name="isCargoCornerProtector"]'
    anti_slip_mats_checkbox = 'css = input[name="isAntiSplitMats"]'
    tent_checkbox = 'css = input[name="isTent"]'
    gpm_checkbox = 'css = input[name="isGPM"]'

    straps_dropdown = 'css = input[name="strap"]'
    sideboards_input = 'css = input[name="sideBoards"]'
    additional_requirements_input = 'css = textarea[name="comment"]'
    comment_for_cmr_input = 'css = textarea[name="commentCMR"]'

    # -----------------Save order block-------------------- #
    order_expiration_date_input = 'css = input[readonly]'

    target_price_input = 'css = input[name="price"]'
    price_dropdown = 'css = div[id="mui-component-select-currency"]'
    price_droplist = 'css = ul[class="MuiList-root"]'
    usd = 'css = li[data-value="USD"]'
    eur = 'css = li[data-value="EUR"]'
    rub = 'css = li[data-value="RUB"]'

    create_order_btn = 'css = button[id="btn-save-order"]'
    publish_order_btn = 'css = button[id="btn-publish-order"]'
