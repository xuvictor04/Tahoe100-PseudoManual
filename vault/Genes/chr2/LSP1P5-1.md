---
symbol: "LSP1P5-1"
type: "gene"
col: 16608
ensembl_id: "ENSG00000291150"
name: ""
location: ""
module: 37
arm: "+"
pooled_cpm: 7.39
n_lines_expressing: 44
n_dd_up: 7
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# LSP1P5-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.49× (z +6.9, q 2e-09, up in 18 of 41 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.70× (z +6.5, q 2e-08, up in 20 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (A498 2.86×; ⚠ cell-cycle shift, explains ~45% of this change).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.530× (z -10.9, q 6e-25, down in 26 of 37 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.512× (z -8.1, q 8e-14, down in 21 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LSP1P4]] (+0.79, fdr 7e-06, ⚠ same locus), [[GET1-SH3BGR]] (+0.66, fdr 7e-06), [[UBE2Q2P13]] (+0.64, fdr 1e-05), [[ECT2L]] (+0.60, fdr 9e-06); moves opposite to [[OMA1]] (-0.57, fdr 1e-05), [[BHLHE41]] (-0.50, fdr 3e-05), [[R3HDM2]] (-0.50, fdr 3e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LSP1P4]] → it (grade C ⚠); 2 go from it, the strongest it → [[PLAC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16608.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (A498 2.86×; ⚠ cell-cycle shift, explains ~45% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.49×** | +6.9 | 2e-09 | 18/41 (A498, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +6.5 | 2e-08 | 20/40 (NCI-H23, SW 900, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.97×** | +4.3 | 0.003 | 5/15 (A498, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +4.0 | 0.008 | 9/30 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.33×** | +3.5 | 0.061 | 9/40 (A498, H4, …) | all doses, stronger at high dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.077 | 7/37 (Panc 03.27, A-427, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.32×** | +3.3 | 0.077 | 10/39 (LOX-IMVI, SHP-77, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.20× | +3.2 | 0.11 | 5/41 (A498, NCI-H1573, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16608.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.530×** | -10.9 | 6e-25 | 26/37 (A498, SNU-423, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.439×** | -9.6 | 2e-19 | 26/40 (A498, NCI-H2030, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.512×** | -8.1 | 8e-14 | 21/37 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.642×** | -5.4 | 1e-05 | 20/40 (LOX-IMVI, A498, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.466×** | -4.9 | 1e-04 | 15/40 (NCI-H23, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.894× | -4.4 | 0.001 | 11/42 (RKO, A549, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.790×** | -4.0 | 0.005 | 13/42 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.724×** | -3.9 | 0.006 | 15/41 (H4, LOX-IMVI, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.826×** | -3.3 | 0.064 | 16/38 (H4, HepG2/C3A, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -3.3 | 0.064 | 8/40 (CHP-212, NCI-H661, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.834× | -3.1 | 0.10 | 8/42 (CFPAC-1, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16608. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 25.2 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -12.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -8.9) |
| [[A498 (line)]] | wt | 15.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.86× (z +9.8) ⚠ cell-cycle shift, explains ~45% of this change | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -18.1) ⚠ cell-cycle shift, explains ~38% of this change |
| [[H4 (line)]] | wt | 15.2 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -11.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HepG2_C3A (line)]] | wt | 13.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -10.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Silodosin (drug)]] 5 µM 0.0876× (z -10.4) |
| [[HOP62 (line)]] | alt | 15.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -14.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW480 (line)]] | alt | 17.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0937× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 10.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -13.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[C-33 A (line)]] | alt | 10.9 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0845× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 7.87 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 7.98 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0960× (z -10.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SNU-423 (line)]] | alt | 5.97 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0691× (z -15.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW48 (line)]] | wt | 10.8 | 0 | 1 | — | [[Clofarabine (drug)]] 0.05 µM 0.0741× (z -8.7) |
| [[A-172 (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.60 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16608), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSP1P4]] | +0.79 | +0.75 / +0.81 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[GET1-SH3BGR]] | +0.66 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[UBE2Q2P13]] | +0.64 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[ECT2L]] | +0.60 | +0.57 / +0.57 | both halves | 9e-06 |  |
| [[SDHAP4-1]] | +0.59 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[RBM44]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ZNF473CR]] | +0.57 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[PLAC1]] | +0.57 | +0.31 / +0.58 | both halves | 2e-04 |  |
| [[CLEC4A]] | +0.57 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[C9orf153]] | +0.56 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[PPP1R32]] | +0.56 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[CCNY-AS1]] | +0.56 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[CAPN10-DT]] | +0.55 | +0.50 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OMA1]] | -0.57 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[BHLHE41]] | -0.50 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[R3HDM2]] | -0.50 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[HIRIP3]] | -0.50 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[MIS12]] | -0.50 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[FAM111A]] | -0.50 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[NRG1]] | -0.49 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[TMEM107]] | -0.49 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[CSTF2T]] | -0.49 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[ZNF252P-1]] | -0.49 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[ADAMTS13]] | -0.48 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[DCLRE1A]] | -0.48 | -0.52 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LSP1P4]] | C | LSP1P4 activity raises LSP1P5-1's level | lines that do not express LSP1P4 (7) vs lines expressing it (43) | 2.92× lower at baseline in the lines without LSP1P4 | 0.060 | ⚠ within organs, on part of the lines; also absent: LSP1P5-1; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAC1]] | B | LSP1P5-1 activity lowers PLAC1's level | lines that do not express LSP1P5-1 (6) vs lines expressing it (44) | 1.28× higher at baseline in the lines without LSP1P5-1 | 0.069 | ⚠ within organs, on part of the lines; also absent: LSP1P4; maybe low, not absent |
| [[LSP1P4]] | C | LSP1P5-1 activity raises LSP1P4's level | lines that do not express LSP1P5-1 (6) vs lines expressing it (44) | 3.61× lower at baseline in the lines without LSP1P5-1 | 0.084 | ⚠ within organs, on part of the lines; also absent: LSP1P4; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.508). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.8, -21.3); signed map (8.8, 6.2). **Vector** length 65.0, 10.5% of its response variance represented; |z| ≥ 3 in 874 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.8 | +6.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +3.8 | +6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +1.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.7 | +1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.6 | +1.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.8 | -9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.2 | -10.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.1 | -5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.9 | -8.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | -3.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -1.3 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.2 | -2.1 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.2 | -2.1 |

## What is on record

> [!warning] No registry record
> LSP1P5-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16608: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16608); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16608, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16608]; `tensor/DDL_lfc|DDL_z.npy` [16608]; `embed/gene_vectors.npy` [16608]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16608 or target_col == 16608). Every well: [[LSP1P5-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LSP1P5-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
