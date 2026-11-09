---
symbol: "XRN2"
type: "gene"
col: 1554
ensembl_id: "ENSG00000088930"
name: "5'-3' exoribonuclease 2"
location: "20p11.22"
module: 4
arm: "+"
pooled_cpm: 207.44
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# XRN2

*5'-3' exoribonuclease 2* — 20p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.83× (z +15.9, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.824× (z -7.3, q 2e-10, down in 23 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAA15]] (+0.71, fdr 7e-06), [[CCT2]] (+0.66, fdr 7e-06), [[TRIM44]] (+0.65, fdr 1e-05); moves opposite to [[FAM117A]] (-0.65, fdr 1e-05), [[ZNF821]] (-0.62, fdr 7e-06), [[CCS]] (-0.61, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HLA-F-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1554.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.83×** | +15.9 | 0e+00 | 44/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.63×** | +13.4 | 3e-38 | 46/48 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.57×** | +13.0 | 1e-36 | 47/49 (NCI-H1573, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +12.3 | 2e-32 | 40/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +11.9 | 2e-30 | 40/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.33×** | +10.6 | 3e-24 | 32/48 (NCI-H1573, NCI-H460, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +10.4 | 3e-23 | 43/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +10.0 | 2e-21 | 34/48 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +9.7 | 3e-20 | 39/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +9.4 | 3e-19 | 41/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +8.0 | 9e-14 | 38/48 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +7.7 | 5e-13 | 40/48 (PANC-1, HCT15, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +6.9 | 2e-10 | 39/45 (Hs 766T, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.31×** | +6.5 | 3e-09 | 33/48 (NCI-H1573, HOP62, …) | rises with dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.50×** | +5.6 | 9e-07 | 26/38 (NCI-H1573, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.17× | +3.8 | 0.004 | 20/48 (NCI-H1573, CFPAC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.010 | 26/49 (PANC-1, SNU-423, …) | all doses, flat | noisy plate (z scaled) |
| [[crizotinib (drug)]] 5 µM |  | 1.15× | +3.3 | 0.024 | 11/48 (A498, C32, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.024 | 20/48 (NCI-H1573, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.065 | 17/47 (HCT15, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1554.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.824×** | -7.3 | 2e-10 | 23/49 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.747×** | -7.0 | 6e-10 | 33/47 (HepG2/C3A, SW1417, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.832×** | -4.9 | 2e-04 | 23/48 (RKO, NCI-H23, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | 0.879× | -4.8 | 2e-04 | 14/48 (A498, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.831×** | -4.5 | 8e-04 | 25/47 (NCI-H23, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.873× | -3.6 | 0.030 | 12/47 (SW480, A-427, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.886× | -3.2 | 0.11 | 14/49 (NCI-H23, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.902× | -3.1 | 0.12 | 11/48 (NCI-H23, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.880× | -3.1 | 0.12 | 15/48 (NCI-H23, A-427, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.892× | -3.1 | 0.12 | 5/49 (CFPAC-1, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.906× | -3.0 | 0.12 | 5/48 (SW480, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1554. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 323 | 13 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.39× (z +21.5) | — |
| [[NCI-H460 (line)]] | wt | 207 | 11 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +18.5) | — |
| [[HOP62 (line)]] | alt | 218 | 10 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +11.8) | — |
| [[PANC-1 (line)]] | alt | 203 | 10 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.61× (z +24.5) | — |
| [[HT-29 (line)]] | alt | 128 | 8 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +10.2) | — |
| [[AsPC-1 (line)]] | alt | 163 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +13.7) | [[Selinexor (drug)]] 5 µM 0.654× (z -8.7) ⚠ cell-cycle shift, explains ~66% of this change |
| [[CFPAC-1 (line)]] | alt | 105 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.53× (z +12.2) | — |
| [[LoVo (line)]] | wt | 168 | 6 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.36× (z +14.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +11.1) | — |
| [[RPMI-7951 (line)]] | alt | 317 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +10.6) | — |
| [[SW480 (line)]] | alt | 287 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +13.5) | — |
| [[A-172 (line)]] | wt | 155 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +12.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.19× (z +10.9) | — |
| [[Hs 766T (line)]] | wt | 138 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +10.9) | — |
| [[SNU-423 (line)]] | alt | 190 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +11.1) | — |
| [[COLO 205 (line)]] | alt | 148 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 219 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.10× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.70× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 77.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +10.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 204 | 2 | 2 | [[TAK-901 (drug)]] 5 µM 3.12× (z +9.1) | [[Cobimetinib (drug)]] 5 µM 0.493× (z -9.9) |
| [[C32 (line)]] | wt | 183 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +10.6) | — |
| [[HepG2_C3A (line)]] | wt | 296 | 2 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.02× (z +9.4) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 3.26× (z +9.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.379× (z -13.0) ⚠ toxic |
| [[LS 180 (line)]] | wt | 146 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +14.6) | — |
| [[SW 900 (line)]] | alt | 204 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +10.9) | — |
| [[A-427 (line)]] | wt | 142 | 1 | 1 | [[PH-797804 (drug)]] 5 µM 3.18× (z +8.6) | [[Auranofin (drug)]] 5 µM 0.547× (z -8.6) |
| [[A549 (line)]] | wt | 284 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +11.1) ⚠ cell-cycle shift, explains ~40% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -12.6) |
| [[H4 (line)]] | wt | 171 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +8.6) | [[Selinexor (drug)]] 5 µM 0.556× (z -9.0) ⚠ cell-cycle shift, explains ~66% of this change |
| [[J82 (line)]] | alt | 214 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +13.6) | — |
| [[KATO III (line)]] | alt | 199 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 3.39× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 264 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +11.3) | — |
| [[NCI-H2030 (line)]] | alt | 153 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 141 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.83× (z +8.8) | — |
| [[RKO (line)]] | wt | 379 | 1 | 1 | [[PH-797804 (drug)]] 5 µM 2.81× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.606× (z -11.8) |
| [[SW1417 (line)]] | alt | 391 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 1.70× (z +8.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.534× (z -10.0) ⚠ toxic |
| [[A498 (line)]] | wt | 244 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -13.7) |
| [[AN3 CA (line)]] | alt | 291 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -9.5) |
| [[HCT15 (line)]] | alt | 146 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.89× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[HEC-1-A (line)]] | alt | 138 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 2.96× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 115 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.09× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | — |
| [[SHP-77 (line)]] | alt | 381 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.73× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 220 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.76× (z +8.5) | — |
| [[SW 1088 (line)]] | alt | 200 | 0 | 1 | — | [[Mebendazole (drug)]] 0.5 µM 0.209× (z -8.7) |
| [[SW48 (line)]] | wt | 206 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.94× (z +12.5) | — |
| [[BT-474 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 213 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 189 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 247 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 142 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 290 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 274 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1554), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA15]] | +0.71 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[CCT2]] | +0.66 | +0.72 / +0.58 | both halves | 7e-06 | pathway: Association of TriC/CCT with target proteins during biosynthesis; STRING 573 |
| [[TRIM44]] | +0.65 | +0.55 / +0.75 | both halves | 1e-05 |  |
| [[LAS1L]] | +0.65 | +0.67 / +0.63 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 445 |
| [[ATIC]] | +0.65 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[FARSB]] | +0.64 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[IPO7]] | +0.64 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[DDX10]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[MYBBP1A]] | +0.64 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[VWA8]] | +0.63 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[DHX9]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 467 |
| [[LRPPRC]] | +0.62 | +0.59 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM117A]] | -0.65 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[ZNF821]] | -0.62 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[CCS]] | -0.61 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[TSC22D4]] | -0.61 | -0.48 / -0.66 | both halves | 2e-05 |  |
| [[APTR]] | -0.60 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[AAMDC]] | -0.60 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[FUT11]] | -0.59 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[HMGCL]] | -0.59 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[TCEAL3]] | -0.57 | -0.44 / -0.68 | both halves | 3e-05 |  |
| [[ZFYVE1]] | -0.57 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[TULP3]] | -0.56 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[RSRP1]] | -0.56 | -0.46 / -0.60 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-F-AS1]] | B | HLA-F-AS1 activity lowers XRN2's level | lines that do not express HLA-F-AS1 (6) vs lines expressing it (44) | 1.21× higher at baseline in the lines without HLA-F-AS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: LRP1, STRIP2, SH2D4B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.721). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-20.6, -34.1); signed map (-7.7, -46.0). **Vector** length 95.7, 32.1% of its response variance represented; |z| ≥ 3 in 1,318 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | +9.0 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.1 | +1.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +7.0 | +4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.0 | +3.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.7 | +9.4 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +3.0 | +0.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.8 | -0.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +2.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.6 | +1.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.6 | -7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -0.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -4.0 | -4.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.8 | +12.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.7 | +15.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.3 | -2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | 5'-3' exoribonuclease 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.22 — chr20:21,303,331-21,389,825 (+) |
| Ensembl biotype | protein_coding |
| Reactome | 11 pathways, smallest: Nuclear RNA decay; Association of TriC/CCT with target proteins during biosynthesis; Chaperonin-mediated protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0D6](https://www.uniprot.org/uniprotkb/Q9H0D6) (5'-3' exoribonuclease 2):

> Possesses 5'->3' exoribonuclease activity (By similarity). May promote the termination of transcription by RNA polymerase II. During transcription termination, cleavage at the polyadenylation site liberates a 5' fragment which is subsequently processed to form the mature mRNA and a 3' fragment which remains attached to the elongating polymerase. The processive degradation of this 3' fragment by this protein may promote termination of transcription. Binds to RNA polymerase II (RNAp II) …

**Summary**, from NCBI Gene [22803](https://www.ncbi.nlm.nih.gov/gene/22803):

> This gene encodes a 5'-3' exonuclease that promotes transcription termination at cotranscriptional cleavage sites. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:12836](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12836) · Entrez [22803](https://www.ncbi.nlm.nih.gov/gene/22803) · UniProt [Q9H0D6](https://www.uniprot.org/uniprotkb/Q9H0D6) · Ensembl [ENSG00000088930](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088930)

## Data

Gene col 1554: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1554); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1554, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1554]; `tensor/DDL_lfc|DDL_z.npy` [1554]; `embed/gene_vectors.npy` [1554]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1554 or target_col == 1554). Every well: [[XRN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XRN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
