odoo.define('pos_restaurant_online.Printer', function (require) {
    'use strict';
    var Printer = require('pos_restaurant_network_printer.Printer');
    var rpc = require('web.rpc');

    Printer.include({
        print: function (widget, receipt) {
            var self = this;
            if (receipt) {
                this.receipt_queue.push(receipt);
            }

            function send_printing_job() {
                if (self.receipt_queue.length > 0) {
                    var receipt_xml = self.receipt_queue.shift();
                    var queue_print_data = {
                        "printer_name": self.config.name,
                        "printer_ip": self.config.proxy_ip,
                        "printer_port": self.config.printer_port,
                        "connector_id": self.config.connector_id[0],
                        "receipt": receipt_xml,
                        "token": self.get_connector_token(widget, self.config),
                    }

                    rpc.query({
                        model: 'queue.print',
                        method: 'create',
                        args: [queue_print_data]
                    }).then(function (result) {
                        console.log('new queue created ' + 1);
                    });
                }
            }

            send_printing_job();
        },
        get_connector_token: function (widget, printer) {
            var connector = _.filter(widget.pos.printer_connectors, function (line) {
                return line.id == printer.connector_id[0]
            });
            return connector[0].token;
        }
    });
});