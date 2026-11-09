---
symbol: "MAPK4"
type: "gene"
col: 6558
ensembl_id: "ENSG00000141639"
name: "mitogen-activated protein kinase 4"
location: "18q21.1-q21.2"
module: 19
arm: "+"
pooled_cpm: 4.7
n_lines_expressing: 15
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 9
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# MAPK4

*mitogen-activated protein kinase 4* — 18q21.1-q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.19× (z +12.3, q 9e-32, up in 4 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H460 0.0501×, BT-474 0.107×, SK-MEL-2 0.158×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.0781×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 0.146×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.181×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPGN]] (+0.66, fdr 1e-05), [[ADGRG2]] (+0.63, fdr 1e-05), [[CPS1]] (+0.61, fdr 1e-05); moves opposite to [[MAGEA4-AS1]] (-0.45, fdr 2e-04), [[NPTX1]] (-0.42, fdr 2e-04), [[ADRA2C]] (-0.42, fdr 6e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[CHL1]] → it (grade C ⚠); 9 go from it, the strongest it → [[SLC26A2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6558.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.19×** | +12.3 | 9e-32 | 4/9 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.83×** | +11.0 | 1e-25 | 6/10 (C32, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.97×** | +9.9 | 8e-21 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.37×** | +9.1 | 2e-17 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.33×** | +7.9 | 4e-13 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.19×** | +5.9 | 4e-07 | 6/12 (NCI-H23, C32, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +5.5 | 3e-06 | 5/7 (SK-MEL-2, LoVo, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.01×** | +5.2 | 1e-05 | 4/10 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.81×** | +4.4 | 6e-04 | 3/10 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.24×** | +4.3 | 1e-03 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.76×** | +4.2 | 0.001 | 5/10 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +4.2 | 0.001 | 3/10 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.74×** | +4.1 | 0.001 | 3/10 (LoVo, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.68×** | +3.9 | 0.005 | 4/10 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +3.7 | 0.009 | 6/10 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.99×** | +3.7 | 0.009 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.97×** | +3.6 | 0.010 | 0/10 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.56×** | +3.3 | 0.025 | 5/10 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +3.3 | 0.025 | 2/10 (SK-MEL-2, C-33 A) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Triamcinolone (drug)]] 0.05 µM |  | **1.55×** | +3.2 | 0.032 | 4/10 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.32×** | +2.9 | 0.075 | 3/10 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.50×** | +2.9 | 0.075 | 4/10 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.71×** | +2.9 | 0.085 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6558.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H460 0.0501×, BT-474 0.107×, SK-MEL-2 0.158×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.0781×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 0.146×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.181×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[9-ING-41 (drug)]] 5 µM |  | 0.439× | -3.2 | 0.35 | 1/10 (NCI-H23) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.653× | -3.1 | 0.35 | 4/10 (C32, C-33 A, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.05 µM |  | 0.649× | -3.1 | 0.35 | 0/10 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6558. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 55.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0501× (z -25.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0781× (z -14.8) |
| [[BT-474 (line)]] | alt | 41.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 7.10 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.887 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.562 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.934 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.876 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.709 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.537 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.806 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.795 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.550 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.775 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.592 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.640 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.859 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.775 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.590 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.619 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.894 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.909 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.742 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.822 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.757 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6558), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPGN]] | +0.66 | +0.51 / +0.68 | both halves | 1e-05 | pathway: MAPK family signaling cascades |
| [[ADGRG2]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[CPS1]] | +0.61 | +0.51 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[SLC15A5]] | +0.60 | +0.39 / +0.75 | both halves | 6e-05 |  |
| [[SNCA]] | +0.59 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[RTN1]] | +0.58 | +0.43 / +0.69 | both halves | 3e-05 |  |
| [[ADGRD1]] | +0.58 | +0.39 / +0.69 | both halves | 5e-05 |  |
| [[LIN7A]] | +0.57 | +0.35 / +0.71 | both halves | 1e-04 |  |
| [[LINC01035]] | +0.57 | +0.43 / +0.65 | both halves | 4e-05 |  |
| [[PALMD]] | +0.55 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[SLC7A2]] | +0.55 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[NRCAM]] | +0.55 | +0.52 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAGEA4-AS1]] | -0.45 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[NPTX1]] | -0.42 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[ADRA2C]] | -0.42 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[SYNJ2]] | -0.41 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[TMEM225B]] | -0.41 | -0.47 / -0.26 | both halves | 4e-04 |  |
| [[BCL10-AS1]] | -0.41 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[KIAA1217]] | -0.41 | -0.46 / -0.29 | both halves | 2e-04 |  |
| [[MSANTD3-TMEFF1]] | -0.41 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[EMP3]] | -0.40 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[PNPLA7]] | -0.40 | -0.40 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHL1]] | C | CHL1 activity raises MAPK4's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 2.60× lower at baseline in the lines without CHL1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168; co-absent with the target |
| [[GTF2I-AS1]] | C | GTF2I-AS1 activity raises MAPK4's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 2.20× lower at baseline in the lines without GTF2I-AS1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[CPS1]] | C | CPS1 activity raises MAPK4's level | lines that do not express CPS1 (36) vs lines expressing it (14) | 1.86× lower at baseline in the lines without CPS1 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, ENSG00000241168, GLP2R; co-absent with the target |
| [[EPGN]] | C | EPGN activity raises MAPK4's level | lines that do not express EPGN (41) vs lines expressing it (9) | 3.31× lower at baseline in the lines without EPGN | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, TBXT, ENSG00000289418; co-absent with the target |
| [[SLC15A5]] | C | SLC15A5 activity raises MAPK4's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 2.71× lower at baseline in the lines without SLC15A5 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent; co-absent with the target |
| [[COL4A4]] | C | COL4A4 activity raises MAPK4's level | lines that do not express COL4A4 (28) vs lines expressing it (22) | 2.11× lower at baseline in the lines without COL4A4 | 0.065 | ⚠ within organs, on part of the lines; also absent: COL4A3, LHX2, EPB41L4A; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises MAPK4's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 2.36× lower at baseline in the lines without LINC03000 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |
| [[TBXT]] | C | TBXT activity raises MAPK4's level | lines that do not express TBXT (47) vs lines expressing it (3) | 5.13× lower at baseline in the lines without TBXT | 0.089 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC26A2]] | B | MAPK4 activity raises SLC26A2's level | lines that do not express MAPK4 (35) vs lines expressing it (15) | 2.11× lower at baseline in the lines without MAPK4 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000289418, SLC15A5, LHFPL3-AS1 |
| [[ADGRG2]] | B | MAPK4 activity raises ADGRG2's level | lines that do not express MAPK4 (35) vs lines expressing it (15) | 1.72× lower at baseline in the lines without MAPK4 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000289418, SLC15A5, LHFPL3-AS1 |
| [[S100P]] | C | MAPK4 activity raises S100P's level | lines that do not express MAPK4 (35) vs lines expressing it (15) | 1.65× lower at baseline in the lines without MAPK4 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000289418, SLC15A5, LHFPL3-AS1; co-absent with the target |
| [[CPS1]] | C | MAPK4 activity raises CPS1's level | lines that do not express MAPK4 (35) vs lines expressing it (15) | 3.56× lower at baseline in the lines without MAPK4 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000289418, SLC15A5, LHFPL3-AS1; co-absent with the target |
| [[KRT6A]] | C | MAPK4 activity raises KRT6A's level | lines that do not express MAPK4 (35) vs lines expressing it (15) | 1.33× lower at baseline in the lines without MAPK4 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000289418, SLC15A5, LHFPL3-AS1; co-absent with the target |
| [[COL4A5]] | C | MAPK4 activity raises COL4A5's level | lines that do not express MAPK4 (35) vs lines expressing it (15) | 4.05× lower at baseline in the lines without MAPK4 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000289418, SLC15A5, LHFPL3-AS1; co-absent with the target |
| [[COL4A4]] | C | MAPK4 activity raises COL4A4's level | lines that do not express MAPK4 (35) vs lines expressing it (15) | 3.18× lower at baseline in the lines without MAPK4 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000289418, SLC15A5, LHFPL3-AS1; co-absent with the target |
| [[NPTX1]] | C | MAPK4 activity raises NPTX1's level | lines that do not express MAPK4 (35) vs lines expressing it (15) | 2.72× lower at baseline in the lines without MAPK4 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000289418, SLC15A5, LHFPL3-AS1; co-absent with the target |
| [[EPGN]] | C | MAPK4 activity raises EPGN's level | lines that do not express MAPK4 (35) vs lines expressing it (15) | 2.56× lower at baseline in the lines without MAPK4 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000289418, SLC15A5, LHFPL3-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.510). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.6, 37.9); signed map (44.8, 44.1). **Vector** length 32.5, 9.10% of its response variance represented; |z| ≥ 3 in 300 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.2 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +9.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +11.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.7 | +3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | +12.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.1 | +3.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.1 | +4.2 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.0 | +2.8 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.0 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -0.9 | -2.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.8 | -0.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.7 | +1.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -0.7 | -0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.7 | -2.4 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.6 | -0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.6 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.1-q21.2 — chr18:50,560,087-50,731,826 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Erk3-related, Erk4; previously PRKM4 |
| Gene groups (HGNC) | Atypical mitogen-activated protein kinases |
| Reactome | 2 pathways, smallest: MAPK6/MAPK4 signaling; MAPK family signaling cascades |
| Matched by | ensembl_id |

