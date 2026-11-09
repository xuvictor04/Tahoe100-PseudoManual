---
symbol: "NRDE2"
type: "gene"
col: 4111
ensembl_id: "ENSG00000119720"
name: "NRDE-2, necessary for RNA interference, domain containing"
location: "14q32.11"
module: 64
arm: "+"
pooled_cpm: 29.49
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 17
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# NRDE2

*NRDE-2, necessary for RNA interference, domain containing* — 14q32.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.53× (z +9.1, q 4e-17, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.621× (z -14.5, q 7e-45, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[E2F6]] (+0.67, fdr 7e-06), [[PSMC1]] (+0.65, fdr 7e-06, ⚠ same locus), [[GTF3C3]] (+0.65, fdr 7e-06), [[DCTN4]] (+0.65, fdr 7e-06); moves opposite to [[LNX2]] (-0.53, fdr 3e-05), [[PAIP2B]] (-0.49, fdr 4e-05), [[SLC35F5]] (-0.48, fdr 4e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4111.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +9.1 | 4e-17 | 38/48 (SW480, RKO, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +5.5 | 1e-05 | 23/47 (HOP62, HCT15, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[NG25 (drug)]] 5 µM |  | **1.52×** | +4.7 | 6e-04 | 14/45 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.25×** | +4.5 | 8e-04 | 19/48 (J82, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +4.3 | 0.002 | 18/48 (LoVo, A-427, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.46×** | +4.2 | 0.002 | 16/47 (NCI-H2030, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.43×** | +4.0 | 0.005 | 17/49 (CFPAC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 1.20× | +3.8 | 0.009 | 7/48 (SW48, NCI-H1573, …) | two highest doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.21×** | +3.8 | 0.009 | 16/47 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.043 | 14/47 (CFPAC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | 1.11× | +3.1 | 0.090 | 10/48 (MIA PaCa-2, A498, …) | two highest doses | low cells (technical?) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.11× | +3.1 | 0.090 | 1/48 (H4) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4111.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.621×** | -14.5 | 7e-45 | 38/48 (NCI-H2030, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.464×** | -14.4 | 2e-44 | 38/47 (HEC-1-A, LS 180, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.566×** | -12.3 | 3e-32 | 38/48 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.582×** | -10.1 | 5e-22 | 34/48 (SW480, SW48, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.683×** | -8.2 | 2e-14 | 32/47 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.647×** | -8.1 | 4e-14 | 28/47 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.690×** | -8.0 | 1e-13 | 26/47 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.663×** | -7.7 | 1e-12 | 22/35 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.653×** | -7.6 | 3e-12 | 26/44 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.705×** | -6.5 | 3e-09 | 25/46 (SNU-423, LS 180, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.770×** | -5.6 | 9e-07 | 23/48 (NCI-H2030, CFPAC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.777×** | -5.4 | 2e-06 | 25/48 (NCI-H460, SK-MEL-2, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.763×** | -5.4 | 3e-06 | 18/37 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.793×** | -5.0 | 2e-05 | 22/48 (NCI-H1573, NCI-H460, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.806×** | -4.6 | 1e-04 | 20/48 (J82, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.675×** | -4.4 | 3e-04 | 14/48 (NCI-H460, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.874× | -4.1 | 0.001 | 14/48 (NCI-H2030, A-172, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.904× | -3.1 | 0.052 | 8/48 (A-427, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4111. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 30.0 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.292× (z -13.6) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 38.5 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -11.1) |
| [[LS 180 (line)]] | wt | 28.6 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -13.8) |
| [[NCI-H1792 (line)]] | alt | 44.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -14.5) ⚠ cell-cycle shift, explains ~88% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.418× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 57.3 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -15.3) |
| [[SW480 (line)]] | alt | 40.5 | 1 | 3 | [[Auranofin (drug)]] 5 µM 1.96× (z +9.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -12.7) |
| [[A-427 (line)]] | wt | 34.2 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 32.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -11.6) |
| [[PANC-1 (line)]] | alt | 17.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.336× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW48 (line)]] | wt | 41.3 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -10.9) |
| [[A549 (line)]] | wt | 32.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[C32 (line)]] | wt | 27.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 42.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -14.5) |
| [[COLO 205 (line)]] | alt | 31.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -12.4) ⚠ cell-cycle shift, explains ~88% of this change |
| [[HEC-1-A (line)]] | alt | 30.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -14.3) |
| [[HepG2_C3A (line)]] | wt | 25.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.177× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[J82 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -8.8) ⚠ cell-cycle shift, explains ~88% of this change |
| [[Panc 03.27 (line)]] | alt | 45.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 32.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -9.4) |
| [[SNU-1 (line)]] | wt | 22.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -8.6) |
| [[SW1417 (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[A-172 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4111), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[E2F6]] | +0.67 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[PSMC1]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 | STRING 588; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[GTF3C3]] | +0.65 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[DCTN4]] | +0.65 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[MCRS1]] | +0.64 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[SARS2]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[NUBP1]] | +0.60 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[ZFP37]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[MINDY4]] | +0.59 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[DNAJC7]] | +0.58 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[ZNF444]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[ZNF180]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[SMIM7]] | +0.57 | +0.58 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LNX2]] | -0.53 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[PAIP2B]] | -0.49 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[SLC35F5]] | -0.48 | -0.49 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NRDE2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers NRDE2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.618). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-23.4, -7.8); signed map (-21.8, -22.5). **Vector** length 89.7, 18.9% of its response variance represented; |z| ≥ 3 in 938 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.3 | +9.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | +5.9 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.7 | +5.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.0 | +4.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.5 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.4 | +4.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.0 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +3.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +1.4 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -10.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -14.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -14.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.3 | -8.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.2 | -6.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.6 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.4 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | NRDE-2, necessary for RNA interference, domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.11 — chr14:90,267,860-90,331,969 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14051; previously C14orf102 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H7Z3](https://www.uniprot.org/uniprotkb/Q9H7Z3) (Nuclear exosome regulator NRDE2):

> Protein of the nuclear speckles that regulates RNA degradation and export from the nucleus through its interaction with MTREX an essential factor directing various RNAs to exosomal degradation. Changes the conformation of MTREX, precluding its association with the nuclear exosome and interaction with proteins required for its function in RNA exosomal degradation. Negatively regulates, for instance, the degradation of mRNAs and lncRNAs by inhibiting their MTREX-mediated recruitment to nuclear …

**Summary**, from NCBI Gene [55051](https://www.ncbi.nlm.nih.gov/gene/55051):

> Involved in several processes, including RNA splicing; mRNA stabilization; and positive regulation of RNA export from nucleus. Located in mitochondrion; nuclear speck; and nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20186](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20186) · Entrez [55051](https://www.ncbi.nlm.nih.gov/gene/55051) · UniProt [Q9H7Z3](https://www.uniprot.org/uniprotkb/Q9H7Z3) · Ensembl [ENSG00000119720](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119720)

## Data

Gene col 4111: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4111); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4111, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4111]; `tensor/DDL_lfc|DDL_z.npy` [4111]; `embed/gene_vectors.npy` [4111]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4111 or target_col == 4111). Every well: [[NRDE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRDE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
