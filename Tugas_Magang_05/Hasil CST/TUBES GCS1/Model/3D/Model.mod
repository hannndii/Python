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

'@ define cylinder: component1:solid2

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Cylinder 
     .Reset 
     .Name "solid2" 
     .Component "component1" 
     .Material "Aluminum" 
     .OuterRadius "RodDiameter" 
     .InnerRadius "0" 
     .Axis "z" 
     .Zrange "-Gap/2", "Gap/2" 
     .Xcenter "DipolePost" 
     .Ycenter "0" 
     .Segments "0" 
     .Create 
End With

'@ boolean subtract shapes: component1:Dipole, component1:solid2

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Solid.Subtract "component1:Dipole", "component1:solid2"

'@ pick circle point

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Pick.PickCirclepointFromId "component1:Dipole", "12"

'@ pick circle point

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Pick.PickCirclepointFromId "component1:Dipole", "11"

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
     .SetP1 "True", "176", "0", "2.5"
     .SetP2 "True", "176", "0", "-2.5"
     .InvertDirection "False"
     .LocalCoordinates "False"
     .Wire ""
     .Position "end1"
     .Create 
End With

'@ define frequency range

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Solver.FrequencyRange "400", "500"

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

'@ define frequency range

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Solver.FrequencyRange "400", "450"

'@ change solver type

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
ChangeSolverType "HF Frequency Domain"

'@ define frequency domain solver parameters

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Mesh.SetCreator "High Frequency" 

With FDSolver
     .Reset 
     .SetMethod "Tetrahedral", "General purpose" 
     .OrderTet "Second" 
     .OrderSrf "First" 
     .Stimulation "All", "1" 
     .ResetExcitationList 
     .AutoNormImpedance "False" 
     .NormingImpedance "50" 
     .ModesOnly "False" 
     .ConsiderPortLossesTet "True" 
     .SetShieldAllPorts "False" 
     .AccuracyHex "1e-6" 
     .AccuracyTet "1e-4" 
     .AccuracySrf "1e-3" 
     .LimitIterations "False" 
     .MaxIterations "0" 
     .SetCalcBlockExcitationsInParallel "True", "True", "" 
     .StoreAllResults "False" 
     .StoreResultsInCache "False" 
     .UseHelmholtzEquation "True" 
     .LowFrequencyStabilization "True" 
     .Type "Auto" 
     .MeshAdaptionHex "False" 
     .MeshAdaptionTet "True" 
     .AcceleratedRestart "True" 
     .FreqDistAdaptMode "Distributed" 
     .NewIterativeSolver "True" 
     .TDCompatibleMaterials "False" 
     .ExtrudeOpenBC "False" 
     .SetOpenBCTypeHex "Default" 
     .SetOpenBCTypeTet "Default" 
     .AddMonitorSamples "True" 
     .CalcPowerLoss "True" 
     .CalcPowerLossPerComponent "False" 
     .SetKeepSolutionCoefficients "MonitorsAndMeshAdaptation" 
     .UseDoublePrecision "False" 
     .UseDoublePrecision_ML "True" 
     .MixedOrderSrf "False" 
     .MixedOrderTet "False" 
     .PreconditionerAccuracyIntEq "0.15" 
     .MLFMMAccuracy "Default" 
     .MinMLFMMBoxSize "0.3" 
     .UseCFIEForCPECIntEq "True" 
     .UseEnhancedCFIE2 "True" 
     .UseFastRCSSweepIntEq "false" 
     .UseSensitivityAnalysis "False" 
     .UseEnhancedNFSImprint "True" 
     .UseFastDirectFFCalc "False" 
     .RemoveAllStopCriteria "Hex"
     .AddStopCriterion "All S-Parameters", "0.01", "2", "Hex", "True"
     .AddStopCriterion "Reflection S-Parameters", "0.01", "2", "Hex", "False"
     .AddStopCriterion "Transmission S-Parameters", "0.01", "2", "Hex", "False"
     .RemoveAllStopCriteria "Tet"
     .AddStopCriterion "All S-Parameters", "0.01", "2", "Tet", "True"
     .AddStopCriterion "Reflection S-Parameters", "0.01", "2", "Tet", "False"
     .AddStopCriterion "Transmission S-Parameters", "0.01", "2", "Tet", "False"
     .AddStopCriterion "All Probes", "0.05", "2", "Tet", "True"
     .RemoveAllStopCriteria "Srf"
     .AddStopCriterion "All S-Parameters", "0.01", "2", "Srf", "True"
     .AddStopCriterion "Reflection S-Parameters", "0.01", "2", "Srf", "False"
     .AddStopCriterion "Transmission S-Parameters", "0.01", "2", "Srf", "False"
     .SweepMinimumSamples "3" 
     .SetNumberOfResultDataSamples "1001" 
     .SetResultDataSamplingMode "Automatic" 
     .SweepWeightEvanescent "1.0" 
     .AccuracyROM "1e-4" 
     .AddSampleInterval "", "", "1", "Automatic", "True" 
     .AddSampleInterval "", "", "", "Automatic", "False" 
     .MPIParallelization "False"
     .UseDistributedComputing "False"
     .NetworkComputingStrategy "RunRemote"
     .NetworkComputingJobCount "3"
     .UseParallelization "True"
     .MaxCPUs "1024"
     .MaximumNumberOfCPUDevices "2"
