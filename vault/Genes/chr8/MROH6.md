---
symbol: "MROH6"
type: "gene"
col: 12923
ensembl_id: "ENSG00000204839"
name: "maestro heat like repeat family member 6"
location: "8q24.3"
module: 29
arm: "-"
pooled_cpm: 5.28
n_lines_expressing: 48
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# MROH6

*maestro heat like repeat family member 6* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.96× (z +10.8, q 2e-24, up in 16 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.82× (z +6.6, q 5e-09, up in 17 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HT-29 0.222×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.242×); [[Panobinostat (drug)]] 5 µM in 1 line (HT-29 0.159×; ⚠ cell-cycle shift, explains ~31% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIME1]] (+0.77, fdr 7e-06), [[CDK3]] (+0.62, fdr 1e-05), [[PAQR6]] (+0.60, fdr 1e-05); moves opposite to [[AIDA]] (-0.53, fdr 1e-05), [[LANCL1]] (-0.52, fdr 1e-05), [[GLO1]] (-0.46, fdr 1e-04).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TNNT2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12923.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.96×** | +10.8 | 2e-24 | 16/19 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.90×** | +10.2 | 3e-22 | 6/6 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.55×** | +7.0 | 4e-10 | 14/23 (LOX-IMVI, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.55×** | +6.8 | 2e-09 | 8/10 (LS 180, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.82×** | +6.6 | 5e-09 | 17/34 (NCI-H460, J82, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.84×** | +4.7 | 2e-04 | 8/21 (NCI-H1573, BT-474, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +4.3 | 0.001 | 11/24 (NCI-H2347, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.43×** | +4.2 | 0.002 | 11/28 (SW480, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.60×** | +3.8 | 0.009 | 7/13 (SW480, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.037 | 9/35 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.54×** | +3.4 | 0.041 | 8/30 (SW1417, HT-29, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.53×** | +3.3 | 0.044 | 8/44 (C-33 A, NCI-H1573, …) | rises with dose | position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.95×** | +3.1 | 0.073 | 5/37 (SW480, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.49×** | +3.1 | 0.078 | 13/43 (NCI-H460, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12923.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HT-29 0.222×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.242×); [[Panobinostat (drug)]] 5 µM in 1 line (HT-29 0.159×; ⚠ cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 0.627× | -3.4 | 0.14 | 8/41 (PANC-1, COLO 205, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.638× | -3.3 | 0.14 | 7/41 (HT-29, HEC-1-A, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.640× | -3.3 | 0.14 | 8/43 (HepG2/C3A, A-172, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.640× | -3.3 | 0.14 | 5/41 (COLO 205, A-427, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | 0.756× | -3.2 | 0.16 | 11/40 (H4, BT-474, …) | top dose only |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.663× | -3.1 | 0.22 | 5/41 (LoVo, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12923. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 28.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -11.1) |
| [[KATO III (line)]] | alt | 6.01 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.1× (z +9.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 12.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.57× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 4.71 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.69× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.51 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12923), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIME1]] | +0.77 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[CDK3]] | +0.62 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[PAQR6]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[FBXL6]] | +0.58 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[UNC5CL]] | +0.58 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[EFNA2]] | +0.57 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[AGER]] | +0.56 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[LCAT]] | +0.56 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[NAPRT]] | +0.55 | +0.59 / +0.58 | both halves | 7e-06 | STRING 568; ⚠ same locus (2.0 kb, same strand: neighbours can correlate without regulation) |
| [[FAM83E]] | +0.54 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ADAP1]] | +0.53 | +0.56 / +0.37 | both halves | 8e-05 |  |
| [[CLDN15]] | +0.52 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[PTCH2]] | +0.52 | +0.58 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AIDA]] | -0.53 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[LANCL1]] | -0.52 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[GLO1]] | -0.46 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[TMX1]] | -0.45 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[TMTC3]] | -0.44 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[TMED7]] | -0.44 | -0.45 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNNT2]] | B | TNNT2 activity raises MROH6's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 2.11× lower at baseline in the lines without TNNT2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[SPINT1-AS1]] | B | SPINT1-AS1 activity raises MROH6's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 2.06× lower at baseline in the lines without SPINT1-AS1 | 0.011 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |
| [[MUC5B]] | B | MUC5B activity raises MROH6's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 1.84× lower at baseline in the lines without MUC5B | 0.042 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[TNFRSF14-AS1]] | B | TNFRSF14-AS1 activity raises MROH6's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 1.78× lower at baseline in the lines without TNFRSF14-AS1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB |
| [[NAPRT]] | B | NAPRT activity raises MROH6's level | lines that do not express NAPRT (9) vs lines expressing it (41) | 2.00× lower at baseline in the lines without NAPRT | 0.066 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.425). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (24.5, -9.2); signed map (3.0, -10.3). **Vector** length 55.4, 8.95% of its response variance represented; |z| ≥ 3 in 691 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +6.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +6.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.7 | +4.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +2.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.3 | +3.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.3 | +2.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.0 | +3.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.6 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.1 | -2.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.0 | -3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -2.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.9 | -3.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.8 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | maestro heat like repeat family member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:143,566,192-143,572,772 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C8orf73 |
| Gene groups (HGNC) | Maestro heat like repeat containing |
| Matched by | ensembl_id |

UniProt [A6NGR9](https://www.uniprot.org/uniprotkb/A6NGR9) carries no function annotation.

**Summary**, from NCBI Gene [642475](https://www.ncbi.nlm.nih.gov/gene/642475):

> Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27814](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27814) · Entrez [642475](https://www.ncbi.nlm.nih.gov/gene/642475) · UniProt [A6NGR9](https://www.uniprot.org/uniprotkb/A6NGR9) · Ensembl [ENSG00000204839](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204839)

## Data

Gene col 12923: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12923); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12923, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12923]; `tensor/DDL_lfc|DDL_z.npy` [12923]; `embed/gene_vectors.npy` [12923]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12923 or target_col == 12923). Every well: [[MROH6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MROH6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
