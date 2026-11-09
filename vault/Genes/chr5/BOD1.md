---
symbol: "BOD1"
type: "gene"
col: 7043
ensembl_id: "ENSG00000145919"
name: "biorientation of chromosomes in cell division 1"
location: "5q35.2"
module: 122
arm: "+"
pooled_cpm: 31.58
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 9
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# BOD1

*biorientation of chromosomes in cell division 1* — 5q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.85× (z +10.4, q 2e-22, up in 26 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.74× (z +9.7, q 7e-20, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.556× (z -10.3, q 4e-22, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARFGEF2]] (+0.66, fdr 7e-06), [[WASHC2C]] (+0.61, fdr 2e-05), [[PLPBP]] (+0.60, fdr 1e-05); moves opposite to [[LUZP1]] (-0.62, fdr 1e-05), [[ARID3B]] (-0.54, fdr 3e-05), [[GDPGP1]] (-0.54, fdr 2e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7043.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +10.4 | 2e-22 | 26/36 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.52×** | +10.3 | 2e-22 | 34/48 (A-172, SNU-423, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.74×** | +9.7 | 7e-20 | 39/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +8.4 | 4e-15 | 33/44 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.64×** | +8.2 | 2e-14 | 38/48 (CFPAC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +7.4 | 1e-11 | 34/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +7.3 | 3e-11 | 31/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.49×** | +7.0 | 2e-10 | 37/48 (A-427, HEC-1-A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +6.9 | 4e-10 | 33/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +6.7 | 1e-09 | 32/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +6.3 | 2e-08 | 29/47 (LoVo, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.41×** | +6.0 | 7e-08 | 31/48 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +5.3 | 5e-06 | 2/48 (HOP62, NCI-H661) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.32×** | +4.9 | 4e-05 | 23/46 (HOP62, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.70×** | +4.9 | 5e-05 | 25/48 (LoVo, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +4.5 | 2e-04 | 21/48 (HEC-1-A, A-172, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.55×** | +4.0 | 0.002 | 16/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.012 | 11/48 (MIA PaCa-2, Panc 03.27, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.039 | 17/48 (NCI-H2030, NCI-H23, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.18× | +2.9 | 0.082 | 12/48 (HOP62, LS 180, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7043.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.556×** | -10.3 | 4e-22 | 38/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.568×** | -9.9 | 1e-20 | 37/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.679×** | -9.6 | 1e-19 | 39/48 (NCI-H2030, SNU-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.707×** | -8.6 | 1e-15 | 42/48 (A498, SW480, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.672×** | -7.0 | 3e-10 | 34/48 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.695×** | -6.4 | 2e-08 | 29/48 (A498, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.717×** | -5.8 | 4e-07 | 31/48 (A498, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.739×** | -5.1 | 2e-05 | 24/48 (SW480, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.864× | -3.7 | 0.016 | 23/48 (SW480, A498, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.823×** | -3.3 | 0.054 | 16/48 (AN3 CA, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7043. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 40.9 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.367× (z -10.5) |
| [[A-172 (line)]] | wt | 31.9 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +15.2) ⚠ cell-cycle shift, explains ~43% of this change | [[Panobinostat (drug)]] 5 µM 0.330× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 28.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.15× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 29.8 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.2) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -13.0) |
| [[SW480 (line)]] | alt | 26.6 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.41× (z +9.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 25.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +11.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.72× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 31.1 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 32.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -12.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 53.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -9.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[AsPC-1 (line)]] | alt | 24.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 38.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.105× (z -15.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 29.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +8.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 28.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +8.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 49.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 19.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.07× (z +8.9) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 53.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +9.0) | — |
| [[RKO (line)]] | wt | 30.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -9.2) |
| [[SNU-1 (line)]] | wt | 27.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -13.0) |
| [[SNU-423 (line)]] | alt | 30.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +12.3) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[SW 900 (line)]] | alt | 55.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.8) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[SW48 (line)]] | wt | 23.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -9.0) |
| [[A-427 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7043), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARFGEF2]] | +0.66 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[WASHC2C]] | +0.61 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[PLPBP]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[COPS2]] | +0.59 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[WASHC2A]] | +0.59 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[PPWD1]] | +0.57 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[SF3A1]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[C1orf43]] | +0.56 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[TMEM126B]] | +0.56 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[HINT3]] | +0.55 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[GNPDA1]] | +0.55 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[COPS5]] | +0.55 | +0.46 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LUZP1]] | -0.62 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[ARID3B]] | -0.54 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[GDPGP1]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[CCNYL1]] | -0.53 | -0.39 / -0.58 | both halves | 5e-05 |  |
| [[RCOR1]] | -0.52 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[SPRED2]] | -0.51 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[CSNK1E]] | -0.50 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[PLAUR]] | -0.49 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[TRIOBP]] | -0.49 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[LFNG]] | -0.49 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[SEMA4B]] | -0.48 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[ZFAND6]] | -0.48 | -0.43 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises BOD1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises BOD1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises BOD1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.591). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-18.5, 12.3); signed map (6.1, -33.4). **Vector** length 83.4, 18.2% of its response variance represented; |z| ≥ 3 in 1,117 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +5.2 | +10.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.2 | +6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +0.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.7 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +8.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +7.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.2 | -0.3 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.1 | -0.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.0 | -0.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -8.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.4 | -5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.6 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.6 | -5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -9.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -3.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | biorientation of chromosomes in cell division 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.2 — chr5:173,607,145-173,616,659 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously FAM44B |
| Gene groups (HGNC) | Biorientation of chromosomes in cell division family |
| Reactome | 3 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; Epigenetic regulation by WDR5-containing histone modifying complexes; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96IK1](https://www.uniprot.org/uniprotkb/Q96IK1) (Biorientation of chromosomes in cell division protein 1):

> Required for proper chromosome biorientation through the detection or correction of syntelic attachments in mitotic spindles.

**Summary**, from NCBI Gene [91272](https://www.ncbi.nlm.nih.gov/gene/91272):

> Enables protein phosphatase 2A binding activity and protein phosphatase inhibitor activity. Involved in mitotic sister chromatid biorientation; mitotic sister chromatid cohesion, centromeric; and protein localization to chromosome, centromeric region. Located in centrosome; spindle microtubule; and spindle pole. Part of outer kinetochore. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25114](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25114) · Entrez [91272](https://www.ncbi.nlm.nih.gov/gene/91272) · UniProt [Q96IK1](https://www.uniprot.org/uniprotkb/Q96IK1) · Ensembl [ENSG00000145919](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145919)

## Data

Gene col 7043: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7043); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7043, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7043]; `tensor/DDL_lfc|DDL_z.npy` [7043]; `embed/gene_vectors.npy` [7043]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7043 or target_col == 7043). Every well: [[BOD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BOD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