End With

With IESolver
     .Reset 
     .UseFastFrequencySweep "True" 
     .UseIEGroundPlane "False" 
     .SetRealGroundMaterialName "" 
     .CalcFarFieldInRealGround "False" 
     .RealGroundModelType "Auto" 
     .PreconditionerType "Auto" 
     .ExtendThinWireModelByWireNubs "False" 
     .ExtraPreconditioning "False" 
End With

With IESolver
     .SetFMMFFCalcStopLevel "0" 
     .SetFMMFFCalcNumInterpPoints "6" 
     .UseFMMFarfieldCalc "True" 
     .SetCFIEAlpha "0.500000" 
     .LowFrequencyStabilization "False" 
     .LowFrequencyStabilizationML "True" 
     .Multilayer "False" 
     .SetiMoMACC_I "0.0001" 
     .SetiMoMACC_M "0.0001" 
     .DeembedExternalPorts "True" 
     .SetOpenBC_XY "True" 
     .OldRCSSweepDefintion "False" 
     .SetRCSOptimizationProperties "True", "100", "0.00001" 
     .SetAccuracySetting "Custom" 
     .CalculateSParaforFieldsources "True" 
     .ModeTrackingCMA "True" 
     .NumberOfModesCMA "3" 
     .StartFrequencyCMA "-1.0" 
     .SetAccuracySettingCMA "Default" 
     .FrequencySamplesCMA "0" 
     .SetMemSettingCMA "Auto" 
     .CalculateModalWeightingCoefficientsCMA "True" 
     .DetectThinDielectrics "True" 
End With

'@ change solver type

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
ChangeSolverType "HF Time Domain"

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

'@ delete port: port1

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Port.Delete "1"

'@ pick circle point

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Pick.PickCirclepointFromId "component1:Dipole", "12"

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
     .SetP1 "True", "176", "0", "2"
     .SetP2 "True", "176", "0", "-2"
     .InvertDirection "False"
     .LocalCoordinates "False"
     .Wire ""
     .Position "end1"
     .Create 
End With

'@ clear picks

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Pick.ClearAllPicks

'@ delete port: port1

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Port.Delete "1"

'@ pick circle point

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Pick.PickCirclepointFromId "component1:Dipole", "10"

'@ pick circle point

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Pick.PickCirclepointFromId "component1:Dipole", "12"

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

'@ set mesh properties (Hexahedral)

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Mesh 
     .MeshType "PBA" 
     .SetCreator "High Frequency"
End With 
With MeshSettings 
     .SetMeshType "Hex" 
     .Set "Version", 1%
     'MAX CELL - WAVELENGTH REFINEMENT 
     .Set "StepsPerWaveNear", "10" 
     .Set "StepsPerWaveFar", "10" 
     .Set "WavelengthRefinementSameAsNear", "1" 
     'MAX CELL - GEOMETRY REFINEMENT 
     .Set "StepsPerBoxNear", "20" 
     .Set "StepsPerBoxFar", "1" 
     .Set "MaxStepNear", "0" 
     .Set "MaxStepFar", "0" 
     .Set "ModelBoxDescrNear", "maxedge" 
     .Set "ModelBoxDescrFar", "maxedge" 
     .Set "UseMaxStepAbsolute", "0" 
     .Set "GeometryRefinementSameAsNear", "0" 
     'MIN CELL 
     .Set "UseRatioLimitGeometry", "1" 
     .Set "RatioLimitGeometry", "15" 
     .Set "MinStepGeometryX", "0" 
     .Set "MinStepGeometryY", "0" 
     .Set "MinStepGeometryZ", "0" 
     .Set "UseSameMinStepGeometryXYZ", "1" 
End With 
With MeshSettings 
     .Set "PlaneMergeVersion", "2" 
