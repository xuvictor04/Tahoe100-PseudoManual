---
symbol: "BTBD3"
type: "gene"
col: 5352
ensembl_id: "ENSG00000132640"
name: "BTB domain containing 3"
location: "20p12.2"
module: 26
arm: "-"
pooled_cpm: 58.16
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 15
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# BTBD3

*BTB domain containing 3* — 20p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.28× (z +5.2, q 9e-05, up in 22 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW480 2.06×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.486× (z -19.9, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM102B]] (+0.69, fdr 1e-05), [[SCML2]] (+0.64, fdr 1e-05), [[ZFAND4]] (+0.62, fdr 3e-05); moves opposite to [[LINC00571]] (-0.66, fdr 1e-05), [[C1S]] (-0.65, fdr 1e-05), [[PYY]] (-0.64, fdr 7e-06).
> It sits in the **-** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5352.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW480 2.06×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +5.2 | 9e-05 | 22/47 (NCI-H2347, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.7 | 0.049 | 21/47 (NCI-H2347, SNU-423, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.049 | 17/48 (NCI-H2347, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.13× | +3.4 | 0.096 | 6/47 (HT-29, H4, …) | all doses, flat |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.13 | 5/47 (NCI-H460, RPMI-7951, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.16× | +3.2 | 0.13 | 14/47 (NCI-H2347, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5352.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.486×** | -19.9 | 0e+00 | 44/48 (AN3 CA, C32, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.492×** | -15.1 | 0e+00 | 46/47 (NCI-H460, KATO III, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.656×** | -11.5 | 2e-28 | 35/47 (AN3 CA, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.587×** | -10.9 | 2e-25 | 30/41 (NCI-H1573, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.617×** | -10.2 | 1e-22 | 30/47 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.661×** | -8.4 | 3e-15 | 30/49 (C32, AN3 CA, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.672×** | -8.4 | 3e-15 | 32/48 (C-33 A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -6.9 | 3e-10 | 3/49 (HOP62, Panc 03.27, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.726×** | -6.5 | 4e-09 | 28/47 (C32, AN3 CA, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.735×** | -5.8 | 3e-07 | 26/43 (AN3 CA, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.764×** | -5.7 | 6e-07 | 26/47 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.810×** | -5.4 | 4e-06 | 25/47 (HOP62, SNU-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.683×** | -4.2 | 0.001 | 22/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.700×** | -4.0 | 0.003 | 18/47 (HT-29, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.846× | -3.4 | 0.025 | 15/48 (SHP-77, PANC-1, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.765×** | -3.0 | 0.095 | 17/47 (A-427, SHP-77, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5352. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 78.4 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -17.9) |
| [[AN3 CA (line)]] | alt | 440 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0520× (z -27.7) |
| [[HOP62 (line)]] | alt | 55.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -20.7) |
| [[NCI-H1573 (line)]] | alt | 35.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -19.6) |
| [[NCI-H460 (line)]] | wt | 45.6 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -21.3) |
| [[C32 (line)]] | wt | 108 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -19.1) |
| [[HepG2_C3A (line)]] | wt | 111 | 0 | 5 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.103× (z -21.7) ⚠ toxic; cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -13.1) |
| [[HEC-1-A (line)]] | alt | 54.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -15.6) |
| [[HS-578T (line)]] | alt | 43.7 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -12.1) |
| [[SNU-423 (line)]] | alt | 58.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -20.2) |
| [[LoVo (line)]] | wt | 49.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -16.4) |
| [[MIA PaCa-2 (line)]] | alt | 55.9 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.353× (z -11.1) |
| [[SNU-1 (line)]] | wt | 87.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -8.9) |
| [[SW 900 (line)]] | alt | 87.8 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 56.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -12.7) |
| [[HT-29 (line)]] | alt | 74.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -10.7) |
| [[KATO III (line)]] | alt | 90.8 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.357× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 50.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -14.0) |
| [[LS 180 (line)]] | wt | 72.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -14.8) |
| [[NCI-H23 (line)]] | alt | 49.4 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.345× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 69.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 74.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -11.5) |
| [[SW480 (line)]] | alt | 83.0 | 1 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -10.8) |
| [[BT-474 (line)]] | alt | 69.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -10.1) |
| [[C-33 A (line)]] | alt | 73.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0641× (z -24.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 48.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.6) |
| [[HCT15 (line)]] | alt | 36.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -10.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 35.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 32.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -11.8) |
| [[RKO (line)]] | wt | 38.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -10.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 209 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -14.1) |
| [[SW1417 (line)]] | alt | 44.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -9.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 35.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -11.9) |
| [[A-427 (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.23 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 82.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5352), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*30 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM102B]] | +0.69 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[SCML2]] | +0.64 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ZFAND4]] | +0.62 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[COPG2]] | +0.62 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[SLC23A2]] | +0.60 | +0.60 / +0.39 | both halves | 6e-05 |  |
| [[CEP57L1]] | +0.60 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[NEURL1B]] | +0.60 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[SPATA6]] | +0.60 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[CEP85]] | +0.59 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[METAP1]] | +0.59 | +0.66 / +0.33 | both halves | 1e-04 |  |
| [[INPP4A]] | +0.58 | +0.52 / +0.37 | both halves | 8e-05 |  |
| [[XPR1]] | +0.58 | +0.57 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*70 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00571]] | -0.66 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[C1S]] | -0.65 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[PYY]] | -0.64 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[ZFHX2-AS1]] | -0.63 | -0.65 / -0.41 | both halves | 4e-05 |  |
| [[SLC9A5]] | -0.63 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[RECQL5]] | -0.62 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[SMIM15-AS1]] | -0.60 | -0.61 / -0.37 | both halves | 9e-05 |  |
| [[GCNA]] | -0.60 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[YME1L1]] | -0.60 | -0.54 / -0.36 | both halves | 9e-05 |  |
| [[ZNF546]] | -0.60 | -0.61 / -0.39 | both halves | 6e-05 |  |
| [[CCT6B]] | -0.59 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[ZNF547]] | -0.59 | -0.58 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises BTBD3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **-** arm (projection on the module's main direction -0.547). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (7.9, 6.6); signed map (-38.8, -16.7). **Vector** length 99.7, 23.8% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM |  | +5.1 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.9 | +2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.8 | -0.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.6 | -15.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -19.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.1 | -11.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.7 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -10.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.7 | -2.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -4.0 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | -2.0 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | BTB domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.2 — chr20:11,890,723-11,926,609 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0952, dJ742J24.1 |
| Gene groups (HGNC) | BTB domain containing |
| Hallmark sets | KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2F9](https://www.uniprot.org/uniprotkb/Q9Y2F9) (BTB/POZ domain-containing protein 3):

> Acts as a key regulator of dendritic field orientation during development of sensory cortex. Also directs dendrites toward active axon terminals when ectopically expressed (By similarity).

**Summary**, from NCBI Gene [22903](https://www.ncbi.nlm.nih.gov/gene/22903):

> Predicted to be involved in cerebral cortex development and dendrite morphogenesis. Predicted to be located in nucleus. Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15854](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15854) · Entrez [22903](https://www.ncbi.nlm.nih.gov/gene/22903) · UniProt [Q9Y2F9](https://www.uniprot.org/uniprotkb/Q9Y2F9) · Ensembl [ENSG00000132640](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132640)

## Data

Gene col 5352: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5352); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5352, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5352]; `tensor/DDL_lfc|DDL_z.npy` [5352]; `embed/gene_vectors.npy` [5352]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5352 or target_col == 5352). Every well: [[BTBD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTBD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
