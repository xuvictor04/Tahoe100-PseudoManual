---
symbol: "STARD10"
type: "gene"
col: 13207
ensembl_id: "ENSG00000214530"
name: "StAR related lipid transfer domain containing 10"
location: "11q13.4"
module: 4
arm: "-"
pooled_cpm: 12.05
n_lines_expressing: 46
n_dd_up: 4
n_dd_down: 7
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 7
direction_downstream: 1
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# STARD10

*StAR related lipid transfer domain containing 10* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.72× (z +4.6, q 0.002, up in 19 of 36 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~25% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 3.33×; ⚠ cell-cycle shift, explains ~85% of this change).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.558× (z -5.0, q 4e-04, down in 28 of 43 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[TAK-901 (drug)]] 0.05 µM: 0.617× (z -3.9, q 0.013, down in 23 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LTB]] (+0.66, fdr 2e-05), [[NINJ1]] (+0.64, fdr 1e-05), [[SELENOM]] (+0.63, fdr 1e-05); moves opposite to [[NUP155]] (-0.66, fdr 1e-05), [[PRKDC]] (-0.66, fdr 7e-06), [[RPE]] (-0.66, fdr 8e-06).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[C11orf52]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PRR5L]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13207.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 3.33×; ⚠ cell-cycle shift, explains ~85% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **1.72×** | +4.6 | 0.002 | 19/36 (BT-474, SHP-77, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +4.2 | 0.009 | 9/44 (HT-29, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +3.6 | 0.047 | 14/33 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.35×** | +3.6 | 0.047 | 15/37 (PANC-1, HEC-1-A, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +3.5 | 0.059 | 9/18 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.88× | +3.2 | 0.14 | 6/37 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.44× | +3.1 | 0.14 | 11/42 (NCI-H2347, LS 180, …) | inconsistent across doses |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.42× | +3.0 | 0.18 | 14/41 (LS 180, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13207.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.558×** | -5.0 | 4e-04 | 28/43 (COLO 205, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.618×** | -4.1 | 0.013 | 20/42 (COLO 205, HT-29, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.618×** | -3.9 | 0.013 | 23/42 (HT-29, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.617×** | -3.9 | 0.013 | 23/43 (LOX-IMVI, LS 180, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.636×** | -3.8 | 0.013 | 22/43 (HT-29, HS-578T, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.638×** | -3.8 | 0.013 | 21/43 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.462×** | -3.2 | 0.099 | 17/37 (LS 180, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 0.688× | -3.2 | 0.11 | 17/42 (RPMI-7951, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13207. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 34.0 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0150× (z -22.4) |
| [[HT-29 (line)]] | alt | 65.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 6.60 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0553× (z -10.0) |
| [[PANC-1 (line)]] | alt | 6.21 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +8.5) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[SW480 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0953× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.23 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13207), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LTB]] | +0.66 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[NINJ1]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[SELENOM]] | +0.63 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[PIK3IP1]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ZNF821]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[SNHG9]] | +0.62 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[ZMYM5]] | +0.62 | +0.42 / +0.70 | both halves | 4e-05 |  |
| [[ABCA5]] | +0.61 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[AFTPH]] | +0.60 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[STAP2]] | +0.60 | +0.49 / +0.63 | both halves | 2e-05 |  |
| [[LIME1]] | +0.60 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[TERF2IP]] | +0.59 | +0.42 / +0.68 | both halves | 4e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP155]] | -0.66 | -0.54 / -0.72 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.66 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[RPE]] | -0.66 | -0.58 / -0.70 | both halves | 8e-06 |  |
| [[EIF2S1]] | -0.64 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[EFTUD2]] | -0.63 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[CCT5]] | -0.63 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[CCT2]] | -0.62 | -0.47 / -0.65 | both halves | 2e-05 |  |
| [[MRPS27]] | -0.61 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[AGPS]] | -0.61 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[XRCC5]] | -0.61 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[ELAC2]] | -0.61 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[HEATR1]] | -0.60 | -0.55 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C11orf52]] | B | C11orf52 activity raises STARD10's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 2.18× lower at baseline in the lines without C11orf52 | 0.012 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[DYRK3]] | B | DYRK3 activity lowers STARD10's level | lines that do not express DYRK3 (7) vs lines expressing it (43) | 3.60× higher at baseline in the lines without DYRK3 | 0.030 | ⚠ within organs, on part of the lines; also absent: SCHIP1, ROBO3, DZIP1L; maybe low, not absent |
| [[CGNL1]] | B | CGNL1 activity raises STARD10's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 1.45× lower at baseline in the lines without CGNL1 | 0.064 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |
| [[C11orf52]] | B | C11orf52 activity strengthens STARD10's drug response | lines that do not express C11orf52 (20) vs lines expressing it (24) | the lines without C11orf52 respond 0.73× as strongly (z diff +0.63); rises at some drug-doses, falls at others (32% from rises): Dinaciclib 0.5 µM: 0.80x vs 1.30x (z diff +2.6); Panobinostat 0.5 µM: 0.72x vs 0.53x (z diff +2.1); Panobinostat 5 µM: 0.59x vs 0.48x (z diff +1.6) | 0.081 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises STARD10's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SELENOM]] | B | SELENOM activity weakens STARD10's drug response | lines that do not express SELENOM (12) vs lines expressing it (32) | the lines without SELENOM respond 1.14× as strongly (z diff -0.29); rises at some drug-doses, falls at others (46% from rises): Panobinostat 0.5 µM: 0.57x vs 0.62x (z diff -1.6); Dinaciclib 0.5 µM: 1.28x vs 1.00x (z diff -1.5); Adagrasib 0.05 µM: 1.16x vs 1.11x (z diff -1.1) | 0.086 | ⚠ within organs, on part of the lines; also absent: PNMA2, C3orf18, RFPL1S; target measured in part of the lines; both ways; rises at some drug-doses, falls at others; artifact flags |
| [[GRB7]] | B | GRB7 activity raises STARD10's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 2.19× lower at baseline in the lines without GRB7 | 0.094 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRR5L]] | C | STARD10 activity lowers PRR5L's level | lines that do not express STARD10 (4) vs lines expressing it (46) | 2.11× higher at baseline in the lines without STARD10 | 0.064 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CARD10, DNM1, SDC1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.676). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-23.5, -33.5); signed map (-8.7, 4.7). **Vector** length 78.9, 18.2% of its response variance represented; |z| ≥ 3 in 657 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | +7.2 | +3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +3.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +3.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | +2.5 | +4.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.5 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | -1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +1.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +1.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.7 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -1.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.4 | -3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | StAR related lipid transfer domain containing 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:72,754,729-72,794,047 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NY-CO-28, CGI-52, PCTP2; previously SDCCAG28 |
| Gene groups (HGNC) | StAR related lipid transfer domain containing |
| Reactome | 4 pathways, smallest: Synthesis of PC; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y365](https://www.uniprot.org/uniprotkb/Q9Y365) (START domain-containing protein 10):

> May play metabolic roles in sperm maturation or fertilization (By similarity). Phospholipid transfer protein that preferentially selects lipid species containing a palmitoyl or stearoyl chain on the sn-1 and an unsaturated fatty acyl chain (18:1 or 18:2) on the sn-2 position. Able to transfer phosphatidylcholine (PC) and phosphatidyetanolamline (PE) between membranes.

**Summary**, from NCBI Gene [10809](https://www.ncbi.nlm.nih.gov/gene/10809):

> Predicted to enable lipid carrier activity and phosphatidylcholine binding activity. Predicted to be involved in phosphatidylcholine biosynthetic process. Predicted to act upstream of or within bile acid secretion and positive regulation of peroxisome proliferator activated receptor signaling pathway. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:10666](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10666) · Entrez [10809](https://www.ncbi.nlm.nih.gov/gene/10809) · UniProt [Q9Y365](https://www.uniprot.org/uniprotkb/Q9Y365) · Ensembl [ENSG00000214530](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214530)

## Data

Gene col 13207: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13207); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13207, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13207]; `tensor/DDL_lfc|DDL_z.npy` [13207]; `embed/gene_vectors.npy` [13207]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13207 or target_col == 13207). Every well: [[STARD10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STARD10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
