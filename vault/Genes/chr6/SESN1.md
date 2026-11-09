---
symbol: "SESN1"
type: "gene"
col: 1283
ensembl_id: "ENSG00000080546"
name: "sestrin 1"
location: "6q21"
module: 62
arm: "+"
pooled_cpm: 44.95
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 7
n_dd_up_clean: 20
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/062", "written"]
generated_by: "tahoemap"
---

# SESN1

*sestrin 1* — 6q21

> [!summary] In one line
> SESN1 encodes sestrin 1, a stress-inducible protein that restrains mTORC1 and lowers reactive oxygen species, and one of the most dependably p53-dependent transcripts in the human genome.

## What it is

SESN1 was cloned as PA26 — "p53-activated gene 26" — and the identification was unusually clean: a p53 response element in intron 2, induction by genotoxic agents only when p53 is present. It is one of three mammalian sestrins (SESN1, SESN2, SESN3). The sestrin fold matches no familiar enzyme class; its closest recognised relative is bacterial AhpD, which is how the original antioxidant hypothesis arose.

What sestrins are now best understood to do is inhibit mTORC1. The first mechanism proposed was indirect: sestrins 1 and 2 activate AMPK, which phosphorylates TSC2 and suppresses mTORC1, linking DNA damage to a halt in anabolic growth. A more direct route came later — sestrins bind GATOR2 in the amino-acid-sensing arm upstream of mTORC1, and for sestrin 2 that interaction is governed by direct leucine binding. Both converge on the same output: less mTORC1, less cap-dependent translation, more autophagy.

The antioxidant side is real but less mechanistically settled. Sestrin expression lowers intracellular ROS in many systems, and sestrin loss raises it; what is no longer tenable is the specific claim that sestrins act as reductases for overoxidised peroxiredoxins. Inputs besides p53 are described for the family, but they sort unevenly across the three paralogues: oxidative and hypoxic induction of SESN2 and SESN3 proceeds without p53, whereas SESN1's requires it, and the clear FOXO target is SESN3, with only a reported minor contribution to SESN1.

## What is uncertain

The strongest claim is the weakest-sounding one: SESN1 is p53-inducible. Almost everything downstream carries qualifications. The AMPK/TSC2 and GATOR2 routes have not been reconciled into a single accounting. More importantly for this gene specifically, the structural and leucine-sensing work was done on sestrin 2; transferring it to sestrin 1 is a paralogue inference, not a result. Much of what is written about "sestrins" rests on SESN2 experiments, so claims about SESN1's own biology are thinner than the family literature suggests.

The redox function remains mechanistically open now that the peroxiredoxin-reductase model has failed; lower ROS may be downstream of mTORC1 inhibition, autophagy or NRF2 rather than a direct catalytic activity. The standing caution that a stress gene's induction need not mean p53 caused it applies less forcefully here than to most of this panel, because the p53-independent routes in the sestrin literature are largely SESN2 and SESN3 results; a FOXO contribution to SESN1 and a HIF1 input have been reported, so it is not a pure p53 reporter, but it is a more specific one than its paralogues. Finally, SESN1 is not a recurrently mutated cancer gene; its tumour-suppressive reading is inherited from p53 rather than established on its own.

## References

