---
symbol: "ZC3H12B"
type: "gene"
col: 2208
ensembl_id: "ENSG00000102053"
name: "zinc finger CCCH-type containing 12B"
location: "Xq11.2-q12"
module: 200
arm: "+"
pooled_cpm: 81.52
n_lines_expressing: 29
n_dd_up: 11
n_dd_down: 28
n_dd_up_clean: 9
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 5
direction_downstream: 7
tags: ["gene", "module/200"]
generated_by: "tahoemap"
---

# ZC3H12B

*zinc finger CCCH-type containing 12B* — Xq11.2-q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.50× (z +10.0, q 8e-21, up in 14 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (14 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.512× (z -11.7, q 1e-28, down in 23 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.338× (z -9.9, q 7e-21, down in 25 of 28 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01473]] (+0.61, fdr 2e-05), [[TBC1D32]] (+0.54, fdr 1e-04), [[CHIC1]] (+0.54, fdr 1e-04); moves opposite to [[CDC42BPB]] (-0.47, fdr 4e-05), [[CYB5R3]] (-0.46, fdr 6e-05), [[RUBCN]] (-0.46, fdr 7e-04).
> It is in [[Module 200]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC01266]] → it (grade B ⚠); 7 go from it, the strongest it → [[EIF2B5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2208.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +10.0 | 8e-21 | 14/27 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.77×** | +9.9 | 9e-21 | 20/27 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +9.8 | 2e-20 | 16/27 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.37×** | +7.9 | 5e-13 | 20/27 (Panc 03.27, SW480, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +4.0 | 0.007 | 14/27 (SW480, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Afatinib (drug)]] 0.5 µM |  | 1.19× | +3.9 | 0.009 | 9/28 (NCI-H1573, C-33 A, …) | two highest doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.009 | 14/27 (LS 180, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.016 | 11/27 (KATO III, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.23×** | +3.6 | 0.021 | 9/27 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.20×** | +3.2 | 0.061 | 15/27 (LS 180, HepG2/C3A, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.061 | 9/28 (NCI-H1573, C-33 A, …) | two highest doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.063 | 10/27 (HOP62, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2208.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.512×** | -11.7 | 1e-28 | 23/27 (RPMI-7951, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.520×** | -10.9 | 2e-25 | 24/27 (RKO, KATO III, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.546×** | -10.1 | 7e-22 | 18/23 (SK-MEL-2, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.548×** | -10.1 | 1e-21 | 20/27 (SHP-77, LS 180, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.338×** | -9.9 | 7e-21 | 25/28 (SNU-423, H4, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.586×** | -9.3 | 1e-18 | 22/27 (C-33 A, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.583×** | -8.7 | 3e-16 | 19/25 (C-33 A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.613×** | -8.5 | 1e-15 | 21/27 (LS 180, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.653×** | -7.4 | 8e-12 | 22/27 (LS 180, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.450×** | -7.3 | 2e-11 | 22/27 (HS-578T, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.691×** | -6.4 | 7e-09 | 20/27 (LS 180, COLO 205, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.786×** | -5.9 | 2e-07 | 20/28 (C-33 A, SNU-423, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.729×** | -5.5 | 2e-06 | 18/27 (LS 180, PANC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.806×** | -5.3 | 5e-06 | 21/28 (LS 180, NCI-H1573, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.730×** | -5.2 | 6e-06 | 21/27 (LS 180, Panc 03.27, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.734×** | -5.2 | 9e-06 | 17/27 (LS 180, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.759×** | -4.8 | 5e-05 | 15/27 (KATO III, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.762×** | -4.7 | 7e-05 | 19/27 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.772×** | -4.5 | 2e-04 | 15/27 (A-427, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.777×** | -4.4 | 3e-04 | 14/27 (LS 180, HCT15, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.825×** | -3.3 | 0.019 | 15/27 (HCT15, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.888× | -2.9 | 0.072 | 2/28 (Panc 03.27, LS 180) | top dose only | position effect removed |
| [[vincristine (drug)]] 5 µM |  | **0.731×** | -2.8 | 0.084 | 10/26 (COLO 205, LS 180, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2208. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 120 | 0 | 15 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.178× (z -13.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Peretinoin (drug)]] 0.5 µM 0.251× (z -10.8) |
| [[KATO III (line)]] | alt | 342 | 2 | 9 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.206× (z -19.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -11.6) |
| [[HCT15 (line)]] | alt | 295 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.273× (z -13.4) |
| [[PANC-1 (line)]] | alt | 268 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -9.1) |
| [[SHP-77 (line)]] | alt | 326 | 0 | 8 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.339× (z -13.6) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 145 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -11.6) |
| [[C-33 A (line)]] | alt | 364 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -12.9) |
| [[RPMI-7951 (line)]] | alt | 157 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.163× (z -9.2) |
| [[HOP62 (line)]] | alt | 112 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +11.8) | [[Digitoxin (drug)]] 5 µM 0.328× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.149× (z -8.5) |
| [[COLO 205 (line)]] | alt | 112 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HS-578T (line)]] | alt | 93.5 | 0 | 4 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0948× (z -9.3) |
| [[RKO (line)]] | wt | 386 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0859× (z -26.2) ⚠ toxic |
| [[SW480 (line)]] | alt | 22.3 | 4 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 4.31× (z +16.2) | — |
| [[NCI-H1792 (line)]] | alt | 102 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 69.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.0874× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SK-MEL-2 (line)]] | alt | 159 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0779× (z -20.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW1417 (line)]] | alt | 55.6 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.93× (z +12.0) | [[Digitoxin (drug)]] 5 µM 0.294× (z -9.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 147 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.400× (z -10.9) |
| [[H4 (line)]] | wt | 134 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.173× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 160 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.294× (z -11.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 21.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.78× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 37.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +12.4) | — |
| [[A-172 (line)]] | wt | 8.26 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.23 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 9.56 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.60 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 8.47 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 78.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.02 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.74 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.69 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.32 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.84 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.48 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.11 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 12.9 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 327 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.91 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 10.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2208), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01473]] | +0.61 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[TBC1D32]] | +0.54 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[CHIC1]] | +0.54 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[LINC01194]] | +0.53 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[DANT2]] | +0.52 | +0.33 / +0.54 | both halves | 1e-04 |  |
| [[ANKRD17]] | +0.52 | +0.35 / +0.57 | both halves | 1e-04 |  |
| [[FHIT]] | +0.51 | +0.34 / +0.49 | both halves | 1e-04 |  |
| [[MIR181A1HG]] | +0.51 | +0.37 / +0.56 | both halves | 8e-05 |  |
| [[LAMA2]] | +0.50 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[IMMP2L]] | +0.50 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[SOX2]] | +0.49 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[TRPS1]] | +0.48 | +0.43 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC42BPB]] | -0.47 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[CYB5R3]] | -0.46 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[RUBCN]] | -0.46 | -0.21 / -0.45 | both halves | 7e-04 |  |
| [[ADCK5]] | -0.45 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[CAPN1]] | -0.45 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[SDHAP4]] | -0.45 | -0.56 / -0.31 | both halves | 2e-04 |  |
| [[ZNF250]] | -0.44 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[SHPK]] | -0.44 | -0.14 / -0.46 | ⚠ not reproduced | 0.002 |  |
| [[ZDHHC7]] | -0.44 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[TMEM127]] | -0.44 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[STARD3]] | -0.44 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[SDHA]] | -0.44 | -0.51 / -0.37 | both halves | 7e-05 |  |
| [[CTNNBIP1]] | -0.43 | -0.39 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01266]] | B | LINC01266 activity raises ZC3H12B's level | lines that do not express LINC01266 (35) vs lines expressing it (15) | 2.91× lower at baseline in the lines without LINC01266 | 0.021 | ⚠ within organs, on part of the lines; also absent: UNC5D, KHDRBS2, ENSG00000260958; maybe low, not absent |
| [[LINC01446]] | B | LINC01446 activity raises ZC3H12B's level | lines that do not express LINC01446 (34) vs lines expressing it (16) | 2.74× lower at baseline in the lines without LINC01446 | 0.024 | ⚠ within organs, on part of the lines; also absent: GABRG2, BAGE2, ENSG00000253363 |
| [[EPIC1]] | B | EPIC1 activity raises ZC3H12B's level | lines that do not express EPIC1 (23) vs lines expressing it (27) | 2.96× lower at baseline in the lines without EPIC1 | 0.044 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000243620, POTEE, FAR2P1 |
| [[DANT2]] | B | DANT2 activity raises ZC3H12B's level | lines that do not express DANT2 (11) vs lines expressing it (39) | 3.41× lower at baseline in the lines without DANT2 | 0.060 | ⚠ within organs, on part of the lines; also absent: DANT1, LRRC36, SGSM1; its own permutation p |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ZC3H12B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EIF2B5]] | B | ZC3H12B activity raises EIF2B5's level | lines that do not express ZC3H12B (21) vs lines expressing it (29) | 1.23× lower at baseline in the lines without ZC3H12B | 0.029 | ⚠ within organs, on part of the lines; also absent: RUNX3, TMEM132D, LINC01876 |
| [[EPIC1]] | B | ZC3H12B activity raises EPIC1's level | lines that do not express ZC3H12B (21) vs lines expressing it (29) | 2.84× lower at baseline in the lines without ZC3H12B | 0.042 | ⚠ within organs, on part of the lines; also absent: RUNX3, TMEM132D, LINC01876 |
| [[ATF7IP2]] | B | ZC3H12B activity raises ATF7IP2's level | lines that do not express ZC3H12B (21) vs lines expressing it (29) | 2.15× lower at baseline in the lines without ZC3H12B | 0.052 | ⚠ within organs, on part of the lines; also absent: RUNX3, TMEM132D, LINC01876 |
| [[CHIC1]] | B | ZC3H12B activity raises CHIC1's level | lines that do not express ZC3H12B (21) vs lines expressing it (29) | 1.86× lower at baseline in the lines without ZC3H12B | 0.072 | ⚠ within organs, on part of the lines; also absent: RUNX3, TMEM132D, LINC01876 |
| [[WWOX]] | B | ZC3H12B activity raises WWOX's level | lines that do not express ZC3H12B (21) vs lines expressing it (29) | 1.52× lower at baseline in the lines without ZC3H12B | 0.084 | ⚠ within organs, on part of the lines; also absent: RUNX3, TMEM132D, LINC01876 |
| [[ZNF518A]] | B | ZC3H12B activity raises ZNF518A's level | lines that do not express ZC3H12B (21) vs lines expressing it (29) | 1.72× lower at baseline in the lines without ZC3H12B | 0.088 | ⚠ within organs, on part of the lines; also absent: RUNX3, TMEM132D, LINC01876 |
| [[CDH12]] | C | ZC3H12B activity raises CDH12's level | lines that do not express ZC3H12B (21) vs lines expressing it (29) | 2.42× lower at baseline in the lines without ZC3H12B | 0.047 | ⚠ within organs, on part of the lines; also absent: RUNX3, TMEM132D, LINC01876; co-absent with the target |

