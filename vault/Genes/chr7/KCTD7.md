---
symbol: "KCTD7"
type: "gene"
col: 14353
ensembl_id: "ENSG00000243335"
name: "potassium channel tetramerization domain containing 7"
location: "7q11.21"
module: 40
arm: "+"
pooled_cpm: 34.15
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 37
n_dd_up_clean: 0
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# KCTD7

*potassium channel tetramerization domain containing 7* — 7q11.21

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 4.04×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 3.96×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H460 3.50×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.451× (z -15.9, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAX]] (+0.73, fdr 7e-06), [[CBFA2T2]] (+0.73, fdr 7e-06), [[SRP54-AS1]] (+0.71, fdr 7e-06); moves opposite to [[TASOR]] (-0.73, fdr 7e-06), [[MED1]] (-0.67, fdr 7e-06), [[TRIM44]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MIR4458HG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14353.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 4.04×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 3.96×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H460 3.50×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.18× | +3.3 | 0.37 | 13/48 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.25× | +3.2 | 0.37 | 10/48 (AN3 CA, A-427, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 17 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14353.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.451×** | -15.9 | 0e+00 | 41/47 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.429×** | -12.0 | 1e-30 | 39/47 (A-427, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.432×** | -11.4 | 5e-28 | 40/48 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.434×** | -11.4 | 9e-28 | 25/33 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.499×** | -9.8 | 1e-20 | 36/44 (NCI-H2347, H4, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.620×** | -9.5 | 1e-19 | 41/48 (NCI-H2347, RPMI-7951, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.523×** | -9.2 | 4e-18 | 41/48 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.514×** | -8.7 | 2e-16 | 28/40 (NCI-H2347, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.560×** | -7.9 | 2e-13 | 36/48 (NCI-H2347, HS-578T, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.604×** | -6.8 | 4e-10 | 33/48 (hTERT-HPNE, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.642×** | -6.3 | 2e-08 | 29/48 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.671×** | -5.6 | 8e-07 | 25/48 (A498, HS-578T, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.506×** | -5.0 | 2e-05 | 25/49 (HS-578T, Hs 766T, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.711×** | -4.8 | 6e-05 | 24/48 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.736×** | -4.3 | 6e-04 | 24/48 (C-33 A, NCI-H1792, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.748×** | -4.1 | 0.001 | 23/48 (hTERT-HPNE, A-172, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.748×** | -4.1 | 0.001 | 24/48 (NCI-H2347, LS 180, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.771×** | -3.7 | 0.007 | 17/48 (Hs 766T, SW1417, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | **0.832×** | -3.6 | 0.007 | 15/48 (LS 180, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.775×** | -3.6 | 0.008 | 19/48 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.769×** | -3.6 | 0.009 | 15/48 (NCI-H2347, AsPC-1, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.777×** | -3.6 | 0.009 | 14/48 (RPMI-7951, BT-474, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.771×** | -3.4 | 0.015 | 13/47 (AsPC-1, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **0.637×** | -3.3 | 0.018 | 17/48 (A498, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14353. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 61.7 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -27.4) |
| [[A498 (line)]] | wt | 60.5 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.229× (z -13.7) |
| [[NCI-H2347 (line)]] | alt | 38.9 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.343× (z -13.5) |
| [[A-172 (line)]] | wt | 59.7 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[NCI-H1792 (line)]] | alt | 43.1 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0426× (z -23.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.217× (z -16.9) |
| [[NCI-H460 (line)]] | wt | 33.9 | 5 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.04× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CHP-212 (line)]] | wt | 37.6 | 0 | 4 (2 ⚠) | — | [[Almonertinib (hydrochloride) (drug)]] 0.5 µM 0.0541× (z -11.2) |
| [[HOP62 (line)]] | alt | 34.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -11.3) |
| [[PANC-1 (line)]] | alt | 38.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -19.4) |
| [[SW480 (line)]] | alt | 28.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 67.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0973× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 43.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.402× (z -8.8) |
| [[SNU-423 (line)]] | alt | 48.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.452× (z -8.5) |
| [[A-427 (line)]] | wt | 34.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -15.0) |
| [[A549 (line)]] | wt | 36.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -10.4) |
| [[H4 (line)]] | wt | 47.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0655× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.181× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 41.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -15.3) |
| [[Hs 766T (line)]] | wt | 48.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 42.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -14.9) |
| [[MIA PaCa-2 (line)]] | alt | 45.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -13.4) |
| [[NCI-H1573 (line)]] | alt | 29.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.284× (z -9.4) |
| [[AN3 CA (line)]] | alt | 39.6 | 0 | 1 | — | [[ULK-101 (drug)]] 0.5 µM 0.0555× (z -8.9) |
| [[BT-474 (line)]] | alt | 19.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[C-33 A (line)]] | alt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -15.4) |
| [[C32 (line)]] | wt | 19.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -12.4) |
| [[CFPAC-1 (line)]] | alt | 24.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -9.2) |
| [[COLO 205 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.102× (z -9.6) ⚠ transcription drop; cell-cycle shift, explains ~56% of this change |
| [[HCT15 (line)]] | alt | 19.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -8.8) |
| [[HT-29 (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[J82 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[SW 900 (line)]] | alt | 40.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -12.5) |
| [[SW1417 (line)]] | alt | 35.3 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.432× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14353), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAX]] | +0.73 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[CBFA2T2]] | +0.73 | +0.81 / +0.67 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[SEC11A]] | +0.71 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[SLC17A5]] | +0.70 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[RAB6A]] | +0.70 | +0.78 / +0.60 | both halves | 7e-06 |  |
| [[HSPB11]] | +0.70 | +0.78 / +0.63 | both halves | 7e-06 |  |
| [[SDHAP2]] | +0.70 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[CAMLG]] | +0.69 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[SDHAP1]] | +0.69 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[SDHAP4-1]] | +0.68 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[TULP3]] | +0.68 | +0.68 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TASOR]] | -0.73 | -0.76 / -0.68 | both halves | 7e-06 |  |
| [[MED1]] | -0.67 | -0.71 / -0.65 | both halves | 7e-06 |  |
| [[TRIM44]] | -0.65 | -0.66 / -0.59 | both halves | 7e-06 |  |
| [[CPSF2]] | -0.65 | -0.68 / -0.59 | both halves | 7e-06 |  |
| [[CEP41]] | -0.65 | -0.65 / -0.65 | both halves | 7e-06 |  |
| [[DNAJC11]] | -0.64 | -0.70 / -0.58 | both halves | 7e-06 |  |
| [[ENC1]] | -0.64 | -0.63 / -0.58 | both halves | 7e-06 | same gene group |
| [[CDK6]] | -0.64 | -0.60 / -0.57 | both halves | 9e-06 |  |
| [[UTP20]] | -0.63 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[CPSF3]] | -0.62 | -0.70 / -0.58 | both halves | 8e-06 |  |
| [[CYREN]] | -0.62 | -0.76 / -0.43 | both halves | 3e-05 |  |
| [[ABCE1]] | -0.62 | -0.62 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR4458HG]] | B | MIR4458HG activity lowers KCTD7's level | lines that do not express MIR4458HG (12) vs lines expressing it (38) | 1.61× higher at baseline in the lines without MIR4458HG | 0.036 | ⚠ within organs, on part of the lines; also absent: PDE3B, LINC02226 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.721). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (3.9, -17.3); signed map (-42.1, 12.8). **Vector** length 114, 32.4% of its response variance represented; |z| ≥ 3 in 1,038 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.4 | -0.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~97% of this change | +3.6 | -4.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +3.6 | -6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +3.3 | -3.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.7 | +1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.4 | +2.0 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.2 | -5.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.0 | -11.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.6 | -9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.5 | -15.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.2 | -12.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.8 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -9.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.0 | -2.3 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -3.2 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | potassium channel tetramerization domain containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.21 — chr7:66,628,881-66,649,067 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32069, EPM3, CLN14 |
| Gene groups (HGNC) | BTB domain containing; KCTD family |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96MP8](https://www.uniprot.org/uniprotkb/Q96MP8) (BTB/POZ domain-containing protein KCTD7):

> Substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin ligase complex that mediates the ubiquitination of multiple substrates, leading to either their proteasomal or lysosomal degradation, or modulating their activity through non-degradative ubiquitination. Regulates voltage-gated potassium channels, thereby modulating hyperpolarizing potassium currents in neurons and inducing potassium-dependent membrane hyperpolarization. Also regulates the neuronal glutamine transporter …

**Summary**, from NCBI Gene [154881](https://www.ncbi.nlm.nih.gov/gene/154881):

> This gene encodes a member of the potassium channel tetramerization domain-containing protein family. Family members are identified on a structural basis and contain an amino-terminal domain similar to the T1 domain present in the voltage-gated potassium channel. Mutations in this gene have been associated with progressive myoclonic epilepsy-3. Alternative splicing results in multiple transcript variants.[provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:21957](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21957) · Entrez [154881](https://www.ncbi.nlm.nih.gov/gene/154881) · UniProt [Q96MP8](https://www.uniprot.org/uniprotkb/Q96MP8) · Ensembl [ENSG00000243335](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243335)

## Data

Gene col 14353: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14353); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14353, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14353]; `tensor/DDL_lfc|DDL_z.npy` [14353]; `embed/gene_vectors.npy` [14353]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14353 or target_col == 14353). Every well: [[KCTD7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCTD7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
