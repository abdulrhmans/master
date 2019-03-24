odoo.define('product_arabic.pos_receipt', function (require) {
"use strict";

var gui = require('point_of_sale.gui');
var models = require('point_of_sale.models');
models.load_fields("product.product", ['product_arabic']);
});