## Where it sits

- **Module**: [[Module 200]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-26.4, 33.1); signed map (11.3, -12.2). **Vector** length 73.5, 18.6% of its response variance represented; |z| ≥ 3 in 763 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +10.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +9.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +9.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | -4.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +2.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.3 | +2.1 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.3 | -4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.2 | -4.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.1 | -9.9 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.9 | -4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -5.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -5.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CCCH-type containing 12B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq11.2-q12 — chrX:65,034,788-65,507,887 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MCPIP2; previously CXorf32 |
| Gene groups (HGNC) | Zinc fingers CCCH-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5HYM0](https://www.uniprot.org/uniprotkb/Q5HYM0) (Probable ribonuclease ZC3H12B):

> May function as RNase and regulate the levels of target RNA species.

**Summary**, from NCBI Gene [340554](https://www.ncbi.nlm.nih.gov/gene/340554):

> The protein encoded by this gene belongs to a family of CCCH-type zinc finger proteins that are involved in the proinflammatory activation of macrophages. The exact function of this family member is unknown, but it is thought to function as a ribonuclease. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:17407](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17407) · Entrez [340554](https://www.ncbi.nlm.nih.gov/gene/340554) · UniProt [Q5HYM0](https://www.uniprot.org/uniprotkb/Q5HYM0) · Ensembl [ENSG00000102053](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102053)

## Data

Gene col 2208: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2208); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2208, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2208]; `tensor/DDL_lfc|DDL_z.npy` [2208]; `embed/gene_vectors.npy` [2208]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2208 or target_col == 2208). Every well: [[ZC3H12B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZC3H12B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
