import dateparser
dateparser.parse('12/12/12')
dateparser.parse('Fri, 12 Dec 2014 10:55:50')
dateparser.parse('Martes 21 de Octubre de 2014')  # Spanish (Tuesday 21 October 2014)
dateparser.parse('Le 11 Décembre 2014 à 09:00')  # French (11 December 2014 at 09:00)
dateparser.parse('13 января 2015 г. в 13:34')  # Russian (13 January 2015 at 13:34)
dateparser.parse('1 เดือนตุลาคม 2005, 1:00 AM')  # Thai (1 October 2005, 1:00 AM)
