---
symbol: "NECTIN4"
type: "gene"
col: 6699
ensembl_id: "ENSG00000143217"
name: "nectin cell adhesion molecule 4"
location: "1q23.3"
module: 8
arm: "+"
pooled_cpm: 15.89
n_lines_expressing: 17
n_dd_up: 11
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 67
direction_downstream: 89
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# NECTIN4

*nectin cell adhesion molecule 4* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.16× (z +6.3, q 1e-07, up in 0 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 2.14× (z +4.6, q 1e-03, up in 5 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.557× (z -4.9, q 7e-04, down in 12 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (COLO 205 0.0648×, HT-29 0.0441×, Panc 03.27 0.124×, Hs 766T 0.100×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 5 lines (COLO 205 0.0464×, NCI-H2347 0.125×, NCI-H1573 0.121×, HT-29 0.0809×, …; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (COLO 205 0.0943×, NCI-H1573 0.218×, NCI-H2347 0.274×, LS 180 0.168×); [[Auranofin (drug)]] 5 µM in 2 lines (Panc 03.27 0.200×, CFPAC-1 0.234×); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H2347 0.299×, COLO 205 0.234×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP30]] (+0.79, fdr 7e-06, ⚠ same locus), [[ADGRF1]] (+0.76, fdr 7e-06), [[CLDN4]] (+0.72, fdr 7e-06), [[ADCY4]] (+0.70, fdr 7e-06); moves opposite to [[MCM3AP]] (-0.47, fdr 4e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 67 arrows point to it, the strongest [[TMCC3]] → it (grade B ⚠); 89 go from it, the strongest it → [[JUP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6699.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +6.3 | 1e-07 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.14×** | +4.6 | 1e-03 | 5/14 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.4 | 0.002 | 2/14 (NCI-H460, A-172) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +4.1 | 0.005 | 1/13 (A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +3.8 | 0.019 | 1/10 (LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.036 | 1/15 (A-172) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +3.5 | 0.036 | 3/15 (NCI-H460, SW48, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.50×** | +3.3 | 0.059 | 8/15 (A-172, COLO 205, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.059 | 4/16 (HepG2/C3A, HT-29, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.083 | 4/15 (COLO 205, LS 180, …) | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.2 | 0.083 | 1/14 (Hs 766T) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6699.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (COLO 205 0.0648×, HT-29 0.0441×, Panc 03.27 0.124×, Hs 766T 0.100×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 5 lines (COLO 205 0.0464×, NCI-H2347 0.125×, NCI-H1573 0.121×, HT-29 0.0809×, …; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (COLO 205 0.0943×, NCI-H1573 0.218×, NCI-H2347 0.274×, LS 180 0.168×); [[Auranofin (drug)]] 5 µM in 2 lines (Panc 03.27 0.200×, CFPAC-1 0.234×); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H2347 0.299×, COLO 205 0.234×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.557×** | -4.9 | 7e-04 | 12/15 (NCI-H2347, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.658×** | -3.6 | 0.083 | 5/15 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.676× | -3.4 | 0.13 | 11/15 (COLO 205, NCI-H2347, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.690× | -3.2 | 0.19 | 8/15 (COLO 205, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.677× | -3.1 | 0.19 | 0/15 | inconsistent across doses | position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.680× | -3.1 | 0.19 | 1/15 (NCI-H460) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.705× | -3.0 | 0.20 | 6/15 (HepG2/C3A, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6699. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 127 | 0 | 12 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -23.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.274× (z -10.1) |
| [[COLO 205 (line)]] | alt | 74.6 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0464× (z -27.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0943× (z -15.1) |
| [[NCI-H1573 (line)]] | alt | 92.0 | 0 | 10 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -20.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.218× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 30.6 | 0 | 9 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.234× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 47.0 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -19.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.200× (z -10.8) |
| [[Hs 766T (line)]] | wt | 135 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.100× (z -19.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.324× (z -9.7) |
| [[LS 180 (line)]] | wt | 17.9 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -16.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -10.0) |
| [[HT-29 (line)]] | alt | 18.6 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0441× (z -23.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 54.7 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.26 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.55 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.962 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.965 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.26 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6699), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP30]] | +0.79 | +0.77 / +0.76 | both halves | 7e-06 | ⚠ same locus (1.0 kb, same strand: neighbours can correlate without regulation) |
| [[ADGRF1]] | +0.76 | +0.72 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[CLDN4]] | +0.72 | +0.72 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION |
| [[ADCY4]] | +0.70 | +0.68 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[DAPP1]] | +0.69 | +0.63 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SLC44A4]] | +0.69 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[RNF39]] | +0.69 | +0.67 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[ST14]] | +0.69 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[TACSTD2]] | +0.68 | +0.71 / +0.54 | both halves | 1e-05 | STRING 600 |
| [[CLDN7]] | +0.67 | +0.64 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION |
| [[CDH1]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION |
| [[TMPRSS4]] | +0.66 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[SPINT1]] | +0.65 | +0.67 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM3AP]] | -0.47 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*67 arrows, 67 of them with an alert ⚠; grade A 0, B 3, C 64. Shown: the 12 strongest; 55 more arrows (55 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMCC3]] | B | TMCC3 activity raises NECTIN4's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 2.35× lower at baseline in the lines without TMCC3 | 0.049 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[JUP]] | B | JUP activity raises NECTIN4's level | lines that do not express JUP (16) vs lines expressing it (34) | 3.15× lower at baseline in the lines without JUP | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[GRHL3]] | B | GRHL3 activity raises NECTIN4's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 2.91× lower at baseline in the lines without GRHL3 | 0.095 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[RAB25]] | C | RAB25 activity raises NECTIN4's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 6.24× lower at baseline in the lines without RAB25 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |
| [[MPZL2]] | C | MPZL2 activity raises NECTIN4's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 5.88× lower at baseline in the lines without MPZL2 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14; co-absent with the target |
| [[ANKRD22]] | C | ANKRD22 activity raises NECTIN4's level | lines that do not express ANKRD22 (34) vs lines expressing it (16) | 6.65× lower at baseline in the lines without ANKRD22 | 5e-04 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25; co-absent with the target |
| [[IRF6]] | C | IRF6 activity raises NECTIN4's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 6.43× lower at baseline in the lines without IRF6 | 1e-03 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises NECTIN4's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 5.82× lower at baseline in the lines without TMPRSS4 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[TACSTD2]] | C | TACSTD2 activity raises NECTIN4's level | lines that do not express TACSTD2 (34) vs lines expressing it (16) | 6.26× lower at baseline in the lines without TACSTD2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC5A1, PRKCH-AS1, KCNE3; co-absent with the target |
| [[TMEM125]] | C | TMEM125 activity raises NECTIN4's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 5.73× lower at baseline in the lines without TMEM125 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14; co-absent with the target |
| [[MACC1]] | C | MACC1 activity raises NECTIN4's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 5.43× lower at baseline in the lines without MACC1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2; co-absent with the target |
| [[SLC28A3]] | C | SLC28A3 activity raises NECTIN4's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 3.57× lower at baseline in the lines without SLC28A3 | 0.001 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14; co-absent with the target |

### Downstream of this gene

*89 arrows, 89 of them with an alert ⚠; grade A 0, B 24, C 65. Shown: the 12 strongest; 77 more arrows (77 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JUP]] | B | NECTIN4 activity raises JUP's level | lines that do not express NECTIN4 (33) vs lines expressing it (17) | 4.75× lower at baseline in the lines without NECTIN4 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM30B, PRSS8, RAB25 |
| [[EPS8L1]] | B | NECTIN4 activity raises EPS8L1's level | lines that do not express NECTIN4 (33) vs lines expressing it (17) | 3.11× lower at baseline in the lines without NECTIN4 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM30B, PRSS8, RAB25 |
| [[CSTB]] | B | NECTIN4 activity raises CSTB's level | lines that do not express NECTIN4 (33) vs lines expressing it (17) | 2.38× lower at baseline in the lines without NECTIN4 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM30B, PRSS8, RAB25 |
| [[PROM2]] | B | NECTIN4 activity raises PROM2's level | lines that do not express NECTIN4 (33) vs lines expressing it (17) | 2.69× lower at baseline in the lines without NECTIN4 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM30B, PRSS8, RAB25 |
| [[FAM83E]] | B | NECTIN4 activity raises FAM83E's level | lines that do not express NECTIN4 (33) vs lines expressing it (17) | 2.99× lower at baseline in the lines without NECTIN4 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM30B, PRSS8, RAB25 |
| [[TMC6]] | B | NECTIN4 activity raises TMC6's level | lines that do not express NECTIN4 (33) vs lines expressing it (17) | 3.26× lower at baseline in the lines without NECTIN4 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM30B, PRSS8, RAB25 |
| [[ELMO3]] | B | NECTIN4 activity raises ELMO3's level | lines that do not express NECTIN4 (33) vs lines expressing it (17) | 2.10× lower at baseline in the lines without NECTIN4 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM30B, PRSS8, RAB25 |
| [[RDH13]] | B | NECTIN4 activity raises RDH13's level | lines that do not express NECTIN4 (33) vs lines expressing it (17) | 1.97× lower at baseline in the lines without NECTIN4 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM30B, PRSS8, RAB25 |
| [[FAM83E]] | B | NECTIN4 activity weakens FAM83E's drug response | lines that do not express NECTIN4 (24) vs lines expressing it (12) | (z diff -2.36); strongest at Homoharringtonine 5 µM: 1.61x vs 0.36x (z diff -8.9) | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM30B, PRSS8, RAB25; target measured in part of the lines; artifact flags |
| [[ATM]] | B | NECTIN4 activity lowers ATM's level | lines that do not express NECTIN4 (33) vs lines expressing it (17) | 1.58× higher at baseline in the lines without NECTIN4 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM30B, PRSS8, RAB25 |
| [[KPNA7]] | B | NECTIN4 activity raises KPNA7's level | lines that do not express NECTIN4 (33) vs lines expressing it (17) | 2.55× lower at baseline in the lines without NECTIN4 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM30B, PRSS8, RAB25 |
| [[OCLN]] | B | NECTIN4 activity raises OCLN's level | lines that do not express NECTIN4 (33) vs lines expressing it (17) | 3.89× lower at baseline in the lines without NECTIN4 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM30B, PRSS8, RAB25 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.590). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.1, 57.7); signed map (56.3, 7.6). **Vector** length 76.7, 30.1% of its response variance represented; |z| ≥ 3 in 479 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.1 | +1.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +4.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.6 | -0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +4.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.0 | +1.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.6 | +2.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +3.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -3.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.5 | -2.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.5 | -2.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | nectin cell adhesion molecule 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:161,070,998-161,089,558 (-) |
| Ensembl biotype | protein_coding |
| Also known as | nectin-4, PRR4, LNIR; previously PVRL4 |
| Gene groups (HGNC) | V-set domain containing; C2-set domain containing; Nectins and nectin-like molecules |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 5 pathways, smallest: Nectin/Necl  trans heterodimerization; Adherens junctions interactions; Cell-cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96NY8](https://www.uniprot.org/uniprotkb/Q96NY8) (Nectin-4):

> Seems to be involved in cell adhesion through trans-homophilic and -heterophilic interactions, the latter including specifically interactions with NECTIN1. Does not act as receptor for alpha-herpesvirus entry into cells.; (Microbial infection) Acts as a receptor for measles virus.

**Summary**, from NCBI Gene [81607](https://www.ncbi.nlm.nih.gov/gene/81607):

> This gene encodes a member of the nectin family. The encoded protein contains two immunoglobulin-like (Ig-like) C2-type domains and one Ig-like V-type domain. It is involved in cell adhesion through trans-homophilic and -heterophilic interactions. It is a single-pass type I membrane protein. The soluble form is produced by proteolytic cleavage at the cell surface by the metalloproteinase ADAM17/TACE. The secreted form is found in both breast tumor cell lines and breast tumor patients. Mutations …

**Accessions** — [HGNC:19688](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19688) · Entrez [81607](https://www.ncbi.nlm.nih.gov/gene/81607) · UniProt [Q96NY8](https://www.uniprot.org/uniprotkb/Q96NY8) · Ensembl [ENSG00000143217](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143217)

## Data

Gene col 6699: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6699); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6699, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6699]; `tensor/DDL_lfc|DDL_z.npy` [6699]; `embed/gene_vectors.npy` [6699]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6699 or target_col == 6699). Every well: [[NECTIN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NECTIN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
