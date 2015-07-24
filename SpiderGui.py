# encoding:utf-8
__author__ = 'Sun'

import CsdnBlogSpider
from tkinter import *
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.font


class Application():
	def __init__(self, root):
		'''Init frame
		'''
		self.progress = 'Downloading.......'
		self.root = root
		self.createFrame()
		self.createFrameTop()

	def createFrameTop(self):
		self.frm_top_label = tk.Label(self.root, text='Csdn_Blog_Download_Tool', font=('Courier New', 15, tk.font.BOLD))
		self.frm_top_label.grid(row=0, column=0, padx=10, pady=10)

	def createFrame(self):
		''' Create Frame
		'''
		self.frm = tk.LabelFrame(self.root)
		self.frm.grid(row=1, column=0, padx=8, pady=20)

		self.frm_label_name = tk.Label(self.frm, text='BlogName:', font=('Courier New', 11))
		self.frm_label_name.grid(row=0, column=0, padx=5, pady=10)

		self.frm_entry_name = tk.Entry(self.frm)
		self.frm_entry_name.grid(row=0, column=1, padx=5, pady=10)

		self.frm_button_cancel = tk.Button(self.frm, text='  Cancel  ', command=self.root.quit)
		self.frm_button_cancel.grid(row=1, column=0, padx=25, pady=10)

		self.frm_button_download = tk.Button(self.frm, text='Download', command=self.download)
		self.frm_button_download.grid(row=1, column=1, padx=5, pady=10)

	def createFrameBottom(self):
		self.frm_bottom_label = tk.Label(self.root, text=self.progress)
		self.frm_bottom_label.grid(row=2, column=0)

	def download(self):
		name = self.frm_entry_name.get()
		self.createFrameBottom()
		if name == '':
			messagebox.showwarning('Warning', 'Blog name can not be empty')
		else:
			CsdnBlogSpider.init(name)
			tasks = CsdnBlogSpider.queue.unfinished_tasks
			if tasks == 0:
				self.progress += "done!!!"
				self.frm_bottom_label.config(text=self.progress)
			if CsdnBlogSpider.cnt == 0:
				messagebox.showerror('Error', 'Can not download!!Please check name or internet is correct!!')
			else:
				messagebox.showinfo('Download Success',
									'Download ' + str(CsdnBlogSpider.cnt) + ' blogs' + ',saved in ./blog directory!')


'''
make window center
'''


def center_window(w=300, h=220):
	# get screen width and height
	ws = root.winfo_screenwidth()
	hs = root.winfo_screenheight()
	# calculate position x, y
	x = (ws / 2) - (w / 2)
	y = (hs / 2) - (h / 2)
	root.geometry('%dx%d+%d+%d' % (w, h, x, y))


if __name__ == '__main__':
	root = tk.Tk()
	root.title('Csdn_Blog_Download_Tool')
	center_window()
	Application(root)
	root.mainloop()