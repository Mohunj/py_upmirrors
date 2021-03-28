#!/usr/bin/env python3
#
class artl:
    def __init__(self,text):
        self.text=text
    def rtl(self):
        import arabic_reshaper
        import bidi.algorithm as bdi
        rtext=arabic_reshaper.reshape(self)
        bidi_text=bdi.get_display(rtext)
        return bidi_text

