from odoo import api, models

class SaleOrderHisReportPrint(models.AbstractModel):
    _name = 'report.sale_history.sale_order_history_line_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        print('product lines==>', lines)
        model = self.env.context.get('active_model')

        for obj in lines:
            if obj.added_history_o:
                c = obj.added_history_o

        # Formate to print data in the xml report
        format1 = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True})
        sheet = workbook.add_worksheet('Sale Order line report')
        sheet.write(0, 0, 'Order id', format1)
        sheet.write(0, 1, 'Customer', format1)
        sheet.write(0, 2, 'Product', format1)
        sheet.write(0, 3, 'quantity', format1)
        sheet.write(0, 4, 'Price', format1)
        sheet.write(0, 5, 'total(Un-tax)', format1)
        sheet.write(0, 6, 'Date/time', format1)

        # Enter data:
        sheet.set_column(0,0,20)
        sheet.set_column(0,1,20)
        sheet.set_column(0,2,20)
        sheet.set_column(0,3,20)
        sheet.set_column(0,4,20)
        sheet.set_column(0,5,20)
        sheet.set_column(0,6,30)

        i = 1
        for x in c:
            j = 0
            sheet.write(i, j, x.product_id, format1)
            j += 1
            sheet.write(i, j, lines.partner_id.name, format1)
            j += 1
            sheet.write(i, j, x.name, format1)
            j += 1
            sheet.write(i, j, x.product_qty, format1)
            j += 1
            sheet.write(i, j, x.unit_price, format1)
            j += 1
            sheet.write(i, j, x.price_subtotal, format1)
            j += 1
            sheet.write(i, j, str(lines.date_order), format1)
            j += 1
            i += 1

