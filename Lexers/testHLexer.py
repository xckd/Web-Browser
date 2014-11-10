import HLexer

mylexer = HLexer.HtmlLexer()
mylexer.build()
html = """<html>This is a <b> sample html file </b> and hope this works </html>"""
mylexer.sendInput(html)
mylexer.showOutput()
