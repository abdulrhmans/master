# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################
{
  "name"                 :  "POS Webkul Addons",
  "summary"              :  "This module works as a configuration base for various POS Apps developed by Webkul Software Pvt. Ltd. ",
  "category"             :  "Point Of Sale",
  "version"              :  "1.0",
  "sequence"             :  1,
  "author"               :  "Webkul Software Pvt. Ltd.",
  "license"              :  "Other proprietary",
  "website"              :  "http://www.webkul.com",
  "description"          :  """POS Webkul Addons""",
  "live_test_url"        :  "http://odoodemo.webkul.com/?module=pos_webkul_addons&version=11.0",
  "depends"              :  ['point_of_sale'],
  "data"                 :  [
                             'views/webkul_addons_config_view.xml',
                            ],
  "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "pre_init_hook"        :  "pre_init_check",
}