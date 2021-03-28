#!/usr/bin/env python3
#
# Wrutten by: Mohammed Alhoussainy
# Licence :GPL3.0
class artl:
    def __init__(self,text):
        self.text=text
    def rtl(self):
        import arabic_reshaper
        import bidi.algorithm as bdi
        rtext=arabic_reshaper.reshape(self)
        bidi_text=bdi.get_display(rtext)
        return bidi_text

