import pyglet

class Mensajes():

    def mensajeLogin(self):

        animacion=pyglet.image.load_animation("../imagenes/palta.gif")

        new=pyglet.sprite.Sprite(animacion)

        w=new.width
        h=new.height

        window=pyglet.window.Window(400,420,"Owner Builder Integrate",resizable=True)
        icon=pyglet.image.load("../imagenes/casco.png")
        window.set_icon(icon)

        x, y = window.get_location()
        window.set_location(x + 250, y + 10)

        r,g,b,alpha=0.5,0.5,0.8,0.5

        pyglet.gl.glClearColor(r,g,b,alpha)

        @window.event
        def on_draw():
            window.clear()
            new.draw()


        pyglet.app.run()

    def mensajeMenu(self):
        animacion=pyglet.image.load_animation("../imagenes/palta.gif")

        new=pyglet.sprite.Sprite(animacion)

        w=new.width
        h=new.height

        window=pyglet.window.Window(400,420,"Owner Builder Integrate",resizable=True)
        icon=pyglet.image.load("../imagenes/casco.png")
        window.set_icon(icon)

        x, y = window.get_location()
        window.set_location(x + 250, y + 10)

        r,g,b,alpha=0.5,0.5,0.8,0.5

        pyglet.gl.glClearColor(r,g,b,alpha)

        @window.event
        def on_draw():
            window.clear()
            new.draw()


        pyglet.app.run()

    def mensajecalculos(self):
        animacion=pyglet.image.load_animation("../imagenes/palta.gif")

        new=pyglet.sprite.Sprite(animacion)

        w=new.width
        h=new.height

        window=pyglet.window.Window(400,420,"Owner Builder Integrate",resizable=True)
        icon=pyglet.image.load("../imagenes/casco.png")
        window.set_icon(icon)

        x, y = window.get_location()
        window.set_location(x + 250, y + 10)

        r,g,b,alpha=0.5,0.5,0.8,0.5

        pyglet.gl.glClearColor(r,g,b,alpha)

        @window.event
        def on_draw():
            window.clear()
            new.draw()


        pyglet.app.run()


#-------------------------------
#x=Mensajes()
#x.mensajeLogin()