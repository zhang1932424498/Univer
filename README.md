{\rtf1\ansi\ansicpg936\cocoartf2903
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # IIT Example: Two Dancers Moving Together\
\
This is a simple example of Integrated Information Theory (IIT).\
\
Two dancers have two possible states:\
\
- `0`: standing\
- `1`: jumping\
\
When they move together, only two future states are possible:\
\
| State | Probability |\
|---|---:|\
| 00 | 0.5 |\
| 01 | 0 |\
| 10 | 0 |\
| 11 | 0.5 |\
\
If we cut their connection, they move independently:\
\
| State | Probability |\
|---|---:|\
| 00 | 0.25 |\
| 01 | 0.25 |\
| 10 | 0.25 |\
| 11 | 0.25 |\
\
The integrated information is calculated by KL divergence:\
\
```text\
Phi = D_KL(P_whole || P_cut) = 1 bit}