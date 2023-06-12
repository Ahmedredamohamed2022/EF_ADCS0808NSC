# Open Source, 8-Bit, Rail-to- Rail DAC
## 1. Description
* The EF_DACR0801 contains an 8-bit voltage-mode digital-to-analog converter. It has a rail-to-rail output buffer and is guaranteed monotonic. The device relies on R-string DAC architecture, hence low cost and fast response can be achieved. The DACR0801 includes an enable line that acts as a power-on-reset function. The EF_DACR0801 is compatible with a parallel interface at a clock up to 3.75 MHz. The functional block diagram is presented in Figure 1.

<img src="https://github.com/Ahmedredamohamed2022/EF_DACR0801/blob/main/docs/_static/figure1.functional_block_diagram.png" width="300" height="250">

*Figure 1. Functional Block Diagram*

## 2. Features
* R-String DAC Architecture 
* Low Cost and Fast Response
*	8-Bit DACs with Output Follower Amplifier
*	Dual Power Supply With 1.8 V, 3.3 V
*	8-Bit Parallel Interface
*	DNL: ±0.62 LSB Maximum
*	INL:  ±1.1 LSB Maximum
* Idle-Power Consumption (EN is off):
   - 3.3-V Supply: 10.3µW (Typical)
   - 1.8-V Supply: 58.8 pW (Typical)

## 3. Applications

*	Wearable Systems
*	Data Acquisition Systems
*	Instrumentation and Control Systems

## 4. Pin Configuration and Functions

* Corresponding to the Block Diagram of the EF_DACR0801, each pin name with its function is described in Table 1. 

*Table 1. Pin Configuration and Functions*
<img src="https://github.com/Ahmedredamohamed2022/EF_DACR0801/blob/main/docs/_static/figure2.pin_configuration.png" width="1000" height="300">

## 5. Electrical Characteristics

* The post-layout simulation results of the proposed EF_DACR0801 are listed in Table 2. Those parameters are reported at Temp.=27°C, VDD = 3.3 V, DVDD = 1.8 V, EN=1.8 V, VH=2.5 V , and VL=0 V. Moreover, VOUT is loaded with CL of 2pF and RL of 50KΩ.

*Table 2. Electrical Characteristics*
<img src="https://github.com/Ahmedredamohamed2022/EF_DACR0801/blob/main/docs/_static/figure3.electrical_characteristics.png" width="1000" height="600">

## 6. Timing Characteristics
* As depicted in Figure 2, the timing diagram of the proposed EF_DACR0801 is activated with an active high of EN.

<img src="https://github.com/Ahmedredamohamed2022/EF_DACR0801/blob/main/docs/_static/figure4.timing_digram.png" width="1000" height="400">

*Figure 2. Timing Diagram*

## 7. Typical Performance Curves

* The proposed EF_DACR0801 has been designed and simulated using open-source tools with SkyWater technology. Herein, [XSCHEM](https://xschem.sourceforge.io/stefan/index.html) is a schematic capture program that provides a graphical method of the electronic schematic circuit, easily. [NGSPICE](http://ngspice.sourceforge.net/download.html) is an open-source spice simulator. It is exploied to simulate and verify the designed circuit. Layout of the EF_DACR0801 is implemented using [MAGIC 8.3](http://opencircuitdesign.com/magic/) and for design rule check (DRC) as well. However, [NETGEN](http://opencircuitdesign.com/netgen/) is used for comparing netlists of the layout and schematic, known as layout vs schamtc (LVS). [PYTHON](https://www.python.org/) can be integrated with NGSPICE simulator for data manipulation/analysis of the simulation result.

#### Next, typical perofmane curves of the EF_DACR0801 post-layout simulations are presented. 

* As presented in Figure 3, differential nonlinearity (DNL) and integral nonlinearity (INL) are calculated vs input code at setting VH=2.5V using a [developed script](https://github.com/Ahmedredamohamed2022/EF_DACR0801/tree/main/scripts). Also, DNL and DNL vs applied VH is shown in Figure 4. It indicates that both DNL and DNL are improved for lower VH. In Figure 5, transient simulation results of the EF_DACR0801 are presented for VH=3V and VH=2.5V. EF_DACR0801 full-scale settling time measurement at VH=2.5V and measured settling time vs VH  are presented in Figure 6. Power supply ripple rejection (PSRR) is calculated at different ripple frequencies and Vpp of 0.5V, as shown in Figure 7. In the end, EF_DACR0801's layout is illustrated in Figure 8.

<img src="https://github.com/Ahmedredamohamed2022/EF_DACR0801/blob/main/docs/_static/figure5.dnl_inl.png" width="1000" height="400">

*Figure 3. DNL and INL vs input code at VH=2.5V*

<img src="https://github.com/Ahmedredamohamed2022/EF_DACR0801/blob/main/docs/_static/figure6.inl_dnl_vh.png" width="1000" height="300">

*Figure 4. DNL and INL vs VH*

<img src="https://github.com/Ahmedredamohamed2022/EF_DACR0801/blob/main/docs/_static/figure7.transient_simulation.png" width="1000" height="400">

*Figure 5. Output of EF_DACR0801 Vs time at VH=3 V and VH=2.5V*

<img src="https://github.com/Ahmedredamohamed2022/EF_DACR0801/blob/main/docs/_static/figure8.settlingtime.png" width="1000" height="400">

*Figure 6. DAC Full-Scale Settling Time Measurement at VH=2.5V, settling time vs VH* 

<img src="https://github.com/Ahmedredamohamed2022/EF_DACR0801/blob/main/docs/_static/figure9.psrr.png" width="500" height="300">

*Figure 7. PSRR vs ripple frequency*

<img src="https://github.com/Ahmedredamohamed2022/EF_DACR0801/blob/main/docs/_static/figure10.layout.png" width="500" height="600">

*Figure 8. EF_DACR0801's layout*

## 8. Downloading the files on your System
<p>&nbsp;</p>

* The files from this repository can be downloaded and used by the following commands :-
>`sudo apt install -y git`

>`git clone https://github.com/Ahmedredamohamed2022/EF_DACR0801.git`

<p>&nbsp;</p>
