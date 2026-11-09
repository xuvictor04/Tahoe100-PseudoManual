---
symbol: "LRP5"
type: "gene"
col: 8499
ensembl_id: "ENSG00000162337"
name: "LDL receptor related protein 5"
location: "11q13.2"
module: 4
arm: "+"
pooled_cpm: 62.69
n_lines_expressing: 45
n_dd_up: 0
n_dd_down: 25
n_dd_up_clean: 0
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 14
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# LRP5

*LDL receptor related protein 5* — 11q13.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.275× (z -22.6, q 0e+00, down in 40 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUP210]] (+0.65, fdr 1e-05), [[SMAD6]] (+0.61, fdr 1e-05), [[RAI1]] (+0.60, fdr 7e-06); moves opposite to [[TRPC1]] (-0.52, fdr 1e-05), [[STX12]] (-0.52, fdr 1e-05), [[OR9Q1]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[SORL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8499.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.275×** | -22.6 | 0e+00 | 40/43 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.318×** | -20.0 | 0e+00 | 40/43 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.461×** | -19.2 | 0e+00 | 36/43 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.362×** | -17.8 | 0e+00 | 38/42 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.437×** | -13.9 | 5e-42 | 37/43 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.491×** | -12.5 | 1e-33 | 37/43 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.633×** | -11.3 | 1e-27 | 27/43 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.587×** | -9.0 | 2e-17 | 33/43 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.635×** | -7.6 | 1e-12 | 27/41 (HepG2/C3A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.658×** | -7.0 | 1e-10 | 28/41 (SW480, SW 900, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.673×** | -6.9 | 2e-10 | 27/43 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.715×** | -5.6 | 8e-07 | 24/45 (SW480, HT-29, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.749×** | -5.1 | 2e-05 | 20/41 (BT-474, HepG2/C3A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.750×** | -5.0 | 2e-05 | 22/43 (BT-474, SW480, …) | inconsistent across doses | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.752×** | -5.0 | 2e-05 | 23/42 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.607×** | -4.6 | 2e-04 | 22/44 (LoVo, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.785×** | -4.0 | 0.002 | 18/43 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.801×** | -3.9 | 0.003 | 16/42 (COLO 205, HT-29, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.807×** | -3.7 | 0.005 | 17/43 (A498, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8499. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 146 | 0 | 14 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.103× (z -23.0) |
| [[PANC-1 (line)]] | alt | 102 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -24.4) |
| [[HT-29 (line)]] | alt | 154 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0679× (z -22.1) |
| [[LS 180 (line)]] | wt | 96.5 | 0 | 9 | — | [[Panobinostat (drug)]] 5 µM 0.114× (z -20.6) |
| [[BT-474 (line)]] | alt | 86.8 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.159× (z -17.4) |
| [[SHP-77 (line)]] | alt | 115 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 57.4 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -18.8) |
| [[KATO III (line)]] | alt | 165 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.116× (z -20.4) |
| [[LoVo (line)]] | wt | 52.7 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -21.4) |
| [[NCI-H1573 (line)]] | alt | 65.5 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -24.1) |
| [[NCI-H23 (line)]] | alt | 45.6 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -18.6) |
| [[NCI-H460 (line)]] | wt | 25.8 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -17.2) |
| [[SW 900 (line)]] | alt | 203 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -15.4) |
| [[HepG2_C3A (line)]] | wt | 116 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.141× (z -16.5) |
| [[A498 (line)]] | wt | 34.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -16.9) |
| [[A549 (line)]] | wt | 34.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -14.8) |
| [[COLO 205 (line)]] | alt | 148 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.131× (z -18.2) |
| [[Panc 03.27 (line)]] | alt | 90.0 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.227× (z -15.8) |
| [[A-427 (line)]] | wt | 53.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -13.6) |
| [[AN3 CA (line)]] | alt | 59.2 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.0993× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 31.3 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.153× (z -16.3) |
| [[NCI-H2030 (line)]] | alt | 39.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -15.7) |
| [[RKO (line)]] | wt | 54.3 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.203× (z -13.3) |
| [[SW1417 (line)]] | alt | 97.7 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -17.8) |
| [[SW48 (line)]] | wt | 64.7 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0677× (z -19.4) |
| [[AsPC-1 (line)]] | alt | 65.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.218× (z -13.4) |
| [[C-33 A (line)]] | alt | 49.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.258× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 64.3 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -12.7) |
| [[J82 (line)]] | alt | 29.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -14.4) |
| [[SNU-1 (line)]] | wt | 30.1 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.119× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.300× (z -8.8) |
| [[SNU-423 (line)]] | alt | 30.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -10.6) |
| [[A-172 (line)]] | wt | 18.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -10.2) |
| [[CHP-212 (line)]] | wt | 34.5 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0836× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 54.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -8.6) |
| [[Hs 766T (line)]] | wt | 16.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -8.6) |
| [[C32 (line)]] | wt | 13.5 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.03 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.35 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.99 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8499), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP210]] | +0.65 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[SMAD6]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[RAI1]] | +0.60 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[PLXNB1]] | +0.57 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[SPTBN2]] | +0.55 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[TRAF5]] | +0.53 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[CTDSPL]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[DLX6-AS1]] | +0.52 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[LINC02595]] | +0.52 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[ARHGEF16]] | +0.52 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[ZNRF3]] | +0.51 | +0.48 / +0.44 | both halves | 3e-05 | pathway: Regulation of FZD by ubiquitination; STRING 881 |
| [[EVPL]] | +0.51 | +0.52 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRPC1]] | -0.52 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[STX12]] | -0.52 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[OR9Q1]] | -0.51 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[CDKL5]] | -0.51 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[WASHC3]] | -0.50 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[WIPF2]] | -0.47 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[JOSD2]] | -0.47 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[KLF7]] | -0.47 | -0.37 / -0.41 | both halves | 7e-05 |  |
| [[AIM2]] | -0.47 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[NAGK]] | -0.46 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[DYNC1I2]] | -0.46 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[MYO9A]] | -0.46 | -0.44 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SORL1]] | B | SORL1 activity raises LRP5's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.90× lower at baseline in the lines without SORL1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[MEST]] | B | MEST activity raises LRP5's level | lines that do not express MEST (17) vs lines expressing it (33) | 2.96× lower at baseline in the lines without MEST | 0.018 | ⚠ within organs, on part of the lines; also absent: COPG2IT1, CHDH, IL17RB |
| [[EVPL]] | B | EVPL activity raises LRP5's level | lines that do not express EVPL (16) vs lines expressing it (34) | 3.02× lower at baseline in the lines without EVPL | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: PTK6, MYO5C, SFN |
| [[RAPGEF5]] | B | RAPGEF5 activity raises LRP5's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 1.99× lower at baseline in the lines without RAPGEF5 | 0.022 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[ESRP2]] | B | ESRP2 activity raises LRP5's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 2.90× lower at baseline in the lines without ESRP2 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |
| [[GPR35]] | B | GPR35 activity raises LRP5's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 2.78× lower at baseline in the lines without GPR35 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |
| [[DMTN]] | B | DMTN activity raises LRP5's level | lines that do not express DMTN (14) vs lines expressing it (36) | 2.49× lower at baseline in the lines without DMTN | 0.032 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent |
| [[OR9Q1]] | B | OR9Q1 activity lowers LRP5's level | lines that do not express OR9Q1 (26) vs lines expressing it (24) | 2.70× higher at baseline in the lines without OR9Q1 | 0.032 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L |
| [[BMP4]] | B | BMP4 activity raises LRP5's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 2.68× lower at baseline in the lines without BMP4 | 0.044 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B |
| [[SORL1]] | B | SORL1 activity strengthens LRP5's drug response | lines that do not express SORL1 (16) vs lines expressing it (27) | the lines without SORL1 respond 0.73× as strongly (z diff +2.16); strongest at Idarubicin (hydrochloride) 5 µM: 0.88x vs 0.51x (z diff +5.5) | 0.047 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3; target measured in part of the lines; the reference differs; artifact flags |
| [[DENND2D]] | B | DENND2D activity raises LRP5's level | lines that do not express DENND2D (21) vs lines expressing it (29) | 2.25× lower at baseline in the lines without DENND2D | 0.048 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, AREG |
| [[SPTBN2]] | B | SPTBN2 activity raises LRP5's level | lines that do not express SPTBN2 (9) vs lines expressing it (41) | 2.83× lower at baseline in the lines without SPTBN2 | 0.061 | ⚠ within organs, on part of the lines; also absent: CCDC88C, HID1, ASS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.364). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-5.2, 40.0); signed map (29.2, -37.1). **Vector** length 101, 26.9% of its response variance represented; |z| ≥ 3 in 1,226 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.5 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.5 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.1 | -0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | -0.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +1.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | +2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +0.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.5 | -9.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.9 | -13.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.7 | -2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -1.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.0 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.9 | -2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | -0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | LDL receptor related protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:68,312,591-68,449,275 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LR3, BMND1, HBM, OPS, OPTA1, VBCH2, EVR4; previously LRP7, OPPG, EVR1 |
| Gene groups (HGNC) | Low density lipoprotein receptors |
| Reactome | 9 pathways, smallest: Signaling by LRP5 mutants; Signaling by RNF43 mutants; Negative regulation of TCF-dependent signaling by WNT ligand antagonists |
| Matched by | ensembl_id |