End With 
With MeshSettings 
     .SetMeshType "Hex" 
     .Set "FaceRefinementType", "NONE" 
     .Set "FaceRefinementRatio", "2" 
     .Set "FaceRefinementStep", "0" 
     .Set "FaceRefinementNSteps", "2" 
     .Set "EllipseRefinementType", "NONE" 
     .Set "EllipseRefinementRatio", "2" 
     .Set "EllipseRefinementStep", "0" 
     .Set "EllipseRefinementNSteps", "2" 
     .Set "FaceRefinementBufferLines", "3" 
     .Set "EdgeRefinementType", "RATIO" 
     .Set "EdgeRefinementRatio", "2" 
     .Set "EdgeRefinementStep", "0" 
     .Set "EdgeRefinementBufferLines", "3" 
     .Set "RefineEdgeMaterialGlobal", "0" 
     .Set "RefineAxialEdgeGlobal", "0" 
     .Set "BufferLinesNear", "3" 
     .Set "UseDielectrics", "1" 
     .Set "EquilibrateOn", "1" 
     .Set "Equilibrate", "1.5" 
     .Set "IgnoreThinPanelMaterial", "0" 
End With 
With MeshSettings 
     .SetMeshType "Hex" 
     .Set "SnapToAxialEdges", "1"
     .Set "SnapToPlanes", "1"
     .Set "SnapToSpheres", "1"
     .Set "SnapToEllipses", "1"
     .Set "SnapToCylinders", "1"
     .Set "SnapToCylinderCenters", "1"
     .Set "SnapToEllipseCenters", "1"
     .Set "SnapToTori", "1"
End With 
With Mesh 
     .ConnectivityCheck "True"
     .UsePecEdgeModel "True" 
     .PointAccEnhancement "0" 
     .TSTVersion "0"
	  .PBAVersion "2023101624" 
     .SetCADProcessingMethod "MultiThread22", "-1" 
     .SetGPUForMatrixCalculationDisabled "False" 
End With

'@ define time domain solver parameters

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Mesh.SetCreator "High Frequency" 

With Solver 
     .Method "Hexahedral"
     .CalculationType "TD-S"
     .StimulationPort "1"
     .StimulationMode "All"
     .SteadyStateLimit "-40"
     .MeshAdaption "False"
     .CalculateModesOnly "False"
     .SParaSymmetry "False"
     .StoreTDResultsInCache  "False"
     .RunDiscretizerOnly "False"
     .FullDeembedding "False"
     .SuperimposePLWExcitation "False"
     .UseSensitivityAnalysis "False"
End With

'@ set mesh properties (Hexahedral)

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Mesh 
     .MeshType "PBA" 
     .SetCreator "High Frequency"
End With 
With MeshSettings 
     .SetMeshType "Hex" 
     .Set "Version", 1%
     'MAX CELL - WAVELENGTH REFINEMENT 
     .Set "StepsPerWaveNear", "5" 
     .Set "StepsPerWaveFar", "5" 
     .Set "WavelengthRefinementSameAsNear", "1" 
     'MAX CELL - GEOMETRY REFINEMENT 
     .Set "StepsPerBoxNear", "20" 
     .Set "StepsPerBoxFar", "1" 
     .Set "MaxStepNear", "0" 
     .Set "MaxStepFar", "0" 
     .Set "ModelBoxDescrNear", "maxedge" 
     .Set "ModelBoxDescrFar", "maxedge" 
     .Set "UseMaxStepAbsolute", "0" 
     .Set "GeometryRefinementSameAsNear", "0" 
     'MIN CELL 
     .Set "UseRatioLimitGeometry", "1" 
     .Set "RatioLimitGeometry", "15" 
     .Set "MinStepGeometryX", "0" 
     .Set "MinStepGeometryY", "0" 
     .Set "MinStepGeometryZ", "0" 
     .Set "UseSameMinStepGeometryXYZ", "1" 
End With 
With MeshSettings 
     .Set "PlaneMergeVersion", "2" 
End With 
With MeshSettings 
     .SetMeshType "Hex" 
     .Set "FaceRefinementType", "NONE" 
     .Set "FaceRefinementRatio", "2" 
     .Set "FaceRefinementStep", "0" 
     .Set "FaceRefinementNSteps", "2" 
     .Set "EllipseRefinementType", "NONE" 
     .Set "EllipseRefinementRatio", "2" 
     .Set "EllipseRefinementStep", "0" 
     .Set "EllipseRefinementNSteps", "2" 
     .Set "FaceRefinementBufferLines", "3" 
     .Set "EdgeRefinementType", "RATIO" 
     .Set "EdgeRefinementRatio", "2" 
     .Set "EdgeRefinementStep", "0" 
     .Set "EdgeRefinementBufferLines", "3" 
     .Set "RefineEdgeMaterialGlobal", "0" 
     .Set "RefineAxialEdgeGlobal", "0" 
     .Set "BufferLinesNear", "3" 
     .Set "UseDielectrics", "1" 
     .Set "EquilibrateOn", "1" 
     .Set "Equilibrate", "1.5" 
     .Set "IgnoreThinPanelMaterial", "0" 
