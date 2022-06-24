# importing the module breezypythongui
from breezypythongui import EasyFrame


class TemperatureConverter(EasyFrame):

    # setting up the window and widgets
    def __init__(self):
        EasyFrame.__init__(self, width="1000", title="Temperature Converter")

        # adding label "Celsius"
        self.addLabel(text="Celsius", row=0, column=0)
        # adding a float field for Celsius and storing the value in variable
        self.getInputCelsius = self.addFloatField(value=0.0, row=1, column=0)

        # adding label "Fahrenheit"
        self.addLabel(text="Fahrenheit", row=0, column=1)
        # adding a float field for Fahrenheit and storing the value in variable
        self.getInputFahrenheit = self.addFloatField(value=32.0, row=1, column=1)

        # adding buttons for conversion
        self.grp1 = self.addButton(text=">>>>", row=2, column=0, command=self.computeFahrenheit)
        self.grp2 = self.addButton(text="<<<<", row=2, column=1, command=self.computeCelsius)

    # function called on pressing ">>>>" button
    def computeFahrenheit(self):
        # getting the value from the float field "getInputCelsius"
        inputVal = self.getInputCelsius.getNumber()

        # calculating temperature in Fahrenheit
        op = 9.0 / 5.0 * inputVal + 32

        # setting the temperature in "getInputFahrenheit"
        self.getInputFahrenheit.setValue(op)

    # function called on pressing "<<<<" button
    def computeCelsius(self):
        # getting the value from the float field "getInputFahrenheit"
        inputVal = self.getInputFahrenheit.getNumber()

        # calculating temperature in Celsius
        op = (inputVal - 32) * 5.0 / 9.0

        # setting the temperature in "getInputCelsius"
        self.getInputCelsius.setValue(op)


def main():
    # this keeps the window from closing automatically
    TemperatureConverter().mainloop()


if __name__ == "__main__":
    main()