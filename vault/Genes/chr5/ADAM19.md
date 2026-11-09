---
symbol: "ADAM19"
type: "gene"
col: 5647
ensembl_id: "ENSG00000135074"
name: "ADAM metallopeptidase domain 19"
location: "5q33.3"
module: 34
arm: "+"
pooled_cpm: 82.95
n_lines_expressing: 37
n_dd_up: 0
n_dd_down: 78
n_dd_up_clean: 0
n_dd_down_clean: 63
in_vector_space: true
direction_upstream: 23
direction_downstream: 28
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# ADAM19

*ADAM metallopeptidase domain 19* — 5q33.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (NCI-H460 3.85×; ⚠ unreliable plate only).
> Pooled over the cell lines (median), lowered significantly by 78 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.207× (z -19.4, q 0e+00, down in 35 of 35 measured lines) ⚠ position correction uncertain. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.338× (z -13.3, q 3e-38, down in 31 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MANCR]] (+0.72, fdr 7e-06), [[DCBLD2]] (+0.69, fdr 7e-06), [[SYNJ2]] (+0.65, fdr 7e-06); moves opposite to [[C1RL]] (-0.54, fdr 5e-05), [[MT1M]] (-0.53, fdr 1e-05), [[NNMT]] (-0.52, fdr 2e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[TINAGL1]] → it (grade B ⚠); 28 go from it, the strongest it → [[DCBLD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (NCI-H460 3.85×; ⚠ unreliable plate only).

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 78 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 78 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5647.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | **0.207×** | -19.4 | 0e+00 | 35/35 (C32, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ position correction uncertain | **0.186×** | -14.6 | 0e+00 | 35/35 (LS 180, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.338×** | -13.3 | 3e-38 | 31/35 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.320×** | -9.9 | 5e-21 | 34/35 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.307×** | -9.9 | 6e-21 | 31/35 (AsPC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.340×** | -9.4 | 6e-19 | 33/35 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.363×** | -8.8 | 9e-17 | 28/35 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.376×** | -8.5 | 1e-15 | 32/35 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.367×** | -8.4 | 3e-15 | 30/34 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.375×** | -8.2 | 1e-14 | 27/35 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.555×** | -7.2 | 3e-11 | 28/35 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.436×** | -7.2 | 3e-11 | 31/35 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Budesonide (drug)]] 0.05 µM |  | **0.479×** | -6.4 | 7e-09 | 24/35 (Hs 766T, NCI-H460, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.529×** | -6.1 | 5e-08 | 23/37 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.534×** | -6.1 | 5e-08 | 27/36 (NCI-H460, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.484×** | -6.1 | 5e-08 | 25/35 (Hs 766T, NCI-H460, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **0.611×** | -6.0 | 5e-08 | 26/35 (NCI-H2347, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.510×** | -5.9 | 2e-07 | 26/35 (Hs 766T, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5647. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 48.9 | 1 (1 ⚠) | 29 (5 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.85× (z +8.8) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -17.6) ⚠ position correction uncertain · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.134× (z -15.9) |
| [[Hs 766T (line)]] | wt | 138 | 0 | 27 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0936× (z -22.6) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -14.3) |
| [[LS 180 (line)]] | wt | 147 | 0 | 26 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0502× (z -27.2) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -15.1) |
| [[SW480 (line)]] | alt | 152 | 0 | 24 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -21.8) |
| [[C32 (line)]] | wt | 254 | 0 | 23 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0366× (z -27.8) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -14.0) |
| [[SK-MEL-2 (line)]] | alt | 110 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0732× (z -26.1) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 96.1 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -14.4) ⚠ position correction uncertain · without an alert: [[Binimetinib (drug)]] 0.05 µM 0.332× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 382 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0939× (z -19.0) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -17.3) |
| [[AsPC-1 (line)]] | alt | 81.3 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -18.3) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.0849× (z -15.4) |
| [[SW1417 (line)]] | alt | 306 | 0 | 9 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -23.3) |
| [[A-172 (line)]] | wt | 215 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -17.9) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.290× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 127 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -13.2) ⚠ position correction uncertain · without an alert: [[Selinexor (drug)]] 5 µM 0.304× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 93.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0896× (z -20.2) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 67.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -19.2) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 58.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0665× (z -14.0) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.174× (z -9.0) |
| [[H4 (line)]] | wt | 53.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -10.6) ⚠ position correction uncertain · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.152× (z -8.8) |
| [[HS-578T (line)]] | alt | 153 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -12.6) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -11.2) |
| [[LoVo (line)]] | wt | 27.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -15.0) ⚠ position correction uncertain · without an alert: [[Trametinib (drug)]] 0.5 µM 0.299× (z -10.1) |
| [[SW 900 (line)]] | alt | 73.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -12.6) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -11.9) |
| [[SW48 (line)]] | wt | 31.0 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0670× (z -10.8) |
| [[HOP62 (line)]] | alt | 117 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -10.9) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -10.6) |
| [[PANC-1 (line)]] | alt | 47.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -11.0) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -10.7) |
| [[SNU-423 (line)]] | alt | 79.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -13.0) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -10.3) |
| [[A-427 (line)]] | wt | 30.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -14.8) ⚠ position correction uncertain |
| [[hTERT-HPNE (line)]] | wt | 96.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -12.0) ⚠ position correction uncertain |
| [[J82 (line)]] | alt | 88.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -13.0) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -10.3) |
| [[A498 (line)]] | wt | 81.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -8.7) ⚠ position correction uncertain |
| [[C-33 A (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -8.5) ⚠ position correction uncertain |
| [[CHP-212 (line)]] | wt | 56.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -9.3) ⚠ position correction uncertain |
| [[HepG2_C3A (line)]] | wt | 26.9 | 0 | 1 (1 ⚠) | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.129× (z -8.8) ⚠ position correction uncertain |
| [[HT-29 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -11.0) ⚠ position correction uncertain |
| [[A549 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.04 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.33 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.51 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.62 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.75 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.97 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 18.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.66 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.94 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.77 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5647), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MANCR]] | +0.72 | +0.76 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[DCBLD2]] | +0.69 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[SYNJ2]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[WWTR1]] | +0.65 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[PPFIBP1]] | +0.64 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[EPHB6]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[COL13A1]] | +0.63 | +0.66 / +0.58 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[ITGA2]] | +0.63 | +0.68 / +0.58 | both halves | 8e-06 | pathway: Extracellular matrix organization |
| [[HIVEP3]] | +0.63 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[GRK5]] | +0.61 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[TINAGL1]] | +0.61 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[TGFA]] | +0.60 | +0.59 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1RL]] | -0.54 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[MT1M]] | -0.53 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[NNMT]] | -0.52 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[EDN2]] | -0.51 | -0.42 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 21, C 2. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TINAGL1]] | B | TINAGL1 activity raises ADAM19's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 1.66× lower at baseline in the lines without TINAGL1 | 0.006 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[PLAT]] | B | PLAT activity raises ADAM19's level | lines that do not express PLAT (28) vs lines expressing it (22) | 3.47× lower at baseline in the lines without PLAT | 0.008 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[MILR1]] | B | MILR1 activity raises ADAM19's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 3.36× lower at baseline in the lines without MILR1 | 0.008 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[CARD11]] | B | CARD11 activity raises ADAM19's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 2.56× lower at baseline in the lines without CARD11 | 0.009 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[NAV1]] | B | NAV1 activity raises ADAM19's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 3.26× lower at baseline in the lines without NAV1 | 0.012 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent |
| [[MMP14]] | B | MMP14 activity raises ADAM19's level | lines that do not express MMP14 (19) vs lines expressing it (31) | 4.11× lower at baseline in the lines without MMP14 | 0.016 | ⚠ within organs, on part of the lines; also absent: IFI16, PTGFR, EVA1A |
| [[FAM107B]] | B | FAM107B activity raises ADAM19's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 2.63× lower at baseline in the lines without FAM107B | 0.016 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[AMOTL1]] | B | AMOTL1 activity raises ADAM19's level | lines that do not express AMOTL1 (16) vs lines expressing it (34) | 2.88× lower at baseline in the lines without AMOTL1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, RNF150, NALCN |
| [[DCBLD2]] | B | DCBLD2 activity raises ADAM19's level | lines that do not express DCBLD2 (9) vs lines expressing it (41) | 4.51× lower at baseline in the lines without DCBLD2 | 0.032 | ⚠ within organs, on part of the lines; also absent: C12orf75, ST3GAL6, OSBPL6; maybe low, not absent |
| [[ADAMTS14]] | B | ADAMTS14 activity raises ADAM19's level | lines that do not express ADAMTS14 (31) vs lines expressing it (19) | 2.92× lower at baseline in the lines without ADAMTS14 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000287335, CARD11, LINC01411 |
| [[CD44]] | B | CD44 activity raises ADAM19's level | lines that do not express CD44 (15) vs lines expressing it (35) | 3.75× lower at baseline in the lines without CD44 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[TM4SF1]] | B | TM4SF1 activity raises ADAM19's level | lines that do not express TM4SF1 (12) vs lines expressing it (38) | 2.83× lower at baseline in the lines without TM4SF1 | 0.048 | ⚠ within organs, on part of the lines; also absent: TM4SF1-AS1; maybe low, not absent |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 28, C 0. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCBLD2]] | B | ADAM19 activity raises DCBLD2's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 2.88× lower at baseline in the lines without ADAM19 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[SYNJ2]] | B | ADAM19 activity raises SYNJ2's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 2.48× lower at baseline in the lines without ADAM19 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[ITGA2]] | B | ADAM19 activity raises ITGA2's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 3.04× lower at baseline in the lines without ADAM19 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[OSBPL3]] | B | ADAM19 activity raises OSBPL3's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 2.36× lower at baseline in the lines without ADAM19 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[DYNLT3]] | B | ADAM19 activity raises DYNLT3's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 2.04× lower at baseline in the lines without ADAM19 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[IL1RAP]] | B | ADAM19 activity raises IL1RAP's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 2.72× lower at baseline in the lines without ADAM19 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[SEPTIN9]] | B | ADAM19 activity raises SEPTIN9's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 1.60× lower at baseline in the lines without ADAM19 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[ITPRID2]] | B | ADAM19 activity raises ITPRID2's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 1.76× lower at baseline in the lines without ADAM19 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[SH3KBP1]] | B | ADAM19 activity raises SH3KBP1's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 1.74× lower at baseline in the lines without ADAM19 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[PTPRE]] | B | ADAM19 activity raises PTPRE's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 2.86× lower at baseline in the lines without ADAM19 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[C13orf46]] | B | ADAM19 activity raises C13orf46's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 1.71× lower at baseline in the lines without ADAM19 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[TINAGL1]] | B | ADAM19 activity raises TINAGL1's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 2.53× lower at baseline in the lines without ADAM19 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.4, 6.3); signed map (5.4, 49.3). **Vector** length 130, 47.8% of its response variance represented; |z| ≥ 3 in 1,792 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.6 | -9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.3 | -9.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.2 | -8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | +3.8 | -3.0 |
|  | [[Vilanterol (drug)]] 0.05 µM |  | +2.4 | +2.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.1 | +2.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.1 | +1.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.0 | +1.4 |
| fall | [[Trametinib (drug)]] 5 µM |  | -8.2 | -6.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -7.5 | -5.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -7.0 | -6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.9 | -5.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -6.6 | -5.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -6.4 | -7.2 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase domain 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.3 — chr5:157,395,534-157,575,775 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MLTNB |
| Gene groups (HGNC) | ADAM metallopeptidase domain containing |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 10 pathways, smallest: Invadopodia formation; Regulation of CDH11 function; Regulation of CDH11 Expression and Function |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H013](https://www.uniprot.org/uniprotkb/Q9H013) (Disintegrin and metalloproteinase domain-containing protein 19):

> Participates in the proteolytic processing of beta-type neuregulin isoforms which are involved in neurogenesis and synaptogenesis, suggesting a regulatory role in glial cell. Also cleaves alpha-2 macroglobulin. May be involved in osteoblast differentiation and/or osteoblast activity in bone (By similarity).

**Summary**, from NCBI Gene [8728](https://www.ncbi.nlm.nih.gov/gene/8728):

> This gene encodes a member of the ADAM (a disintegrin and metalloprotease domain) family. Members of this family are membrane-anchored proteins structurally related to snake venom disintegrins and have been implicated in a variety of biological processes involving cell-cell and cell-matrix interactions, including fertilization, muscle development, and neurogenesis. This member is a type I transmembrane protein and serves as a marker for dendritic cell differentiation. It has been demonstrated …

**Accessions** — [HGNC:197](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:197) · Entrez [8728](https://www.ncbi.nlm.nih.gov/gene/8728) · UniProt [Q9H013](https://www.uniprot.org/uniprotkb/Q9H013) · Ensembl [ENSG00000135074](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135074)

## Data

Gene col 5647: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5647); `tables/drug_effects.parquet` (78 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5647, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5647]; `tensor/DDL_lfc|DDL_z.npy` [5647]; `embed/gene_vectors.npy` [5647]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5647 or target_col == 5647). Every well: [[ADAM19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAM19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
