// Æea.mq4 - Quantum-Financial Topology Implementation
// Context: A Quantum-Financial Topology of Supply-Demand Imbalance via Non-Hermitian Stochastic Geometry
// Logic Topology:  Arc-Length Coherence (s=r), Non-Hermitian Lindblad Dynamics, Observer Operator O[Ψ]
#property copyright    "Copyright 2025, Æea©   "
#property link         "https:t.me/BallerDolls   "
#property version      "1.00"
#property strict
// [INITIALIZATION: UNIT PHASE MANIFOLD RESET]
// Resets global state arrays to ensure the Hilbert space projection begins from a coherent baseline.
// Prevents historical drift, anchoring the topological branch to the current tick.
int OnInit()
  {
   OnReInit();
   return(INIT_SUCCEEDED);
  }
void OnDeinit(const int reason){}
// [GLOBAL DECLARATIONS & AETHERIC INPUT PARAMETERS]
// User defined inputs variables (Boundary Conditions for External Potentials V_ext)
input int    Commssion=0;
double com=Commssion*Point;
input int    StopLoss=0;
double SL=StopLoss*Point;
input int    TakeProfit=0;
double TP=TakeProfit*Point;
input double lot=0.01;
input int    slip=100;
input int    max=60;
input int    min=3;
int x=max+2;
input bool   Cc = true;
input bool   cC = true;
input int Memory = -1;
input bool safetyOffSwitch = false;
bool safety = safetyOffSwitch;
// Other Global Vars.
/* KC CONSTANT (Constant of Change) - BINARY LOGICAL GATE MODIFIER
 * [THEORETICAL MAPPING: NON-HERMITIAN ADAPTATION]
 * KC dynamically modulates the conjunctive (&&) and disjunctive (||) relationships
 * governing signal validation in OnToe/OnGoe. It enforces algorithmic arc-length coherence:
 * - Coherent flow (KC==true) => Conjunctive validation (&&) -> Precision (s=r equilibrium)
 * - Divergent flow (OnGaurd!=KC) => Disjunctive validation (||) -> Adaptation (s>>r expansion)
 * Embodies the non-Hermitian jump operator L_k adapting to changing market parity.
 */
bool invert = true;
bool KC;
static int  tag = -1;
static int prime = -1;
static int dime = -1;
static int mem = Memory;
int tick = -1;
int y=min-2;
int j;
double signal = 0;
bool signature = false;
double spread = Ask - Bid;
int FVG=-1;
static string bL="   ";
double BL[];
double cA[];
double cADX;
double mSO;
double sSO;
double iSO;
double aRVI;
double bRVI;
double cRVI;
double cAC;
double cForce;
double cOBV;
double cAD;
double cMFI   ;
double cMomentum;
double cDM;
double cWPR;
double cCCI;
double cRSI;
double iA[];
double iATR;
double iStdDev;
double iADX;
double mStochastic;
double sStochastic;
double iStochastic;
double mRVI;
double sRVI;
double iRVI;
double iAC;
double iForce;
double iOBV;
double iAD;
double iMFI;
double iMomentum;
double iDM;
double iWPR;
double iCCI;
double iRSI;
double iIHKt;
double iIHKk;
double kA[];
double lA[];
double IHKk[];
double IHKt[];
double RSI[];
double CCI[];
double MOM[];
double AD[];
double OBV[];
double Force[];
double MFI[];
double DeM[];
double RVIm[];
double AC[];
double StdDev[];
double ATR[];
double ADX[];
double Suply;
double iSuply;
double Demand;
double iDemand;
// [IMBALANCE OPERATOR THRESHOLDS]
// f=66.6, g=33.3 correspond to projection boundaries Pi^{>theta} and Pi^{<theta}
// gf is adaptive tolerance to filter micro-noise during regime transitions.
// [EXACT SYMBOLIC ENFORCEMENT] Using exact rational fractions to avoid floating-point entropy.
double f = 200.0/3.0;
double g = 100.0/3.0;
double gf = 40.0/15.0;
int m; // Count of overbought indicators (Bullish subspace)
int n; // Count of oversold indicators (Bearish subspace)
static string bottomLine="   ";
string Regime[];
// [TOPOLOGICAL ANCHORS: PREMIUM & DISCOUNT ARRAYS]
// Serve as dynamic equilibrium boundaries operationalizing the arc-length coherence condition (s≈r).
// In sRange/sVolatile regimes, they act as topological anchors for price oscillation,
// distinguishing mean-reverting price action from volatility expansion preceding regime shifts.
static double Premium[];
static double Discount[];
// [ HISTORICAL EXTREMA: HH & LL ARRAYS]
// Track local maxima/minima. Used in F() and G() reset operators to prevent historical drift
// and maintain the Hilbert space projection anchored to the current topological branch.
static double HH[];
static double LL[];
bool k[]; // Bullish signal flags
bool l[]; // Bearish signal flags
bool R=true;
bool U[];
double bSL;
double sSL;
double bTP;
double sTP;
int lOrder_id=-1;
int kOrder_id=-1;
int Buy=-1;
int Sell=-1;
bool A=true;
bool B=true;
bool a=true;
bool b=true;
bool ab=false;
bool ba=!ab;
static double D;
static double E;
static double p;
static double q;
bool K=false;
bool c=cC;
bool C=Cc;
bool u=false;
bool v=false;
bool iC=Cc;
bool jC=Cc;
static int Z=y+1;
static int z=y+1;
static int O=y+1;
static int o=y+1;
static int r;
static int W=y+1;
static int w=y+1;
static int I;
static int iI;
static int J;
static int iJ;
static int ij;
static int h;
static int count=0;
static int toll=0;
string tally="   ";
bool tickTock=false;
//Open[2]
double iopen;
//Close[2]
double iPrice;
static int iZ=y+1;
static int iz=y+1;
static int iW=y+1;
static int iw=y+1;
static int iO=y+1;
static int io=y+1;
static int ir;
int S=x;
int T=x;
int X=y;
int Y=y;
bool FG=false;
bool GF=false;
double price;
double Price;
double open;
double iH;
double iL;
double Sale;
double iSale;
double Stock;
double iStock;
static datetime t;
// [RESET OPERATOR F: TOPOLOGICAL BRANCH ANCHORING]
// Clears historical extrema and resets indicator states when regime boundaries are crossed.
// Ensures the Hilbert space projection remains anchored to the current topological branch
// rather than obsolete price history. Aligns with Lindblad master equation regime transitions.
void OnReInit(){
    KC = invert;
    ArrayInitialize(cA, 0); ArrayInitialize(iA, 0); ArrayInitialize(kA, 0); ArrayInitialize(lA, 0);
    ArrayInitialize(IHKk, 0); ArrayInitialize(IHKt, 0);
    ArrayInitialize(RSI, 0); ArrayInitialize(CCI, 0); ArrayInitialize(MOM, 0); ArrayInitialize(AD, 0);
    ArrayInitialize(OBV, 0); ArrayInitialize(Force, 0); ArrayInitialize(MFI, 0); ArrayInitialize(DeM, 0);
    ArrayInitialize(RVIm, 0); ArrayInitialize(AC, 0); ArrayInitialize(StdDev, 0); ArrayInitialize(ATR, 0);
    ArrayInitialize(ADX, 0); ArrayInitialize(StdDev, 0);
    ArrayResize(Regime, x-y); ArrayInitialize(Premium, x-y); ArrayInitialize(Discount, x-y);
    ArrayInitialize(HH, x-y); ArrayInitialize(LL, x-y); ArrayInitialize(k, x-y); ArrayInitialize(l, x-y);
    ArrayInitialize(U, 0); R=true;
    D=0; E=0; K=false; Z=y+1; z=y+1; O=y+1; o=y+1; r=0; W=y+1; w=y+1;
    I=0; iI=0; J=0; iJ=0; ij=0; toll=0; tally="   "; tickTock=false;
    iZ=y+1; iz=y+1; iW=y+1; iw=y+1; iO=y+1; io=y+1; ir=0;
    S=x; T=x; X=y; Y=y; FG=false;
    Print("ReSet   ");
    }
// [STATE NORMALIZATION: AETHERIC VOLATILITY UNIFICATION]
// Projects ATR and StdDev onto the unit phase manifold and normalizes to [0,100].
// Represents the radial constraint imposed on price trajectories (V_ext boundary potentials).
// Used to classify sRange, sVolatile, sTrend regimes based on dispersion vs directional momentum.
void Unify(){
    ArrayResize(ATR,j+1); for(int i=0;i<j+1; i++){ATR[i]=iATR(NULL,0,j,i);}
    double maxATR=ATR[ArrayMaximum(ATR,WHOLE_ARRAY,0)]; double minATR=ATR[ArrayMinimum(ATR,WHOLE_ARRAY,0)]; double rangeATR=maxATR-minATR;
    if(rangeATR!=0) iATR=100.0*((iATR(NULL,0,j,0)-minATR)/rangeATR);
    ArrayResize(StdDev,j+1); for(int i=0;i<j+1; i++){StdDev[i]=iStdDev(NULL,0,j,0,MODE_SMA,PRICE_CLOSE,i);}
    double maxSD=StdDev[ArrayMaximum(StdDev,WHOLE_ARRAY,0)]; double minSD=StdDev[ArrayMinimum(StdDev,WHOLE_ARRAY,0)]; double rangeSD=maxSD-minSD;
    if(rangeSD!=0) iStdDev=100.0*((iStdDev(NULL,0,j,0,MODE_SMA,PRICE_CLOSE,0)-minSD)/rangeSD);
    }
