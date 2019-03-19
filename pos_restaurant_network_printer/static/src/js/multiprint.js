odoo.define('pos_restaurant_network_printer.Multiprint', function (require) {
    "use strict";

    var models = require('point_of_sale.models');
    var screens = require('point_of_sale.screens');
    var core = require('web.core');
    var mixins = require('web.mixins');
    var Session = require('web.Session');

    var QWeb = core.qweb;
    var _t = core._t;

    var Printer = core.Class.extend(mixins.PropertiesMixin, {
        init: function (parent) {
            mixins.PropertiesMixin.init.call(this, parent);
            this.receipt_queue = [];
        },
        print: function (widget, receipt) {
            var self = this;
            if (receipt) {
                this.receipt_queue.push(receipt);
            }
            function send_printing_job() {
                if (self.receipt_queue.length > 0) {
                    var receipt_xml = self.receipt_queue.shift();
                    var order = widget.pos.get_order();
                    var receipt_data = {
                        "uid": order.uid,
                        "printer_ip": self.config.proxy_ip,
                        "printer_port": self.config.printer_port,
                        "receipt": receipt_xml,
                    }

                    var receipt_db = widget.pos.db.load('receipt', []);
                    receipt_db.push(receipt_data);
                    widget.pos.db.save('receipt', receipt_db);

                    var json_data = {
                        "jsonrpc": "2.0",
                        "params": receipt_data,
                    }
                    $.ajax({
                        dataType: 'json',
                        headers: {
                            "content-type": "application/json",
                            "cache-control": "no-cache",
                        },
                        url: '/print-network-xmlreceipt',
                        type: 'POST',
                        proccessData: false,
                        data: JSON.stringify(json_data),
                        success: function (res) {
                            var data = JSON.parse(res.result);
                            if (data.error == 0) {
                                self.remove_printed_order_change(widget, data.uid);
                            }
                            if (data.error == 1) {
                                widget.pos.set({printer: {state: 'disconnected'}, spooler: {state: 'connecting'}});
                            }
                        }
                    });
                }
            }

            send_printing_job();
        },
        remove_printed_order_change: function (widget, uid) {
            var receipt = widget.pos.db.load('receipt', []);
            var printed_receipt = receipt.pop();
            if (printed_receipt.uid != uid) {
                receipt.push(printed_receipt);
            }
            widget.pos.db.save('receipt', receipt);
        },
    });

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