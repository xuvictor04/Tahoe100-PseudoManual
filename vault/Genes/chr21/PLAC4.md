---
symbol: "PLAC4"
type: "gene"
col: 15952
ensembl_id: "ENSG00000280109"
name: "placenta associated 4"
location: "21q22.2"
module: 19
arm: "+"
pooled_cpm: 5.23
n_lines_expressing: 38
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 15
direction_downstream: 12
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# PLAC4

*placenta associated 4* — 21q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 4.34× (z +12.2, q 2e-31, up in 18 of 28 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (C32 53.5×).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.503× (z -5.5, q 3e-05, down in 17 of 29 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERPINB11]] (+0.74, fdr 7e-06), [[SCUBE1]] (+0.71, fdr 7e-06), [[DPP10]] (+0.71, fdr 9e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[GTF2I-AS1]] → it (grade B ⚠); 12 go from it, the strongest it → [[BACE2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 9 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15952.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (C32 53.5×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **4.34×** | +12.2 | 2e-31 | 18/28 (C32, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.87×** | +8.1 | 2e-13 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.47×** | +7.5 | 1e-11 | 2/5 (HS-578T, HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +6.9 | 7e-10 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.56×** | +4.1 | 0.005 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +4.0 | 0.005 | 2/16 (SK-MEL-2, A549) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.84×** | +3.6 | 0.024 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.50×** | +3.4 | 0.045 | 3/18 (NCI-H1792, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.4 | 0.045 | 1/16 (HOP62) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +3.4 | 0.045 | 1/6 (RKO) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 2.00× | +3.0 | 0.13 | 0/2 | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15952.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.503×** | -5.5 | 3e-05 | 17/29 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.641×** | -3.7 | 0.056 | 7/32 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.647×** | -3.6 | 0.056 | 9/34 (NCI-H460, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.651×** | -3.5 | 0.056 | 13/22 (NCI-H460, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.637×** | -3.4 | 0.065 | 7/32 (NCI-H460, SNU-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.667×** | -3.3 | 0.075 | 11/31 (NCI-H460, A549, …) | top dose only |  |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.648×** | -3.3 | 0.075 | 5/34 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.655×** | -3.2 | 0.084 | 5/32 (A549, NCI-H1573, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.678×** | -3.2 | 0.084 | 9/31 (NCI-H460, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15952. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 71.7 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0555× (z -14.0) |
| [[C32 (line)]] | wt | 3.51 | 1 | 0 | [[Auranofin (drug)]] 5 µM 53.5× (z +11.4) | — |
| [[SW480 (line)]] | alt | 2.18 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0988× (z -8.5) |
| [[A-172 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.985 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15952), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPINB11]] | +0.74 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[SCUBE1]] | +0.71 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[DPP10]] | +0.71 | +0.57 / +0.73 | both halves | 9e-06 |  |
| [[NCKAP5-AS2]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[CTNND2]] | +0.68 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[SPDYE10]] | +0.68 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[SCARA5]] | +0.68 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[FENDRR]] | +0.67 | +0.57 / +0.65 | both halves | 9e-06 | same gene group |
| [[KCNK2]] | +0.66 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[CHL1]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[GREM2]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[SLITRK4]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 14, C 1. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GTF2I-AS1]] | B | GTF2I-AS1 activity raises PLAC4's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 3.56× lower at baseline in the lines without GTF2I-AS1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent |
| [[LINC03000]] | B | LINC03000 activity raises PLAC4's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 3.67× lower at baseline in the lines without LINC03000 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4 |
| [[SLC15A5]] | B | SLC15A5 activity raises PLAC4's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 3.77× lower at baseline in the lines without SLC15A5 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent |
| [[SCARA5]] | B | SCARA5 activity raises PLAC4's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 3.26× lower at baseline in the lines without SCARA5 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5 |
| [[CHL1]] | B | CHL1 activity raises PLAC4's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 2.93× lower at baseline in the lines without CHL1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168 |
| [[SERPINB11]] | B | SERPINB11 activity raises PLAC4's level | lines that do not express SERPINB11 (43) vs lines expressing it (7) | 3.39× lower at baseline in the lines without SERPINB11 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SUCNR1, HOPX |
| [[GLP2R]] | B | GLP2R activity raises PLAC4's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 3.04× lower at baseline in the lines without GLP2R | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054 |
| [[GREM2]] | B | GREM2 activity raises PLAC4's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 2.28× lower at baseline in the lines without GREM2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054 |
| [[CTNND2]] | B | CTNND2 activity raises PLAC4's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 2.23× lower at baseline in the lines without CTNND2 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent |
| [[LINC01967]] | B | LINC01967 activity raises PLAC4's level | lines that do not express LINC01967 (38) vs lines expressing it (12) | 2.13× lower at baseline in the lines without LINC01967 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000234352, SLC15A5, PCSK1 |
| [[FENDRR]] | B | FENDRR activity raises PLAC4's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 2.15× lower at baseline in the lines without FENDRR | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10 |
| [[DPP10]] | B | DPP10 activity raises PLAC4's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 2.29× lower at baseline in the lines without DPP10 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BACE2]] | B | PLAC4 activity raises BACE2's level | lines that do not express PLAC4 (12) vs lines expressing it (38) | 4.93× lower at baseline in the lines without PLAC4 | 0.007 | ⚠ within organs, on part of the lines; also absent: FAM3B, TXNIP, SNCAIP; maybe low, not absent |
| [[SHC4]] | B | PLAC4 activity raises SHC4's level | lines that do not express PLAC4 (12) vs lines expressing it (38) | 2.66× lower at baseline in the lines without PLAC4 | 0.023 | ⚠ within organs, on part of the lines; also absent: FAM3B, TXNIP, SNCAIP; maybe low, not absent |
| [[PDE7B]] | B | PLAC4 activity raises PDE7B's level | lines that do not express PLAC4 (12) vs lines expressing it (38) | 2.24× lower at baseline in the lines without PLAC4 | 0.047 | ⚠ within organs, on part of the lines; also absent: FAM3B, TXNIP, SNCAIP; maybe low, not absent |
| [[TMEM154]] | B | PLAC4 activity raises TMEM154's level | lines that do not express PLAC4 (12) vs lines expressing it (38) | 1.80× lower at baseline in the lines without PLAC4 | 0.048 | ⚠ within organs, on part of the lines; also absent: FAM3B, TXNIP, SNCAIP; maybe low, not absent |
| [[RGS2]] | B | PLAC4 activity raises RGS2's level | lines that do not express PLAC4 (12) vs lines expressing it (38) | 1.91× lower at baseline in the lines without PLAC4 | 0.059 | ⚠ within organs, on part of the lines; also absent: FAM3B, TXNIP, SNCAIP; maybe low, not absent |
| [[PAK3]] | B | PLAC4 activity raises PAK3's level | lines that do not express PLAC4 (12) vs lines expressing it (38) | 1.91× lower at baseline in the lines without PLAC4 | 0.061 | ⚠ within organs, on part of the lines; also absent: FAM3B, TXNIP, SNCAIP; maybe low, not absent |
| [[SCUBE1]] | B | PLAC4 activity raises SCUBE1's level | lines that do not express PLAC4 (12) vs lines expressing it (38) | 1.86× lower at baseline in the lines without PLAC4 | 0.070 | ⚠ within organs, on part of the lines; also absent: FAM3B, TXNIP, SNCAIP; maybe low, not absent |
| [[LINC00922]] | B | PLAC4 activity raises LINC00922's level | lines that do not express PLAC4 (12) vs lines expressing it (38) | 1.98× lower at baseline in the lines without PLAC4 | 0.076 | ⚠ within organs, on part of the lines; also absent: FAM3B, TXNIP, SNCAIP; maybe low, not absent |
| [[NRCAM]] | B | PLAC4 activity raises NRCAM's level | lines that do not express PLAC4 (12) vs lines expressing it (38) | 1.58× lower at baseline in the lines without PLAC4 | 0.079 | ⚠ within organs, on part of the lines; also absent: FAM3B, TXNIP, SNCAIP; maybe low, not absent |
| [[LINC01583]] | B | PLAC4 activity raises LINC01583's level | lines that do not express PLAC4 (12) vs lines expressing it (38) | 1.64× lower at baseline in the lines without PLAC4 | 0.087 | ⚠ within organs, on part of the lines; also absent: FAM3B, TXNIP, SNCAIP; maybe low, not absent |
| [[LINC02742]] | B | PLAC4 activity raises LINC02742's level | lines that do not express PLAC4 (12) vs lines expressing it (38) | 1.70× lower at baseline in the lines without PLAC4 | 0.089 | ⚠ within organs, on part of the lines; also absent: FAM3B, TXNIP, SNCAIP; maybe low, not absent |
| [[ST8SIA4]] | B | PLAC4 activity raises ST8SIA4's level | lines that do not express PLAC4 (12) vs lines expressing it (38) | 1.87× lower at baseline in the lines without PLAC4 | 0.093 | ⚠ within organs, on part of the lines; also absent: FAM3B, TXNIP, SNCAIP; maybe low, not absent |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.673). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.9, 35.7); signed map (42.3, 45.1). **Vector** length 43.8, 6.42% of its response variance represented; |z| ≥ 3 in 775 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.4 | +12.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.9 | -0.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | -0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +1.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -3.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.8 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.8 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -2.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.5 | -2.9 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | placenta associated 4 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 21q22.2 — chr21:41,175,231-41,186,788 (-) |
| Ensembl biotype | lncRNA |
| Also known as | MGC126664, MGC126666, PRED78; previously C21orf115 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

UniProt [Q8WY50](https://www.uniprot.org/uniprotkb/Q8WY50) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:14616](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14616) · Entrez [191585](https://www.ncbi.nlm.nih.gov/gene/191585) · UniProt [Q8WY50](https://www.uniprot.org/uniprotkb/Q8WY50) · Ensembl [ENSG00000280109](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000280109)

## Data

Gene col 15952: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15952); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15952, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15952]; `tensor/DDL_lfc|DDL_z.npy` [15952]; `embed/gene_vectors.npy` [15952]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15952 or target_col == 15952). Every well: [[PLAC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLAC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