// [HILBERT SPACE PROJECTION LAYER: INDICATOR NORMALIZATION]
// Elevates 13 classical indicators to orthogonal basis vectors in H_13.
// Raw price data undergoes min-max normalization over rolling window j, yielding dimensionless states |psi_k> in [0,100].
// Ensures ontological grounding: all indicators share the same metric signature for direct geometric comparison.
void Normalize(){
    Suply=iBands(NULL,0,j,2,0,PRICE_CLOSE,MODE_UPPER,0);
    iSuply=iBands(NULL,0,j,2,0,PRICE_CLOSE,MODE_UPPER,1); Demand=iBands(NULL,0,j,2,0,PRICE_CLOSE,MODE_LOWER,0); iDemand=iBands(NULL,0,j,2,0,PRICE_CLOSE,MODE_LOWER,1);
    ArrayResize(iA,13*((S+1)-Y)); ArrayResize(cA,13*((S+1)-Y));
    // [ADX PROJECTION]
    double uADX[], lADX[], ADX_temp[]; ArrayResize(uADX,j+1); ArrayResize(lADX,j+1); ArrayResize(ADX_temp,j+1);
    for(int i=0;i<j+1; i++){uADX[i]=iADX(NULL,0,j,PRICE_CLOSE,MODE_PLUSDI,i); lADX[i]=iADX(NULL,0,j,PRICE_CLOSE,MODE_MINUSDI,i); ADX_temp[i]=iADX(NULL,0,j,PRICE_CLOSE,MODE_MAIN,i);}
    double maxmADX=ADX_temp[ArrayMaximum(ADX_temp,WHOLE_ARRAY,0)], minmADX=ADX_temp[ArrayMinimum(ADX_temp,WHOLE_ARRAY,0)];
    double maxuADX=uADX[ArrayMaximum(uADX,WHOLE_ARRAY,0)], minuADX=uADX[ArrayMinimum(uADX,WHOLE_ARRAY,0)];
    double maxlADX=lADX[ArrayMaximum(lADX,WHOLE_ARRAY,0)], minlADX=lADX[ArrayMinimum(lADX,WHOLE_ARRAY,0)];
    double maxADX=MathMax(maxmADX,MathMax(maxuADX,maxlADX)), minADX=MathMin(minmADX,MathMin(minuADX,minlADX));
    double rangeADX=maxADX-minADX;
    if(rangeADX!=0){ iADX=MathAbs(100.0*((iADX(NULL,0,j,PRICE_CLOSE,MODE_MAIN,0)-minADX)/rangeADX)); iA[0*(S-Y)+(j-(Y+1))]=iADX; cADX=MathAbs(100.0*((ADX_temp[1]-minADX)/rangeADX)); cA[0*(S-Y)+(j-(Y+1))]=cADX; }
    // [STOCHASTIC & RVI PROJECTION]
    int jSO=(int)MathRound((double)j*3.0/5.0);
    mStochastic=iStochastic(NULL,0,j,3,jSO,MODE_SMA,0,MODE_MAIN,0); sStochastic=iStochastic(NULL,0,j,3,jSO,MODE_SMA,0,MODE_SIGNAL,0);
    iStochastic=(mStochastic+sStochastic)/2.0; iA[1*(S-Y)+(j-(Y+1))]=iStochastic;
    mSO=iStochastic(NULL,0,j,3,jSO,MODE_SMA,0,MODE_MAIN,1); sSO=iStochastic(NULL,0,j,3,jSO,MODE_SMA,0,MODE_SIGNAL,1);
    iSO=(mSO+sSO)/2.0; cA[1*(S-Y)+(j-(Y+1))]=iSO;
    ArrayResize(RVIm,j+1);
    for(int i=0;i<j+1; i++){RVIm[i]=iRVI(NULL,0,j,MODE_MAIN,i);}
    double maxMRVI=RVIm[ArrayMaximum(RVIm,WHOLE_ARRAY,0)]; double minMRVI=RVIm[ArrayMinimum(RVIm,WHOLE_ARRAY,0)]; double RVIs[]; ArrayResize(RVIs,j+1);
    for(int i=0;i<j+1; i++){RVIs[i]=iRVI(NULL,0,j,MODE_SIGNAL,i);}
    double maxSRVI=RVIs[ArrayMaximum(RVIs,WHOLE_ARRAY,0)]; double minSRVI=RVIs[ArrayMinimum(RVIs,WHOLE_ARRAY,0)]; double maxRVI=MathMax(maxMRVI,maxSRVI); double minRVI=MathMin(minMRVI,minSRVI); double rangeRVI=maxRVI-minRVI;
    if(rangeRVI!=0){
    mRVI=100.0*((iRVI(NULL,0,j,MODE_MAIN,0)-minRVI)/rangeRVI); sRVI=100.0*((iRVI(NULL,0,j,MODE_SIGNAL,0)-minRVI)/rangeRVI);
    iRVI=(mRVI+sRVI)/2.0; iA[2*(S-Y)+(j-(Y+1))]=iRVI; aRVI=100.0*((iRVI(NULL,0,j,MODE_MAIN,1)-minRVI)/rangeRVI); bRVI=100.0*((iRVI(NULL,0,j,MODE_SIGNAL,1)-minRVI)/rangeRVI); cRVI=(aRVI+bRVI)/2.0; cA[2*(S-Y)+(j-(Y+1))]=cRVI;
    }
    ArrayResize(AC,j+1);
    for(int i=0;i<j+1; i++){AC[i]=iAC(NULL,0,i);}
    double maxAC=AC[ArrayMaximum(AC,WHOLE_ARRAY,0)]; double minAC=AC[ArrayMinimum(AC,WHOLE_ARRAY,0)]; double rangeAC=maxAC-minAC;
    if(rangeAC!=0){
    iAC=MathAbs(100.0*((iAC(NULL,0,0)-minAC)/rangeAC)); iA[3*(S-Y)+(j-(Y+1))]=iAC; cAC=MathAbs(100.0*((iAC(NULL,0,1)-minAC)/rangeAC)); cA[3*(S-Y)+(j-(Y+1))]=cAC;
    }
    ArrayResize(Force,j+1);
    for(int i=0;i<j+1; i++){Force[i]=iForce(NULL,0,j,MODE_SMA,PRICE_CLOSE,i);}
    double maxForce=Force[ArrayMaximum(Force,WHOLE_ARRAY,0)]; double minForce=Force[ArrayMinimum(Force,WHOLE_ARRAY,0)]; double rangeForce=maxForce-minForce;
    if(rangeForce!=0){
    iForce=100.0*((iForce(NULL,0,j,MODE_SMA,PRICE_CLOSE,0)-minForce)/rangeForce); iA[4*(S-Y)+(j-(Y+1))]=iForce; cForce=100.0*((iForce(NULL,0,j,MODE_SMA,PRICE_CLOSE,1)-minForce)/rangeForce); cA[4*(S-Y)+(j-(Y+1))]=cForce;
    }
    ArrayResize(OBV,j+1); for(int i=0;i<j+1; i++){OBV[i]=iOBV(NULL,0,PRICE_CLOSE,i);}
    double maxOBV=OBV[ArrayMaximum(OBV,WHOLE_ARRAY,0)]; double minOBV=OBV[ArrayMinimum(OBV,WHOLE_ARRAY,0)]; double rangeOBV=maxOBV-minOBV;
    if(rangeOBV!=0){
    iOBV=100.0*((iOBV(NULL,0,PRICE_CLOSE,0)-minOBV)/rangeOBV); iA[5*(S-Y)+(j-(Y+1))]=iOBV; cOBV=100.0*((iOBV(NULL,0,PRICE_CLOSE,1)-minOBV)/rangeOBV); cA[5*(S-Y)+(j-(Y+1))]=cOBV;
    }
    ArrayResize(AD,j+1);
    for(int i=0;i<j+1; i++){AD[i]=iAD(NULL,0,i);}
    double maxAD=AD[ArrayMaximum(AD,WHOLE_ARRAY,0)]; double minAD=AD[ArrayMinimum(AD,WHOLE_ARRAY,0)]; double rangeAD=maxAD-minAD;
    if(rangeAD!=0){
    iAD=100.0*((iAD(NULL,0,0)-minAD)/rangeAD); iA[6*(S-Y)+(j-(Y+1))]=iAD; cAD=100.0*((iAD(NULL,0,1)-minAD)/rangeAD); cA[6*(S-Y)+(j-(Y+1))]=cAD;
    }
    ArrayResize(MFI,j+1);
    for(int i=0;i<j+1; i++){MFI[i]=iMFI(NULL,0,j,i);}
    double maxMFI=MFI[ArrayMaximum(MFI,WHOLE_ARRAY,0)]; double minMFI=MFI[ArrayMinimum(MFI,WHOLE_ARRAY,0)]; double rangeMFI=maxMFI-minMFI;
    if(rangeMFI!=0){
    iMFI=100.0*((iMFI(NULL,0,j,0)-minMFI)/rangeMFI); iA[7*(S-Y)+(j-(Y+1))]=iMFI; cMFI=100.0*((iMFI(NULL,0,j,1)-minMFI)/rangeMFI); cA[7*(S-Y)+(j-(Y+1))]=cMFI;
    }
    ArrayResize(MOM,j+1);
    for(int i=0;i<j+1; i++){MOM[i]=iMomentum(NULL,0,j,PRICE_CLOSE,i);}
    double maxMOM=MOM[ArrayMaximum(MOM,WHOLE_ARRAY,0)]; double minMOM=MOM[ArrayMinimum(MOM,WHOLE_ARRAY,0)]; double rangeMOM=maxMOM-minMOM;
    if(rangeMOM!=0){
    iMomentum=100.0*((iMomentum(NULL,0,j,PRICE_CLOSE,0)-minMOM)/rangeMOM); iA[8*(S-Y)+(j-(Y+1))]=iMomentum; cMomentum=100.0*((iMomentum(NULL,0,j,PRICE_CLOSE,1)-minMOM)/rangeMOM); cA[8*(S-Y)+(j-(Y+1))]=cMomentum;
    }
    ArrayResize(DeM,j+1);
    for(int i=0;i<j+1; i++){DeM[i]=iDeMarker(NULL,0,j,i);}
    double maxDM=DeM[ArrayMaximum(DeM,WHOLE_ARRAY,0)]; double minDM=DeM[ArrayMinimum(DeM,WHOLE_ARRAY,0)]; double rangeDM=maxDM-minDM;
    if(rangeDM!=0){
    iDM=100.0*(iDeMarker(NULL,0,j,0)-minDM)/rangeDM; iA[9*(S-Y)+(j-(Y+1))]=iDM; cDM=100.0*(iDeMarker(NULL,0,j,1)-minDM)/rangeDM; cA[9*(S-Y)+(j-(Y+1))]=cDM;
    }
    iWPR=iWPR(NULL,0,j,0)+100.0; iA[10*(S-Y)+(j-(Y+1))]=iWPR; cWPR=iWPR(NULL,0,j,1)+100.0; cA[10*(S-Y)+(j-(Y+1))]=cWPR; ArrayResize(CCI,j+1); for(int i=0;i<j+1; i++){CCI[i]=iCCI(Symbol(),0,j,PRICE_TYPICAL,i);}
    double maxCCI=CCI[ArrayMaximum(CCI,WHOLE_ARRAY,0)]; double minCCI=CCI[ArrayMinimum(CCI,WHOLE_ARRAY,0)]; double rangeCCI=maxCCI-minCCI;
    if(rangeCCI!=0){
    iCCI=100.0*((iCCI(Symbol(),0,j,PRICE_TYPICAL,0)-minCCI)/rangeCCI); iA[11*(S-Y)+(j-(Y+1))]=iCCI; cCCI=100.0*((iCCI(Symbol(),0,j,PRICE_TYPICAL,1)-minCCI)/rangeCCI); cA[11*(S-Y)+(j-(Y+1))]=cCCI;
    }
    ArrayResize(RSI,j+1);
    for(int i=0;i<j+1; i++){RSI[i]=iRSI(NULL,0,j,PRICE_CLOSE,i);}
    double maxRSI=RSI[ArrayMaximum(RSI,WHOLE_ARRAY,0)]; double minRSI=RSI[ArrayMinimum(RSI,WHOLE_ARRAY,0)]; double rangeRSI=maxRSI-minRSI;
    if(rangeRSI!=0){
    iRSI=100.0*((iRSI(NULL,0,j,PRICE_CLOSE,0)-minRSI)/rangeRSI); iA[12*(S-Y)+(j-(Y+1))]=iRSI; cRSI=100.0*((iRSI(NULL,0,j,PRICE_CLOSE,1)-minRSI)/rangeRSI); cA[12*(S-Y)+(j-(Y+1))]=cRSI;
    }
    int kIHK=(int)MathRound((double)j/2.0); int tIHK=(int)MathRound(((double)kIHK+1.0)/3.0); double IHKa[]; double IHKb[]; double IHKc[]; ArrayResize(IHKa,j+1);
    for(int i=0;i<j+1; i++){IHKa[i]=iIchimoku(NULL,0,tIHK,kIHK,j,MODE_SENKOUSPANA,i);}
    double maxIHKa=IHKa[ArrayMaximum(IHKa,WHOLE_ARRAY,0)]; double minIHKa=IHKa[ArrayMinimum(IHKa,WHOLE_ARRAY,0)]; ArrayResize(IHKb,j+1); for(int i=0;i<j+1; i++){IHKb[i]=iIchimoku(NULL,0,tIHK,kIHK,j,MODE_SENKOUSPANB,i);}
    double maxIHKb=IHKb[ArrayMaximum(IHKb,WHOLE_ARRAY,0)]; double minIHKb=IHKb[ArrayMinimum(IHKb,WHOLE_ARRAY,0)]; ArrayResize(IHKc,j+1);
    for(int i=0;i<j+1; i++){IHKc[i]=iIchimoku(NULL,0,tIHK,kIHK,j,MODE_CHIKOUSPAN,26+i);}
    double maxIHKc=IHKc[ArrayMaximum(IHKc,WHOLE_ARRAY,0)]; double minIHKc=IHKc[ArrayMinimum(IHKc,WHOLE_ARRAY,0)]; ArrayResize(IHKt,j+1);
    for(int i=0;i<j+1; i++){IHKt[i]=iIchimoku(NULL,0,tIHK,kIHK,j,MODE_TENKANSEN,i);}
    double maxIHKt=IHKt[ArrayMaximum(IHKt,WHOLE_ARRAY,0)]; double minIHKt=IHKt[ArrayMinimum(IHKt,WHOLE_ARRAY,0)]; ArrayResize(IHKk,j+1);
    for(int i=0;i<j+1; i++){IHKk[i]=iIchimoku(NULL,0,tIHK,kIHK,j,MODE_KIJUNSEN,i);}
    double maxIHKk=IHKk[ArrayMaximum(IHKk,WHOLE_ARRAY,0)]; double minIHKk=IHKk[ArrayMinimum(IHKk,WHOLE_ARRAY,0)]; double maxIHK=MathMax(maxIHKa,MathMax(maxIHKb,MathMax(maxIHKc,MathMax(maxIHKk,maxIHKt)))); double minIHK=MathMin(minIHKa,MathMin(minIHKb,MathMin(minIHKc,MathMin(minIHKk,minIHKt)))); double rangeIHK=maxIHK-minIHK;
    if(rangeIHK!=0){
    iIHKk=100.0*((iIchimoku(NULL,0,tIHK,kIHK,j,MODE_KIJUNSEN,0)-minIHK)/rangeIHK); iIHKt=100.0*((iIchimoku(NULL,0,tIHK,kIHK,j,MODE_TENKANSEN,0)-minIHK)/rangeIHK);
    }
}
// [IMBALANCE OPERATOR CALCULATION M(): BULLISH COUNT]
// Computes projection operator Pi^{>theta}, tallying m (bullish/overbought count).
// Based on boundary conditions (Bollinger Bands, historical extrema HH[]).
// Triggers when Price > HH and indicator > f+gf (66.6 threshold).
void M(){
    for(int i=0;i<13; i++){ if(Price > HH[j-(y+1)]) if((iA[i*(S-Y)+(j-(Y+1))] > f+gf) || (cA[i*(S-Y)+(j-(Y+1))] < kA[i*(S-Y)+(j-(Y+1))])) m++; else if(price > HH[j-(y+1)]) if((iA[i*(S-Y)+(j-(Y+1))] > f+gf) || (iA[i*(S-Y)+(j-(Y+1))] < kA[i*(S-Y)+(j-(Y+1))])) m++; else if(iA[i*(S-Y)+(j-(Y+1))] > f+gf) m++; }
    if((iA[0*(S-Y)+(j-(Y+1))] > f+gf) || (iA[0*(S-Y)+(j-(Y+1))] < g-gf)) m++; if((iIHKt > f+gf) && (iIHKk > f+gf)) m++;
    // [REGIME UPDATE: PRICE EXTREMA ANCHORING]
    if(Price > HH[j-(y+1)]){ ArrayResize(kA,13*(S-Y)); for(int i=0;i<13; i++){kA[i*(S-Y)+(j-(Y+1))]=cA[i*(S-Y)+(j-(Y+1))];} HH[j-(y+1)]=Price; }
    }