End With 
With MeshSettings 
     .SetMeshType "Hex" 
     .Set "SnapToAxialEdges", "1"
     .Set "SnapToPlanes", "1"
     .Set "SnapToSpheres", "1"
     .Set "SnapToEllipses", "1"
     .Set "SnapToCylinders", "1"
     .Set "SnapToCylinderCenters", "1"
     .Set "SnapToEllipseCenters", "1"
     .Set "SnapToTori", "1"
End With 
With Mesh 
     .ConnectivityCheck "True"
     .UsePecEdgeModel "True" 
     .PointAccEnhancement "0" 
     .TSTVersion "0"
	  .PBAVersion "2023101624" 
     .SetCADProcessingMethod "MultiThread22", "-1" 
     .SetGPUForMatrixCalculationDisabled "False" 
End With

'@ define time domain solver parameters

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Mesh.SetCreator "High Frequency" 

With Solver 
     .Method "Hexahedral"
     .CalculationType "TD-S"
     .StimulationPort "All"
     .StimulationMode "All"
     .SteadyStateLimit "-40"
     .MeshAdaption "True"
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

'@ set mesh properties (Hexahedral)

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Mesh 
     .MeshType "PBA" 
     .SetCreator "High Frequency"
End With 
With MeshSettings 
     .SetMeshType "Hex" 
     .Set "Version", 1%
     'MAX CELL - WAVELENGTH REFINEMENT 
     .Set "StepsPerWaveNear", "15" 
     .Set "StepsPerWaveFar", "15" 
     .Set "WavelengthRefinementSameAsNear", "0" 
     'MAX CELL - GEOMETRY REFINEMENT 
     .Set "StepsPerBoxNear", "20" 
     .Set "StepsPerBoxFar", "20" 
     .Set "MaxStepNear", "0" 
     .Set "MaxStepFar", "0" 
     .Set "ModelBoxDescrNear", "maxedge" 
     .Set "ModelBoxDescrFar", "maxedge" 
     .Set "UseMaxStepAbsolute", "0" 
     .Set "GeometryRefinementSameAsNear", "1" 
     'MIN CELL 
     .Set "UseRatioLimitGeometry", "1" 
     .Set "RatioLimitGeometry", "15" 
     .Set "MinStepGeometryX", "0" 
     .Set "MinStepGeometryY", "0" 
     .Set "MinStepGeometryZ", "0" 
     .Set "UseSameMinStepGeometryXYZ", "1" 
End With 
With MeshSettings 
     .Set "PlaneMergeVersion", "2" 
End With 
With MeshSettings 
     .SetMeshType "Hex" 
     .Set "FaceRefinementType", "NONE" 
     .Set "FaceRefinementRatio", "2" 
     .Set "FaceRefinementStep", "0" 
     .Set "FaceRefinementNSteps", "2" 
     .Set "EllipseRefinementType", "NONE" 
     .Set "EllipseRefinementRatio", "2" 
     .Set "EllipseRefinementStep", "0" 
     .Set "EllipseRefinementNSteps", "2" 
     .Set "FaceRefinementBufferLines", "3" 
     .Set "EdgeRefinementType", "RATIO" 
     .Set "EdgeRefinementRatio", "2" 
     .Set "EdgeRefinementStep", "0" 
     .Set "EdgeRefinementBufferLines", "3" 
     .Set "RefineEdgeMaterialGlobal", "0" 
     .Set "RefineAxialEdgeGlobal", "0" 
     .Set "BufferLinesNear", "3" 
     .Set "UseDielectrics", "1" 
     .Set "EquilibrateOn", "1" 
     .Set "Equilibrate", "1.5" 
     .Set "IgnoreThinPanelMaterial", "0" 
End With 
With MeshSettings 
     .SetMeshType "Hex" 
     .Set "SnapToAxialEdges", "1"
     .Set "SnapToPlanes", "1"
     .Set "SnapToSpheres", "1"
     .Set "SnapToEllipses", "1"
     .Set "SnapToCylinders", "1"
     .Set "SnapToCylinderCenters", "1"
     .Set "SnapToEllipseCenters", "1"
     .Set "SnapToTori", "1"
End With 
With Mesh 
     .ConnectivityCheck "True"
     .UsePecEdgeModel "True" 
     .PointAccEnhancement "0" 
     .TSTVersion "0"
	  .PBAVersion "2023101624" 
     .SetCADProcessingMethod "MultiThread22", "-1" 
     .SetGPUForMatrixCalculationDisabled "False" 
