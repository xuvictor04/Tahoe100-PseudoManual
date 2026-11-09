---
symbol: "RAF1"
type: "gene"
col: 5279
ensembl_id: "ENSG00000132155"
name: "Raf-1 proto-oncogene, serine/threonine kinase"
location: "3p25.2"
module: 46
arm: "+"
pooled_cpm: 98.79
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 13
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# RAF1

*Raf-1 proto-oncogene, serine/threonine kinase* — 3p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.91× (z +19.1, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.393× (z -17.7, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DYRK1A]] (+0.76, fdr 7e-06), [[TLK2]] (+0.69, fdr 7e-06), [[WTAP]] (+0.68, fdr 7e-06); moves opposite to [[LRRFIP1]] (-0.60, fdr 4e-05), [[R3HDM4]] (-0.59, fdr 1e-04), [[SEPTIN10]] (-0.59, fdr 4e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Bendamustine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5279.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.91×** | +19.1 | 0e+00 | 49/49 (SW480, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.73×** | +19.0 | 0e+00 | 48/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.50×** | +17.4 | 0e+00 | 48/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **4.41×** | +14.7 | 0e+00 | 48/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.05×** | +13.6 | 6e-40 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.95×** | +12.7 | 8e-35 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +11.5 | 6e-29 | 40/48 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +8.5 | 1e-15 | 37/48 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +8.1 | 4e-14 | 35/47 (LoVo, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.46×** | +7.2 | 4e-11 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +4.9 | 4e-05 | 30/48 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.29×** | +4.8 | 9e-05 | 27/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +4.5 | 2e-04 | 28/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.018 | 18/49 (NCI-H460, A-172, …) | top dose only | plate-row cell shift |
| [[Tomivosertib (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.022 | 19/48 (NCI-H2030, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Asciminib (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.064 | 15/48 (SW480, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5279.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.393×** | -17.7 | 0e+00 | 48/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.416×** | -16.7 | 0e+00 | 48/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.469×** | -14.4 | 2e-44 | 45/49 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.476×** | -13.5 | 1e-39 | 39/44 (SHP-77, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.507×** | -12.9 | 5e-36 | 47/48 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.616×** | -9.2 | 3e-18 | 44/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.636×** | -8.0 | 1e-13 | 29/45 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.772×** | -7.0 | 2e-10 | 33/48 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.778×** | -4.8 | 1e-04 | 26/48 (HepG2/C3A, SW 900, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.778×** | -4.8 | 1e-04 | 25/48 (SW 900, SNU-423, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.797×** | -4.3 | 8e-04 | 26/49 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.670×** | -4.0 | 0.003 | 24/49 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.826×** | -3.6 | 0.012 | 19/48 (HEC-1-A, NCI-H1573, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.844× | -3.2 | 0.049 | 17/48 (RPMI-7951, AsPC-1, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.852× | -3.1 | 0.083 | 15/47 (LS 180, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5279. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 89.0 | 9 (1 ⚠) | 8 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 12.0× (z +23.8) | [[Panobinostat (drug)]] 5 µM 0.380× (z -17.7) |
| [[NCI-H460 (line)]] | wt | 77.3 | 12 (3 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.96× (z +23.0) | [[Panobinostat (drug)]] 0.5 µM 0.420× (z -11.2) |
| [[HOP62 (line)]] | alt | 120 | 6 (1 ⚠) | 6 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.86× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.82× (z +12.7) | [[Panobinostat (drug)]] 0.5 µM 0.292× (z -15.7) |
| [[NCI-H2347 (line)]] | alt | 222 | 3 | 8 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.50× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.296× (z -15.9) |
| [[SW 900 (line)]] | alt | 138 | 4 (1 ⚠) | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.95× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.262× (z -14.3) |
| [[SW1417 (line)]] | alt | 153 | 5 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +13.4) | [[Panobinostat (drug)]] 5 µM 0.285× (z -14.0) |
| [[PANC-1 (line)]] | alt | 63.8 | 7 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.67× (z +21.3) | [[Panobinostat (drug)]] 5 µM 0.387× (z -13.0) |
| [[BT-474 (line)]] | alt | 102 | 8 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 9.63× (z +13.9) | [[Panobinostat (drug)]] 0.5 µM 0.430× (z -9.9) |
| [[KATO III (line)]] | alt | 68.4 | 6 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.27× (z +20.2) | [[Panobinostat (drug)]] 5 µM 0.386× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 147 | 4 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.240× (z -14.4) |
| [[NCI-H1573 (line)]] | alt | 56.1 | 6 (1 ⚠) | 3 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.92× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.67× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.377× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 87.9 | 7 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.0863× (z -29.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 109 | 3 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +13.2) | [[Panobinostat (drug)]] 5 µM 0.380× (z -12.6) |
| [[NCI-H1792 (line)]] | alt | 139 | 5 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.99× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.398× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 88.4 | 4 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.11× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.262× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.308× (z -14.3) |
| [[A549 (line)]] | wt | 102 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +19.5) | [[Panobinostat (drug)]] 0.5 µM 0.317× (z -13.7) |
| [[LoVo (line)]] | wt | 76.0 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.12× (z +23.9) | — |
| [[SW48 (line)]] | wt | 103 | 5 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 6.78× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.188× (z -12.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 107 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.344× (z -13.4) |
| [[A-427 (line)]] | wt | 104 | 3 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.58× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.494× (z -8.8) |
| [[H4 (line)]] | wt | 97.4 | 5 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.98× (z +11.8) | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 138 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -13.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 103 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.63× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.234× (z -11.9) |
| [[HT-29 (line)]] | alt | 54.6 | 3 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.273× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.372× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 119 | 3 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 10.5× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -12.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 95.2 | 2 | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.325× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 69.3 | 3 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.61× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.321× (z -9.6) |
| [[C32 (line)]] | wt | 100 | 2 | 3 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 15.0× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.399× (z -9.1) |
| [[COLO 205 (line)]] | alt | 67.4 | 3 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 24.6× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.345× (z -9.1) |
| [[RKO (line)]] | wt | 107 | 4 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.1× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -14.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 126 | 2 (1 ⚠) | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.20× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.327× (z -11.0) |
| [[SHP-77 (line)]] | alt | 100 | 3 (1 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.61× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.0764× (z -26.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.381× (z -10.5) |
| [[SNU-1 (line)]] | wt | 126 | 3 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 11.9× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.102× (z -18.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 63.8 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +14.4) | [[Panobinostat (drug)]] 0.5 µM 0.341× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 58.3 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.72× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.326× (z -11.0) |
| [[HS-578T (line)]] | alt | 95.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.331× (z -9.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 79.3 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.96× (z +14.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 70.4 | 3 | 1 | [[TAK-901 (drug)]] 5 µM 11.5× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.390× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 121 | 2 | 2 | [[TAK-901 (drug)]] 5 µM 8.70× (z +13.2) | [[Panobinostat (drug)]] 0.5 µM 0.420× (z -10.2) |
| [[C-33 A (line)]] | alt | 128 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 6.19× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.388× (z -9.8) |
| [[Hs 766T (line)]] | wt | 59.4 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 11.8× (z +12.7) | — |
| [[AN3 CA (line)]] | alt | 155 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0555× (z -21.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 112 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.92× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -12.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 70.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 153 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5279), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYRK1A]] | +0.76 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[TLK2]] | +0.69 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[WTAP]] | +0.68 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[SIAH1]] | +0.68 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[RPRD2]] | +0.68 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[C14orf93]] | +0.68 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[ZNF362]] | +0.67 | +0.49 / +0.49 | both halves | 2e-05 |  |
| [[ACOT2]] | +0.67 | +0.34 / +0.53 | both halves | 1e-04 |  |
| [[RPRD1B]] | +0.66 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[C2orf42]] | +0.65 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[ZCCHC8]] | +0.65 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[WDFY3]] | +0.65 | +0.53 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRFIP1]] | -0.60 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[R3HDM4]] | -0.59 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[SEPTIN10]] | -0.59 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[EHD4]] | -0.58 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[STK4]] | -0.57 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[CMIP]] | -0.57 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[KCTD20]] | -0.57 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[CAP1]] | -0.56 | -0.34 / -0.43 | both halves | 1e-04 | pathway: Platelet activation, signaling and aggregation |
| [[PAQR5]] | -0.55 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[ITGA2]] | -0.55 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[EFL1]] | -0.55 | -0.45 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises RAF1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises RAF1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Bendamustine (drug)]] 0.5 µM | C | RAF1's natural level raises the cells' numbers under Bendamustine 0.5 µM (protects the cells) | RAF1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.59 | 0.484 over the table, 0.087 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.796). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-4.7, 14.9); signed map (28.4, -23.4). **Vector** length 85.9, 30.2% of its response variance represented; |z| ≥ 3 in 1,294 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +9.7 | +1.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.3 | +1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.1 | -0.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | -1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.8 | +0.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.7 | +1.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.6 | +0.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.6 | -17.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.4 | -12.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -4.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.0 | -9.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.6 | -16.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.3 | +1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -7.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | Raf-1 proto-oncogene, serine/threonine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.2 — chr3:12,582,101-12,664,201 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Raf-1, c-Raf, CRAF |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinase kinases; RAF family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, INFLAMMATORY_RESPONSE, COMPLEMENT |
| Reactome | 34 pathways, smallest: Negative feedback regulation of MAPK pathway; GP1b-IX-V activation signalling; IFNG signaling activates MAPKs |
| Matched by | ensembl_id |

