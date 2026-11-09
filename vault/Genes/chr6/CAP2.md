---
symbol: "CAP2"
type: "gene"
col: 3333
ensembl_id: "ENSG00000112186"
name: "cyclase associated actin cytoskeleton regulatory protein 2"
location: "6p22.3"
module: 64
arm: "+"
pooled_cpm: 47.1
n_lines_expressing: 43
n_dd_up: 20
n_dd_down: 24
n_dd_up_clean: 16
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# CAP2

*cyclase associated actin cytoskeleton regulatory protein 2* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 2.22× (z +15.2, q 0e+00, up in 29 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.267× (z -26.7, q 0e+00, down in 39 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAG2]] (+0.67, fdr 1e-05), [[PSMD11]] (+0.63, fdr 1e-05), [[TYW3]] (+0.62, fdr 1e-05); moves opposite to [[B3GAT3]] (-0.52, fdr 9e-05), [[FHIP1B]] (-0.51, fdr 1e-04), [[SH3GL1]] (-0.50, fdr 1e-04).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF618]] → it (grade B ⚠); 4 go from it, the strongest it → [[ZNF618]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3333.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **2.22×** | +15.2 | 0e+00 | 29/41 (NCI-H2347, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.91×** | +13.1 | 1e-36 | 28/40 (RKO, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.88×** | +12.7 | 2e-34 | 24/40 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +10.7 | 2e-24 | 26/39 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +10.1 | 5e-22 | 22/35 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.52×** | +9.7 | 2e-20 | 28/36 (RKO, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.53×** | +8.5 | 1e-15 | 24/41 (RKO, A498, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **2.01×** | +7.4 | 1e-11 | 28/39 (RKO, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +6.5 | 6e-09 | 21/39 (A498, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.52×** | +6.0 | 8e-08 | 21/41 (MIA PaCa-2, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.23×** | +5.8 | 3e-07 | 19/41 (HOP62, SNU-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +5.6 | 1e-06 | 26/40 (NCI-H23, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +5.3 | 6e-06 | 21/41 (RKO, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.8 | 7e-05 | 19/41 (HEC-1-A, C-33 A, …) | rises with dose | composition shift |
| [[Infigratinib (drug)]] 5 µM |  | **1.57×** | +4.8 | 8e-05 | 18/41 (RKO, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.24×** | +4.3 | 6e-04 | 16/41 (RKO, NCI-H23, …) | rises with dose |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.24×** | +4.1 | 0.001 | 15/40 (SW 900, HOP62, …) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 5 µM |  | **1.41×** | +3.6 | 0.010 | 8/41 (PANC-1, SNU-423, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.012 | 12/40 (HOP62, RKO, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.012 | 8/41 (LOX-IMVI, RKO, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3333.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.267×** | -26.7 | 0e+00 | 39/41 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.272×** | -26.3 | 0e+00 | 39/41 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.314×** | -23.4 | 0e+00 | 37/40 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.641×** | -12.7 | 1e-34 | 32/41 (NCI-H2030, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.605×** | -10.1 | 4e-22 | 31/40 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.618×** | -9.7 | 3e-20 | 32/41 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.646×** | -8.8 | 8e-17 | 26/40 (MIA PaCa-2, HCT15, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.706×** | -7.0 | 1e-10 | 26/41 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.711×** | -6.9 | 4e-10 | 25/41 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **0.739×** | -6.1 | 6e-08 | 24/39 (HCT15, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.748×** | -5.9 | 2e-07 | 24/40 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.774×** | -5.2 | 1e-05 | 19/41 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.771×** | -5.1 | 2e-05 | 23/40 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.621×** | -5.0 | 2e-05 | 21/41 (HEC-1-A, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.637×** | -4.8 | 7e-05 | 15/40 (PANC-1, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.799×** | -4.5 | 2e-04 | 17/41 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.811×** | -4.2 | 7e-04 | 13/40 (NCI-H2030, LoVo, …) | two highest doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.695×** | -3.8 | 0.004 | 16/40 (SW48, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.826×** | -3.7 | 0.006 | 14/40 (LOX-IMVI, NCI-H661, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.850× | -3.3 | 0.026 | 10/41 (NCI-H2030, PANC-1, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.809×** | -3.1 | 0.055 | 14/41 (SNU-423, Panc 03.27, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.862× | -3.0 | 0.062 | 15/40 (NCI-H2030, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3333. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 64.3 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -29.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -14.4) |
| [[NCI-H460 (line)]] | wt | 44.3 | 0 | 12 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.131× (z -21.0) |
| [[HEC-1-A (line)]] | alt | 102 | 3 (3 ⚠) | 8 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.132× (z -30.7) |
| [[MIA PaCa-2 (line)]] | alt | 77.9 | 3 | 7 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.15× (z +13.3) | [[Panobinostat (drug)]] 5 µM 0.157× (z -18.4) |
| [[PANC-1 (line)]] | alt | 69.5 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.267× (z -14.9) |
| [[A498 (line)]] | wt | 33.4 | 6 (2 ⚠) | 2 | [[Auranofin (drug)]] 5 µM 2.98× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.350× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 85.2 | 1 | 7 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.55× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.154× (z -17.9) |
| [[RKO (line)]] | wt | 47.6 | 4 | 4 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.54× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.168× (z -14.8) |
| [[HOP62 (line)]] | alt | 47.2 | 5 (1 ⚠) | 2 | [[Bortezomib (drug)]] 0.05 µM 3.57× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -15.1) |
| [[LoVo (line)]] | wt | 31.5 | 1 | 6 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.58× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.230× (z -13.8) |
| [[C-33 A (line)]] | alt | 82.4 | 2 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.159× (z -15.0) |
| [[C32 (line)]] | wt | 45.8 | 1 | 5 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.83× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -13.2) |
| [[J82 (line)]] | alt | 127 | 1 | 5 | [[Ixazomib citrate (drug)]] 5 µM 2.58× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.129× (z -19.3) |
| [[A549 (line)]] | wt | 54.6 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.114× (z -16.9) |
| [[LS 180 (line)]] | wt | 38.2 | 2 | 3 | [[Bortezomib (drug)]] 0.05 µM 4.05× (z +11.4) | [[Belinostat (drug)]] 5 µM 0.223× (z -13.0) |
| [[SNU-1 (line)]] | wt | 81.3 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.106× (z -19.5) |
| [[A-172 (line)]] | wt | 52.8 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -14.5) |
| [[AN3 CA (line)]] | alt | 140 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0820× (z -16.5) |
| [[NCI-H2347 (line)]] | alt | 18.6 | 4 | 0 | [[Bortezomib (drug)]] 0.05 µM 7.52× (z +13.5) | — |
| [[SNU-423 (line)]] | alt | 73.4 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.297× (z -11.9) |
| [[SW1417 (line)]] | alt | 37.9 | 1 | 3 | [[Auranofin (drug)]] 5 µM 2.93× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.264× (z -11.6) |
| [[SW48 (line)]] | wt | 47.7 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.123× (z -12.5) |
| [[A-427 (line)]] | wt | 65.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.199× (z -15.2) |
| [[HepG2_C3A (line)]] | wt | 82.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.226× (z -12.2) |
| [[HS-578T (line)]] | alt | 52.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.155× (z -15.1) |
| [[NCI-H2030 (line)]] | alt | 76.9 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -14.7) |
| [[SW480 (line)]] | alt | 26.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.183× (z -15.2) |
| [[BT-474 (line)]] | alt | 158 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.104× (z -17.3) |
| [[HCT15 (line)]] | alt | 41.9 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.169× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 39.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.304× (z -8.8) |
| [[HT-29 (line)]] | alt | 11.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.59× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0730× (z -10.7) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 29.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.71× (z +8.8) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.63 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.03 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.05 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 97.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.86 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3333), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAG2]] | +0.67 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[PSMD11]] | +0.63 | +0.51 / +0.57 | both halves | 1e-05 | pathway: Signaling by ROBO receptors |
| [[TYW3]] | +0.62 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[CUL5]] | +0.61 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[OSBPL1A]] | +0.60 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[IDE]] | +0.60 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[FECH]] | +0.60 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[NUDT9]] | +0.59 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[MTA3]] | +0.59 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[ALOX12P2-1]] | +0.58 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[SMIM10L1]] | +0.58 | +0.66 / +0.33 | both halves | 1e-04 |  |
| [[RHBDD3]] | +0.58 | +0.55 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GAT3]] | -0.52 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[FHIP1B]] | -0.51 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[SH3GL1]] | -0.50 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[MINK1]] | -0.49 | -0.45 / -0.37 | both halves | 9e-05 |  |
| [[TAF5]] | -0.49 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[WIPF2]] | -0.48 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[TXNDC17]] | -0.48 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[MCRIP1]] | -0.48 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[MGAT1]] | -0.47 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[KMT5C]] | -0.47 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[DEPP1]] | -0.47 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[FRMD8]] | -0.47 | -0.49 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF618]] | B | ZNF618 activity raises CAP2's level | lines that do not express ZNF618 (9) vs lines expressing it (41) | 2.59× lower at baseline in the lines without ZNF618 | 0.068 | ⚠ within organs, on part of the lines; also absent: NCS1, MRAS, GPR63 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF618]] | B | CAP2 activity raises ZNF618's level | lines that do not express CAP2 (7) vs lines expressing it (43) | 3.78× lower at baseline in the lines without CAP2 | 0.065 | ⚠ within organs, on part of the lines; also absent: SCML2, ADORA1, ASAP3 |
| [[CCDC102A]] | B | CAP2 activity raises CCDC102A's level | lines that do not express CAP2 (7) vs lines expressing it (43) | 2.08× lower at baseline in the lines without CAP2 | 0.071 | ⚠ within organs, on part of the lines; also absent: SCML2, ADORA1, ASAP3 |
| [[CUL5]] | B | CAP2 activity raises CUL5's level | lines that do not express CAP2 (7) vs lines expressing it (43) | 1.24× lower at baseline in the lines without CAP2 | 0.089 | ⚠ within organs, on part of the lines; also absent: SCML2, ADORA1, ASAP3 |
| [[HSPA4L]] | B | CAP2 activity strengthens HSPA4L's drug response | lines that do not express CAP2 (6) vs lines expressing it (40) | the lines without CAP2 respond 0.93× as strongly (z diff +0.08); strongest at Homoharringtonine 0.5 µM: 1.26x vs 2.72x (z diff +4.4) | 0.090 | ⚠ within organs, on part of the lines; also absent: SCML2, ADORA1, ASAP3; target measured in part of the lines; both ways; artifact flags |

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.604). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-18.3, 10.3); signed map (8.0, -32.3). **Vector** length 125, 36.3% of its response variance represented; |z| ≥ 3 in 1,348 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.2 | +13.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.7 | +15.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.0 | +12.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.3 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +10.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.9 | +5.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.5 | +5.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.4 | +6.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.9 | -26.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.9 | -23.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.6 | -26.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -3.9 | -3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.4 | -4.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.7 | -2.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.6 | -3.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -4.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | cyclase associated actin cytoskeleton regulatory protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:17,393,595-17,557,780 (+) |
| Ensembl biotype | protein_coding |
| Hallmark sets | UV_RESPONSE_DN, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 4 pathways, smallest: Role of ABL in ROBO-SLIT signaling; Signaling by ROBO receptors; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [P40123](https://www.uniprot.org/uniprotkb/P40123) (Adenylyl cyclase-associated protein 2):

> Involved in the regulation of actin polymerization.

**Summary**, from NCBI Gene [10486](https://www.ncbi.nlm.nih.gov/gene/10486):

> This gene was identified by its similarity to the gene for human adenylyl cyclase-associated protein. The function of the protein encoded by this gene is unknown. However, the protein appears to be able to interact with adenylyl cyclase-associated protein and actin. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20039](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20039) · Entrez [10486](https://www.ncbi.nlm.nih.gov/gene/10486) · UniProt [P40123](https://www.uniprot.org/uniprotkb/P40123) · Ensembl [ENSG00000112186](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112186)

## Data

Gene col 3333: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3333); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3333, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3333]; `tensor/DDL_lfc|DDL_z.npy` [3333]; `embed/gene_vectors.npy` [3333]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3333 or target_col == 3333). Every well: [[CAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
