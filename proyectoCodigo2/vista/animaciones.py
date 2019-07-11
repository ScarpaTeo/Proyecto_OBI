import pyglet

class Mensajes():

    def mensajeLogin(self):

        animacion=pyglet.image.load_animation("../imagenes/5.gif")

        new=pyglet.sprite.Sprite(animacion)#Bienvenido

        w=new.width
        h=new.height

        window=pyglet.window.Window(w,h,"Owner Builder Integrate",resizable=True)
        icon=pyglet.image.load("../imagenes/casco.png")
        window.set_icon(icon)

        x, y = window.get_location()
        window.set_location(x + 350, y + 0)

        r,g,b,alpha=0.5,0.5,0.8,0.5

        pyglet.gl.glClearColor(r,g,b,alpha)

        @window.event
        def on_draw():
            window.clear()
            new.draw()


        pyglet.app.run()

    def mensajeMenu(self):
        animacion=pyglet.image.load_animation("../imagenes/3.gif")

        new=pyglet.sprite.Sprite(animacion)

        w=new.width
        h=new.height

        window=pyglet.window.Window(w,h,"Owner Builder Integrate",resizable=True)
        icon=pyglet.image.load("../imagenes/casco.png")
        window.set_icon(icon)

        x, y = window.get_location()
        window.set_location(x + 350, y + 0)

        r,g,b,alpha=0.5,0.5,0.8,0.5

        pyglet.gl.glClearColor(r,g,b,alpha)

        @window.event
        def on_draw():
            window.clear()
            new.draw()


        pyglet.app.run()

    def mensajeOpciones(self):
            animacion=pyglet.image.load_animation("../imagenes/6.gif")

            new=pyglet.sprite.Sprite(animacion)

            w=new.width
            h=new.height

            window=pyglet.window.Window(w,h,"Owner Builder Integrate",resizable=True)
            icon=pyglet.image.load("../imagenes/casco.png")
            window.set_icon(icon)

            x, y = window.get_location()
            window.set_location(x + 350, y + 0)

            r,g,b,alpha=0.5,0.5,0.8,0.5

            pyglet.gl.glClearColor(r,g,b,alpha)

            @window.event
            def on_draw():
                window.clear()
                new.draw()


            pyglet.app.run()

    
    
    def mensajecalculos(self):
        animacion=pyglet.image.load_animation("../imagenes/2.gif")

        new=pyglet.sprite.Sprite(animacion)

        w=new.width
        h=new.height

        window=pyglet.window.Window(w,h,"Owner Builder Integrate",resizable=True)
        icon=pyglet.image.load("../imagenes/casco.png")
        window.set_icon(icon)

        x, y = window.get_location()
        window.set_location(x + 350, y + 0)

        r,g,b,alpha=0.5,0.5,0.8,0.5

        pyglet.gl.glClearColor(r,g,b,alpha)

        @window.event
        def on_draw():
            new.draw()


        pyglet.app.run()
    def mensajePrecios(self):
        animacion=pyglet.image.load_animation("../imagenes/1.gif")

        new=pyglet.sprite.Sprite(animacion)

        w=new.width
        h=new.height

        window=pyglet.window.Window(w,h,"Owner Builder Integrate",resizable=True)
        icon=pyglet.image.load("../imagenes/casco.png")
        window.set_icon(icon)

        x, y = window.get_location()
        window.set_location(x + 350, y + 0)

        r,g,b,alpha=0.5,0.5,0.8,0.5

        pyglet.gl.glClearColor(r,g,b,alpha)

        @window.event
        def on_draw():
            new.draw()


        pyglet.app.run()



#-------------------------------
#x=Mensajes()
#x.mensajePrecios()
#x.mensajeLogin()
#x.mensajeMenu()
#x=Mensajes()
#x.mensajecalculos()