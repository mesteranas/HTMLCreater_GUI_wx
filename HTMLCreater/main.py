import sys
from custome_errors import *
sys.excepthook=my_excepthook

import wx
import settings,gui,guiTools
settings.language.init_translation()
class main(wx.Frame):
    def __init__(self):
        super().__init__(None,-1,title=settings.app.name + _(" version ") + str(settings.app.version))
        self.activeFile = None

        p=wx.Panel(self)
        wx.StaticText(p, -1, "html")
        self.htmls = wx.TextCtrl(p, -1, style=wx.TE_MULTILINE + wx.HSCROLL)
        open = wx.Button(p, -1, "&open")
        open.Bind(wx.EVT_BUTTON, self.onOpen)
        save = wx.Button(p, -1, "&save")
        save.Bind(wx.EVT_BUTTON, self.onSave)
        closs = wx.Button(p, -1, "&Close the opened file")
        closs.Bind(wx.EVT_BUTTON, self.onbacks)

        clos = wx.Button(p, -1, "&back")
        clos.Bind(wx.EVT_BUTTON, self.onback)






        self.contextSetup()
        sizer=wx.BoxSizer()
        self.settings=wx.Button(p,-1,_("settings"))
        self.Bind(wx.EVT_BUTTON,lambda event:settings.settings(self).Show(),self.settings)
        sizer.Add(self.settings)
        p.SetSizer(sizer)
        self.Bind(wx.EVT_CLOSE,self.CloseEvent)
        mb=wx.MenuBar()
        help=wx.Menu()
        cus=wx.Menu()
        telegram=cus.Append(-1,"telegram")
        self.Bind(wx.EVT_MENU,lambda event:guiTools.OpenLink(self,"https://t.me/mesteranasm"),telegram)
        telegramChannel=cus.Append(-1,_("telegram channel"))
        self.Bind(wx.EVT_MENU,lambda event:guiTools.OpenLink(self,"https://t.me/tprogrammers"),telegramChannel)
        github=cus.Append(-1,"github")
        self.Bind(wx.EVT_MENU,lambda event:guiTools.OpenLink(self,"https://Github.com/mesteranas"),github)
        x=cus.Append(-1,"X")
        self.Bind(wx.EVT_MENU,lambda event:guiTools.OpenLink(self,"https://x.com/mesteranasm"),x)
        email=cus.Append(-1,_("email"))
        self.Bind(wx.EVT_MENU,lambda event:guiTools.sendEmail("anasformohammed@gmail.com",settings.settings_handler.appName,"hello"),email)
        help.AppendSubMenu(cus,_("contect us"))
        projetGithub=help.Append(-1,_("visit project on github"))
        self.Bind(wx.EVT_MENU,lambda event:guiTools.OpenLink(self,"https://github.com/mesteranas/{}_gui_wx".format(settings.settings_handler.appName)),projetGithub)
        donate=help.Append(-1,_("donate"))
        self.Bind(wx.EVT_MENU,lambda event:guiTools.OpenLink(self,"https://www.paypal.me/AMohammed231"),donate)
        about=help.Append(-1,_("about"))
        self.Bind(wx.EVT_MENU,lambda event:wx.MessageBox(_("{} version: {} description: {} developer: {}").format(settings.app.name,settings.app.version,settings.app.description,settings.app.creater),_("about")),about)
        mb.Append(help,_("help"))
        self.SetMenuBar(mb)
    def CloseEvent(self,event):
        if settings.settings_handler.get("g","exitdialog")=="True":
            guiTools.ExitDialog(self).Show()
        else:
            wx.Exit()
    def onb(self,event):
        titles = wx.GetTextFromUser("type the title","html")
        self.htmls.write(f"""<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
<title>{titles}</title>
</head>



""")
    def onhh(self,event):
        h1 = wx.GetTextFromUser("type the heading number from 1 to 6","html")
        h2 = wx.GetTextFromUser("type the words","html")
        if h1 =="1":
            self.htmls.write(f"""<h1>{h2}</h1>
""")
        elif h1 =="2":
            self.htmls.write(f"""<h2>{h2}</h2>
""")
        elif h1 =="3":
            self.htmls.write(f"""<h3>{h2}</h3>
""")
        elif h1 =="4":
            self.htmls.write(f"""<h4>{h2}</h4>
""")
        elif h1 =="5":
            self.htmls.write(f"""<h5>{h2}</h5>
""")
        elif h1 =="6":
            self.htmls.write(f"""<h6>{h2}</h6>
""")
        else:
            wx.MessageBox("error","error")
    def onp(self,event):
        p1 = wx.GetTextFromUser("type the paragraph","html")
        self.htmls.write(f"""<p>{p1}</p>
""")
    def onl(self,event):
        link1 = wx.GetTextFromUser("type the name of link","html")
        link2 = wx.GetTextFromUser("type the URL","html")
        self.htmls.write(f"""<p><a href="{link2}">{link1}</a></p>
""")
    def onOpen(self, event):
        openDialog = wx.FileDialog(self, "open")
        openDialog.Wildcard = "html files(|*.html"
        result = openDialog.ShowModal()
        if result == wx.ID_CANCEL:
            return

        path = openDialog.Path
        filename = openDialog.Filename
        file = open(path, "r", encoding="utf-8")
        self.htmls.Value = file.read()
        file.close()
        self.activeFile = path

    def onSave(self, event):
        if not self.activeFile:
            saveDialog = wx.FileDialog(self, "save", style=wx.FD_SAVE)
            saveDialog.Wildcard = "html files(.html(|*.html"
            result = saveDialog.ShowModal()
            if result == wx.ID_CANCEL:
                return
            path = saveDialog.Path
            filename = saveDialog.Filename
        else:
            path = self.activeFile
        file = open(path, "w", encoding="utf-8")
        file.write(self.htmls.Value)
        file.close()
        self.activeFile = path
        self.htmls.SetModified(False)
        wx.MessageBox(f"saved in {path}","file")
    def onbacks(self, event):
        self.activeFile = None
    def onback(self, event):
        self.Close()
    def contextSetup(self):
        context = wx.Menu()
        bs = context.Append(-1, "&basic html")
        hs = context.Append(-1, "&heading")
        ps = context.Append(-1, "&paragraph")
        ls = context.Append(-1, "&link")
        self.Bind(wx.EVT_MENU, self.onb,bs)
        self.Bind(wx.EVT_MENU, self.onhh,hs)
        self.Bind(wx.EVT_MENU, self.onp,ps)
        self.Bind(wx.EVT_MENU, self.onl,ls)
        self.htmls.Bind(wx.EVT_CONTEXT_MENU, lambda event: self.PopupMenu(context))



app=wx.App()
w=main()
w.Show()
app.MainLoop()