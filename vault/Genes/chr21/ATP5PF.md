---
symbol: "ATP5PF"
type: "gene"
col: 7831
ensembl_id: "ENSG00000154723"
name: "ATP synthase peripheral stalk subunit F6"
location: "21q21.3"
module: 48
arm: "+"
pooled_cpm: 37.82
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# ATP5PF

*ATP synthase peripheral stalk subunit F6* — 21q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.11× (z +10.5, q 4e-23, up in 44 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +5.6, q 2e-06, up in 40 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (A549 10.2×, NCI-H460 7.27×, PANC-1 6.04×, NCI-H1792 8.81×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (A549 9.34×, NCI-H460 5.68×, PANC-1 4.85×, KATO III 5.22×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.539× (z -6.6, q 2e-08, down in 38 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SW480 0.377×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBL5]] (+0.79, fdr 7e-06), [[NEDD8]] (+0.78, fdr 7e-06), [[UQCRQ]] (+0.74, fdr 7e-06, ⚠ UQCRQ in the vector space only through flagged drug-doses), [[COX6C]] (+0.74, fdr 7e-06); moves opposite to [[HUS1]] (-0.58, fdr 1e-05), [[SRSF6]] (-0.58, fdr 1e-05), [[SFPQ]] (-0.57, fdr 1e-04).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7831.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (A549 10.2×, NCI-H460 7.27×, PANC-1 6.04×, NCI-H1792 8.81×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (A549 9.34×, NCI-H460 5.68×, PANC-1 4.85×, KATO III 5.22×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **4.11×** | +10.5 | 4e-23 | 44/46 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **3.21×** | +8.4 | 1e-14 | 37/38 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.49×** | +6.3 | 5e-08 | 36/42 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +5.6 | 2e-06 | 40/48 (AsPC-1, SNU-423, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.2 | 0.003 | 38/48 (SNU-1, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.74×** | +4.1 | 0.003 | 33/47 (A-427, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.59×** | +3.3 | 0.075 | 31/48 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.55× | +3.2 | 0.11 | 29/46 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.53× | +3.0 | 0.15 | 26/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7831.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SW480 0.377×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.539×** | -6.6 | 2e-08 | 38/48 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.640× | -3.4 | 0.20 | 25/47 (A-427, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.661× | -3.1 | 0.35 | 30/47 (SW 1271, AsPC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7831. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 44.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -9.0) |
| [[A-172 (line)]] | wt | 55.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A549 (line)]] | wt | 23.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.2× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LOX-IMVI (line)]] | wt | 39.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.03× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H460 (line)]] | wt | 28.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.27× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[PANC-1 (line)]] | alt | 36.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.04× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A498 (line)]] | wt | 57.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[C32 (line)]] | wt | 25.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.46× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[H4 (line)]] | wt | 42.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.16× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HOP62 (line)]] | alt | 29.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HT-29 (line)]] | alt | 27.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[KATO III (line)]] | alt | 32.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.22× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 43.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.78× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H1792 (line)]] | alt | 22.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.81× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[RKO (line)]] | wt | 43.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.75× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 35.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SNU-423 (line)]] | alt | 32.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A-427 (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7831), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 9 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBL5]] | +0.79 | +0.72 / +0.82 | both halves | 7e-06 |  |
| [[NEDD8]] | +0.78 | +0.69 / +0.82 | both halves | 7e-06 | STRING 483 |
| [[UQCRQ]] ⚠ | +0.74 | +0.67 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 904; ⚠ in the vector space only through flagged drug-doses |
| [[COX6C]] | +0.74 | +0.70 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 908 |
| [[COX6B1]] | +0.72 | +0.62 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 855 |
| [[ZNHIT1]] | +0.71 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[COX7C]] | +0.70 | +0.73 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 975 |
| [[OST4]] | +0.70 | +0.56 / +0.74 | both halves | 1e-05 |  |
| [[NDUFA4]] | +0.70 | +0.60 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 963 |
| [[UQCR11]] | +0.70 | +0.73 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 926 |
| [[NDUFB11]] ⚠ | +0.69 | +0.72 / +0.69 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 600; ⚠ in the vector space only through flagged drug-doses |
| [[NDUFA2]] | +0.69 | +0.48 / +0.72 | both halves | 2e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 688 |
| [[ATP5MK]] | +0.69 | +0.57 / +0.79 | both halves | 1e-05 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 996 |
| [[COX5B]] | +0.68 | +0.45 / +0.83 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 834 |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HUS1]] | -0.58 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[SRSF6]] | -0.58 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[SFPQ]] | -0.57 | -0.36 / -0.62 | both halves | 1e-04 |  |
| [[SRSF3]] | -0.56 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[BCL7B]] | -0.54 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[TEX261]] | -0.54 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[ZNF354A]] | -0.54 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[CELSR3]] | -0.54 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[SLC4A3]] | -0.53 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[ATXN7L2]] | -0.53 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[CSRP1]] | -0.52 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[PLEKHG4]] | -0.52 | -0.55 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ATP5PF's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.780). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-46.5, -22.2); signed map (-35.5, 10.0). **Vector** length 53.6, 15.4% of its response variance represented; |z| ≥ 3 in 514 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Respiratory electron transport* (reactome, mean cos +0.61 to 24); *Complex IV assembly* (reactome, mean cos +0.63 to 11); *Cytoprotection by HMOX1* (reactome, mean cos +0.66 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | -0.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | -1.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.0 | +1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | -0.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +0.8 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.3 | -6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -3.4 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -3.2 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -2.6 | +10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | +0.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | ATP synthase peripheral stalk subunit F6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q21.3 — chr21:25,716,503-25,735,673 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CF6; previously ATP5A, ATP5, ATPM, ATP5J |
| Gene groups (HGNC) | Mitochondrial complex V: ATP synthase subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 6 pathways, smallest: Formation of ATP by chemiosmotic coupling; Cristae formation; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P18859](https://www.uniprot.org/uniprotkb/P18859) (ATP synthase peripheral stalk subunit F6, mitochondrial):

> Subunit F6, of the mitochondrial membrane ATP synthase complex (F(1)F(0) ATP synthase or Complex V) that produces ATP from ADP in the presence of a proton gradient across the membrane which is generated by electron transport complexes of the respiratory chain. ATP synthase complex consist of a soluble F(1) head domain - the catalytic core - and a membrane F(1) domain - the membrane proton channel. These two domains are linked by a central stalk rotating inside the F(1) region and a stationary …

**Summary**, from NCBI Gene [522](https://www.ncbi.nlm.nih.gov/gene/522):

> Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. It is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, which comprises the proton channel. The F1 complex consists of 5 different subunits (alpha, beta, gamma, delta, and epsilon) assembled in a ratio of 3 alpha, 3 beta, and a single representative of the other 3. …

**Accessions** — [HGNC:847](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:847) · Entrez [522](https://www.ncbi.nlm.nih.gov/gene/522) · UniProt [P18859](https://www.uniprot.org/uniprotkb/P18859) · Ensembl [ENSG00000154723](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154723)

## Data

Gene col 7831: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7831); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7831, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7831]; `tensor/DDL_lfc|DDL_z.npy` [7831]; `embed/gene_vectors.npy` [7831]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7831 or target_col == 7831). Every well: [[ATP5PF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP5PF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
