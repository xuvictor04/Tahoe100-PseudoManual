---
symbol: "FAM83A"
type: "gene"
col: 7218
ensembl_id: "ENSG00000147689"
name: "scaffolding CK1 anchoring protein A"
location: "8q24.13"
module: 31
arm: "+"
pooled_cpm: 49.6
n_lines_expressing: 13
n_dd_up: 2
n_dd_down: 18
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 25
direction_downstream: 50
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# FAM83A

*scaffolding CK1 anchoring protein A* — 8q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.60× (z +6.8, q 5e-09, up in 0 of 12 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Dexamethasone (drug)]] 0.5 µM in 1 line (Hs 766T 11.1×); [[Dexamethasone (drug)]] 0.05 µM in 1 line (Hs 766T 9.89×).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.338× (z -7.7, q 7e-12, down in 10 of 11 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GSDMC]] (+0.69, fdr 7e-06), [[PRSS8]] (+0.62, fdr 7e-06), [[P2RY2]] (+0.60, fdr 1e-05); moves opposite to [[ABCG2]] (-0.46, fdr 4e-05), [[CNNM1]] (-0.45, fdr 4e-05), [[NFIX]] (-0.41, fdr 2e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[PLEK2]] → it (grade B ⚠); 50 go from it, the strongest it → [[RAPGEF3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7218.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Dexamethasone (drug)]] 0.5 µM in 1 line (Hs 766T 11.1×); [[Dexamethasone (drug)]] 0.05 µM in 1 line (Hs 766T 9.89×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.60×** | +6.8 | 5e-09 | 0/12 | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +4.1 | 0.013 | 0/10 | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.66× | +3.4 | 0.15 | 0/10 | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7218.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.338×** | -7.7 | 7e-12 | 10/11 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.470×** | -7.6 | 9e-12 | 11/11 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.445×** | -5.5 | 6e-06 | 10/11 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.586×** | -5.4 | 1e-05 | 11/11 (NCI-H2347, J82, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **0.497×** | -5.0 | 8e-05 | 11/11 (AsPC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.513×** | -4.8 | 2e-04 | 10/11 (AsPC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.498×** | -4.6 | 4e-04 | 7/11 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.584×** | -3.5 | 0.029 | 2/11 (A549, J82) | inconsistent across doses | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.614×** | -3.5 | 0.034 | 0/11 | two highest doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.633×** | -3.3 | 0.056 | 5/11 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.633×** | -3.2 | 0.056 | 11/11 (AsPC-1, NCI-H1573, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.634×** | -3.2 | 0.056 | 9/11 (AsPC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.635×** | -3.2 | 0.056 | 11/11 (AsPC-1, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.720×** | -3.2 | 0.064 | 4/11 (AsPC-1, BT-474, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.645×** | -3.1 | 0.067 | 9/11 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[Encorafenib (drug)]] 5 µM |  | **0.378×** | -3.1 | 0.067 | 3/11 (HT-29, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.385×** | -3.0 | 0.077 | 9/12 (AsPC-1, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.645×** | -3.0 | 0.087 | 6/11 (A549, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7218. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 925 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.00932× (z -40.1) |
| [[J82 (line)]] | alt | 31.2 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0747× (z -15.9) |
| [[NCI-H2347 (line)]] | alt | 320 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0626× (z -25.7) |
| [[NCI-H1573 (line)]] | alt | 81.5 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0350× (z -19.9) |
| [[CFPAC-1 (line)]] | alt | 229 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0289× (z -30.8) |
| [[Panc 03.27 (line)]] | alt | 241 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0988× (z -22.2) |
| [[HT-29 (line)]] | alt | 27.4 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0831× (z -13.9) |
| [[BT-474 (line)]] | alt | 25.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -10.5) |
| [[Hs 766T (line)]] | wt | 28.6 | 2 | 1 | [[Dexamethasone (drug)]] 0.5 µM 11.1× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.0960× (z -12.3) |
| [[A549 (line)]] | wt | 15.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -13.5) |
| [[A-172 (line)]] | wt | 5.65 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.69 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.27 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.74 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.34 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.81 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.06 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.19 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.79 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.25 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.39 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.98 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.71 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.75 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.50 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.14 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.74 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.40 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.30 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.43 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.80 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7218), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSDMC]] | +0.69 | +0.72 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[PRSS8]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[P2RY2]] | +0.60 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[SDR16C5]] | +0.57 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[KRT6A]] | +0.57 | +0.48 / +0.56 | both halves | 2e-05 | **novel candidate** |
| [[CORO2A]] | +0.57 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[LINC02725]] | +0.57 | +0.53 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[PTK6]] | +0.57 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[S100A9]] | +0.56 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[CYTH1]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[LINC01610]] | +0.54 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[S100P]] | +0.54 | +0.47 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCG2]] | -0.46 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[CNNM1]] | -0.45 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[NFIX]] | -0.41 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[LRRN1]] | -0.40 | -0.40 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 2, C 23. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEK2]] | B | PLEK2 activity raises FAM83A's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 2.76× lower at baseline in the lines without PLEK2 | 0.040 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[SEMA3B]] | B | SEMA3B activity raises FAM83A's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 1.82× lower at baseline in the lines without SEMA3B | 0.060 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[SCEL]] | C | SCEL activity raises FAM83A's level | lines that do not express SCEL (35) vs lines expressing it (15) | 5.44× lower at baseline in the lines without SCEL | 0.001 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1; co-absent with the target |
| [[S100A14]] | C | S100A14 activity raises FAM83A's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 4.39× lower at baseline in the lines without S100A14 | 0.001 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises FAM83A's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 4.34× lower at baseline in the lines without TMPRSS4 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[P2RY2]] | C | P2RY2 activity raises FAM83A's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 3.93× lower at baseline in the lines without P2RY2 | 0.001 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223; co-absent with the target |
| [[GSDMC]] | C | GSDMC activity raises FAM83A's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 14.01× lower at baseline in the lines without GSDMC | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1; co-absent with the target |
| [[HS3ST1]] | C | HS3ST1 activity raises FAM83A's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 4.05× lower at baseline in the lines without HS3ST1 | 0.004 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4; co-absent with the target |
| [[FAM83B]] | C | FAM83B activity raises FAM83A's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 3.97× lower at baseline in the lines without FAM83B | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14; co-absent with the target |
| [[CEACAM1]] | C | CEACAM1 activity raises FAM83A's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 3.66× lower at baseline in the lines without CEACAM1 | 0.005 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29; co-absent with the target |
| [[FOXQ1]] | C | FOXQ1 activity raises FAM83A's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 3.73× lower at baseline in the lines without FOXQ1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1; co-absent with the target |
| [[FUT3]] | C | FUT3 activity raises FAM83A's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 2.06× lower at baseline in the lines without FUT3 | 0.011 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004; co-absent with the target |

