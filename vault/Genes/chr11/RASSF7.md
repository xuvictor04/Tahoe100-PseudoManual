---
symbol: "RASSF7"
type: "gene"
col: 1820
ensembl_id: "ENSG00000099849"
name: "Ras association domain family member 7"
location: "11p15.5"
module: 3
arm: "+"
pooled_cpm: 14.86
n_lines_expressing: 45
n_dd_up: 1
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 13
direction_downstream: 4
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# RASSF7

*Ras association domain family member 7* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.65× (z +3.9, q 0.058, up in 18 of 35 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~41% of this change.
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.371× (z -11.0, q 4e-25, down in 31 of 40 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGPAT2]] (+0.73, fdr 9e-06), [[DOK4]] (+0.70, fdr 1e-05), [[CARHSP1]] (+0.70, fdr 1e-05); moves opposite to [[ANTXR1]] (-0.66, fdr 1e-05), [[BTBD1]] (-0.66, fdr 3e-05), [[ZMPSTE24]] (-0.64, fdr 2e-04).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[CLDN7]] → it (grade B ⚠); 4 go from it, the strongest it → [[POLR2J]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1820.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.65×** | +3.9 | 0.058 | 18/35 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | 1.50× | +3.1 | 0.37 | 15/42 (HOP62, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.49× | +3.1 | 0.37 | 14/42 (RKO, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1820.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.371×** | -11.0 | 4e-25 | 31/40 (AsPC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.297×** | -9.5 | 7e-19 | 32/36 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.322×** | -8.8 | 2e-16 | 34/42 (KATO III, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.134×** | -8.2 | 4e-14 | 34/41 (KATO III, AsPC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.357×** | -8.0 | 1e-13 | 36/41 (H4, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.166×** | -7.3 | 2e-11 | 31/38 (Panc 03.27, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.582×** | -6.0 | 2e-07 | 26/38 (SW1417, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.470×** | -5.7 | 1e-06 | 28/41 (LoVo, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.538×** | -4.8 | 8e-05 | 27/41 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.556×** | -4.6 | 3e-04 | 25/40 (KATO III, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.580×** | -4.3 | 0.001 | 26/41 (SW 900, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.589×** | -4.1 | 0.002 | 25/42 (AN3 CA, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.589×** | -3.9 | 0.004 | 17/40 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.606×** | -3.8 | 0.007 | 23/39 (BT-474, A-172, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.719×** | -3.6 | 0.010 | 19/42 (NCI-H2347, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.459×** | -3.2 | 0.044 | 13/42 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1820. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 27.9 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0523× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0587× (z -15.9) |
| [[AsPC-1 (line)]] | alt | 43.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0968× (z -19.8) |
| [[Hs 766T (line)]] | wt | 23.5 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0399× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.113× (z -15.2) |
| [[LoVo (line)]] | wt | 22.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 25.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -13.7) |
| [[NCI-H1573 (line)]] | alt | 6.96 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0671× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.188× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 17.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0602× (z -19.5) |
| [[A498 (line)]] | wt | 20.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -10.3) |
| [[COLO 205 (line)]] | alt | 23.1 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.146× (z -9.2) |
| [[H4 (line)]] | wt | 12.0 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0318× (z -11.4) |
| [[HT-29 (line)]] | alt | 49.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -15.1) |
| [[LOX-IMVI (line)]] | wt | 5.44 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0718× (z -9.1) |
| [[LS 180 (line)]] | wt | 33.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -13.6) |
| [[NCI-H2030 (line)]] | alt | 5.45 | 0 | 2 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0800× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 23.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -12.2) |
| [[PANC-1 (line)]] | alt | 10.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -13.3) |
| [[SW1417 (line)]] | alt | 39.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -11.1) |
| [[SW480 (line)]] | alt | 19.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.355× (z -8.9) |
| [[BT-474 (line)]] | alt | 8.78 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -10.3) |
| [[HCT15 (line)]] | alt | 27.7 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0240× (z -9.2) |
| [[J82 (line)]] | alt | 21.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 7.73 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 3.90 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0579× (z -8.6) |
| [[SNU-423 (line)]] | alt | 7.16 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -8.7) |
| [[A-172 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.08 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1820), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 7 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGPAT2]] | +0.73 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[DOK4]] | +0.70 | +0.73 / +0.50 | both halves | 1e-05 |  |
| [[CARHSP1]] | +0.70 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[EFNA4]] | +0.69 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[MKNK2]] | +0.68 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[PMM1]] | +0.67 | +0.36 / +0.68 | both halves | 9e-05 |  |
| [[MRPL55]] | +0.67 | +0.34 / +0.73 | both halves | 1e-04 |  |
| [[RALGDS]] | +0.65 | +0.48 / +0.62 | both halves | 2e-05 | STRING 402 |
| [[MPST]] | +0.65 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[CARD19]] | +0.64 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[POLR2J]] ⚠ | +0.64 | +0.19 / +0.66 | ⚠ one half (not replicated) | 9e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[PRSS8]] | +0.63 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[TRIM11]] | +0.63 | +0.36 / +0.60 | both halves | 1e-04 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANTXR1]] | -0.66 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[BTBD1]] | -0.66 | -0.43 / -0.74 | both halves | 3e-05 |  |
| [[ZMPSTE24]] | -0.64 | -0.30 / -0.65 | both halves | 2e-04 |  |
| [[HDHD2]] | -0.63 | -0.32 / -0.68 | both halves | 2e-04 |  |
| [[ZMYND11]] | -0.63 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[ERLIN2]] | -0.63 | -0.38 / -0.67 | both halves | 6e-05 |  |
| [[DHFR]] | -0.63 | -0.14 / -0.74 | ⚠ one half (not replicated) | 0.002 |  |
| [[SRSF1]] | -0.62 | -0.33 / -0.61 | both halves | 1e-04 |  |
| [[ACADM]] | -0.62 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[SDCBP2-AS1]] | -0.62 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[U2AF2]] | -0.61 | -0.13 / -0.57 | ⚠ one half (not replicated) | 0.002 |  |
| [[DARS2]] | -0.61 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[GALC]] | -0.61 | -0.26 / -0.62 | both halves | 4e-04 |  |
| [[ZNF514]] | -0.61 | -0.40 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 12, C 1. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLDN7]] | B | CLDN7 activity raises RASSF7's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 2.79× lower at baseline in the lines without CLDN7 | 2e-04 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |
| [[PRSS8]] | B | PRSS8 activity raises RASSF7's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 2.64× lower at baseline in the lines without PRSS8 | 0.003 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[FA2H]] | B | FA2H activity raises RASSF7's level | lines that do not express FA2H (27) vs lines expressing it (23) | 2.29× lower at baseline in the lines without FA2H | 0.003 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[GRB7]] | B | GRB7 activity raises RASSF7's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 2.42× lower at baseline in the lines without GRB7 | 0.005 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[TMEM92]] | B | TMEM92 activity raises RASSF7's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 2.02× lower at baseline in the lines without TMEM92 | 0.007 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[MSRB3]] | B | MSRB3 activity lowers RASSF7's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 2.27× higher at baseline in the lines without MSRB3 | 0.016 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[CXXC5]] | B | CXXC5 activity raises RASSF7's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 2.16× lower at baseline in the lines without CXXC5 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |
| [[FA2H]] | B | FA2H activity strengthens RASSF7's drug response | lines that do not express FA2H (23) vs lines expressing it (19) | the lines without FA2H respond 0.60× as strongly (z diff +2.14); strongest at Homoharringtonine 5 µM: 0.42x vs 0.21x (z diff +4.3) | 0.036 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2; target measured in part of the lines; artifact flags |
| [[ANTXR1]] | B | ANTXR1 activity lowers RASSF7's level | lines that do not express ANTXR1 (17) vs lines expressing it (33) | 2.42× higher at baseline in the lines without ANTXR1 | 0.037 | ⚠ within organs, on part of the lines; also absent: VASH1, RFLNB, ENSG00000285804 |
| [[JUP]] | B | JUP activity raises RASSF7's level | lines that do not express JUP (16) vs lines expressing it (34) | 1.80× lower at baseline in the lines without JUP | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[JUP]] | B | JUP activity strengthens RASSF7's drug response | lines that do not express JUP (15) vs lines expressing it (27) | the lines without JUP respond 0.65× as strongly (z diff +1.76); strongest at Homoharringtonine 5 µM: 0.49x vs 0.24x (z diff +4.6) | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671; target measured in part of the lines; artifact flags |
| [[KRT19]] | B | KRT19 activity raises RASSF7's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 2.18× lower at baseline in the lines without KRT19 | 0.061 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POLR2J]] | B | RASSF7 activity raises POLR2J's level | lines that do not express RASSF7 (5) vs lines expressing it (45) | 1.53× lower at baseline in the lines without RASSF7 | 0.036 | ⚠ within organs, on part of the lines; also absent: SORBS1, CTSV, BCL2L1; maybe low, not absent |
| [[SYNGR2]] | B | RASSF7 activity raises SYNGR2's level | lines that do not express RASSF7 (5) vs lines expressing it (45) | 1.72× lower at baseline in the lines without RASSF7 | 0.051 | ⚠ within organs, on part of the lines; also absent: SORBS1, CTSV, BCL2L1; maybe low, not absent |
| [[CARHSP1]] | B | RASSF7 activity raises CARHSP1's level | lines that do not express RASSF7 (5) vs lines expressing it (45) | 1.84× lower at baseline in the lines without RASSF7 | 0.079 | ⚠ within organs, on part of the lines; also absent: SORBS1, CTSV, BCL2L1; maybe low, not absent |
| [[RHPN2]] | C | RASSF7 activity raises RHPN2's level | lines that do not express RASSF7 (5) vs lines expressing it (45) | 3.48× lower at baseline in the lines without RASSF7 | 0.048 | ⚠ within organs, on part of the lines; also absent: SORBS1, CTSV, BCL2L1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.713). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (5.2, -3.9); signed map (-30.3, 18.4). **Vector** length 92.5, 25.3% of its response variance represented; |z| ≥ 3 in 790 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +2.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.6 | +3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.6 | +3.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +0.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.2 | +0.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.5 | +0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | -0.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.2 | +0.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.2 | +1.0 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | +1.1 | +1.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.9 | -3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.1 | -0.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.9 | -3.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -6.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -4.0 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -0.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | Ras association domain family member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:560,404-564,025 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HRC1, HRAS1, FAP88, CFAP88; previously C11orf13 |
| Gene groups (HGNC) | Ras association domain family; Cilia and flagella associated |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02833](https://www.uniprot.org/uniprotkb/Q02833) (Ras association domain-containing protein 7):

> Negatively regulates stress-induced JNK activation and apoptosis by promoting MAP2K7 phosphorylation and inhibiting its ability to activate JNK. Following prolonged stress, anti-apoptotic effect stops because of degradation of RASSF7 protein via the ubiquitin-proteasome pathway. Required for the activation of AURKB and chromosomal congression during mitosis where it stimulates microtubule polymerization.

**Summary**, from NCBI Gene [8045](https://www.ncbi.nlm.nih.gov/gene/8045):

> Predicted to be involved in apoptotic process and signal transduction. Located in centriolar satellite. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1166](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1166) · Entrez [8045](https://www.ncbi.nlm.nih.gov/gene/8045) · UniProt [Q02833](https://www.uniprot.org/uniprotkb/Q02833) · Ensembl [ENSG00000099849](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099849)

## Data

Gene col 1820: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1820); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1820, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1820]; `tensor/DDL_lfc|DDL_z.npy` [1820]; `embed/gene_vectors.npy` [1820]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1820 or target_col == 1820). Every well: [[RASSF7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RASSF7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
