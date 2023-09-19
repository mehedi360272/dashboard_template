odoo.define("custom_dashboard.Dashboard", function (require) {
   "use strict";
   var AbstractAction = require('web.AbstractAction');
   var core = require('web.core');
   var DashBoard = AbstractAction.extend({
       contentTemplate: 'table_name_dashboard',
   });
   core.action_registry.add('custom_dashboard', DashBoard);
   return DashBoard;
});
