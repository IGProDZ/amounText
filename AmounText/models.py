

from openerp import models, fields, api
from montantEnLettres import montant_en_lettres

class Invoice(models.Model):
    _inherit = 'account.invoice'

    amounTexte = fields.Text(compute="amountToText", default="Montant en lettres")
    
    @api.depends("amount_total")
    def amountToText(self):
        for r in self:
            montant = montant_en_lettres(r.amount_total)
            
            r.amounTexte = (montant[0] + r.currency_id.litteral_name.capitalize() + montant[1]).capitalize()

class Curreuncy(models.Model):
    _inherit = "res.currency"
    
    litteral_name = fields.Char(string="Nom complet")
    