- Velasco-Miguel et al., 1999, Oncogene — identified PA26/SESN1 as a p53-inducible gene with a p53 response element in intron 2.
- Budanov & Karin, 2008, Cell — sestrin1 and sestrin2 are p53 targets that activate AMPK, target it to TSC2 and inhibit mTOR.
- Woo et al., 2009, Antioxidants & Redox Signaling — sestrin 2 does not reduce the cysteine sulfinic acid of peroxiredoxins, contradicting the proposed reductase role.
- Chantranupong et al., 2014, Cell Reports — the sestrins interact with GATOR2 to negatively regulate the amino-acid-sensing pathway upstream of mTORC1.
- Wolfson et al., 2016, Science — sestrin 2 binds leucine directly and acts as a leucine sensor for mTORC1.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.08× (z +28.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.519× (z -11.4, q 2e-27, down in 32 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.597× (z -9.4, q 1e-18, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPM1D]] (+0.71, fdr 7e-06), [[FDXR]] (+0.66, fdr 1e-05), [[GPX1]] (+0.65, fdr 1e-05); moves opposite to [[LMCD1-AS1]] (-0.57, fdr 8e-05), [[ANAPC1P4]] (-0.55, fdr 2e-05), [[ZNF473]] (-0.55, fdr 4e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TP53]] → it (grade A ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1283.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.08×** | +28.8 | 0e+00 | 48/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.76×** | +17.6 | 0e+00 | 44/47 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +13.8 | 6e-41 | 40/49 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +11.5 | 1e-28 | 42/47 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.83×** | +10.9 | 1e-25 | 38/48 (NCI-H2030, SNU-423, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.74×** | +10.0 | 1e-21 | 37/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.74×** | +10.0 | 1e-21 | 38/48 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +8.0 | 6e-14 | 33/48 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.53×** | +7.7 | 8e-13 | 37/48 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +7.4 | 1e-11 | 32/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +7.1 | 9e-11 | 26/48 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +6.7 | 8e-10 | 27/48 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.44×** | +6.6 | 2e-09 | 34/47 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.29×** | +6.5 | 3e-09 | 24/48 (SNU-1, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.91×** | +6.1 | 3e-08 | 28/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +5.1 | 1e-05 | 25/48 (SW480, NCI-H661, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +4.8 | 5e-05 | 22/47 (SNU-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.32×** | +4.6 | 1e-04 | 22/48 (SW480, BT-474, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1283.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.519×** | -11.4 | 2e-27 | 32/41 (LS 180, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.543×** | -11.1 | 5e-26 | 35/48 (CHP-212, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.597×** | -9.4 | 1e-18 | 39/48 (A498, SK-MEL-2, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.789×** | -4.1 | 0.005 | 17/47 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.801×** | -4.0 | 0.006 | 19/47 (NCI-H23, A-427, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.823×** | -3.5 | 0.039 | 14/48 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~65% of this change | **0.827×** | -3.5 | 0.043 | 18/46 (RPMI-7951, NCI-H661, …) | inconsistent across doses | low cells (technical?) |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.840× | -3.2 | 0.11 | 12/48 (NCI-H460, LS 180, …) | top dose only |  |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.845× | -3.1 | 0.14 | 11/48 (LS 180, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1283. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 78.4 | 6 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +19.1) | [[Dinaciclib (drug)]] 5 µM 0.347× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 40.3 | 6 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.00× (z +19.6) | [[Dinaciclib (drug)]] 5 µM 0.295× (z -11.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 52.1 | 4 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.336× (z -8.8) |
| [[A498 (line)]] | wt | 48.1 | 4 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.308× (z -9.7) |
| [[RKO (line)]] | wt | 41.5 | 5 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.75× (z +16.5) | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 60.8 | 5 (3 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.03× (z +10.7) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.90× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 43.3 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.218× (z -11.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 71.3 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.187× (z -13.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 39.1 | 4 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.67× (z +14.5) | — |
| [[hTERT-HPNE (line)]] | wt | 59.9 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.121× (z -13.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 60.8 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +14.2) | — |
| [[NCI-H2347 (line)]] | alt | 29.5 | 2 (1 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.30× (z +10.4) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.190× (z -14.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 35.8 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.438× (z -8.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 31.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +14.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 25.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.39× (z +20.6) | — |
| [[NCI-H2030 (line)]] | alt | 37.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.88× (z +12.1) | — |
| [[RPMI-7951 (line)]] | alt | 35.5 | 2 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.53× (z +12.1) | [[Docetaxel (drug)]] 0.05 µM 0.0879× (z -16.3) ⚠ transcription drop; cell-cycle shift, explains ~65% of this change |
| [[SK-MEL-2 (line)]] | alt | 47.3 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.358× (z -9.4) |
| [[A-427 (line)]] | wt | 64.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.117× (z -18.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 46.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.47× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 62.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -10.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 76.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0521× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.114× (z -10.2) |
| [[HCT15 (line)]] | alt | 32.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -10.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 27.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +17.5) | — |
| [[HepG2_C3A (line)]] | wt | 68.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -9.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 58.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +11.6) | — |
| [[KATO III (line)]] | alt | 37.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -9.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 71.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -12.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 94.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.92× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.0904× (z -19.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 50.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.27× (z +15.1) | — |
| [[AsPC-1 (line)]] | alt | 31.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.23× (z +14.5) | — |
| [[BT-474 (line)]] | alt | 68.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 12.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +11.8) | — |
| [[COLO 205 (line)]] | alt | 31.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +9.7) | — |
| [[H4 (line)]] | wt | 24.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.20× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 30.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +12.7) | — |
| [[J82 (line)]] | alt | 32.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 19.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.277× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 34.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +9.1) | — |
| [[NCI-H661 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.149× (z -9.6) ⚠ transcription drop; cell-cycle shift, explains ~65% of this change |
| [[Panc 03.27 (line)]] | alt | 23.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +11.9) | — |
| [[SHP-77 (line)]] | alt | 58.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -16.7) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 57.9 | 0 | 1 | — | [[Resveratrol (drug)]] 0.5 µM 0.0716× (z -9.1) |
| [[SW 900 (line)]] | alt | 29.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 18.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.24× (z +13.9) | — |
| [[AN3 CA (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1283), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPM1D]] | +0.71 | +0.61 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 452 |
| [[FDXR]] | +0.66 | +0.57 / +0.71 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY; STRING 545 |
| [[GPX1]] | +0.65 | +0.49 / +0.64 | both halves | 1e-05 | pathway: Cellular response to chemical stress |
| [[FBXO22]] | +0.64 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[DDB2]] | +0.62 | +0.48 / +0.63 | both halves | 2e-05 | pathway: HALLMARK_P53_PATHWAY; STRING 528 |
| [[ANKRA2]] | +0.62 | +0.51 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[ACTA2]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[TP53INP1]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 | STRING 470 |
| [[ZMAT3]] | +0.60 | +0.50 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY; STRING 554 |
| [[FAS]] | +0.59 | +0.44 / +0.56 | both halves | 3e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[TIGAR]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 | pathway: TP53 Regulates Metabolic Genes; STRING 568 |
| [[GRIN2C]] | +0.58 | +0.43 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMCD1-AS1]] | -0.57 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[ANAPC1P4]] | -0.55 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[ZNF473]] | -0.55 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[RUVBL2]] | -0.55 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[MIR4435-2HG]] | -0.50 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[DNAJB1]] | -0.49 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[UTP11]] | -0.49 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[TAF1A]] | -0.47 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[CCT2]] | -0.47 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[DRG2]] | -0.47 | -0.46 / -0.25 | both halves | 4e-04 |  |
| [[NUDC]] | -0.46 | -0.38 / -0.50 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 1, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53]] | A | TP53 activity strengthens SESN1's drug response | recorded loss-of-function mutation of TP53 in 32 lines vs 17 not recorded | the TP53-altered lines respond 0.79× as strongly (z diff +0.91); strongest at Topotecan (hydrochloride) 5 µM: 1.67x vs 2.90x (z diff +3.7) | 0.040 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; both ways; artifact flags |
| [[PINCR]] | B | PINCR activity strengthens SESN1's drug response | lines that do not express PINCR (29) vs lines expressing it (20) | the lines without PINCR respond 0.84× as strongly (z diff +0.80); strongest at Topotecan (hydrochloride) 5 µM: 1.66x vs 2.76x (z diff +3.6) | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; both ways; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers SESN1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PTCHD4]] | B | PTCHD4 activity strengthens SESN1's drug response | lines that do not express PTCHD4 (33) vs lines expressing it (16) | the lines without PTCHD4 respond 0.91× as strongly (z diff +0.88); rises at some drug-doses, falls at others (74% from rises): Idarubicin (hydrochloride) 0.5 µM: 1.56x vs 2.46x (z diff +3.4); Topotecan (hydrochloride) 5 µM: 1.76x vs 2.78x (z diff +3.2); Dinaciclib 5 µM: 0.55x vs 0.29x (z diff +3.1) | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[PTCHD4]] | B | PTCHD4 activity raises SESN1's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 1.44× lower at baseline in the lines without PTCHD4 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[TP53INP1]] | B | TP53INP1 activity raises SESN1's level | lines that do not express TP53INP1 (7) vs lines expressing it (43) | 1.61× lower at baseline in the lines without TP53INP1 | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379; maybe low, not absent |
| [[ATP8B3]] | B | ATP8B3 activity lowers SESN1's level | lines that do not express ATP8B3 (5) vs lines expressing it (45) | 1.65× higher at baseline in the lines without ATP8B3 | 0.079 | ⚠ within organs, on part of the lines; also absent: CEP85L, PARP3, SOAT1; maybe low, not absent |
| [[PINCR]] | B | PINCR activity raises SESN1's level | lines that do not express PINCR (29) vs lines expressing it (21) | 1.36× lower at baseline in the lines without PINCR | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.701). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.3, 35.8); signed map (42.0, -25.4). **Vector** length 105, 29.1% of its response variance represented; |z| ≥ 3 in 1,353 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +17.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +13.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.0 | +11.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +28.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.6 | +10.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.8 | +3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.3 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +7.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.3 | +3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.2 | +4.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.8 | -9.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.8 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | +1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.6 | +8.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.5 | +10.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | +0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | +1.7 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | sestrin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:108,984,309-109,094,846 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SEST1, PA26 |
| Gene groups (HGNC) | Sestrin family |
| Hallmark sets | P53_PATHWAY |
| Reactome | 8 pathways, smallest: Amino acids regulate mTORC1; TP53 Regulates Metabolic Genes; KEAP1-NFE2L2 pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6P5](https://www.uniprot.org/uniprotkb/Q9Y6P5) (Sestrin-1):

> Functions as an intracellular leucine sensor that negatively regulates the TORC1 signaling pathway through the GATOR complex. In absence of leucine, binds the GATOR subcomplex GATOR2 and prevents TORC1 signaling. Binding of leucine to SESN2 disrupts its interaction with GATOR2 thereby activating the TORC1 signaling pathway. This stress-inducible metabolic regulator may also play a role in protection against oxidative and genotoxic stresses (By similarity). May positively regulate the …

**Summary**, from NCBI Gene [27244](https://www.ncbi.nlm.nih.gov/gene/27244):

> This gene encodes a member of the sestrin family. Sestrins are induced by the p53 tumor suppressor protein and play a role in the cellular response to DNA damage and oxidative stress. The encoded protein mediates p53 inhibition of cell growth by activating AMP-activated protein kinase, which results in the inhibition of the mammalian target of rapamycin protein. The encoded protein also plays a critical role in antioxidant defense by regenerating overoxidized peroxiredoxins, and the expression …

**Accessions** — [HGNC:21595](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21595) · Entrez [27244](https://www.ncbi.nlm.nih.gov/gene/27244) · UniProt [Q9Y6P5](https://www.uniprot.org/uniprotkb/Q9Y6P5) · Ensembl [ENSG00000080546](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080546)

## Data

Gene col 1283: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1283); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1283, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1283]; `tensor/DDL_lfc|DDL_z.npy` [1283]; `embed/gene_vectors.npy` [1283]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1283 or target_col == 1283). Every well: [[SESN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/SESN1.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
