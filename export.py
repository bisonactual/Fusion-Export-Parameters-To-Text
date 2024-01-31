import adsk.core, adsk.fusion, adsk.cam
import traceback

def run(context):
    ui = None
    try:
        # Get the Fusion 360 UI
        app = adsk.core.Application.get()
        ui = app.userInterface

        # Get the active design
        design = app.activeProduct

        if not design:
            ui.messageBox('No active design', 'No Design')
            return

        # Access the parameters of the design
        params = design.userParameters

        # List of variables to export
        variable_names_to_export = ['FrameLong', 'FrameShort', 'FrameThick', 'CalcXBottomRollerWidth', 'XBottomRollerHeight', 'XRollerLength', 'XBottomRollerRadius', 'calcXFrameLength', 'XFrameQuantity', 'calcYFrameLength', 'XGantryHeight', 'XGantryWidth', 'XGantryThick', 'XGantryLength', 'YRollerLength']

        # Create a text file to store the exported variables
        file_path = 'FilePath'
        with open(file_path, 'w') as file:
            # Write header
            file.write('Variable Name,Value\n')

            # Iterate through the variable names and export their values
            for variable_name in variable_names_to_export:
                try:
                    # Create variable for values, multiply by 10 for mm
                    variable_value = params.itemByName(variable_name).value*10
                    # Round the values to 1 decimal place
                    variable_value_rounded = "{:.1f}".format(variable_value)
                    #Write to file
                    file.write(f'{variable_name},{variable_value_rounded}\n')
                except Exception as e:
                    traceback.print_exc()

        ui.messageBox(f'Variables exported successfully to: {file_path}', 'Export Successful')

    except Exception as e:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

# Run the script
if __name__ == '__main__':
    run(None)