**Function**, from UniProt [P04049](https://www.uniprot.org/uniprotkb/P04049) (RAF proto-oncogene serine/threonine-protein kinase):

> Serine/threonine-protein kinase that acts as a regulatory link between the membrane-associated Ras GTPases and the MAPK/ERK cascade, and this critical regulatory link functions as a switch determining cell fate decisions including proliferation, differentiation, apoptosis, survival and oncogenic transformation. RAF1 activation initiates a mitogen-activated protein kinase (MAPK) cascade that comprises a sequential phosphorylation of the dual-specific MAPK kinases (MAP2K1/MEK1 and MAP2K2/MEK2) …

**Summary**, from NCBI Gene [5894](https://www.ncbi.nlm.nih.gov/gene/5894):

> This gene is the cellular homolog of viral raf gene (v-raf). The encoded protein is a MAP kinase kinase kinase (MAP3K), which functions downstream of the Ras family of membrane associated GTPases to which it binds directly. Once activated, the cellular RAF1 protein can phosphorylate to activate the dual specificity protein kinases MEK1 and MEK2, which in turn phosphorylate to activate the serine/threonine specific protein kinases, ERK1 and ERK2. Activated ERKs are pleiotropic effectors of cell …

**Accessions** — [HGNC:9829](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9829) · Entrez [5894](https://www.ncbi.nlm.nih.gov/gene/5894) · UniProt [P04049](https://www.uniprot.org/uniprotkb/P04049) · Ensembl [ENSG00000132155](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132155)

## Data

Gene col 5279: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5279); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5279, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5279]; `tensor/DDL_lfc|DDL_z.npy` [5279]; `embed/gene_vectors.npy` [5279]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5279 or target_col == 5279). Every well: [[RAF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
