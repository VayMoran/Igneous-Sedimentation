#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "QtCore/QCoreApplication"
#include "iostream"
#include "math.h"
#include <string>
#include "sstream"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

}

void MainWindow::limestone()
{

}
void MainWindow::shale()
{

}
void MainWindow::sandstone()
{

}

MainWindow::~MainWindow()
{

    delete ui;
}

void MainWindow::on_calculate_clicked()
{
    // Create map storing limestone/shale transfer in string
    // and added absoulte values of remainder for sorting
    std::map<double, std::string> sedMap;

    // Calculate button can't be clicked until finished
    ui->calculate->setEnabled(false);

    // Grab oxide input from gui form
    double oxideSilica = ui->oxideSilica->text().toDouble();
    double oxideAluminum = ui->oxideAluminum->text().toDouble();
    double oxideFerrous = ui->oxideFerrous->text().toDouble();
    double oxideFerric = ui->oxideFerric->text().toDouble();
    double oxideMagnesia = ui->oxideMagnesia->text().toDouble();
    double oxideManganese = ui->oxideManganese->text().toDouble();
    double oxideCalcium = ui->oxideCalcium->text().toDouble();
    double oxideSodium = ui->oxideSodium->text().toDouble();
    double oxidePotassium = ui->oxidePotassium->text().toDouble();
    //double oxidePhosphorus = ui->oxidePhosphorus->text().toDouble();

    // Add magnesia and manganese together
    oxideMagnesia = oxideMagnesia + oxideManganese;

    // Grab accuracy of calculation from radio buttons
    double accuracy = 0;
    if (ui->percent1->isChecked())
            accuracy = 1;
    if (ui->percent10->isChecked())
            accuracy = 10;
    if (ui->percentTenth->isChecked())
            accuracy = 0.1;
    if (ui->percentHundreth->isChecked())
            accuracy = 0.01;

    for (double limestoneStep = 0; limestoneStep <= 100; limestoneStep = limestoneStep + accuracy)
    {
        for (double shaleStep =0; shaleStep <=100; shaleStep =shaleStep + accuracy)
        {
            // Calculate Limestone porpotions
            double limestoneOxideCalcium = oxideCalcium * limestoneStep/100;
            double limestoneFactor = limestoneOxideCalcium/43;

            double limestoneOxideSilica = (5.19 * limestoneFactor);
            double limestoneOxideAluminum = (.81 * limestoneFactor);
            double limestoneOxideFerrous = (.54 * limestoneFactor);
            double limestoneOxideFerric = (.54 * limestoneFactor);
            double limestoneOxideMagnesia = (8 * limestoneFactor);
            //double limestoneOxideManganese;
            double limestoneOxideSodium = (.05 * limestoneFactor);
            double limestoneOxidePotassium = (.33 * limestoneFactor);
            //double limestoneOxidePhosphorous;
            double limestoneDioxideCarbon = (41.9 * limestoneFactor);
            double limestoneWater = (.21 * limestoneFactor);

            std::cout << "Limestone Calcium Oxide: "  << limestoneOxideCalcium << std::endl;
            std::cout << "Limestone Silica Oxide: " << limestoneOxideSilica << std::endl;
            std::cout << "Limestone Aluminum Oxide: " << limestoneOxideAluminum << std::endl;
            std::cout << "Limestone Magnesia Oxide: " << limestoneOxideMagnesia << std::endl;
            std::cout << "Limestone Carbon Dioxide: " << limestoneDioxideCarbon << std::endl << std::endl;

            // Calculate remainder after limestone calculations
            double remainderOxideSilica = oxideSilica - limestoneOxideSilica;
            double remainderOxideAluminum = oxideAluminum - limestoneOxideAluminum;
            double remainderOxideFerrous = oxideFerrous - limestoneOxideFerrous;
            double remainderOxideFerric = oxideFerric - limestoneOxideFerric;
            double remainderOxideMagnesia = oxideMagnesia - limestoneOxideMagnesia;
            double remainderOxideCalcium = oxideCalcium - limestoneOxideCalcium;
            double remainderOxideSodium = oxideSodium - limestoneOxideSodium;
            double remainderOxidePotassium = oxidePotassium - limestoneOxidePotassium;
            double remainderDioxideCarbon = 0 - limestoneDioxideCarbon;
            double remainderWater = 0 - limestoneWater;

            // Calculate Shale proportions
            double shaleOxidePotassium = remainderOxidePotassium * shaleStep/100;
            double shaleFactor = shaleOxidePotassium/3.70;

            double shaleOxideSilica = (61.90 * shaleFactor);
            double shaleOxideAluminum = (16.9 * shaleFactor);
            double shaleOxideFerrous = (4.20 * shaleFactor);
            double shaleOxideFerric = (3.00 * shaleFactor);
            double shaleOxideMagnesia = (2.4 * shaleFactor);
            double shaleOxideCalcium = (1.49 * shaleFactor);
            double shaleOxideSodium = (1.07 * shaleFactor);
            double shaleDioxideCarbon = (1.54 * shaleFactor);
            double shaleWater = (3.90 * shaleFactor);

            std::cout << "Shale Silica Oxide: " << shaleOxideSilica << std::endl;
            std::cout << "Shale Aluminum Oxide: " << shaleOxideAluminum << std::endl;
            std::cout << "Shale Ferrous Oxide: " << shaleOxideFerrous << std::endl;
            std::cout << "Shale Ferric Oxide: " << shaleOxideFerric << std::endl;
            std::cout << "Shale Magnesia Oxide: " << shaleOxideMagnesia << std::endl;
            std::cout << "Shale Calcium Oxide: "  << shaleOxideCalcium << std::endl;
            std::cout << "Shale Sodium Oxide: " << shaleOxideSodium << std::endl;
            std::cout << "Shale Potassium Oxide: " << shaleOxidePotassium << std::endl;
            std::cout << "Shale Carbon Dioxide: " << shaleDioxideCarbon << std::endl;
            std::cout << "Shale Water: " << shaleWater << std::endl << std::endl;

            // Calculate remainder after shale calculations
            remainderOxideSilica = remainderOxideSilica - shaleOxideSilica;
            remainderOxideAluminum = remainderOxideAluminum - shaleOxideAluminum;
            remainderOxideFerrous = remainderOxideFerrous - shaleOxideFerrous;
            remainderOxideFerric = remainderOxideFerric - shaleOxideFerric;
            remainderOxideMagnesia = remainderOxideMagnesia - shaleOxideMagnesia;
            remainderOxideCalcium = remainderOxideCalcium - shaleOxideCalcium;
            remainderOxideSodium = remainderOxideSodium - shaleOxideSodium;
            remainderOxidePotassium = remainderOxidePotassium - shaleOxidePotassium;
            remainderDioxideCarbon = remainderDioxideCarbon - shaleDioxideCarbon;
            remainderWater = remainderWater - shaleWater;

            // Calculate sandstone proportions
            double ssOxideSilica = remainderOxideSilica;
            double ssFactor = remainderOxideSilica/78;

            double ssOxidePotassium = (1.3 * ssFactor);
            double ssOxideAluminum = (7.2 * ssFactor);
            double ssOxideFerrous = (1.7 * ssFactor);
            double ssOxideFerric = (1.5 * ssFactor);
            double ssOxideMagnesia = (1.2 * ssFactor);
            double ssOxideCalcium = (3.2 * ssFactor);
            double ssOxideSodium = (1.2 * ssFactor);
            double ssDioxideCarbon = (2.6 * ssFactor);
            double ssWater = (2.2 * ssFactor);

            std::cout << "Sandstone Silica Oxide: " << ssOxideSilica << std::endl;
            std::cout << "Sandstone Aluminum Oxide: " << ssOxideAluminum << std::endl;
            std::cout << "Sandstone Ferrous Oxide: " << ssOxideFerrous << std::endl;
            std::cout << "Sandstone Ferric Oxide: " << ssOxideFerric << std::endl;
            std::cout << "Sandstone Magnesia Oxide: " << ssOxideMagnesia << std::endl;
            std::cout << "Sandstone Calcium Oxide: "  << ssOxideCalcium << std::endl;
            std::cout << "Sandstone Sodium Oxide: " << ssOxideSodium << std::endl;
            std::cout << "Sandstone Potassium Oxide: " << ssOxidePotassium << std::endl;
            std::cout << "Sandstone Carbon Dioxide: " << ssDioxideCarbon << std::endl;
            std::cout << "Sandstone Water: " << ssWater << std::endl << std::endl;

            // Calculate remainder after sandstone calculations
            remainderOxideSilica = remainderOxideSilica - ssOxideSilica;
            remainderOxideAluminum = remainderOxideAluminum - ssOxideAluminum;
            remainderOxideFerrous = remainderOxideFerrous - ssOxideFerrous;
            remainderOxideFerric = remainderOxideFerric - ssOxideFerric;
            remainderOxideMagnesia = remainderOxideMagnesia - ssOxideMagnesia;
            remainderOxideCalcium = remainderOxideCalcium - ssOxideCalcium;
            remainderOxideSodium = remainderOxideSodium - ssOxideSodium;
            remainderOxidePotassium = remainderOxidePotassium - ssOxidePotassium;
            remainderDioxideCarbon = remainderDioxideCarbon - ssDioxideCarbon;
            remainderWater = remainderWater - ssWater;

            double ranking = fabs(remainderOxideSilica) + fabs(remainderOxideAluminum) + fabs(remainderOxideFerrous) + fabs(remainderOxideFerric) + fabs(remainderOxideMagnesia) + fabs(remainderOxideCalcium) + fabs(remainderOxideSodium) + fabs(remainderOxidePotassium) + fabs(remainderDioxideCarbon) + fabs(remainderWater);
            std::cout << "Ranking final: " << ranking << std::endl;

            std::ostringstream stringLimestoneStep;
            std::ostringstream stringShaleStep;
            stringLimestoneStep << limestoneStep;
            stringShaleStep<<shaleStep;

            std::string sedMapKey = "Limestone: " + stringLimestoneStep.str() + "% "+ "Shale: " + stringShaleStep.str() + "% ";
            sedMap[ranking] = sedMapKey;


        }
    }

    for(std::map <double, std::string>::iterator it = sedMap.begin(); it != sedMap.end(); it++)
    {
        std::cout<< it->first << ", " << it->second << std::endl;
    }

    // Calculate button clickable again
    ui->calculate->setEnabled(true);

}
