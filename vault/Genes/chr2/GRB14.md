---
symbol: "GRB14"
type: "gene"
col: 3653
ensembl_id: "ENSG00000115290"
name: "growth factor receptor bound protein 14"
location: "2q24.3"
module: 188
arm: "+"
pooled_cpm: 16.38
n_lines_expressing: 36
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/188"]
generated_by: "tahoemap"
---

# GRB14

*growth factor receptor bound protein 14* — 2q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.09× (z +17.2, q 0e+00, up in 31 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (HS-578T 0.117×, NCI-H2030 0.237×, A549 0.283×, A-172 0.166×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HS-578T 0.0757×, NCI-H2030 0.342×; ⚠ cell-cycle shift, explains ~54% of this change); [[Trametinib (drug)]] 5 µM in 1 line (HS-578T 0.123×; ⚠ cell-cycle shift, explains ~22% of this change); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (HS-578T 0.160×); [[Cobimetinib (drug)]] 5 µM in 1 line (HS-578T 0.159×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAR1]] (+0.59, fdr 1e-05), [[GNPTAB]] (+0.59, fdr 1e-05), [[SYBU]] (+0.59, fdr 2e-05); moves opposite to [[FANK1]] (-0.56, fdr 2e-05), [[UNKL]] (-0.54, fdr 4e-05), [[CYTH2]] (-0.49, fdr 4e-04).
> It is in [[Module 188]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[FAR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3653.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.09×** | +17.2 | 0e+00 | 31/34 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.68×** | +12.1 | 5e-31 | 20/34 (HT-29, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.96×** | +11.1 | 3e-26 | 23/32 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +9.1 | 1e-17 | 2/15 (HepG2/C3A, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.65×** | +8.2 | 2e-14 | 24/34 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.64×** | +8.1 | 5e-14 | 23/33 (HT-29, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.62×** | +8.0 | 1e-13 | 23/33 (NCI-H1792, HS-578T, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.58×** | +7.6 | 3e-12 | 8/25 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 0.05 µM |  | **1.58×** | +7.5 | 4e-12 | 21/34 (HT-29, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.57×** | +7.4 | 9e-12 | 18/34 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.51×** | +6.8 | 6e-10 | 18/33 (CFPAC-1, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +6.5 | 4e-09 | 19/34 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +5.8 | 4e-07 | 11/32 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.35×** | +4.9 | 4e-05 | 15/33 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.76×** | +4.9 | 5e-05 | 9/31 (NCI-H1792, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.75×** | +4.8 | 5e-05 | 14/32 (NCI-H23, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.009 | 5/32 (NCI-H2347, J82, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.012 | 6/32 (A-427, CFPAC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.023 | 10/32 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.026 | 7/33 (HepG2/C3A, A-427, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.038 | 4/34 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3653.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (HS-578T 0.117×, NCI-H2030 0.237×, A549 0.283×, A-172 0.166×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HS-578T 0.0757×, NCI-H2030 0.342×; ⚠ cell-cycle shift, explains ~54% of this change); [[Trametinib (drug)]] 5 µM in 1 line (HS-578T 0.123×; ⚠ cell-cycle shift, explains ~22% of this change); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (HS-578T 0.160×); [[Cobimetinib (drug)]] 5 µM in 1 line (HS-578T 0.159×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.841× | -4.1 | 0.025 | 10/34 (NCI-H23, HS-578T, …) | top dose only |  |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | 0.808× | -3.5 | 0.11 | 3/33 (A-427, HEC-1-A, …) | two highest doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 0.825× | -3.2 | 0.25 | 13/32 (HEC-1-A, A498, …) | top dose only | position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.825× | -3.0 | 0.25 | 5/34 (A-427, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.880× | -3.0 | 0.25 | 3/34 (NCI-H2347, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3653. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 65.9 | 0 | 12 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0757× (z -20.9) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.117× (z -17.3) |
| [[HT-29 (line)]] | alt | 38.4 | 1 | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.56× (z +10.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.176× (z -12.8) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[vincristine (drug)]] 0.5 µM 0.177× (z -9.5) |
| [[A-172 (line)]] | wt | 13.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 33.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.302× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.331× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 82.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -14.4) |
| [[A549 (line)]] | wt | 42.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -11.7) |
| [[HOP62 (line)]] | alt | 4.37 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.86× (z +10.3) | — |
| [[J82 (line)]] | alt | 5.80 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.10× (z +8.6) | — |
| [[LoVo (line)]] | wt | 10.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.91× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 9.49 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.108× (z -9.7) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -9.1) ⚠ cell-cycle shift, explains ~54% of this change |
| [[NCI-H460 (line)]] | wt | 4.30 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.58× (z +11.2) | — |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.133× (z -9.8) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 63.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.61 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.09 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.46 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.08 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.82 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3653), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAR1]] | +0.59 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[GNPTAB]] | +0.59 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[SYBU]] | +0.59 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[SLC29A1]] | +0.56 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[FHOD3]] | +0.55 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[SUGT1P4-STRA6LP]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[PPAT]] | +0.54 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[LPAR3]] | +0.53 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[ELP1]] | +0.53 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[MPZL1]] | +0.52 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[MAP6]] | +0.52 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[MCOLN2]] | +0.52 | +0.39 / +0.51 | both halves | 6e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FANK1]] | -0.56 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[UNKL]] | -0.54 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[CYTH2]] | -0.49 | -0.26 / -0.56 | both halves | 4e-04 | same gene group |
| [[XRN1]] | -0.49 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[KIAA0753]] | -0.48 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[AKT1S1]] | -0.48 | -0.29 / -0.53 | both halves | 2e-04 |  |
| [[UBE3B]] | -0.48 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[ZFYVE26]] | -0.48 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[SMCR8]] | -0.47 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[ASH1L]] | -0.47 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[CDKN2B-AS1]] | -0.47 | -0.41 / -0.37 | both halves | 7e-05 |  |
| [[ASXL2]] | -0.47 | -0.37 / -0.40 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP6]] | B | MAP6 activity lowers GRB14's level | lines that do not express MAP6 (22) vs lines expressing it (28) | 1.35× higher at baseline in the lines without MAP6 | 0.054 | ⚠ within organs, on part of the lines; also absent: PCSK1N, ZFP28, SNAP91 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAR1]] | B | GRB14 activity lowers FAR1's level | lines that do not express GRB14 (14) vs lines expressing it (36) | 1.32× higher at baseline in the lines without GRB14 | 0.084 | ⚠ within organs, on part of the lines; also absent: GPR37; maybe low, not absent |

