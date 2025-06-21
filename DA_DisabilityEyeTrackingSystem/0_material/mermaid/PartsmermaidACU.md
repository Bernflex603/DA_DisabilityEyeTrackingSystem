```mermaid
erDiagram
  
  AssemblyDirectorySystem {}
    AdaptiveControlUnit {}
      AutomatedWiring {}
        Stator {}
          SteelPipe {}
          Wire {}
        Cable {}
      CircuitBoard {}
        CopperSheet {}
        Plastic {}
      HeavyModularFrame {}
        ModularFrame {}
          ReinforcedIronPlate {}
            IronPlate {}
            Screw {}
          IronRod {}
        EncasedIndustrialBeam {}
          SteelBeam {}
          Concrete {}
          Limestone {}
      Computer {}
    SuperComputer {}
      AiLimiter {}
        Quickwire {}
      HighSpeedConnector {}

  AssemblyDirectorySystem }o--|| AdaptiveControlUnit : "2x"
    AdaptiveControlUnit }o--|| AutomatedWiring : "5x"
      AutomatedWiring }o--|| Stator : "1x"
        Stator }o--|| SteelPipe : "3x"
        Stator }o--|| Wire : "8x"
      AutomatedWiring }o--|| Cable : "20x"
        Cable }o--|| Wire : "2x"
    AdaptiveControlUnit }o--|| CircuitBoard : "5x"
      CircuitBoard }o--|| CopperSheet : "2x"
      CircuitBoard }o--|| Plastic : "4x"
    AdaptiveControlUnit }o--|| HeavyModularFrame : "1x"
      HeavyModularFrame }o--|| ModularFrame : "5x"
        ModularFrame }o--|| ReinforcedIronPlate : "3x"
          ReinforcedIronPlate }o--|| IronPlate : "18x"
          ReinforcedIronPlate }o--|| Screw : "50x"
        ModularFrame }o--|| IronRod : "12x"
      HeavyModularFrame }o--|| SteelPipe : "20x"
      HeavyModularFrame }o--|| EncasedIndustrialBeam : "5x"
        EncasedIndustrialBeam }o--|| SteelBeam : "3x"
        EncasedIndustrialBeam }o--|| Concrete : "5x"
          Concrete }o--|| Limestone : "3x"
        Screw }o--|| IronRod : "1x"
        Screw }o--|| SteelBeam : "1x"
    AdaptiveControlUnit }o--|| Computer : "2x"
      Computer }o--|| CircuitBoard : "4x"
      Computer }o--|| Cable : "8x"
      Computer }o--|| Plastic : "16x"
  AssemblyDirectorySystem }o--|| SuperComputer : "1x"
    SuperComputer }o--|| Computer : "4x"
    SuperComputer }o--|| AiLimiter : "2x"
      AiLimiter }o--|| Quickwire : "20x"
      AiLimiter }o--|| CopperSheet : "5x"
    SuperComputer }o--|| HighSpeedConnector : "3x"
      HighSpeedConnector }o--|| Cable : "10x"
      HighSpeedConnector }o--|| Quickwire : "56x"
      HighSpeedConnector }o--|| CircuitBoard : "1x"
    SuperComputer }o--|| Plastic : "28x"