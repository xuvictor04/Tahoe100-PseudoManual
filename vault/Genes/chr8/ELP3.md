---
symbol: "ELP3"
type: "gene"
col: 5498
ensembl_id: "ENSG00000134014"
name: "elongator acetyltransferase complex subunit 3"
location: "8p21.1"
module: 17
arm: "+"
pooled_cpm: 57.9
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ELP3

*elongator acetyltransferase complex subunit 3* — 8p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.07× (z +7.1, q 8e-10, up in 33 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.320× (z -21.2, q 0e+00, down in 45 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.780× (z -4.6, q 5e-04, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR89]] (+0.66, fdr 7e-06), [[HEATR6]] (+0.66, fdr 7e-06), [[GEMIN2]] (+0.63, fdr 2e-05); moves opposite to [[CASTOR3P-1]] (-0.57, fdr 1e-05), [[NUTM2A-AS1]] (-0.53, fdr 4e-05), [[SFXN5]] (-0.52, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5498.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.07×** | +7.1 | 8e-10 | 33/49 (SW480, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.04×** | +7.0 | 9e-10 | 34/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.38×** | +6.0 | 3e-07 | 33/48 (NCI-H2347, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +5.9 | 5e-07 | 33/48 (NCI-H2347, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.33×** | +5.3 | 2e-05 | 32/48 (NCI-H2347, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.22×** | +5.2 | 2e-05 | 24/48 (HT-29, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.29×** | +4.8 | 1e-04 | 24/48 (SW480, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.0 | 0.004 | 18/48 (NCI-H2347, RKO, …) | two highest doses | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.006 | 24/48 (NCI-H2347, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | 1.18× | +3.1 | 0.12 | 13/48 (A498, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5498.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.320×** | -21.2 | 0e+00 | 45/48 (Panc 03.27, A549, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.400×** | -16.4 | 0e+00 | 40/44 (KATO III, LoVo, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.395×** | -16.0 | 0e+00 | 37/45 (A-172, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.780×** | -4.6 | 5e-04 | 23/48 (CFPAC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.782×** | -4.4 | 0.001 | 23/46 (NCI-H2030, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.796×** | -4.2 | 0.002 | 22/48 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.803×** | -4.1 | 0.003 | 25/48 (SW480, SHP-77, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.818×** | -3.7 | 0.013 | 21/48 (CFPAC-1, HCT15, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.822×** | -3.5 | 0.028 | 22/47 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.840× | -3.2 | 0.069 | 21/48 (NCI-H460, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5498. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 59.4 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -15.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 79.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -15.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 77.1 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -17.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 55.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -20.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 66.3 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -16.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 75.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -21.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 96.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -17.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 80.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[OTS514 (drug)]] 5 µM 0.105× (z -9.6) |
| [[HS-578T (line)]] | alt | 86.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -19.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 53.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -20.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 76.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -13.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 85.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 41.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.44× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -9.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 43.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0409× (z -29.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 72.9 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -20.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 113 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -19.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 57.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -17.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 64.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.302× (z -12.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 76.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -10.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 57.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -11.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 77.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -18.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 42.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -12.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 69.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.299× (z -12.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 77.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -15.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 52.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.234× (z -10.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 67.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0478× (z -29.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 30.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -11.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 70.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -11.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 78.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0972× (z -18.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 96.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.204× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[HOP62 (line)]] | alt | 42.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.296× (z -10.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 29.3 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0674× (z -12.1) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 59.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -16.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 67.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -11.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 27.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.443× (z -9.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 42.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -13.1) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 86.9 | 0 | 1 | — | [[5-Azacytidine (drug)]] 5 µM 0.0825× (z -8.5) |
| [[SW1417 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -12.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 56.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0985× (z -14.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 63.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5498), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR89]] | +0.66 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[HEATR6]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[GEMIN2]] | +0.63 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[TUT1]] | +0.62 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[POT1]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[PARL]] | +0.62 | +0.71 / +0.47 | both halves | 2e-05 |  |
| [[FASTKD3]] | +0.62 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[PPIE]] | +0.61 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[NUP35]] | +0.61 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[RARS1]] | +0.61 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[MTX2]] | +0.60 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[CEPT1]] | +0.60 | +0.66 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASTOR3P-1]] | -0.57 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[NUTM2A-AS1]] | -0.53 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[SFXN5]] | -0.52 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[LARGE1]] | -0.51 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[ATP9A]] | -0.50 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[SANBR]] | -0.50 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[CDKN2B-AS1]] | -0.49 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[SLC6A16]] | -0.49 | -0.46 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ELP3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[EBF4]] | B | EBF4 activity raises ELP3's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 1.33× lower at baseline in the lines without EBF4 | 0.098 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.522). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-25.4, -5.0); signed map (-27.7, -13.7). **Vector** length 91.3, 22.5% of its response variance represented; |z| ≥ 3 in 956 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +5.7 | +5.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.3 | +7.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.5 | +5.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.4 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +1.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.0 | +0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | -0.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.8 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.5 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.9 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -2.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -3.8 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -4.2 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -2.3 | +0.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | -1.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | elongator acetyltransferase complex subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.1 — chr8:28,089,673-28,191,156 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10422, KAT9 |
| Gene groups (HGNC) | Lysine acetyltransferases; Elongator acetyltransferase complex ; GCN5 related N-acetyltransferases; Radical S-adenosylmethionine domain containing |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9T3](https://www.uniprot.org/uniprotkb/Q9H9T3) (Elongator complex protein 3):

> Catalytic tRNA acetyltransferase subunit of the elongator complex which is required for multiple tRNA modifications, including mcm5U (5-methoxycarbonylmethyl uridine), mcm5s2U (5-methoxycarbonylmethyl-2-thiouridine), and ncm5U (5-carbamoylmethyl uridine). In the elongator complex, acts as a tRNA uridine(34) acetyltransferase by mediating formation of carboxymethyluridine in the wobble base at position 34 in tRNAs (By similarity). May also act as a protein lysine acetyltransferase by mediating …

**Summary**, from NCBI Gene [55140](https://www.ncbi.nlm.nih.gov/gene/55140):

> Enables acetyltransferase activity. Involved in regulation of transcription by RNA polymerase II and tRNA wobble uridine modification. Located in cytosol and nucleolus. Part of elongator holoenzyme complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20696](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20696) · Entrez [55140](https://www.ncbi.nlm.nih.gov/gene/55140) · UniProt [Q9H9T3](https://www.uniprot.org/uniprotkb/Q9H9T3) · Ensembl [ENSG00000134014](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134014)

## Data

Gene col 5498: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5498); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5498, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5498]; `tensor/DDL_lfc|DDL_z.npy` [5498]; `embed/gene_vectors.npy` [5498]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5498 or target_col == 5498). Every well: [[ELP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
