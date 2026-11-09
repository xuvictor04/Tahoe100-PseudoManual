---
symbol: "TBK1"
type: "gene"
col: 11445
ensembl_id: "ENSG00000183735"
name: "TANK binding kinase 1"
location: "12q14.2"
module: 72
arm: "+"
pooled_cpm: 138.85
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 8
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# TBK1

*TANK binding kinase 1* — 12q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.01× (z +17.4, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.381× (z -24.1, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.642× (z -11.1, q 3e-26, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMA1]] (+0.57, fdr 3e-05), [[PSMA6]] (+0.56, fdr 2e-05), [[METTL16]] (+0.55, fdr 4e-05); moves opposite to [[PLEC]] (-0.55, fdr 2e-05), [[AHNAK]] (-0.51, fdr 2e-05), [[NAB1]] (-0.50, fdr 3e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11445.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.01×** | +17.4 | 0e+00 | 48/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.90×** | +16.0 | 0e+00 | 47/48 (SW480, LS 180, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.29×** | +15.5 | 0e+00 | 46/49 (HOP62, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.88×** | +14.9 | 0e+00 | 45/48 (LOX-IMVI, SW480, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +9.3 | 2e-18 | 36/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +8.7 | 3e-16 | 32/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +7.7 | 1e-12 | 27/38 (SNU-423, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +7.5 | 3e-12 | 32/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.49×** | +7.1 | 9e-11 | 41/49 (LOX-IMVI, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.71×** | +7.0 | 1e-10 | 35/48 (A-172, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +6.7 | 9e-10 | 33/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.22×** | +5.1 | 2e-05 | 26/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.38×** | +4.2 | 0.001 | 22/45 (SNU-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.002 | 22/48 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Hexylresorcinol (drug)]] 5 µM |  | 1.11× | +3.7 | 0.007 | 2/49 (HOP62, CHP-212) | rises with dose | position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.007 | 18/48 (NCI-H460, NCI-H2030, …) | two highest doses | noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.012 | 17/48 (NCI-H2030, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.09× | +3.1 | 0.050 | 9/49 (SNU-1, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11445.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.381×** | -24.1 | 0e+00 | 46/49 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.381×** | -23.2 | 0e+00 | 44/44 (A-427, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.642×** | -11.1 | 3e-26 | 42/48 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.884× | -10.8 | 7e-25 | 2/50 (NCI-H23, SW 1088) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.663×** | -10.3 | 1e-22 | 41/48 (BT-474, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.763×** | -6.7 | 1e-09 | 36/48 (LoVo, SW 900, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.766×** | -6.6 | 2e-09 | 32/48 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.770×** | -6.0 | 1e-07 | 26/45 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~13% of this change | **0.832×** | -4.6 | 3e-04 | 23/48 (A-427, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.896× | -3.9 | 0.006 | 17/49 (A549, J82, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.858× | -3.7 | 0.013 | 16/48 (C32, COLO 205, …) | rises with dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | 0.868× | -3.5 | 0.018 | 17/48 (NCI-H23, NCI-H1792, …) | rises with dose |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.905× | -3.5 | 0.018 | 3/48 (SHP-77, RPMI-7951, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.874× | -3.4 | 0.031 | 15/48 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.911× | -3.3 | 0.038 | 5/49 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.863× | -3.3 | 0.038 | 15/48 (HCT15, A498, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.915× | -3.2 | 0.054 | 6/49 (COLO 205, LoVo, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.844× | -3.0 | 0.076 | 18/47 (CHP-212, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11445. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 184 | 7 (2 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.273× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.534× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 165 | 8 (3 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.40× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -16.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 192 | 4 (1 ⚠) | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.30× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.431× (z -11.6) |
| [[A-427 (line)]] | wt | 303 | 2 | 6 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.95× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.0838× (z -39.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.497× (z -11.5) |
| [[NCI-H2030 (line)]] | alt | 163 | 4 (2 ⚠) | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.13× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.239× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.546× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 233 | 6 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.82× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -24.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 163 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -16.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 77.2 | 3 | 4 (4 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.67× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.302× (z -15.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 113 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.47× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -10.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 104 | 3 | 4 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.59× (z +18.4) | [[Dinaciclib (drug)]] 5 µM 0.400× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.573× (z -10.9) |
| [[A549 (line)]] | wt | 240 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.73× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.437× (z -10.4) |
| [[KATO III (line)]] | alt | 99.1 | 4 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.50× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.357× (z -14.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 105 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.66× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -10.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 104 | 5 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.02× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.438× (z -10.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 97.9 | 4 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.01× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.470× (z -9.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 96.5 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 11.1× (z +14.3) | — |
| [[J82 (line)]] | alt | 152 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.52× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -17.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 142 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.11× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.441× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 111 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.29× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.279× (z -16.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 149 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.21× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.382× (z -14.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 141 | 1 | 4 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.29× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.179× (z -22.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 220 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0927× (z -22.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 80.3 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.98× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.369× (z -9.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 146 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.91× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -13.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 156 | 2 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.89× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.225× (z -19.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 126 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.70× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -16.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 155 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.23× (z +8.7) | [[Harringtonine (drug)]] 5 µM 0.386× (z -10.0) ⚠ cell-cycle shift, explains ~17% of this change |
| [[H4 (line)]] | wt | 116 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.82× (z +9.7) | — |
| [[HCT15 (line)]] | alt | 119 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.75× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -15.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 147 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.23× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -13.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 128 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.58× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 177 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.18× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.201× (z -18.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 130 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.03× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -11.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 134 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -19.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 93.8 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.42× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.453× (z -8.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 99.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.30× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.342× (z -11.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 177 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -13.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 120 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.354× (z -10.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 123 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0813× (z -28.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 200 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.84× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -13.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 125 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.11× (z +11.3) | — |
| [[AN3 CA (line)]] | alt | 212 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 72.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -12.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 120 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 93.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.436× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 195 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11445), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMA1]] | +0.57 | +0.58 / +0.44 | both halves | 3e-05 | pathway: Interleukin-1 family signaling |
| [[PSMA6]] | +0.56 | +0.59 / +0.47 | both halves | 2e-05 | pathway: Interleukin-1 family signaling |
| [[METTL16]] | +0.55 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[TMEM161A]] | +0.54 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[PHTF1]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[DIPK1A]] | +0.53 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[MRPS15]] | +0.52 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[SMIM10L1]] | +0.52 | +0.43 / +0.41 | both halves | 4e-05 |  |
| [[ECSIT]] | +0.52 | +0.50 / +0.42 | both halves | 4e-05 | pathway: HALLMARK_PI3K_AKT_MTOR_SIGNALING |
| [[PSMB4]] | +0.52 | +0.54 / +0.36 | both halves | 9e-05 | pathway: Interleukin-1 family signaling |
| [[COA6]] | +0.51 | +0.43 / +0.39 | both halves | 5e-05 |  |
| [[ORC2]] | +0.51 | +0.46 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEC]] | -0.55 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[AHNAK]] | -0.51 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[NAB1]] | -0.50 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[MYO1C]] | -0.49 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[RSC1A1]] | -0.47 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[ARHGAP23]] | -0.45 | -0.41 / -0.40 | both halves | 4e-05 |  |
| [[PNPLA2]] | -0.45 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[PLXNA3]] | -0.45 | -0.46 / -0.32 | both halves | 1e-04 |  |
| [[ARHGDIA]] | -0.45 | -0.44 / -0.35 | both halves | 1e-04 | pathway: HALLMARK_PI3K_AKT_MTOR_SIGNALING |
| [[ARHGAP39]] | -0.45 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[CLIC1]] | -0.45 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[LASP1]] | -0.43 | -0.39 / -0.47 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises TBK1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.524). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.0, -10.2); signed map (-25.4, -23.8). **Vector** length 108, 34.8% of its response variance represented; |z| ≥ 3 in 1,276 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +9.4 | +17.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.8 | +14.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.5 | +16.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +7.0 | +2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | +5.3 | +3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.5 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +0.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.9 | +2.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.3 | +0.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -1.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -5.5 | -3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.9 | +0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.2 | -23.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.7 | -6.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.4 | -3.2 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.4 | -0.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.1 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | TANK binding kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.2 — chr12:64,452,090-64,502,114 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NAK |
| Gene groups (HGNC) | I kappa B kinase family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, MTORC1_SIGNALING |
| Reactome | 43 pathways, smallest: IRF3 mediated activation of type 1 IFN; STAT6-mediated induction of chemokines; IRF3-mediated induction of type I IFN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHD2](https://www.uniprot.org/uniprotkb/Q9UHD2) (Serine/threonine-protein kinase TBK1):

> Serine/threonine kinase that plays an essential role in regulating inflammatory responses to foreign agents. Following activation of toll-like receptors by viral or bacterial components, associates with TRAF3 and TANK and phosphorylates interferon regulatory factors (IRFs) IRF3 and IRF7 as well as DDX3X. This activity allows subsequent homodimerization and nuclear translocation of the IRFs leading to transcriptional activation of pro-inflammatory and antiviral genes including IFNA and IFNB. In …

**Summary**, from NCBI Gene [29110](https://www.ncbi.nlm.nih.gov/gene/29110):

> The NF-kappa-B (NFKB) complex of proteins is inhibited by I-kappa-B (IKB) proteins, which inactivate NFKB by trapping it in the cytoplasm. Phosphorylation of serine residues on the IKB proteins by IKB kinases marks them for destruction via the ubiquitination pathway, thereby allowing activation and nuclear translocation of the NFKB complex. The protein encoded by this gene is similar to IKB kinases and can mediate NFKB activation in response to certain growth factors. The protein is also an …

**Accessions** — [HGNC:11584](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11584) · Entrez [29110](https://www.ncbi.nlm.nih.gov/gene/29110) · UniProt [Q9UHD2](https://www.uniprot.org/uniprotkb/Q9UHD2) · Ensembl [ENSG00000183735](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183735)

## Data

Gene col 11445: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11445); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11445, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11445]; `tensor/DDL_lfc|DDL_z.npy` [11445]; `embed/gene_vectors.npy` [11445]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11445 or target_col == 11445). Every well: [[TBK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
