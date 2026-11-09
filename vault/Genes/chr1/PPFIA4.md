---
symbol: "PPFIA4"
type: "gene"
col: 6814
ensembl_id: "ENSG00000143847"
name: "PPFI scaffold protein A4"
location: "1q32.1"
module: 103
arm: "+"
pooled_cpm: 63.61
n_lines_expressing: 46
n_dd_up: 1
n_dd_down: 32
n_dd_up_clean: 1
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# PPFIA4

*PPFI scaffold protein A4* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.12× (z +4.1, q 0.020, up in 1 of 46 measured lines) ⚠ position not correctable. The strongest without an alert is [[Roxadustat (drug)]] 5 µM: 1.43× (z +4.0, q 0.020, up in 26 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.154× (z -30.6, q 0e+00, down in 44 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3D21]] (+0.75, fdr 7e-06), [[GYS1]] (+0.72, fdr 7e-06), [[DDX41]] (+0.72, fdr 7e-06); moves opposite to [[ARAP2]] (-0.53, fdr 5e-05), [[TCF12]] (-0.52, fdr 7e-05), [[SH3D19]] (-0.51, fdr 3e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[NRN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6814.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.1 | 0.020 | 1/46 (HOP62) | inconsistent across doses |  |
| [[Roxadustat (drug)]] 5 µM |  | **1.43×** | +4.0 | 0.020 | 26/44 (BT-474, A-172, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.72× | +3.3 | 0.20 | 18/44 (HOP62, A-172, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 17 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6814.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.154×** | -30.6 | 0e+00 | 44/44 (C32, A549, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.122×** | -23.4 | 0e+00 | 44/44 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.164×** | -20.9 | 0e+00 | 43/44 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.175×** | -19.4 | 0e+00 | 43/43 (SK-MEL-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.358×** | -10.9 | 1e-25 | 34/43 (SNU-423, A-172, …) | all doses, flat | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.410×** | -10.3 | 6e-23 | 41/44 (BT-474, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.388×** | -10.1 | 4e-22 | 34/40 (C32, NCI-H1573, …) | all doses, flat | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.617×** | -7.9 | 2e-13 | 36/45 (SNU-423, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.506×** | -7.6 | 2e-12 | 29/40 (A-172, SW 900, …) | all doses, flat | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.532×** | -7.3 | 2e-11 | 34/44 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.540×** | -7.1 | 6e-11 | 35/44 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.556×** | -6.8 | 5e-10 | 33/44 (RPMI-7951, C32, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.555×** | -6.6 | 2e-09 | 34/42 (Panc 03.27, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.571×** | -6.5 | 4e-09 | 36/44 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.609×** | -5.7 | 3e-07 | 32/44 (LS 180, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.613×** | -5.7 | 5e-07 | 31/44 (C32, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.637×** | -5.2 | 6e-06 | 34/44 (C32, CFPAC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.659×** | -4.6 | 1e-04 | 25/44 (C32, NCI-H1792, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.674×** | -4.6 | 1e-04 | 26/44 (HEC-1-A, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~24% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.659×** | -4.5 | 1e-04 | 26/44 (SNU-423, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.719×** | -3.8 | 0.003 | 22/44 (J82, C32, …) | top dose only | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.748×** | -3.4 | 0.016 | 25/45 (HEC-1-A, BT-474, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.824×** | -3.2 | 0.030 | 17/44 (J82, A549, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.763×** | -3.1 | 0.034 | 20/44 (SNU-423, NCI-H1573, …) | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.768×** | -2.9 | 0.060 | 20/45 (HepG2/C3A, SW 1271, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6814. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 480 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0495× (z -35.4) |
| [[NCI-H460 (line)]] | wt | 134 | 0 | 12 (7 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0255× (z -31.4) |
| [[SNU-423 (line)]] | alt | 127 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0750× (z -27.7) |
| [[MIA PaCa-2 (line)]] | alt | 137 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0212× (z -32.6) |
| [[HEC-1-A (line)]] | alt | 66.6 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -19.5) |
| [[RPMI-7951 (line)]] | alt | 113 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -21.8) |
| [[Hs 766T (line)]] | wt | 66.2 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0764× (z -23.8) |
| [[A-172 (line)]] | wt | 115 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0221× (z -31.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.127× (z -25.5) |
| [[CFPAC-1 (line)]] | alt | 80.1 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0665× (z -28.6) |
| [[HOP62 (line)]] | alt | 84.4 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0769× (z -26.9) |
| [[J82 (line)]] | alt | 45.2 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -18.6) |
| [[NCI-H1792 (line)]] | alt | 83.6 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0786× (z -27.6) |
| [[NCI-H2030 (line)]] | alt | 36.4 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -18.5) |
| [[NCI-H2347 (line)]] | alt | 72.7 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -21.0) |
| [[SW 900 (line)]] | alt | 72.2 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0640× (z -28.1) |
| [[BT-474 (line)]] | alt | 52.8 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0248× (z -21.6) |
| [[NCI-H1573 (line)]] | alt | 35.9 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0550× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0908× (z -15.5) |
| [[NCI-H23 (line)]] | alt | 63.4 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -22.4) |
| [[Panc 03.27 (line)]] | alt | 34.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -19.8) |
| [[PANC-1 (line)]] | alt | 37.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -25.9) |
| [[SW480 (line)]] | alt | 38.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -19.4) |
| [[A549 (line)]] | wt | 40.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0576× (z -29.3) |
| [[AN3 CA (line)]] | alt | 101 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0986× (z -17.8) |
| [[C-33 A (line)]] | alt | 61.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.117× (z -13.9) |
| [[LoVo (line)]] | wt | 33.6 | 0 | 5 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.135× (z -15.2) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.146× (z -14.6) |
| [[LOX-IMVI (line)]] | wt | 34.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -18.7) |
| [[SK-MEL-2 (line)]] | alt | 124 | 0 | 5 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.00878× (z -33.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0832× (z -18.5) |
| [[A-427 (line)]] | wt | 30.3 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0482× (z -20.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -14.2) |
| [[AsPC-1 (line)]] | alt | 21.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -14.0) |
| [[COLO 205 (line)]] | alt | 25.7 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0629× (z -14.1) |
| [[HS-578T (line)]] | alt | 46.1 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0706× (z -17.6) |
| [[HT-29 (line)]] | alt | 24.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -16.9) |
| [[LS 180 (line)]] | wt | 42.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -18.2) |
| [[CHP-212 (line)]] | wt | 90.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0822× (z -16.0) |
| [[SW1417 (line)]] | alt | 19.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -14.5) |
| [[SW48 (line)]] | wt | 32.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -11.7) |
| [[H4 (line)]] | wt | 99.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0724× (z -22.5) |
| [[HCT15 (line)]] | alt | 44.6 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.119× (z -11.3) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.122× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 29.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -14.9) |
| [[SHP-77 (line)]] | alt | 46.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -10.1) |
| [[SW 1088 (line)]] | alt | 79.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0426× (z -9.5) |
| [[SW 1271 (line)]] | alt | 36.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -9.2) |
| [[A498 (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.67 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.06 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.96 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6814), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3D21]] | +0.75 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[GYS1]] | +0.72 | +0.78 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[DDX41]] | +0.72 | +0.76 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[YEATS2]] | +0.72 | +0.80 / +0.60 | both halves | 7e-06 |  |
| [[TBC1D9B]] | +0.69 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[PFKFB4]] | +0.68 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[CABIN1]] | +0.68 | +0.78 / +0.56 | both halves | 1e-05 |  |
| [[AK2]] | +0.68 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.66 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[PRSS53]] | +0.65 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[CEP250]] | +0.65 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[DPYSL4]] | +0.64 | +0.55 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARAP2]] | -0.53 | -0.61 / -0.39 | both halves | 5e-05 | same gene group |
| [[TCF12]] | -0.52 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[SH3D19]] | -0.51 | -0.47 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRN1]] | B | NRN1 activity raises PPFIA4's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.79× lower at baseline in the lines without NRN1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[ZNF141]] | B | ZNF141 activity raises PPFIA4's level | lines that do not express ZNF141 (12) vs lines expressing it (38) | 1.93× lower at baseline in the lines without ZNF141 | 0.039 | ⚠ within organs, on part of the lines; also absent: SLC1A3 |
| [[PLXNB3]] | B | PLXNB3 activity raises PPFIA4's level | lines that do not express PLXNB3 (10) vs lines expressing it (40) | 1.82× lower at baseline in the lines without PLXNB3 | 0.051 | ⚠ within organs, on part of the lines |
| [[EEF1A2]] | B | EEF1A2 activity raises PPFIA4's level | lines that do not express EEF1A2 (11) vs lines expressing it (39) | 2.18× lower at baseline in the lines without EEF1A2 | 0.058 | ⚠ within organs, on part of the lines; also absent: NRG2, RRAGD, RAB39A |
| [[APLN]] | B | APLN activity raises PPFIA4's level | lines that do not express APLN (13) vs lines expressing it (37) | 1.22× lower at baseline in the lines without APLN | 0.078 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[DDX41]] | C | DDX41's natural level strengthens PPFIA4's drug response | DDX41's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.49; direction not clear | 0.046 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.832). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.1, -17.4); signed map (-38.8, 25.8). **Vector** length 96.8, 31.1% of its response variance represented; |z| ≥ 3 in 1,164 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +4.3 | -4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +3.9 | -4.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.3 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | -3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +1.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.8 | +0.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.6 | +1.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.0 | -19.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -23.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -20.9 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -3.4 | -3.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.1 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.1 | -3.1 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | -2.6 | -2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -4.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | PPFI scaffold protein A4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:203,026,491-203,078,740 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sterile alpha motif domain containing; PPFI scaffold protein family |
| Hallmark sets | MYOGENESIS, GLYCOLYSIS, HYPOXIA |
| Reactome | 10 pathways, smallest: Acetylcholine Neurotransmitter Release Cycle; Norepinephrine Neurotransmitter Release Cycle; Receptor-type tyrosine-protein phosphatases |
| Matched by | ensembl_id |

**Function**, from UniProt [O75335](https://www.uniprot.org/uniprotkb/O75335) (Liprin-alpha-4):

> May regulate the disassembly of focal adhesions. May localize receptor-like tyrosine phosphatases type 2A at specific sites on the plasma membrane, possibly regulating their interaction with the extracellular environment and their association with substrates (By similarity).

**Summary**, from NCBI Gene [8497](https://www.ncbi.nlm.nih.gov/gene/8497):

> PPFIA4, or liprin-alpha-4, belongs to the liprin-alpha gene family. See liprin-alpha-1 (LIP1, or PPFIA1; MIM 611054) for background on liprins.[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:9248](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9248) · Entrez [8497](https://www.ncbi.nlm.nih.gov/gene/8497) · UniProt [O75335](https://www.uniprot.org/uniprotkb/O75335) · Ensembl [ENSG00000143847](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143847)

## Data

Gene col 6814: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6814); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6814, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6814]; `tensor/DDL_lfc|DDL_z.npy` [6814]; `embed/gene_vectors.npy` [6814]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6814 or target_col == 6814). Every well: [[PPFIA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPFIA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
