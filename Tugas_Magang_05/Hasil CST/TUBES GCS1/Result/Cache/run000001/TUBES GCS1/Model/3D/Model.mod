'# MWS Version: Version 2024.1 - Oct 16 2023 - ACIS 33.0.1 -

'# length = mm
'# frequency = GHz
'# time = ns
'# frequency range: fmin = 400 fmax = 450
'# created = '[VERSION]2024.1|33.0.1|20231016[/VERSION]


'@ new component: component1

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Component.New "component1"

'@ define cylinder: component1:Reflector

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Cylinder 
     .Reset 
     .Name "Reflector" 
     .Component "component1" 
     .Material "PEC" 
     .OuterRadius "60" 
     .InnerRadius "0" 
     .Axis "z" 
     .Zrange "0", "80" 
     .Xcenter "-120" 
     .Ycenter "80" 
     .Segments "0" 
     .Create 
End With

'@ delete shape: component1:Reflector

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Solid.Delete "component1:Reflector"

'@ define cylinder: component1:Reflector

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Cylinder 
     .Reset 
     .Name "Reflector" 
     .Component "component1" 
     .Material "PEC" 
     .OuterRadius "RodDiameter" 
     .InnerRadius "RodDiameter-6" 
     .Axis "z" 
     .Zrange "-RLength/2", "RLength/2" 
     .Xcenter "0" 
     .Ycenter "0" 
     .Segments "0" 
     .Create 
End With

'@ define material: Aluminum

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Material
     .Reset
     .Name "Aluminum"
     .Folder ""
     .FrqType "static"
     .Type "Normal"
     .SetMaterialUnit "Hz", "mm"
     .Epsilon "1"
     .Mu "1.0"
     .Kappa "3.56e+007"
     .TanD "0.0"
     .TanDFreq "0.0"
     .TanDGiven "False"
     .TanDModel "ConstTanD"
     .KappaM "0"
     .TanDM "0.0"
     .TanDMFreq "0.0"
     .TanDMGiven "False"
     .TanDMModel "ConstTanD"
     .DispModelEps "None"
     .DispModelMu "None"
     .DispersiveFittingSchemeEps "General 1st"
     .DispersiveFittingSchemeMu "General 1st"
     .UseGeneralDispersionEps "False"
     .UseGeneralDispersionMu "False"
     .FrqType "all"
     .Type "Lossy metal"
     .MaterialUnit "Frequency", "GHz"
     .MaterialUnit "Geometry", "mm"
     .MaterialUnit "Time", "s"
     .MaterialUnit "Temperature", "Kelvin"
     .Mu "1.0"
     .Sigma "3.56e+007"
     .Rho "2700.0"
     .ThermalType "Normal"
     .ThermalConductivity "237.0"
     .SpecificHeat "900", "J/K/kg"
     .MetabolicRate "0"
     .BloodFlow "0"
     .VoxelConvection "0"
     .MechanicsType "Isotropic"
     .YoungsModulus "69"
     .PoissonsRatio "0.33"
     .ThermalExpansionRate "23"
     .ReferenceCoordSystem "Global"
     .CoordSystemType "Cartesian"
     .NLAnisotropy "False"
     .NLAStackingFactor "1"
     .NLADirectionX "1"
     .NLADirectionY "0"
     .NLADirectionZ "0"
     .Colour "1", "1", "0"
     .Wireframe "False"
     .Reflection "False"
     .Allowoutline "True"
     .Transparentoutline "False"
     .Transparency "0"
     .Create
End With

'@ define cylinder: component1:Dipole

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Cylinder 
     .Reset 
     .Name "Dipole" 
     .Component "component1" 
     .Material "Aluminum" 
     .OuterRadius "RodDiameter" 
     .InnerRadius "RodDiameter-6" 
     .Axis "z" 
     .Zrange "-AntenaLength/2", "AntenaLength/2" 
     .Xcenter "DipolePost" 
     .Ycenter "0" 
     .Segments "0" 
     .Create 
End With

'@ change material: component1:Reflector to: Aluminum

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Solid.ChangeMaterial "component1:Reflector", "Aluminum"

'@ define cylinder: component1:Dir1

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Cylinder 
     .Reset 
     .Name "Dir1" 
     .Component "component1" 
     .Material "Aluminum" 
     .OuterRadius "RodDiameter" 
     .InnerRadius "RodDiameter-5" 
     .Axis "z" 
     .Zrange "-DirLength1/2", "DirLength1/2" 
     .Xcenter "DirPost1" 
     .Ycenter "0" 
     .Segments "0" 
     .Create 
End With

'@ define cylinder: component1:Dir2

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Cylinder 
     .Reset 
     .Name "Dir2" 
     .Component "component1" 
     .Material "Aluminum" 
     .OuterRadius "RodDiameter" 
     .InnerRadius "RodDiameter-5" 
     .Axis "z" 
     .Zrange "-DirLength2/2", "DirLength2/2" 
     .Xcenter "DirPost2" 
     .Ycenter "0" 
     .Segments "0" 
     .Create 
End With

'@ define cylinder: component1:solid1

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Cylinder 
     .Reset 
     .Name "solid1" 
     .Component "component1" 
     .Material "Aluminum" 
     .OuterRadius "RodDiameter" 
     .InnerRadius "RodDiameter-5" 
     .Axis "z" 
     .Zrange "-DirLength3/2", "DirLength3/2" 
     .Xcenter "DirPost3" 
     .Ycenter "0" 
     .Segments "0" 
     .Create 
