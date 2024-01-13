odoo.define('victorikus_web.buildYourCake', function (require) {
    "use strict";

    const {Component} = require('@odoo/owl');

    class BuildYourCakeComponent extends Component {
        static template = "victorikus_web.BuildYourCakeComponent";

        setup() {
            console.log("setup: BuildYourCakeComponent");
        }
    }
});

