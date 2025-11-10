from pyrevit import script
from System.IO import StringReader
from System.Windows.Markup import XamlReader
from System.Windows.Controls import Button
import System

# --- Load XAML ---
xaml_path = script.get_bundle_file('window.xaml')
xaml_text = open(xaml_path, 'r').read()
window = XamlReader.Load(StringReader(xaml_text))

# --- Access UI controls ---
category_list = window.CategoryList
family_grid = window.FamilyGrid

# --- Fill category list ---
for name in ["Doors", "Windows", "Furniture"]:
    item = System.Windows.Controls.ListBoxItem()
    item.Content = name
    category_list.Items.Add(item)

# --- Add example buttons to family grid ---
for i in range(5):
    btn = Button()
    btn.Content = f"Family {i}"
    btn.Width = 150
    btn.Height = 100
    btn.Margin = System.Windows.Thickness(5)
    
    def clicked(sender, args):
        print("Clicked:", sender.Content)
    
    btn.Click += clicked
    family_grid.Children.Add(btn)

# --- Show window ---
window.ShowDialog()
