---
symbol: "MEIS3"
type: "gene"
col: 2601
ensembl_id: "ENSG00000105419"
name: "Meis homeobox 3"
location: "19q13.32"
module: 136
arm: "+"
pooled_cpm: 16.03
n_lines_expressing: 38
n_dd_up: 10
n_dd_down: 33
n_dd_up_clean: 10
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 7
direction_downstream: 12
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# MEIS3

*Meis homeobox 3* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.56× (z +7.1, q 6e-10, up in 26 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.344× (z -12.1, q 9e-31, down in 33 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RTN2]] (+0.67, fdr 7e-06), [[EPOR]] (+0.60, fdr 1e-05), [[PLIN3]] (+0.60, fdr 2e-05); moves opposite to [[HINT3]] (-0.57, fdr 1e-05), [[MBTPS2]] (-0.56, fdr 1e-05), [[MANEA]] (-0.55, fdr 1e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[CRMP1]] → it (grade B ⚠); 12 go from it, the strongest it → [[NLGN2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2601.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +7.1 | 6e-10 | 26/36 (SW1417, HT-29, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +6.1 | 3e-07 | 22/36 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.5 | 6e-06 | 19/36 (A-427, PANC-1, …) | rises with dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.48×** | +4.5 | 0.001 | 16/35 (NCI-H460, RPMI-7951, …) | two highest doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +3.9 | 0.011 | 14/35 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +3.7 | 0.019 | 14/36 (SW1417, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.019 | 16/34 (NCI-H460, J82, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.029 | 14/36 (SK-MEL-2, H4, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.35×** | +3.4 | 0.035 | 10/36 (HT-29, BT-474, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.035 | 18/36 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2601.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.344×** | -12.1 | 9e-31 | 33/36 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.365×** | -11.4 | 1e-27 | 31/36 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.367×** | -11.3 | 2e-27 | 29/35 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.409×** | -10.1 | 7e-22 | 26/34 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.401×** | -9.9 | 3e-21 | 25/32 (LoVo, AsPC-1, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.482×** | -8.3 | 1e-14 | 25/36 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.260×** | -8.0 | 1e-13 | 26/36 (A549, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.500×** | -7.5 | 4e-12 | 23/36 (NCI-H23, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.543×** | -6.9 | 3e-10 | 23/36 (A-172, A-427, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.551×** | -6.7 | 1e-09 | 20/34 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.558×** | -6.6 | 2e-09 | 22/36 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.580×** | -6.2 | 3e-08 | 22/36 (A549, A-172, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.602×** | -5.7 | 4e-07 | 21/36 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.385×** | -5.6 | 7e-07 | 23/35 (RKO, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.709×** | -5.5 | 1e-06 | 18/35 (A549, AsPC-1, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.652×** | -4.8 | 5e-05 | 21/36 (RPMI-7951, PANC-1, …) | two highest doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.746×** | -4.7 | 9e-05 | 20/36 (AsPC-1, NCI-H1792, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.668×** | -4.5 | 2e-04 | 23/36 (HepG2/C3A, H4, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.689×** | -4.2 | 7e-04 | 18/36 (HS-578T, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.727×** | -3.5 | 0.014 | 14/36 (NCI-H23, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2601. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 26.4 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0914× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.130× (z -15.0) |
| [[NCI-H460 (line)]] | wt | 15.5 | 1 (1 ⚠) | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +9.6) ⚠ cell-cycle shift, explains ~77% of this change | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.128× (z -13.1) |
| [[A549 (line)]] | wt | 43.6 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -16.6) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 58.6 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.149× (z -13.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -11.4) |
| [[A-172 (line)]] | wt | 27.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -13.4) |
| [[H4 (line)]] | wt | 62.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0822× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.185× (z -11.2) |
| [[AsPC-1 (line)]] | alt | 11.3 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0394× (z -12.5) ⚠ toxic |
| [[HOP62 (line)]] | alt | 19.5 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.224× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 46.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.140× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.163× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 11.9 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.137× (z -9.8) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0280× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 4.91 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0325× (z -11.5) |
| [[NCI-H23 (line)]] | alt | 20.3 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +8.5) | [[Auranofin (drug)]] 5 µM 0.0453× (z -18.8) |
| [[SW480 (line)]] | alt | 23.6 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.22× (z +8.8) | [[Lonafarnib (drug)]] 5 µM 0.0840× (z -10.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.275× (z -9.9) |
| [[C-33 A (line)]] | alt | 61.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.214× (z -10.3) ⚠ toxic |
| [[HT-29 (line)]] | alt | 8.21 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 6.12× (z +10.7) | [[Digitoxin (drug)]] 0.5 µM 0.0274× (z -15.2) |
| [[RKO (line)]] | wt | 42.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 20.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -13.3) |
| [[A498 (line)]] | wt | 19.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -9.6) ⚠ cell-cycle shift, explains ~77% of this change |
| [[C32 (line)]] | wt | 10.4 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0917× (z -10.0) |
| [[HS-578T (line)]] | alt | 39.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.270× (z -8.7) |
| [[J82 (line)]] | alt | 26.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.186× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 19.9 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.204× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 5.58 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0816× (z -9.6) |
| [[PANC-1 (line)]] | alt | 6.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +11.3) | — |
| [[SHP-77 (line)]] | alt | 18.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.204× (z -8.6) ⚠ toxic |
| [[SW 900 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 5.26 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 10.9× (z +11.7) | — |
| [[AN3 CA (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.19 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.73 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2601), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTN2]] | +0.67 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[EPOR]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[PLIN3]] | +0.60 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[TNNT1]] | +0.60 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[FRMD8]] | +0.58 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[C11orf91]] | +0.58 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ELL]] | +0.58 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ARID3B]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[RABGEF1]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[CDR2L]] | +0.57 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[HAPLN3]] | +0.56 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[ORMDL2]] | +0.56 | +0.41 / +0.67 | both halves | 4e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HINT3]] | -0.57 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[MBTPS2]] | -0.56 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[MANEA]] | -0.55 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[DLEU1]] | -0.54 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[POMK]] | -0.53 | -0.39 / -0.59 | both halves | 5e-05 |  |
| [[TRUB1]] | -0.53 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[NT5DC1]] | -0.51 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[DIS3L]] | -0.51 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[TBC1D5]] | -0.50 | -0.50 / -0.43 | both halves | 4e-05 |  |
| [[MBNL3]] | -0.50 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[HNF4G]] | -0.49 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[PRTFDC1]] | -0.49 | -0.50 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRMP1]] | B | CRMP1 activity raises MEIS3's level | lines that do not express CRMP1 (19) vs lines expressing it (31) | 2.81× lower at baseline in the lines without CRMP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: JAM3, NHSL2, ENSG00000286033; maybe low, not absent |
| [[TGFB1]] | B | TGFB1 activity raises MEIS3's level | lines that do not express TGFB1 (8) vs lines expressing it (42) | 3.70× lower at baseline in the lines without TGFB1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ZDHHC2, NUAK1, SLC22A4; maybe low, not absent |
| [[SERPINE1]] | B | SERPINE1 activity raises MEIS3's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 2.45× lower at baseline in the lines without SERPINE1 | 0.060 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |
| [[ABL1]] | B | ABL1 activity raises MEIS3's level | compounds that target ABL1: 4 of 6 lower it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 6.2% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers MEIS3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers MEIS3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NLGN2]] | C | NLGN2 activity raises MEIS3's level | lines that do not express NLGN2 (4) vs lines expressing it (46) | 4.53× lower at baseline in the lines without NLGN2 | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with CTNNB1; also absent: FSD1L, SLC29A4, DPF1 |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NLGN2]] | B | MEIS3 activity raises NLGN2's level | lines that do not express MEIS3 (12) vs lines expressing it (38) | 2.41× lower at baseline in the lines without MEIS3 | 0.008 | ⚠ within organs, on part of the lines; also absent: PARVG, HECW2, RFLNB |
| [[NPAS1]] | B | MEIS3 activity raises NPAS1's level | lines that do not express MEIS3 (12) vs lines expressing it (38) | 2.51× lower at baseline in the lines without MEIS3 | 0.013 | ⚠ within organs, on part of the lines; also absent: PARVG, HECW2, RFLNB |
| [[RTN2]] | B | MEIS3 activity raises RTN2's level | lines that do not express MEIS3 (12) vs lines expressing it (38) | 1.64× lower at baseline in the lines without MEIS3 | 0.023 | ⚠ within organs, on part of the lines; also absent: PARVG, HECW2, RFLNB |
| [[MYO5C]] | B | MEIS3 activity lowers MYO5C's level | lines that do not express MEIS3 (12) vs lines expressing it (38) | 4.11× higher at baseline in the lines without MEIS3 | 0.029 | ⚠ within organs, on part of the lines; also absent: PARVG, HECW2, RFLNB |
| [[MICAL1]] | B | MEIS3 activity raises MICAL1's level | lines that do not express MEIS3 (12) vs lines expressing it (38) | 2.18× lower at baseline in the lines without MEIS3 | 0.032 | ⚠ within organs, on part of the lines; also absent: PARVG, HECW2, RFLNB |
| [[ADAMTSL4]] | B | MEIS3 activity raises ADAMTSL4's level | lines that do not express MEIS3 (12) vs lines expressing it (38) | 1.61× lower at baseline in the lines without MEIS3 | 0.058 | ⚠ within organs, on part of the lines; also absent: PARVG, HECW2, RFLNB |
| [[MBNL3]] | B | MEIS3 activity lowers MBNL3's level | lines that do not express MEIS3 (12) vs lines expressing it (38) | 1.15× higher at baseline in the lines without MEIS3 | 0.065 | ⚠ within organs, on part of the lines; also absent: PARVG, HECW2, RFLNB |
| [[TUBB6]] | B | MEIS3 activity raises TUBB6's level | lines that do not express MEIS3 (12) vs lines expressing it (38) | 3.14× lower at baseline in the lines without MEIS3 | 0.065 | ⚠ within organs, on part of the lines; also absent: PARVG, HECW2, RFLNB |
| [[AKAP12]] | B | MEIS3 activity raises AKAP12's level | lines that do not express MEIS3 (12) vs lines expressing it (38) | 3.80× lower at baseline in the lines without MEIS3 | 0.077 | ⚠ within organs, on part of the lines; also absent: PARVG, HECW2, RFLNB |
| [[SERPINE1]] | B | MEIS3 activity raises SERPINE1's level | lines that do not express MEIS3 (12) vs lines expressing it (38) | 4.50× lower at baseline in the lines without MEIS3 | 0.079 | ⚠ within organs, on part of the lines; also absent: PARVG, HECW2, RFLNB |
| [[LRRC8A]] | B | MEIS3 activity lowers LRRC8A's level | lines that do not express MEIS3 (12) vs lines expressing it (38) | 1.50× higher at baseline in the lines without MEIS3 | 0.084 | ⚠ within organs, on part of the lines; also absent: PARVG, HECW2, RFLNB |
| cells under [[Tirabrutinib (drug)]] 0.5 µM | B | MEIS3 activity raises the cells' numbers under Tirabrutinib 0.5 µM (protects the cells) | lines that do not express MEIS3 (12) vs lines expressing it (36) | the lines without MEIS3: 0.91× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; also absent: PARVG, HECW2, RFLNB |

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.656). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.5, -1.3); signed map (-24.2, 24.5). **Vector** length 93.3, 22.7% of its response variance represented; |z| ≥ 3 in 1,021 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +7.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.0 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +3.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +4.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.2 | +2.1 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -5.0 | -4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.2 | -4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.8 | -8.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.7 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -6.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.2 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | Meis homeobox 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:47,403,124-47,419,527 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MRG2, DKFZp547H236 |
| Gene groups (HGNC) | TALE class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99687](https://www.uniprot.org/uniprotkb/Q99687) (Homeobox protein Meis3):

> Transcriptional regulator which directly modulates PDPK1 expression, thus promoting survival of pancreatic beta-cells. Also regulates expression of NDFIP1, BNIP3, and CCNG1.

**Summary**, from NCBI Gene [56917](https://www.ncbi.nlm.nih.gov/gene/56917):

> This gene encodes a homeobox protein and probable transcriptional regulator. The orthologous protein in mouse controls expression of 3-phosphoinositide dependent protein kinase 1, which promotes survival of pancreatic beta-cells. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:29537](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29537) · Entrez [56917](https://www.ncbi.nlm.nih.gov/gene/56917) · UniProt [Q99687](https://www.uniprot.org/uniprotkb/Q99687) · Ensembl [ENSG00000105419](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105419)

## Data

Gene col 2601: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2601); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2601, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2601]; `tensor/DDL_lfc|DDL_z.npy` [2601]; `embed/gene_vectors.npy` [2601]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2601 or target_col == 2601). Every well: [[MEIS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEIS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
