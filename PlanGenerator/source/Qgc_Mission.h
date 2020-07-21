#ifndef QGC_MISSION_H
#define QGC_MISSION_H

#include <cstdint>
#include <string>
#include <vector>

namespace Qgc
{
   struct Mission
   {
      std::uint8_t CruiseSpeed;
      std::uint8_t firmwareType;
      std::uint8_t hoverSpeed;
   };

   struct Items
   {
      std::uint8_t altitude;
      std::uint8_t altitudeMode;
      bool autoContinue;
      std::uint8_t command;
      std::uint8_t doJumpId;
      std::uint8_t frame;
      std::string type;
   };

   struct Coordinates
   {
      Coordinates() : x_{0}, y_{0}, z_{0}
      {
      }
      explicit Coordinates(const float& x, const float& y, const std::uint16_t& z)
         : x_{x}
         , y_{y}
         , z_{z}
      {
      }
      float x_;
      float y_;
      std::uint16_t z_;
   };
} // namespace Qgc
 
#endif