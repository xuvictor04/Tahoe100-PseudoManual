---
symbol: "SNX14"
type: "gene"
col: 5681
ensembl_id: "ENSG00000135317"
name: "sorting nexin 14"
location: "6q14.3"
module: 134
arm: "+"
pooled_cpm: 225.0
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 29
n_dd_up_clean: 0
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# SNX14

*sorting nexin 14* — 6q14.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 2.18×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.467× (z -18.1, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIAA1958]] (+0.60, fdr 7e-06), [[ZNF143]] (+0.58, fdr 1e-05), [[PYGL]] (+0.58, fdr 1e-05); moves opposite to [[DMAP1]] (-0.61, fdr 1e-05), [[ACP2]] (-0.57, fdr 1e-05), [[PABIR1]] (-0.56, fdr 1e-05).
> It is in [[Module 134]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5681.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 2.18×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.11× | +3.6 | 0.15 | 2/48 (Panc 03.27, CHP-212) | rises with dose | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | 1.35× | +3.4 | 0.15 | 25/48 (C32, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Naproxen (drug)]] 5 µM |  | 1.16× | +3.4 | 0.15 | 15/48 (NCI-H1573, NCI-H23, …) | top dose only | position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.09× | +3.0 | 0.38 | 0/48 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5681.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.467×** | -18.1 | 0e+00 | 47/48 (A549, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.475×** | -17.7 | 0e+00 | 47/48 (A549, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.487×** | -16.5 | 0e+00 | 45/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.521×** | -15.5 | 0e+00 | 45/49 (RKO, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.664×** | -13.8 | 4e-41 | 36/48 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.565×** | -13.1 | 5e-37 | 38/44 (C-33 A, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.588×** | -11.7 | 1e-29 | 40/45 (SNU-423, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.623×** | -11.2 | 2e-27 | 43/48 (A549, HepG2/C3A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.637×** | -10.3 | 4e-23 | 41/47 (RKO, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.653×** | -10.1 | 2e-22 | 38/48 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.656×** | -9.6 | 3e-20 | 35/47 (C32, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.504×** | -7.8 | 4e-13 | 38/49 (NCI-H1573, HS-578T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.757×** | -6.6 | 1e-09 | 39/48 (hTERT-HPNE, H4, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.757×** | -6.6 | 2e-09 | 30/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.778×** | -6.0 | 9e-08 | 29/48 (NCI-H460, BT-474, …) | top dose only | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.786×** | -5.5 | 1e-06 | 31/48 (NCI-H1792, C32, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.833×** | -5.1 | 1e-05 | 22/48 (NCI-H1573, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.829×** | -4.5 | 2e-04 | 23/48 (C32, A-172, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.828×** | -4.3 | 4e-04 | 25/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.683×** | -4.3 | 4e-04 | 31/49 (C32, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.889× | -3.9 | 0.002 | 11/48 (A549, J82, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.789×** | -3.8 | 0.003 | 26/48 (NCI-H23, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.792×** | -3.7 | 0.004 | 26/47 (SNU-1, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5681. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 193 | 0 | 13 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.199× (z -21.2) |
| [[PANC-1 (line)]] | alt | 464 | 0 | 11 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.266× (z -16.0) |
| [[HS-578T (line)]] | alt | 229 | 0 | 10 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.320× (z -15.7) |
| [[J82 (line)]] | alt | 258 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -19.1) |
| [[A549 (line)]] | wt | 177 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -24.5) |
| [[HEC-1-A (line)]] | alt | 252 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -17.2) |
| [[HOP62 (line)]] | alt | 243 | 0 | 9 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.300× (z -15.3) |
| [[LOX-IMVI (line)]] | wt | 223 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.357× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.428× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 372 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 166 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -25.5) |
| [[NCI-H2030 (line)]] | alt | 410 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -18.6) |
| [[BT-474 (line)]] | alt | 208 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.297× (z -15.8) |
| [[C32 (line)]] | wt | 306 | 0 | 8 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.346× (z -14.6) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.382× (z -13.7) |
| [[SK-MEL-2 (line)]] | alt | 265 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -16.1) |
| [[A-172 (line)]] | wt | 195 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -15.9) |
| [[AsPC-1 (line)]] | alt | 176 | 1 (1 ⚠) | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +14.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -15.5) |
| [[HepG2_C3A (line)]] | wt | 185 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.285× (z -16.6) |
| [[NCI-H23 (line)]] | alt | 228 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.441× (z -10.7) |
| [[RKO (line)]] | wt | 356 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -31.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.438× (z -13.5) |
| [[hTERT-HPNE (line)]] | wt | 252 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.372× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.442× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 147 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.385× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.466× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 300 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.298× (z -14.6) |
| [[SNU-423 (line)]] | alt | 309 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.389× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.433× (z -13.0) |
| [[SW 900 (line)]] | alt | 175 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.375× (z -12.1) |
| [[NCI-H1792 (line)]] | alt | 203 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.426× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.447× (z -10.3) |
| [[SW480 (line)]] | alt | 188 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.402× (z -15.5) |
| [[A-427 (line)]] | wt | 219 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.629× (z -10.7) |
| [[H4 (line)]] | wt | 187 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -13.1) |
| [[HT-29 (line)]] | alt | 190 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.426× (z -12.4) |
| [[KATO III (line)]] | alt | 173 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.390× (z -13.9) |
| [[SHP-77 (line)]] | alt | 187 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.427× (z -11.6) |
| [[SW48 (line)]] | wt | 221 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.367× (z -12.4) |
| [[A498 (line)]] | wt | 115 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.471× (z -11.4) |
| [[HCT15 (line)]] | alt | 262 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.417× (z -10.4) |
| [[LoVo (line)]] | wt | 186 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.517× (z -11.2) |
| [[LS 180 (line)]] | wt | 218 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.438× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 100.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.600× (z -9.7) |
| [[SNU-1 (line)]] | wt | 247 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -12.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 271 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -21.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[CFPAC-1 (line)]] | alt | 114 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -14.5) |
| [[SW 1271 (line)]] | alt | 427 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -10.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 186 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 196 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 195 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 101 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5681), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA1958]] | +0.60 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[ZNF143]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[PYGL]] | +0.58 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[LPIN2]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[CSNK1E]] | +0.57 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[PRKRIP1]] | +0.57 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[TPTEP2-CSNK1E]] | +0.57 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[EEF1AKMT4]] | +0.57 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[NUP58]] | +0.57 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[GAN]] | +0.56 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[DNAJC5]] | +0.56 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[TENT4A]] | +0.56 | +0.66 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DMAP1]] | -0.61 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[ACP2]] | -0.57 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[PABIR1]] | -0.56 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[ARHGAP42]] | -0.55 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[ALDH3B1]] | -0.55 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[ARAF]] | -0.54 | -0.30 / -0.56 | both halves | 2e-04 |  |
| [[MYL5]] | -0.53 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[PIGO]] | -0.53 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[TLR3]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[ZNF512B]] | -0.52 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[CHTOP]] | -0.52 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[ZNF260]] | -0.51 | -0.54 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.630). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.2, -17.5); signed map (-41.8, 20.3). **Vector** length 113, 39.5% of its response variance represented; |z| ≥ 3 in 1,459 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +9.1 | +0.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +5.2 | -4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +0.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.1 | -5.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.0 | +3.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.8 | +1.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.5 | +2.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.9 | -16.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.9 | -3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.7 | -5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.4 | -4.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -5.4 | -3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.8 | -5.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -4.5 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.3 — chr6:85,504,776-85,594,156 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RGS-PX2 |
| Gene groups (HGNC) | Sorting nexins |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5W7](https://www.uniprot.org/uniprotkb/Q9Y5W7) (Sorting nexin-14):

> Plays a role in maintaining normal neuronal excitability and synaptic transmission. May be involved in several stages of intracellular trafficking (By similarity). Required for autophagosome clearance, possibly by mediating the fusion of lysosomes with autophagosomes (Probable). Binds phosphatidylinositol 3,5-bisphosphate (PtdIns(3,5)P2), a key component of late endosomes/lysosomes. Does not bind phosphatidylinositol 3-phosphate (PtdIns(3P)).

**Summary**, from NCBI Gene [57231](https://www.ncbi.nlm.nih.gov/gene/57231):

> This gene encodes a member of the sorting nexin family. Members of this family have a phox (PX) phosphoinositide binding domain and are involved in intracellular trafficking. The encoded protein also contains a regulator of G protein signaling (RGS) domain. Regulator of G protein signaling family members are regulatory molecules that act as GTPase activating proteins for G alpha subunits of heterotrimeric G proteins. Alternate splicing results in transcript variants encoding distinct isoforms. …

**Accessions** — [HGNC:14977](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14977) · Entrez [57231](https://www.ncbi.nlm.nih.gov/gene/57231) · UniProt [Q9Y5W7](https://www.uniprot.org/uniprotkb/Q9Y5W7) · Ensembl [ENSG00000135317](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135317)

## Data

Gene col 5681: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5681); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5681, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5681]; `tensor/DDL_lfc|DDL_z.npy` [5681]; `embed/gene_vectors.npy` [5681]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5681 or target_col == 5681). Every well: [[SNX14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
