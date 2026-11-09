---
symbol: "SCAF8"
type: "gene"
col: 13080
ensembl_id: "ENSG00000213079"
name: "SR-related CTD associated factor 8"
location: "6q25.2"
module: 51
arm: "+"
pooled_cpm: 186.42
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 15
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# SCAF8

*SR-related CTD associated factor 8* — 6q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.46× (z +16.9, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.386× (z -18.1, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFYC]] (+0.83, fdr 1e-05), [[SENP6]] (+0.76, fdr 7e-06), [[ZNF644]] (+0.75, fdr 1e-05); moves opposite to [[ZCCHC17]] (-0.63, fdr 6e-05), [[DNAJC5]] (-0.62, fdr 5e-05), [[QSOX1]] (-0.61, fdr 1e-04).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13080.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.46×** | +16.9 | 0e+00 | 48/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.06×** | +13.9 | 1e-41 | 48/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.94×** | +12.6 | 4e-34 | 48/48 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +12.6 | 4e-34 | 42/48 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +10.5 | 1e-23 | 44/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.68×** | +9.9 | 5e-21 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +8.8 | 1e-16 | 45/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.57×** | +8.3 | 1e-14 | 45/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +4.5 | 4e-04 | 28/47 (LoVo, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.24×** | +4.1 | 0.002 | 28/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.23×** | +4.0 | 0.003 | 32/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.21×** | +3.7 | 0.012 | 22/48 (A498, NCI-H460, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.064 | 26/49 (C-33 A, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.1 | 0.077 | 0/50 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13080.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.386×** | -18.1 | 0e+00 | 48/48 (AsPC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.391×** | -17.9 | 0e+00 | 48/49 (SNU-423, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.518×** | -17.7 | 0e+00 | 48/49 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.392×** | -17.2 | 0e+00 | 44/44 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.414×** | -16.8 | 0e+00 | 48/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.416×** | -16.7 | 0e+00 | 48/48 (AsPC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.497×** | -12.3 | 9e-33 | 42/45 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.588×** | -10.1 | 4e-22 | 47/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.600×** | -9.7 | 2e-20 | 48/48 (SK-MEL-2, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.642×** | -8.4 | 2e-15 | 46/48 (SW 1088, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.651×** | -7.9 | 2e-13 | 41/50 (A-172, NCI-H23, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.716×** | -6.1 | 4e-08 | 38/48 (SNU-423, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.845× | -4.5 | 2e-04 | 17/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.793×** | -4.4 | 4e-04 | 32/48 (SW 1271, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **0.786×** | -4.4 | 4e-04 | 28/47 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.663×** | -4.1 | 0.002 | 33/49 (AsPC-1, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13080. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 153 | 11 (2 ⚠) | 7 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.38× (z +18.0) | [[Panobinostat (drug)]] 0.5 µM 0.353× (z -15.3) |
| [[SW480 (line)]] | alt | 255 | 6 (1 ⚠) | 10 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 8.88× (z +18.9) | [[Dinaciclib (drug)]] 5 µM 0.313× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -16.6) |
| [[SW1417 (line)]] | alt | 224 | 6 (1 ⚠) | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.316× (z -17.8) |
| [[SNU-423 (line)]] | alt | 297 | 3 | 11 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -18.9) |
| [[LOX-IMVI (line)]] | wt | 260 | 4 | 9 (5 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.19× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -15.1) |
| [[PANC-1 (line)]] | alt | 229 | 6 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -18.0) |
| [[HOP62 (line)]] | alt | 180 | 2 | 10 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 5.93× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.349× (z -14.9) |
| [[HS-578T (line)]] | alt | 178 | 4 | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -13.8) |
| [[KATO III (line)]] | alt | 182 | 7 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.47× (z +17.0) | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.452× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 177 | 6 (1 ⚠) | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.71× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.373× (z -12.8) |
| [[NCI-H2347 (line)]] | alt | 142 | 3 | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.316× (z -15.8) |
| [[RPMI-7951 (line)]] | alt | 218 | 3 | 9 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.19× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.297× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -14.5) |
| [[AsPC-1 (line)]] | alt | 149 | 5 (1 ⚠) | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +16.9) | [[Panobinostat (drug)]] 5 µM 0.285× (z -18.2) |
| [[HEC-1-A (line)]] | alt | 208 | 5 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +14.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -16.3) |
| [[LoVo (line)]] | wt | 161 | 6 (2 ⚠) | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.03× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.421× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.473× (z -10.6) |
| [[LS 180 (line)]] | wt | 192 | 5 (1 ⚠) | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.66× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.405× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 192 | 2 | 9 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 5.45× (z +11.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.324× (z -14.4) ⚠ toxic; cell-cycle shift, explains ~47% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.355× (z -13.7) |
| [[SK-MEL-2 (line)]] | alt | 217 | 3 | 8 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.21× (z +14.7) | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.380× (z -13.0) |
| [[A-172 (line)]] | wt | 154 | 2 | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -19.7) |
| [[A498 (line)]] | wt | 110 | 5 (2 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +22.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -15.3) |
| [[NCI-H1573 (line)]] | alt | 157 | 5 (1 ⚠) | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.88× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.382× (z -11.5) |
| [[NCI-H2030 (line)]] | alt | 239 | 2 | 8 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 6.64× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -15.8) |
| [[RKO (line)]] | wt | 228 | 4 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +17.5) | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.414× (z -11.3) |
| [[A549 (line)]] | wt | 166 | 3 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +19.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -23.3) |
| [[C-33 A (line)]] | alt | 209 | 3 | 6 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.31× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.176× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.331× (z -13.2) |
| [[C32 (line)]] | wt | 210 | 3 | 6 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 11.2× (z +13.8) | [[Panobinostat (drug)]] 0.5 µM 0.333× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 123 | 2 | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.92× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.425× (z -11.2) |
| [[J82 (line)]] | alt | 167 | 2 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -13.7) |
| [[NCI-H23 (line)]] | alt | 175 | 1 | 8 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.97× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.0766× (z -33.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -13.9) |
| [[Panc 03.27 (line)]] | alt | 156 | 3 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.81× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.386× (z -11.7) |
| [[SW 900 (line)]] | alt | 168 | 3 | 6 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.83× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -13.1) |
| [[BT-474 (line)]] | alt | 106 | 6 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +11.3) | [[Panobinostat (drug)]] 0.5 µM 0.370× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 247 | 1 | 7 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.44× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.274× (z -15.4) |
| [[HT-29 (line)]] | alt | 169 | 2 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.39× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.382× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 154 | 2 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.32× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -11.6) |
| [[SNU-1 (line)]] | wt | 264 | 2 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.22× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -15.1) |
| [[SW48 (line)]] | wt | 208 | 3 | 5 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 5.43× (z +14.4) | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.309× (z -10.6) |
| [[A-427 (line)]] | wt | 187 | 3 | 4 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 6.10× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.240× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.473× (z -10.3) |
| [[CHP-212 (line)]] | wt | 188 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -10.8) |
| [[Hs 766T (line)]] | wt | 141 | 2 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.02× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.381× (z -11.5) |
| [[SHP-77 (line)]] | alt | 214 | 3 (1 ⚠) | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.63× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.429× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.606× (z -9.0) |
| [[H4 (line)]] | wt | 147 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.51× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -11.2) |
| [[COLO 205 (line)]] | alt | 116 | 2 | 3 | [[TAK-901 (drug)]] 5 µM 13.2× (z +14.2) | [[Belinostat (drug)]] 5 µM 0.376× (z -10.3) |
| [[AN3 CA (line)]] | alt | 276 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -9.8) |
| [[HCT15 (line)]] | alt | 191 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.72× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.377× (z -10.4) |
| [[SW 1271 (line)]] | alt | 241 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -10.2) |
| [[SW 1088 (line)]] | alt | 183 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.130× (z -10.7) |
| [[NCI-H661 (line)]] | alt | 258 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 200 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13080), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFYC]] | +0.83 | +0.54 / +0.81 | both halves | 1e-05 |  |
| [[SENP6]] | +0.76 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[ZNF644]] | +0.75 | +0.54 / +0.73 | both halves | 1e-05 |  |
| [[POGZ]] | +0.73 | +0.61 / +0.76 | both halves | 7e-06 | STRING 532 |
| [[ZFX]] | +0.71 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[EPC1]] | +0.70 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[SREK1]] | +0.69 | +0.57 / +0.64 | both halves | 9e-06 | same gene group |
| [[BRAF]] | +0.69 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[RNF115]] | +0.69 | +0.39 / +0.61 | both halves | 5e-05 |  |
| [[SRSF4]] | +0.69 | +0.58 / +0.60 | both halves | 7e-06 | same gene group |
| [[PUM2]] | +0.69 | +0.56 / +0.73 | both halves | 1e-05 | STRING 401 |
| [[WARS2]] | +0.69 | +0.45 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCCHC17]] | -0.63 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[DNAJC5]] | -0.62 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[QSOX1]] | -0.61 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[UBA6]] | -0.60 | -0.32 / -0.45 | both halves | 1e-04 |  |
| [[P4HB]] | -0.59 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[TPD52L2]] | -0.59 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[TPST2]] | -0.58 | -0.21 / -0.56 | both halves | 7e-04 |  |
| [[LMAN1]] | -0.58 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[GSDMB]] | -0.57 | -0.27 / -0.54 | both halves | 3e-04 |  |
| [[TMEM184B]] | -0.57 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[RECQL]] | -0.56 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[NGLY1]] | -0.56 | -0.35 / -0.51 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SCAF8's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF214]] | B | ZNF214 activity lowers SCAF8's level | lines that do not express ZNF214 (6) vs lines expressing it (44) | 1.14× higher at baseline in the lines without ZNF214 | 0.089 | ⚠ within organs, on part of the lines; also absent: S100A6, CDKN1A, PRRG1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.853). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-24.8, 12.5); signed map (12.2, -33.8). **Vector** length 80.1, 32.4% of its response variance represented; |z| ≥ 3 in 1,331 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.4 | +8.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | -17.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | -17.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | +5.4 | -4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | -2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | -1.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.1 | -1.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.0 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +13.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.4 | -9.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.5 | -8.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.6 | -10.1 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.9 | -0.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.8 | -16.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | +0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | +0.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | SR-related CTD associated factor 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.2 — chr6:154,733,378-154,834,244 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1116; previously RBM16 |
| Gene groups (HGNC) | RNA binding motif containing; CTD interacting domain containing |
| Hallmark sets | UV_RESPONSE_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPN6](https://www.uniprot.org/uniprotkb/Q9UPN6) (SR-related and CTD-associated factor 8):

> Anti-terminator protein required to prevent early mRNA termination during transcription. Together with SCAF4, acts by suppressing the use of early, alternative poly(A) sites, thereby preventing the accumulation of non-functional truncated proteins. Mechanistically, associates with the phosphorylated C-terminal heptapeptide repeat domain (CTD) of the largest RNA polymerase II subunit (POLR2A), and subsequently binds nascent RNA upstream of early polyadenylation sites to prevent premature mRNA …

**Summary**, from NCBI Gene [22828](https://www.ncbi.nlm.nih.gov/gene/22828):

> Enables RNA binding activity and RNA polymerase II C-terminal domain phosphoserine binding activity. Involved in negative regulation of termination of RNA polymerase II transcription, poly(A)-coupled and positive regulation of DNA-templated transcription, elongation. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20959](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20959) · Entrez [22828](https://www.ncbi.nlm.nih.gov/gene/22828) · UniProt [Q9UPN6](https://www.uniprot.org/uniprotkb/Q9UPN6) · Ensembl [ENSG00000213079](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213079)

## Data

Gene col 13080: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13080); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13080, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13080]; `tensor/DDL_lfc|DDL_z.npy` [13080]; `embed/gene_vectors.npy` [13080]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13080 or target_col == 13080). Every well: [[SCAF8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCAF8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
