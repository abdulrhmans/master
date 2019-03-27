odoo.define('pos_restaurant_network_printer.Models', function (require) {
    'use strict';
    var models = require('point_of_sale.models');
    var Printer = require('pos_restaurant_network_printer.Printer');
    models.load_models({
        model: 'restaurant.printer',
        fields: ['name', 'proxy_ip', 'printer_port', 'product_categories_ids'],
        domain: null,
        loaded: function (self, printers) {
            var active_printers = {};
            for (var i = 0; i < self.config.printer_ids.length; i++) {
                active_printers[self.config.printer_ids[i]] = true;
            }
            self.printers = [];
            self.printers_categories = {};

            for (var i = 0; i < printers.length; i++) {
                if (active_printers[printers[i].id]) {
                    var printer = new Printer(self);
                    printer.config = printers[i];
                    self.printers.push(printer);
                    for (var j = 0; j < printer.config.product_categories_ids.length; j++) {
                        self.printers_categories[printer.config.product_categories_ids[j]] = true;
                    }
                }
            }
            self.printers_categories = _.keys(self.printers_categories);
            self.config.iface_printers = !!self.printers.length;
        },
    });

});