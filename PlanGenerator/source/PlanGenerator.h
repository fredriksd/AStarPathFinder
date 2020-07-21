#ifndef PATHFINDER_UTIL_PLANGENERATOR_H
#define PATHFINDER_UTIL_PLANGENERATOR_H

#include <string>
#include <fstream>
#include "Qgc_Mission.h"

namespace PathFinder
{
   namespace Util
   {
      class PlanGenerator
      {
      public:
         explicit PlanGenerator(const std::string &filename);
         ~PlanGenerator();
         PlanGenerator(const PlanGenerator &) = delete;
         PlanGenerator(PlanGenerator &&) = delete;
         PlanGenerator &operator=(const PlanGenerator &) = delete;
         PlanGenerator &operator=(PlanGenerator &&) = delete;

         void makeMinimumPlan();
         void addMission(const Qgc::Mission& mission);

      private:
         void verifyExtension(const std::string &filename);
         void close();
         bool isOpen();
         std::ofstream os_;
      };
   } // namespace Util
} // namespace PathFinder

#endif