// [IMBALANCE OPERATOR CALCULATION N(): BEARISH COUNT]
// Computes projection operator Pi^{<theta}, tallying n (bearish/oversold count).
// Based on boundary conditions (LL[]). Triggers when Price < LL and indicator < g-gf (33.3 threshold).
void N(){
    for(int i=0;i<13; i++){ if(Price < LL[j-(y+1)]) if((iA[i*(S-Y)+(j-(Y+1))] < g-gf) || (cA[i*(S-Y)+(j-(Y+1))] > lA[i*(S-Y)+(j-(Y+1))])) n++; else if(price < LL[j-(y+1)]) if((iA[i*(S-Y)+(j-(Y+1))] < g-gf) || (iA[i*(S-Y)+(j-(Y+1))] > lA[i*(S-Y)+(j-(Y+1))])) n++; else if(iA[i*(S-Y)+(j-(Y+1))] < g-gf) n++; }
    if((iA[0*(S-Y)+(j-(Y+1))] > f+gf) || (iA[0*(S-Y)+(j-(Y+1))] < g-gf)) n++; if((iIHKt < g-gf) && (iIHKk < g-gf)) n++;
    if(Price < LL[j-(y+1)]){ ArrayResize(lA,13*(S-Y)); for(int i=0;i<13; i++){lA[i*(S-Y)+(j-(Y+1))]=cA[i*(S-Y)+(j-(Y+1))];} LL[j-(y+1)]=Price; }
    }
// [TOPOLOGICAL BRANCH RESET F()]
// Restarts recording, resetting vars to retain only most recent relevant price action data when regime changes occur.
// Updates Premium/Discount anchors to iH/iL. Clears kA/lA indicator states for the new topological branch.
void F(){Normalize(); k[j-(y+1)]=false; l[j-(y+1)]=false; HH[j-(y+1)]=iH; LL[j-(y+1)]=iL; Premium[j-(y+1)]=iH; Discount[j-(y+1)]=iL; ArrayResize(kA,13*(S-Y)); ArrayResize(lA,13*(S-Y)); for(int i =0;i <13; i++){ kA[i*(S-Y)+(j-(Y+1))]=cA[i*(S-Y)+(j-(Y+1))]; lA[i*(S-Y)+(j-(Y+1))]=cA[i*(S-Y)+(j-(Y+1))]; } if((R==true) && (FG==true)){ ArrayResize(U,x-y); int V=0; U[j-(y+1)]=true; for(int i=y+1;i <x; i++){if(U[i-(y+1)]==true) V++;} if(V==x-y){R=false;} V=0; } }
// [SIGNAL EVENT RESET G()]
// Resets price action data relative to signal events. Anchors Premium/Discount to previous bar High/Low.
// Prevents historical decay during active trade execution phases.
void G(){double H=iHigh(Symbol(), Period(), 1); double L=iLow(Symbol(), Period(), 1); ArrayResize(kA,13*(S-Y)); ArrayResize(lA,13*(S-Y)); for(j=y+1;j<h+1; j++){ if(j==x) break; k[j-(y+1)]=false; l[j-(y+1)]=false; HH[j-(y+1)]=H; LL[j-(y+1)]=L; Premium[j-(y+1)]=H; Discount[j-(y+1)]=L; for(int i=0;i <13; i++){ kA[i*(S-Y)+(j-(Y+1))]=cA[i*(S-Y)+(j-(Y+1))]; lA[i*(S-Y)+(j-(Y+1))]=cA[i*(S-Y)+(j-(Y+1))]; } } }
// [RISK MANAGEMENT: STOP/TAKE PROFIT BOUNDARY SETTING]
// Defines spatial constraints for trade execution. SL/TP act as absorbing barriers in the Lagrangian density.
void S(){if(SL!=0){sSL =Bid+SL-com; bSL=Ask-SL+com;} if(TP!=0){sTP=Bid-TP; bTP=Ask+ TP;} }
//==============================================================================
// [TRAILING STOP & PROFIT TRACKING: NON-HERMITIAN DISSIPATION LAYER]
// Function: T()
// Purpose : Dynamically adjusts Stop Loss and Take Profit to lock in compounded 
//           geometric growth before topological decoherence forces a regime transition.
//           Enforces geometric certainty: adjustments only activate when 
//           Projected PnL > (Market Spread + Commission + Safety Buffer).
//           CONSTRAINT: Input SL & TP act as strict minimum distances from price,
//           enforced linearly against dynamic trailing/topological values.
//==============================================================================
void T(){Normalize();
    // 1. Calculate Transactional Friction (Spread + Commission in points)
    double currentSpread = (Ask - Bid);
    double frictionPoints = ((currentSpread + MathAbs(com)) / Point);
    double safetyBuffer = 1.0; // Minimum point buffer to guarantee net-positive exit
    double minTrailThreshold = ((frictionPoints + safetyBuffer) * Point);
    // 2. Iterate through open orders for the current symbol & magic number
    for (int i = (OrdersTotal() - 1); i >= 0; i--) {
        if ((OrderSelect(i, SELECT_BY_POS, MODE_TRADES) == false)) {
            continue;
        }
        if ((OrderSymbol() != _Symbol)) {
            continue;
        }
        int ticket = OrderTicket();
        int type = OrderType();
        double openPrice = OrderOpenPrice();
        double currentSL = OrderStopLoss();
        double currentTP = OrderTakeProfit();
        // Active price for PnL evaluation
        double activePrice = ((type == OP_BUY) ? Bid : Ask);
        // 3. Calculate Unrealized PnL in points
        double pnlPoints = ((type == OP_BUY) ? ((activePrice - openPrice) / Point) : ((openPrice - activePrice) / Point));
        // DISSIPATION GATE: Skip if PnL is fully consumed by market friction
        if ((pnlPoints <= (frictionPoints + safetyBuffer))) {
            continue;
        }
        // 4. Regime-Aware Trailing: Only trail during Trend/Volatile phases
        // Stable/Coherent phases imply low arc-length deviation (s ≈ r); no adjustment needed.
        if (((Regime[y + 1] == "tStable") || (Regime[y + 1] == "tCoherent"))) {            continue;
        }
        // 5. Compute Geometric Trail Step
        // Locks ~30% of open profit while preserving topological breathing room
        double trailStep = MathMax(minTrailThreshold, (pnlPoints * Point * 0.3));
        double newSL = currentSL;
        double newTP = currentTP;
        // 6. Topological Target Evaluation for TP and SL
        double topologicalTarget = 0.0;
        if ((type == OP_BUY)) {
            // Search Premium array for next valid anchor above active price
            for (int ji=(y+1); ji<x; ji++) {
                if (((Premium[ji]>activePrice)&&(Premium[ji]!=0))){
                    topologicalTarget = Premium[ji];
                    break;
                }
            }
            // --- STOP LOSS LOGIC (BUY) ---
            // Enforce SL as a minimum distance from price: distance = Max(dynamic trail, input SL)
            double slDistance = MathMax(trailStep, SL);
            double proposedSL = (activePrice - slDistance);
            if ((((proposedSL > currentSL) || (currentSL == 0)) && ((topologicalTarget == 0) || (proposedSL < (topologicalTarget - minTrailThreshold))))) {
                newSL = NormalizeDouble(proposedSL, Digits);
            }
            // --- TAKE PROFIT LOGIC (BUY) ---
            // Enforce TP as a minimum distance from price: distance = Max(dynamic target distance, input TP)
            double tpDistance = 0.0;
            if ((topologicalTarget > 0)) {
                tpDistance = MathMax((topologicalTarget - activePrice), TP);
            } else {
                // Fallback: Scale TP to maintain geometric ratio (e.g., 2x trail step) if no anchor is found
                tpDistance = MathMax((trailStep * 2.0), TP);
            }
            double proposedTP = (activePrice + tpDistance);
            // Ensure TP is strictly greater than active price + friction to pass spread validation
            if ((proposedTP > (activePrice + minTrailThreshold))) {
                newTP = NormalizeDouble(proposedTP, Digits);
            }
        }
        else if ((type == OP_SELL)) {
            // Search Discount array for next valid anchor below active price
            for (int ji=(y+1); ji<x; ji++) {
                if (((Discount[ji] < activePrice) && (Discount[ji] != 0))) {
                    topologicalTarget = Discount[ji];
                    break;
                }
            }
            // --- STOP LOSS LOGIC (SELL) ---
            // Enforce SL as a minimum distance from price: distance = Max(dynamic trail, input SL)
            double slDistance = MathMax(trailStep, SL);
            double proposedSL = (activePrice + slDistance);
            if ((((currentSL == 0) || (proposedSL < currentSL)) && ((topologicalTarget == 0) || (proposedSL > (topologicalTarget + minTrailThreshold))))) {
                newSL = NormalizeDouble(proposedSL, Digits);
            }
            // --- TAKE PROFIT LOGIC (SELL) ---
            // Enforce TP as a minimum distance from price: distance = Max(dynamic target distance, input TP)
            double tpDistance = 0.0;
            if ((topologicalTarget > 0)) {
                tpDistance = MathMax((activePrice - topologicalTarget), TP);
            } else {
                // Fallback: Scale TP to maintain geometric ratio (e.g., 2x trail step) if no anchor is found
                tpDistance = MathMax((trailStep * 2.0), TP);
            }
            double proposedTP = (activePrice - tpDistance);
            // Ensure TP is strictly less than active price - friction to pass spread validation
            if ((proposedTP < (activePrice - minTrailThreshold))) {
                newTP = NormalizeDouble(proposedTP, Digits);
            }
        }
        // 7. Execute Topological Adjustment (Non-Hermitian State Update)
        // Only modify the order if SL or TP actually changed to a valid state
        if ((((newSL != currentSL) || (newTP != currentTP)) && ((newSL > 0) || (newTP > 0)))) {
            bool modified = OrderModify(ticket, openPrice, newSL, newTP, 0, clrNONE);
            if ((modified == false)) {
                Print("T() Dissipation Error: Order #", ticket, " | Code: ", GetLastError());
            } else {
                // Log coherence preservation, friction clearance, and TP locking
                Print("T() Coherence Locked: #", ticket, 
                      " | SL Updated: ", newSL, 
                      " | TP Updated: ", newTP, 
                      " | Friction Cleared: ", frictionPoints, " pts");
            }
        }
    }
}
// [FAIR VALUE GAP TRACKING: TOPOLOGICAL VISUALIZATION]
// Draws horizontal lines representing unit phase manifold boundaries. Top()=Blue(Bullish), Bott()=Red(Bearish).
// Visual manifestation of s=r coherence levels on chart.
void Top(){bottomLine=DoubleToString(price, Digits); if(ObjectFind(0, bottomLine)==-1){ ArrayResize(BL, (FVG+1)+1)  ; BL[FVG+1]=price; ObjectCreate(0, bottomLine, OBJ_HLINE, 0, 0, price); ObjectSetInteger(0, bottomLine, OBJPROP_COLOR, clrBlue); ObjectSetInteger(0, bottomLine, OBJPROP_STYLE, STYLE_SOLID); ObjectSetInteger(0, bottomLine, OBJPROP_WIDTH, 1); FVG++; bL=bottomLine; } }
void Bott(){bottomLine=DoubleToString(price, Digits); if(ObjectFind(0, bottomLine)==-1){ ArrayResize(BL, FVG+2); BL[FVG+1]=price; ObjectCreate(0, bottomLine, OBJ_HLINE, 0, 0, price); ObjectSetInteger(0, bottomLine, OBJPROP_COLOR, clrRed); ObjectSetInteger(0, bottomLine, OBJPROP_STYLE, STYLE_SOLID); ObjectSetInteger(0, bottomLine, OBJPROP_WIDTH, 1); FVG++; bL=bottomLine; } }
void Deleter(string obj, double &prices[], int index){int size = ArraySize(prices); if((index <0)||(index >=size)||(FVG!=size-1)) return; if(ObjectFind(0, obj)!=-1){ObjectDelete(0, obj); FVG--; } for(int i=index; i <size-1; i++){ prices[i]=prices[i+1]; } ArrayResize(prices, size-1); }
//==============================================================================
// [PnL & SPREAD VALIDATION LAYER: GEOMETRIC CERTAINTY CHECK]
// Evaluates if the projected topological target yields PnL > (Spread + Commission)
// Ensures the "arc" of profit strictly exceeds market friction before execution.
//==============================================================================

