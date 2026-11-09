---
symbol: "RAB2A"
type: "gene"
col: 2454
ensembl_id: "ENSG00000104388"
name: "RAB2A, member RAS oncogene family"
location: "8q12.1-q12.2"
module: 56
arm: "+"
pooled_cpm: 315.97
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# RAB2A

*RAB2A, member RAS oncogene family* — 8q12.1-q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.96× (z +9.0, q 1e-16, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.662× (z -14.9, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPA]] (+0.74, fdr 7e-06), [[EIF2AK3]] (+0.71, fdr 7e-06), [[TXNDC11]] (+0.68, fdr 7e-06); moves opposite to [[GCFC2]] (-0.65, fdr 1e-05), [[GPATCH4]] (-0.63, fdr 1e-05), [[POGLUT1]] (-0.62, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PAPSS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2454.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.96×** | +9.0 | 1e-16 | 46/49 (A498, hTERT-HPNE, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.39×** | +8.6 | 3e-15 | 31/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +7.1 | 3e-10 | 31/48 (RKO, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +7.0 | 5e-10 | 32/47 (SHP-77, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.53×** | +5.7 | 1e-06 | 32/48 (hTERT-HPNE, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | **1.24×** | +5.5 | 3e-06 | 26/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.18× | +4.3 | 0.001 | 21/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.16× | +3.9 | 0.007 | 17/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.11× | +3.8 | 0.010 | 3/48 (SW48, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.14× | +3.3 | 0.049 | 14/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 5 µM |  | 1.09× | +3.1 | 0.088 | 1/49 (MIA PaCa-2) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2454.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.662×** | -14.9 | 0e+00 | 44/48 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.762×** | -9.8 | 2e-20 | 36/49 (A549, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **0.754×** | -6.9 | 6e-10 | 30/47 (HOP62, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.755×** | -6.9 | 6e-10 | 33/48 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.773×** | -6.6 | 6e-09 | 27/48 (A498, AsPC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.775×** | -6.5 | 8e-09 | 43/48 (NCI-H2347, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.784×** | -6.2 | 4e-08 | 27/48 (A498, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.785×** | -6.2 | 5e-08 | 25/48 (A498, AsPC-1, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.856× | -5.6 | 1e-06 | 22/48 (A549, J82, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.857× | -5.6 | 1e-06 | 16/48 (RPMI-7951, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.805×** | -5.5 | 1e-06 | 27/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.804×** | -5.4 | 4e-06 | 25/48 (hTERT-HPNE, HOP62, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.818×** | -4.9 | 3e-05 | 25/48 (J82, HS-578T, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.831×** | -4.7 | 1e-04 | 25/48 (HT-29, AsPC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.840× | -4.4 | 3e-04 | 21/48 (J82, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.876× | -3.4 | 0.022 | 20/48 (A-172, SW 900, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.916× | -3.1 | 0.045 | 3/48 (A498, HS-578T, …) | rises with dose |  |
| [[Brimonidine (drug)]] 5 µM |  | 0.888× | -3.0 | 0.065 | 4/48 (NCI-H460, COLO 205, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.920× | -3.0 | 0.065 | 4/48 (J82, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2454. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 605 | 2 (1 ⚠) | 9 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 2.48× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.590× (z -15.6) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.487× (z -15.0) |
| [[AsPC-1 (line)]] | alt | 515 | 1 | 7 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.61× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -16.2) |
| [[HOP62 (line)]] | alt | 426 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -26.5) |
| [[A-172 (line)]] | wt | 283 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -18.4) |
| [[HT-29 (line)]] | alt | 368 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -20.4) |
| [[hTERT-HPNE (line)]] | wt | 356 | 2 | 4 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 2.89× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -18.2) |
| [[J82 (line)]] | alt | 363 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -23.3) |
| [[NCI-H2347 (line)]] | alt | 393 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.545× (z -18.6) |
| [[HS-578T (line)]] | alt | 697 | 1 | 4 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 2.42× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -22.5) |
| [[PANC-1 (line)]] | alt | 244 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +16.8) | — |
| [[CFPAC-1 (line)]] | alt | 273 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.584× (z -14.2) |
| [[Hs 766T (line)]] | wt | 393 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.511× (z -11.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.629× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 277 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.86× (z +11.0) | — |
| [[NCI-H460 (line)]] | wt | 169 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +13.9) | — |
| [[RKO (line)]] | wt | 305 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 1.89× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 272 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.539× (z -15.5) |
| [[SW480 (line)]] | alt | 216 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +12.4) | — |
| [[LoVo (line)]] | wt | 262 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.606× (z -10.7) |
| [[LS 180 (line)]] | wt | 278 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 262 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -19.7) |
| [[NCI-H2030 (line)]] | alt | 342 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.66× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -21.5) |
| [[RPMI-7951 (line)]] | alt | 404 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -15.5) |
| [[SHP-77 (line)]] | alt | 364 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 1.91× (z +10.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.67× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 397 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -14.5) |
| [[A549 (line)]] | wt | 319 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -17.9) ⚠ cell-cycle shift, explains ~23% of this change |
| [[BT-474 (line)]] | alt | 297 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.551× (z -9.9) ⚠ cell-cycle shift, explains ~45% of this change |
| [[C32 (line)]] | wt | 382 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -10.2) ⚠ cell-cycle shift, explains ~23% of this change |
| [[COLO 205 (line)]] | alt | 258 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 380 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.556× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~40% of this change |
| [[NCI-H1573 (line)]] | alt | 161 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -26.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H661 (line)]] | alt | 332 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 269 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.80× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 228 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.603× (z -9.0) |
| [[SW 1271 (line)]] | alt | 300 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -8.5) |
| [[A-427 (line)]] | wt | 215 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 234 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 179 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 219 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 346 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 311 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 238 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 230 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 385 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 306 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 297 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 300 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 378 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 243 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2454), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPA]] | +0.74 | +0.84 / +0.67 | both halves | 7e-06 |  |
| [[EIF2AK3]] | +0.71 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[TXNDC11]] | +0.68 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[PDXDC2P]] | +0.68 | +0.75 / +0.58 | both halves | 7e-06 |  |
| [[COPB1]] | +0.68 | +0.70 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 494 |
| [[DNAJC3]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[PDXDC1]] | +0.68 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[ACBD3]] | +0.67 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[HERPUD1]] | +0.67 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[CYB561D2]] | +0.67 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[IER3IP1]] | +0.66 | +0.76 / +0.54 | both halves | 1e-05 |  |
| [[MACO1]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCFC2]] | -0.65 | -0.74 / -0.55 | both halves | 1e-05 |  |
| [[GPATCH4]] | -0.63 | -0.71 / -0.51 | both halves | 1e-05 |  |
| [[POGLUT1]] | -0.62 | -0.68 / -0.53 | both halves | 1e-05 |  |
| [[ZC3H7B]] | -0.61 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[ZNF507]] | -0.59 | -0.70 / -0.37 | both halves | 8e-05 |  |
| [[ZNF649]] | -0.58 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[PTP4A3]] | -0.58 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[ST7L]] | -0.57 | -0.68 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAPSS2]] | B | PAPSS2 activity strengthens RAB2A's drug response | lines that do not express PAPSS2 (15) vs lines expressing it (34) | the lines without PAPSS2 respond 0.74× as strongly (z diff +1.22); strongest at Homoharringtonine 5 µM: 0.77x vs 0.57x (z diff +3.4) | 0.074 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, A4GALT, NT5E; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.733). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.0, -33.4); signed map (-49.8, 10.5). **Vector** length 126, 46.0% of its response variance represented; |z| ≥ 3 in 1,151 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.58 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.60 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.60 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.1 | +7.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +6.6 | -6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +6.4 | -6.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +5.8 | -4.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +0.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.2 | +0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | -2.2 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.5 | +3.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.8 | -14.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.6 | -6.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.5 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.1 | -5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -6.3 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -5.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -4.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | RAB2A, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q12.1-q12.2 — chr8:60,516,936-60,623,644 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously RAB2 |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 6 pathways, smallest: Golgi Cisternae Pericentriolar Stack Reorganization; RAB geranylgeranylation; Mitotic Prophase |
| Matched by | ensembl_id |

