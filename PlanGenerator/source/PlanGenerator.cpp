#include "PlanGenerator.h"
#include <exception>
#include <sstream>

PathFinder::Util::PlanGenerator::PlanGenerator(const std::string& filename)
{
    verifyExtension(filename);
    if(isOpen())
    {
        throw std::logic_error{"File is already open\n"};
    }
    os_.open(filename);
}


PathFinder::Util::PlanGenerator::~PlanGenerator()
{
    close();
}


void
PathFinder::Util::PlanGenerator::makeMinimumPlan()
{
    os_ << "{"
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
    close();
}


void
PathFinder::Util::PlanGenerator::addMission(const Qgc::Mission& mission)
{
    
}


void
PathFinder::Util::PlanGenerator::verifyExtension(const std::string& filename)
{
    const auto extension = filename.substr(filename.find_last_of(".") + 1);
    if (extension != "json")
    {
        throw std::logic_error{"Wrong file type extension."};
    }
}


void
PathFinder::Util::PlanGenerator::close()
{
    if(isOpen())
    {
        os_.close();
    }
}

bool
PathFinder::Util::PlanGenerator::isOpen()
{
    return os_.is_open();
}