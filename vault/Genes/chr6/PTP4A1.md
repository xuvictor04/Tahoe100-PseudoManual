---
symbol: "PTP4A1"
type: "gene"
col: 3342
ensembl_id: "ENSG00000112245"
name: "protein tyrosine phosphatase 4A1"
location: "6q12"
module: 20
arm: "+"
pooled_cpm: 56.66
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# PTP4A1

*protein tyrosine phosphatase 4A1* — 6q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 9.50× (z +12.3, q 3e-32, up in 48 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2030 0.196×, HepG2/C3A 0.308×, NCI-H23 0.409×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2030 0.317×, NCI-H23 0.407×; ⚠ cell-cycle shift, explains ~20% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.213×, COLO 205 0.131×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2030 0.161×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SW48 0.144×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGAM1]] (+0.56, fdr 2e-05), [[SCARB2]] (+0.55, fdr 1e-05), [[SOD2]] (+0.54, fdr 3e-05); moves opposite to [[ANKS3]] (-0.51, fdr 1e-04), [[LINC02976]] (-0.49, fdr 8e-05), [[PMM1]] (-0.49, fdr 4e-04).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[FGA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3342.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **9.50×** | +12.3 | 3e-32 | 48/49 (LoVo, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **5.69×** | +9.5 | 5e-19 | 39/47 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +7.9 | 7e-13 | 28/48 (SW1417, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.03×** | +7.4 | 2e-11 | 37/48 (SW48, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.65×** | +7.4 | 2e-11 | 37/48 (LoVo, SNU-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.99×** | +6.9 | 5e-10 | 37/48 (AsPC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.78×** | +6.0 | 1e-07 | 36/48 (NCI-H460, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.77×** | +6.0 | 2e-07 | 37/48 (HOP62, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +5.8 | 5e-07 | 30/47 (LS 180, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 0.05 µM |  | **1.71×** | +5.6 | 1e-06 | 42/49 (HT-29, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.68×** | +5.4 | 4e-06 | 28/48 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +5.0 | 3e-05 | 27/48 (SW480, Panc 03.27, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.61×** | +5.0 | 3e-05 | 35/48 (NCI-H1792, H4, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.64×** | +5.0 | 3e-05 | 32/47 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +4.8 | 6e-05 | 24/41 (LoVo, H4, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +4.1 | 0.001 | 24/47 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.002 | 24/48 (LoVo, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.007 | 25/48 (HOP62, H4, …) | two highest doses | cell-cycle shift (explains ~19% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2030 0.196×, HepG2/C3A 0.308×, NCI-H23 0.409×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2030 0.317×, NCI-H23 0.407×; ⚠ cell-cycle shift, explains ~20% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.213×, COLO 205 0.131×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2030 0.161×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SW48 0.144×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3342. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 135 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.89× (z +11.0) | — |
| [[COLO 205 (line)]] | alt | 74.6 | 3 (2 ⚠) | 1 (1 ⚠) | [[Daptomycin (drug)]] 5 µM 6.31× (z +10.0) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 3.44× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 36.4 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +11.5) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 20.6× (z +11.3) | — |
| [[AsPC-1 (line)]] | alt | 25.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +13.2) | — |
| [[KATO III (line)]] | alt | 16.5 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.98× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 314 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -17.2) |
| [[SW1417 (line)]] | alt | 35.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.68× (z +16.8) | — |
| [[SW48 (line)]] | wt | 41.3 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 11.4× (z +10.9) | [[Temsirolimus (drug)]] 0.5 µM 0.144× (z -8.7) |
| [[SW480 (line)]] | alt | 15.7 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 15.5× (z +10.2) | — |
| [[A-427 (line)]] | wt | 29.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +11.2) | — |
| [[C32 (line)]] | wt | 56.6 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 19.2× (z +9.8) | — |
| [[HepG2_C3A (line)]] | wt | 314 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -12.4) |
| [[HOP62 (line)]] | alt | 34.9 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.56× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 43.1 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.23× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 110 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -9.6) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.409× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 85.9 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.57× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 35.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +9.8) | — |
| [[BT-474 (line)]] | alt | 48.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[HEC-1-A (line)]] | alt | 24.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +11.4) | — |
| [[LOX-IMVI (line)]] | wt | 33.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 15.9× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 51.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 13.3× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 18.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.98× (z +9.1) | — |
| [[RKO (line)]] | wt | 20.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +9.0) | — |
| [[A-172 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 92.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 109 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 67.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 95.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3342), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGAM1]] | +0.56 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[SCARB2]] | +0.55 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[SOD2]] | +0.54 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[PTGR2]] | +0.54 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[SZRD1]] | +0.54 | +0.35 / +0.60 | both halves | 1e-04 |  |
| [[TSPYL4]] | +0.52 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[EFEMP1]] | +0.52 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[ANKRD30BL]] | +0.52 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[PDIA3P1]] | +0.52 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[HAVCR1]] | +0.52 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[FGA]] | +0.52 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[LIPA]] | +0.51 | +0.38 / +0.50 | both halves | 6e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKS3]] | -0.51 | -0.32 / -0.56 | both halves | 1e-04 |  |
| [[LINC02976]] | -0.49 | -0.37 / -0.56 | both halves | 8e-05 |  |
| [[PMM1]] | -0.49 | -0.25 / -0.58 | both halves | 4e-04 |  |
| [[POLR2J4]] | -0.49 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[PLEKHM1P1]] | -0.47 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[PPARA]] | -0.46 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[FBXL18]] | -0.46 | -0.26 / -0.53 | both halves | 4e-04 |  |
| [[RGP1]] | -0.46 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[RASA4B]] | -0.45 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[ARHGAP27P1-BPTFP1-KPNA2P3]] | -0.45 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[MPP3]] | -0.45 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[CROCCP2-1]] | -0.45 | -0.39 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGA]] | B | FGA activity raises PTP4A1's level | lines that do not express FGA (43) vs lines expressing it (7) | 3.17× lower at baseline in the lines without FGA | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG |
| [[KCNK6]] | B | KCNK6 activity lowers PTP4A1's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 1.83× higher at baseline in the lines without KCNK6 | 0.031 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |
| [[FGG]] | B | FGG activity raises PTP4A1's level | lines that do not express FGG (42) vs lines expressing it (8) | 2.96× lower at baseline in the lines without FGG | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB |
| [[CYP24A1]] | B | CYP24A1 activity raises PTP4A1's level | lines that do not express CYP24A1 (39) vs lines expressing it (11) | 2.41× lower at baseline in the lines without CYP24A1 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, S100A9, FGG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.448). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (52.5, -11.2); signed map (22.0, -42.8). **Vector** length 111, 31.9% of its response variance represented; |z| ≥ 3 in 1,227 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.5 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +9.0 | +1.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +8.3 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | +8.2 | +0.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.3 | +12.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.0 | +5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +9.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.5 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | +7.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | +1.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.9 | -2.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.9 | -2.7 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.4 | -2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase 4A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q12 — chr6:63,521,746-63,583,588 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PTPCAAX1, PRL-1, PRL1 |
| Gene groups (HGNC) | Protein tyrosine phosphatase 4A family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q93096](https://www.uniprot.org/uniprotkb/Q93096) (Protein tyrosine phosphatase type IVA 1):

> Protein tyrosine phosphatase which stimulates progression from G1 into S phase during mitosis. May play a role in the development and maintenance of differentiating epithelial tissues. Enhances cell proliferation, cell motility and invasive activity, and promotes cancer metastasis.

**Summary**, from NCBI Gene [7803](https://www.ncbi.nlm.nih.gov/gene/7803):

> This gene encodes a member of a small class of prenylated protein tyrosine phosphatases (PTPs), which contain a PTP domain and a characteristic C-terminal prenylation motif. The encoded protein is a cell signaling molecule that plays regulatory roles in a variety of cellular processes, including cell proliferation and migration. The protein may also be involved in cancer development and metastasis. This tyrosine phosphatase is a nuclear protein, but may associate with plasma membrane by means …

**Accessions** — [HGNC:9634](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9634) · Entrez [7803](https://www.ncbi.nlm.nih.gov/gene/7803) · UniProt [Q93096](https://www.uniprot.org/uniprotkb/Q93096) · Ensembl [ENSG00000112245](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112245)

## Data

Gene col 3342: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3342); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3342, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3342]; `tensor/DDL_lfc|DDL_z.npy` [3342]; `embed/gene_vectors.npy` [3342]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3342 or target_col == 3342). Every well: [[PTP4A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTP4A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
