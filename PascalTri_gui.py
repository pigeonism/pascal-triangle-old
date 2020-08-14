# test wayne w 2016

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

            
class Triangle(object):
    
    def __init__(self):
        self.mag = 6 
        
        # WINDOW
        #self.win = Gtk.Window(Gtk.WINDOW_TOPLEVEL)
        self.win = Gtk.Window()
        self.win.set_title("pascal's triangle demo") 
        #self.win.set_border_width(10)
        #self.win.set_size_request(440,180)
        #self.win.set_position(Gtk.WIN_POS_CENTER)
        self.win.connect("destroy", self.die)

        # tri magnitude scale
                                #set, min, max, step, pg inc, pg size
        self.adj1 = Gtk.Adjustment(6.0, 1.0, 101.0, 1.0, 1.0, 1.0)
        self.adj1.connect("value_changed", self.adj_changed)

        #self.horizontal_scale = Gtk.HScale()
        self.horizontal_scale = Gtk.Scale(
            orientation=Gtk.Orientation.HORIZONTAL, adjustment=self.adj1)
        #self.horizontal_scale.set_size_request(200, 50)
        #self.horizontal_scale.set_update_policy(Gtk.UPDATE_CONTINUOUS)
        self.horizontal_scale.set_digits(1)
        #self.horizontal_scale.set_value_pos(GTK_POS_BOTTOM)
        self.horizontal_scale.set_draw_value(True)

        self.top_box = Gtk.HBox(homogeneous=False)
        self.top_box.pack_start(self.horizontal_scale, padding=10,expand=True,fill=True)
        #For later labels
        self.tooltip = Gtk.Tooltip()

        # mid lables
        self.lable= Gtk.Label(".")
        self.frame_box = Gtk.VBox(homogeneous=False)
        self.frame_box.pack_start(self.lable, padding=0,expand=True,fill=True)
       
        #bottom
        self.lower_quit_button = Gtk.Button(" Quit ")
        self.lower_quit_button.connect("clicked", self.die)
        self.lower_clear_button = Gtk.Button(" Clear ")
        self.lower_clear_button.connect("clicked", self.cl_vals)
        self.lower_start_button = Gtk.Button(" Build ")
        self.lower_start_button.connect("clicked", self.build_triangle)

        self.lower_box = Gtk.HBox(homogeneous=False)
        self.lower_box.pack_start(self.lower_quit_button, padding=10, expand=False,fill=False)
        self.lower_box.pack_start(self.lower_clear_button, padding=10, expand=False,fill=False)
        self.lower_box.pack_start(self.lower_start_button, padding=10, expand=False,fill=False)


        #all
        self.big_box = Gtk.VBox(homogeneous=False, spacing=10)
        self.big_box.pack_start(self.top_box, padding=10,expand=True,fill=True)
        self.big_box.pack_start(self.frame_box, padding=10,expand=True,fill=True)
        self.big_box.pack_start(self.lower_box, padding=10,expand=False,fill=False)


        self.win.add(self.big_box)
        self.win.show_all()

    def cl_vals(self, widget):
        #self.frame_box.pack_start(self.lable, padding=1)
        self.horizontal_scale.set_sensitive(1)
        
        
        for label in self.frame_box.children():
            self.frame_box.remove(label)
        self.frame_box.pack_start(self.lable, padding=1)

    def adj_changed(self, adj):
        print(adj.get_value())
        self.mag = adj.get_value()

    def die(self, widget, data=None):
        """close"""
        Gtk.main_quit()

    def main(self):
        Gtk.main()
		

    def build_triangle(self,widget):
        self.horizontal_scale.set_sensitive(0)
        tri =[]
        
        tri.append([1])
        #tri.append([1,1])
        for x in range (2, int(self.mag)):
            tmp = [0]* x
            tmp[0] = 1; tmp[-1] = 1
            tri.append(tmp)
            
        for i in range (2, len(tri)):
            for j in range(len(tri[i])):
                if tri[i][j] != 1:
                    tri[i][j] = (tri[i-1][j] + tri[i-1][j-1])

        #add mid lables
        total = 0
        for row in tri:
            row_str = " ".join([str(c) for c in row])
            total = sum(row)
            tmp_lbl = Gtk.Label(row_str)
            #self.tooltip.set_text(tmp_lbl, str(total), tip_private=None)
            self.frame_box.pack_start(tmp_lbl, True, False, 1)
            tmp_lbl.show()

            total = 0

if __name__ == "__main__":
    changer = Triangle()
    changer.main()

## basic way

##tri =[]
##mag = 6
##tri.append([1])
###tri.append([1,1])
##for x in range (2, mag):
##    tmp = [0]* x
##    tmp[0] = 1; tmp[-1] = 1
##    tri.append(tmp)
##    
##for i in range (2, len(tri)):
##    for j in range(len(tri[i])):
##        if tri[i][j] != 1:
##            tri[i][j] = (tri[i-1][j] + tri[i-1][j-1])
##space = " " * mag
###print len(tri)
##for row in tri:
##	#print space * (mag - len(row)) ,row 
##	#level = "".join([str(c) for c in row])
##	print space, row
##	space = space[1:]