**Function**, from UniProt [P61019](https://www.uniprot.org/uniprotkb/P61019) (Ras-related protein Rab-2A):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between active GTP-bound and inactive GDP-bound states. In their active state, drive transport of vesicular carriers from donor organelles to acceptor organelles to regulate the membrane traffic that maintains organelle identity and morphology. RAB2A regulates autophagy by promoting autophagosome-lysosome fusion via recruitment of …

**Summary**, from NCBI Gene [5862](https://www.ncbi.nlm.nih.gov/gene/5862):

> The protein encoded by this gene belongs to the Rab family, members of which are small molecular weight guanosine triphosphatases (GTPases) that contain highly conserved domains involved in GTP binding and hydrolysis. The Rabs are membrane-bound proteins, involved in vesicular fusion and trafficking. This protein is a resident of pre-Golgi intermediates, and is required for protein transport from the endoplasmic reticulum (ER) to the Golgi complex. Alternatively spliced transcript variants …

**Accessions** — [HGNC:9763](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9763) · Entrez [5862](https://www.ncbi.nlm.nih.gov/gene/5862) · UniProt [P61019](https://www.uniprot.org/uniprotkb/P61019) · Ensembl [ENSG00000104388](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104388)

## Data

Gene col 2454: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2454); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2454, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2454]; `tensor/DDL_lfc|DDL_z.npy` [2454]; `embed/gene_vectors.npy` [2454]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2454 or target_col == 2454). Every well: [[RAB2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
