---
symbol: "WWC3"
type: "gene"
col: 522
ensembl_id: "ENSG00000047644"
name: "WWC family member 3"
location: "Xp22.2"
module: 143
arm: "+"
pooled_cpm: 30.81
n_lines_expressing: 46
n_dd_up: 19
n_dd_down: 10
n_dd_up_clean: 15
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# WWC3

*WWC family member 3* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.95× (z +17.4, q 0e+00, up in 37 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.35× (z +6.8, q 1e-09, up in 27 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.778× (z -5.7, q 8e-06, down in 24 of 44 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[REEP3]] (+0.62, fdr 1e-05), [[CDC42BPA]] (+0.60, fdr 1e-05), [[GNG12]] (+0.60, fdr 1e-04); moves opposite to [[RBM4B]] (-0.60, fdr 7e-06), [[ATAT1]] (-0.58, fdr 9e-06), [[ZNF816-ZNF321P]] (-0.57, fdr 4e-05).
> It is in [[Module 143]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[PPP3CA]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 522.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.95×** | +17.4 | 0e+00 | 37/40 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.70×** | +15.4 | 0e+00 | 32/34 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +9.9 | 8e-21 | 29/37 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +6.8 | 1e-09 | 27/44 (A-172, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +6.3 | 3e-08 | 29/44 (SW480, A-172, …) | all doses, flat | cell-cycle shift (explains ~1% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.39×** | +5.4 | 8e-06 | 20/44 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.2 | 2e-05 | 20/43 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.37×** | +5.1 | 2e-05 | 26/44 (NCI-H1792, NCI-H1573, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +4.8 | 1e-04 | 25/44 (BT-474, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.004 | 20/44 (A-172, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Megestrol (drug)]] 0.05 µM |  | **1.28×** | +3.9 | 0.004 | 16/44 (A549, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.004 | 16/44 (SNU-423, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.005 | 20/44 (A-172, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.006 | 16/44 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.55×** | +3.7 | 0.008 | 17/44 (LoVo, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.012 | 20/42 (NCI-H460, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.027 | 12/44 (BT-474, Hs 766T, …) | inconsistent across doses |  |
| [[DTP3 (drug)]] 5 µM |  | **1.42×** | +3.0 | 0.090 | 6/42 (A-172, Hs 766T, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 522.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.778×** | -5.7 | 8e-06 | 24/44 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.731×** | -5.0 | 1e-04 | 20/43 (LoVo, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.746×** | -4.7 | 5e-04 | 22/43 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.758×** | -4.4 | 0.001 | 22/44 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.602×** | -4.3 | 0.002 | 21/44 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.771×** | -4.0 | 0.006 | 19/41 (SW 900, A-427, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -3.8 | 0.012 | 19/43 (A-172, HS-578T, …) | top dose only | composition shift |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.809×** | -3.4 | 0.048 | 14/44 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.669×** | -3.4 | 0.048 | 17/43 (LOX-IMVI, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.814×** | -3.3 | 0.055 | 15/44 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.813×** | -3.1 | 0.087 | 9/44 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.826× | -3.1 | 0.10 | 16/44 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 522. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 48.2 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 44.6 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +14.2) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.473× (z -8.5) ⚠ toxic |
| [[HOP62 (line)]] | alt | 31.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +11.9) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 39.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.80× (z +9.4) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.189× (z -11.8) ⚠ toxic |
| [[A-172 (line)]] | wt | 44.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.66× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 22.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 17.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.58× (z +9.6) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.210× (z -9.3) ⚠ cell-cycle shift, explains ~14% of this change |
| [[NCI-H1792 (line)]] | alt | 50.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +12.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 24.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +10.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 38.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.75× (z +10.1) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.362× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 29.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.221× (z -11.3) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 42.3 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.121× (z -8.8) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 16.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.12× (z +9.1) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 19.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.61× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 34.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.95× (z +10.0) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 43.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.48× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 48.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 19.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.252× (z -10.4) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 29.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +11.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 13.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.41× (z +9.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 31.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +9.8) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 53.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 18.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.02× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 43.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.209× (z -11.8) ⚠ toxic |
| [[A498 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.50 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.85 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 522), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REEP3]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[CDC42BPA]] | +0.60 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[GNG12]] | +0.60 | +0.33 / +0.56 | both halves | 1e-04 |  |
| [[ROCK2]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ARHGEF12]] | +0.57 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[WWC2]] | +0.56 | +0.43 / +0.60 | both halves | 3e-05 | same gene group |
| [[ATE1]] | +0.56 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[TULP4]] | +0.56 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[CDH2]] | +0.56 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[PAK2]] | +0.56 | +0.36 / +0.56 | both halves | 9e-05 |  |
| [[SLC25A24]] | +0.55 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[ZC3H14]] | +0.55 | +0.54 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM4B]] | -0.60 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[ATAT1]] | -0.58 | -0.57 / -0.64 | both halves | 9e-06 |  |
| [[ZNF816-ZNF321P]] | -0.57 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[RINT1]] | -0.56 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[CDK7]] | -0.55 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[CUL7]] | -0.54 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[CNNM4]] | -0.53 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[MAPKAPK5-AS1]] | -0.53 | -0.29 / -0.52 | both halves | 2e-04 |  |
| [[SCNM1]] | -0.53 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[PSMD5]] | -0.53 | -0.37 / -0.59 | both halves | 8e-05 |  |
| [[SUGP1]] | -0.53 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[NDUFAF7]] | -0.53 | -0.45 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP3CA]] | C | WWC3 activity raises PPP3CA's level | lines that do not express WWC3 (4) vs lines expressing it (46) | 2.41× lower at baseline in the lines without WWC3 | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZMIZ1, ADD3, RASSF5 |
| [[ZMYND11]] | C | WWC3 activity lowers ZMYND11's level | lines that do not express WWC3 (4) vs lines expressing it (46) | 1.71× higher at baseline in the lines without WWC3 | 0.096 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZMIZ1, ADD3, RASSF5 |

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.551). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-34.7, -12.2); signed map (9.8, -9.4). **Vector** length 91.4, 20.3% of its response variance represented; |z| ≥ 3 in 998 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +17.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.5 | +3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +15.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +9.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +6.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +3.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.8 | -5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.4 | -4.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.2 | -4.4 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | -3.8 | -3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.4 | -5.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.0 | -2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.5 | -3.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.4 | -2.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | WWC family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:10,015,254-10,144,474 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1280, BM042 |
| Gene groups (HGNC) | WWC family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULE0](https://www.uniprot.org/uniprotkb/Q9ULE0) (Protein WWC3):

> Regulator of the Hippo signaling pathway, also known as the Salvador-Warts-Hippo (SWH) pathway. Enhances phosphorylation of LATS1 and YAP1 and negatively regulates cell proliferation and organ growth due to a suppression of the transcriptional activity of YAP1, the major effector of the Hippo pathway.

**Summary**, from NCBI Gene [55841](https://www.ncbi.nlm.nih.gov/gene/55841):

> This gene encodes a member of the WWC family of proteins, which also includes the WWC1 (KIBRA) gene product and the WWC2 gene product. The protein encoded by this gene includes a C2 domain, which is known to mediate homodimerization in the related WWC1 gene product. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:29237](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29237) · Entrez [55841](https://www.ncbi.nlm.nih.gov/gene/55841) · UniProt [Q9ULE0](https://www.uniprot.org/uniprotkb/Q9ULE0) · Ensembl [ENSG00000047644](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000047644)

## Data

Gene col 522: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 522); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 522, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 522]; `tensor/DDL_lfc|DDL_z.npy` [522]; `embed/gene_vectors.npy` [522]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 522 or target_col == 522). Every well: [[WWC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WWC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
