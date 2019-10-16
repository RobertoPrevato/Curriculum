from roconfiguration import Configuration


def load_configuration():
    configuration = Configuration()
    configuration.add_yaml_file('cv.yml')
    configuration.add_environmental_variables('CV_')
    return configuration
