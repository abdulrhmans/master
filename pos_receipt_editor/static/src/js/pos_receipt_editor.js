odoo.define('pos_receipt_editor.LoadXml', function (require) {
    "use strict";
    var core = require('web.core');
    var QWeb = core.qweb;
    var models = require('point_of_sale.models');
    models.load_models({
        model: 'receipt.template',
        fields: ['id', 'template'],
        domain: null,
        loaded: function (self, receipt_template) {
            var parse_to_xml = function (name, template) {
                var all_template = '<t t-name="' + name + '">' + template + '</t>';
                var parser = new DOMParser();
                var xmlDocument = parser.parseFromString(all_template, "text/xml");
                return xmlDocument.documentElement;
            }
            if (self.config.use_custom_receipt == true) {
                for (var i = 0; i < receipt_template.length; i++) {
                    if (receipt_template[i].id == self.config.ticket_receipt_id[0]) {
                        QWeb.templates['XmlReceipt'] = parse_to_xml('XmlReceipt', receipt_template[i].template);
                    }
                    if (receipt_template[i].id == self.config.ticket_order_id[0]) {
                        QWeb.templates['OrderChangeReceipt'] = parse_to_xml('OrderChangeReceipt', receipt_template[i].template);
                    }
                    if (receipt_template[i].id == self.config.ticket_bill_id[0]) {
                        QWeb.templates['BillReceipt'] = parse_to_xml('BillReceipt', receipt_template[i].template);
                    }
                }
            }
        },
    });

});