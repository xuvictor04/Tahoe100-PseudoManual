---
symbol: "TNS1"
type: "gene"
col: 1249
ensembl_id: "ENSG00000079308"
name: "tensin 1"
location: "2q35"
module: 13
arm: "+"
pooled_cpm: 54.97
n_lines_expressing: 27
n_dd_up: 4
n_dd_down: 48
n_dd_up_clean: 3
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 28
direction_downstream: 39
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# TNS1

*tensin 1* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.27× (z +4.7, q 6e-04, up in 5 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 48 drug-doses (25 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.507× (z -13.3, q 2e-37, down in 22 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAMTS14]] (+0.61, fdr 1e-05), [[SYNDIG1]] (+0.61, fdr 1e-05), [[GFPT2]] (+0.55, fdr 3e-05); moves opposite to [[HMGA1P4]] (-0.41, fdr 2e-04), [[GTF2I]] (-0.41, fdr 3e-04), [[MCM9]] (-0.41, fdr 2e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[DAB2]] → it (grade B ⚠); 39 go from it, the strongest it → [[FAM167A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1249.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +4.7 | 6e-04 | 5/25 (Hs 766T, SW1417, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.40×** | +4.7 | 6e-04 | 6/25 (Hs 766T, SW480, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.69×** | +3.8 | 0.024 | 10/25 (SW480, SHP-77, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[BAY1125976 (drug)]] 5 µM |  | **1.61×** | +3.5 | 0.073 | 11/25 (Hs 766T, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.27× | +3.2 | 0.16 | 10/25 (Hs 766T, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 26 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 48 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 25 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1249.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.507×** | -13.3 | 2e-37 | 22/25 (HS-578T, HT-29, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.538×** | -12.1 | 3e-31 | 22/25 (HT-29, RPMI-7951, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.474×** | -10.3 | 1e-22 | 22/25 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.496×** | -9.7 | 5e-20 | 19/25 (NCI-H1792, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.497×** | -9.7 | 5e-20 | 22/25 (HS-578T, RPMI-7951, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.498×** | -9.6 | 6e-20 | 21/25 (LOX-IMVI, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.513×** | -8.8 | 8e-17 | 20/25 (HS-578T, hTERT-HPNE, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.533×** | -8.7 | 3e-16 | 20/24 (LOX-IMVI, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.564×** | -7.6 | 2e-12 | 20/24 (A549, HT-29, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.581×** | -7.5 | 5e-12 | 16/25 (HT-29, RPMI-7951, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.576×** | -7.3 | 1e-11 | 17/25 (HT-29, SW480, …) | rises with dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.604×** | -6.9 | 2e-10 | 20/25 (CHP-212, KATO III, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.611×** | -6.8 | 5e-10 | 16/25 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.611×** | -6.8 | 5e-10 | 18/25 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **0.620×** | -6.3 | 1e-08 | 20/23 (HOP62, HepG2/C3A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.688×** | -5.1 | 8e-06 | 16/25 (LOX-IMVI, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.778×** | -4.8 | 3e-05 | 16/25 (HT-29, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.723×** | -4.4 | 2e-04 | 15/26 (A-172, SW480, …) | top dose only |  |
| [[Menadione (drug)]] 5 µM |  | **0.737×** | -4.0 | 0.001 | 8/24 (SW1417, HT-29, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.747×** | -4.0 | 0.001 | 16/25 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.823×** | -3.8 | 0.003 | 14/25 (HOP62, A549, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.773×** | -3.5 | 0.007 | 13/25 (A549, H4, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.775×** | -3.5 | 0.008 | 7/25 (A498, SW480, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.617×** | -3.5 | 0.009 | 12/25 (H4, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.628×** | -3.3 | 0.013 | 8/25 (Hs 766T, A549, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.629×** | -3.3 | 0.013 | 10/26 (HS-578T, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.61 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1249. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 245 | 0 | 19 (16 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0148× (z -29.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -23.0) |
| [[RPMI-7951 (line)]] | alt | 98.7 | 0 | 19 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0567× (z -28.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -20.4) |
| [[HT-29 (line)]] | alt | 162 | 0 | 18 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0259× (z -35.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0513× (z -29.0) |
| [[HOP62 (line)]] | alt | 326 | 0 | 17 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0826× (z -22.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -16.0) |
| [[HS-578T (line)]] | alt | 253 | 0 | 14 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0997× (z -29.4) |
| [[LOX-IMVI (line)]] | wt | 63.7 | 0 | 13 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -15.6) |
| [[SW480 (line)]] | alt | 30.0 | 0 | 12 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -16.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 415 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0385× (z -22.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -19.5) |
| [[SK-MEL-2 (line)]] | alt | 94.2 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0544× (z -26.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -12.3) |
| [[hTERT-HPNE (line)]] | wt | 237 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0867× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -16.1) |
| [[LoVo (line)]] | wt | 27.2 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -21.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -12.7) |
| [[NCI-H1792 (line)]] | alt | 66.5 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0318× (z -19.0) |
| [[SNU-423 (line)]] | alt | 57.9 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -15.2) |
| [[A498 (line)]] | wt | 142 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.254× (z -11.8) |
| [[A-172 (line)]] | wt | 34.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.203× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change · without an alert: [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.246× (z -9.6) |
| [[SHP-77 (line)]] | alt | 24.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0540× (z -17.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -9.2) |
| [[Hs 766T (line)]] | wt | 17.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -9.4) |
| [[BT-474 (line)]] | alt | 19.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +10.9) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[CFPAC-1 (line)]] | alt | 15.0 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.210× (z -9.3) |
| [[SW1417 (line)]] | alt | 18.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -8.5) |
| [[A-427 (line)]] | wt | 7.45 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.93 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.45 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.17 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.01 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.12 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 9.39 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.1 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.38 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.57 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.13 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.69 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.22 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 7.85 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.60 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.37 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 9.72 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 19.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1249), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTS14]] | +0.61 | +0.53 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[SYNDIG1]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[GFPT2]] | +0.55 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[CA12]] | +0.55 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[THBS2]] | +0.55 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[PMP22]] | +0.54 | +0.57 / +0.45 | both halves | 3e-05 | same gene group |
| [[SYTL3]] | +0.53 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[CSPG4]] | +0.53 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[OR9Q1]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[LINC03047]] | +0.53 | +0.56 / +0.37 | both halves | 8e-05 |  |
| [[FAM167A]] | +0.52 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[LINC01411]] | +0.52 | +0.43 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGA1P4]] | -0.41 | -0.44 / -0.29 | both halves | 2e-04 |  |
| [[GTF2I]] | -0.41 | -0.27 / -0.30 | both halves | 3e-04 |  |
| [[MCM9]] | -0.41 | -0.30 / -0.35 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 5, C 23. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DAB2]] | B | DAB2 activity raises TNS1's level | lines that do not express DAB2 (18) vs lines expressing it (32) | 3.82× lower at baseline in the lines without DAB2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: C9, NNMT, DPYSL3 |
| [[LRIG1]] | B | LRIG1 activity raises TNS1's level | lines that do not express LRIG1 (11) vs lines expressing it (39) | 3.95× lower at baseline in the lines without LRIG1 | 0.045 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MTSS1]] | B | MTSS1 activity raises TNS1's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 2.47× lower at baseline in the lines without MTSS1 | 0.049 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |
| [[PGF]] | B | PGF activity raises TNS1's level | lines that do not express PGF (12) vs lines expressing it (38) | 2.32× lower at baseline in the lines without PGF | 0.078 | ⚠ within organs, on part of the lines; also absent: ZSCAN12, LOXL1, REEP2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises TNS1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.5% of all compounds | 0.095 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ITIH5]] | C | ITIH5 activity raises TNS1's level | lines that do not express ITIH5 (37) vs lines expressing it (13) | 7.32× lower at baseline in the lines without ITIH5 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GDNF, TDRD9, ENSG00000234426; co-absent with the target |
| [[CARMN]] | C | CARMN activity raises TNS1's level | lines that do not express CARMN (40) vs lines expressing it (10) | 5.86× lower at baseline in the lines without CARMN | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN; co-absent with the target |
| [[AGTR1]] | C | AGTR1 activity raises TNS1's level | lines that do not express AGTR1 (37) vs lines expressing it (13) | 6.08× lower at baseline in the lines without AGTR1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, APBB1IP, CARMN; co-absent with the target |
| [[CA12]] | C | CA12 activity raises TNS1's level | lines that do not express CA12 (29) vs lines expressing it (21) | 3.25× lower at baseline in the lines without CA12 | 0.007 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1; co-absent with the target |
| [[GDNF]] | C | GDNF activity raises TNS1's level | lines that do not express GDNF (38) vs lines expressing it (12) | 5.17× lower at baseline in the lines without GDNF | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9; co-absent with the target |
| [[CSPG4]] | C | CSPG4 activity raises TNS1's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 2.97× lower at baseline in the lines without CSPG4 | 0.015 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1; co-absent with the target |
| [[BDKRB2]] | C | BDKRB2 activity raises TNS1's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 3.42× lower at baseline in the lines without BDKRB2 | 0.019 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003; co-absent with the target |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 14, C 25. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM167A]] | B | TNS1 activity raises FAM167A's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 2.49× lower at baseline in the lines without TNS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |
| [[LRIG1]] | B | TNS1 activity raises LRIG1's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 2.90× lower at baseline in the lines without TNS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |
| [[NDNF]] | B | TNS1 activity raises NDNF's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 2.16× lower at baseline in the lines without TNS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |
| [[MTSS1]] | B | TNS1 activity raises MTSS1's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 2.92× lower at baseline in the lines without TNS1 | 0.009 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |
| [[GPR68]] | B | TNS1 activity raises GPR68's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 1.75× lower at baseline in the lines without TNS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |
| [[METRNL]] | B | TNS1 activity raises METRNL's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 2.12× lower at baseline in the lines without TNS1 | 0.040 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |
| [[PGF]] | B | TNS1 activity raises PGF's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 1.94× lower at baseline in the lines without TNS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |
| [[MARCHF3]] | B | TNS1 activity raises MARCHF3's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 1.85× lower at baseline in the lines without TNS1 | 0.048 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |
| [[THEMIS2]] | B | TNS1 activity raises THEMIS2's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 1.89× lower at baseline in the lines without TNS1 | 0.052 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |
| [[COL6A1]] | B | TNS1 activity raises COL6A1's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 2.98× lower at baseline in the lines without TNS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |
| [[STRA6]] | B | TNS1 activity raises STRA6's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 2.65× lower at baseline in the lines without TNS1 | 0.062 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |
| [[ZNF385A]] | B | TNS1 activity raises ZNF385A's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 1.75× lower at baseline in the lines without TNS1 | 0.073 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.550). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.9, 16.5); signed map (24.1, 46.9). **Vector** length 84.2, 22.9% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.6 | -3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.1 | +0.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | +4.0 | -6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.7 | +4.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.6 |
|  | [[Glycyrrhizic acid (drug)]] 0.05 µM |  | +1.6 | +0.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +3.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -2.9 | -6.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -1.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | -2.6 | -4.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.4 | -4.8 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.0 | -2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -4.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.7 | -1.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -3.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | tensin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:217,799,588-218,033,982 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp586K0617, PPP1R155; previously TNS, MXRA6 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; SH2 domain containing; C2 tensin-type domain containing; PTEN protein phosphatases; MicroRNA protein coding host genes |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBL0](https://www.uniprot.org/uniprotkb/Q9HBL0) (Tensin-1):

> May act as a protein phosphatase and/or a lipid phosphatase (Probable). Involved in fibrillar adhesion formation. Essential for myofibroblast differentiation and myofibroblast-mediated extracellular matrix deposition. Enhances RHOA activation in the presence of DLC1. Plays a role in cell polarization and migration. May be involved in cartilage development and in linking signal transduction pathways to the cytoskeleton.

**Summary**, from NCBI Gene [7145](https://www.ncbi.nlm.nih.gov/gene/7145):

> The protein encoded by this gene localizes to focal adhesions, regions of the plasma membrane where the cell attaches to the extracellular matrix. This protein crosslinks actin filaments and contains a Src homology 2 (SH2) domain, which is often found in molecules involved in signal transduction. This protein is a substrate of calpain II. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Apr 2015]

**Accessions** — [HGNC:11973](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11973) · Entrez [7145](https://www.ncbi.nlm.nih.gov/gene/7145) · UniProt [Q9HBL0](https://www.uniprot.org/uniprotkb/Q9HBL0) · Ensembl [ENSG00000079308](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079308)

## Data

Gene col 1249: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1249); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1249, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1249]; `tensor/DDL_lfc|DDL_z.npy` [1249]; `embed/gene_vectors.npy` [1249]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1249 or target_col == 1249). Every well: [[TNS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