End With

'@ delete shape: component1:Boom

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Solid.Delete "component1:Boom"

'@ delete shape: component1:solid1

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Solid.Delete "component1:solid1"

'@ delete port: port1

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Port.Delete "1"

'@ pick circle point

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Pick.PickCirclepointFromId "component1:Dipole", "12"

'@ pick circle point

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Pick.PickCirclepointFromId "component1:Dipole", "11"

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
     .SetP1 "True", "176", "0", "2.5"
     .SetP2 "True", "176", "0", "-2.5"
     .InvertDirection "False"
     .LocalCoordinates "False"
     .Wire ""
     .Position "end1"
     .Create 
End With

'@ delete port: port1

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Port.Delete "1"

'@ pick circle point

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Pick.PickCirclepointFromId "component1:Dipole", "12"

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
     .SetP1 "True", "176", "0", "1"
     .SetP2 "True", "176", "0", "-1"
     .InvertDirection "False"
     .LocalCoordinates "False"
     .Wire ""
     .Position "end1"
     .Create 
End With

'@ set mesh properties (Hexahedral)

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Mesh 
     .MeshType "PBA" 
     .SetCreator "High Frequency"
End With 
With MeshSettings 
     .SetMeshType "Hex" 
     .Set "Version", 1%
     'MAX CELL - WAVELENGTH REFINEMENT 
     .Set "StepsPerWaveNear", "15" 
     .Set "StepsPerWaveFar", "15" 
     .Set "WavelengthRefinementSameAsNear", "1" 
     'MAX CELL - GEOMETRY REFINEMENT 
     .Set "StepsPerBoxNear", "20" 
     .Set "StepsPerBoxFar", "20" 
     .Set "MaxStepNear", "0" 
     .Set "MaxStepFar", "0" 
     .Set "ModelBoxDescrNear", "maxedge" 
     .Set "ModelBoxDescrFar", "maxedge" 
     .Set "UseMaxStepAbsolute", "0" 
     .Set "GeometryRefinementSameAsNear", "0" 
     'MIN CELL 
     .Set "UseRatioLimitGeometry", "1" 
     .Set "RatioLimitGeometry", "15" 
     .Set "MinStepGeometryX", "0" 
     .Set "MinStepGeometryY", "0" 
     .Set "MinStepGeometryZ", "0" 
     .Set "UseSameMinStepGeometryXYZ", "1" 
End With 
With MeshSettings 
     .Set "PlaneMergeVersion", "2" 
End With 
With MeshSettings 
     .SetMeshType "Hex" 
     .Set "FaceRefinementType", "NONE" 
     .Set "FaceRefinementRatio", "2" 
     .Set "FaceRefinementStep", "0" 
     .Set "FaceRefinementNSteps", "2" 
     .Set "EllipseRefinementType", "NONE" 
     .Set "EllipseRefinementRatio", "2" 
     .Set "EllipseRefinementStep", "0" 
     .Set "EllipseRefinementNSteps", "2" 
     .Set "FaceRefinementBufferLines", "3" 
     .Set "EdgeRefinementType", "RATIO" 
     .Set "EdgeRefinementRatio", "2" 
     .Set "EdgeRefinementStep", "0" 
     .Set "EdgeRefinementBufferLines", "3" 
     .Set "RefineEdgeMaterialGlobal", "0" 
     .Set "RefineAxialEdgeGlobal", "0" 
     .Set "BufferLinesNear", "3" 
     .Set "UseDielectrics", "1" 
     .Set "EquilibrateOn", "1" 
     .Set "Equilibrate", "1.5" 
     .Set "IgnoreThinPanelMaterial", "0" 
End With 
With MeshSettings 
     .SetMeshType "Hex" 
     .Set "SnapToAxialEdges", "1"
     .Set "SnapToPlanes", "1"
     .Set "SnapToSpheres", "1"
     .Set "SnapToEllipses", "1"
     .Set "SnapToCylinders", "1"
     .Set "SnapToCylinderCenters", "1"
     .Set "SnapToEllipseCenters", "1"
     .Set "SnapToTori", "1"
End With 
With Mesh 
     .ConnectivityCheck "True"
     .UsePecEdgeModel "True" 
     .PointAccEnhancement "0" 
     .TSTVersion "0"
	  .PBAVersion "2023101624" 
     .SetCADProcessingMethod "MultiThread22", "-1" 
     .SetGPUForMatrixCalculationDisabled "False" 
End With

'@ delete shape: component1:Dipole

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Solid.Delete "component1:Dipole"

'@ delete shape: component1:Dir1

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Solid.Delete "component1:Dir1"

'@ delete shape: component1:Dir2

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Solid.Delete "component1:Dir2"

