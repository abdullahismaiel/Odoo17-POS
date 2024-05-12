/** @odoo-module */

import { Component } from "@odoo/owl";

export class Orderline extends Component {
    static template = "pos_hide_receipt_price.Orderline";
    static props = {
        class: { type: Object, optional: true },
        line: {
            type: Object,
            shape: {
                productName: String,
                price: String,
                qty: String,
                unit: { type: String, optional: true },
                unitPrice: String,
                discount: { type: String, optional: true },
                comboParent: { type: String, optional: true },
                oldUnitPrice: { type: String, optional: true },
                customerNote: { type: String, optional: true },
                internalNote: { type: String, optional: true },
                attributes: { type: Array, optional: true },
                "*": true,
            },
        },
        slots: { type: Object, optional: true },
    };
    static defaultProps = {
        class: {},
    };
}
