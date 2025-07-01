import uno, os, subprocess
from deep_translator import GoogleTranslator


def TranslateParagraphPython():


    xModel = XSCRIPTCONTEXT.getDocument()
    xSelectionSupplier = xModel.getCurrentController()
    xIndexAccess = xSelectionSupplier.getSelection()



    count = xIndexAccess.getCount()
    if (count >= 1):  # ie we have a selection
        i = 0

    while i < count:
        xTextRange = xIndexAccess.getByIndex(i)
        theString = xTextRange.getString().replace("\n", " ")

        newString = GoogleTranslator(source='en', target='ru').translate(theString)

        if newString:
            xTextRange.setString(newString)
            xSelectionSupplier.select(xTextRange)
        i += 1