'@ delete shape: component1:Reflector

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Solid.Delete "component1:Reflector"

'@ define cylinder: component1:Reflector

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Cylinder 
     .Reset 
     .Name "Reflector" 
     .Component "component1" 
     .Material "Aluminum" 
     .OuterRadius "RodDiameter" 
     .InnerRadius "RodDiameter-6" 
     .Axis "x" 
     .Xrange "0", "0" 
     .Ycenter "0" 
     .Zcenter "0" 
     .Segments "0" 
     .Create 
End With

'@ delete port: port1

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Port.Delete "1"

'@ delete shape: component1:Reflector

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Solid.Delete "component1:Reflector"

'@ define cylinder: component1:Reflector

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Cylinder 
     .Reset 
     .Name "Reflector" 
     .Component "component1" 
     .Material "Aluminum" 
     .OuterRadius "RodDiameter" 
     .InnerRadius "RodDiameter-6" 
     .Axis "x" 
     .Xrange "-RLength/2", "RLength/2" 
     .Ycenter "RPosition" 
     .Zcenter "0" 
     .Segments "0" 
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
     .Axis "x" 
     .Xrange "-AntenaLength/2", "AntenaLength/2" 
     .Ycenter "DipolePost" 
     .Zcenter "0" 
     .Segments "0" 
     .Create 
End With

'@ define cylinder: component1:D1

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Cylinder 
     .Reset 
     .Name "D1" 
     .Component "component1" 
     .Material "Aluminum" 
     .OuterRadius "RodDiameter" 
     .InnerRadius "RodDiameter-6" 
     .Axis "x" 
     .Xrange "-DirLength1/2", "DirLength1/2" 
     .Ycenter "DirPost1" 
     .Zcenter "0" 
     .Segments "0" 
     .Create 
End With

'@ define cylinder: component1:D2

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Cylinder 
     .Reset 
     .Name "D2" 
     .Component "component1" 
     .Material "Aluminum" 
     .OuterRadius "RodDiameter" 
     .InnerRadius "RodDiameter-6" 
     .Axis "x" 
     .Xrange "-DirLength2/2", "DirLength2/2" 
     .Ycenter "DirPost2" 
     .Zcenter "0" 
     .Segments "0" 
     .Create 
End With

'@ define cylinder: component1:D3

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Cylinder 
     .Reset 
     .Name "D3" 
     .Component "component1" 
     .Material "Aluminum" 
     .OuterRadius "RodDiameter" 
     .InnerRadius "RodDiameter-6" 
     .Axis "x" 
     .Xrange "-DirLength3/2", "DirLength3/2" 
     .Ycenter "DirPost3" 
     .Zcenter "0" 
     .Segments "0" 
     .Create 
End With

'@ define cylinder: component1:boom

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With Cylinder 
     .Reset 
     .Name "boom" 
     .Component "component1" 
     .Material "Aluminum" 
     .OuterRadius "20" 
     .InnerRadius "0" 
     .Axis "y" 
     .Yrange "-BoomLength/2", "BoomLength" 
     .Xcenter "0" 
     .Zcenter "30" 
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
     .OuterRadius "RodDiameter" 
     .InnerRadius "0" 
     .Axis "x" 
     .Xrange "-Gap/2", "Gap/2" 
     .Ycenter "DipolePost" 
     .Zcenter "0" 
     .Segments "0" 
     .Create 
End With

'@ boolean subtract shapes: component1:Dipole, component1:Gap

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Solid.Subtract "component1:Dipole", "component1:Gap"

'@ pick circle point

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Pick.PickCirclepointFromId "component1:Dipole", "10"

'@ pick circle point

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Pick.PickCirclepointFromId "component1:Dipole", "8"

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
     .SetP1 "True", "2.5", "166", "-10"
     .SetP2 "True", "-2.5", "166", "-10"
     .InvertDirection "False"
     .LocalCoordinates "False"
     .Wire ""
     .Position "end1"
     .Create 
End With

'@ create group: meshgroup1

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Group.Add "meshgroup1", "mesh"

