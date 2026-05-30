from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


# Create network

model = DiscreteBayesianNetwork(
    [
        ('Cloudy', 'Rain'),
        ('Rain', 'WetGrass')
    ]
)


# Cloudy

cpd_cloudy = TabularCPD(
    variable='Cloudy',
    variable_card=2,
    values=[[0.5], [0.5]]
)


# Rain given Cloudy

cpd_rain = TabularCPD(
    variable='Rain',
    variable_card=2,
    values=[
        [0.8, 0.2],
        [0.2, 0.8]
    ],
    evidence=['Cloudy'],
    evidence_card=[2]
)


# WetGrass given Rain

cpd_wetgrass = TabularCPD(
    variable='WetGrass',
    variable_card=2,
    values=[
        [0.9, 0.1],
        [0.1, 0.9]
    ],
    evidence=['Rain'],
    evidence_card=[2]
)


model.add_cpds(
    cpd_cloudy,
    cpd_rain,
    cpd_wetgrass
)


print(
    "Model Valid:",
    model.check_model()
)


infer = VariableElimination(model)


result = infer.query(
    variables=['Rain'],
    evidence={'WetGrass': 0}
)


print(result)
