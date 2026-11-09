---
symbol: "ITGBL1"
type: "gene"
col: 12612
ensembl_id: "ENSG00000198542"
name: "integrin subunit beta like 1"
location: "13q33.1"
module: 121
arm: "+"
pooled_cpm: 52.65
n_lines_expressing: 20
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 9
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# ITGBL1

*integrin subunit beta like 1* — 13q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.22× (z +23.7, q 0e+00, up in 12 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[GSK1059615 (drug)]] 5 µM: 0.574× (z -4.2, q 0.018, down in 9 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (NCI-H460 0.151×, A-172 0.311×, NCI-H1792 0.292×, Panc 03.27 0.485×); [[Panobinostat (drug)]] 0.5 µM in 3 lines (Panc 03.27 0.114×, Hs 766T 0.0929×, NCI-H460 0.250×; ⚠ cell-cycle shift, explains ~52% of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (Panc 03.27 0.163×, NCI-H460 0.191×, Hs 766T 0.107×; ⚠ cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 3 lines (NCI-H460 0.249×, Panc 03.27 0.280×, A-427 0.333×); [[Homoharringtonine (drug)]] 5 µM in 1 line (Panc 03.27 0.380×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NALCN]] (+0.64, fdr 1e-05, ⚠ same locus), [[EPHA5]] (+0.63, fdr 1e-05), [[SYT14]] (+0.61, fdr 1e-05), [[DISC1FP1]] (+0.61, fdr 3e-05); moves opposite to [[EEF1AKMT4]] (-0.54, fdr 2e-05), [[ZCCHC17]] (-0.49, fdr 3e-05), [[NFATC3]] (-0.47, fdr 5e-05).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NALCN]] → it (grade C ⚠); 9 go from it, the strongest it → [[DCLK1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12612.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.22×** | +23.7 | 0e+00 | 12/18 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.20×** | +16.7 | 0e+00 | 7/17 (H4, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +10.4 | 7e-23 | 4/15 (H4, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +10.1 | 8e-22 | 9/18 (SHP-77, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +9.9 | 4e-21 | 6/17 (CFPAC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +8.6 | 5e-16 | 11/18 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +7.7 | 1e-12 | 11/18 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +6.1 | 8e-08 | 0/18 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +4.9 | 5e-05 | 6/18 (J82, SHP-77, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +4.7 | 1e-04 | 6/18 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.58×** | +4.7 | 1e-04 | 2/18 (SHP-77, H4) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.54×** | +4.4 | 5e-04 | 3/18 (SNU-423, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.019 | 7/18 (H4, RPMI-7951, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +3.5 | 0.021 | 4/17 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.087 | 5/18 (C32, A-172, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.16× | +3.0 | 0.087 | 4/18 (C32, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12612.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (NCI-H460 0.151×, A-172 0.311×, NCI-H1792 0.292×, Panc 03.27 0.485×); [[Panobinostat (drug)]] 0.5 µM in 3 lines (Panc 03.27 0.114×, Hs 766T 0.0929×, NCI-H460 0.250×; ⚠ cell-cycle shift, explains ~52% of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (Panc 03.27 0.163×, NCI-H460 0.191×, Hs 766T 0.107×; ⚠ cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 3 lines (NCI-H460 0.249×, Panc 03.27 0.280×, A-427 0.333×); [[Homoharringtonine (drug)]] 5 µM in 1 line (Panc 03.27 0.380×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **0.574×** | -4.2 | 0.018 | 9/18 (Panc 03.27, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.783× | -3.5 | 0.13 | 4/18 (SNU-423, NCI-H460, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.792× | -3.3 | 0.16 | 5/18 (A-172, SNU-423, …) | two highest doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.787× | -3.2 | 0.21 | 0/18 | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.810× | -3.0 | 0.22 | 3/18 (RPMI-7951, SNU-423, …) | top dose only |  |
| [[Lapatinib ditosylate (drug)]] 0.5 µM |  | 0.746× | -3.0 | 0.22 | 0/18 | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12612. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 317 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.114× (z -18.3) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.380× (z -11.5) |
| [[C32 (line)]] | wt | 102 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +13.4) | — |
| [[NCI-H460 (line)]] | wt | 231 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -23.5) |
| [[A-172 (line)]] | wt | 105 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 19.1× (z +30.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -11.9) |
| [[A-427 (line)]] | wt | 357 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.333× (z -9.7) |
| [[Hs 766T (line)]] | wt | 295 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0929× (z -14.1) ⚠ cell-cycle shift, explains ~52% of this change |
| [[J82 (line)]] | alt | 73.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +25.5) | — |
| [[NCI-H23 (line)]] | alt | 27.6 | 0 | 3 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0750× (z -13.4) ⚠ cell-cycle shift, explains ~61% of this change |
| [[PANC-1 (line)]] | alt | 61.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +17.7) | — |
| [[NCI-H1792 (line)]] | alt | 70.0 | 1 | 1 | [[Harringtonine (drug)]] 5 µM 3.72× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 101 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +11.1) | — |
| [[SHP-77 (line)]] | alt | 24.9 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.71× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 40.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +24.9) | — |
| [[H4 (line)]] | wt | 20.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.116× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 73.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +10.6) | — |
| [[A498 (line)]] | wt | 4.76 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.01 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.89 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.65 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.84 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.99 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.27 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.17 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.54 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.35 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.04 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.37 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.68 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.63 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.62 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.06 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.19 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.36 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.06 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.40 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.46 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 9.03 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.42 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.68 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.95 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12612), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NALCN]] | +0.64 | +0.57 / +0.67 | both halves | 1e-05 | ⚠ same locus (36.1 kb: neighbours can correlate without regulation) |
| [[EPHA5]] | +0.63 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[SYT14]] | +0.61 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[DISC1FP1]] | +0.61 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[LINC00882]] | +0.61 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[CPED1]] | +0.60 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[SCN3A]] | +0.60 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[TRPC4]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ZEB2]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[DIO2]] | +0.56 | +0.57 / +0.39 | both halves | 6e-05 |  |
| [[LINC02930]] | +0.56 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[SHISAL1]] | +0.56 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[FMN2]] | +0.56 | +0.57 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEF1AKMT4]] | -0.54 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[ZCCHC17]] | -0.49 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[NFATC3]] | -0.47 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[ZNF549]] | -0.45 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[SS18L1]] | -0.45 | -0.43 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NALCN]] | C | NALCN activity raises ITGBL1's level | lines that do not express NALCN (22) vs lines expressing it (28) | 5.29× lower at baseline in the lines without NALCN | 0.037 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229; co-absent with the target |
| [[PCDH18]] | C | PCDH18 activity raises ITGBL1's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 4.95× lower at baseline in the lines without PCDH18 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677; co-absent with the target |
| [[SYT14]] | C | SYT14 activity raises ITGBL1's level | lines that do not express SYT14 (29) vs lines expressing it (21) | 3.05× lower at baseline in the lines without SYT14 | 0.094 | ⚠ within organs, on part of the lines; also absent: ITGA4, MMP2, PHACTR1; co-absent with the target |
| [[ABI3BP]] | C | ABI3BP activity raises ITGBL1's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 5.23× lower at baseline in the lines without ABI3BP | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCLK1]] | B | ITGBL1 activity raises DCLK1's level | lines that do not express ITGBL1 (30) vs lines expressing it (20) | 2.14× lower at baseline in the lines without ITGBL1 | 0.010 | ⚠ within organs, on part of the lines; also absent: STEAP1B-AS1, FLI1, ENSG00000255983 |
| [[SYT14]] | C | ITGBL1 activity raises SYT14's level | lines that do not express ITGBL1 (30) vs lines expressing it (20) | 3.83× lower at baseline in the lines without ITGBL1 | 0.033 | ⚠ within organs, on part of the lines; also absent: STEAP1B-AS1, FLI1, ENSG00000255983; co-absent with the target |
| [[SHISAL1]] | C | ITGBL1 activity raises SHISAL1's level | lines that do not express ITGBL1 (30) vs lines expressing it (20) | 2.73× lower at baseline in the lines without ITGBL1 | 0.048 | ⚠ within organs, on part of the lines; also absent: STEAP1B-AS1, FLI1, ENSG00000255983; co-absent with the target |
| [[LINC01116]] | C | ITGBL1 activity raises LINC01116's level | lines that do not express ITGBL1 (30) vs lines expressing it (20) | 2.29× lower at baseline in the lines without ITGBL1 | 0.052 | ⚠ within organs, on part of the lines; also absent: STEAP1B-AS1, FLI1, ENSG00000255983; co-absent with the target |
| [[SALL1]] | C | ITGBL1 activity raises SALL1's level | lines that do not express ITGBL1 (30) vs lines expressing it (20) | 2.80× lower at baseline in the lines without ITGBL1 | 0.055 | ⚠ within organs, on part of the lines; also absent: STEAP1B-AS1, FLI1, ENSG00000255983; co-absent with the target |
| [[TRHDE]] | C | ITGBL1 activity raises TRHDE's level | lines that do not express ITGBL1 (30) vs lines expressing it (20) | 2.52× lower at baseline in the lines without ITGBL1 | 0.068 | ⚠ within organs, on part of the lines; also absent: STEAP1B-AS1, FLI1, ENSG00000255983; co-absent with the target |
| [[COL22A1]] | C | ITGBL1 activity raises COL22A1's level | lines that do not express ITGBL1 (30) vs lines expressing it (20) | 3.03× lower at baseline in the lines without ITGBL1 | 0.071 | ⚠ within organs, on part of the lines; also absent: STEAP1B-AS1, FLI1, ENSG00000255983; co-absent with the target |
| [[ZNF365]] | C | ITGBL1 activity raises ZNF365's level | lines that do not express ITGBL1 (30) vs lines expressing it (20) | 2.32× lower at baseline in the lines without ITGBL1 | 0.079 | ⚠ within organs, on part of the lines; also absent: STEAP1B-AS1, FLI1, ENSG00000255983; co-absent with the target |
| [[BCAT1]] | C | ITGBL1 activity raises BCAT1's level | lines that do not express ITGBL1 (30) vs lines expressing it (20) | 3.71× lower at baseline in the lines without ITGBL1 | 0.081 | ⚠ within organs, on part of the lines; also absent: STEAP1B-AS1, FLI1, ENSG00000255983; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.625). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.9, 25.4); signed map (40.7, 25.9). **Vector** length 69.9, 20.1% of its response variance represented; |z| ≥ 3 in 628 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.5 | +16.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.1 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.8 | +9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +23.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +10.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +0.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.0 | +1.9 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -3.2 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | integrin subunit beta like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q33.1 — chr13:101,452,593-101,720,856 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TIED, OSCP |
| Gene groups (HGNC) | Integrin beta subunits |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 2 pathways, smallest: RUNX2 regulates genes involved in cell migration; Transcriptional regulation by RUNX2 |
| Matched by | ensembl_id |

UniProt [O95965](https://www.uniprot.org/uniprotkb/O95965) carries no function annotation.

**Summary**, from NCBI Gene [9358](https://www.ncbi.nlm.nih.gov/gene/9358):

> This gene encodes a beta integrin-related protein that is a member of the EGF-like protein family. The encoded protein contains integrin-like cysteine-rich repeats. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:6164](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6164) · Entrez [9358](https://www.ncbi.nlm.nih.gov/gene/9358) · UniProt [O95965](https://www.uniprot.org/uniprotkb/O95965) · Ensembl [ENSG00000198542](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198542)

## Data

Gene col 12612: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12612); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12612, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12612]; `tensor/DDL_lfc|DDL_z.npy` [12612]; `embed/gene_vectors.npy` [12612]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12612 or target_col == 12612). Every well: [[ITGBL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGBL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