### Downstream of this gene

*50 arrows, 50 of them with an alert ⚠; grade A 0, B 23, C 27. Shown: the 12 strongest; 38 more arrows (38 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAPGEF3]] | B | FAM83A activity raises RAPGEF3's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 2.12× lower at baseline in the lines without FAM83A | 0.005 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9 |
| [[FAM83E]] | B | FAM83A activity raises FAM83E's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 1.99× lower at baseline in the lines without FAM83A | 0.006 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9 |
| [[UNC13D]] | B | FAM83A activity raises UNC13D's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 2.71× lower at baseline in the lines without FAM83A | 0.015 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9 |
| [[PTK6]] | B | FAM83A activity raises PTK6's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 2.50× lower at baseline in the lines without FAM83A | 0.016 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9 |
| [[TMC6]] | B | FAM83A activity raises TMC6's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 1.65× lower at baseline in the lines without FAM83A | 0.018 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9 |
| [[ST3GAL1]] | B | FAM83A activity raises ST3GAL1's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 2.99× lower at baseline in the lines without FAM83A | 0.021 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9 |
| [[ARHGEF34P]] | B | FAM83A activity raises ARHGEF34P's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 2.09× lower at baseline in the lines without FAM83A | 0.023 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9 |
| [[RDH13]] | B | FAM83A activity raises RDH13's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 1.67× lower at baseline in the lines without FAM83A | 0.023 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9 |
| [[PTK2B]] | B | FAM83A activity raises PTK2B's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 2.40× lower at baseline in the lines without FAM83A | 0.024 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9 |
| [[SERINC2]] | B | FAM83A activity raises SERINC2's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 2.12× lower at baseline in the lines without FAM83A | 0.026 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9 |
| [[PKP2]] | B | FAM83A activity raises PKP2's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 2.21× lower at baseline in the lines without FAM83A | 0.041 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9 |
| [[ZNF185]] | B | FAM83A activity raises ZNF185's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 3.65× lower at baseline in the lines without FAM83A | 0.042 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.457). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.2, 59.7); signed map (2.0, 37.2). **Vector** length 79.8, 35.6% of its response variance represented; |z| ≥ 3 in 543 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +2.2 | -4.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.0 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.6 | +2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +1.6 | +1.3 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.6 | +2.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.5 | +1.7 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.5 | +1.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.4 | -5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -1.7 | -3.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -2.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.6 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -4.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.4 | -0.1 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | scaffolding CK1 anchoring protein A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.13 — chr8:123,178,960-123,210,079 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC14128, BJ-TSA-9; previously FAM83A |
| Gene groups (HGNC) | Scaffolding anchor of CK1 domain containing |
| Reactome | 2 pathways, smallest: Signaling by EGFR; Signaling by Receptor Tyrosine Kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UY5](https://www.uniprot.org/uniprotkb/Q86UY5) (Scaffolding CK1 anchoring protein A):

> Involved in mitochondrial maintenance during adipogenesis. May be acting by playing a role in the maintenance of normal mitochondrial function.

**Summary**, from NCBI Gene [84985](https://www.ncbi.nlm.nih.gov/gene/84985):

> Enables identical protein binding activity; phosphatidylinositol 3-kinase regulatory subunit binding activity; and protein kinase binding activity. Involved in cell population proliferation and epidermal growth factor receptor signaling pathway. Predicted to be located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28210](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28210) · Entrez [84985](https://www.ncbi.nlm.nih.gov/gene/84985) · UniProt [Q86UY5](https://www.uniprot.org/uniprotkb/Q86UY5) · Ensembl [ENSG00000147689](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147689)

## Data

Gene col 7218: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7218); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7218, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7218]; `tensor/DDL_lfc|DDL_z.npy` [7218]; `embed/gene_vectors.npy` [7218]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7218 or target_col == 7218). Every well: [[FAM83A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM83A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
