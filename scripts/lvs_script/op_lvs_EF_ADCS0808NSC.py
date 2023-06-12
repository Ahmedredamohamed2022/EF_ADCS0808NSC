#!/usr/bin/env python3
import os
import sys
import subprocess


############################################# sample and hold ###############################################
subprocess.call(["sed -i 's/XD/D/' EF_ADCS0808NSCX.spice","www.txt"], shell=True)
subprocess.call(["sed -i 's/sky130_fd_pr__res_high_po_0p35/sky130_fd_pr__res_high_po W=0.35/' EF_ADCS0808NSCX.spice","www.txt"], shell=True)
subprocess.call(["sed -i 's/sky130_fd_pr__res_xhigh_po_0p35/sky130_fd_pr__res_xhigh_po W=0.35/' EF_ADCS0808NSCX.spice","www.txt"], shell=True)
subprocess.call(["sed -i 's/sky130_fd_pr__diode_pw2nd_05v5 area=1e12 pj=4e6/sky130_fd_pr__diode_pw2nd_05v5/' EF_ADCS0808NSCX.spice","www.txt"], shell=True)
subprocess.call(["sed -i 's/sky130_fd_pr__diode_pw2nd_05v5 area=1 pj=4e6/sky130_fd_pr__diode_pw2nd_05v5/' EF_ADCS0808NSCX.spice","www.txt"], shell=True)

subprocess.call(["sed -i 's/sky130_fd_pr__pnp_05v5_W0p68L0p68 NE=1/sky130_fd_pr__pnp_05v5 W=0.68 L=0.68/' EF_ADCS0808NSCX.spice","www.txt"], shell=True)
subprocess.call(["sed -i 's/sky130_fd_pr__res_xhigh_po_0p69/sky130_fd_pr__res_xhigh_po W=0.69/' EF_ADCS0808NSCX.spice","www.txt"], shell=True)



####################### ADD w ADN l T0 NPN WHICH IS EXTRACTED FROM MAGIC
subprocess.call(["sed -i 's/sky130_fd_pr__pnp_05v5 area=0p/sky130_fd_pr__pnp_05v5 W=0.68 L=0.68 m=1/' EF_ADCS0808NSCM.spice","www.txt"], shell=True)
subprocess.call(["sed -i 's/sky130_fd_pr__res_xhigh_po_0p69/sky130_fd_pr__res_xhigh_po W=0.69/' EF_ADCS0808NSCM.spice","www.txt"], shell=True)

subprocess.call(["sed -i 's/sky130_fd_pr__diode_pw2nd_05v5 pj=1.8e+06 area=2.025e+11/sky130_fd_pr__diode_pw2nd_05v5/' EF_ADCS0808NSCM.spice","www.txt"], shell=True)
subprocess.call(["sed -i 's/sky130_fd_pr__diode_pw2nd_05v5 pj=2.4e+06 area=3.6e+11/sky130_fd_pr__diode_pw2nd_05v5/' EF_ADCS0808NSCM.spice","www.txt"], shell=True)


os.system('netgen -batch lvs "EF_ADCS0808NSCM.spice EF_ADCS0808NSCM" "EF_ADCS0808NSCX.spice EF_ADCS0808NSCX" /home/ahmedreda/PDK/sky130A/libs.tech/netgen/sky130A_setup.tcl')