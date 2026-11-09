---
symbol: "SDK1"
type: "gene"
col: 7104
ensembl_id: "ENSG00000146555"
name: "sidekick cell adhesion molecule 1"
location: "7p22.2"
module: 113
arm: "+"
pooled_cpm: 257.64
n_lines_expressing: 28
n_dd_up: 13
n_dd_down: 28
n_dd_up_clean: 13
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 5
direction_downstream: 14
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# SDK1

*sidekick cell adhesion molecule 1* — 7p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.68× (z +12.5, q 4e-33, up in 21 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.499× (z -11.4, q 2e-27, down in 22 of 25 measured lines) ⚠ toxic. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.575× (z -9.1, q 2e-17, down in 20 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JAKMIP1]] (+0.58, fdr 1e-05), [[MAP3K15]] (+0.53, fdr 2e-05), [[TANC2]] (+0.50, fdr 4e-05); moves opposite to [[IQCK]] (-0.44, fdr 4e-05), [[VPS54]] (-0.43, fdr 2e-04), [[ZNF280D]] (-0.42, fdr 5e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[KCNK13]] → it (grade B ⚠); 14 go from it, the strongest it → [[KIAA1958]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7104.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +12.5 | 4e-33 | 21/26 (RPMI-7951, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.76×** | +9.6 | 2e-19 | 14/26 (SHP-77, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.72×** | +9.2 | 5e-18 | 11/26 (A498, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +8.2 | 3e-14 | 10/26 (A498, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +7.9 | 4e-13 | 19/27 (RPMI-7951, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.53×** | +7.3 | 4e-11 | 11/26 (A498, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +6.8 | 1e-09 | 12/26 (SHP-77, MIA PaCa-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.77×** | +5.1 | 3e-05 | 10/27 (A498, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.56×** | +4.0 | 0.004 | 16/26 (SHP-77, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.006 | 9/26 (RPMI-7951, A498, …) | two highest doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.15× | +3.4 | 0.036 | 7/26 (A498, SW480, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.041 | 11/25 (SW 900, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.044 | 9/26 (RPMI-7951, A498, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.067 | 10/26 (A498, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7104.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.499×** | -11.4 | 2e-27 | 22/25 (NCI-H1792, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.500×** | -11.3 | 2e-27 | 21/25 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.505×** | -11.2 | 1e-26 | 21/24 (J82, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.578×** | -9.3 | 2e-18 | 24/27 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.575×** | -9.1 | 2e-17 | 20/26 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.694×** | -8.8 | 2e-16 | 19/26 (SNU-1, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.608×** | -8.5 | 2e-15 | 22/26 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.618×** | -8.2 | 2e-14 | 19/26 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.623×** | -8.1 | 5e-14 | 25/26 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.642×** | -7.5 | 2e-12 | 16/26 (SNU-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.445×** | -7.2 | 3e-11 | 21/27 (SW480, A498, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.660×** | -7.1 | 7e-11 | 18/26 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.625×** | -6.6 | 2e-09 | 18/24 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.685×** | -6.4 | 5e-09 | 15/26 (C-33 A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.779×** | -6.0 | 7e-08 | 17/26 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.736×** | -5.2 | 6e-06 | 16/26 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.573×** | -5.0 | 2e-05 | 18/26 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.763×** | -4.6 | 1e-04 | 16/26 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.748×** | -4.5 | 2e-04 | 17/26 (SNU-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.768×** | -4.5 | 2e-04 | 15/26 (HOP62, A-427, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.769×** | -4.5 | 2e-04 | 14/26 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.784×** | -4.1 | 9e-04 | 13/26 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.798×** | -3.8 | 0.003 | 16/27 (A498, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7104. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 359 | 0 | 17 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.199× (z -16.3) |
| [[MIA PaCa-2 (line)]] | alt | 326 | 1 | 15 (8 ⚠) | [[Auranofin (drug)]] 5 µM 3.25× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -17.5) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.161× (z -15.5) |
| [[RPMI-7951 (line)]] | alt | 125 | 14 | 0 | [[Tucidinostat (drug)]] 5 µM 3.48× (z +14.1) | — |
| [[HOP62 (line)]] | alt | 452 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.362× (z -12.0) |
| [[SNU-1 (line)]] | wt | 217 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0667× (z -24.8) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.106× (z -14.5) |
| [[A498 (line)]] | wt | 178 | 8 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +15.7) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 3.07× (z +11.9) | [[TAK-901 (drug)]] 5 µM 0.209× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 1,674 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0873× (z -25.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.342× (z -11.1) |
| [[SW480 (line)]] | alt | 365 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -15.8) |
| [[A-427 (line)]] | wt | 148 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.336× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 287 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -28.9) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.147× (z -21.6) |
| [[PANC-1 (line)]] | alt | 923 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.460× (z -10.3) |
| [[SNU-423 (line)]] | alt | 690 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -21.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 164 | 1 | 4 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.41× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -14.0) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.201× (z -12.5) |
| [[J82 (line)]] | alt | 532 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -22.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 362 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.06× (z +13.0) | — |
| [[A-172 (line)]] | wt | 369 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -12.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 82.3 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +14.4) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.10× (z +10.2) | [[Harringtonine (drug)]] 0.5 µM 0.374× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 113 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.208× (z -11.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 615 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -16.7) ⚠ cell-cycle shift, explains ~55% of this change |
| [[CFPAC-1 (line)]] | alt | 190 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -9.8) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.402× (z -8.5) |
| [[H4 (line)]] | wt | 618 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.349× (z -9.1) |
| [[SW 900 (line)]] | alt | 185 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.369× (z -9.4) ⚠ toxic |
| [[BT-474 (line)]] | alt | 97.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.50× (z +11.1) | — |
| [[CHP-212 (line)]] | wt | 373 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.247× (z -10.2) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 42.3 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 20.5 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 61.5 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 18.5 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 20.0 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 51.4 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 21.6 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 42.7 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 40.8 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 23.0 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.9 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 18.3 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 17.2 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 24.3 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 17.1 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 37.2 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 30.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.9 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.2 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 32.7 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 19.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7104), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JAKMIP1]] | +0.58 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[MAP3K15]] | +0.53 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[TANC2]] | +0.50 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[ADARB1]] | +0.50 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[ELL2]] | +0.49 | +0.37 / +0.43 | both halves | 8e-05 |  |
| [[GALNT18]] | +0.49 | +0.55 / +0.37 | both halves | 8e-05 |  |
| [[PCBP3]] | +0.49 | +0.34 / +0.52 | both halves | 1e-04 |  |
| [[ISM2]] | +0.49 | +0.37 / +0.52 | both halves | 8e-05 |  |
| [[DPYSL4]] | +0.47 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[SLC45A1]] | +0.47 | +0.37 / +0.43 | both halves | 8e-05 |  |
| [[MAPT]] | +0.46 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[FYN]] | +0.46 | +0.35 / +0.51 | both halves | 1e-04 | pathway: Cell junction organization |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQCK]] | -0.44 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[VPS54]] | -0.43 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[ZNF280D]] | -0.42 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[TADA2B]] | -0.42 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[JHY]] | -0.40 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[CTSO]] | -0.40 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[TLR3]] | -0.39 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[AMIGO2]] | -0.39 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[PAIP1]] | -0.39 | -0.21 / -0.46 | both halves | 6e-04 |  |
| [[HNF4G]] | -0.39 | -0.29 / -0.34 | both halves | 2e-04 |  |
| [[STK36]] | -0.38 | -0.22 / -0.45 | both halves | 6e-04 |  |
| [[SMPDL3A]] | -0.38 | -0.27 / -0.34 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNK13]] | B | KCNK13 activity raises SDK1's level | lines that do not express KCNK13 (9) vs lines expressing it (41) | 4.85× lower at baseline in the lines without KCNK13 | 0.032 | ⚠ within organs, on part of the lines; also absent: TMEM170B, TMEM145, LINC02609; maybe low, not absent |
| [[NAV2]] | B | NAV2 activity raises SDK1's level | lines that do not express NAV2 (17) vs lines expressing it (33) | 3.20× lower at baseline in the lines without NAV2 | 0.043 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1 |
| [[JAKMIP1]] | C | JAKMIP1 activity raises SDK1's level | lines that do not express JAKMIP1 (27) vs lines expressing it (23) | 3.36× lower at baseline in the lines without JAKMIP1 | 0.011 | ⚠ within organs, on part of the lines; also absent: CHST8, JPH3, GABBR2; co-absent with the target |
| [[PCBP3]] | C | PCBP3 activity raises SDK1's level | lines that do not express PCBP3 (22) vs lines expressing it (28) | 4.40× lower at baseline in the lines without PCBP3 | 0.015 | ⚠ within organs, on part of the lines; also absent: SDK1, RBM20, ANO4; co-absent with the target |
| [[PDZD4]] | C | PDZD4 activity raises SDK1's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 3.34× lower at baseline in the lines without PDZD4 | 0.058 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 11, C 3. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA1958]] | B | SDK1 activity raises KIAA1958's level | lines that do not express SDK1 (22) vs lines expressing it (28) | 1.29× lower at baseline in the lines without SDK1 | 0.029 | ⚠ within organs, on part of the lines; also absent: PCBP3, ACKR3, SLIT3 |
| [[FIBCD1]] | B | SDK1 activity raises FIBCD1's level | lines that do not express SDK1 (22) vs lines expressing it (28) | 1.67× lower at baseline in the lines without SDK1 | 0.040 | ⚠ within organs, on part of the lines; also absent: PCBP3, ACKR3, SLIT3 |
| [[CAMK2B]] | B | SDK1 activity raises CAMK2B's level | lines that do not express SDK1 (22) vs lines expressing it (28) | 1.76× lower at baseline in the lines without SDK1 | 0.043 | ⚠ within organs, on part of the lines; also absent: PCBP3, ACKR3, SLIT3 |
| [[WASF1]] | B | SDK1 activity weakens WASF1's drug response | lines that do not express SDK1 (21) vs lines expressing it (26) | the lines without SDK1 respond 1.33× as strongly (z diff -0.81); strongest at Belinostat 5 µM: 1.60x vs 1.14x (z diff -2.5) | 0.046 | ⚠ within organs, on part of the lines; also absent: PCBP3, ACKR3, SLIT3; target measured in part of the lines; artifact flags |
| [[KCNK13]] | B | SDK1 activity raises KCNK13's level | lines that do not express SDK1 (22) vs lines expressing it (28) | 1.63× lower at baseline in the lines without SDK1 | 0.054 | ⚠ within organs, on part of the lines; also absent: PCBP3, ACKR3, SLIT3 |
| [[DOCK11]] | B | SDK1 activity raises DOCK11's level | lines that do not express SDK1 (22) vs lines expressing it (28) | 2.25× lower at baseline in the lines without SDK1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PCBP3, ACKR3, SLIT3 |
| [[CPNE5]] | B | SDK1 activity strengthens CPNE5's drug response | lines that do not express SDK1 (19) vs lines expressing it (23) | the lines without SDK1 respond 0.54× as strongly (z diff +0.98); strongest at Ouabain (Octahydrate) 0.5 µM: 0.71x vs 0.28x (z diff +3.2) | 0.070 | ⚠ within organs, on part of the lines; also absent: PCBP3, ACKR3, SLIT3; target measured in part of the lines; artifact flags |
| [[PPP4R4]] | B | SDK1 activity raises PPP4R4's level | lines that do not express SDK1 (22) vs lines expressing it (28) | 2.30× lower at baseline in the lines without SDK1 | 0.089 | ⚠ within organs, on part of the lines; also absent: PCBP3, ACKR3, SLIT3 |
| [[WASF1]] | B | SDK1 activity raises WASF1's level | lines that do not express SDK1 (22) vs lines expressing it (28) | 1.54× lower at baseline in the lines without SDK1 | 0.096 | ⚠ within organs, on part of the lines; also absent: PCBP3, ACKR3, SLIT3 |
| [[GPR155]] | B | SDK1 activity raises GPR155's level | lines that do not express SDK1 (22) vs lines expressing it (28) | 1.77× lower at baseline in the lines without SDK1 | 0.097 | ⚠ within organs, on part of the lines; also absent: PCBP3, ACKR3, SLIT3 |
| [[TADA2B]] | B | SDK1 activity lowers TADA2B's level | lines that do not express SDK1 (22) vs lines expressing it (28) | 1.20× higher at baseline in the lines without SDK1 | 0.098 | ⚠ within organs, on part of the lines; also absent: PCBP3, ACKR3, SLIT3 |
| [[PCBP3]] | C | SDK1 activity raises PCBP3's level | lines that do not express SDK1 (22) vs lines expressing it (28) | 4.34× lower at baseline in the lines without SDK1 | 0.010 | ⚠ within organs, on part of the lines; also absent: PCBP3, ACKR3, SLIT3; co-absent with the target |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.448). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (5.5, 45.3); signed map (-29.2, 35.4). **Vector** length 105, 29.7% of its response variance represented; |z| ≥ 3 in 1,094 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.3 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +12.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +7.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.6 | +9.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +4.0 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.1 | +3.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.7 | -8.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.3 | -11.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.7 | -4.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.6 | -4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -3.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | -0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -5.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | sidekick cell adhesion molecule 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.2 — chr7:3,301,252-4,269,000 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31425 |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; Sidekick cell adhesion molecule family |
| Reactome | 3 pathways, smallest: Cell-cell junction organization; Cell junction organization; Cell-Cell communication |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z5N4](https://www.uniprot.org/uniprotkb/Q7Z5N4) (Protein sidekick-1):

> Adhesion molecule that promotes lamina-specific synaptic connections in the retina. Expressed in specific subsets of interneurons and retinal ganglion cells (RGCs) and promotes synaptic connectivity via homophilic interactions.

**Summary**, from NCBI Gene [221935](https://www.ncbi.nlm.nih.gov/gene/221935):

> The protein encoded by this gene is a member of the immunoglobulin superfamily. The protein contains six immunoglobulin-like domains and thirteen fibronectin type III domains. Fibronectin type III domains are present in both extracellular and intracellular proteins and tandem repeats are known to contain binding sites for DNA, heparin and the cell surface. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:19307](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19307) · Entrez [221935](https://www.ncbi.nlm.nih.gov/gene/221935) · UniProt [Q7Z5N4](https://www.uniprot.org/uniprotkb/Q7Z5N4) · Ensembl [ENSG00000146555](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146555)

## Data

Gene col 7104: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7104); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7104, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7104]; `tensor/DDL_lfc|DDL_z.npy` [7104]; `embed/gene_vectors.npy` [7104]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7104 or target_col == 7104). Every well: [[SDK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
