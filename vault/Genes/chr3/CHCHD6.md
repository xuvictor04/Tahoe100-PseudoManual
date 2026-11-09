---
symbol: "CHCHD6"
type: "gene"
col: 8268
ensembl_id: "ENSG00000159685"
name: "coiled-coil-helix-coiled-coil-helix domain containing 6"
location: "3q21.3"
module: 36
arm: "+"
pooled_cpm: 42.59
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 15
n_dd_up_clean: 9
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# CHCHD6

*coiled-coil-helix-coiled-coil-helix domain containing 6* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.65× (z +8.0, q 1e-12, up in 33 of 47 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.48× (z +6.9, q 1e-09, up in 31 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.430× (z -21.0, q 0e+00, down in 39 of 47 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.536× (z -15.5, q 0e+00, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DIS3L2]] (+0.76, fdr 7e-06), [[CDIN1]] (+0.74, fdr 7e-06), [[HERC2]] (+0.74, fdr 7e-06); moves opposite to [[FAM117A]] (-0.70, fdr 1e-05), [[ABCA5]] (-0.66, fdr 7e-06), [[HLA-A]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[GNAZ]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8268.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.65×** | +8.0 | 1e-12 | 33/47 (HS-578T, HOP62, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +6.9 | 1e-09 | 31/46 (NCI-H2347, HOP62, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.48×** | +6.8 | 1e-09 | 33/47 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.48×** | +6.8 | 1e-09 | 30/46 (HOP62, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.06×** | +6.6 | 3e-09 | 27/47 (RKO, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +5.9 | 4e-07 | 27/47 (NCI-H2347, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.85×** | +5.7 | 1e-06 | 26/41 (NCI-H460, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.73×** | +5.1 | 3e-05 | 21/47 (HEC-1-A, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +5.1 | 3e-05 | 23/47 (NCI-H2347, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +4.8 | 1e-04 | 29/47 (HOP62, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.33×** | +4.5 | 4e-04 | 22/46 (SW48, BT-474, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +4.3 | 7e-04 | 14/33 (NCI-H1573, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +4.3 | 7e-04 | 19/47 (NCI-H1792, LOX-IMVI, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.26×** | +4.0 | 0.002 | 19/47 (NCI-H2347, CFPAC-1, …) | all doses, flat | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.004 | 13/47 (NCI-H2347, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +3.1 | 0.060 | 14/46 (SNU-423, SHP-77, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8268.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.430×** | -21.0 | 0e+00 | 39/47 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.536×** | -15.5 | 0e+00 | 37/47 (J82, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.438×** | -14.0 | 2e-42 | 39/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.495×** | -12.4 | 4e-33 | 35/46 (C-33 A, SW1417, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.505×** | -12.1 | 2e-31 | 33/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.520×** | -11.1 | 1e-26 | 25/42 (NCI-H23, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.595×** | -8.8 | 1e-16 | 32/47 (J82, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.642×** | -7.8 | 4e-13 | 29/47 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.687×** | -6.4 | 1e-08 | 25/46 (J82, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.711×** | -6.0 | 9e-08 | 25/45 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.749×** | -5.1 | 2e-05 | 20/46 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.839× | -4.4 | 5e-04 | 18/47 (J82, A498, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.791×** | -4.1 | 0.001 | 21/47 (NCI-H460, BT-474, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.734×** | -3.9 | 0.004 | 20/47 (J82, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.877× | -3.3 | 0.039 | 12/47 (SNU-1, LS 180, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.775×** | -3.2 | 0.047 | 20/45 (A549, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.722×** | -3.0 | 0.086 | 15/46 (HEC-1-A, PANC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8268. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 96.6 | 0 | 13 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -23.5) |
| [[NCI-H460 (line)]] | wt | 35.2 | 1 (1 ⚠) | 11 (7 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.28× (z +8.9) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -27.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.230× (z -15.3) |
| [[MIA PaCa-2 (line)]] | alt | 57.3 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -15.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -10.1) |
| [[SW48 (line)]] | wt | 82.4 | 1 | 7 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.64× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -17.6) |
| [[RKO (line)]] | wt | 79.4 | 1 | 6 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 7.12× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -16.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -13.2) |
| [[PANC-1 (line)]] | alt | 48.0 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -33.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.186× (z -19.1) |
| [[C32 (line)]] | wt | 48.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -17.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -14.6) |
| [[LoVo (line)]] | wt | 43.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -20.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -11.5) |
| [[NCI-H2030 (line)]] | alt | 60.2 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -17.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -13.8) |
| [[SK-MEL-2 (line)]] | alt | 51.0 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0906× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.275× (z -10.1) |
| [[A-427 (line)]] | wt | 101 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0948× (z -23.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.342× (z -11.0) |
| [[A498 (line)]] | wt | 35.6 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -16.7) |
| [[C-33 A (line)]] | alt | 80.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change |
| [[HOP62 (line)]] | alt | 29.7 | 1 (1 ⚠) | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.71× (z +8.6) ⚠ cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -11.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -10.6) |
| [[HS-578T (line)]] | alt | 44.8 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 28.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -18.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -13.2) |
| [[SNU-1 (line)]] | wt | 105 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -11.9) |
| [[SW1417 (line)]] | alt | 49.4 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -13.2) |
| [[A-172 (line)]] | wt | 38.9 | 0 | 3 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -11.9) |
| [[BT-474 (line)]] | alt | 31.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -10.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.242× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 14.6 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.55× (z +9.4) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Belinostat (drug)]] 5 µM 4.40× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 67.8 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.68× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.566× (z -10.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 83.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0932× (z -24.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 16.4 | 3 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.95× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 75.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change |
| [[SW480 (line)]] | alt | 46.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -11.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.409× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 18.5 | 0 | 2 (1 ⚠) | — | [[Monocrotaline (drug)]] 0.05 µM 0.0773× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 32.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -16.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A549 (line)]] | wt | 25.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -11.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[AN3 CA (line)]] | alt | 61.7 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.121× (z -10.7) |
| [[COLO 205 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0939× (z -10.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 32.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -18.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[RPMI-7951 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -10.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[AsPC-1 (line)]] | alt | 8.23 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8268), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIS3L2]] | +0.76 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[CDIN1]] | +0.74 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[HERC2]] | +0.74 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[TSEN2]] | +0.73 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[ERI3]] | +0.73 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[CDC123]] | +0.73 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[ZNF496]] | +0.73 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[TCOF1]] | +0.73 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[MINDY4]] | +0.72 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[HERC2P9]] | +0.72 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[MRPS27]] | +0.72 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[VWA8]] | +0.72 | +0.72 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM117A]] | -0.70 | -0.75 / -0.57 | both halves | 1e-05 |  |
| [[ABCA5]] | -0.66 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[HLA-A]] | -0.65 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[RSRP1]] | -0.65 | -0.68 / -0.57 | both halves | 9e-06 |  |
| [[ATOSA]] | -0.63 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[HHLA3]] | -0.62 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[SGO1-AS1]] | -0.62 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[HMGCL]] | -0.62 | -0.65 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAZ]] | B | GNAZ activity raises CHCHD6's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.00× lower at baseline in the lines without GNAZ | 0.037 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[MVB12B]] | B | MVB12B activity raises CHCHD6's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 2.56× lower at baseline in the lines without MVB12B | 0.038 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[FAM78B]] | B | FAM78B activity raises CHCHD6's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.55× lower at baseline in the lines without FAM78B | 0.078 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[TOP2A]] | B | TOP2A activity raises CHCHD6's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ADCY3]] | B | ADCY3 activity raises CHCHD6's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.42× lower at baseline in the lines without ADCY3 | 0.096 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.806). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-9.2, -33.8); signed map (-12.7, -50.7). **Vector** length 129, 38.1% of its response variance represented; |z| ≥ 3 in 1,102 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +7.5 | +6.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | +6.6 | +8.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.5 | +6.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.3 | +6.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.4 | +4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.3 | +4.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.4 | +4.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +3.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -9.4 | -21.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -8.0 | -8.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.3 | -6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -15.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.5 | -14.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -4.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.9 | -2.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.5 | -3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil-helix-coiled-coil-helix domain containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:126,704,240-126,960,420 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC13016, PPP1R23, CHCM1, Mic25, MICOS25 |
| Gene groups (HGNC) | Coiled-coil-helix-coiled-coil-helix domain containing proteins; Protein phosphatase 1 regulatory subunits; Mitochondrial contact site and cristae organizing system subunits |
| Reactome | 3 pathways, smallest: Cristae formation; Mitochondrial biogenesis; Organelle biogenesis and maintenance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRQ6](https://www.uniprot.org/uniprotkb/Q9BRQ6) (MICOS complex subunit MIC25):

> Component of the MICOS complex, a large protein complex of the mitochondrial inner membrane that plays crucial roles in the maintenance of crista junctions, inner membrane architecture, and formation of contact sites to the outer membrane.

**Summary**, from NCBI Gene [84303](https://www.ncbi.nlm.nih.gov/gene/84303):

> Involved in DNA damage response and cristae formation. Located in mitochondrial inner membrane. Part of MICOS complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28184](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28184) · Entrez [84303](https://www.ncbi.nlm.nih.gov/gene/84303) · UniProt [Q9BRQ6](https://www.uniprot.org/uniprotkb/Q9BRQ6) · Ensembl [ENSG00000159685](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159685)

## Data

Gene col 8268: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8268); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8268, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8268]; `tensor/DDL_lfc|DDL_z.npy` [8268]; `embed/gene_vectors.npy` [8268]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8268 or target_col == 8268). Every well: [[CHCHD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHCHD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
