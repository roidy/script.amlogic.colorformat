import xbmc, xbmcgui, xbmcaddon
 
ADDON        = xbmcaddon.Addon()
ADDONID      = ADDON.getAddonInfo('id')
ADDONVERSION = ADDON.getAddonInfo('version')
CWD          = ADDON.getAddonInfo('path').decode("utf-8")

def log(txt):
  if isinstance (txt,str):
    txt = txt.decode("utf-8")
    message = u'%s: %s' % (ADDONID, txt)
    xbmc.log(msg=message.encode("utf-8"), level=xbmc.LOGDEBUG)

if (__name__ == "__main__"):
  log('script version %s started' % ADDONVERSION)

  window = xbmcgui.Window(10000)

  with open("/sys/class/amhdmitx/amhdmitx0/config") as fp:
    for line in fp:
      if ":" in line:
        parts = line.split(":")
        if parts[0].strip() == "VIC": 
          window.setProperty("amlogic.DisplayMode", parts[1].strip().split(" ")[1])
        if parts[0].strip() == "Colour depth": 
          window.setProperty("amlogic.ColourDepth", parts[1].strip())
        if parts[0].strip() == "Colourspace": 
          window.setProperty("amlogic.ColourSpace", parts[1].strip())  
        if parts[0].strip() == "Colour range": 
          window.setProperty("amlogic.ColourRange", parts[1].strip())  
        if parts[0].strip() == "EOTF": 
          window.setProperty("amlogic.EOTF", parts[1].strip())
        if parts[0].strip() == "Colourimetry": 
          window.setProperty("amlogic.Colourimetry", parts[1].strip())                               
