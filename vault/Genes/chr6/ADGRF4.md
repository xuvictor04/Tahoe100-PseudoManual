---
symbol: "ADGRF4"
type: "gene"
col: 7713
ensembl_id: "ENSG00000153294"
name: "adhesion G protein-coupled receptor F4"
location: "6p12.3"
module: 8
arm: "+"
pooled_cpm: 2.9
n_lines_expressing: 27
n_dd_up: 27
n_dd_down: 4
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 39
direction_downstream: 47
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ADGRF4

*adhesion G protein-coupled receptor F4* — 6p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.05× (z +10.9, q 4e-25, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.49× (z +10.5, q 3e-23, up in 6 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.538× (z -5.1, q 2e-04, down in 13 of 24 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM: 0.634× (z -3.7, q 0.054, down in 1 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (HT-29 0.0371×, LS 180 0.0771×, CFPAC-1 0.194×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (CFPAC-1 0.134×, COLO 205 0.0988×; ⚠ cell-cycle shift, explains ~29% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2347 0.239×, CFPAC-1 0.302×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DAPP1]] (+0.63, fdr 1e-05), [[KPNA7]] (+0.62, fdr 1e-05), [[NECTIN4]] (+0.62, fdr 7e-06); moves opposite to [[ARMC10]] (-0.42, fdr 8e-05), [[ANGEL1]] (-0.41, fdr 4e-04), [[REG4]] (-0.41, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 39 arrows point to it, the strongest [[HSH2D]] → it (grade B ⚠); 47 go from it, the strongest it → [[RBM47]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7713.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.05×** | +10.9 | 4e-25 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.49×** | +10.5 | 3e-23 | 6/19 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +8.4 | 8e-15 | 2/19 (SNU-423, SW 900) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.07×** | +8.4 | 9e-15 | 11/23 (BT-474, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.29×** | +6.2 | 5e-08 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.70×** | +6.1 | 1e-07 | 2/24 (SW 900, NCI-H1573) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.05×** | +5.6 | 2e-06 | 2/13 (NCI-H1573, LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +5.2 | 2e-05 | 3/23 (NCI-H1573, SW 900, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.81×** | +4.8 | 8e-05 | 13/24 (LoVo, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.81×** | +4.8 | 9e-05 | 12/24 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +4.8 | 9e-05 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.70×** | +4.3 | 7e-04 | 2/19 (LS 180, LoVo) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.68×** | +4.2 | 0.001 | 1/13 (KATO III) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.69×** | +4.1 | 0.002 | 7/16 (HEC-1-A, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.70×** | +4.0 | 0.003 | 3/13 (A498, LoVo, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.63×** | +4.0 | 0.003 | 4/22 (NCI-H2347, BT-474, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +3.4 | 0.020 | 3/19 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cytarabine (drug)]] 5 µM |  | **1.54×** | +3.4 | 0.022 | 5/21 (LS 180, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.024 | 7/24 (HEC-1-A, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.76×** | +3.3 | 0.026 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7713.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (HT-29 0.0371×, LS 180 0.0771×, CFPAC-1 0.194×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (CFPAC-1 0.134×, COLO 205 0.0988×; ⚠ cell-cycle shift, explains ~29% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2347 0.239×, CFPAC-1 0.302×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.538×** | -5.1 | 2e-04 | 13/24 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | **0.634×** | -3.7 | 0.054 | 1/23 (LoVo) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.643×** | -3.6 | 0.057 | 10/23 (A549, CFPAC-1, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | **0.660×** | -3.4 | 0.096 | 3/21 (LOX-IMVI, A498, …) | rises with dose |  |
| [[Malotilate (drug)]] 5 µM |  | 0.688× | -3.1 | 0.25 | 6/23 (hTERT-HPNE, A549, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7713. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 17.1 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -10.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.302× (z -8.8) |
| [[COLO 205 (line)]] | alt | 15.4 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0988× (z -9.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H2347 (line)]] | alt | 17.0 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0993× (z -11.3) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.239× (z -9.9) |
| [[HT-29 (line)]] | alt | 9.79 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0371× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 2.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 7.99 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0771× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.216 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.914 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.279 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.406 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.958 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.880 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.199 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.391 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.285 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.258 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.583 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.301 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.865 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.554 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.259 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7713), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAPP1]] | +0.63 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[KPNA7]] | +0.62 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[NECTIN4]] | +0.62 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[OCLN]] | +0.61 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[HHLA2]] | +0.60 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[GPR87]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 | STRING 414 |
| [[LURAP1L]] | +0.56 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ADGRF1]] | +0.56 | +0.59 / +0.54 | both halves | 1e-05 | same gene group |
| [[TMC1]] | +0.56 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[TACSTD2]] | +0.55 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[MUC20]] | +0.55 | +0.57 / +0.40 | both halves | 4e-05 |  |
| [[MYO5B]] | +0.54 | +0.50 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC10]] | -0.42 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[ANGEL1]] | -0.41 | -0.42 / -0.26 | both halves | 4e-04 |  |
| [[REG4]] | -0.41 | -0.34 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 10, C 29. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSH2D]] | B | HSH2D activity raises ADGRF4's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 2.14× lower at baseline in the lines without HSH2D | 0.014 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[FAAH2]] | B | FAAH2 activity raises ADGRF4's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 2.00× lower at baseline in the lines without FAAH2 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[ST6GALNAC5]] | B | ST6GALNAC5 activity raises ADGRF4's level | lines that do not express ST6GALNAC5 (31) vs lines expressing it (19) | 1.77× lower at baseline in the lines without ST6GALNAC5 | 0.035 | ⚠ within organs, on part of the lines; also absent: TRBC2, ENPP5, KCNH8 |
| [[SLC34A2]] | B | SLC34A2 activity raises ADGRF4's level | lines that do not express SLC34A2 (44) vs lines expressing it (6) | 2.36× lower at baseline in the lines without SLC34A2 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, SFTPA2, GABRP |
| [[LINC02889]] | B | LINC02889 activity raises ADGRF4's level | lines that do not express LINC02889 (12) vs lines expressing it (38) | 1.95× lower at baseline in the lines without LINC02889 | 0.044 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, SAMD5, ENSG00000226640; maybe low, not absent |
| [[TTC9]] | B | TTC9 activity raises ADGRF4's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 1.82× lower at baseline in the lines without TTC9 | 0.049 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |
| [[MUC20]] | B | MUC20 activity raises ADGRF4's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 1.83× lower at baseline in the lines without MUC20 | 0.070 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[TTC6]] | B | TTC6 activity raises ADGRF4's level | lines that do not express TTC6 (15) vs lines expressing it (35) | 1.59× lower at baseline in the lines without TTC6 | 0.076 | ⚠ within organs, on part of the lines; also absent: SLC27A2, FOXA1, LIMCH1; maybe low, not absent |
| [[SPATA6L]] | B | SPATA6L activity raises ADGRF4's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 1.70× lower at baseline in the lines without SPATA6L | 0.092 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[ARHGAP30]] | B | ARHGAP30 activity raises ADGRF4's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 1.75× lower at baseline in the lines without ARHGAP30 | 0.094 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[ADGRF1]] | C | ADGRF1 activity raises ADGRF4's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 3.47× lower at baseline in the lines without ADGRF1 | 1e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |
| [[BMP2]] | C | BMP2 activity raises ADGRF4's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 2.45× lower at baseline in the lines without BMP2 | 0.001 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44; co-absent with the target |

