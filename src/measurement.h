#ifndef __MEASUREMENT_H
#define __MEASUREMENT_H
#include "model.h"

void adcSetup();
void performMeasurement(volatile t_InputRegisters *inputRegisters);
void processMeasurements(volatile t_InputRegisters *inputRegisters);
void timer1msStart(volatile uint16_t *ptrToTimeout);
void measurementReset();
#endif