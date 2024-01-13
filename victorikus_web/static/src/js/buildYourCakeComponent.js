odoo.define('victorikus_web.buildYourCakeComponent', function (require) {
    "use strict";

    const {Component} = require('@odoo/owl');

    class BuildYourCakeComponent extends Component {
        setup() {
            console.log("setup: BuildYourCakeComponent");
        }
    }

    BuildYourCakeComponent.template = "victorikus_web.buildYourCakeComponentTemplate";
    return BuildYourCakeComponent;
});

