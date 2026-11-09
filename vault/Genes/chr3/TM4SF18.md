---
symbol: "TM4SF18"
type: "gene"
col: 8774
ensembl_id: "ENSG00000163762"
name: "transmembrane 4 L six family member 18"
location: "3q25.1"
module: 19
arm: "+"
pooled_cpm: 4.86
n_lines_expressing: 17
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# TM4SF18

*transmembrane 4 L six family member 18* — 3q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.39× (z +14.0, q 7e-42, up in 9 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.46× (z +9.6, q 1e-19, up in 4 of 12 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 5 lines (PANC-1 0.0923×, MIA PaCa-2 0.131×, AsPC-1 0.0589×, Hs 766T 0.162×, …); [[Homoharringtonine (drug)]] 5 µM in 4 lines (MIA PaCa-2 0.131×, CFPAC-1 0.167×, PANC-1 0.292×, NCI-H460 0.177×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 4 lines (PANC-1 0.109×, MIA PaCa-2 0.157×, SNU-1 0.107×, Hs 766T 0.176×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.0907×, NCI-H460 0.109×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANK1]] (+0.61, fdr 1e-05), [[GASK1B]] (+0.59, fdr 4e-05), [[PDE7B]] (+0.58, fdr 3e-05); moves opposite to [[ACAP2]] (-0.47, fdr 1e-04), [[MT1X]] (-0.47, fdr 1e-04), [[PEX16]] (-0.46, fdr 8e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LAMB4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8774.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.39×** | +14.0 | 7e-42 | 9/9 (MIA PaCa-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **7.13×** | +13.3 | 1e-37 | 8/8 (NCI-H460, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.85×** | +12.8 | 2e-35 | 5/5 (MIA PaCa-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +9.6 | 1e-19 | 4/12 (Hs 766T, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +5.1 | 4e-05 | 2/13 (Hs 766T, MIA PaCa-2) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.94×** | +5.0 | 5e-05 | 1/9 (A-427) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +4.6 | 3e-04 | 3/12 (CFPAC-1, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.3 | 1e-03 | 5/15 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.98×** | +4.3 | 0.001 | 1/7 (A498) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +4.3 | 0.001 | 2/13 (MIA PaCa-2, C32) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.20×** | +4.2 | 0.001 | 2/9 (A-427, Hs 766T) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.012 | 3/15 (MIA PaCa-2, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.6 | 0.013 | 5/12 (MIA PaCa-2, A498, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.82×** | +3.2 | 0.050 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +3.1 | 0.062 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8774.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 5 lines (PANC-1 0.0923×, MIA PaCa-2 0.131×, AsPC-1 0.0589×, Hs 766T 0.162×, …); [[Homoharringtonine (drug)]] 5 µM in 4 lines (MIA PaCa-2 0.131×, CFPAC-1 0.167×, PANC-1 0.292×, NCI-H460 0.177×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 4 lines (PANC-1 0.109×, MIA PaCa-2 0.157×, SNU-1 0.107×, Hs 766T 0.176×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.0907×, NCI-H460 0.109×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | 0.648× | -3.3 | 0.38 | 11/15 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.656× | -3.2 | 0.38 | 7/15 (MIA PaCa-2, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8774. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 57.5 | 2 (2 ⚠) | 8 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -17.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0907× (z -14.9) |
| [[PANC-1 (line)]] | alt | 18.0 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +9.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.0923× (z -14.4) |
| [[Hs 766T (line)]] | wt | 23.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.39× (z +9.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.162× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 4.82 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 11.8× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -10.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -9.3) |
| [[A-427 (line)]] | wt | 12.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -8.9) |
| [[A549 (line)]] | wt | 8.66 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.40× (z +9.1) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 4.93 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0589× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 7.19 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 16.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.107× (z -8.8) |
| [[A-172 (line)]] | wt | 0.477 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.536 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.434 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.710 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.477 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.485 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.554 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.415 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.507 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.392 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.646 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.445 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.506 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.439 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8774), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANK1]] | +0.61 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[GASK1B]] | +0.59 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[PDE7B]] | +0.58 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[CTSC]] | +0.58 | +0.52 / +0.34 | both halves | 1e-04 |  |
| [[KCNK2]] | +0.56 | +0.44 / +0.40 | both halves | 5e-05 |  |
| [[COL4A6]] | +0.55 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[PRTFDC1]] | +0.55 | +0.28 / +0.56 | both halves | 3e-04 |  |
| [[LYPD1]] | +0.54 | +0.27 / +0.48 | both halves | 3e-04 |  |
| [[QPCT]] | +0.53 | +0.40 / +0.34 | both halves | 1e-04 |  |
| [[HFE]] | +0.53 | +0.37 / +0.56 | both halves | 9e-05 |  |
| [[LINC01139]] | +0.52 | +0.41 / +0.34 | both halves | 1e-04 |  |
| [[F2R]] | +0.51 | +0.50 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACAP2]] | -0.47 | -0.37 / -0.33 | both halves | 1e-04 |  |
| [[MT1X]] | -0.47 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[PEX16]] | -0.46 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[METRNL]] | -0.45 | -0.39 / -0.30 | both halves | 2e-04 |  |
| [[MKNK2]] | -0.45 | -0.29 / -0.36 | both halves | 3e-04 |  |
| [[SYT7]] | -0.44 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[ARRDC1]] | -0.44 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[MT1F]] | -0.44 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[NOL7]] ⚠ | -0.44 | -0.31 / -0.33 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[MPST]] | -0.43 | -0.26 / -0.37 | both halves | 4e-04 |  |
| [[TNIP2]] | -0.43 | -0.35 / -0.29 | both halves | 2e-04 |  |
| [[CEBPB]] | -0.43 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[ZXDC]] | -0.43 | -0.27 / -0.37 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TM4SF18's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DLEU1]] | B | DLEU1 activity raises TM4SF18's level | lines that do not express DLEU1 (16) vs lines expressing it (34) | 1.80× lower at baseline in the lines without DLEU1 | 0.046 | ⚠ within organs, on part of the lines; also absent: MLXIPL, TESC, PDE3B; maybe low, not absent |
| [[LINC02643]] | C | LINC02643 activity raises TM4SF18's level | lines that do not express LINC02643 (38) vs lines expressing it (12) | 2.75× lower at baseline in the lines without LINC02643 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, GCG, ENSG00000289530; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMB4]] | C | TM4SF18 activity raises LAMB4's level | lines that do not express TM4SF18 (33) vs lines expressing it (17) | 1.81× lower at baseline in the lines without TM4SF18 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000244468, LINC01610, SERPINB11; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.538). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.8, 31.2); signed map (45.3, 41.0). **Vector** length 37.3, 8.90% of its response variance represented; |z| ≥ 3 in 359 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +13.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +14.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +12.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +0.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.0 | +2.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.8 | +1.6 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -3.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | -0.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | -1.1 | -1.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.1 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -2.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane 4 L six family member 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.1 — chr3:149,318,498-149,334,414 (-) |
| Ensembl biotype | protein_coding |
| Also known as | L6D |
| Gene groups (HGNC) | Transmembrane 4 L six family |
| Matched by | ensembl_id |

UniProt [Q96CE8](https://www.uniprot.org/uniprotkb/Q96CE8) carries no function annotation.

**Summary**, from NCBI Gene [116441](https://www.ncbi.nlm.nih.gov/gene/116441):

> Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25181](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25181) · Entrez [116441](https://www.ncbi.nlm.nih.gov/gene/116441) · UniProt [Q96CE8](https://www.uniprot.org/uniprotkb/Q96CE8) · Ensembl [ENSG00000163762](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163762)

## Data

Gene col 8774: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8774); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8774, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8774]; `tensor/DDL_lfc|DDL_z.npy` [8774]; `embed/gene_vectors.npy` [8774]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8774 or target_col == 8774). Every well: [[TM4SF18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TM4SF18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
