---
symbol: "TTI1"
type: "gene"
col: 2131
ensembl_id: "ENSG00000101407"
name: "TELO2 interacting protein 1"
location: "20q11.23"
module: 71
arm: "+"
pooled_cpm: 45.56
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# TTI1

*TELO2 interacting protein 1* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.44× (z +9.5, q 8e-19, up in 42 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (CFPAC-1 2.57×).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.471× (z -15.5, q 0e+00, down in 42 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.663× (z -8.1, q 6e-14, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUP107]] (+0.66, fdr 7e-06), [[HAUS6]] (+0.66, fdr 7e-06), [[RFWD3]] (+0.65, fdr 7e-06); moves opposite to [[DUSP8]] (-0.57, fdr 1e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2131.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (CFPAC-1 2.57×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.44×** | +9.5 | 8e-19 | 42/49 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.42×** | +7.2 | 1e-10 | 30/48 (A498, NCI-H2347, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.87×** | +6.7 | 3e-09 | 29/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +6.6 | 4e-09 | 0/48 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.30×** | +5.4 | 8e-06 | 28/48 (Hs 766T, COLO 205, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.27×** | +4.8 | 1e-04 | 22/48 (HepG2/C3A, AsPC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.24×** | +4.5 | 6e-04 | 21/48 (KATO III, NCI-H2030, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +4.1 | 0.003 | 17/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.18× | +3.4 | 0.048 | 16/48 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.060 | 11/48 (SNU-423, PANC-1, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 1.16× | +3.1 | 0.11 | 11/48 (CFPAC-1, NCI-H1792, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2131.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.471×** | -15.5 | 0e+00 | 42/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.506×** | -13.5 | 7e-39 | 33/42 (A549, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.521×** | -12.4 | 6e-33 | 39/43 (SNU-423, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.682×** | -11.1 | 1e-26 | 38/47 (NCI-H1792, C32, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.663×** | -8.1 | 6e-14 | 36/48 (A-427, PANC-1, …) | top dose only | cell-cycle shift (explains ~22% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.801×** | -6.5 | 1e-08 | 32/48 (NCI-H460, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.744×** | -6.1 | 1e-07 | 26/47 (HOP62, SNU-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.763×** | -5.3 | 7e-06 | 27/47 (C32, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.777×** | -5.2 | 1e-05 | 29/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.785×** | -5.0 | 4e-05 | 25/48 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **0.826×** | -3.9 | 0.004 | 22/48 (CFPAC-1, SW 1271, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.828×** | -3.9 | 0.005 | 19/48 (SNU-423, C32, …) | top dose only |  |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 0.859× | -3.1 | 0.077 | 10/48 (NCI-H2347, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2131. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 66.2 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -18.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 55.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.386× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 49.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -16.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 45.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0280× (z -31.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.310× (z -11.4) |
| [[C32 (line)]] | wt | 30.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -16.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 71.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.320× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 72.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -14.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 39.7 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.333× (z -13.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 37.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -14.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 31.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -19.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 34.0 | 1 | 1 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 2.57× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.273× (z -10.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 60.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -10.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 35.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -10.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 35.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -17.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 94.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -16.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 42.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -16.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 68.8 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 56.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -9.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 37.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.382× (z -9.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 32.1 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0923× (z -8.9) |
| [[C-33 A (line)]] | alt | 50.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -9.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 44.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0976× (z -15.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 43.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.545× (z -9.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HOP62 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -11.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[hTERT-HPNE (line)]] | wt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -11.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 33.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.281× (z -10.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 23.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 54.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -11.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 60.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 38.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 42.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0836× (z -18.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 81.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -10.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[AsPC-1 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2131), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP107]] | +0.66 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[HAUS6]] | +0.66 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[RFWD3]] | +0.65 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[WDHD1]] | +0.65 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[PRIM2]] | +0.64 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[TOPBP1]] | +0.64 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[FEN1]] | +0.64 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[GTF3C2]] | +0.64 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[PRPF4]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[TBRG4]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[TOMM40]] | +0.63 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[IPO11]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP8]] | -0.57 | -0.61 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers TTI1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.634). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-30.6, -45.7); signed map (-38.5, -39.7). **Vector** length 108, 27.3% of its response variance represented; |z| ≥ 3 in 1,024 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.1 | +9.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.3 | +6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +4.3 | +4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.2 | +0.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +3.6 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | -0.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.6 | +1.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.6 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -7.4 | -11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.1 | -6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -6.6 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -4.9 | -6.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -8.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -2.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | -0.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | TELO2 interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:37,983,007-38,033,461 (-) |
| Ensembl biotype | protein_coding |
| Also known as | smg-10; previously KIAA0406 |
| Gene groups (HGNC) | TTT complex; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O43156](https://www.uniprot.org/uniprotkb/O43156) (TELO2-interacting protein 1 homolog):

> Regulator of the DNA damage response (DDR). Part of the TTT complex that is required to stabilize protein levels of the phosphatidylinositol 3-kinase-related protein kinase (PIKK) family proteins. The TTT complex is involved in the cellular resistance to DNA damage stresses, like ionizing radiation (IR), ultraviolet (UV) and mitomycin C (MMC). Together with the TTT complex and HSP90 may participate in the proper folding of newly synthesized PIKKs. Promotes assembly, stabilizes and maintains the …

**Summary**, from NCBI Gene [9675](https://www.ncbi.nlm.nih.gov/gene/9675):

> Enables kinase binding activity and protein-containing complex stabilizing activity. Involved in positive regulation of DNA damage checkpoint and regulation of TOR signaling. Acts upstream of or within protein stabilization. Located in cytoplasm. Part of TORC1 complex; TORC2 complex; and TTT Hsp90 cochaperone complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29029](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29029) · Entrez [9675](https://www.ncbi.nlm.nih.gov/gene/9675) · UniProt [O43156](https://www.uniprot.org/uniprotkb/O43156) · Ensembl [ENSG00000101407](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101407)

## Data

Gene col 2131: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2131); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2131, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2131]; `tensor/DDL_lfc|DDL_z.npy` [2131]; `embed/gene_vectors.npy` [2131]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2131 or target_col == 2131). Every well: [[TTI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
