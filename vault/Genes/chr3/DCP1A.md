---
symbol: "DCP1A"
type: "gene"
col: 15749
ensembl_id: "ENSG00000272886"
name: "decapping mRNA 1A"
location: "3p21.1"
module: 12
arm: "+"
pooled_cpm: 121.66
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# DCP1A

*decapping mRNA 1A* — 3p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.74× (z +16.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.273× (z -37.2, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.591× (z -15.7, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PI4KB]] (+0.76, fdr 7e-06), [[MRPS18C]] (+0.71, fdr 1e-05), [[TRAPPC2B]] (+0.70, fdr 7e-06); moves opposite to [[ARHGAP4]] (-0.66, fdr 1e-05), [[AHCY]] (-0.62, fdr 1e-05), [[ITPR3]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15749.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.74×** | +16.6 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.62×** | +15.1 | 0e+00 | 45/49 (SW480, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.37×** | +13.3 | 8e-38 | 30/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +11.7 | 2e-29 | 36/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +10.9 | 2e-25 | 33/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +10.6 | 5e-24 | 33/48 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +9.7 | 4e-20 | 39/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +9.2 | 2e-18 | 35/48 (SW480, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.34×** | +8.8 | 1e-16 | 30/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +8.7 | 2e-16 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +6.3 | 2e-08 | 28/48 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.23×** | +6.2 | 2e-08 | 24/48 (NCI-H460, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.20× | +5.4 | 3e-06 | 21/48 (SW480, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.19× | +5.3 | 4e-06 | 21/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.17× | +4.5 | 2e-04 | 21/47 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.14× | +3.8 | 0.005 | 19/48 (SW480, SNU-1, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.08× | +3.2 | 0.036 | 1/48 (Hs 766T) | top dose only |  |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 1.07× | +3.1 | 0.064 | 0/48 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15749.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.273×** | -37.2 | 0e+00 | 43/44 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.342×** | -32.0 | 0e+00 | 49/49 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.468×** | -20.9 | 0e+00 | 43/45 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.591×** | -15.7 | 0e+00 | 46/48 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.618×** | -14.3 | 2e-44 | 45/48 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.748×** | -12.2 | 3e-32 | 37/49 (CHP-212, A549, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.690×** | -11.0 | 2e-26 | 41/48 (RPMI-7951, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.782×** | -10.4 | 2e-23 | 35/48 (LOX-IMVI, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.707×** | -10.3 | 3e-23 | 41/48 (RPMI-7951, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.797×** | -6.5 | 5e-09 | 26/50 (A-172, SNU-423, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.805×** | -6.2 | 3e-08 | 25/48 (MIA PaCa-2, NCI-H1792, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.819×** | -6.0 | 1e-07 | 26/48 (HOP62, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.688×** | -5.8 | 2e-07 | 32/49 (CFPAC-1, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.842× | -4.9 | 4e-05 | 22/48 (SNU-423, A-172, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.873× | -4.0 | 0.002 | 15/48 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.881× | -3.8 | 0.005 | 10/48 (A549, SNU-423, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.845× | -3.6 | 0.010 | 17/47 (RKO, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.889× | -3.5 | 0.013 | 11/48 (MIA PaCa-2, COLO 205, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.896× | -3.2 | 0.027 | 8/48 (A549, SW 1088, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 0.899× | -3.2 | 0.037 | 3/48 (NCI-H1792, SW 900, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.902× | -3.1 | 0.048 | 9/48 (LoVo, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15749. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 103 | 12 (7 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.87× (z +23.6) | [[Dinaciclib (drug)]] 5 µM 0.119× (z -35.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 81.4 | 8 (3 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +24.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.333× (z -17.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 134 | 7 (3 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +18.0) | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.620× (z -9.6) |
| [[A-172 (line)]] | wt | 114 | 1 (1 ⚠) | 7 (5 ⚠) | [[Harringtonine (drug)]] 0.5 µM 1.77× (z +8.8) ⚠ cell-cycle shift, explains ~8% of this change | [[Dinaciclib (drug)]] 5 µM 0.193× (z -24.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -14.8) |
| [[LOX-IMVI (line)]] | wt | 125 | 1 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +11.7) ⚠ cell-cycle shift, explains ~25% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.587× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 171 | 2 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.82× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.161× (z -25.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.456× (z -11.4) |
| [[A498 (line)]] | wt | 116 | 2 (1 ⚠) | 5 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 1.84× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.606× (z -11.6) |
| [[A549 (line)]] | wt | 108 | 2 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +14.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.04× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.261× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -14.8) |
| [[HEC-1-A (line)]] | alt | 145 | 3 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +9.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.34× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.210× (z -21.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 137 | 1 | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.224× (z -22.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.422× (z -13.6) |
| [[CFPAC-1 (line)]] | alt | 101 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.422× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 112 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +14.0) | [[Dinaciclib (drug)]] 0.05 µM 0.406× (z -10.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 136 | 1 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.0) ⚠ cell-cycle shift, explains ~25% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.616× (z -9.8) |
| [[LoVo (line)]] | wt | 161 | 3 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.215× (z -24.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.595× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 114 | 3 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.27× (z +12.0) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.09× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -13.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 134 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -27.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -12.3) |
| [[SW 900 (line)]] | alt | 143 | 1 | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.431× (z -11.5) |
| [[LS 180 (line)]] | wt | 144 | 2 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -18.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 88.1 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.491× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 138 | 2 | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.18× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.0498× (z -41.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.528× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 134 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.5) ⚠ cell-cycle shift, explains ~25% of this change | [[Dinaciclib (drug)]] 5 µM 0.261× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.560× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 182 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -30.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.567× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 145 | 2 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +14.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.97× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.0836× (z -33.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.510× (z -9.4) |
| [[SW48 (line)]] | wt | 123 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +11.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -16.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 68.2 | 2 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -12.1) |
| [[hTERT-HPNE (line)]] | wt | 134 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 134 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +13.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -15.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 122 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.10× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.147× (z -27.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 154 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.102× (z -24.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 98.0 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.90× (z +9.1) ⚠ cell-cycle shift, explains ~22% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -17.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 120 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -17.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 105 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.81× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.168× (z -25.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 107 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.466× (z -10.5) |
| [[C-33 A (line)]] | alt | 133 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -26.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 99.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -10.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 154 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -16.1) |
| [[H4 (line)]] | wt | 111 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -10.5) |
| [[HCT15 (line)]] | alt | 202 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -16.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 109 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.253× (z -15.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 82.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -12.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 166 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0647× (z -33.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 96.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.04× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 76.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -13.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 105 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15749), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PI4KB]] | +0.76 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[MRPS18C]] | +0.71 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[TRAPPC2B]] | +0.70 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[TTF1]] | +0.68 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[SLC4A1AP]] | +0.67 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[SNRPB2]] | +0.67 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[NKAPD1]] | +0.67 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[PIGBOS1]] | +0.67 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[GPBP1]] | +0.66 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[N4BP2L2]] | +0.66 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[MTRFR]] | +0.64 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[SYNRG]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP4]] | -0.66 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[AHCY]] | -0.62 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[ITPR3]] | -0.62 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[LINC03009]] | -0.61 | -0.39 / -0.57 | both halves | 6e-05 |  |
| [[RPSA]] | -0.60 | -0.45 / -0.58 | both halves | 3e-05 | pathway: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC); STRING 536 |
| [[PTPN18]] | -0.60 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[AKT1]] | -0.60 | -0.52 / -0.49 | both halves | 1e-05 | pathway: Butyrate Response Factor 1 (BRF1) binds and destabilizes mRNA |
| [[TFDP1]] | -0.58 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[RBBP7]] | -0.58 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[SMG1P3]] | -0.58 | -0.38 / -0.59 | both halves | 6e-05 |  |
| [[MAT2A]] | -0.57 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[TBCD]] | -0.57 | -0.39 / -0.56 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.659). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-41.4, -11.6); signed map (-8.9, -7.5). **Vector** length 96.7, 30.4% of its response variance represented; |z| ≥ 3 in 1,368 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.6 | +4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.8 | +13.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.6 | +10.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +3.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +0.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.0 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.9 | +0.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +0.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.3 | -20.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -10.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | +8.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.1 | -3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.8 | -32.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -6.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | decapping mRNA 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.1 — chr3:53,283,429-53,347,586 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSA275986, SMIF, SMAD4IP1 |
| Gene groups (HGNC) | RNA decapping and exonuclease complex subunits |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 8 pathways, smallest: mRNA decay by 5' to 3' exoribonuclease; Butyrate Response Factor 1 (BRF1) binds and destabilizes mRNA; Tristetraprolin (TTP, ZFP36) binds and destabilizes mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPI6](https://www.uniprot.org/uniprotkb/Q9NPI6) (mRNA-decapping enzyme 1A):

> Necessary for the degradation of mRNAs, both in normal mRNA turnover and in nonsense-mediated mRNA decay. Removes the 7-methyl guanine cap structure from mRNA molecules, yielding a 5'-phosphorylated mRNA fragment and 7m-GDP. Contributes to the transactivation of target genes after stimulation by TGFB1. Essential for embryonic development.

**Summary**, from NCBI Gene [55802](https://www.ncbi.nlm.nih.gov/gene/55802):

> Decapping is a key step in general and regulated mRNA decay. The protein encoded by this gene is a decapping enzyme. This protein and another decapping enzyme form a decapping complex, which interacts with the nonsense-mediated decay factor hUpf1 and may be recruited to mRNAs containing premature termination codons. This protein also participates in the TGF-beta signaling pathway. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Feb 2014]

**Accessions** — [HGNC:18714](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18714) · Entrez [55802](https://www.ncbi.nlm.nih.gov/gene/55802) · UniProt [Q9NPI6](https://www.uniprot.org/uniprotkb/Q9NPI6) · Ensembl [ENSG00000272886](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000272886)

## Data

Gene col 15749: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15749); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15749, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15749]; `tensor/DDL_lfc|DDL_z.npy` [15749]; `embed/gene_vectors.npy` [15749]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15749 or target_col == 15749). Every well: [[DCP1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCP1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
