---
symbol: "SLC33A1"
type: "gene"
col: 9797
ensembl_id: "ENSG00000169359"
name: "solute carrier family 33 member 1"
location: "3q25.31"
module: 49
arm: "+"
pooled_cpm: 52.38
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 13
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# SLC33A1

*solute carrier family 33 member 1* — 3q25.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.34× (z +3.9, q 0.025, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (12 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.444× (z -10.8, q 2e-24, down in 41 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.758× (z -3.7, q 0.010, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A498 0.293×, RKO 0.233×, A549 0.290×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 0.164×, NCI-H1573 0.153×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (A498 0.190×, PANC-1 0.326×; ⚠ cell-cycle shift, explains ~71% of this change); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0922×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (SW 1088 0.0418×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OSTC]] (+0.82, fdr 7e-06), [[PCGF3-AS1]] (+0.79, fdr 7e-06), [[COG3]] (+0.76, fdr 7e-06).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FICD]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9797.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.025 | 22/48 (LOX-IMVI, PANC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.025 | 21/48 (PANC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +3.8 | 0.025 | 23/48 (NCI-H2347, HOP62, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.025 | 21/48 (LOX-IMVI, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.32× | +3.3 | 0.10 | 23/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.26× | +3.1 | 0.17 | 18/48 (A-427, SW1417, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 12 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9797.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A498 0.293×, RKO 0.233×, A549 0.290×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 0.164×, NCI-H1573 0.153×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (A498 0.190×, PANC-1 0.326×; ⚠ cell-cycle shift, explains ~71% of this change); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0922×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (SW 1088 0.0418×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.444×** | -10.8 | 2e-24 | 41/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.497×** | -9.3 | 3e-18 | 38/48 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.562×** | -7.7 | 3e-12 | 36/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.629×** | -6.2 | 8e-08 | 30/48 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.634×** | -5.9 | 5e-07 | 33/47 (NCI-H1573, HS-578T, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.634×** | -5.9 | 5e-07 | 29/48 (A498, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.649×** | -5.8 | 7e-07 | 29/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.671×** | -5.1 | 2e-05 | 23/41 (H4, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.704×** | -4.8 | 9e-05 | 27/47 (A498, RKO, …) | inconsistent across doses | composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.570×** | -3.9 | 0.005 | 22/47 (SHP-77, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.586×** | -3.7 | 0.010 | 22/36 (SW480, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.758×** | -3.7 | 0.010 | 22/48 (NCI-H1573, SW 1088, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.745×** | -3.6 | 0.012 | 23/41 (NCI-H1792, SHP-77, …) | all doses, stronger at high dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9797. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 87.3 | 1 | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.37× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[PANC-1 (line)]] | alt | 45.4 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.259× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[H4 (line)]] | wt | 126 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[A-172 (line)]] | wt | 65.3 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.281× (z -10.6) ⚠ cell-cycle shift, explains ~71% of this change |
| [[A498 (line)]] | wt | 54.7 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.190× (z -15.1) ⚠ cell-cycle shift, explains ~71% of this change |
| [[A549 (line)]] | wt | 39.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 80.0 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.325× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[SW480 (line)]] | alt | 58.6 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.373× (z -9.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[KATO III (line)]] | alt | 97.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.224× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 54.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[CHP-212 (line)]] | wt | 46.8 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0922× (z -10.1) |
| [[HT-29 (line)]] | alt | 68.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[hTERT-HPNE (line)]] | wt | 41.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[J82 (line)]] | alt | 83.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[LS 180 (line)]] | wt | 50.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.200× (z -10.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[MIA PaCa-2 (line)]] | alt | 62.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[NCI-H1792 (line)]] | alt | 51.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[NCI-H23 (line)]] | alt | 53.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[NCI-H460 (line)]] | wt | 32.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.366× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[RKO (line)]] | wt | 38.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 78.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[SHP-77 (line)]] | alt | 49.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[SNU-1 (line)]] | wt | 37.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 1088 (line)]] | alt | 69.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0418× (z -9.6) |
| [[SW 900 (line)]] | alt | 58.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 99.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9797), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSTC]] | +0.82 | +0.74 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[PCGF3-AS1]] | +0.79 | +0.76 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[COG3]] | +0.76 | +0.69 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[SERP1]] | +0.74 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.74 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[GOLGA5]] | +0.74 | +0.73 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[PGM3]] | +0.73 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[RUSF1]] | +0.72 | +0.74 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[DERL2]] | +0.72 | +0.71 / +0.63 | both halves | 7e-06 | pathway: Disorders of transmembrane transporters |
| [[SELENOS]] | +0.71 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[GMPPA]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[COX7A2L]] | +0.70 | +0.66 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FICD]] | C | FICD's natural level strengthens SLC33A1's drug response | FICD's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.08; direction not clear | 0.082 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.829). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.0, -36.4); signed map (-53.9, 12.1). **Vector** length 113, 31.9% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *XBP1(S) activates chaperone genes* (reactome, mean cos +0.61 to 8); *IRE1alpha activates chaperones* (reactome, mean cos +0.61 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.61 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.4 | +3.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.7 | +1.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +1.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +1.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.8 | +2.5 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.6 | +3.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -4.1 | -7.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.7 | -9.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -3.7 | -10.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -3.2 | -1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.1 | -2.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.8 | -2.7 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.7 | -2.5 |
|  | [[Busulfan (drug)]] 5 µM |  | -2.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 33 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.31 — chr3:155,821,024-155,854,456 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AT-1, AT1; previously ACATN, SPG42 |
| Gene groups (HGNC) | Solute carrier family 33 |
| Reactome | 5 pathways, smallest: Transport of vitamins, nucleosides, and related molecules; SLC transporter disorders; Disorders of transmembrane transporters |
| Matched by | ensembl_id |

**Function**, from UniProt [O00400](https://www.uniprot.org/uniprotkb/O00400) (Acetyl-coenzyme A transporter 1):

> Acetyl-CoA transporter that mediates active acetyl-CoA import through the endoplasmic reticulum (ER) membrane into the ER lumen where specific ER-based acetyl-CoA:lysine acetyltransferases are responsible for the acetylation of ER-based protein substrates, such as BACE1. Necessary for O-acetylation of gangliosides.

**Summary**, from NCBI Gene [9197](https://www.ncbi.nlm.nih.gov/gene/9197):

> The protein encoded by this gene is required for the formation of O-acetylated (Ac) gangliosides. The encoded protein is predicted to contain 6 to 10 transmembrane domains, and a leucine zipper motif in transmembrane domain III. Defects in this gene have been reported to cause spastic paraplegia autosomal dominant type 42 (SPG42) in one Chinese family, but not in similar patients of European descent. Two transcript variants encoding the same protein have been found for this gene. [provided by …

**Accessions** — [HGNC:95](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:95) · Entrez [9197](https://www.ncbi.nlm.nih.gov/gene/9197) · UniProt [O00400](https://www.uniprot.org/uniprotkb/O00400) · Ensembl [ENSG00000169359](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169359)

## Data

Gene col 9797: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9797); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9797, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9797]; `tensor/DDL_lfc|DDL_z.npy` [9797]; `embed/gene_vectors.npy` [9797]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9797 or target_col == 9797). Every well: [[SLC33A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC33A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
