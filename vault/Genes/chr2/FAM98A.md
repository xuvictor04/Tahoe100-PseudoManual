---
symbol: "FAM98A"
type: "gene"
col: 4123
ensembl_id: "ENSG00000119812"
name: "tRNA splicing ligase complex subunit 3A"
location: "2p22.3"
module: 49
arm: "+"
pooled_cpm: 37.56
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 13
n_dd_up_clean: 17
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# FAM98A

*tRNA splicing ligase complex subunit 3A* — 2p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.75× (z +10.6, q 2e-23, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.552× (z -15.0, q 0e+00, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMED3]] (+0.73, fdr 7e-06), [[SRPRB]] (+0.72, fdr 7e-06), [[COG3]] (+0.68, fdr 7e-06); moves opposite to [[RDH5]] (-0.50, fdr 9e-04, ⚠ not reproduced).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4123.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +10.6 | 2e-23 | 38/48 (SW480, NCI-H23, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +7.6 | 1e-11 | 31/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +7.4 | 3e-11 | 31/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +7.1 | 2e-10 | 27/47 (PANC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +6.9 | 6e-10 | 28/48 (C32, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +6.8 | 1e-09 | 27/48 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +6.7 | 1e-09 | 31/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +6.5 | 7e-09 | 28/48 (CFPAC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +5.5 | 2e-06 | 22/47 (SNU-423, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.68×** | +5.1 | 2e-05 | 21/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +5.0 | 2e-05 | 23/47 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +4.8 | 7e-05 | 23/48 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +4.7 | 1e-04 | 20/48 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +4.4 | 5e-04 | 17/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.2 | 9e-04 | 20/48 (SW480, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +4.2 | 9e-04 | 16/48 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 0.001 | 11/48 (LoVo, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.004 | 16/48 (NCI-H1573, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4123.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.552×** | -15.0 | 0e+00 | 39/48 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.690×** | -7.0 | 6e-10 | 28/48 (KATO III, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.712×** | -6.2 | 1e-07 | 28/48 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.791×** | -6.2 | 1e-07 | 21/48 (A498, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.792×** | -5.9 | 5e-07 | 26/48 (HS-578T, CHP-212, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.814×** | -3.9 | 0.008 | 17/48 (HOP62, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.817×** | -3.8 | 0.010 | 20/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.812×** | -3.8 | 0.010 | 19/48 (SNU-1, SW 1088, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.684×** | -3.8 | 0.010 | 17/47 (RKO, BT-474, …) | top dose only | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.824×** | -3.7 | 0.013 | 18/48 (NCI-H2030, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.826×** | -3.6 | 0.014 | 14/48 (NCI-H2030, SW 1088, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.947× | -3.5 | 0.024 | 0/48 | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.789×** | -3.2 | 0.056 | 8/47 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.834× | -3.2 | 0.056 | 15/47 (hTERT-HPNE, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.850× | -3.1 | 0.074 | 18/48 (A498, hTERT-HPNE, …) | inconsistent across doses |  |
| [[AZD-8055 (drug)]] 5 µM |  | **0.740×** | -3.0 | 0.094 | 3/48 (HEC-1-A, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.856× | -3.0 | 0.095 | 10/48 (NCI-H460, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4123. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 118 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -24.0) |
| [[NCI-H460 (line)]] | wt | 39.5 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 2.43× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 30.0 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -12.2) |
| [[HOP62 (line)]] | alt | 35.4 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -12.4) |
| [[KATO III (line)]] | alt | 49.7 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.286× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -10.7) |
| [[PANC-1 (line)]] | alt | 27.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +16.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.52× (z +12.3) | — |
| [[RPMI-7951 (line)]] | alt | 54.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.281× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[SNU-1 (line)]] | wt | 51.6 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -11.6) |
| [[SW 900 (line)]] | alt | 53.0 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.140× (z -13.4) ⚠ transcription drop; cell-cycle shift, explains ~3% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -11.7) |
| [[A-172 (line)]] | wt | 48.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -11.4) |
| [[BT-474 (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.268× (z -8.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 25.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HEC-1-A (line)]] | alt | 40.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HepG2_C3A (line)]] | wt | 22.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -8.9) |
| [[HS-578T (line)]] | alt | 66.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -13.7) |
| [[hTERT-HPNE (line)]] | wt | 46.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -10.4) |
| [[LoVo (line)]] | wt | 36.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 51.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -9.6) |
| [[NCI-H2122 (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Raltitrexed (drug)]] 5 µM 0.278× (z -17.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H23 (line)]] | alt | 39.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 30.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 38.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -9.5) |
| [[SW480 (line)]] | alt | 33.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.13× (z +8.7) | — |
| [[A-427 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 49.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4123), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED3]] | +0.73 | +0.70 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[SRPRB]] | +0.72 | +0.71 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[COG3]] | +0.68 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[MED8]] | +0.65 | +0.69 / +0.38 | both halves | 7e-05 |  |
| [[SEC13]] | +0.65 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[YKT6]] | +0.64 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[GORASP2]] | +0.64 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[LINC00632]] | +0.63 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[SEC23IP]] | +0.62 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[RPGRIP1L]] | +0.62 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[LINC02693]] | +0.62 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[CLINT1]] | +0.61 | +0.63 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RDH5]] | -0.50 | -0.50 / -0.18 | ⚠ not reproduced | 9e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises FAM98A's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TMEM243]] | C | TMEM243's natural level weakens FAM98A's drug response | TMEM243's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.27; direction not clear | 0.062 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.671). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.0, -33.8); signed map (-53.4, 10.5). **Vector** length 119, 31.7% of its response variance represented; |z| ≥ 3 in 1,028 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.0 | +10.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +6.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.2 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.0 | +7.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.9 | +3.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.5 | +4.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +2.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.5 | -15.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -6.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.4 | -7.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.9 | -3.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.1 | -6.2 |
|  | [[Docetaxel (drug)]] 5 µM |  | -2.6 | -1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.1 | -3.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.0 | -3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | tRNA splicing ligase complex subunit 3A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.3 — chr2:33,532,744-33,599,347 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564F0522; previously FAM98A |
| Gene groups (HGNC) | tRNA splicing ligase complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCA5](https://www.uniprot.org/uniprotkb/Q8NCA5) (Protein TSLIG3A):

> Positively stimulates PRMT1-induced protein arginine methylation. Involved in skeletal homeostasis (By similarity). Positively regulates lysosome peripheral distribution and ruffled border formation in osteoclasts (By similarity).

**Summary**, from NCBI Gene [25940](https://www.ncbi.nlm.nih.gov/gene/25940):

> Enables protein methyltransferase activity. Involved in positive regulation of cell population proliferation; positive regulation of gene expression; and protein methylation. Predicted to be located in cytoplasm and nucleus. Predicted to be part of tRNA-splicing ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24520](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24520) · Entrez [25940](https://www.ncbi.nlm.nih.gov/gene/25940) · UniProt [Q8NCA5](https://www.uniprot.org/uniprotkb/Q8NCA5) · Ensembl [ENSG00000119812](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119812)

## Data

Gene col 4123: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4123); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4123, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4123]; `tensor/DDL_lfc|DDL_z.npy` [4123]; `embed/gene_vectors.npy` [4123]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4123 or target_col == 4123). Every well: [[FAM98A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM98A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
