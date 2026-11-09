---
symbol: "ABL1"
type: "gene"
col: 1774
ensembl_id: "ENSG00000097007"
name: "ABL proto-oncogene 1, non-receptor tyrosine kinase"
location: "9q34.12"
module: 103
arm: "+"
pooled_cpm: 148.06
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 15
direction_downstream: 54
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# ABL1

*ABL proto-oncogene 1, non-receptor tyrosine kinase* — 9q34.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.23× (z +9.3, q 1e-17, up in 43 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (MIA PaCa-2 2.13×, HCT15 2.01×, KATO III 1.64×, SW480 1.50×; ⚠ cell-cycle shift, explains ~14% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 1.97×, MIA PaCa-2 1.66×; ⚠ cell-cycle shift, would explain all of this change); [[PH-797804 (drug)]] 5 µM in 1 line (HS-578T 5.31×); [[TAK-901 (drug)]] 5 µM in 1 line (HOP62 4.29×).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.465× (z -16.9, q 0e+00, down in 43 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.796× (z -5.1, q 3e-05, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED27]] (+0.57, fdr 1e-05), [[IPPK]] (+0.55, fdr 2e-05), [[RPTOR]] (+0.54, fdr 1e-05); moves opposite to [[KIAA1522]] (-0.48, fdr 9e-05), [[NOXA1]] (-0.48, fdr 1e-04), [[EPS8L3]] (-0.46, fdr 4e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[CCDC120]] → it (grade B ⚠); 54 go from it, the strongest it → [[ANKMY2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1774.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (MIA PaCa-2 2.13×, HCT15 2.01×, KATO III 1.64×, SW480 1.50×; ⚠ cell-cycle shift, explains ~14% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 1.97×, MIA PaCa-2 1.66×; ⚠ cell-cycle shift, would explain all of this change); [[PH-797804 (drug)]] 5 µM in 1 line (HS-578T 5.31×); [[TAK-901 (drug)]] 5 µM in 1 line (HOP62 4.29×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.23×** | +9.3 | 1e-17 | 43/49 (HOP62, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.47×** | +4.5 | 0.002 | 26/48 (HS-578T, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.16× | +3.3 | 0.19 | 19/48 (BT-474, HS-578T, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1774.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.465×** | -16.9 | 0e+00 | 43/49 (C32, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.467×** | -16.2 | 0e+00 | 38/44 (C32, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.470×** | -16.1 | 0e+00 | 45/47 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.478×** | -15.1 | 0e+00 | 40/45 (C32, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **0.746×** | -6.5 | 9e-09 | 36/48 (KATO III, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.763×** | -5.8 | 8e-07 | 32/48 (C32, NCI-H460, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.796×** | -5.1 | 3e-05 | 25/48 (LOX-IMVI, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.805×** | -4.6 | 3e-04 | 28/50 (LOX-IMVI, SW 1271, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.680×** | -4.5 | 5e-04 | 24/38 (SK-MEL-2, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | 0.836× | -4.0 | 0.004 | 22/48 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.886× | -3.8 | 0.007 | 12/48 (LOX-IMVI, RKO, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.751×** | -3.4 | 0.028 | 16/47 (SW48, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.745×** | -3.4 | 0.029 | 18/49 (C32, J82, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.867× | -3.2 | 0.062 | 21/48 (LOX-IMVI, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.907× | -3.1 | 0.083 | 20/48 (C32, J82, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | 0.872× | -3.0 | 0.088 | 21/48 (LOX-IMVI, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1774. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 393 | 0 | 19 (16 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -14.6) |
| [[NCI-H460 (line)]] | wt | 297 | 0 | 19 (16 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.366× (z -12.2) |
| [[C32 (line)]] | wt | 262 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0990× (z -27.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.485× (z -8.9) |
| [[J82 (line)]] | alt | 327 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -19.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 123 | 2 (2 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +13.6) ⚠ cell-cycle shift, explains ~14% of this change | [[Dinaciclib (drug)]] 5 µM 0.274× (z -15.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 360 | 0 | 5 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.404× (z -10.2) ⚠ toxic · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -9.4) |
| [[A549 (line)]] | wt | 119 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.403× (z -10.8) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 244 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 162 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.29× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -12.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 116 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.332× (z -11.5) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 230 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -9.0) |
| [[PANC-1 (line)]] | alt | 136 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.355× (z -13.9) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 145 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -17.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 145 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -17.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 205 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -14.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 128 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.407× (z -12.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 146 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 5.31× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.394× (z -10.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 129 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +9.0) ⚠ cell-cycle shift, explains ~14% of this change | [[Dinaciclib (drug)]] 5 µM 0.310× (z -14.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 99.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.354× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 169 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -14.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 140 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.322× (z -12.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 119 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.339× (z -15.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 86.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -24.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 134 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +10.2) ⚠ cell-cycle shift, explains ~14% of this change | [[Dinaciclib (drug)]] 5 µM 0.421× (z -8.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 122 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +14.3) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.432× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 119 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.432× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 109 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.130× (z -12.7) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 103 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0815× (z -15.4) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 413 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -9.9) |
| [[SW48 (line)]] | wt | 124 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -10.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 159 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.410× (z -11.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 174 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -9.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 63.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.466× (z -8.9) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 200 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -15.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.424× (z -8.5) ⚠ toxic |
| [[HT-29 (line)]] | alt | 94.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 80.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.169× (z -10.4) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 202 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.353× (z -10.7) ⚠ toxic |
| [[SW1417 (line)]] | alt | 98.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.444× (z -8.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 69.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 89.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 132 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1774), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED27]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 | pathway: Epigenetic regulation by WDR5-containing histone modifying complexes |
| [[IPPK]] | +0.55 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[RPTOR]] | +0.54 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[CHSY1]] | +0.52 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[KDM2B]] | +0.52 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[PAQR7]] | +0.50 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[ZNF668]] | +0.49 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[PRCC]] | +0.49 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[SCAND2P]] | +0.49 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[KIAA0753]] | +0.49 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[LRRC41]] | +0.48 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[PPAN]] | +0.48 | +0.45 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA1522]] | -0.48 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[NOXA1]] | -0.48 | -0.36 / -0.50 | both halves | 1e-04 | same gene group; pathway: Leishmania infection |
| [[EPS8L3]] | -0.46 | -0.42 / -0.42 | both halves | 4e-05 | same gene group |
| [[OPTN]] | -0.45 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[PRSS16]] | -0.45 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[DMTN]] | -0.45 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[EPS8L2]] | -0.43 | -0.27 / -0.43 | both halves | 3e-04 | same gene group |
| [[AP1AR]] | -0.43 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[FMR1]] | -0.43 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[GRB7]] | -0.43 | -0.33 / -0.40 | both halves | 1e-04 | same gene group |
| [[SNX15]] | -0.42 | -0.32 / -0.37 | both halves | 1e-04 |  |
| [[KRAS]] | -0.42 | -0.30 / -0.46 | both halves | 2e-04 | STRING 703 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC120]] | B | CCDC120 activity lowers ABL1's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 1.83× higher at baseline in the lines without CCDC120 | 8e-04 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[GRB7]] | B | GRB7 activity lowers ABL1's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 1.67× higher at baseline in the lines without GRB7 | 0.007 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[TMEM45A]] | B | TMEM45A activity raises ABL1's level | lines that do not express TMEM45A (13) vs lines expressing it (37) | 1.59× lower at baseline in the lines without TMEM45A | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000289516, TTC28, ARHGEF25 |
| [[CCDC120]] | B | CCDC120 activity weakens ABL1's drug response | lines that do not express CCDC120 (11) vs lines expressing it (39) | the lines without CCDC120 respond 1.49× as strongly (z diff -1.97); strongest at Epirubicin (hydrochloride) 5 µM: 0.47x vs 0.87x (z diff -4.4) | 0.033 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2; the reference differs; artifact flags |
| [[DMTN]] | B | DMTN activity weakens ABL1's drug response | lines that do not express DMTN (14) vs lines expressing it (36) | the lines without DMTN respond 1.45× as strongly (z diff -1.93); strongest at Panobinostat 0.5 µM: 0.56x vs 0.87x (z diff -3.9) | 0.046 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent; artifact flags |
| [[MIR100HG]] | B | MIR100HG activity raises ABL1's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 1.48× lower at baseline in the lines without MIR100HG | 0.057 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[HS3ST3A1]] | B | HS3ST3A1 activity raises ABL1's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 1.45× lower at baseline in the lines without HS3ST3A1 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1 |
| [[DMTN]] | B | DMTN activity lowers ABL1's level | lines that do not express DMTN (14) vs lines expressing it (36) | 1.52× higher at baseline in the lines without DMTN | 0.066 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent |
| [[GRB7]] | B | GRB7 activity weakens ABL1's drug response | lines that do not express GRB7 (25) vs lines expressing it (25) | the lines without GRB7 respond 1.66× as strongly (z diff -2.29); strongest at Panobinostat 0.5 µM: 0.63x vs 0.94x (z diff -3.9) | 0.068 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP; artifact flags |
| [[TOX3]] | B | TOX3 activity lowers ABL1's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 1.49× higher at baseline in the lines without TOX3 | 0.073 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[NIHCOLE]] | B | NIHCOLE activity lowers ABL1's level | lines that do not express NIHCOLE (22) vs lines expressing it (28) | 1.39× higher at baseline in the lines without NIHCOLE | 0.073 | ⚠ within organs, on part of the lines; also absent: RORC, TSPAN1, VIL1 |
| [[HS3ST3A1]] | B | HS3ST3A1 activity strengthens ABL1's drug response | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | the lines without HS3ST3A1 respond 0.74× as strongly (z diff +1.72); rises at some drug-doses, falls at others (32% from rises): Panobinostat 0.5 µM: 0.88x vs 0.56x (z diff +4.2); Dinaciclib 5 µM: 0.55x vs 0.30x (z diff +2.9); PH-797804 5 µM: 1.33x vs 2.18x (z diff +2.4) | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1; rises at some drug-doses, falls at others; artifact flags |

### Downstream of this gene

*54 arrows, 54 of them with an alert ⚠; grade A 0, B 54, C 0. Shown: the 12 strongest; 42 more arrows (42 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKMY2]] | B | ABL1 activity lowers ANKMY2's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 2.8% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CDKN2B]] | B | ABL1 activity raises CDKN2B's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.1% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GSG1L]] | B | ABL1 activity raises GSG1L's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.1% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TMEM185A]] | B | ABL1 activity lowers TMEM185A's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 3.4% of all compounds | 0.025 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NUAK1]] | B | ABL1 activity lowers NUAK1's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 3.6% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CAMK2G]] | B | ABL1 activity lowers CAMK2G's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 3.9% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CDKN1A]] | B | ABL1 activity raises CDKN1A's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ENSG00000225218]] | B | ABL1 activity raises ENSG00000225218's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ENSG00000290241]] | B | ABL1 activity raises ENSG00000290241's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HEATR6]] | B | ABL1 activity lowers HEATR6's level | compounds that target ABL1: 3 of 6 raise it (Flumatinib, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds |
| [[PRKAB2]] | B | ABL1 activity lowers PRKAB2's level | compounds that target ABL1: 3 of 6 raise it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SLC8A2]] | B | ABL1 activity raises SLC8A2's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.412). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.4, -20.7); signed map (-33.3, 32.6). **Vector** length 102, 28.8% of its response variance represented; |z| ≥ 3 in 1,071 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.0 | +9.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | +4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +4.0 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.1 | -2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +0.6 |
|  | [[Infigratinib (drug)]] 5 µM |  | +1.6 | +1.3 |
|  | [[Ritonavir (drug)]] 5 µM |  | +1.5 | +0.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -8.9 | -16.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.3 | -3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.0 | -16.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.8 | -16.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.7 | -0.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.0 | -1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ABL proto-oncogene 1, non-receptor tyrosine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.12 — chr9:130,713,043-130,887,675 (+) |
| Ensembl biotype | protein_coding |
| Also known as | JTK7, c-ABL, p150; previously ABL |
| Gene groups (HGNC) | SH2 domain containing; Abl family tyrosine kinases; SH3 domain containing |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE |
| Reactome | 45 pathways, smallest: Role of ABL in ROBO-SLIT signaling; RUNX2 regulates osteoblast differentiation; Myogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P00519](https://www.uniprot.org/uniprotkb/P00519) (Tyrosine-protein kinase ABL1):

> Non-receptor tyrosine-protein kinase that plays a role in many key processes linked to cell growth and survival such as cytoskeleton remodeling in response to extracellular stimuli, cell motility and adhesion, receptor endocytosis, autophagy, DNA damage response and apoptosis. Coordinates actin remodeling through tyrosine phosphorylation of proteins controlling cytoskeleton dynamics like WASF3 (involved in branch formation); ANXA1 (involved in membrane anchoring); DBN1, DBNL, CTTN, RAPH1 and …

**Summary**, from NCBI Gene [25](https://www.ncbi.nlm.nih.gov/gene/25):

> This gene is a protooncogene that encodes a protein tyrosine kinase involved in a variety of cellular processes, including cell division, adhesion, differentiation, and response to stress. The activity of the protein is negatively regulated by its SH3 domain, whereby deletion of the region encoding this domain results in an oncogene. The ubiquitously expressed protein has DNA-binding activity that is regulated by CDC2-mediated phosphorylation, suggesting a cell cycle function. This gene has …

**Accessions** — [HGNC:76](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:76) · Entrez [25](https://www.ncbi.nlm.nih.gov/gene/25) · UniProt [P00519](https://www.uniprot.org/uniprotkb/P00519) · Ensembl [ENSG00000097007](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000097007)

## Data

Gene col 1774: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1774); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1774, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1774]; `tensor/DDL_lfc|DDL_z.npy` [1774]; `embed/gene_vectors.npy` [1774]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1774 or target_col == 1774). Every well: [[ABL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