### Downstream of this gene

*47 arrows, 47 of them with an alert ⚠; grade A 0, B 22, C 25. Shown: the 12 strongest; 35 more arrows (35 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBM47]] | B | ADGRF4 activity raises RBM47's level | lines that do not express ADGRF4 (23) vs lines expressing it (27) | 4.27× lower at baseline in the lines without ADGRF4 | 0.001 | ⚠ within organs, on part of the lines; also absent: VNN1, PTPRB, PTPRR |
| [[ANGEL1]] | B | ADGRF4 activity weakens ANGEL1's drug response | lines that do not express ADGRF4 (23) vs lines expressing it (24) | the lines without ADGRF4 respond 1.00× as strongly (z diff -0.21); strongest at Ixazomib citrate 5 µM: 0.57x vs 0.83x (z diff -2.2) | 0.005 | ⚠ within organs, on part of the lines; also absent: VNN1, PTPRB, PTPRR; target measured in part of the lines; both ways; artifact flags |
| [[ZFAND5]] | B | ADGRF4 activity raises ZFAND5's level | lines that do not express ADGRF4 (23) vs lines expressing it (27) | 1.27× lower at baseline in the lines without ADGRF4 | 0.007 | ⚠ within organs, on part of the lines; also absent: VNN1, PTPRB, PTPRR |
| [[ANGEL1]] | B | ADGRF4 activity lowers ANGEL1's level | lines that do not express ADGRF4 (23) vs lines expressing it (27) | 1.55× higher at baseline in the lines without ADGRF4 | 0.010 | ⚠ within organs, on part of the lines; also absent: VNN1, PTPRB, PTPRR |
| [[MUC20]] | B | ADGRF4 activity raises MUC20's level | lines that do not express ADGRF4 (23) vs lines expressing it (27) | 2.68× lower at baseline in the lines without ADGRF4 | 0.012 | ⚠ within organs, on part of the lines; also absent: VNN1, PTPRB, PTPRR |
| [[RNF103-CHMP3]] | B | ADGRF4 activity raises RNF103-CHMP3's level | lines that do not express ADGRF4 (23) vs lines expressing it (27) | 2.13× lower at baseline in the lines without ADGRF4 | 0.022 | ⚠ within organs, on part of the lines; also absent: VNN1, PTPRB, PTPRR |
| [[LINC01504]] | B | ADGRF4 activity raises LINC01504's level | lines that do not express ADGRF4 (23) vs lines expressing it (27) | 1.61× lower at baseline in the lines without ADGRF4 | 0.036 | ⚠ within organs, on part of the lines; also absent: VNN1, PTPRB, PTPRR |
| [[TMC1]] | B | ADGRF4 activity raises TMC1's level | lines that do not express ADGRF4 (23) vs lines expressing it (27) | 1.55× lower at baseline in the lines without ADGRF4 | 0.038 | ⚠ within organs, on part of the lines; also absent: VNN1, PTPRB, PTPRR |
| [[OCLN]] | B | ADGRF4 activity strengthens OCLN's drug response | lines that do not express ADGRF4 (14) vs lines expressing it (16) | the lines without ADGRF4 respond 0.28× as strongly (z diff +3.85); strongest at Homoharringtonine 5 µM: 1.01x vs 0.47x (z diff +6.4) | 0.045 | ⚠ within organs, on part of the lines; also absent: VNN1, PTPRB, PTPRR; target measured in part of the lines; artifact flags |
| [[HSH2D]] | B | ADGRF4 activity raises HSH2D's level | lines that do not express ADGRF4 (23) vs lines expressing it (27) | 2.50× lower at baseline in the lines without ADGRF4 | 0.045 | ⚠ within organs, on part of the lines; also absent: VNN1, PTPRB, PTPRR |
| [[STS]] | B | ADGRF4 activity raises STS's level | lines that do not express ADGRF4 (23) vs lines expressing it (27) | 2.67× lower at baseline in the lines without ADGRF4 | 0.047 | ⚠ within organs, on part of the lines; also absent: VNN1, PTPRB, PTPRR |
| [[UBAP1]] | B | ADGRF4 activity raises UBAP1's level | lines that do not express ADGRF4 (23) vs lines expressing it (27) | 1.34× lower at baseline in the lines without ADGRF4 | 0.051 | ⚠ within organs, on part of the lines; also absent: VNN1, PTPRB, PTPRR |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.527). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.2, 58.5); signed map (55.5, 6.9). **Vector** length 53.5, 12.3% of its response variance represented; |z| ≥ 3 in 615 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +10.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.6 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.5 | +3.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -1.1 | -5.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | +0.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.0 | -3.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | -0.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -0.9 | +0.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.8 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | adhesion G protein-coupled receptor F4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.3 — chr6:47,685,864-47,722,021 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38076, PGR18; previously GPR115 |
| Gene groups (HGNC) | Adhesion G protein-coupled receptors, subfamily F |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZF3](https://www.uniprot.org/uniprotkb/Q8IZF3) (Adhesion G protein-coupled receptor F4):

> Orphan receptor.

**Summary**, from NCBI Gene [221393](https://www.ncbi.nlm.nih.gov/gene/221393):

> Sequence analysis of this gene suggests that it is encodes a member of the superfamily of G protein-couple receptors. G protein-coupled receptors typically contain seven hydrophobic transmembrane domains, interact with guanine nucleotide binding regulatory proteins, and detect molecules outside the cell and act to transduce these signals into intracellular responses. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2016]

**Accessions** — [HGNC:19011](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19011) · Entrez [221393](https://www.ncbi.nlm.nih.gov/gene/221393) · UniProt [Q8IZF3](https://www.uniprot.org/uniprotkb/Q8IZF3) · Ensembl [ENSG00000153294](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153294)

## Data

Gene col 7713: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7713); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7713, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7713]; `tensor/DDL_lfc|DDL_z.npy` [7713]; `embed/gene_vectors.npy` [7713]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7713 or target_col == 7713). Every well: [[ADGRF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADGRF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
