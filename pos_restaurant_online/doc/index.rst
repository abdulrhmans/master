=====================
POS RESTAURANT ONLINE
=====================

Installation
============

* Copy the modules in addons path and install it from Apps menu
* Uncomment depends in ``pos_restaurant_network_printer`` in __manifest__.py file of the module

Configuration
=============

* Open menu ``Point Of Sale >>  Configuration >> Point of Sale``
* Edit selected Point of Sale. On **PosBox / Hardware Proxy** section, check Order Printer to True
* Click on Printers button
* Edit the selected printer and add the Connector
* At **Bill & Receipts** section
    * Keep Ticket print mode to Network
    * Check Bill printing to True
    * Keep Bill print mode to Network
* Odoo Printer Connector: follow the configuration at **pos_network_printer_online"

Usage
=====

* Print ticket from Point Of Sale Restaurant
* Open menu ``Point Of Sale >>  Configuration >> Queue print`` to see queue print
* Odoo Printer Connector will print receipt in local printer


