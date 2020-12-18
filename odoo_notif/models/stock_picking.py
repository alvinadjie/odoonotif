from odoo import models, fields, api, _

class StockPicking(models.Model):
    """ inherit stock picking """
    _inherit = 'stock.picking'

    
    def button_validate(self):
        """ Extend this function send notification to user 
        """
        res = super(StockPicking, self).button_validate()
        notification_ids = [(0, 0, {
            'res_partner_id': self.user_id.partner_id.id,
            'notification_type': 'inbox'
        })]
        self.message_post(body='This picking has been validated!', message_type="notification", subtype="mail.mt_comment", 
                            author_id=self.env.user.partner_id.id, 
                            notification_ids=notification_ids)