---
symbol: "VPS37C"
type: "gene"
col: 9572
ensembl_id: "ENSG00000167987"
name: "VPS37C subunit of ESCRT-I"
location: "11q12.2"
module: 3
arm: "+"
pooled_cpm: 29.18
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 10
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# VPS37C

*VPS37C subunit of ESCRT-I* — 11q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 1.52× (z +5.3, q 5e-05, up in 24 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.410× (z -16.0, q 0e+00, down in 38 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.576× (z -13.7, q 2e-40, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC85B]] (+0.64, fdr 1e-05), [[CRTC1]] (+0.64, fdr 1e-05), [[SNU13]] (+0.64, fdr 1e-05); moves opposite to [[PAPOLA]] (-0.74, fdr 1e-05), [[EIF4G2]] (-0.66, fdr 1e-05), [[MOB1A]] (-0.64, fdr 2e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9572.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.52×** | +5.3 | 5e-05 | 24/46 (C32, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.38 | 15/45 (RPMI-7951, J82, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.5 µM |  | 1.27× | +3.0 | 0.38 | 6/48 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | 1.26× | +3.0 | 0.38 | 7/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9572.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.410×** | -16.0 | 0e+00 | 38/42 (RPMI-7951, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.576×** | -13.7 | 2e-40 | 42/47 (SNU-423, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.489×** | -12.4 | 7e-33 | 28/35 (HEC-1-A, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.495×** | -11.7 | 2e-29 | 34/39 (KATO III, A549, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.577×** | -9.5 | 2e-19 | 35/48 (SW48, HOP62, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.613×** | -8.5 | 3e-15 | 33/47 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.682×** | -6.9 | 5e-10 | 30/48 (SNU-423, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.817×** | -5.0 | 4e-05 | 22/47 (A-427, COLO 205, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.771×** | -4.5 | 5e-04 | 25/47 (SNU-423, SHP-77, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.839× | -4.4 | 7e-04 | 19/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.804×** | -3.9 | 0.005 | 18/48 (LOX-IMVI, CFPAC-1, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.841× | -3.1 | 0.090 | 13/47 (A-427, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9572. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 39.0 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -17.6) |
| [[HOP62 (line)]] | alt | 27.9 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -14.2) |
| [[HS-578T (line)]] | alt | 43.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -11.1) |
| [[SW 900 (line)]] | alt | 28.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -8.6) |
| [[AN3 CA (line)]] | alt | 31.4 | 0 | 3 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0603× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 23.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 29.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0947× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 25.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -10.7) |
| [[SW480 (line)]] | alt | 26.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.405× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.452× (z -9.0) |
| [[A-172 (line)]] | wt | 23.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -11.0) |
| [[A549 (line)]] | wt | 39.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -18.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 33.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0947× (z -19.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 30.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -13.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 30.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -13.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 34.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0879× (z -19.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 34.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -12.0) |
| [[A-427 (line)]] | wt | 31.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -9.8) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A498 (line)]] | wt | 18.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -9.0) |
| [[BT-474 (line)]] | alt | 66.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.405× (z -9.0) |
| [[C-33 A (line)]] | alt | 24.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -9.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 23.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.119× (z -10.4) |
| [[Hs 766T (line)]] | wt | 28.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -16.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 36.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.323× (z -9.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 42.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 29.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 30.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0977× (z -18.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 24.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0735× (z -18.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 25.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 38.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0409× (z -22.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -10.7) |
| [[SW48 (line)]] | wt | 29.2 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0586× (z -15.9) |
| [[AsPC-1 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9572), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC85B]] | +0.64 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[CRTC1]] | +0.64 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[SNU13]] | +0.64 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[PIGU]] | +0.63 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[GGA1]] | +0.63 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[KLHL26]] | +0.62 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[RMND1]] | +0.61 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[MTRES1]] | +0.61 | +0.18 / +0.63 | ⚠ one half (not replicated) | 9e-04 |  |
| [[DDX19B]] | +0.61 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[TBC1D25]] | +0.61 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[ZBTB48]] | +0.60 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[ZNF316]] | +0.60 | +0.39 / +0.75 | both halves | 5e-05 |  |
| [[C19orf81]] | +0.60 | +0.51 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAPOLA]] | -0.74 | -0.55 / -0.70 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.66 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[MOB1A]] | -0.64 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[NXT2]] | -0.62 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[IRAK4]] | -0.61 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ADI1]] | -0.61 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[PDIA3P1]] | -0.60 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[PGRMC1]] | -0.60 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[DDX3X]] | -0.59 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[GIPC2]] | -0.59 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[IL13RA1]] | -0.59 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[UTRN]] | -0.59 | -0.45 / -0.57 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises VPS37C's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[KLHL3]] | B | KLHL3 activity raises VPS37C's level | lines that do not express KLHL3 (12) vs lines expressing it (38) | 1.13× lower at baseline in the lines without KLHL3 | 0.063 | ⚠ within organs, on part of the lines; also absent: PKD2L2-DT, CLIP4, ZNF550 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.594). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-33.7, -23.2); signed map (-33.0, 1.2). **Vector** length 97.2, 21.8% of its response variance represented; |z| ≥ 3 in 850 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.1 | +2.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | +0.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | -0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.3 | +5.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.3 | +2.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.1 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +2.2 |
|  | [[EX229 (drug)]] 0.5 µM |  | +2.4 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +1.5 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -8.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.2 | -11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.0 | -16.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.8 | -12.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -4.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.6 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -2.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | VPS37C subunit of ESCRT-I |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.2 — chr11:61,130,257-61,161,615 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20847 |
| Gene groups (HGNC) | ESCRT-I |
| Reactome | 15 pathways, smallest: Membrane binding and targetting of GAG proteins; Synthesis And Processing Of GAG, GAGPOL Polyproteins; Assembly Of The HIV Virion |
| Matched by | ensembl_id |

**Function**, from UniProt [A5D8V6](https://www.uniprot.org/uniprotkb/A5D8V6) (Vacuolar protein sorting-associated protein 37C):

> Component of the ESCRT-I complex, a regulator of vesicular trafficking process. Required for the sorting of endocytic ubiquitinated cargos into multivesicular bodies. May be involved in cell growth and differentiation.

**Summary**, from NCBI Gene [55048](https://www.ncbi.nlm.nih.gov/gene/55048):

> VPS37C is a subunit of ESCRT-I (endosomal sorting complex required for transport I), a complex in the class E vacuolar protein sorting (VPS) pathway required for sorting ubiquitinated transmembrane proteins into internal vesicles of multivesicular bodies (Eastman et al., 2005 [PubMed 15509564]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:26097](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26097) · Entrez [55048](https://www.ncbi.nlm.nih.gov/gene/55048) · UniProt [A5D8V6](https://www.uniprot.org/uniprotkb/A5D8V6) · Ensembl [ENSG00000167987](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167987)

## Data

Gene col 9572: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9572); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9572, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9572]; `tensor/DDL_lfc|DDL_z.npy` [9572]; `embed/gene_vectors.npy` [9572]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9572 or target_col == 9572). Every well: [[VPS37C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS37C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
