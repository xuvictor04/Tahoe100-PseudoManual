---
symbol: "HOXA6"
type: "gene"
col: 2704
ensembl_id: "ENSG00000106006"
name: "homeobox A6"
location: "7p15.2"
module: 201
arm: "+"
pooled_cpm: 2.88
n_lines_expressing: 37
n_dd_up: 2
n_dd_down: 13
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/201"]
generated_by: "tahoemap"
---

# HOXA6

*homeobox A6* — 7p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.34× (z +6.8, q 8e-09, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.45× (z +4.4, q 0.004, up in 7 of 19 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 5.31×); [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 5.33×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.429× (z -6.9, q 2e-09, down in 21 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXA5]] (+0.79, fdr 7e-06, ⚠ same locus), [[HOXA3]] (+0.73, fdr 7e-06, ⚠ read-through risk), [[HOXA10]] (+0.66, fdr 3e-05, ⚠ same locus), [[LINC00461]] (+0.62, fdr 1e-05), [[INHA]] (+0.56, fdr 5e-05), [[DNAJC27]] (+0.55, fdr 2e-04); moves opposite to [[R3HDM4]] (-0.65, fdr 3e-05), [[MICAL2]] (-0.56, fdr 4e-05), [[PPP1R12C]] (-0.54, fdr 6e-05).
> It is in [[Module 201]], a single-armed module (Kidney development).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HOXA9]] → it (grade B ⚠); 2 go from it, the strongest it → [[HOXA3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2704.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 5.31×); [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 5.33×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +6.8 | 8e-09 | 0/3 | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.4 | 0.004 | 7/19 (LoVo, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.52× | +3.3 | 0.16 | 4/24 (HCT15, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.50× | +3.2 | 0.19 | 4/12 (SW1417, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 1.69× | +3.1 | 0.22 | 2/10 (NCI-H2030, NCI-H460) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2704.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.429×** | -6.9 | 2e-09 | 21/29 (SW 900, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.472×** | -6.2 | 2e-07 | 16/32 (HCT15, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.494×** | -5.8 | 1e-06 | 17/31 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.556×** | -4.8 | 2e-04 | 11/32 (HT-29, Hs 766T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.570×** | -4.4 | 0.001 | 14/27 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.585×** | -4.4 | 0.001 | 12/31 (HT-29, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.618×** | -3.9 | 0.007 | 17/29 (HT-29, SW 900, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.626×** | -3.8 | 0.009 | 10/32 (LS 180, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.648×** | -3.5 | 0.025 | 10/27 (NCI-H460, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.653×** | -3.5 | 0.027 | 9/28 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.647×** | -3.4 | 0.029 | 7/27 (HOP62, CFPAC-1, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.658×** | -3.4 | 0.029 | 15/29 (HT-29, SW 900, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.672×** | -3.1 | 0.095 | 13/25 (LoVo, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2704. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 13.4 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 2.84 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0211× (z -13.4) |
| [[C32 (line)]] | wt | 6.90 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0636× (z -14.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.0678× (z -10.1) |
| [[HCT15 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0629× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[HEC-1-A (line)]] | alt | 3.55 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0612× (z -9.6) |
| [[LoVo (line)]] | wt | 9.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.31× (z +11.4) | — |
| [[LS 180 (line)]] | wt | 7.09 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.33× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 900 (line)]] | alt | 5.77 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0644× (z -9.2) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0586× (z -15.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.503 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.885 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.217 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.345 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.682 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.348 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.516 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.176 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.909 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.194 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.901 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.672 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.778 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.591 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2704), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA5]] | +0.79 | +0.79 / +0.76 | both halves | 7e-06 | same gene group; STRING 969; ⚠ same locus (1.7 kb, same strand: neighbours can correlate without regulation) |
| [[HOXA3]] | +0.73 | +0.71 / +0.66 | both halves | 7e-06 | same gene group; STRING 707; ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of HOXA3 on the same strand (can correlate by spillover, not regulation) |
| [[HOXA10]] | +0.66 | +0.45 / +0.67 | both halves | 3e-05 | same gene group; STRING 553; ⚠ same locus (20.0 kb, same strand: neighbours can correlate without regulation) |
| [[HOXA11]] | +0.62 | +0.57 / +0.57 | both halves | 1e-05 | same gene group; pathway: Kidney development; STRING 523; ⚠ same locus (30.6 kb, same strand: neighbours can correlate without regulation) |
| [[LINC00461]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[HOXA9]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 | same gene group; STRING 530; ⚠ same locus (11.8 kb, same strand: neighbours can correlate without regulation) |
| [[INHA]] | +0.56 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[DNAJC27]] | +0.55 | +0.29 / +0.59 | both halves | 2e-04 |  |
| [[WHAMMP2]] | +0.54 | +0.32 / +0.53 | both halves | 2e-04 |  |
| [[B4GAT1]] | +0.54 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[NR2F1]] | +0.53 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[RPRD2]] | +0.53 | +0.43 / +0.39 | both halves | 5e-05 |  |
| [[CHD6]] | +0.53 | +0.41 / +0.39 | both halves | 6e-05 |  |
| [[RSBN1]] | +0.53 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[ACBD5]] | +0.53 | +0.34 / +0.50 | both halves | 1e-04 |  |
| [[DCAF5]] | +0.52 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[HOXB5]] | +0.51 | +0.39 / +0.47 | both halves | 5e-05 | same gene group; STRING 848 |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[R3HDM4]] | -0.65 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[MICAL2]] | -0.56 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[PPP1R12C]] | -0.54 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[ADAMTSL5]] | -0.54 | -0.37 / -0.56 | both halves | 8e-05 |  |
| [[ARHGAP23]] | -0.53 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[TPCN2]] | -0.53 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[CEP170B]] | -0.51 | -0.40 / -0.54 | both halves | 4e-05 |  |
| [[TELO2]] | -0.49 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[LIMS1]] | -0.49 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[MTG1]] | -0.49 | -0.37 / -0.42 | both halves | 7e-05 |  |
| [[FAAP100]] | -0.48 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[KLF13]] | -0.47 | -0.44 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA9]] | B | HOXA9 activity raises HOXA6's level | lines that do not express HOXA9 (31) vs lines expressing it (19) | 2.23× lower at baseline in the lines without HOXA9 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HOXA11, IGFL2-AS1, GPA33 |
| [[APLN]] | B | APLN activity raises HOXA6's level | lines that do not express APLN (13) vs lines expressing it (37) | 1.54× lower at baseline in the lines without APLN | 0.078 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HOXA3]] | C | HOXA3 activity raises HOXA6's level | lines that do not express HOXA3 (9) vs lines expressing it (41) | 2.51× lower at baseline in the lines without HOXA3 | 0.003 | ⚠ within organs, on part of the lines; also absent: HOXA5, HOXA6, LINC01186; maybe low, not absent; co-absent with the target |
| [[HOXA5]] | C | HOXA5 activity raises HOXA6's level | lines that do not express HOXA5 (9) vs lines expressing it (41) | 2.54× lower at baseline in the lines without HOXA5 | 0.019 | ⚠ within organs, on part of the lines; also absent: HOXA3, HOXA6, HOTAIRM1; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA3]] | C | HOXA6 activity raises HOXA3's level | lines that do not express HOXA6 (13) vs lines expressing it (37) | 3.53× lower at baseline in the lines without HOXA6 | 0.001 | ⚠ within organs, on part of the lines; also absent: HOXA3, HOXA5; maybe low, not absent; co-absent with the target |
| [[HOXA5]] | C | HOXA6 activity raises HOXA5's level | lines that do not express HOXA6 (13) vs lines expressing it (37) | 2.81× lower at baseline in the lines without HOXA6 | 0.007 | ⚠ within organs, on part of the lines; also absent: HOXA3, HOXA5; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 201]] — Kidney development; 15 genes; every member is in the + arm (projection on the module's main direction 0.752). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.1, 27.5); signed map (-5.1, 6.7). **Vector** length 45.3, 7.01% of its response variance represented; |z| ≥ 3 in 774 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +2.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +2.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | -0.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +0.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.1 | +1.1 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +1.0 | +2.2 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -2.1 | -5.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.0 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -4.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.6 | -3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | +0.5 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | homeobox A6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.2 — chr7:27,145,396-27,150,603 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX1B, HOX1 |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Reactome | 2 pathways, smallest: Formation of the nephric duct; Kidney development |
| Matched by | ensembl_id |

**Function**, from UniProt [P31267](https://www.uniprot.org/uniprotkb/P31267) (Homeobox protein Hox-A6):

> Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis.

**Summary**, from NCBI Gene [3203](https://www.ncbi.nlm.nih.gov/gene/3203):

> In vertebrates, the genes encoding the class of transcription factors called homeobox genes are found in clusters named A, B, C, and D on four separate chromosomes. Expression of these proteins is spatially and temporally regulated during embryonic development. This gene is part of the A cluster on chromosome 7 and encodes a DNA-binding transcription factor which may regulate gene expression, morphogenesis, and differentiation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5107](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5107) · Entrez [3203](https://www.ncbi.nlm.nih.gov/gene/3203) · UniProt [P31267](https://www.uniprot.org/uniprotkb/P31267) · Ensembl [ENSG00000106006](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106006)

## Data

Gene col 2704: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2704); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2704, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2704]; `tensor/DDL_lfc|DDL_z.npy` [2704]; `embed/gene_vectors.npy` [2704]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2704 or target_col == 2704). Every well: [[HOXA6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXA6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
