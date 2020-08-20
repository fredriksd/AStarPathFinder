#include <fstream>
#include <gtest/gtest.h>
#include <gmock/gmock.h>
#include "../source/PlanGenerator.h"

namespace
{
   class PlanGeneratorTest
      : public testing::Test
   {
      public:
         ~PlanGeneratorTest()
         {  
            std::remove(filename);
         }
         std::string readFile(const std::string& filename)
         {
            std::ifstream file{filename, std::ios::in};
            std::stringstream buffer;
            buffer << file.rdbuf();
            return buffer.str();
         }
      protected:
         const char* filename{"ExampleFile.json"};
         PathFinder::Util::PlanGenerator pGenerator{filename};
   };
}


TEST_F(PlanGeneratorTest, CanaryTest)
{
   EXPECT_EQ(1, 1);
}


TEST_F(PlanGeneratorTest, makeMinimumPlan)
{
   pGenerator.makeMinimumPlan();
   const auto expected = "{"
                         "\n   \"fileType\": \"Plan\","
                         "\n   \"geoFence\": {"
                         "\n       \"circles\": ["
                         "\n       ],"
                         "\n       \"polygons\": ["
                         "\n       ],"
                         "\n       \"version\": 1"
                         "\n   },"
                         "\n   \"groundStation\": \"QGroundControl\","
                         "\n   \"mission\": {"
                         "\n   },"
                         "\n   \"rallyPoints\": {"
                         "\n       \"points\": ["
                         "\n       ],"
                         "\n       \"version\": 1"
                         "\n   },"
                         "\n   \"version\": 1"
                         "\n}";
   const auto actual = readFile("ExampleFile.json");
   
   EXPECT_THAT(actual, testing::HasSubstr(expected));
}


TEST_F(PlanGeneratorTest, makeMinimalMission)
{
   const auto expected =  "\"mission\": {"
                              "\n \"cruiseSpeed\": 15,"
                              "\n \"firmwareType\": 12,"
                              "\n \"hoverSpeed\": 5,"
                              "\n \"items\": ["
                              "\n      {"
                              "\n         \"AMSLAltAboveTerrain\": null,"
                              "\n         \"Altitude\": 50,"
                              "\n         \"AltitudeMode\": 0,"
                              "\n         \"autoContinue\": true,"
                              "\n         \"command\": 22,"
                              "\n         \"doJumpId\": 1,"
                              "\n         \"frame\": 3,"
                              "\n         \"params\": ["
                              "\n            15,"
                              "\n            0,"
                              "\n            0,"
                              "\n            null,"
                              "\n            47.3985099,"
                              "\n            8.5451002,"
                              "\n            50"
                              "\n         ],"
                              "\n         \"type\": \"SimpleItem\""
                              "\n      }"
                              "\n],"
                              "\n\"plannedHomePosition\": ["
                              "\n      47.3977419,"
                              "\n      8.545594,"
                              "\n      487.989"
                              "\n],"
                              "\n\"vehicleType\": 2,"
                              "\n\"version\": 2"
                           "\n}";
   pGenerator.addMission(Qgc::Mission{});
   const auto actual = readFile("ExampleFile.json");
   EXPECT_EQ(actual, expected);
}
