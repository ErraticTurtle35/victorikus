odoo.define('victorikus_web.BuildYourCakeApp', function (require) {
    'use strict';

    const {Component, mount, whenReady, loadFile} = require('@odoo/owl');

    class BuildYourCakeApp extends Component {
        static template = "victorikus_web.BuildYourCakeApp";

        setup() {
            console.log("BuildYourCakeApp, setup")
        }
    }

    whenReady(async function () {
        const root = document.querySelector("#BuildYourCakeApp");
        if (root) {
            const templates = await loadFile(`victorikus_web/static/src/xml/BuildYourCakeApp.xml`);
            const env = {
                templates,
            };
            mount(BuildYourCakeApp, root, env);
        }
    });
});