**Function**, from UniProt [O75197](https://www.uniprot.org/uniprotkb/O75197) (Low-density lipoprotein receptor-related protein 5):

> Acts as a coreceptor with members of the frizzled family of seven-transmembrane spanning receptors to transduce signal by Wnt proteins. Activates the canonical Wnt signaling pathway that controls cell fate determination and self-renewal during embryonic development and adult tissue regeneration. In particular, may play an important role in the development of the posterior patterning of the epiblast during gastrulation (By similarity). During bone development, regulates osteoblast proliferation …

**Summary**, from NCBI Gene [4041](https://www.ncbi.nlm.nih.gov/gene/4041):

> This gene encodes a transmembrane low-density lipoprotein receptor that binds and internalizes ligands in the process of receptor-mediated endocytosis. This protein also acts as a co-receptor with Frizzled protein family members for transducing signals by Wnt proteins and was originally cloned on the basis of its association with type 1 diabetes mellitus in humans. This protein plays a key role in skeletal homeostasis and many bone density related diseases are caused by mutations in this gene. …

**Accessions** — [HGNC:6697](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6697) · Entrez [4041](https://www.ncbi.nlm.nih.gov/gene/4041) · UniProt [O75197](https://www.uniprot.org/uniprotkb/O75197) · Ensembl [ENSG00000162337](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162337)

## Data

Gene col 8499: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8499); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8499, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8499]; `tensor/DDL_lfc|DDL_z.npy` [8499]; `embed/gene_vectors.npy` [8499]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8499 or target_col == 8499). Every well: [[LRP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