## Where it sits

- **Module**: [[Module 188]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.648). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-5.4, -6.4); signed map (-35.9, -16.9). **Vector** length 75.1, 15.8% of its response variance represented; |z| ≥ 3 in 812 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +17.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +11.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.0 | +12.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.3 | +8.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.0 | +6.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +4.8 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +4.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.5 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.1 | -2.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -2.0 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | growth factor receptor bound protein 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.3 — chr2:164,492,417-164,621,482 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Pleckstrin homology domain containing; SH2 domain containing; Growth factor receptor bound protein 7 family |
| Reactome | 3 pathways, smallest: Tie2 Signaling; Cell surface interactions at the vascular wall; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14449](https://www.uniprot.org/uniprotkb/Q14449) (Growth factor receptor-bound protein 14):

> Adapter protein which modulates coupling of cell surface receptor kinases with specific signaling pathways. Binds to, and suppresses signals from, the activated insulin receptor (INSR). Potent inhibitor of insulin-stimulated MAPK3 phosphorylation. Plays a critical role regulating PDPK1 membrane translocation in response to insulin stimulation and serves as an adapter protein to recruit PDPK1 to activated insulin receptor, thus promoting PKB/AKT1 phosphorylation and transduction of the insulin …

**Summary**, from NCBI Gene [2888](https://www.ncbi.nlm.nih.gov/gene/2888):

> The product of this gene belongs to a small family of adapter proteins that are known to interact with a number of receptor tyrosine kinases and signaling molecules. This gene encodes a growth factor receptor-binding protein that interacts with insulin receptors and insulin-like growth-factor receptors. This protein likely has an inhibitory effect on receptor tyrosine kinase signaling and, in particular, on insulin receptor signaling. This gene may play a role in signaling pathways that …

**Accessions** — [HGNC:4565](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4565) · Entrez [2888](https://www.ncbi.nlm.nih.gov/gene/2888) · UniProt [Q14449](https://www.uniprot.org/uniprotkb/Q14449) · Ensembl [ENSG00000115290](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115290)

## Data

Gene col 3653: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3653); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3653, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3653]; `tensor/DDL_lfc|DDL_z.npy` [3653]; `embed/gene_vectors.npy` [3653]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3653 or target_col == 3653). Every well: [[GRB14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRB14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
