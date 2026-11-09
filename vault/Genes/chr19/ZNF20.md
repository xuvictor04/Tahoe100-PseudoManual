---
symbol: "ZNF20"
type: "gene"
col: 5269
ensembl_id: "ENSG00000132010"
name: "zinc finger protein 20"
location: "19p13.2"
module: 94
arm: "+"
pooled_cpm: 4.82
n_lines_expressing: 46
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 14
direction_downstream: 10
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# ZNF20

*zinc finger protein 20* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.55× (z +19.7, q 0e+00, up in 33 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Nimesulide (drug)]] 5 µM in 1 line (NCI-H23 0.0832×; ⚠ toxic; unreliable plate only); [[Docetaxel (drug)]] 0.05 µM in 1 line (LS 180 0.130×; ⚠ transcription drop; cell-cycle shift, explains ~36% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF442]] (+0.68, fdr 7e-06), [[ZNF44]] (+0.64, fdr 7e-06), [[ZNF441]] (+0.63, fdr 7e-06); moves opposite to [[LMBR1]] (-0.52, fdr 5e-05), [[FAM135A]] (-0.49, fdr 3e-05), [[TOMM5]] (-0.48, fdr 5e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[ZNF441]] → it (grade B ⚠); 10 go from it, the strongest it → [[ZNF44]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5269.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.55×** | +19.7 | 0e+00 | 33/37 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +14.4 | 2e-44 | 27/37 (HS-578T, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.45×** | +12.9 | 1e-35 | 32/41 (J82, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.80×** | +12.4 | 6e-33 | 24/42 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.13×** | +11.3 | 2e-27 | 23/35 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.98×** | +10.2 | 2e-22 | 26/42 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.89×** | +9.5 | 2e-19 | 25/43 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.88×** | +8.3 | 9e-15 | 22/41 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.74×** | +8.3 | 9e-15 | 17/43 (J82, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.66×** | +7.6 | 2e-12 | 17/42 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.59×** | +6.9 | 3e-10 | 11/43 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +5.7 | 4e-07 | 9/24 (SW1417, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.7 | 5e-07 | 8/34 (HS-578T, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +5.7 | 5e-07 | 5/12 (BT-474, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +5.6 | 1e-06 | 12/43 (SW1417, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.45×** | +5.6 | 1e-06 | 10/39 (NCI-H2347, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.44×** | +5.4 | 2e-06 | 6/43 (RKO, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5269.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Nimesulide (drug)]] 5 µM in 1 line (NCI-H23 0.0832×; ⚠ toxic; unreliable plate only); [[Docetaxel (drug)]] 0.05 µM in 1 line (LS 180 0.130×; ⚠ transcription drop; cell-cycle shift, explains ~36% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.808× | -3.2 | 0.47 | 6/43 (SW480, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5269. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 5.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 4.87 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.130× (z -8.5) ⚠ transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H23 (line)]] | alt | 4.89 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0832× (z -8.8) ⚠ toxic; unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 4.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 9.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +9.6) | — |
| [[SW480 (line)]] | alt | 7.54 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +12.1) | — |
| [[A-172 (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.608 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.795 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.854 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5269), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF442]] | +0.68 | +0.69 / +0.63 | both halves | 7e-06 | same gene group |
| [[ZNF44]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 | same gene group |
| [[ZNF441]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 | same gene group |
| [[ZNF436]] | +0.58 | +0.57 / +0.41 | both halves | 4e-05 | same gene group |
| [[ZNF563]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 | same gene group |
| [[ZNF844]] | +0.56 | +0.48 / +0.53 | both halves | 2e-05 | same gene group; ⚠ same locus (11.3 kb: neighbours can correlate without regulation) |
| [[ZNF627]] | +0.56 | +0.57 / +0.48 | both halves | 2e-05 | same gene group |
| [[ARRDC3]] | +0.55 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[ZNF433]] | +0.54 | +0.54 / +0.50 | both halves | 1e-05 | same gene group |
| [[GIN1]] | +0.53 | +0.62 / +0.33 | both halves | 1e-04 |  |
| [[ZNF101]] | +0.53 | +0.58 / +0.42 | both halves | 4e-05 | same gene group |
| [[CCNG2]] | +0.51 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[ZNF888]] | +0.51 | +0.55 / +0.33 | both halves | 1e-04 | same gene group |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMBR1]] | -0.52 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[FAM135A]] | -0.49 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[TOMM5]] | -0.48 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[DUS1L]] | -0.47 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[TMEM120B]] | -0.47 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[CCNY]] | -0.45 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[VKORC1L1]] | -0.45 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[UCHL3]] | -0.44 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[GMDS]] | -0.44 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[PIP4K2A]] | -0.44 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[MYO19]] | -0.44 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[PSME4]] | -0.43 | -0.42 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 8, C 6. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF441]] | B | ZNF441 activity raises ZNF20's level | lines that do not express ZNF441 (7) vs lines expressing it (43) | 2.00× lower at baseline in the lines without ZNF441 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000286098, ZNF442, ZNF433 |
| [[CIART]] | B | CIART activity raises ZNF20's level | lines that do not express CIART (22) vs lines expressing it (28) | 1.42× lower at baseline in the lines without CIART | 0.013 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, PTN, PPP2R2B |
| [[ZNF391]] | B | ZNF391 activity raises ZNF20's level | lines that do not express ZNF391 (5) vs lines expressing it (45) | 1.63× lower at baseline in the lines without ZNF391 | 0.014 | ⚠ within organs, on part of the lines; also absent: LINC00159, ENSG00000283491, ASIC1; maybe low, not absent |
| [[ZNF563]] | B | ZNF563 activity raises ZNF20's level | lines that do not express ZNF563 (9) vs lines expressing it (41) | 1.99× lower at baseline in the lines without ZNF563 | 0.022 | ⚠ within organs, on part of the lines; also absent: ZNF442, ZNF433, ENSG00000269755 |
| [[ZNF85]] | B | ZNF85 activity raises ZNF20's level | lines that do not express ZNF85 (17) vs lines expressing it (33) | 1.53× lower at baseline in the lines without ZNF85 | 0.024 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF66, ZNF726 |
| [[ZNF625]] | B | ZNF625 activity raises ZNF20's level | lines that do not express ZNF625 (19) vs lines expressing it (31) | 1.38× lower at baseline in the lines without ZNF625 | 0.033 | ⚠ within organs, on part of the lines; also absent: ZNF415, ZNF829, ZNF347 |
| [[ZNF888]] | B | ZNF888 activity raises ZNF20's level | lines that do not express ZNF888 (6) vs lines expressing it (44) | 2.07× lower at baseline in the lines without ZNF888 | 0.070 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF816, ZNF468, ZNF701 |
| [[ZNF682]] | B | ZNF682 activity raises ZNF20's level | lines that do not express ZNF682 (20) vs lines expressing it (30) | 1.52× lower at baseline in the lines without ZNF682 | 0.087 | ⚠ within organs, on part of the lines; also absent: ZNF93, ZNF90, SCUBE3 |
| [[ZNF44]] | C | ZNF44 activity raises ZNF20's level | lines that do not express ZNF44 (3) vs lines expressing it (46) | 3.58× lower at baseline in the lines without ZNF44 | 2e-04 | ⚠ few lines (3 vs 46); across organs; also absent: ZNF20, ENSG00000268870, SORT1; co-absent with the target |
| [[ZNF433]] | C | ZNF433 activity raises ZNF20's level | lines that do not express ZNF433 (8) vs lines expressing it (42) | 2.40× lower at baseline in the lines without ZNF433 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF563, ZNF442; co-absent with the target |
| [[ZNF442]] | C | ZNF442 activity raises ZNF20's level | lines that do not express ZNF442 (7) vs lines expressing it (43) | 2.29× lower at baseline in the lines without ZNF442 | 0.011 | ⚠ within organs, on part of the lines; also absent: ZNF563, ENSG00000286098, ENSG00000268870; co-absent with the target |
| [[ZNF253]] | C | ZNF253 activity raises ZNF20's level | lines that do not express ZNF253 (4) vs lines expressing it (46) | 2.83× lower at baseline in the lines without ZNF253 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF20, ZNF440, DEF6; co-absent with the target; its own permutation p |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF44]] | C | ZNF20 activity raises ZNF44's level | lines that do not express ZNF20 (4) vs lines expressing it (46) | 6.62× lower at baseline in the lines without ZNF20 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000268870, ZNF700, ZNF44; maybe low, not absent; co-absent with the target; its own permutation p |
| [[ZNF563]] | C | ZNF20 activity raises ZNF563's level | lines that do not express ZNF20 (4) vs lines expressing it (46) | 3.65× lower at baseline in the lines without ZNF20 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000268870, ZNF700, ZNF44; maybe low, not absent; its own permutation p |
| [[ZNF253]] | C | ZNF20 activity raises ZNF253's level | lines that do not express ZNF20 (4) vs lines expressing it (46) | 3.44× lower at baseline in the lines without ZNF20 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000268870, ZNF700, ZNF44; maybe low, not absent; co-absent with the target; its own permutation p |
| [[ZNF440]] | C | ZNF20 activity raises ZNF440's level | lines that do not express ZNF20 (4) vs lines expressing it (46) | 5.34× lower at baseline in the lines without ZNF20 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000268870, ZNF700, ZNF44; maybe low, not absent; co-absent with the target; its own permutation p |
| [[ZNF433]] | C | ZNF20 activity raises ZNF433's level | lines that do not express ZNF20 (4) vs lines expressing it (46) | 4.52× lower at baseline in the lines without ZNF20 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000268870, ZNF700, ZNF44; maybe low, not absent; co-absent with the target; its own permutation p |
| [[ZNF625]] | C | ZNF20 activity raises ZNF625's level | lines that do not express ZNF20 (4) vs lines expressing it (46) | 4.05× lower at baseline in the lines without ZNF20 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000268870, ZNF700, ZNF44; maybe low, not absent; its own permutation p |
| [[ZNF888]] | C | ZNF20 activity raises ZNF888's level | lines that do not express ZNF20 (4) vs lines expressing it (46) | 4.04× lower at baseline in the lines without ZNF20 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000268870, ZNF700, ZNF44; maybe low, not absent; its own permutation p |
| [[ZNF442]] | C | ZNF20 activity raises ZNF442's level | lines that do not express ZNF20 (4) vs lines expressing it (46) | 3.57× lower at baseline in the lines without ZNF20 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000268870, ZNF700, ZNF44; maybe low, not absent; co-absent with the target; its own permutation p |
| [[ZNF441]] | C | ZNF20 activity raises ZNF441's level | lines that do not express ZNF20 (4) vs lines expressing it (46) | 3.19× lower at baseline in the lines without ZNF20 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000268870, ZNF700, ZNF44; maybe low, not absent; its own permutation p |
| [[TEF]] | C | ZNF20 activity raises TEF's level | lines that do not express ZNF20 (4) vs lines expressing it (46) | 1.70× lower at baseline in the lines without ZNF20 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000268870, ZNF700, ZNF44; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.8, 23.9); signed map (16.1, -16.8). **Vector** length 45.6, 5.32% of its response variance represented; |z| ≥ 3 in 864 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.5 | +12.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.0 | +19.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +2.6 | +5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +14.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.5 | +12.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +5.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | +4.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.0 | +3.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -3.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.3 | -2.9 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.2 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:12,092,843-12,140,355 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KOX13 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P17024](https://www.uniprot.org/uniprotkb/P17024) (Zinc finger protein 20):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7568](https://www.ncbi.nlm.nih.gov/gene/7568):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II transcription regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:12992](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12992) · Entrez [7568](https://www.ncbi.nlm.nih.gov/gene/7568) · UniProt [P17024](https://www.uniprot.org/uniprotkb/P17024) · Ensembl [ENSG00000132010](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132010)

## Data

Gene col 5269: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5269); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5269, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5269]; `tensor/DDL_lfc|DDL_z.npy` [5269]; `embed/gene_vectors.npy` [5269]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5269 or target_col == 5269). Every well: [[ZNF20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
