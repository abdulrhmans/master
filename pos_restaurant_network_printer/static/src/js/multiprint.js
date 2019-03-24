odoo.define('pos_restaurant_network_printer.Multiprint', function (require) {
    "use strict";

    var models = require('point_of_sale.models');
    var core = require('web.core');
    var QWeb = core.qweb;

    models.Order = models.Order.extend({
        printChanges: function () {
            var self = this;
            var printers = this.pos.printers;
            for (var i = 0; i < printers.length; i++) {
                var changes = this.computeChanges(printers[i].config.product_categories_ids);
                if (changes['new'].length > 0 || changes['cancelled'].length > 0) {
                    _.each(changes.new, function (line) {
                        // quantity
                        var nb = String(line.qty);
                        if (nb.length == 1) {
                            line.qty_nb = '<pre>  ' + line.qty + '</pre>';
                        }
                        else if (nb.length == 2) {
                            line.qty_nb = '<pre> ' + line.qty + '</pre>';
                        }
                        else if (nb.length == 3) {
                            line.qty_nb = line.qty;
                        }
                    });
                    _.each(changes.cancelled, function (line) {
                        // quantity
                        var nb = String(line.qty);
                        if (nb.length == 1) {
                            line.qty_nb = '<pre>  -' + line.qty + '</pre>';
                        }
                        else if (nb.length == 2) {
                            line.qty_nb = '<pre> -' + line.qty + '</pre>';
                        }
                        else if (nb.length == 3) {
                            line.qty_nb = '-' + line.qty;
                        }
                    });
                    var receipt = QWeb.render('OrderChangeReceipt', {changes: changes, widget: self});
                    printers[i].print(self, receipt);
                }
            }
        },
    });

});