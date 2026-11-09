---
symbol: "KCNAB1"
type: "gene"
col: 9790
ensembl_id: "ENSG00000169282"
name: "potassium voltage-gated channel subfamily A regulatory beta subunit 1"
location: "3q25.31"
module: 191
arm: "+"
pooled_cpm: 3.94
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 1
n_dd_up_clean: 26
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/191"]
generated_by: "tahoemap"
---

# KCNAB1

*potassium voltage-gated channel subfamily A regulatory beta subunit 1* — 3q25.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 10.7× (z +38.4, q 0e+00, up in 38 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.887× (z -4.9, q 5e-04, down in 14 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Pyridoxine (hydrochloride) (drug)]] 5 µM: 0.778× (z -4.0, q 0.015, down in 9 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pentoxifylline (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0426×; ⚠ transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (SK-MEL-2 0.0961×; ⚠ toxic; transcription drop); [[Pyridoxine (drug)]] 0.5 µM in 1 line (PANC-1 0.110×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HULC]] (+0.84, fdr 7e-06), [[DPP6]] (+0.82, fdr 7e-06), [[MIR4300HG]] (+0.82, fdr 7e-06).
> It is in [[Module 191]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TMEM132D]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9790.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **10.7×** | +38.4 | 0e+00 | 38/38 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **10.4×** | +37.9 | 0e+00 | 36/38 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **13.9×** | +30.2 | 0e+00 | 43/43 (NCI-H460, SK-MEL-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.81×** | +20.2 | 0e+00 | 35/37 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **5.32×** | +19.2 | 0e+00 | 41/47 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **3.40×** | +13.5 | 1e-39 | 34/42 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.22×** | +13.4 | 3e-39 | 16/21 (PANC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.06×** | +12.9 | 6e-36 | 33/44 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.96×** | +12.5 | 7e-34 | 35/43 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.74×** | +11.1 | 5e-27 | 26/38 (A-172, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.72×** | +10.6 | 1e-24 | 7/9 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.54×** | +10.3 | 3e-23 | 21/36 (HEC-1-A, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +9.9 | 1e-21 | 25/45 (SW480, SHP-77, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.36×** | +9.9 | 3e-21 | 27/45 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +9.6 | 4e-20 | 5/7 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.23×** | +9.2 | 1e-18 | 31/45 (NCI-H23, H4, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.76×** | +9.2 | 2e-18 | 24/47 (HOP62, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.58×** | +5.2 | 4e-06 | 17/43 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9790.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pentoxifylline (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0426×; ⚠ transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (SK-MEL-2 0.0961×; ⚠ toxic; transcription drop); [[Pyridoxine (drug)]] 0.5 µM in 1 line (PANC-1 0.110×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.887× | -4.9 | 5e-04 | 14/48 (HepG2/C3A, HEC-1-A, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.778×** | -4.0 | 0.015 | 9/47 (SW48, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Hexylresorcinol (drug)]] 5 µM |  | 0.828× | -3.0 | 0.47 | 2/47 (SW 1271, SK-MEL-2) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9790. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 2.48 | 6 | 1 | [[Homoharringtonine (drug)]] 5 µM 21.8× (z +16.6) | [[Pyridoxine (drug)]] 0.5 µM 0.110× (z -8.5) |
| [[SW480 (line)]] | alt | 3.91 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 89.3× (z +18.0) | — |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 5 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 21.6× (z +14.0) | [[Digitoxin (drug)]] 5 µM 0.0961× (z -10.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 3.09 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.6× (z +12.0) | — |
| [[HEC-1-A (line)]] | alt | 4.88 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.5× (z +17.6) | — |
| [[SW1417 (line)]] | alt | 4.23 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 69.0× (z +11.6) | — |
| [[HOP62 (line)]] | alt | 3.62 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.4× (z +15.9) | — |
| [[KATO III (line)]] | alt | 4.05 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +13.1) | — |
| [[NCI-H460 (line)]] | wt | 3.10 | 4 | 0 | [[Auranofin (drug)]] 5 µM 39.2× (z +14.4) | — |
| [[SHP-77 (line)]] | alt | 5.44 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 115× (z +14.8) | — |
| [[A-172 (line)]] | wt | 4.06 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +12.2) | — |
| [[C32 (line)]] | wt | 4.39 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.4× (z +14.3) | — |
| [[HS-578T (line)]] | alt | 4.38 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +12.4) | — |
| [[LoVo (line)]] | wt | 3.24 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.8× (z +14.1) | — |
| [[LOX-IMVI (line)]] | wt | 4.68 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +14.3) | — |
| [[NCI-H2030 (line)]] | alt | 3.34 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.1× (z +15.7) | — |
| [[NCI-H2347 (line)]] | alt | 2.91 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.50× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 3.57 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +10.5) | — |
| [[RPMI-7951 (line)]] | alt | 5.01 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +9.7) | — |
| [[A498 (line)]] | wt | 2.75 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +13.6) | — |
| [[CFPAC-1 (line)]] | alt | 3.20 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +11.4) | — |
| [[H4 (line)]] | wt | 5.95 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 28.5× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 3.87 | 2 | 0 | [[Auranofin (drug)]] 5 µM 65.6× (z +12.1) | — |
| [[J82 (line)]] | alt | 3.15 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +11.9) | — |
| [[LS 180 (line)]] | wt | 4.07 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +11.4) | — |
| [[NCI-H1573 (line)]] | alt | 4.71 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +8.6) | [[Pentoxifylline (drug)]] 0.05 µM 0.0426× (z -12.4) ⚠ transcription drop |
| [[NCI-H23 (line)]] | alt | 5.46 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +11.0) | — |
| [[SNU-423 (line)]] | alt | 12.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +13.4) | — |
| [[A-427 (line)]] | wt | 2.58 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 27.6× (z +9.5) | — |
| [[BT-474 (line)]] | alt | 3.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.4× (z +11.3) | — |
| [[HCT15 (line)]] | alt | 3.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.0× (z +10.6) | — |
| [[Hs 766T (line)]] | wt | 3.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.62× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 3.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 2.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.9× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 3.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +9.2) | — |
| [[SW48 (line)]] | wt | 3.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.1× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9790), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HULC]] | +0.84 | +0.87 / +0.82 | both halves | 7e-06 |  |
| [[DPP6]] | +0.82 | +0.77 / +0.82 | both halves | 7e-06 | same gene group; STRING 429 |
| [[MIR4300HG]] | +0.82 | +0.82 / +0.79 | both halves | 7e-06 |  |
| [[DNAH3]] | +0.80 | +0.83 / +0.79 | both halves | 7e-06 |  |
| [[MAP3K20-AS1]] | +0.80 | +0.85 / +0.65 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.80 | +0.83 / +0.78 | both halves | 7e-06 | pathway: Neuronal System |
| [[LINC01033]] | +0.79 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.78 | +0.83 / +0.73 | both halves | 7e-06 |  |
| [[DNAH10]] | +0.76 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[SYNM-AS1]] | +0.76 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[ESR1]] | +0.76 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[LINC02755]] | +0.75 | +0.74 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM132D]] | B | TMEM132D activity raises KCNAB1's level | lines that do not express TMEM132D (29) vs lines expressing it (21) | 1.29× lower at baseline in the lines without TMEM132D | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000271955, ENSG00000287211, GABRG2; maybe low, not absent |
| [[CCDC144NL-1]] | B | CCDC144NL-1 activity raises KCNAB1's level | lines that do not express CCDC144NL-1 (5) vs lines expressing it (45) | 1.42× lower at baseline in the lines without CCDC144NL-1 | 0.036 | ⚠ within organs, on part of the lines; also absent: LINC00298, ARHGAP15, XIRP2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers KCNAB1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00871]] | B | LINC00871 activity raises KCNAB1's level | lines that do not express LINC00871 (12) vs lines expressing it (38) | 1.33× lower at baseline in the lines without LINC00871 | 0.069 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PDE4C]] | C | PDE4C activity strengthens KCNAB1's drug response | lines that do not express PDE4C (3) vs lines expressing it (44) | the lines without PDE4C respond 0.64× as strongly (z diff +1.70); strongest at Homoharringtonine 0.5 µM: 1.26x vs 6.35x (z diff +4.8) | 0.059 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD4; also absent: ZDHHC1, DBNDD1, CDKL5; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 191]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.830). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.8, 27.3); signed map (30.7, 13.9). **Vector** length 60.5, 9.21% of its response variance represented; |z| ≥ 3 in 1,227 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.2 | +30.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +38.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.6 | +37.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +20.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +9.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +5.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +2.9 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | +1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | +1.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | +2.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.4 | -0.5 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.1 | -0.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel subfamily A regulatory beta subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.31 — chr3:156,037,701-156,538,756 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AKR6A3, KCNA1B, hKvBeta3, Kvb1.3, hKvb3 |
| Gene groups (HGNC) | Aldo-keto reductases; Potassium voltage-gated channel regulatory subunits |
| Reactome | 3 pathways, smallest: Voltage gated Potassium channels; Potassium Channels; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14722](https://www.uniprot.org/uniprotkb/Q14722) (Voltage-gated potassium channel subunit beta-1):

> Regulatory subunit of the voltage-gated potassium (Kv) Shaker channels composed of pore-forming and potassium-conducting alpha subunits and of regulatory beta subunits. The beta-1/KCNAB1 cytoplasmic subunit mediates closure of delayed rectifier potassium channels by physically obstructing the pore via its N-terminal domain and increases the speed of channel closure for other family members. Promotes the inactivation of Kv1.1/KCNA1, Kv1.2/KCNA2, Kv1.4/KCNA4, Kv1.5/KCNA5 and Kv1.6/KCNA6 alpha …

**Summary**, from NCBI Gene [7881](https://www.ncbi.nlm.nih.gov/gene/7881):

> Potassium channels represent the most complex class of voltage-gated ion channels from both functional and structural standpoints. Their diverse functions include regulating neurotransmitter release, heart rate, insulin secretion, neuronal excitability, epithelial electrolyte transport, smooth muscle contraction, and cell volume. Four sequence-related potassium channel genes - shaker, shaw, shab, and shal - have been identified in Drosophila, and each has been shown to have human homolog(s). …

**Accessions** — [HGNC:6228](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6228) · Entrez [7881](https://www.ncbi.nlm.nih.gov/gene/7881) · UniProt [Q14722](https://www.uniprot.org/uniprotkb/Q14722) · Ensembl [ENSG00000169282](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169282)

## Data

Gene col 9790: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9790); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9790, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9790]; `tensor/DDL_lfc|DDL_z.npy` [9790]; `embed/gene_vectors.npy` [9790]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9790 or target_col == 9790). Every well: [[KCNAB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNAB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
