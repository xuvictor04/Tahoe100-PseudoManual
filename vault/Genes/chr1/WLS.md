---
symbol: "WLS"
type: "gene"
col: 3829
ensembl_id: "ENSG00000116729"
name: "Wnt ligand secretion mediator"
location: "1p31.3"
module: 3
arm: "-"
pooled_cpm: 80.42
n_lines_expressing: 43
n_dd_up: 6
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# WLS

*Wnt ligand secretion mediator* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.52× (z +7.5, q 4e-11, up in 22 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.25× (z +5.7, q 2e-06, up in 21 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.499× (z -12.8, q 9e-35, down in 35 of 41 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMB1]] (+0.54, fdr 3e-05), [[B4GALT6]] (+0.54, fdr 3e-05), [[NETO2]] (+0.52, fdr 6e-05); moves opposite to [[TRADD]] (-0.54, fdr 4e-05), [[SPSB3]] (-0.51, fdr 6e-05), [[ZNHIT3]] (-0.51, fdr 5e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KCTD12]] → it (grade B ⚠); 1 goes from it, the strongest it → [[NPRL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3829.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.52×** | +7.5 | 4e-11 | 22/42 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +7.4 | 4e-11 | 25/36 (A-172, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +5.7 | 2e-06 | 21/41 (SW480, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +5.0 | 1e-04 | 21/42 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.28×** | +4.5 | 9e-04 | 24/41 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.043 | 18/41 (SNU-423, J82, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.4 | 0.049 | 16/41 (J82, Hs 766T, …) | top dose only | composition shift |
| [[Busulfan (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.11 | 15/42 (A-172, NCI-H1792, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.19× | +3.1 | 0.11 | 10/41 (SW480, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3829.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.499×** | -12.8 | 9e-35 | 35/41 (LoVo, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.504×** | -12.6 | 5e-34 | 35/41 (LoVo, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.611×** | -9.1 | 2e-17 | 32/41 (C-33 A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.724×** | -5.7 | 1e-06 | 25/40 (SNU-1, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.736×** | -5.7 | 2e-06 | 25/41 (C32, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.753×** | -5.2 | 2e-05 | 23/41 (C32, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.819×** | -5.2 | 2e-05 | 20/42 (C-33 A, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.830×** | -4.2 | 0.002 | 19/41 (HOP62, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.821×** | -4.1 | 0.003 | 15/43 (NCI-H23, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.794×** | -4.0 | 0.003 | 20/41 (C32, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.819×** | -3.7 | 0.011 | 17/41 (SW480, H4, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.826×** | -3.7 | 0.011 | 16/42 (Hs 766T, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.874× | -3.5 | 0.018 | 13/42 (A-172, H4, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.877× | -3.4 | 0.026 | 6/42 (LOX-IMVI, RPMI-7951, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | 0.837× | -3.3 | 0.039 | 9/41 (SK-MEL-2, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.713×** | -3.3 | 0.039 | 14/42 (COLO 205, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.835× | -3.2 | 0.042 | 17/42 (NCI-H23, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3829. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 128 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -14.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 108 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.298× (z -15.1) |
| [[C-33 A (line)]] | alt | 422 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.171× (z -17.4) |
| [[HEC-1-A (line)]] | alt | 76.8 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.565× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.504× (z -8.9) |
| [[HT-29 (line)]] | alt | 217 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.265× (z -13.9) |
| [[RKO (line)]] | wt | 129 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -14.6) |
| [[LoVo (line)]] | wt | 138 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.219× (z -18.8) |
| [[J82 (line)]] | alt | 91.0 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.446× (z -9.0) |
| [[KATO III (line)]] | alt | 69.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +8.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.346× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 215 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -11.8) |
| [[A-172 (line)]] | wt | 55.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.96× (z +12.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 74.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.313× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 109 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.455× (z -9.5) |
| [[LS 180 (line)]] | wt | 141 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.310× (z -13.5) |
| [[Panc 03.27 (line)]] | alt | 85.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.259× (z -13.9) |
| [[HCT15 (line)]] | alt | 65.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.33× (z +9.1) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 100 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.396× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 40.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[PANC-1 (line)]] | alt | 27.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.03× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 78.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[SNU-1 (line)]] | wt | 81.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.256× (z -10.3) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 65.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 67.6 | 0 | 1 | — | [[Fenofibrate (drug)]] 5 µM 0.0725× (z -9.7) |
| [[SW480 (line)]] | alt | 39.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.09× (z +10.9) | — |
| [[A-427 (line)]] | wt | 54.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 173 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.77 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 170 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.21 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 17.8 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 93.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 83.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3829), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*38 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMB1]] | +0.54 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[B4GALT6]] | +0.54 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[NETO2]] | +0.52 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[EXTL2]] | +0.52 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[KCTD12]] | +0.51 | +0.39 / +0.53 | both halves | 5e-05 |  |
| [[SRPX2]] | +0.50 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[SEPTIN11]] | +0.50 | +0.39 / +0.43 | both halves | 6e-05 |  |
| [[STAMBPL1]] | +0.50 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[NID1]] | +0.50 | +0.40 / +0.41 | both halves | 5e-05 |  |
| [[ENC1]] | +0.49 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[HEXB]] | +0.48 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[GALNT1]] | +0.48 | +0.43 / +0.56 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*62 of its nearest partners move opposite, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRADD]] | -0.54 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[SPSB3]] | -0.51 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[ZNHIT3]] | -0.51 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[LCMT1]] | -0.51 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[RAB40C]] | -0.51 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[CRYZL1]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[C1orf174]] | -0.49 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[NPRL2]] | -0.48 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[SIRT7]] | -0.48 | -0.37 / -0.39 | both halves | 7e-05 |  |
| [[PPOX]] | -0.48 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[SLC15A4]] | -0.48 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[SSNA1]] | -0.48 | -0.40 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCTD12]] | B | KCTD12 activity raises WLS's level | lines that do not express KCTD12 (16) vs lines expressing it (34) | 1.33× lower at baseline in the lines without KCTD12 | 0.081 | ⚠ within organs, on part of the lines; also absent: CACNA2D1, NALCN, LINC01828 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPRL2]] | B | WLS activity raises NPRL2's level | lines that do not express WLS (7) vs lines expressing it (43) | 1.43× lower at baseline in the lines without WLS | 0.049 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.464). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (45.3, -25.9); signed map (10.1, 47.3). **Vector** length 117, 30.8% of its response variance represented; |z| ≥ 3 in 1,069 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.9 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.8 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | -1.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.8 | +2.8 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -4.5 | -4.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.2 | -12.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.9 | -12.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.8 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.6 | -3.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.4 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.4 | -2.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | Wnt ligand secretion mediator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:68,098,473-68,233,120 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23091, MRP, EVI, mig-14; previously C1orf139, GPR177 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 2 pathways, smallest: WNT ligand biogenesis and trafficking; Signaling by WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T9L3](https://www.uniprot.org/uniprotkb/Q5T9L3) (Protein wntless homolog):

> Regulates Wnt proteins sorting and secretion in a feedback regulatory mechanism. This reciprocal interaction plays a key role in the regulation of expression, subcellular location, binding and organelle-specific association of Wnt proteins. Plays also an important role in establishment of the anterior-posterior body axis formation during development (By similarity).

**Summary**, from NCBI Gene [79971](https://www.ncbi.nlm.nih.gov/gene/79971):

> Enables Wnt-protein binding activity and identical protein binding activity. Involved in Wnt protein secretion; intracellular protein transport; and positive regulation of cell communication. Located in several cellular components, including Golgi apparatus; early endosome; and endoplasmic reticulum membrane. Implicated in Zaki syndrome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30238](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30238) · Entrez [79971](https://www.ncbi.nlm.nih.gov/gene/79971) · UniProt [Q5T9L3](https://www.uniprot.org/uniprotkb/Q5T9L3) · Ensembl [ENSG00000116729](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116729)

## Data

Gene col 3829: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3829); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3829, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3829]; `tensor/DDL_lfc|DDL_z.npy` [3829]; `embed/gene_vectors.npy` [3829]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3829 or target_col == 3829). Every well: [[WLS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WLS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
