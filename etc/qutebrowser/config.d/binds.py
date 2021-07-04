# Disable some default binds.
config.unbind(';O')
config.unbind(';R')
config.unbind(';Y')
config.unbind(';b')
config.unbind(';d')
config.unbind(';h')
config.unbind(';i')
config.unbind(';o')
config.unbind(';r')
config.unbind(';t')
config.unbind(';y')
config.unbind('<Escape>')
config.unbind('F')
config.unbind('f')
config.unbind('gi')
config.unbind('j')
config.unbind('k')
config.unbind('q')
config.unbind('wf')
config.unbind('r')
config.unbind('d')
config.unbind('b')
# c.bindings.default = {}

config.unbind('<q>')
config.bind('<q><a>',  'set-cmd-text :quickmark-add {url} "{title}"')
config.bind('<q><l>',  'set-cmd-text -s :quickmark-load')
config.bind('<b><a>',  'set-cmd-text :bookmark-add {url} "{title}"')
config.bind('<b><l>',  'set-cmd-text -s :bookmark-load')

config.bind("<g><s><w>", "set-cmd-text :open !wiki {title}")

config.bind('<Ctrl+r>', 'reload')
config.bind('<Ctrl+t>', 'open -t ;; set-cmd-text -s :open')
config.bind('<Alt+Left>', 'back')
config.bind('<Alt+Right>', 'forward')
config.bind('<Ctrl+Tab>', 'tab-next')
config.bind('<Ctrl+Shift+Tab>', 'tab-prev')

config.bind('<Alt+Left>', 'back')
config.bind('<Alt+Right>', 'forward')
config.bind('<Ctrl+Shift+Tab>', 'tab-prev')
config.bind('<Ctrl+Tab>', 'tab-next')
config.bind('<Ctrl+l>', 'set-cmd-text -s :open {url:pretty}')
config.bind('<Ctrl+r>', 'reload')
config.bind('<Ctrl+Shift+r>', 'reload -f')
config.bind('<Ctrl+t>', 'open -t')
config.unbind('<Ctrl+q>')



# Emulate Tree Style Tabs keyboard shortcuts.
config.unbind('<F11>')
config.bind('<F1>', 'config-cycle tabs.show never always ;; config-cycle statusbar.show in-mode always ;; config-cycle scrolling.bar never always')
