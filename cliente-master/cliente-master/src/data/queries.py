##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: queries.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define las consultas que permiten obtener información 
#   y realizar el llenado de datos del tablero
#
#-------------------------------------------------------------------------
class Queries:

    @staticmethod
    def get_total_products():
        return """
            {
                response(func: has(description)) {
                    count(uid)
                }
            }
        """

    @staticmethod
    def get_total_providers():
        return """
            {
                response(func: has(pid)) {
                    count(uid)
                }
            }
        """

    @staticmethod
    def get_total_locations():
        return """
            {
                response(func: has(name)) {
                    count(uid)
                }
            }
        """

    @staticmethod
    def get_total_orders():
        return """
            {
                response(func: has(invoice)) {
                    count(uid)
                }
            }
        """

    @staticmethod
    def get_total_sales():
        return """
            {
                var(func: has(invoice)) {
                    t as total
                }

                response() {
                    total: sum(val(t))
                }
            }
        """

    @staticmethod
    def get_providers_per_location():
        return """
            {
                response(func: has(name)) {
                    name
                    providers: ~belongs {
                        count(uid)
                    }
                }
            }
        """

    @staticmethod
    def get_sales_per_location():
        return """
            {
                response(func: has(name)){
                    name
                    providers: ~belongs {
                        sold: ~sold {
                            price
                            quantity: count(bought)
                        }
                    }
                }
            }
        """

    @staticmethod
    def get_orders_per_location():
        return """
            {
                response(func: has(name)){
                    name
                    providers: ~belongs {
                        sold: count(~sold)
                    }
                }
            }
        """

    @staticmethod
    def get_best_sellers():
        return """
            {
                var(func: has(description)) {
                    c as count(bought) 
                }
                    
                response(func: has(description), orderdesc: val(c)){
                    description
                    times: val(c)
                    price
                }
            }
        """

    @staticmethod
    def get_worst_sales():
        return """
            {
                var(func: has(description)) {
                    c as count(bought) 
                }
                    
                response(func: has(description), orderasc: val(c)){
                    description
                    times: val(c)
                    price
                }
            }
        """

    @staticmethod
    def get_most_selled_products():
        return """
            {
                var(func: has(description)) {
                    c as count(bought) 
                }
                    
                response(func: has(description), orderdesc: val(c)){
                    description
                    times: val(c)
                }
            }
        """

    @staticmethod
    def get_month_sales_reports(currentYear):
        return f"""
            {{
                var(func:has(invoice)) @filter(ge(date, "{currentYear}-01") AND lt(date, "{currentYear}-02")) {{
                    amount1 as total
                }}

                var(func:has(invoice)) @filter(ge(date, "{currentYear}-02") AND lt(date, "{currentYear}-03")) {{
                    amount2 as total
                }}

                var(func:has(invoice)) @filter(ge(date, "{currentYear}-03") AND lt(date, "{currentYear}-04")) {{
                    amount3 as total
                }}

                var(func:has(invoice)) @filter(ge(date, "{currentYear}-04") AND lt(date, "{currentYear}-05")) {{
                    amount4 as total
                }}

                var(func:has(invoice)) @filter(ge(date, "{currentYear}-05") AND lt(date, "{currentYear}-06")) {{
                    amount5 as total
                }}

                var(func:has(invoice)) @filter(ge(date, "{currentYear}-06") AND lt(date, "{currentYear}-07")) {{
                    amount6 as total
                }}

                var(func:has(invoice)) @filter(ge(date, "{currentYear}-07") AND lt(date, "{currentYear}-08")) {{
                    amount7 as total
                }}

                var(func:has(invoice)) @filter(ge(date, "{currentYear}-08") AND lt(date, "{currentYear}-09")) {{
                    amount8 as total
                }}

                var(func:has(invoice)) @filter(ge(date, "{currentYear}-09") AND lt(date, "{currentYear}-10")) {{
                    amount9 as total
                }}

                var(func:has(invoice)) @filter(ge(date, "{currentYear}-10") AND lt(date, "{currentYear}-11")) {{
                    amount10 as total
                }}

                var(func:has(invoice)) @filter(ge(date, "{currentYear}-11") AND lt(date, "{currentYear}-12")) {{
                    amount11 as total
                }}

                var(func:has(invoice)) @filter(ge(date, "{currentYear}-12") AND lt(date, "{currentYear + 1}-01")) {{
                    amount12 as total
                }}

                response(){{
                    total1: sum(val(amount1))
                    total2: sum(val(amount2))
                    total3: sum(val(amount3))
                    total4: sum(val(amount4))
                    total5: sum(val(amount5))
                    total6: sum(val(amount6))
                    total7: sum(val(amount7))
                    total8: sum(val(amount8))
                    total9: sum(val(amount9))
                    total10: sum(val(amount10))
                    total11: sum(val(amount11))
                    total12: sum(val(amount12))
                }}
            }}
        """

    @staticmethod
    def get_month_sales_count(currentYear):
        return f"""
            {{
                var(func:has(invoice)) @filter(ge(date, "{currentYear}-01") AND lt(date, "{currentYear}-02")) {{
                    count1 as count(quantity)
                }}

                var(func:has(invoice)) @filter(ge(date, "{currentYear}-02") AND lt(date, "{currentYear}-03")) {{
                    count2 as count(quantity)
                }}

                var(func:has(invoice)) @filter(ge(date, "{currentYear}-03") AND lt(date, "{currentYear}-04")) {{
                    count3 as count(quantity)
                }}

                var(func:has(invoice)) @filter(ge(date, "{currentYear}-04") AND lt(date, "{currentYear}-05")) {{
                    count4 as count(quantity)
                }}

                var(func:has(invoice)) @filter(ge(date, "{currentYear}-05") AND lt(date, "{currentYear}-06")) {{
                    count5 as count(quantity)
                }}

                var(func:has(invoice)) @filter(ge(date, "{currentYear}-06") AND lt(date, "{currentYear}-07")) {{
                    count6 as count(quantity)
                }}

                var(func:has(invoice)) @filter(ge(date, "{currentYear}-07") AND lt(date, "{currentYear}-08")) {{
                    count7 as count(quantity)
                }}

                var(func:has(invoice)) @filter(ge(date, "{currentYear}-08") AND lt(date, "{currentYear}-09")) {{
                    count8 as count(quantity)
                }}

                var(func:has(invoice)) @filter(ge(date, "{currentYear}-09") AND lt(date, "{currentYear}-10")) {{
                    count9 as count(quantity)
                }}

                var(func:has(invoice)) @filter(ge(date, "{currentYear}-10") AND lt(date, "{currentYear}-11")) {{
                    count10 as count(quantity)
                }}

                var(func:has(invoice)) @filter(ge(date, "{currentYear}-11") AND lt(date, "{currentYear}-12")) {{
                    count11 as count(quantity)
                }}

                var(func:has(invoice)) @filter(ge(date, "{currentYear}-12") AND lt(date, "{currentYear + 1}-01")) {{
                    count12 as count(quantity)
                }}

                response(){{
                    total1: sum(val(count1))
                    total2: sum(val(count2))
                    total3: sum(val(count3))
                    total4: sum(val(count4))
                    total5: sum(val(count5))
                    total6: sum(val(count6))
                    total7: sum(val(count7))
                    total8: sum(val(count8))
                    total9: sum(val(count9))
                    total10: sum(val(count10))
                    total11: sum(val(count11))
                    total12: sum(val(count12))
                }}
            }}
        """