'@ set local mesh properties for: meshgroup1

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
With MeshSettings
     With .ItemMeshSettings ("group$meshgroup1")
          .SetMeshType "Hex"
          .Set "ConsiderGlobalEdgeRefinement", 1
          .Set "ConsiderGlobalFaceRefinement", 1
          .Set "ConsiderGlobalMaterialRefinement", 1
          .Set "ConsiderGlobalRefinement", 1
          .Set "ConsiderGlobalSnapping", 1
          .Set "EdgeRefinementBufferLines", 3
          .Set "EdgeRefinementRatio", "2"
          .Set "EdgeRefinementStep", "0"
          .Set "EdgeRefinementType", "RATIO"
          .Set "EllipseRefinementNSteps", 2
          .Set "EllipseRefinementRatio", 2
          .Set "EllipseRefinementStep", 0
          .Set "EllipseRefinementType", "NONE"
          .Set "FaceRefinementBufferLines", 3
          .Set "FaceRefinementNSteps", 2
          .Set "FaceRefinementRatio", 2
          .Set "FaceRefinementStep", 0
          .Set "FaceRefinementType", "NONE"
          .Set "SnappingIntervals", 0, 0, 0
          .Set "SnappingPriority", 0
          .Set "SnapToAxialEdges", 1
          .Set "SnapToCylinderCenters", 1
          .Set "SnapToCylinders", 1
          .Set "SnapToEllipseCenters", 1
          .Set "SnapToEllipses", 1
          .Set "SnapToObjectBoundaries", 0
          .Set "SnapToPlanes", 1
          .Set "SnapToSpheres", 1
          .Set "SnapToTori", 1
          .Set "SnapXYZ", "1", "1", "1"
          .Set "UseMaterialRefinement", 1
          .Set "UseSnappingPriority", 0
          .Set "VolumeRefinementExtentNumSteps", 3, 3, 3
          .Set "VolumeRefinementExtentStep", 0, 0, 0
          .Set "VolumeRefinementExtentType", "STEPS_PER_DIM"
          .Set "VolumeRefinementExtentValueUseSameXYZ", 1
          .Set "VolumeRefinementNumSteps", "0", "0", "0"
          .Set "VolumeRefinementRatio", "2", "2", "2"
          .Set "VolumeRefinementScopeType", "ALL"
          .Set "VolumeRefinementStep", "0", "0", "0"
          .Set "VolumeRefinementType", "NONE"
          .Set "VolumeRefinementValueUseSameXYZ", 1
     End With
End With

'@ add items to group: "meshgroup1"

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Group.AddItem "port$port1", "meshgroup1"

'@ delete port: port1

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Port.Delete "1"

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
     .SetP1 "True", "-2.5", "166", "-10"
     .SetP2 "True", "2.5", "166", "-10"
     .InvertDirection "False"
     .LocalCoordinates "False"
     .Wire ""
     .Position "end1"
     .Create 
End With

'@ change solver type

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
ChangeSolverType "HF Frequency Domain"

'@ define frequency domain solver parameters

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Mesh.SetCreator "High Frequency" 

With FDSolver
     .Reset 
     .SetMethod "Tetrahedral", "General purpose" 
     .OrderTet "Second" 
     .OrderSrf "First" 
     .Stimulation "All", "1" 
     .ResetExcitationList 
     .AutoNormImpedance "False" 
     .NormingImpedance "50" 
     .ModesOnly "False" 
     .ConsiderPortLossesTet "True" 
     .SetShieldAllPorts "False" 
     .AccuracyHex "1e-6" 
     .AccuracyTet "1e-4" 
     .AccuracySrf "1e-3" 
     .LimitIterations "False" 
     .MaxIterations "0" 
     .SetCalcBlockExcitationsInParallel "True", "True", "" 
     .StoreAllResults "False" 
     .StoreResultsInCache "False" 
     .UseHelmholtzEquation "True" 
     .LowFrequencyStabilization "True" 
     .Type "Auto" 
     .MeshAdaptionHex "False" 
     .MeshAdaptionTet "True" 
     .AcceleratedRestart "True" 
     .FreqDistAdaptMode "Distributed" 
     .NewIterativeSolver "True" 
     .TDCompatibleMaterials "False" 
     .ExtrudeOpenBC "False" 
     .SetOpenBCTypeHex "Default" 
     .SetOpenBCTypeTet "Default" 
     .AddMonitorSamples "True" 
     .CalcPowerLoss "True" 
     .CalcPowerLossPerComponent "False" 
     .SetKeepSolutionCoefficients "MonitorsAndMeshAdaptation" 
     .UseDoublePrecision "False" 
     .UseDoublePrecision_ML "True" 
     .MixedOrderSrf "False" 
     .MixedOrderTet "False" 
     .PreconditionerAccuracyIntEq "0.15" 
     .MLFMMAccuracy "Default" 
     .MinMLFMMBoxSize "0.3" 
     .UseCFIEForCPECIntEq "True" 
     .UseEnhancedCFIE2 "True" 
     .UseFastRCSSweepIntEq "false" 
     .UseSensitivityAnalysis "False" 
     .UseEnhancedNFSImprint "True" 
     .UseFastDirectFFCalc "False" 
     .RemoveAllStopCriteria "Hex"
     .AddStopCriterion "All S-Parameters", "0.01", "2", "Hex", "True"
     .AddStopCriterion "Reflection S-Parameters", "0.01", "2", "Hex", "False"
     .AddStopCriterion "Transmission S-Parameters", "0.01", "2", "Hex", "False"
     .RemoveAllStopCriteria "Tet"
     .AddStopCriterion "All S-Parameters", "0.01", "2", "Tet", "True"
     .AddStopCriterion "Reflection S-Parameters", "0.01", "2", "Tet", "False"
     .AddStopCriterion "Transmission S-Parameters", "0.01", "2", "Tet", "False"
     .AddStopCriterion "All Probes", "0.05", "2", "Tet", "True"
     .RemoveAllStopCriteria "Srf"
     .AddStopCriterion "All S-Parameters", "0.01", "2", "Srf", "True"
     .AddStopCriterion "Reflection S-Parameters", "0.01", "2", "Srf", "False"
     .AddStopCriterion "Transmission S-Parameters", "0.01", "2", "Srf", "False"
     .SweepMinimumSamples "3" 
     .SetNumberOfResultDataSamples "1001" 
     .SetResultDataSamplingMode "Automatic" 
     .SweepWeightEvanescent "1.0" 
     .AccuracyROM "1e-4" 
     .AddSampleInterval "", "", "1", "Automatic", "True" 
     .AddSampleInterval "", "", "", "Automatic", "False" 
     .MPIParallelization "False"
     .UseDistributedComputing "False"
     .NetworkComputingStrategy "RunRemote"
     .NetworkComputingJobCount "3"
     .UseParallelization "True"
     .MaxCPUs "1024"
     .MaximumNumberOfCPUDevices "2"
