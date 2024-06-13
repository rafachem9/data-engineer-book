from util.loggging_utils import create_log_file


logger = create_log_file('log.log')

dim_product_cols = ['product_pk', 'product_id', 'product_name', 'category', 'subcategory', 'brand']
fact_sales_cols = ['transaction_id',  'transactional_date',  'transactional_date_fk',  'product_id',
                   'product_fk',  'customer_id',  'payment_fk',  'credit_card',  'cost',  'quantity',
                   'price', 'total_cost', 'total_price', 'profit']
