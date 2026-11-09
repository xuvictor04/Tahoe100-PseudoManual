---
symbol: "GTF2IRD2B"
type: "gene"
col: 10490
ensembl_id: "ENSG00000174428"
name: "GTF2I repeat domain containing 2B"
location: "7q11.23"
module: 23
arm: "+"
pooled_cpm: 27.2
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 32
n_dd_up_clean: 4
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# GTF2IRD2B

*GTF2I repeat domain containing 2B* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.45× (z +4.3, q 0.011, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (14 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.141× (z -22.9, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF2IRD2]] (+0.91, fdr 7e-06), [[RBM5]] (+0.77, fdr 7e-06), [[LINC01004]] (+0.74, fdr 1e-05); moves opposite to [[ANXA6]] (-0.67, fdr 1e-05), [[USB1]] (-0.64, fdr 1e-05), [[KIF21B]] (-0.64, fdr 1e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10490.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +4.3 | 0.011 | 24/47 (LoVo, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.41×** | +4.1 | 0.013 | 26/48 (HOP62, NCI-H1792, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.28×** | +4.0 | 0.015 | 24/48 (SW480, HEC-1-A, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.057 | 19/48 (SW480, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.24× | +3.1 | 0.19 | 13/48 (SW480, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.29× | +3.1 | 0.19 | 19/48 (PANC-1, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10490.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.141×** | -22.9 | 0e+00 | 47/48 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.159×** | -21.5 | 0e+00 | 47/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.184×** | -19.8 | 0e+00 | 46/48 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.288×** | -13.6 | 6e-40 | 47/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.321×** | -13.2 | 6e-38 | 44/47 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.398×** | -10.3 | 6e-23 | 39/45 (NCI-H1792, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.457×** | -9.1 | 7e-18 | 43/48 (RPMI-7951, C32, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.483×** | -8.5 | 2e-15 | 39/48 (HT-29, SW 900, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.514×** | -7.7 | 7e-13 | 33/47 (NCI-H1573, H4, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.286×** | -7.6 | 1e-12 | 42/48 (PANC-1, NCI-H1573, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.648×** | -7.1 | 7e-11 | 38/48 (HT-29, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.316×** | -7.0 | 1e-10 | 35/47 (MIA PaCa-2, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.561×** | -6.7 | 8e-10 | 33/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.350×** | -6.4 | 6e-09 | 35/48 (HT-29, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | **0.602×** | -5.9 | 2e-07 | 24/42 (NCI-H1573, Panc 03.27, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.624×** | -5.2 | 8e-06 | 29/47 (C32, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.679×** | -4.5 | 2e-04 | 27/48 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.719×** | -3.8 | 0.003 | 22/48 (SW 900, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 0.05 µM |  | **0.741×** | -3.2 | 0.026 | 16/48 (A-172, HT-29, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.53 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10490. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 29.7 | 0 | 11 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.104× (z -16.4) |
| [[PANC-1 (line)]] | alt | 33.2 | 0 | 11 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0989× (z -21.6) |
| [[C32 (line)]] | wt | 68.9 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.107× (z -17.4) |
| [[NCI-H1573 (line)]] | alt | 65.1 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0751× (z -21.9) |
| [[NCI-H1792 (line)]] | alt | 51.4 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0973× (z -18.5) |
| [[NCI-H23 (line)]] | alt | 17.7 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0586× (z -14.9) |
| [[A549 (line)]] | wt | 21.4 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.108× (z -13.1) |
| [[H4 (line)]] | wt | 41.1 | 0 | 7 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0380× (z -19.5) |
| [[HCT15 (line)]] | alt | 39.8 | 0 | 7 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.112× (z -12.7) |
| [[SW480 (line)]] | alt | 21.4 | 0 | 7 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.106× (z -17.6) |
| [[COLO 205 (line)]] | alt | 26.8 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0135× (z -25.3) |
| [[KATO III (line)]] | alt | 42.6 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.117× (z -16.8) |
| [[NCI-H460 (line)]] | wt | 23.2 | 0 | 6 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0769× (z -19.9) |
| [[Panc 03.27 (line)]] | alt | 22.1 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.130× (z -12.2) |
| [[RPMI-7951 (line)]] | alt | 29.7 | 0 | 6 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0929× (z -14.1) |
| [[SK-MEL-2 (line)]] | alt | 27.6 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.101× (z -14.6) |
| [[Hs 766T (line)]] | wt | 24.5 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.164× (z -11.0) |
| [[SW 900 (line)]] | alt | 32.7 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0617× (z -17.8) |
| [[HEC-1-A (line)]] | alt | 59.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.132× (z -16.5) |
| [[LoVo (line)]] | wt | 24.2 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.213× (z -11.4) |
| [[MIA PaCa-2 (line)]] | alt | 32.0 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.108× (z -14.8) |
| [[SNU-423 (line)]] | alt | 27.4 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.141× (z -12.6) |
| [[A-172 (line)]] | wt | 24.7 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0791× (z -16.3) |
| [[AN3 CA (line)]] | alt | 35.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0333× (z -12.8) |
| [[AsPC-1 (line)]] | alt | 29.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.145× (z -12.8) |
| [[BT-474 (line)]] | alt | 39.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.136× (z -13.3) |
| [[CFPAC-1 (line)]] | alt | 27.4 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.136× (z -13.8) |
| [[HOP62 (line)]] | alt | 23.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.128× (z -12.6) |
| [[HS-578T (line)]] | alt | 18.9 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0380× (z -17.7) |
| [[LS 180 (line)]] | wt | 16.2 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.135× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 21.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 15.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.145× (z -10.5) |
| [[SW1417 (line)]] | alt | 17.1 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.226× (z -8.8) |
| [[A-427 (line)]] | wt | 10.8 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -10.0) |
| [[J82 (line)]] | alt | 12.9 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.0900× (z -13.2) |
| [[SNU-1 (line)]] | wt | 25.5 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0941× (z -10.7) |
| [[A498 (line)]] | wt | 22.6 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.247× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 22.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.128× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 10.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0840× (z -11.2) |
| [[RKO (line)]] | wt | 6.97 | 0 | 1 | — | [[Ligustrazine (drug)]] 5 µM 0.0759× (z -8.6) |
| [[SW 1271 (line)]] | alt | 35.5 | 0 | 1 | — | [[Imiquimod (hydrochloride) (drug)]] 0.5 µM 0.0495× (z -8.7) |
| [[C-33 A (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10490), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2IRD2]] | +0.91 | +0.93 / +0.84 | both halves | 7e-06 | same gene group; STRING 965 |
| [[RBM5]] | +0.77 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[LINC01004]] | +0.74 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[ATE1OSP]] | +0.73 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[ANKHD1-EIF4EBP3]] | +0.73 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[ASH1L]] | +0.73 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[ANKRD17-DT]] | +0.72 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[N4BP2L2]] | +0.72 | +0.73 / +0.57 | both halves | 8e-06 |  |
| [[MFF-DT]] | +0.71 | +0.70 / +0.43 | both halves | 3e-05 |  |
| [[DNAI4]] | +0.71 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[PRANCR]] | +0.71 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[OXA1L-DT]] | +0.70 | +0.67 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANXA6]] | -0.67 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[USB1]] | -0.64 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[KIF21B]] | -0.64 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[METAP1]] | -0.64 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[WASF3]] | -0.64 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[RALB]] | -0.63 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[TTLL12]] | -0.63 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[CORO1C]] | -0.63 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[APMAP]] | -0.63 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[PARP1]] | -0.62 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[LRRC20]] | -0.61 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[ATP13A2]] | -0.61 | -0.60 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers GTF2IRD2B's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.1% of all compounds | 0.013 | ⚠ off-target possible; 3 compounds |
| [[MAP2K2]] | B | MAP2K2 activity lowers GTF2IRD2B's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.790). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (2.6, 10.9); signed map (21.7, -9.7). **Vector** length 102, 31.3% of its response variance represented; |z| ≥ 3 in 1,231 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +6.7 | -4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.6 | +0.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | -3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | -1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.7 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +2.6 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.4 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.1 | +3.5 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -8.9 | -13.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -8.1 | -13.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.2 | -7.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.6 | -22.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.4 | -7.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.5 | -3.2 |
|  | [[Lopinavir (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -8.5 |

## What is on record

|  |  |
|---|---|
| Name | GTF2I repeat domain containing 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:75,092,573-75,149,817 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Zinc fingers BED-type |
| Matched by | ensembl_id |

UniProt [Q6EKJ0](https://www.uniprot.org/uniprotkb/Q6EKJ0) carries no function annotation.

**Summary**, from NCBI Gene [389524](https://www.ncbi.nlm.nih.gov/gene/389524):

> This gene encodes a glycosylated phosphoprotein with a leucine zipper motif, two helix-loop-helix motifs (I repeats) that are similar to domains found in the TFII-I family of transcription factors, one CHARLIE8 transposable element-like sequence, and a BED zinc finger. This gene lies within a region that is deleted in Williams-Beuren syndrome. Alternatively spliced variants which encode different protein isoforms have been described; however, not all variants have been fully characterized. …

**Accessions** — [HGNC:33125](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33125) · Entrez [389524](https://www.ncbi.nlm.nih.gov/gene/389524) · UniProt [Q6EKJ0](https://www.uniprot.org/uniprotkb/Q6EKJ0) · Ensembl [ENSG00000174428](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174428)

## Data

Gene col 10490: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10490); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10490, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10490]; `tensor/DDL_lfc|DDL_z.npy` [10490]; `embed/gene_vectors.npy` [10490]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10490 or target_col == 10490). Every well: [[GTF2IRD2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF2IRD2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