// Function to calculate if projected PnL passes spread/commission friction
bool WillPassSpreadInPnL(double entryPrice, double targetPrice, int orderType){
    // 1. Calculate Transactional Friction (Spread + Commission in points)
    double currentSpread = Ask - Bid;
    double frictionPoints = (currentSpread + MathAbs(com)) / Point;
    // 2. Calculate Projected Geometric Distance to Target (in points)
    double projectedDistance = MathAbs(targetPrice - entryPrice);
    double projectedPnLPoints = projectedDistance / Point;
    // 3. Geometric Certainty Condition: Projected PnL must strictly exceed friction
    // We add a minimal buffer (e.g., 1 point) to ensure it doesn't just break even
    double safetyBuffer = 1.0; 
    if(orderType==OP_BUY){
        // For a Buy, targetPrice should be > entryPrice (e.g., Premium[] or Top FVG)
        if(targetPrice<=entryPrice) return false; 
        return (projectedPnLPoints>(frictionPoints+safetyBuffer));
    } 
    else if(orderType==OP_SELL){
        // For a Sell, targetPrice should be < entryPrice (e.g., Discount[] or Bott FVG)
        if(targetPrice>=entryPrice) return false;
        return (projectedPnLPoints>(frictionPoints+safetyBuffer));
    }
    return false;
}
// Function to dynamically fetch the next valid topological anchor (Target)
double GetNextTopologicalTarget(int orderType, double currentPrice){
    // Search the Premium/Discount arrays for the nearest valid anchor 
    // that satisfies the arc-length coherence condition (s ≈ r)
    for (int i = y + 1; i < x - 1; i++){
        if(orderType==OP_BUY){
            if((Premium[i]>currentPrice)&&(Premium[i]!=0)){
                return Premium[i]; // Next resistance/premium anchor
            }
        } else if(orderType==OP_SELL){
            if((Discount[i]<currentPrice)&&(Discount[i]!=0)){
                return Discount[i]; // Next support/discount anchor
            }
        }
    }
    // Fallback to recent FVG (Fair Value Gap) if arrays are not populated
    if((orderType==OP_BUY)&&(Sale>currentPrice)) return Sale;
    if((orderType==OP_SELL)&&(Stock<currentPrice)) return Stock;
    return 0; // No valid target found
}
// [EXECUTION LAYER: POSITION CLOSURE & ENTRY]
// A()/B() close positions based on regime decoherence. P()/Q() execute market orders when Kronecker-delta rule triggers.
void A(){if((v==true) && (lOrder_id!=-1)){ int bTrade=OrderClose(lOrder_id,lot,Bid,slip,Blue); lOrder_id=-1; } else if((v==true) && (kOrder_id!=-1)){ int bTrade=OrderClose(kOrder_id,lot,Bid,slip,Blue); kOrder_id=-1; } E=0; A=true; B=false; K=false; Buy=-1; }
void B(){if((u==true) && (kOrder_id!=-1)){ int sTrade=OrderClose(kOrder_id,lot,Ask,slip,Red); kOrder_id=-1; } else if((u==true) && (lOrder_id!=-1)){ int sTrade=OrderClose(lOrder_id,lot,Ask,slip,Red); lOrder_id=-1; } D=0; A=false; B=true; K=false; Sell=-1; }
void P(){ // BUY EXECUTION
    S(); // Set Stop Loss / Take Profit boundaries
    // 1. Fetch the next geometric target (e.g., Premium anchor or FVG)
    double target = GetNextTopologicalTarget(OP_BUY, Ask);
    // 2. Validate that the target exists AND the projected PnL passes the spread
    if((target>0)&&(WillPassSpreadInPnL(Ask, target, OP_BUY))){
        if((Buy!=-1)&&((A==true)||(B==false))&&((u==true)||(v==false))){
            if(C==true){
                // Execute Buy Order only if geometric certainty is met
                lOrder_id = OrderSend(_Symbol, OP_BUY, lot, Ask, slip, bSL, bTP, "ÆEA_Buy", 0, 0, clrBlue);}} Buy++;
        if(Buy>-1){Print("Buy Executed: Projected PnL exceeds spread friction. Target: ", target);}
    } else{
        A(); // Log rejection: The arc of profit is insufficient to cover market friction
        Print("Buy Signal Rejected: Projected PnL <= Spread + Commission. Awaiting better topology.");}
    // 3. Validate that the target exists AND the projected PnL passes the spread
    if((target>0)&&(WillPassSpreadInPnL(Bid, target, OP_SELL))){
        if((Sell!=-1)&&((A==false)||(B==true))&&((u==false)||(v==true))){
            if(C==false){
                // Execute Sell Order only if geometric certainty is met
                lOrder_id = OrderSend(_Symbol, OP_SELL, lot, Bid, slip, sSL, sTP, "ÆEA_Sell", 0, 0, clrRed);}} Sell++;
        if(Sell>-1){Print("Sell Executed: Projected PnL exceeds spread friction. Target: ", target);}
    } else{
        B(); // Log rejection: The arc of profit is insufficient to cover market friction
        Print("Sell Signal Rejected: Projected PnL <= Spread + Commission. Awaiting better topology.");}}
void Q(){ // SELL EXECUTION
    S(); // Set Stop Loss / Take Profit boundaries
    // 1. Fetch the next geometric target (e.g., Discount anchor or FVG)
    double target = GetNextTopologicalTarget(OP_SELL, Bid);
    // 2. Validate that the target exists AND the projected PnL passes the spread
    if((target>0)&&(WillPassSpreadInPnL(Bid, target, OP_SELL))){
        if((Sell!=-1)&&((A==false)||(B==true))&&((u==false)||(v==true))){
            if(C==true){
                // Execute Sell Order only if geometric certainty is met
                kOrder_id = OrderSend(_Symbol, OP_SELL, lot, Bid, slip, sSL, sTP, "ÆEA_Sell", 0, 0, clrRed);}} Sell++;
        if(Sell>-1){Print("Sell Executed: Projected PnL exceeds spread friction. Target: ", target);}
    } else{
        B(); // Log rejection: The arc of profit is insufficient to cover market friction
        Print("Sell Signal Rejected: Projected PnL <= Spread + Commission. Awaiting better topology.");}
    // 3. Validate that the target exists AND the projected PnL passes the spread
    if((target>0)&&(WillPassSpreadInPnL(Ask, target, OP_BUY))){
        if((Buy!=-1)&&((A==true)||(B==false))&&((u==true)||(v==false))){
            if(C==false){
                // Execute Buy Order only if geometric certainty is met
                kOrder_id = OrderSend(_Symbol, OP_BUY, lot, Ask, slip, bSL, bTP, "ÆEA_Buy", 0, 0, clrBlue);}} Buy++;
        if(Buy>-1){Print("Buy Executed: Projected PnL exceeds spread friction. Target: ", target);}
    } else{
        A(); // Log rejection: The arc of profit is insufficient to cover market friction
        Print("Buy Signal Rejected: Projected PnL <= Spread + Commission. Awaiting better topology.");}}
