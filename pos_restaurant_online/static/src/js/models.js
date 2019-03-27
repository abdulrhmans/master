odoo.define('pos_restaurant_online.Models', function(require){
   'use strict';

   var models = require('point_of_sale.models');
   models.load_fields('restaurant.printer', 'connector_id');

});