End With

'@ define cylinder: component1:Boom

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Cylinder 
     .Reset 
     .Name "Boom" 
     .Component "component1" 
     .Material "Aluminum" 
     .OuterRadius "BoomDiameter" 
     .InnerRadius "0" 
     .Axis "x" 
     .Xrange "-BoomLength/2", "BoomLength/2" 
     .Ycenter "30" 
     .Zcenter "10" 
     .Segments "0" 
     .Create 
End With

'@ delete shape: component1:Boom

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Solid.Delete "component1:Boom"

'@ define cylinder: component1:Boom

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Cylinder 
     .Reset 
     .Name "Boom" 
     .Component "component1" 
     .Material "Aluminum" 
     .OuterRadius "BoomDiameter" 
     .InnerRadius "0" 
     .Axis "x" 
     .Xrange "-BoomLength/2", "BoomLength/2" 
     .Ycenter "0" 
     .Zcenter "0" 
     .Segments "0" 
     .Create 
End With

'@ delete shape: component1:Boom

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Solid.Delete "component1:Boom"

'@ define cylinder: component1:Boom

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Cylinder 
     .Reset 
     .Name "Boom" 
     .Component "component1" 
     .Material "Aluminum" 
     .OuterRadius "BoomDiameter" 
     .InnerRadius "0" 
     .Axis "x" 
     .Xrange "-BoomLength/2", "BoomLength/2" 
     .Ycenter "0" 
     .Zcenter "0" 
     .Segments "0" 
     .Create 
End With

'@ delete shape: component1:Boom

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Solid.Delete "component1:Boom"

'@ define cylinder: component1:Boom

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Cylinder 
     .Reset 
     .Name "Boom" 
     .Component "component1" 
     .Material "Aluminum" 
     .OuterRadius "BoomDiameter" 
     .InnerRadius "0" 
     .Axis "x" 
     .Xrange "-BoomLength/2", "BoomLength/2" 
     .Ycenter "30" 
     .Zcenter "0" 
     .Segments "0" 
     .Create 
End With

'@ delete shape: component1:Boom

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Solid.Delete "component1:Boom"

'@ define cylinder: component1:solid2

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Cylinder 
     .Reset 
     .Name "solid2" 
     .Component "component1" 
     .Material "Aluminum" 
     .OuterRadius "BoomDiameter" 
     .InnerRadius "0" 
     .Axis "x" 
     .Xrange "-BoomLength/2", "BoomLength" 
     .Ycenter "0" 
     .Zcenter "0" 
     .Segments "0" 
     .Create 
End With

'@ delete shape: component1:solid2

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Solid.Delete "component1:solid2"

'@ define cylinder: component1:Boom

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Cylinder 
     .Reset 
     .Name "Boom" 
     .Component "component1" 
     .Material "Aluminum" 
     .OuterRadius "boomDiameter" 
     .InnerRadius "0" 
     .Axis "x" 
     .Xrange "-BoomLength/2", "BoomLength" 
     .Ycenter "30" 
     .Zcenter "0" 
     .Segments "0" 
     .Create 
End With

'@ define cylinder: component1:Gap

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Cylinder 
     .Reset 
     .Name "Gap" 
     .Component "component1" 
     .Material "Aluminum" 
     .OuterRadius "Gap" 
     .InnerRadius "0" 
     .Axis "z" 
     .Zrange "-Gap/2", "Gap/2" 
     .Xcenter "DipolePost" 
     .Ycenter "0" 
     .Segments "0" 
     .Create 
End With

'@ boolean subtract shapes: component1:Dipole, component1:Gap

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Solid.Subtract "component1:Dipole", "component1:Gap"

'@ define material colour: Aluminum

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Material 
     .Name "Aluminum"
     .Folder ""
     .Colour "0.752941", "0.752941", "0.752941" 
     .Wireframe "False" 
     .Reflection "False" 
     .Allowoutline "True" 
     .Transparentoutline "False" 
     .Transparency "0" 
     .ChangeColour 
End With

'@ pick circle point

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Pick.PickCirclepointFromId "component1:Dipole", "8"

'@ pick circle point

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Pick.PickCirclepointFromId "component1:Dipole", "10"

'@ define discrete port: 1

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With DiscretePort 
     .Reset 
     .PortNumber "1" 
     .Type "SParameter"
     .Label ""
     .Folder ""
     .Impedance "50.0"
     .Voltage "1.0"
     .Current "1.0"
     .Monitor "True"
     .Radius "0.0"
     .SetP1 "True", "176", "0", "-5"
     .SetP2 "True", "176", "0", "5"
     .InvertDirection "False"
     .LocalCoordinates "False"
     .Wire ""
     .Position "end1"
     .Create 
End With

'@ define frequency range

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Solver.FrequencyRange "400", "450"

'@ define time domain solver parameters

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Mesh.SetCreator "High Frequency" 

With Solver 
     .Method "Hexahedral"
     .CalculationType "TD-S"
     .StimulationPort "All"
     .StimulationMode "All"
     .SteadyStateLimit "-40"
     .MeshAdaption "False"
     .AutoNormImpedance "False"
     .NormingImpedance "50"
     .CalculateModesOnly "False"
     .SParaSymmetry "False"
     .StoreTDResultsInCache  "False"
     .RunDiscretizerOnly "False"
     .FullDeembedding "False"
     .SuperimposePLWExcitation "False"
     .UseSensitivityAnalysis "False"
End With

'@ set PBA version

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Discretizer.PBAVersion "2023101624"