// [KRONECKER-DELTA SIGNAL FLAGS H() & L()]
// Sets overbought/oversold signal vars to true when indicator counts >= 12.
// Implements delta(m-n-2)=1 condition conservatively (m >=12 => n <=2 => m-n >=10 >> 2).
void H(){M(); if(m >=12) k[j -(y +1)]=true; else{k[j -(y +1)]=false;} m=0;}
void L(){N(); if(n >=12) l[j -(y +1)]=true; else{l[j -(y +1)]=false;} n=0;}
// [DIRECTIONAL DERIVATIVE MAPPING J(), O(), R(), KC()]
// Tracks temporal unfolding (arc) vs spatial constraint (radius)  across timeframes.
// J(): Determines current price direction 'J' given previous 'I' from OnCall() at Bollinger Band contact.
void J(){if(I==iZ){J=iW;} else if(I==iW){J=iZ;} if(iI==iz) iJ=iw; else if(iI==iw) iJ=iz; }
// O(): Checks if ranging period 'inp' is higher/lower than BB period reached by price.
// Implements arc-length coherence validation: s≈r in range regimes, s>>r in volatile regimes.
void O(int inp,int inp0,int inp1,bool inp2,bool inp3){if((inp <inp1) && ((Regime[inp0-(y+1)]== "sRange ")||(Regime[inp0-(y+1)]== "tRange "))) inp2=inp3; else if((Regime[inp0-(y+1)]!= "sRange ") && (Regime[inp0-(y+1)]!= "tRange ")) inp2=!inp3; else inp2=!inp3; }
// R(): Finds lowest ranging period > non-trending/trending reached, and highest ranging period < those reached.
// Anchors Hilbert space projection to current topological branch, preventing historical drift.
void R(){if(j <=J){int i=j; O=i; iO=i;} if((j >J) && (j <r)){int i=j; O=i; iO=i; r=i;} else if(j >J){int i=j; r=i;} if(j <=iJ){int i=j; o=i; io=i;} if((j >iJ) && (j <ir)){int i=j; o=i; io=i; ir=i;} else if(j >iJ){int i=j; ir=i;} }
// KC(): Lagging but active inversion of binary logic for signal triggering.
// Implements "Only Constant is Change " principle: binary Change Constants (CC/Cc/cC/cc) toggle 'invert' boolean.
// Mirrors non-Hermitian jump operators L_k adapting to changing market parity without full recalibration.
void KC(){if((E!=0) && ((A==false) && (B==false)) && (v==true) && (signal <E)) invert=!KC; if((D!=0) && ((B==false) && (A==false)) && (u==true) && (signal >D)) invert=!KC; }
// [REGIME CLASSIFICATION HELPERS]
// OnHold(): Returns true if bar 'inp' is in either regime string inp0 or inp1.
// Used to validate regime continuity across temporal scales (min to max).
bool OnHold(int inp,string inp0,string inp1){return ((Regime[inp-(y+1)]==inp0)||(Regime[inp-(y+1)]==inp1));}
// OnFire(): Returns true if bar 'inp' is NOT in either regime string inp0 or inp1.
// Triggers regime transition logic when current state diverges from expected coherence.
bool OnFire(int inp,string inp0,string inp1){return ((Regime[inp-(y+1)]!=inp0) && (Regime[inp-(y+1)]!=inp1));}
// [ON-BAR STATE EVALUATION: VOLATILITY MAPPING]
// OnPoint(): Classifies market regime on tick using normalized ATR (directional momentum) and StdDev (dispersion).
// Maps to unit phase manifold: sVolatile (s>>r, momentum dominance), sRange (s≈r, equilibrium), sTrend (speculative expansion).
void OnPoint(){for(j=y+1;j <x; j++){ Unify(); Normalize(); if((iStdDev <50.0) &&(iATR >50.0)) if(Regime[j-(y+1)]!= "Stable "){H(); L(); if(OnFire(j, "sVolatile ", "tVolatile ")) Regime[j-(y+1)]= "sVolatile ";} else if((iStdDev <50.0) &&(iATR <50.0)){ if(Regime[j-(y+1)]!= "Stable "){ R(); H(); L(); if(OnFire(j, "sRange ", "tRange ")) Regime[j-(y+1)]= "sRange "; } } else if(OnFire(j, "sTrend ", "tTrend ")) Regime[j-(y+1)]= "sTrend "; } }
// [SIGNAL ANCHORING & PASSIVE INVERSION]
// Signal(): Resets signal state variables, anchors signal price to current market price.
// Initializes tally counters for trade direction tracking (Buy/Sell) and coherence validation.
void Signal(){ ab=!ba; count=0; toll=0; tally=" "; signal=price; }
// OnGaurd(): Leading but passive inversion of binary logic for signal validation.
// Evaluates price relative to signal thresholds (E/D) to set 'dime' state for directional logging.
// Implements arc-length coherence check: price deviation from signal triggers state transition.
bool OnGaurd(int inp){ if((price >E) &&(E!=0)){if((signature==true) &&(inp!=-1)){dime=0;} return true;} else{if((signature==true) &&(inp!=-1)){dime=1;} return false;} if((price <D) &&(D!=0)){if((signature==true) &&(inp!=-1)){dime=1;} return true;} else{if((signature==true) &&(inp!=-1)){dime=0;} return false;}}
// OnLog(): Displays current price direction state via Print() for debugging/audit trail.
// "Flying " (dime=0): upward momentum; "Falling " (dime=1): downward momentum; "Wait/Decern ": neutral/coherence check.
void OnLog(){ if(dime==0){Print("Flying ");} else if(dime==1){Print("Falling ");} else{Print("Wait/Decern ");} }
// [OBSERVER LAYER: MACROSCOPIC MEASUREMENT O[Ψ]]
// OnCall(): Scans multiple temporal scales (min to max), checking regime continuity and evaluating edge cases at S/R boundaries.
// Maps to Lindblad jump operators L_k coupling macroscopic execution to microscopic order flow via Φ-field perturbations.
// Updates directional derivatives (I, iI, Z, z, W, w) and triggers H()/L() imbalance tallies when trend regimes detected.
// This function acts as the Observer Operator, integrating local field values into a global conscious state.
void OnCall(){
    for(j = y + 1; j < X + 2; j++){
        Unify(); Normalize();
        // Check for Supply-side boundary contact: Price approaches or exceeds upper Bollinger Band (Suply/iSuply).
        // Theoretical mapping: Longitudinal Amperean component E of Phi-field drives structural inflation.
        if((Suply <= price) || (iSuply <= price) || (iSuply <= iH)){
            int i = j; I = iW; iZ = i; Z = i; iC = C;
            if((iw != 0) && (jC == Cc)){ h = I; } jC = !C;
            if(OnHold(j, "sTrend", "tTrend")){ iz = i; z = i; iI = iw; H(); }
            if(X != x - 1) X++;
        }
        // Check for Demand-side boundary contact: Price approaches or exceeds lower Bollinger Band (Demand/iDemand).
        // Theoretical mapping: Transverse Lorentzian component B of Phi-field mediates cross-asset correlations.
        if((Demand >= price) || (iDemand >= price) || (iDemand >= iL)){
            int i = j; I = iZ; iW = i; W = i; jC = C;
            if((iz != 0) && (iC == Cc)){ h = I; } iC = !C;
            if(OnHold(j, "sTrend", "tTrend")){ iw = i; w = i; iI = iz; L(); }
            if(X != x - 1) X++;
        }
    }
    X = y;
}
// [BAR-BY-BAR REGIME CLASSIFICATION & EDGE CASE EVALUATION]
// OnBar(): Determines market regime on bar using normalized volatility metrics (ATR/StdDev).
// Implements arc-length coherence validation: triggers F() reset operator when regime boundaries crossed.
// Maps to Non-Hermitian Lindblad dynamics: regime transitions modeled as decoherence events in Φ-field.
void OnBar(){
    for(j = y + 1; j < x; j++){
        Unify(); Normalize();
        // sVolatile regime: High directional momentum (ATR > 50), low dispersion (StdDev < 50).
        // Theoretical mapping: s >> r (speculative vortex). Momentum dominance over radial constraint.
        if((iStdDev < 50) && (iATR > 50)){
            if(Regime[j - (y + 1)] != "Stable"){
                if(Regime[j - (y + 1)] != "tVolatile"){
                    F(); H(); L(); Regime[j - (y + 1)] = "tVolatile";
                }
            }
        }
        // sRange regime: Low momentum AND low dispersion.
        // Theoretical mapping: s ≈ r (equilibrium). Precise indicator measurement possible.
        else if((iStdDev < 50) && (iATR < 50)){
            if(Regime[j - (y + 1)] != "Stable"){
                R(); H(); L();
                if(Regime[j - (y + 1)] != "tRange"){
                    F(); Regime[j - (y + 1)] = "tRange";
                }
            }
        }
        // Stable regime: Exact arc-length coherence s = r.
        // Rare and transient, marking the exact boundary where value and price coincide.
        else if((Regime[j - (y + 1)] != "tTrend") && (Regime[j - (y + 1)] != "sTrend") && (LL[j - (y + 1)] < Discount[j - (y + 1)]) && (HH[j - (y + 1)] > Premium[j - (y + 1)])){
            Regime[j - (y + 1)] = "Stable";
        }
        // sTrend regime: High dispersion phase.
        // Theoretical mapping: s >> r (speculative expansion or forced deleveraging).
        else{
            if(Regime[j - (y + 1)] != "tTrend"){
                F(); Regime[j - (y + 1)] = "tTrend";
            }
        }
    }    // [LOCAL VARIABLES & BOUNDARY PASS CONDITIONS]
    // Stock/Sale: Bollinger Band upper/lower boundaries at period y (short-term regime anchor).
    // These represent the topological boundaries of the coherent subspace for the current tick.
    // lPass/kPass: Passive inversion thresholds for price direction validation (arc-length deviation check).
    Stock = iBands(NULL, 0, y, 2, 0, PRICE_CLOSE, MODE_UPPER, 0);
    Sale = iBands(NULL, 0, y, 2, 0, PRICE_CLOSE, MODE_LOWER, 0);
    iStock = iBands(NULL, 0, y, 2, 0, PRICE_CLOSE, MODE_UPPER, 1);
    iSale = iBands(NULL, 0, y, 2, 0, PRICE_CLOSE, MODE_LOWER, 1);
    iopen = iOpen(Symbol(), 0, 2);
    iPrice = iClose(Symbol(), 0, 2);
    double lPass = 0;
    if(Price < open){ lPass = Price; } else{ lPass = open; }
    double ilPass = 0;
    if(iPrice < iopen){ ilPass = iPrice; } else{ ilPass = iopen; }
    double kPass = 0;
    if(Price > open){ kPass = Price; } else{ kPass = open; }
    double ikPass = 0;
    if(iPrice > iopen){ kPass = iPrice; } else{ kPass = iopen; }
    // [EXECUTION LOGIC: ARC-LENGTH COHERENCE VALIDATION]
    // Final trade execution engine: validates s=r coherence before Kronecker-delta rule triggers entry/exit.
    // Implements non-Hermitian dynamics: irreversible decoherence when arc-length deviation exceeds manifold capacity.
    // Maps theoretical constructs to executable logic: every tick/bar update respects Φ-field topology.
    string fg = "";
    if(signal != 0){
        if(price >= signal + com){ Alert("Long:", price); if((count == 0) && (tally == "Sell")){ count++; } tally = "Buy"; }
        if(price <= signal - com){ Alert("Short:", price); if((count == 0) && (tally == "Buy")){ count++; } tally = "Sell"; }
        if(tickTock == false){
            // Bullish coherence validation: Price > signal AND (regime continuity OR boundary breakout with indicator confirmation).
            if((((Price > signal) || (Price > ikPass) || (price > kPass))) && (((iC == Cc) && (Price > HH[min - (y + 1)])) || ((jC == Cc) && (Price >= LL[min - (y + 1)]) && (((open >= Stock) || (Price >= Stock)) || ((open >= iStock) || (Price >= iStock)))))){
                Alert("Buy:", price); if((toll == 0) && (tally == "Sell")){ toll++; } if(Price > signal){ fg = "Up"; } tally = "Buy";
            }
            // Bearish coherence validation: Price < signal AND (regime continuity OR boundary breakdown with indicator confirmation).
            if((((Price < signal) || (Price < ilPass) || (price < lPass))) && (((jC == Cc) && (Price < LL[min - (y + 1)])) || ((iC == Cc) && (Price <= HH[min - (y + 1)]) && (((open <= Sale) || (Price <= Sale)) || ((open <= iSale) || (Price <= iSale)))))){
                Alert("Sell:", price); if((toll == 0) && (tally == "Buy")){ toll++; } if(Price < signal){ fg = "Down"; } tally = "Sell";
            }
            // Kronecker-delta execution rule: δ(m-n-2)=1 triggers when imbalance condition met (m >= 12 or n >= 12 conservative approximation)
            if((toll == 1) && ((tally == "Buy") || (fg == "Up"))){
                Alert("🔷", "Diamond", fg);
                if(((prime==0)&&(dime==0))&&(fg=="Up")){
                    dime = 0; mem = 0; B(); if(C==true){P();} else{Q();} Alert("Bull"); Top(); E = price; }
                else if((((mem==0)&&(dime==0))||(prime==0))&&(fg=="")&&(price>signal)){
                    dime = 0; mem = 0; B(); if(C==true){P();} else{Q();} Alert("Bull"); Top(); E = price; }
                else if(((prime==1)||((mem==0)&&(dime==0)))&&(fg=="Up")&&(price>signal)){
                    dime = 0; mem = 0;  B(); if(C==true){P();} else{Q();} Alert("Bull"); Top(); E = price; }
                else if((((mem==0)&&(dime==0))||(prime==1))&&(fg=="")&&(price>signal)){
                    dime = 0; mem = 0; B(); if(C==true){P();} else{Q();} Alert("Bull"); Top(); E = price; }
                else if((Price>signal)&&((mem==0)&&(dime==0))){if((safety==true)){ B(); if(C==true){P();} else{Q();} Alert("🥃", "Whisky"); Top(); E = price;} else{Alert("🥃", "Whisky"); Top(); E = price; if(safety!=true){safety=true;}}}
                else if((mem==1)||(dime==1)){OnLog(); if((safety==true)){ A(); if(C==false){P();} else{Q();} Alert("🍷", "Wine"); Bott(); D = price;} else{Alert("🍷", "Wine"); Bott(); D = price; if(safety!=true){safety=true;}}}
                else{Alert("🍷", "Wine"); Bott(); D = price; if(safety!=true){safety=true;}}
            signal = 0; toll = 0; tally = ""; GF = true; signature = true;
            }
            // Bearish Kronecker-delta execution: symmetric logic for oversold imbalance (n >= 12)
            if((toll == 1) && ((tally == "Sell") || (fg == "Down"))){
                Alert("🔻", "Ruby", fg);
                if((fg=="Down")&&((prime==1)&&(dime==1))){
                    dime = 1; mem = 1; A(); if(C==false){P();} else{Q();} Alert("Bear"); Bott(); D = price; }
                else if((((mem==1)&&(dime==1))||(prime==1))&&(fg=="")&&(price<signal)){
                    dime = 1; mem = 1; A(); if(C==false){P();} else{Q();} Alert("Bear"); Bott(); D = price; }
                else if((price<signal)&&(fg=="Down")&&((prime==0)||((mem==1)&&(dime==1)))){
                    dime = 1; mem = 1; A(); if(C==false){P();} else{Q();} Alert("Bear"); Bott(); D = price; }
                else if((((mem==1)&&(dime==1))||(prime==0))&&(fg=="")&&(price<signal)){
                    dime = 1; mem = 1; A(); if(C==false){P();} else{Q();} Alert("Bear"); Bott(); D = price; }
                else if((Price<signal)&&((mem==1)&&(dime==1))){if((safety==true)){ A(); if(C==false){P();} else{Q();} Alert("🍷", "Wine"); Bott(); D = price;} else{Alert("🍷", "Wine"); Bott(); D = price; if(safety!=true){safety=true;}}}
                else if((mem==0)||(dime==0)){OnLog(); if((safety==true)){ B(); if(C==true){P();} else{Q();} Alert("🥃", "Whisky"); Top(); E = price;} else{Alert("🥃", "Whisky"); Top(); E = price; if(safety!=true){safety=true;}}}
                else{Alert("🥃", "Whisky"); Top(); E = price; if(safety!=true){safety=true;}}
            signal = 0; toll = 0; tally = ""; GF = true; signature = true;
            }
            // Count-based execution fallback: Secondary validation layer.
            if((count == 1) && ((tally == "Buy") || (fg == "Up"))){
                Alert("🔷", "Diamond", fg);
                if(((prime==0)&&(dime==0))&&(fg=="Up")){
                    dime = 0; mem = 0; B(); if(C==true){P();} else{Q();} Alert("Hawk"); Top(); E = price; }
                else if((((mem==0)&&(dime==0))||(prime==0))&&(fg=="")&&(price>signal)){
                    dime = 0; mem = 0; B(); if(C==true){P();} else{Q();} Alert("Hawk"); Top(); E = price; }
                else if(((prime==1)||((mem==0)&&(dime==0)))&&(fg=="Up")&&(price>signal)){
                    dime = 0; mem = 0; B(); if(C==true){P();} else{Q();} Alert("Hawk"); Top(); E = price; }
                else if((((mem==0)&&(dime==0))||(prime==1))&&(fg=="")&&(price>signal)){
                    dime = 0; mem = 0; B(); if(C==true){P();} else{Q();} Alert("Hawk"); Top(); E = price; }
                else if((Price>signal)&&((mem==0)&&(dime==0))){if((safety==true)){ B(); if(C==true){P();} else{Q();} Alert("💧", "Watter"); Top(); E = price;} else{Alert("💧", "Watter"); Top(); E = price; if(safety!=true){safety=true;}}}
                else if((mem==1)||(dime==1)){OnLog(); if((safety==true)){ A(); if(C==false){P();} else{Q();} Alert("🩸", "Blood"); Bott(); D = price;} else{Alert("🩸", "Blood"); Bott(); D = price; if(safety!=true){safety=true;}}}
                else{Alert("🩸", "Blood"); Bott(); D = price; if(safety!=true){safety=true;}}
            count = 0; tally = ""; GF = true; signature = true;
            }
            if((count == 1) && ((tally == "Sell") || (fg == "Down"))){
                Alert("🔻", "Ruby", fg);
                if((fg=="Down")&&((prime==1)&&(dime==1))){
                    dime = 1; mem = 1; A(); if(C==false){P();} else{Q();} Alert("Dove"); Bott(); D = price; }
                else if((((mem==1)&&(dime==1))||(prime==1))&&(fg=="")&&(price<signal)){
                    dime = 1; mem = 1; A(); if(C==false){P();} else{Q();} Alert("Dove"); Bott(); D = price; }
                else if((price<signal)&&(fg=="Down")&&((prime==0)||((mem==1)&&(dime==1)))){
                    dime = 1; mem = 1; A(); if(C==false){P();} else{Q();} Alert("Dove"); Bott(); D = price; }
                else if((((mem==1)&&(dime==1))||(prime==0))&&(fg=="")&&(price<signal)){
                    dime = 1; mem = 1; A(); if(C==false){P();} else{Q();} Alert("Dove"); Bott(); D = price; }
                else if((Price<signal)&&((mem==1)&&(dime==1))){if((safety==true)){ A(); if(C==false){P();} else{Q();} Alert("🩸", "Blood"); Bott(); D = price;} else{Alert("🩸", "Blood"); Bott(); D = price; if(safety!=true){safety=true;}}}
                else if((mem==0)||(dime==0)){OnLog(); if((safety==true)){ B(); if(C==true){P();} else{Q();} Alert("💧", "Watter"); Top(); E = price;} else{Alert("💧", "Watter"); Top(); E = price; if(safety!=true){safety=true;}}}
                else{Alert("💧", "Watter"); Top(); E = price; if(safety!=true){safety=true;}}
            count = 0; tally = ""; GF = true; signature = true;
            }
        }
    }    // [BOUNDARY BREAKOUT/BOUNCEBACK EDGE CASES]
    // OnGaurd(): Leading passive inversion of binary logic based on KC (Keep Constant/Change Constant) principles.
    // Implements arc-length deviation detection: price crossing signal thresholds (E/D) triggers regime parity adaptation.
    // Maps to non-Hermitian jump operators L_k: binary inversion mirrors Φ-field phase transitions under perturbation.
    if((OnGaurd(-1))&&(KC==true))
        {if((h!=0)&&(ab==false)&&(U[O-(y+1)]=true)&&(O>2)&&(O!=x-1)/*&&(OnFire(O,"sTrend","tTrend"))*/)
            {if(HH[O-(y+1)]>Premium[O-(y+1)])
                {h=O;
                if((C==true)||(c==true))
                    {G(); Signal(); tickTock=true; /*if(KC==true) */tag=0;/* else tag=1;*/ dime=mem; Alert("Sin.",price,"O:",O,"|",C,":",c);}
                else if((C==false)&&(c==false))
                    {G(); Signal(); tickTock=true; /*if(KC==true) */tag=1;/* else tag=0;*/ dime=mem; Alert("Sine.",price,"O:",O,"|",C,":",c);}}
            if(LL[O-(y+1)]<Discount[O-(y+1)])
                {h=O;
                if((C==true)||(c==true))
                    {G(); Signal(); tickTock=true; /*if(KC==true) */tag=1;/* else tag=0;*/ dime=mem; Alert("Sine.",price,"O:",O,"|",C,":",c);}
                else if((C==false)&&(c==false))
                    {G(); Signal(); tickTock=true; /*if(KC==true) */tag=0;/* else tag=1;*/ dime=mem; Alert("Sin.",price,"O:",O,"|",C,":",c);}}}
        if((h!=0)&&(ab==false)&&(U[o-(y+1)]=true)&&(o>2)&&(o!=x-1)/*&&(OnFire(o,"sTrend","tTrend"))*/)
            {if(HH[o-(y+1)]>Premium[o-(y+1)])
                {h=o;
                if((C==false)&&(c==false))
                    {G(); Signal(); tickTock=true; /*if(KC==true) */tag=0;/* else tag=1;*/ dime=mem; Alert("Sin.",price,"o:",o,"|",C,":",c);}
                else if((C==true)||(c==true))
                    {G(); Signal(); tickTock=true; /*if(KC==true) */tag=1;/* else tag=0;*/ dime=mem; Alert("Sine.",price,"o:",o,"|",C,":",c);}}
            if(LL[o-(y+1)]<Discount[o-(y+1)])
                {h=o;
                if((C==false)&&(c==false))
                    {G(); Signal(); tickTock=true; /*if(KC==true) */tag=1;/* else tag=0;*/ dime=mem; Alert("Sine.",price,"o:",o,"|",C,":",c);}
                else if((C==true)||(c==true))
                    {G(); Signal(); tickTock=true; /*if(KC==true) */tag=0;/* else tag=1;*/ dime=mem; Alert("Sin.",price,"o:",o,"|",C,":",c);}}}}
    else if(OnGaurd(-1)!=KC)
        {if((h!=0)&&(ab==false)&&(U[O-(y+1)]=true)&&(O>2)&&(O!=x-1)/*&&(OnFire(O,"sTrend","tTrend"))*/)
            {if(HH[O-(y+1)]>Premium[O-(y+1)])
                {h=O;
                if((C==false)||(c==false))
                    {G(); Signal(); tickTock=true; /*if(KC==true) */tag=0;/* else tag=1;*/ dime=mem; Alert("Sin.",price,"O:",O,"|",C,":",c);}
                else if((C==true)&&(c==true))
                    {G(); Signal(); tickTock=true; /*if(KC==true) */tag=1;/* else tag=0;*/ dime=mem; Alert("Sine.",price,"O:",O,"|",C,":",c);}} 
            if(LL[O-(y+1)]<Discount[O-(y+1)])
                {h=O;
                if((C==false)||(c==false))
                    {G(); Signal(); tickTock=true; /*if(KC==true) */tag=1;/* else tag=0;*/ dime=mem; Alert("Sine.",price,"O:",O,"|",C,":",c);}
                else if((C==true)&&(c==true))
                    {G(); Signal(); tickTock=true; /*if(KC==true) */tag=0;/* else tag=1;*/ dime=mem; Alert("Sin.",price,"O:",O,"|",C,":",c);}}}
        if((h!=0)&&(ab==false)&&(U[o-(y+1)]=true)&&(o>2)&&(o!=x-1)/*&&(OnFire(o,"sTrend","tTrend"))*/)
            {if(HH[o-(y+1)]>Premium[o-(y+1)])
                {h=o;
                if((C==true)&&(c==true))
                    {G(); Signal(); tickTock=true; /*if(KC==true) */tag=0;/* else tag=1;*/ dime=mem; Alert("Sin.",price,"o:",o,"|",C,":",c);}
                else if((C==false)||(c==false))
                    {G(); Signal(); tickTock=true; /*if(KC==true) */tag=1;/* else tag=0;*/ dime=mem; Alert("Sine.",price,"o:",o,"|",C,":",c);}}
            if(LL[o-(y+1)]<Discount[o-(y+1)])
                {h=o;
                if((C==true)&&(c==true))
                    {G(); Signal(); tickTock=true; /*if(KC==true) */tag=1;/* else tag=0;*/ dime=mem; Alert("Sine.",price,"o:",o,"|",C,":",c);}
                else if((C==false)||(c==false))
                    {G(); Signal(); tickTock=true; /*if(KC==true) */tag=0;/* else tag=1;*/ dime=mem; Alert("Sin.",price,"o:",o,"|",C,":",c);}
                }
            }
        }    // Complex edge case resolution: Multi-scale indicator convergence at support/resistance boundaries.
    // Validates arc-length coherence across nested temporal derivatives (iz, iO, iw, io).
    if((h!=0)&&(signal!=0)&&(ab==ba))
        {if((OnGaurd(-1))&&(KC==true))
            {if((iz>=h)&&(iz>2)&&(((iZ>2)&&((iZ==iz)||(iZ==iz+h)||((iZ==iz+io)&&(l[io-(y+1)]==false)/*&&(OnHold(o,"sRange","tRange"))*/)))||((I>2)&&((I==iz)||(I==iz+h)||((I==iz+io)&&(l[io-(y+1)]==false)/*&&(OnHold(o,"sRange","tRange"))*/))))&&(k[iz-(y+1)]==false)/*&&(OnHold(z,"sTrend","tTrend"))*/)
                {h=iz;
                if((C==false)&&(c==false))
                    {G(); Signal(); tickTock=true; /*if(KC==true) */tag=0;/* else tag=1;*/ dime=mem; Alert("Sin.",price," h:",h,"iZ:",iZ,"I:",I,"|=iz:",iz,"|",C);}
                else if((C==true)||(c==true))
                    {G(); Signal(); tickTock=true; /*if(KC==true) */tag=1;/* else tag=0;*/ dime=mem; Alert("Sine.",price," h:",h,"iZ:",iZ,"I:",I,"|=iz:",iz,"|",C);}}
            else if((iO>=h)&&(iO>2)&&(((iZ>2)&&((iZ==iO)||(iZ==iO+h)||((iZ==iO+io)&&(l[io-(y+1)]==false)/*&&(OnHold(o,"sRange","tRange"))*/)))||((I>2)&&((I==iO)||(I==iO+h)||((I==iO+io)&&(l[io-(y+1)]==false)/*&&(OnHold(o,"sRange","tRange"))*/))))&&(k[iO-(y+1)]==false)/*&&(OnHold(O,"sRange","tRange"))*/)
                {h=iO;
                if((C==false)&&(c==false))
                    {G(); Signal(); tickTock=true; /*if(KC==true) */tag=1;/* else tag=0;*/ dime=mem; Alert("Sine.",price," h:",h,"o:",o,"iZ:",iZ,"I:",I,"|=iO:",iO,"|",C);}
                if((C==true)||(c==true))
                    {G(); Signal(); tickTock=true; /*if(KC==true) */tag=0;/* else tag=1;*/ dime=mem; Alert("Sin.",price," h:",h,"o:",o,"iZ:",iZ,"I:",I,"|=iO:",iO,"|",C);}}
            if((iw>=h)&&(iw>2)&&(((iW>2)&&((iW==iw)||(iW==iw+h)||((iW==iw+io)&&(l[io-(y+1)]==false)/*&&(OnHold(o,"sRange","tRange"))*/)))||((I>2)&&((I==iw)||(I==iw+h)||((I==iw+io)&&(l[io-(y+1)]==false)/*&&(OnHold(o,"sRange","tRange"))*/))))&&(l[iw-(y+1)]==false)/*&&(OnHold(w,"sTrend","tTrend"))*/)
                {h=iw;
                if((C==false)&&(c==false))
                    {G(); Signal(); tickTock=true; /*if(KC==true) */tag=1;/* else tag=0;*/ dime=mem; Alert("Sine.",price," h:",h,"iW:",iW,"I:",I,"|=iw:",iw,"|",C);}
                else if((C==true)||(c==true))
                    {G(); Signal(); tickTock=true; /*if(KC==true) */tag=0;/* else tag=1;*/ dime=mem; Alert("Sin.",price," h:",h,"iW:",iW,"I:",I,"|=iw:",iw,"|",C);}}
            else if((iO>=h)&&(iO>2)&&(((iW>2)&&((iW==iO)||(iW==iO+h)||((iW==iO+io)&&(l[io-(y+1)]==false)/*&&(OnHold(o,"sRange","tRange"))*/)))||((I>2)&&((I==iO)||(I==iO+h)||((I==iO+io)&&(l[io-(y+1)]==false)/*&&(OnHold(o,"sRange","tRange"))*/))))&&(l[iO-(y+1)]==false)/*&&(OnHold(O,"sRange","tRange"))*/)
                {h=iO;
                if((C==false)&&(c==false))
                    {G(); Signal(); tickTock=true; /*if(KC==true) */tag=0;/* else tag=1;*/ dime=mem; Alert("Sin.",price," h:",h,"o:",o,"iW:",iW,"I:",I,"|=iO:",iO,"|",C);}
                else if((C==true)||(c==true))
                    {G(); Signal(); tickTock=true; /*if(KC==true) */tag=1;/* else tag=0;*/ dime=mem; Alert("Sine.",price," h:",h,"o:",o,"iW:",iW,"I:",I,"|=iO:",iO,"|",C);}}}
        else if(OnGaurd(-1)!=KC)
            {if((iz>=h)&&(iz>2)&&(((iZ>2)&&((iZ==iz)||(iZ==iz+h)||((iZ==iz+io)&&(l[io-(y+1)]==false)/*&&(OnHold(o,"sRange","tRange"))*/)))||((I>2)&&((I==iz)||(I==iz+h)||((I==iz+io)&&(l[io-(y+1)]==false)/*&&(OnHold(o,"sRange","tRange"))*/))))&&(k[iz-(y+1)]==false)/*&&(OnHold(z,"sTrend","tTrend"))*/)
                {h=iz;
                if((C==true)&&(c==true)){G(); Signal(); tickTock=true; /*if(KC==true) */tag=0;/* else tag=1;*/ dime=mem; Alert("Sin.",price," h:",h,"iZ:",iZ,"I:",I,"|=iz:",iz,"|",C);}
                else if((C==false)||(c==false)){G(); Signal(); tickTock=true; /*if(KC==true) */tag=1;/* else tag=0;*/ dime=mem; Alert("Sine.",price," h:",h,"iZ:",iZ,"I:",I,"|=iz:",iz,"|",C);}}
            else if((iO>=h)&&(iO>2)&&(((iZ>2)&&((iZ==iO)||(iZ==iO+h)||((iZ==iO+io)&&(l[io-(y+1)]==false)/*&&(OnHold(o,"sRange","tRange"))*/)))||((I>2)&&((I==iO)||(I==iO+h)||((I==iO+io)&&(l[io-(y+1)]==false)/*&&(OnHold(o,"sRange","tRange"))*/))))&&(k[iO-(y+1)]==false)/*&&(OnHold(O,"sRange","tRange"))*/)
                {h=iO;
                if((C==true)&&(c==true)){G(); Signal(); tickTock=true; /*if(KC==true) */tag=1;/* else tag=0;*/ dime=mem; Alert("Sine.",price," h:",h,"o:",o,"iZ:",iZ,"I:",I,"|=iO:",iO,"|",C);}
                if((C==false)||(c==false)){G(); Signal(); tickTock=true; /*if(KC==true) */tag=0;/* else tag=1;*/ dime=mem; Alert("Sin.",price," h:",h,"o:",o,"iZ:",iZ,"I:",I,"|=iO:",iO,"|",C);}}
            if((iw>=h)&&(iw>2)&&(((iW>2)&&((iW==iw)||(iW==iw+h)||((iW==iw+io)&&(l[io-(y+1)]==false)/*&&(OnHold(o,"sRange","tRange"))*/)))||((I>2)&&((I==iw)||(I==iw+h)||((I==iw+io)&&(l[io-(y+1)]==false)/*&&(OnHold(o,"sRange","tRange"))*/))))&&(l[iw-(y+1)]==false)/*&&(OnHold(w,"sTrend","tTrend"))*/)
                {h=iw;
                if((C==true)&&(c==true)){G(); Signal(); tickTock=true; /*if(KC==true) */tag=1;/* else tag=0;*/ dime=mem; Alert("Sine.",price," h:",h,"iW:",iW,"I:",I,"|=iw:",iw,"|",C);}
                else if((C==false)||(c==false)){G(); Signal(); tickTock=true; /*if(KC==true) */tag=0;/* else tag=1;*/ dime=mem; Alert("Sin.",price," h:",h,"iW:",iW,"I:",I,"|=iw:",iw,"|",C);}}
            else if((iO>=h)&&(iO>2)&&(((iW>2)&&((iW==iO)||(iW==iO+h)||((iW==iO+io)&&(l[io-(y+1)]==false)/*&&(OnHold(o,"sRange","tRange"))*/)))||((I>2)&&((I==iO)||(I==iO+h)||((I==iO+io)&&(l[io-(y+1)]==false)/*&&(OnHold(o,"sRange","tRange"))*/))))&&(l[iO-(y+1)]==false)/*&&(OnHold(O,"sRange","tRange"))*/)
                {h=iO; 
                if((C==true)&&(c==true)){G(); Signal(); tickTock=true; /*if(KC==true) */tag=0;/* else tag=1;*/ dime=mem; Alert("Sin.",price," h:",h,"o:",o,"iW:",iW,"I:",I,"|=iO:",iO,"|",C);}
                else if((C==false)||(c==false)){G(); Signal(); tickTock=true; /*if(KC==true) */tag=1;/* else tag=0;*/ dime=mem; Alert("Sine.",price," h:",h,"o:",o,"iW:",iW,"I:",I,"|=iO:",iO,"|",C);}}
            }
        }
    tick ++;
    if(ab!=ba){ab=ba;} tickTock = false;
    }
