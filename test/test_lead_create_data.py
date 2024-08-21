# coding: utf-8

"""
    Engine by MoneyLion API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.58.0
    Contact: help@engine.tech
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.lead_create_data import LeadCreateData

class TestLeadCreateData(unittest.TestCase):
    """LeadCreateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LeadCreateData:
        """Test LeadCreateData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LeadCreateData`
        """
        model = LeadCreateData()
        if include_optional:
            return LeadCreateData(
                product_types = [
                    'credit_card'
                    ],
                uuid = '',
                session_uuid = '',
                device_id = '',
                loan_information = openapi_client.models.lead_loan_information.LeadLoanInformation(
                    purpose = 'auto', 
                    loan_amount = 56, ),
                personal_information = openapi_client.models.lead_personal_information.LeadPersonalInformation(
                    first_name = '', 
                    last_name = '', 
                    alias_first_name = '', 
                    alias_last_name = '', 
                    email = '7.7kp={R/g2*SVXkjc1XP^68kTyn!RSD}A?k-F-^+^%dG+%40$okj#v~z_k`mAwSdahssq^U0.YAPBcee8jqrmb='mk#ik&^m~Y#-y|{pDWbO.jEPFVfXE8^Ej3ivU+}0'3ba5ng!NY8RFHCzKsJ3PJRFdvJiioPWo'G!+Cqg&xs8QX|V.zSdd'BOPeeq0ytC_7QRG9&n+ADTr%qIWZ{G7^q#/XM5}uMUC3oXkEDfs9iVJJ6uyAxmx4KkpP%rUjo.nRLjHba0KFCPIf_nngxBYmN&J~wT`mhGFn#i0v_Xcw%2gT=K2=_I4WfD{f`'}/7G{.EGFK*'LUA7V3c.}m|^AjUCYqyL38l3}B23YEfvC!9OtvR&5!_0`8.F#18cYR5`H9FRePCcc4Yolh+cnRMpkE=bpD3'K-1~06?.!M+aY?vEa%fOhK!MRzF3Fji=e&6O$kG~zQCd2r4}2E{qT-mTc!tE~/^YCWi$cMr.r`Q|'lDEC~nSmNUy&Z7-+oWzGSi'ZP.9!xG4esl%N9G6|EXKX8alZiUDfb4*${W?`fN-_7{e?*?sTQL3D5.Mx5OJk32RgE~m=NXAh'pEI*mKM=RuSculcIYSM?pH4y&D6$t||?+k6nvg0LJW!u%#GygMxUEFm.j+l~hjNdSTA{h!!OElFLP+R&mIyjH7u!^kZ}w$I~yiw'Xb$hdzwmW_TinGxtcW!.}Jugm=#zWcX8Fjx/EM5#0wkWX1c*wb'2n1{d8&2*X!xf'%GhF{oo?j51AuL5c}QXTMsz!hO-%}g{Vb|_ja--.*UOnpNz#-fkfhpE2CwY$YzM4J~6BZaF!h/A}UaMlRV`ZrDq+_IDiYQ~xyp-IOF{G24J5%/.22Z*Akgrq4-6WAVfnxMC-%QRapCV{tL*tvsh'LNSxNSy4EBqPfGaMgMn$C_5%v*3sV^s5%uQZ=FYbWpfwzHfx%X$D36bL$ZT.'uHMWCKhE3FiRc?N'&MDPvgs9votz0~vT~tZLB2cP3uEESw?gqG`Ldb6R~~V92=|_NxRLyue6P0oGa29M3B7y&rKpL.gKl_3vMPSNYYbf2gi-71~%pohKYhHe4cFLB64BD+QW^-D+U%H==FQ9$Ys.}zh/GFK?lDX.%X=7kCw2YxT2.WIx~=v80Pqmp`}md+eGD{rdW~A5XZ6pZF~lMzNzO-{*^8Oy*7Q+cDwwS|jGwCbq.k|7&Pby6$5y`Od9`HPh3jAI3u*?HY?#.jT&N7ZELavUjL4w$W8GOA/iFYRihZYJPn0ym$~hjh15ut48Hb5}A~~T'Z7N*jl0.N1PX38gmt0CnV&*!Fy~9PYW`O}X8^Zwg*4T=.W3z&YoohI4OcYABkKA-{-qfeIvy%UK8hlTA1R1hSoW!6Uqy9S.MSItPxh5ET90H*?h_`pmcq`y{0PKp3}mo?7Vpy+GCvfJkRPW?CCJ1NpFQFk9B1^J8.A#GpUSzEiA'|4U?qA~ERv$hXW{tvKb?4&DcTvGKJ8^R6H%/~FgqmkMQIV8R}'!-FfZHI0r6f%$u7VqYjy`DGZ+BU.pP2SIMvH8j${rUm8w34-7381C8$pS#y8R-q_TT~dWyTztybJuM?41G'NPX.}lDS}H3|v/3A.h#ikh{VcD2s7^-9R|5qFr7ixZ*O_H4?u324fbhMH*-`5VyR`%3u3Lf7TYK!.28KKvsp}z*kXaJj`.yga}|uRvPaih2s~4k7`p1Y4!G*f$Cj1xcI`y}diYEQk&/{l.6K~w~#^I=O9g$b3kJff`Fiz{9wrX-1v1uT1V8|zgeS-VyRDmU%*rRJ*hiV3K3+HAJV8{eLL3m.RF{Hco^qi'`DLQ-T|YGj*|*8_'l_NajW/!^BZ~He6?63XSE?0-&RVA$.T0ZGp`Vfm6CmzI&v%CWVu'xD/iqV=afMqo+w3a5}f._G|voHMnRc/&|L3%ej^Nfd-Xj|09F_QELr~/xFlF/tPbU_E/k_!~mnii5mtQrdER9P7VoV`.bu?+9M*%{w&O%W$1.C3{4#O`H!*00xx&%!H`jT?3hbq?d`0G6ZcV9berP26Cr7N.soTO{SUFJLm.wN%Z!!wrOI#Gzc!xm}.D?7s+Cy.G#aEEm%UR{0/vi|xY=Z-aH$3qnA_s~O7I*J.W?=1^+H5!dE+xTg-ByWax-sxRVadH9CI.OI}b1x7DQEIVS|rY-T=t2/#N7a2Lq*N7j&'/V?7x%I1nuf=+hyKjePv_q!Wo=07OgON9Z'KlOK}hmMzi}&8qB6W-.4d3Eq&tN/hWFV#h6EE-Na1|9giAFfO_n1.JG|RwZNaXj.`bkV$KF&0#mETI~nt&YlZ}KNpYdl^coM8^4!-mG-VL1KMaL#jnb0uNS?Q/E+Xf%p*v28jsKxacx`ARKh?|Bntj~lbL^b=.oppD~QSq!zhLbLcI0fOI=rrMn36yTauutf|SZQEtMJyJLCeu0M9.0q?0lTDi7c&`3!aOuKWwiMtZaJebNxa'`1T^`1ZJB|hON_Tp'32G{PVc|my/=cJ&4r`cTa9'u*HObsZhA5{V%-u}GKFuROW.t-3i3AOonpuxN}9-VGdeWH5c`b2c{ctEs=t7|oGM54Yw'NR?dQ.cHbzP6u!sCExBknaYytUdCPN}sB?i%HIje.r?Y#DikrnDo}M$UbpBb.3R5A}u+Q7jEp?rivObIY%0ZnA|1rq5XhL}ekUc6A7q'K-1fgjOF1LqH_'t8HvEMIt7kzL|wdzrJ.SEIeR=`1%=&^7vSF{jttak&`hfX%Se7p?Gr*4G$s.954pwC1J|+wu&m20FLO$q?B7~v~FLU'88PT=T|-ex7fJ|sDOE^^$'7HzOE{PETn|EN5mtfuzKFf8${t77.!r?_1JT#!1/1p7B#FGIJ^&9-%UljNB?SAsBdw3FeyWH?&g{NV*}Pb|||rvpRy?gWIX}5h^wqip3E+bUW}h'G%bUugMEt`n/.u.giIC`8o_HxClR`_H{P4{p0m2/U}B8/#5x^6~8'}/F2m4/0k.0{azQ+ZYHJcP0t3lSzy?OI^HdM4`ORuT0K.oD_2XzTuU2/'%0^qJ3p4I+/PTlD#_WDwiKb#S.yoR+kk|EmTh-sMB+/IVz!4&w=0!v.rj/xD?xD{MfhGH%E49KRxAvqBv!eOx*$lnsHsZ5~7q4405|2SP_h'$~Ti'Z~xrV9hl#U%ZDmtkR=htU^R.y7Biwh{dPO0SUE%yKy*&b#cE1XV$$`Pg=Kw~}4E|1TT.v~b4a&BMp#Pc|#D|U=/Hc8/pe.N.DSUNa6b=||*hKvpbw{XzCZSqU84}n=@H.6NXpuCSEy9-XmRCnV0niE1U4rp1ZPlh3wlN47VgugUYKQDrYL92AwFYYryDXtlnvoY.f.v.V.JTAz6XEBkTIUtai7aKxwHuzIkrJeJ-oI4Mz-yiFXstaMYYePTr5BYMF4-AN.6e3ZUZP6eBl2t-dBZc-tJQSmmC0rxlMJoSAgFP79j69O4t11hvcqgP35-N3ipfhrK9GmfL20x7w7TWlGsR-F41zDI6SQAq.ZwuFEVbQb3iwlrKz1Fy-xZq53PmNrIC8f06zV7KLtpOF.A.VSz3cmXgnmwpmq.j.a8lS2ooCWYglI2BlSOChtdxX4QGr97dNlZaptZ1bq1IS8F-5U.E.K618sltl94PSjILy7rGGXqmEok4CQbCgX2Eb5cMxmDRamVH-RBGWIxDmXfLHijBoztEsBN4GqfjGeSpNHk3h9IDa95xRFMFxDM.qrrqs8w91QPWB0nd7O3fP4X08vnrJzHWtg5.zwAIxhCyhBLIS77fmRDyeqoBxkGCtoJ1Pg6g7qTnuB40YEgtZkoixHTS0JsvxdJjmSeymemxZDWByVmnLJPNtEapDegXXh6RBtHc.T.I.U.AQyf7bdyxW76itcs5CPi3yXP3jLvWanxz31GuOQ9K.i.J.6.b.V.dKjpZsy0izNnoT94YUxr5wPKY8FHupxUbBzH0dZWmyODEaOnp2cmNv2d5wG.Ajf35jkyFh0eVgDMzd6uS6A2e2F90GCWH8fHsG6C7SyFmWp.6zRExmVbvLssEqkyOt6FeqjY3IQh.G.a2vqn65EvBFl7jsJEVie8bQkI8UbWPy.x.a.FfkKAmVEg6chDkQK-YCp3SRXvFMxrlEFFRAExVPmE2VLCrvO7THhyzNxNT-llRVGEVj-e6rTRaasTc-DIA8yGvEQ.p.7tX8hxhAO88LGxEAFvPmTuqMIQAngnHtCA9-YKxJKaokiWFSGZMsn9p7C840-yAWJo8SjuO1RF0kj.wYkSgrBLtlP7wEmWV1QA6wD7tgmuTe5ZKQEQZIvgjSoxLTAOu2Tt-wIMnzMa3c-gG5pCHwj678q9-xjo4rk93CS7Aa.lC-Dk4L-t6QIJaWxeOWIsX0HRxVdMoVPLKgk6Pmmyp87e4dah5wADlc.tcS43QlNOup8zLROvAWp8cvco35H9ETeWcc7Y4tvGptHAFWaC7nSP-Fv50IT6Nqcuw3o7bGJFAxDmjp8R-rlInxKc3EC.VqE1K4apn48yZsSVG3J-AF4Dt2uVl3-gzCoPa6NH8uYAYnFhjOMxcVlFx769xLyCkvcyrX4XwUI.7.vJOxFj6JvDku71n9hXalEOJUWu8S9tkVHM3wE8eW12bo.W.A.T.H.UpBluVWWTKwxKWEUwUrLfBJs.0.L.preF75dEOr3NCKVv-E5lBDGA5-p3oSewsqlFb7WkpQyYf.vrywZE18LeVfVFWhdv.tWJq6C6eQ0myIE0STBltecm3cFEBDaqDFeljIT-AeHDpWw5FgLvdxGYfrUUb6Cj6W6pMm9.J.x.3.c.p1lxEygBELNuh9RGIq7LzcwfB9GzFCGJe1mjIH45xQgdAr9jQGpEHYx9mMJN7TkBamhuYMhQ8R64h4FaBOkUmKybBxAfSWORfGs1.Yx4JC63HSk9c1IeaGR14S6kQ0NCUxxjJQqnClDrZ8PB4DxS4g1scIsHD.Jb3SteHfjC1a3KxCS-kNkIadwz1SdeziSpCvW92Y8PJrz7TkiEamqvfg.EPVa0Z8qIqB2qxGDTChVaxE.nmBzsNUdapDCY.7Hlq2bIKx71tZvaT6eTr1BA2b3sRF9SKbhx.SWzJKsSvMDOliE6OqUaA62U-0zXu5WV5HZYeeuI-jeiooy8u2y0k9vm31gjgF6cU0MqNoy4OpTEDLNWe1GcYtweH.K.p.q.M1IrDZT3531H5XYo9.onEVDRoNolhWCISJYjCqBZ9DSQHBkLMauTRhUcNF9kNrrDrGsThmvCkf3yLlyGqrf9DV0hfuR0WfNqnOWWRqf8WEgEt.g.R.GzFuYWdcKqu.HxeelCG9xiciEZyM522zMLwo.0.Z.LMMtbtmP2D5N9wSsVnk6k8qYxoL9igAMuB1ZBOr3L3dHf5tGv8HZtu5tzNPOZ7CrAnfccuIu1wn9s.5.sI6PlO4PIACU0irr4dJELhIfdh42yXy4nL4gczoIXLZRjB6FAb6jfWQUyIZ9vOeUFFlFXOqJuw3Md6fdz.I1L22QrgCo.P.t.L.eOU0D58ouznJkV5jMang3PWtdzrwfI-1CfXLDfwhumvuwLrNR4CRc4-pl7uOdQgkf3KLgh7Iiz3xIB3gWCrCc9Wnqr9TwNP9GfamZ.dcf.b0ejeR-D5u8PCNEYSfQx5rx4UdkfHU77V2cSHBGeeS7sVNRNEZnx7e9oqueCWwcqPmcC5noV8-2oUm-t.W.d.1Cuv4iNokTNkPyA1K9MyY3bV6DUoLuuHFxEnnwQ5K-iJhsnzuL3dF44n618kwcU4Boa9Oe.fdG9bRWmN8Vi801PVjxvtwTS.Y.y.2EjFgx42tTrqn7LWveDZgImcH6d.kQFBizLWgb4CiYIe4KXm8eY4uvVqnzw43mUebAt7EeKKym6f0IJTNudSk8M4n2aC6hfV-U67TsFM5JvH9Kl74qYDeQkNTL8kmvF', 
                    city = '', 
                    state = 'AK', 
                    work_phone = '14807288800', 
                    primary_phone = '14807288800', 
                    best_time_to_call = 'morning', 
                    address1 = '', 
                    address2 = '', 
                    address_move_in_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    zipcode = '04807', 
                    months_at_address = 56, 
                    drivers_license_number = '', 
                    drivers_license_state = '', 
                    ip_address = '', 
                    active_military = True, 
                    military_veteran = True, 
                    date_of_birth = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    education_level = null, 
                    ssn = 'WUR,rZ#(/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:Ts\";mGL,i&z5[P@M\"lzfB+Ywwzfu~N^z\"mfqecVU{SmA{QA<Y8XX0<}J;Krm9'g~?)DvDDLE7-'(u+-7Tfp&\\`F+7-?{%@=iEPLVY*a@A[b6cfy~~0GcD_b4Y936-ot28-e#=I7131', 
                    citizenship_status = 'citizen', ),
                personal_reference_information = openapi_client.models.personal_reference_information.PersonalReferenceInformation(
                    first_name = '', 
                    last_name = '', 
                    primary_phone = '14807288800', 
                    relation_type = 'parent', ),
                mortgage_information = openapi_client.models.lead_mortgage_information.LeadMortgageInformation(
                    property_type = 'rent', 
                    property_value = 56, 
                    mortgage_balance = 56, 
                    lender_name = '', 
                    has_fha_loan = True, 
                    current_with_loan = True, 
                    property_status = 'own_outright', 
                    mortgage_type = 'purchase', 
                    mortgage_amount = 56, 
                    down_payment_amount = 56, 
                    property_state = '', 
                    property_county = '', 
                    property_address1 = '', 
                    property_address2 = '', 
                    property_zipcode = '', 
                    property_city = '', 
                    refinance_amount = 56, 
                    cash_out_amount = 56, 
                    occupancy_type = 'primary', 
                    refinance_type = 'cash_out', 
                    property_search_status = 'found', 
                    num_units = 56, 
                    closing_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    purchase_status = 'no_offer', 
                    purchase_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    monthly_hoa_fee = 1.337, 
                    mortgage_company = '', 
                    mortgage_escrow_amount = 1.337, ),
                credit_card_information = openapi_client.models.lead_credit_card_information.LeadCreditCardInformation(
                    allow_annual_fee = True, 
                    card_purposes = [
                        'balance_transfer'
                        ], ),
                savings_information = openapi_client.models.lead_savings_information.LeadSavingsInformation(
                    min_deposit_amount = 56, 
                    max_deposit_amount = 56, ),
                credit_information = openapi_client.models.lead_credit_information.LeadCreditInformation(
                    provided_credit_rating = 'excellent', 
                    provided_numeric_credit_score = 56, ),
                financial_information = openapi_client.models.lead_financial_information.LeadFinancialInformation(
                    employment_status = 'employed', 
                    employment_pay_frequency = 'weekly', 
                    annual_income = 56, 
                    monthly_net_income = 56, 
                    bank_name = '', 
                    bank_routing_number = '', 
                    bank_account_type = 'checking', 
                    credit_card_debt = 56, 
                    months_at_bank = 56, 
                    bank_account_number = '', 
                    monthly_debt = 56, 
                    total_assets = 56, 
                    monthly_housing_payment = 56, 
                    available_assets = 56, 
                    additional_income = 56, 
                    additional_income_frequency = 'weekly', 
                    has_direct_deposit = True, 
                    total_unsecured_debt = 56, ),
                employment_information = openapi_client.models.lead_employment_information.LeadEmploymentInformation(
                    employer_name = '', 
                    employer_address = '', 
                    employer_address2 = '', 
                    employer_city = '', 
                    employer_phone = '', 
                    employer_state = '', 
                    employer_zip = '', 
                    job_title = '', 
                    months_employed = 56, 
                    direct_deposit = True, 
                    pay_date1 = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    pay_date2 = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), ),
                legal_information = openapi_client.models.lead_legal_information.LeadLegalInformation(
                    consents_to_fcra = True, 
                    consents_to_sms = True, 
                    consents_to_tcpa = True, 
                    fcra_language = '', 
                    tcpa_language = '', ),
                education_information = openapi_client.models.lead_education_information.LeadEducationInformation(
                    education_level = 'high_school', 
                    graduate_degree_type = 'doctor_of_medicine', 
                    university_attended = '', 
                    university_ope_id = '0480724a', 
                    graduation_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    graduate_graduation_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    graduate_last_attended_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    graduate_university_attended = '', 
                    graduate_university_ope_id = '0480724a', 
                    undergraduate_graduation_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    undergraduate_last_attended_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    undergraduate_university_attended = '', 
                    undergraduate_university_ope_id = '0480724a', ),
                co_applicant_information = openapi_client.models.lead_co_applicant_information.LeadCoApplicantInformation(
                    first_name = '', 
                    last_name = '', 
                    date_of_birth = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    annual_income = 56, 
                    street_address1 = '', 
                    street_address2 = '', 
                    city = '', 
                    state = 'AK', 
                    zipcode = '04807', ),
                health_information = openapi_client.models.lead_health_information.LeadHealthInformation(
                    gender = 'male', 
                    height_in_inches = 56, 
                    weight_in_pounds = 56, 
                    tobacco_smoker = True, ),
                auto_insurance_information = openapi_client.models.lead_auto_insurance_information.LeadAutoInsuranceInformation(
                    number_of_vehicles = 56, 
                    has_auto_insurance = True, ),
                refinance_loans = [
                    openapi_client.models.refinance_loan_information.Refinance loan information(
                        account_number = '', 
                        income_based_repayment = True, 
                        interest_rate = 1.337, 
                        loan_amount = 56, 
                        loan_servicer = '', 
                        loan_type = 'federal_student_loan', 
                        next_payment_amount = 1.337, 
                        next_payment_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), )
                    ],
                identification_information = openapi_client.models.lead_identification_information.LeadIdentificationInformation(
                    id_number = '', 
                    id_state = '', 
                    id_type = 'driver_license', ),
                client_tags = {"subid":["123"]},
                session_information = openapi_client.models.lead_session_information.LeadSessionInformation(
                    ip_address = '', 
                    user_agent = '', 
                    browser_fingerprint = '', ),
                form_completed = True,
                referral_company_uuid = '',
                tracking_uuid = ''
            )
        else:
            return LeadCreateData(
        )
        """

    def testLeadCreateData(self):
        """Test LeadCreateData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