**Function**, from UniProt [P31152](https://www.uniprot.org/uniprotkb/P31152) (Mitogen-activated protein kinase 4):

> Atypical MAPK protein. Phosphorylates microtubule-associated protein 2 (MAP2) and MAPKAPK5. The precise role of the complex formed with MAPKAPK5 is still unclear, but the complex follows a complex set of phosphorylation events: upon interaction with atypical MAPKAPK5, ERK4/MAPK4 is phosphorylated at Ser-186 and then mediates phosphorylation and activation of MAPKAPK5, which in turn phosphorylates ERK4/MAPK4. May promote entry in the cell cycle (By similarity).

**Summary**, from NCBI Gene [5596](https://www.ncbi.nlm.nih.gov/gene/5596):

> Mitogen-activated protein kinase 4 is a member of the mitogen-activated protein kinase family. Tyrosine kinase growth factor receptors activate mitogen-activated protein kinases which then translocate into the nucleus and phosphorylate nuclear targets. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2014]

**Accessions** — [HGNC:6878](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6878) · Entrez [5596](https://www.ncbi.nlm.nih.gov/gene/5596) · UniProt [P31152](https://www.uniprot.org/uniprotkb/P31152) · Ensembl [ENSG00000141639](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141639)

## Data

Gene col 6558: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6558); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6558, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6558]; `tensor/DDL_lfc|DDL_z.npy` [6558]; `embed/gene_vectors.npy` [6558]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6558 or target_col == 6558). Every well: [[MAPK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPK4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