// [FINAL REVERSAL SIGNAL TRIGGERS: ONGOE() & ONTOE()]
// OnGoe(): Bearish reversal signal generator - Triggers when arc-length deviation exceeds self-correcting capacity.
// Implements Kronecker-delta execution rule: delta(m-n-2)=1 via conservative approximation (m >= 12 guarantees n <= 2).
// Maps to non-Hermitian Lindblad dynamics: decoherence event mediated by Observer Operator O[Ψ] collapses superposition.
void OnGoe(){
    if(signal == 0){
        if((OnGaurd(0)) && (KC == true)){
            if(((h == io) && (z > o)) || ((h == iO) && (Z > O)) || ((h == iz) && (Z > z)) || ((h == iZ) && (Z < z))){
                if((C == false) && (c == false)){
                    prime = 1; G(); Signal(); tickTock = true; tag = 1; Alert("Sign.", price, " h:", h, "| ", "Z:", iZ, "z:", iz, "O:", iO, "o:", io, "| ", C, ":", c);
                } else{
                    prime = 1; G(); Signal(); tickTock = true; tag = 1; Alert("Sig.", price, " h:", h, "| ", "Z:", iZ, "z:", iz, "O:", iO, "o:", io, "| ", C, ":", c);
                }
            } else if(((h == io) || (h == iZ) || (h == iz) || (h == iO))){
                if((C == false) && (c == false)){
                    prime = 1; G(); Signal(); tickTock = true; tag = 1; Alert("Sig.", price, " h:", h, "Z:", iZ, "z:", iz, "O:", iO, "o:", io, "| ", C, ":", c);
                } else{
                    prime = 1; G(); Signal(); tickTock = true; tag = 1; Alert("Sign.", price, " h:", h, "Z:", iZ, "z:", iz, "O:", iO, "o:", io, "| ", C, ":", c);
                }
            }
        } else if(OnGaurd(0) != KC){
            if(((h == io) && (z > o)) || ((h == iO) && (Z > O)) || ((h == iz) && (Z > z)) || ((h == iZ) && (Z < z))){
                if((C == false) || (c == false)){
                    prime = 1; G(); Signal(); tickTock = true; tag = 1; Alert("Sign.", price, " h:", h, "| ", "Z:", iZ, "z:", iz, "O:", iO, "o:", io, "| ", C, ":", c);
                } else{
                    prime = 1; G(); Signal(); tickTock = true; tag = 1; Alert("Sig.", price, " h:", h, "| ", "Z:", iZ, "z:", iz, "O:", iO, "o:", io, "| ", C, ":", c);
                }
            } else if(((h == io) || (h == iZ) || (h == iz) || (h == iO))){
                if((C == false) || (c == false)){
                    prime = 1; G(); Signal(); tickTock = true; tag = 1; Alert("Sig.", price, " h:", h, "Z:", iZ, "z:", iz, "O:", iO, "o:", io, "| ", C, ":", c);
                } else{
                    prime = 1; G(); Signal(); tickTock = true; tag = 1; Alert("Sign.", price, " h:", h, "Z:", iZ, "z:", iz, "O:", iO, "o:", io, "| ", C, ":", c);
                }
            }
            KC();
        }
    }
}
// OnToe(): Bullish reversal signal generator - Triggers when arc-length compression exceeds self-correcting capacity.
// Symmetric logic to OnGoe() with inverted conditions: Oversold confirmation (n >= 12) triggers contrarian long entry.
// Maps to unit phase manifold topology: Snap-back to equilibrium when perturbation exceeds manifold's self-correcting threshold.
void OnToe(){
    if(signal == 0){
        if((OnGaurd(0)) && (KC == true)){
            if(((h == io) && (w > o)) || ((h == iO) && (W > O)) || ((h == iw) && (W > w)) || ((h == iW) && (W < w))){
                if((C == false) && (c == false)){
                    prime = 0; G(); Signal(); tickTock = true; tag = 0; Alert("Sig.", price, " h:", h, " W<w ", "| ", "W:", iW, "w:", iw, "O:", iO, "o:", io, "| ", C, ":", c);
                } else{
                    prime = 0; G(); Signal(); tickTock = true; tag = 0; Alert("Sign.", price, " h:", h, " W<w ", "| ", "W:", iW, "w:", iw, "O:", iO, "o:", io, "| ", C, ":", c);
                }
            } else if(((h == io) || (h == iW) || (h == iw) || (h == iO))){
                if((C == false) && (c == false)){
                    prime = 0; G(); Signal(); tickTock = true; tag = 0; Alert("Sign.", price, " h:", h, "W:", iW, "w:", iw, "O:", iO, "o:", io, "| ", C, ":", c);
                } else{
                    prime = 0; G(); Signal(); tickTock = true; tag = 0; Alert("Sig.", price, " h:", h, "W:", iW, "w:", iw, "O:", iO, "o:", io, "| ", C, ":", c);
                }
            }
        } else if(OnGaurd(0) != KC){
            if(((h == io) && (w > o)) || ((h == iO) && (W > O)) || ((h == iw) && (W > w)) || ((h == iW) && (W < w))){
                if((C == false) || (c == false)){
                    prime = 0; G(); Signal(); tickTock = true; tag = 0; Alert("Sig.", price, " h:", h, " W<w ", "| ", "W:", iW, "w:", iw, "O:", iO, "o:", io, "| ", C, ":", c);
                } else{
                    prime = 0; G(); Signal(); tickTock = true; tag = 0; Alert("Sign.", price, " h:", h, " W<w ", "| ", "W:", iW, "w:", iw, "O:", iO, "o:", io, "| ", C, ":", c);
                }
            } else if(((h == io) || (h == iW) || (h == iw) || (h == iO))){
                if((C == false) || (c == false)){
                    prime = 0; G(); Signal(); tickTock = true; tag = 0; Alert("Sign.", price, " h:", h, "W:", iW, "w:", iw, "O:", iO, "o:", io, "| ", C, ":", c);
                } else{
                    prime = 0; G(); Signal(); tickTock = true; tag = 0; Alert("Sig.", price, " h:", h, "W:", iW, "w:", iw, "O:", iO, "o:", io, "| ", C, ":", c);
                }
            }
            KC();
        }
    }
}
// [EXTREMA TRACKING: ONTRACK() & ONSTAND()]
// OnTrack(): Upside regime scanner - extends analysis beyond maximum valued range during news-worthy events
// Theoretical basis: Scans periods where price trajectory exceeds Premium boundary (s >> r expansion phase)
// Maps to Aetheric volatility classification: identifies sVolatile/tVolatile regimes via normalized turbulence metrics
void OnTrack(){
    S = x; T = x; X = y; Y = y; datetime is = iTime(_Symbol, 0, 0);
    for(int s = x - 1; s < S; s++){
        int js = s; j = js; Normalize(); Unify();
        if((Suply <= price) || (iSuply <= price) || (iSuply <= iH)){
            int i = s; I = iW; j = max; Z = j; iZ = i; T++; iC = C;
            if((iw != 0) && (jC == Cc)){ h = I; } jC = !C;
            if(iStdDev > 50){ S++; iz = i; iI = iw; j = i; H(); }
            else if(iATR < 50){ S++; iO = i; io = i; j = i; H(); }
            else{ j = i; H(); if(is != t){ if(OnFire(j, "Stable", "tVolatile")){ F(); Regime[j - (y + 1)] = "tVolatile"; } } else{ Regime[j - (y + 1)] = "sVolatile"; } S++; }
        }
        if((Demand >= price) || (iDemand >= price) || (iDemand >= iL)){
            int i = s; I = iZ; j = max; W = j; iW = i; T++; jC = C;
            if((iz != 0) && (iC == Cc)){ h = I; } iC = !C;
            if(iStdDev > 50){ S++; iw = i; iI = iz; j = i; L(); }
            else if(iATR < 50){ S++; iO = i; io = i; j = i; L(); }
            else{ j = i; L(); if(is != t){ if(OnFire(j, "Stable", "tVolatile")){ F(); Regime[j - (y + 1)] = "tVolatile"; } } else{ Regime[j - (y + 1)] = "sVolatile"; } S++; }
        } if(s == 4 * max) break;
    }
    for(int s = x - 1; s < S; s++){
        int js = s; j = js; Normalize(); Unify();
        if((iStdDev < 50) && (iATR < 50)){ R(); L(); H(); }
    }
    S = x; T = x;
    if((Z != 4 * max) && (Z >= z)){ j = max - 1; z = j; if(is != t){ if(Regime[j - (y + 1)] != "tTrend"){ F(); Regime[j - (y + 1)] = "tTrend"; } } else{ Regime[j - (y + 1)] = "sTrend"; } }
    else if((Z != 4 * max) && (Z < z)){ j = max; z = j; if(is != t){ if(Regime[j - (y + 1)] != "tTrend"){ F(); Regime[j - (y + 1)] = "tTrend"; } } else{ Regime[j - (y + 1)] = "sTrend"; } }
    else{ j = x - 1; z = j; if(is != t){ if(Regime[j - (y + 1)] != "tTrend"){ F(); Regime[j - (y + 1)] = "tTrend"; } } else{ Regime[j - (y + 1)] = "sTrend"; } }
    if((W != 4 * max) && (W >= w)){ j = max - 1; w = j; if(is != t){ if(Regime[j - (y + 1)] != "tTrend"){ F(); Regime[j - (y + 1)] = "tTrend"; } } else{ Regime[j - (y + 1)] = "sTrend"; } }
    else if((W != 4 * max) && (W < w)){ j = max; w = j; if(is != t){ if(Regime[j - (y + 1)] != "tTrend"){ F(); Regime[j - (y + 1)] = "tTrend"; } } else{ Regime[j - (y + 1)] = "sTrend"; } }
    else{ j = x - 1; w = j; if(is != t){ if(Regime[j - (y + 1)] != "tTrend"){ F(); Regime[j - (y + 1)] = "tTrend"; } } else{ Regime[j - (y + 1)] = "sTrend"; } }
}
// OnStand(): Downside regime scanner - extends analysis below minimum valued range during extenuating circumstances
// Theoretical basis: Scans periods where price trajectory falls below Discount boundary (s << r compression phase)
// Maps to Aetheric volatility classification: identifies forced deleveraging or panic capitulation regimes
void OnStand(){
    S = x; T = x; X = y; Y = y; datetime is = iTime(_Symbol, 0, 0);
    for(int s = y + 1; s > Y; s--){
        if(s == 1) break; int js = s; j = js; ir = 0; ij = 0; Normalize(); Unify();
        if((Suply <= price) || (iSuply <= price) || (iSuply <= iH)){
            int i = s; I = iW; j = min + 1; Z = j; iZ = i; T--; iC = C;
            if((iw != 0) && (jC == Cc)){ h = I; } jC = !C;
            if((X != Y) && (iz == 0) && (iStdDev > 50)){ ij = i; iz = i; iI = iw; j = i; H(); if((ir == 0) && (Y != 2)){ Y--; } }
            else if((X != Y) && (iO == 0) && (iATR < 50)){ iO = i; ir = i; j = i; H(); if((ij == 0) && (Y != 2)){ Y--; } }
            else if(X == Y){ j = i; H(); if(is != t){ if(OnFire(j, "Stable", "tVolatile")){ F(); Regime[j - (y + 1)] = "tVolatile"; } } else{ Regime[j - (y + 1)] = "sVolatile"; } if((Y != 2) && (X != 2)){ Y--; X--; } }
        }
        if((Demand >= price) || (iDemand >= price) || (iDemand >= iL)){
            int i = s; I = iZ; j = min + 1; W = j; iW = i; T--; jC = C;
            if((iz != 0) && (iC == Cc)){ h = I; } iC = !C;
            if((X != Y) && (iw == 0) && (iStdDev > 50)){ ij = i; iw = i; iI = iz; j = i; L(); if((ir == 0) && (Y != 2)){ Y--; } }
            else if((X != Y) && (iO == 0) && (iATR < 50)){ iO = i; io = i; ir = 0; j = i; L(); if((ij == 0) && (Y != 2)){ Y--; } }
            else if(X == Y){ j = i; L(); if(is != t){ if(OnFire(j, "Stable", "tVolatile")){ F(); Regime[j - (y + 1)] = "tVolatile"; } } else{ Regime[j - (y + 1)] = "sVolatile"; } if((Y != 2) && (X != 2)){ Y--; X--; } }
        }
        else{ if((Y != 2) && (X != 2)){ Y--; X--; } }
    }
    for(int s = Y + 1; s < y + 1; s++){
        int js = s; j = js; Normalize(); Unify();
        if((iStdDev < 50) && (iATR < 50)){ R(); L(); H(); }
    }
    X = y; Y = y;
    if((Z != 2) && (Z >= z)){ j = min; z = j; if(is != t){ if(Regime[j - (y + 1)] != "tTrend"){ F(); Regime[j - (y + 1)] = "tTrend"; } } else{ Regime[j - (y + 1)] = "sTrend"; } }
    else if((Z != 2) && (Z < z)){ j = min + 1; z = j; if(is != t){ if(Regime[j - (y + 1)] != "tTrend"){ F(); Regime[j - (y + 1)] = "tTrend"; } } else{ Regime[j - (y + 1)] = "sTrend"; } }
    else{ j = y + 1; z = j; if(is != t){ if(Regime[j - (y + 1)] != "tTrend"){ F(); Regime[j - (y + 1)] = "tTrend"; } } else{ Regime[j - (y + 1)] = "sTrend"; } }
    if((W != 2) && (W >= w)){ j = min; w = j; if(is != t){ if(Regime[j - (y + 1)] != "tTrend"){ F(); Regime[j - (y + 1)] = "tTrend"; } } else{ Regime[j - (y + 1)] = "sTrend"; } }
    else if((W != 2) && (W < w)){ j = min + 1; w = j; if(is != t){ if(Regime[j - (y + 1)] != "tTrend"){ F(); Regime[j - (y + 1)] = "tTrend"; } } else{ Regime[j - (y + 1)] = "sTrend"; } }
    else{ j = y + 1; w = j; if(is != t){ if(Regime[j - (y + 1)] != "tTrend"){ F(); Regime[j - (y + 1)] = "tTrend"; } } else{ Regime[j - (y + 1)] = "sTrend"; } }
}
// [MASTER EXECUTION LOOP: ONTICK()]
// Orchestrates all operational layers: Validation, State Update, Regime Classification, Signal Triggering
// Theoretical basis: Computes directional derivatives (Z/z, W/w, O/o) across temporal scales, monitors decoherence events
// Maps to Non-Hermitian Lindblad dynamics: computes d(rho)/dt in discrete steps synchronized with market ticks
void OnTick()
    {/*Unify(); Normalize();*/
    datetime is = iTime(_Symbol, 0, 0);
    price = SymbolInfoDouble(_Symbol, SYMBOL_BID);
    Price = iClose(Symbol(), 0, 1);
    open = iOpen(Symbol(), 0, 1);
    iH = iHigh(Symbol(), 0, 1);
    iL = iLow(Symbol(), 0, 1);
    // [FAIR VALUE GAP TRACKING: TOPOLOGICAL VISUALIZATION MAINTENANCE]
    if(FVG >= 0){
        for(int ii = 0; ii < FVG; ii++){
            bottomLine = DoubleToString(BL[ii], Digits);
            color bLC = (color)ObjectGet(bottomLine, OBJPROP_COLOR);
            if(bottomLine != bL){
                if((bLC == clrRed) && ((A == true) || (B == false)) && (BL[ii] <= price)){ if(E != 0){ Alert("Red"); } Deleter(bottomLine, BL, ii); }
                if((bLC == clrBlue) && ((B == true) || (A == false)) && (BL[ii] >= price)){ if(D != 0){ Alert("Blue"); } Deleter(bottomLine, BL, ii); }
            }
        }
    }
    // [INITIALIZATION PHASE: UNIT PHASE MANIFOLD RESET ON FIRST EXECUTION]
    if(FG == false){
        if(signature == false){ D = price; E = price; }
        ArrayResize(k, x - y); ArrayResize(l, x - y); ArrayResize(HH, x - y); ArrayResize(LL, x - y);
        ArrayResize(Premium, x - y); ArrayResize(Discount, x - y); ArrayResize(Regime, x - y);
        for(j = y + 1; j < x; j++){ F(); }
        FG = true;
    }
    // [RISK MANAGEMENT UPDATE: TRAILING STOP AND PROFIT TRACKING]
    T();
    // [REGIME CLASSIFICATION: ON-BAR STATE EVALUATION]
    OnPoint();
    O(iO, O, J, C, Cc); O(io, o, iJ, c, cC);
    // [OBSERVER LAYER: MACROSCOPIC MEASUREMENT APPARATUS]
    OnCall();
    J();
    // [BAR-BY-BAR REGIME RECLASSIFICATION: EDGE CASE EVALUATION]
    if(is != t){ OnBar(); O(iO, O, J, C, Cc); O(io, o, iJ, c, cC); }
    // [DOWNSIDE EXTREMUM SCANNING: ONSTAND() ACTIVATION]
    if((J == y + 1) && (J != 2)){
        OnStand(); J(); O(iO, O, J, C, Cc); O(io, o, iJ, c, cC);
        if((iO != 2) && (J >= iO)){ j = min; O = j; if(is != t){ if(OnFire(j, "Stable", "tRange")){ F(); Regime[j - (y + 1)] = "tRange"; } } else{ Regime[j - (y + 1)] = "sRange"; } }
        else if((iO != 2) && (J < iO)){ j = min + 1; O = j; if(is != t){ if(OnFire(j, "Stable", "tRange")){ F(); Regime[j - (y + 1)] = "tRange"; } } else{ Regime[j - (y + 1)] = "sRange"; } }
        else{ j = 2; O = j; if(is != t){ if(OnFire(j, "Stable", "tRange")){ F(); Regime[j - (y + 1)] = "tRange"; } } else{ Regime[j - (y + 1)] = "sRange"; } }
        if((io != 2) && (iJ >= io)){ j = min; o = j; if(is != t){ if(OnFire(j, "Stable", "tRange")){ F(); Regime[j - (y + 1)] = "tRange"; } } else{ Regime[j - (y + 1)] = "sRange"; } }
        else if((io != 2) && (iJ < io)){ j = min + 1; o = j; if(is != t){ if(OnFire(j, "Stable", "tRange")){ F(); Regime[j - (y + 1)] = "tRange"; } } else{ Regime[j - (y + 1)] = "sRange"; } }
        else{ j = 2; o = j; if(is != t){ if(OnFire(j, "Stable", "tRange")){ F(); Regime[j - (y + 1)] = "tRange"; } } else{ Regime[j - (y + 1)] = "sRange"; } }
    }
    // [UPSIDE EXTREMUM SCANNING: ONTRACK() ACTIVATION]
    if(J == x - 1){
        OnTrack(); J(); O(iO, O, J, C, Cc); O(io, o, iJ, c, cC);
        if((iO != 4 * max) && (J >= iO)){ j = max - 1; O = j; if(is != t){ if(OnFire(j, "Stable", "tRange")){ F(); Regime[j - (y + 1)] = "tRange"; } } else{ Regime[j - (y + 1)] = "sRange"; } }
        else if((iO != 4 * max) && (J < iO)){ j = max; O = j; if(is != t){ if(OnFire(j, "Stable", "tRange")){ F(); Regime[j - (y + 1)] = "tRange"; } } else{ Regime[j - (y + 1)] = "sRange"; } }
        else{ j = x - 1; o = j; if(is != t){ if(OnFire(j, "Stable", "tRange")){ F(); Regime[j - (y + 1)] = "tRange"; } } else{ Regime[j - (y + 1)] = "sRange"; } }
        if((io != 4 * max) && (iJ >= io)){ j = max - 1; o = j; if(is != t){ if(OnFire(j, "Stable", "tRange")){ F(); Regime[j - (y + 1)] = "tRange"; } } else{ Regime[j - (y + 1)] = "sRange"; } }
        else if((io != 4 * max) && (iJ < io)){ j = max; o = j; if(is != t){ if(OnFire(j, "Stable", "tRange")){ F(); Regime[j - (y + 1)] = "tRange"; } } else{ Regime[j - (y + 1)] = "sRange"; } }
        else{ j = x - 1; o = j; if(is != t){ if(OnFire(j, "Stable", "tRange")){ F(); Regime[j - (y + 1)] = "tRange"; } } else{ Regime[j - (y + 1)] = "sRange"; } }
    } t = is;
    // [REVERSAL SIGNAL TRIGGERING: BEARISH DIRECTION (OnGoe())]
    if(Z != x - 1){
        if((Z != y + 1) && (k[iZ - (y + 1)] == true)){ h = iZ; OnGoe(); }
        else if((k[iz - (y + 1)] == true) && (z != y + 1) && (z != x - 1)){ h = iz; OnGoe(); }
        else if((k[io - (y + 1)] == true) && (o != y + 1) && (o != x - 1)){ h = io; OnGoe(); }
        else if((k[iO - (y + 1)] == true) && (O != y + 1) && (O != x - 1)){ h = iO; OnGoe(); }
    }
    // [REVERSAL SIGNAL TRIGGERING: BULLISH DIRECTION (OnToe())]
    if(W != x - 1){
        if((W != y + 1) && (l[iW - (y + 1)] == true)){ h = iW; OnToe(); }
        else if((l[iw - (y + 1)] == true) && (w != y + 1) && (w != x - 1)){ h = iw; OnToe(); }
        else if((l[io - (y + 1)] == true) && (o != y + 1) && (o != x - 1)){ h = io; OnToe(); }
        else if((l[iO - (y + 1)] == true) && (O != y + 1) && (O != x - 1)){ h = iO; OnToe(); }
    }
    // [SELF-EVOLUTION PROTOCOL: REINITIALIZATION ON COHERENCE RESTORATION]
    if(GF == true){ OnReInit(); GF = false; }
    // [STATE VISUALIZATION: REAL-TIME DIAGNOSTIC OUTPUT]
    Comment("    ^", iZ, ":", Z, "|", iz, ":", z, "=", k[Z - (y + 1)], "|", k[z - (y + 1)], "                                           <! †, ‡, # — ↑(0)|↓(1): ", prime, dime,mem," >",
    "\n Lim", iO, ":", O, "^", k[O - (y + 1)], "_", l[O - (y + 1)], ".", io, ":", o, "^", k[o - (y + 1)], "_", l[o - (y + 1)], "=", h, ".", C, ":", c,"             <! 100%✓ >",
    "\n    _", iW, ":", W, "|", iw, ":", w, "=", l[W - (y + 1)], "|", l[w - (y + 1)], "                                                 <! Natalia Tanyatia >");
    }
/*💎*/