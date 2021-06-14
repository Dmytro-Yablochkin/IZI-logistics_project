class CPLocators:
    # ---------------Sign in locators------------------- #
    email_field = 'css = input[name="email"]'
    password_field = 'css = input[name="password"]'
    submit_login_button = 'css = button[type="submit"]'
    login_form = 'css = #root main'
    customer_page = 'css = a[href="/"] :nth-child(1)'

    # ------------- customer page locators-------------- #
    # ------------- left side items ---------------- #
    order_creation = 'css = a[href="/orders/create"]'
    open_orders = 'css = a[href="/open-orders"]'
    in_progress = 'css = a[href="/in-progress"]'
    archive = 'css = a[href="/archive"]'
    drafts = 'css = a[href="/drafts"]'
    templates = 'css = a[href="/templates"]'
    team = 'css = a[href="/team"]'
    carriers = 'css = a[href="/carriers"]'
    locations = 'css = a[href="/locations"]'
    warehouses = 'css = a[href="/warehouses"]'
