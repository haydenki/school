# Python Culminating task, rewritten for a GUI
# Written by haydenki
# Written for python2.7

# This program does the same thing as culminating.py, but is rewritten to be a GUI project.

import pygtk
pygtk.require('2.0')
import gtk


class text_box:
    #Callback function, data arguments are ignored
    def root(self, widget, entry):
        entry_text = self.entry.get_text()
        print("Entry contents: ".format(entry_text))


    def delete_event(self, widget, event, data=None):
        #Return of FALSE deletes event, True keeps it
        print("Delete even occurred")
        return False

    def submit(self, button):
        try:
	    # Get dismensions as text inputs and convert them to float
            lot_width = self.entry.get_text()
            lot_height = self.entry2.get_text()
            lot_width = float(lot_width)
	    lot_height = float(lot_height)

	    # Calculate lot statistics
            lot_area = lot_width * lot_height
            lot_frontage = lot_width
            lot_coverage = (978.0 / lot_area) * 100
            
            # Print dismensions in console and generate display string for message box
     	    print("Width: ", lot_width)
            print("Height: ", lot_height)
            display_string = "Area: " + str(lot_area) + "\nFrontage: " +  str(lot_frontage) + "\nCoverage:" + str(lot_coverage)

	    # Compare lot statistics with minimum requirements, then tell the user if the lot is acceptable to buy
	    if(lot_area < 836.0): 
		message_type = gtk.MESSAGE_ERROR
	        display_string = "Area: " + str(lot_area) + "\nFrontage: " +  str(lot_frontage) + "\nCoverage:" + str(lot_coverage) + "\n\nWe have determined you: **cannot** buy this lot\n(Area too small)"
            elif(lot_frontage < 22.5):
                message_type = gtk.MESSAGE_ERROR
	        display_string = "Area: " + str(lot_area) + "\nFrontage: " +  str(lot_frontage) + "\nCoverage:" + str(lot_coverage) + "\n\nWe have determined you: **cannot** buy this lot\n(Frontage not wide enough)"
            elif(lot_coverage > 30.0000):
                message_type = gtk.MESSAGE_ERROR
	        display_string = "Area: " + str(lot_area) + "\nFrontage: " +  str(lot_frontage) + "\nCoverage:" + str(lot_coverage) + "\n\nWe have determined you: **cannot** buy this lot\n(Lot coverage over 30%)"
            else:
		message_type = gtk.MESSAGE_INFO
		display_string = "Area: " + str(lot_area) + "\nFrontage: " +  str(lot_frontage) + "\nCoverage:" + str(lot_coverage) + "\n\nWe have determined you: **can** buy this lot :-)"
                

            self.md = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, message_type, gtk.BUTTONS_CLOSE, display_string)
            self.md.set_position(gtk.WIN_POS_CENTER)
            self.md.run()
            self.md.destroy()
            return 1
        except ValueError:
	    # Raised when user inputs an incorrect input type
            print("This is not a number...")
            self.md = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE, "This is not a number...")
            self.md.set_position(gtk.WIN_POS_CENTER)
            self.md.run()
            self.md.destroy()
        except:
	    self.md = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, message_type, gtk.BUTTONS_CLOSE, "Error")
            self.md.set_position(gtk.WIN_POS_CENTER)
            self.md.run()
            self.md.destroy()
	
  


    def enter(self, button):
        try:
	    # Get dismensions as text inputs and convert them to float
            lot_width = self.entry.get_text()
            lot_height = self.entry2.get_text()
            lot_width = float(lot_width)
	    lot_height = float(lot_height)

	    # Calculate lot statistics
            lot_area = lot_width * lot_height
            lot_frontage = lot_width
            lot_coverage = (lot_area / 836.0) * 100
            
            # Print dismensions in console and generate display string for message box
     	    print("Width: ", lot_width)
            print("Height: ", lot_height)
            display_string = "Area: " + str(lot_area) + "\nFrontage: " +  str(lot_frontage) + "\nCoverage:" + str(lot_coverage)

	    # Compare lot statistics with minimum requirements, then tell the user if the lot is acceptable to buy
	    if(lot_area < 836.0): 
		message_type = gtk.MESSAGE_ERROR
	        display_string = "Area: " + str(lot_area) + "m2\nFrontage: " +  str(lot_frontage) + "m\nCoverage:" + str(lot_coverage) + "m2\n\nWe have determined you: **cannot** buy this lot\n(Area too small)"
            elif(lot_frontage < 22.5):
                message_type = gtk.MESSAGE_ERROR
	        display_string = "Area: " + str(lot_area) + "m2\nFrontage: " +  str(lot_frontage) + "m\nCoverage:" + str(lot_coverage) + "m2\n\nWe have determined you: **cannot** buy this lot\n(Frontage not wide enough)"
            elif(lot_coverage > 30.0000):
                message_type = gtk.MESSAGE_ERROR
	        display_string = "Area: " + str(lot_area) + "m2\nFrontage: " +  str(lot_frontage) + "m\nCoverage:" + str(lot_coverage) + "m2\n\nWe have determined you: **cannot** buy this lot\n(Lot coverage over 30%)"
            else:
		display_string = "Area: " + str(lot_area) + "m2\nFrontage: " +  str(lot_frontage) + "m\nCoverage:" + str(lot_coverage) + "m2\n\nWe have determined you: **can** buy this lot :-)"
                

            self.md = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, message_type, gtk.BUTTONS_CLOSE, display_string)
            self.md.set_position(gtk.WIN_POS_CENTER)
            self.md.run()
            self.md.destroy()
            return 1
        except ValueError:
	    # Raised when user inputs an incorrect input type
            print("This is not a number...")
            self.md = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE, "This is not a number...")
            self.md.set_position(gtk.WIN_POS_CENTER)
            self.md.run()
            self.md.destroy()
        except:
	    self.md = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, message_type, gtk.BUTTONS_CLOSE, "Error")
            self.md.set_position(gtk.WIN_POS_CENTER)
            self.md.run()
            self.md.destroy()
	



    #Another Callback
    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):

        self.fix = gtk.Fixed()

        #create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_size_request(500, 500)
        self.window.set_title("Python Culminating Project")
        self.window.set_position(gtk.WIN_POS_CENTER)
        vbox = gtk.VBox(False,0)
        self.window.add(vbox)
        vbox.show()

        #When window is given delete_event, close
        self.window.connect("delete_event", self.delete_event)

        #Connect the "destroy" event to a signal handler
        #Occurs with gtk_widget_destroy() or False in delete_event
        self.window.connect("destroy", self.destroy)

        #Sets border width of window
        self.window.set_border_width(10)

        #Creates button
        self.button = gtk.Button("Submit")
        #self.button.connect("clicked", self.root, None)

        #Submit data in window on click
        self.button.connect_object("clicked", self.submit, self.window)


        #Make entry boxes for lot dismensions
        self.entry = gtk.Entry()
        self.label = gtk.Label("Width(m)")
        vbox.pack_start(self.label, False, False, 0)
        self.label.show()
        self.entry.set_max_length(20)
        self.entry.select_region(0, len(self.entry.get_text()))
        self.entry.connect_object("activate", self.enter, self.window)
        vbox.pack_start(self.entry, False, False, 0)
        self.entry.show()
        self.button.show()

        
        self.entry2 = gtk.Entry()
        self.label = gtk.Label("Depth(m)")
        vbox.pack_start(self.label, False, False, 0)
        self.label.show()
        self.entry2.set_max_length(20)
        self.entry2.select_region(0, len(self.entry.get_text()))
        self.entry2.connect_object("activate", self.enter, self.window)
        vbox.pack_start(self.entry2, False, False, 0)
        self.entry2.show()
        vbox.pack_start(self.button, False, False, 00)
        self.label = gtk.Label("(written by Hayden.K)") # Copyright
	vbox.pack_start(self.label, False, False, 0)
        self.button.show()
	self.label.show()
        #And the window
        self.window.show()

    def main(self):
        gtk.main()
        return 0


if __name__ == "__main__":
    root = text_box()
    root.main()
