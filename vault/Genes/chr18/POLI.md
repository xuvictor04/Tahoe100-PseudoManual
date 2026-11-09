---
symbol: "POLI"
type: "gene"
col: 2169
ensembl_id: "ENSG00000101751"
name: "DNA polymerase iota"
location: "18q21.2"
module: 28
arm: "+"
pooled_cpm: 25.85
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 30
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# POLI

*DNA polymerase iota* — 18q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.36× (z +4.8, q 8e-04, up in 24 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (16 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.306× (z -18.5, q 0e+00, down in 45 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.329× (z -17.4, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EBAG9]] (+0.68, fdr 1e-05), [[MRPL58]] (+0.66, fdr 1e-05), [[TRMT10B]] (+0.66, fdr 9e-06); moves opposite to [[LMTK2]] (-0.66, fdr 7e-06), [[MBOAT7]] (-0.59, fdr 1e-05), [[ILRUN]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[BRSK1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2169.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +4.8 | 8e-04 | 24/46 (A-427, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +4.7 | 8e-04 | 23/47 (NCI-H2347, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +3.6 | 0.054 | 16/47 (A-172, C-33 A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2169.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.306×** | -18.5 | 0e+00 | 45/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.329×** | -17.4 | 0e+00 | 46/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.358×** | -16.0 | 0e+00 | 46/47 (RPMI-7951, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.424×** | -13.4 | 7e-39 | 43/47 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.447×** | -12.6 | 3e-34 | 37/47 (HEC-1-A, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.447×** | -12.6 | 3e-34 | 41/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.599×** | -11.3 | 8e-28 | 40/47 (AN3 CA, A-172, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.418×** | -11.1 | 7e-27 | 37/46 (J82, H4, …) | top dose only | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.530×** | -9.9 | 2e-21 | 37/47 (RPMI-7951, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.527×** | -9.4 | 2e-19 | 38/47 (J82, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.588×** | -7.7 | 9e-13 | 25/41 (C-33 A, HCT15, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.405×** | -7.4 | 7e-12 | 30/40 (HEC-1-A, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.631×** | -7.2 | 3e-11 | 29/47 (MIA PaCa-2, NCI-H1792, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.464×** | -6.3 | 1e-08 | 32/47 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.676×** | -6.1 | 4e-08 | 27/47 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.540×** | -5.0 | 1e-05 | 24/45 (PANC-1, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.670×** | -4.5 | 2e-04 | 19/47 (LS 180, C-33 A, …) | all doses, flat | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.767×** | -4.1 | 8e-04 | 19/46 (H4, HT-29, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.793×** | -3.6 | 0.007 | 17/47 (NCI-H23, A549, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.685×** | -3.1 | 0.040 | 15/46 (RPMI-7951, H4, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2169. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.8 | 0 | 11 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.165× (z -17.2) |
| [[PANC-1 (line)]] | alt | 28.0 | 0 | 9 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.198× (z -17.2) |
| [[NCI-H1792 (line)]] | alt | 54.0 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -16.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.298× (z -10.6) |
| [[H4 (line)]] | wt | 43.4 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.131× (z -12.4) |
| [[HEC-1-A (line)]] | alt | 28.2 | 0 | 6 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.168× (z -14.3) |
| [[J82 (line)]] | alt | 27.0 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.185× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.217× (z -12.2) |
| [[LS 180 (line)]] | wt | 20.8 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0711× (z -18.7) |
| [[SK-MEL-2 (line)]] | alt | 35.6 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -9.7) |
| [[SW480 (line)]] | alt | 12.1 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -14.0) |
| [[A-427 (line)]] | wt | 44.6 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.74× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.403× (z -8.6) |
| [[BT-474 (line)]] | alt | 33.4 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.215× (z -10.8) |
| [[C-33 A (line)]] | alt | 68.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.338× (z -9.0) |
| [[HCT15 (line)]] | alt | 37.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.192× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 44.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.297× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 34.4 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.107× (z -14.9) |
| [[A-172 (line)]] | wt | 28.9 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -9.8) |
| [[C32 (line)]] | wt | 36.1 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.200× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 30.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.178× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -9.8) |
| [[SNU-1 (line)]] | wt | 36.5 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.168× (z -10.7) |
| [[COLO 205 (line)]] | alt | 19.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0749× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0978× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 42.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.231× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -9.1) |
| [[KATO III (line)]] | alt | 15.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.192× (z -10.4) |
| [[LoVo (line)]] | wt | 13.2 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.224× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 30.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.300× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.332× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 38.3 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.173× (z -11.6) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.294× (z -9.9) |
| [[A549 (line)]] | wt | 31.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[AN3 CA (line)]] | alt | 31.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 24.0 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.273× (z -9.2) |
| [[CHP-212 (line)]] | wt | 37.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[HOP62 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.267× (z -9.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0762× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 19.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.167× (z -13.1) |
| [[SHP-77 (line)]] | alt | 45.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.325× (z -9.1) |
| [[SW 1271 (line)]] | alt | 45.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0295× (z -11.1) |
| [[SW 900 (line)]] | alt | 11.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.107× (z -10.2) |
| [[SW48 (line)]] | wt | 14.4 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.111× (z -8.5) |
| [[A498 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.47 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2169), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EBAG9]] | +0.68 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[MRPL58]] | +0.66 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[TRMT10B]] | +0.66 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[ZNF397]] | +0.66 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[CCDC113]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[PEX1]] | +0.65 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ICE2]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[ARL14EP]] | +0.64 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[ZNF23]] | +0.64 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[TRMT13]] | +0.64 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[ZSCAN12]] | +0.64 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[CCDC25]] | +0.64 | +0.63 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMTK2]] | -0.66 | -0.66 / -0.64 | both halves | 7e-06 |  |
| [[MBOAT7]] | -0.59 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[ILRUN]] | -0.57 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[UBE2G1]] | -0.56 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[RAD9A]] | -0.56 | -0.51 / -0.53 | both halves | 1e-05 | STRING 525 |
| [[STIM1]] | -0.56 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[HSPA1B]] | -0.55 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[CMTM8]] | -0.55 | -0.55 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BRSK1]] | B | BRSK1 activity raises POLI's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without BRSK1 | 0.015 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |
| [[ZNF571]] | B | ZNF571 activity raises POLI's level | lines that do not express ZNF571 (6) vs lines expressing it (44) | 1.92× lower at baseline in the lines without ZNF571 | 0.066 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF420, ZNF850, ZNF540 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.744). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-29.5, 5.6); signed map (5.1, -22.7). **Vector** length 82.2, 19.9% of its response variance represented; |z| ≥ 3 in 1,250 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.9 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.2 | +4.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +7.3 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.6 | +3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.9 | -0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.3 | +2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.5 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.4 | -0.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -5.3 | -16.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.9 | -9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -11.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.1 | -7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -12.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -9.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.0 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | DNA polymerase iota |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.2 — chr18:54,269,517-54,321,266 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously RAD3OB, RAD30B |
| Gene groups (HGNC) | DNA polymerases |
| Reactome | 11 pathways, smallest: Translesion synthesis by POLI; Somatic hypermutation of immunoglobulin genes by error-prone base excision repair (BER); Somatic hypermutation of immunoglobulin genes by error-prone mismatch repair (MMR) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNA4](https://www.uniprot.org/uniprotkb/Q9UNA4) (DNA polymerase iota):

> Error-prone DNA polymerase specifically involved in DNA repair. Plays an important role in translesion synthesis, where the normal high-fidelity DNA polymerases cannot proceed and DNA synthesis stalls. Favors Hoogsteen base-pairing in the active site. Inserts the correct base with high-fidelity opposite an adenosine template. Exhibits low fidelity and efficiency opposite a thymidine template, where it will preferentially insert guanosine. May play a role in hypermutation of immunoglobulin …

**Summary**, from NCBI Gene [11201](https://www.ncbi.nlm.nih.gov/gene/11201):

> The protein encoded by this gene is an error-prone DNA polymerase involved in DNA repair. The encoded protein promotes DNA synthesis across lesions in the template DNA, which other polymerases cannot do. The encoded polymerase inserts deoxynucleotides across lesions and then relies on DNA polymerase zeta to extend the nascent DNA strand to bypass the lesion. [provided by RefSeq, May 2017]

**Accessions** — [HGNC:9182](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9182) · Entrez [11201](https://www.ncbi.nlm.nih.gov/gene/11201) · UniProt [Q9UNA4](https://www.uniprot.org/uniprotkb/Q9UNA4) · Ensembl [ENSG00000101751](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101751)

## Data

Gene col 2169: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2169); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2169, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2169]; `tensor/DDL_lfc|DDL_z.npy` [2169]; `embed/gene_vectors.npy` [2169]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2169 or target_col == 2169). Every well: [[POLI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