End With

With IESolver
     .Reset 
     .UseFastFrequencySweep "True" 
     .UseIEGroundPlane "False" 
     .SetRealGroundMaterialName "" 
     .CalcFarFieldInRealGround "False" 
     .RealGroundModelType "Auto" 
     .PreconditionerType "Auto" 
     .ExtendThinWireModelByWireNubs "False" 
     .ExtraPreconditioning "False" 
End With

With IESolver
     .SetFMMFFCalcStopLevel "0" 
     .SetFMMFFCalcNumInterpPoints "6" 
     .UseFMMFarfieldCalc "True" 
     .SetCFIEAlpha "0.500000" 
     .LowFrequencyStabilization "False" 
     .LowFrequencyStabilizationML "True" 
     .Multilayer "False" 
     .SetiMoMACC_I "0.0001" 
     .SetiMoMACC_M "0.0001" 
     .DeembedExternalPorts "True" 
     .SetOpenBC_XY "True" 
     .OldRCSSweepDefintion "False" 
     .SetRCSOptimizationProperties "True", "100", "0.00001" 
     .SetAccuracySetting "Custom" 
     .CalculateSParaforFieldsources "True" 
     .ModeTrackingCMA "True" 
     .NumberOfModesCMA "3" 
     .StartFrequencyCMA "-1.0" 
     .SetAccuracySettingCMA "Default" 
     .FrequencySamplesCMA "0" 
     .SetMemSettingCMA "Auto" 
     .CalculateModalWeightingCoefficientsCMA "True" 
     .DetectThinDielectrics "True" 
End With

'@ define frequency range

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Solver.FrequencyRange "420", "430"

'@ change solver type

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
ChangeSolverType "HF Time Domain"

'@ define time domain solver parameters

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Mesh.SetCreator "High Frequency" 

With Solver 
     .Method "Hexahedral"
     .CalculationType "TD-S"
     .StimulationPort "All"
     .StimulationMode "All"
     .SteadyStateLimit "-40"
     .MeshAdaption "True"
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

'@ define frequency range

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Solver.FrequencyRange "400", "450"

'@ delete shape: component1:boom

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Solid.Delete "component1:boom"

'@ delete port: port1

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Port.Delete "1"

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
     .SetP1 "True", "-2.5", "166", "-10"
     .SetP2 "True", "2.5", "166", "-10"
     .InvertDirection "False"
     .LocalCoordinates "False"
     .Wire ""
     .Position "end1"
     .Create 
End With

'@ delete port: port1

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Port.Delete "1"

'@ pick circle point

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Pick.PickCirclepointFromId "component1:Dipole", "7"

'@ pick circle point

'[VERSION]2024.1|33.0.1|20231016[/VERSION]
Pick.PickCirclepointFromId "component1:Dipole", "9"

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
     .SetP1 "True", "-5", "166", "-4"
     .SetP2 "True", "5", "166", "-4"
     .InvertDirection "False"
     .LocalCoordinates "False"
     .Wire ""
     .Position "end1"
     .Create 
End With

