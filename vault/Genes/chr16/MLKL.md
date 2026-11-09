---
symbol: "MLKL"
type: "gene"
col: 9645
ensembl_id: "ENSG00000168404"
name: "mixed lineage kinase domain like pseudokinase"
location: "16q23.1"
module: 97
arm: "+"
pooled_cpm: 36.86
n_lines_expressing: 43
n_dd_up: 9
n_dd_down: 50
n_dd_up_clean: 7
n_dd_down_clean: 38
in_vector_space: true
direction_upstream: 11
direction_downstream: 2
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# MLKL

*mixed lineage kinase domain like pseudokinase* — 16q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 5 µM: 2.10× (z +5.7, q 5e-06, up in 19 of 34 measured lines) ⚠ toxic. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.5 µM: 1.31× (z +4.1, q 0.014, up in 18 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 50 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.202× (z -23.6, q 0e+00, down in 40 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OSBPL5]] (+0.57, fdr 9e-06), [[TLR2]] (+0.56, fdr 2e-05), [[IL18R1]] (+0.56, fdr 2e-05); moves opposite to [[NR0B1]] (-0.49, fdr 3e-05), [[GALNT7]] (-0.44, fdr 3e-05), [[SYTL2]] (-0.43, fdr 4e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[PI3]] → it (grade B ⚠); 2 go from it, the strongest it → [[C1RL-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9645.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.10×** | +5.7 | 5e-06 | 19/34 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled); position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.014 | 18/41 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.37×** | +3.9 | 0.022 | 14/41 (Hs 766T, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.18× | +3.6 | 0.044 | 15/41 (Hs 766T, NCI-H1573, …) | all doses, flat |  |
| [[Econazole (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.055 | 13/41 (NCI-H1573, Hs 766T, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.073 | 11/41 (Hs 766T, NCI-H1573, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.26×** | +3.2 | 0.096 | 17/41 (A498, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.096 | 13/41 (Hs 766T, NCI-H1573, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.096 | 14/41 (NCI-H1573, Hs 766T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.096 | 13/41 (A498, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 55 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 50 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9645.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.202×** | -23.6 | 0e+00 | 40/41 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.337×** | -22.6 | 0e+00 | 36/41 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.239×** | -21.1 | 0e+00 | 41/41 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.288×** | -18.4 | 0e+00 | 39/41 (SNU-423, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.432×** | -17.5 | 0e+00 | 34/39 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.360×** | -15.0 | 0e+00 | 31/39 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.544×** | -8.9 | 3e-17 | 28/41 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.559×** | -8.6 | 8e-16 | 33/41 (LoVo, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.525×** | -7.8 | 4e-13 | 29/41 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.576×** | -7.8 | 4e-13 | 22/38 (NCI-H23, SNU-423, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.621×** | -7.0 | 1e-10 | 27/40 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.610×** | -7.0 | 1e-10 | 26/41 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.627×** | -6.3 | 1e-08 | 21/31 (NCI-H460, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.746×** | -6.1 | 5e-08 | 21/41 (A549, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.654×** | -6.0 | 8e-08 | 29/41 (H4, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.755×** | -5.8 | 2e-07 | 19/41 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.678×** | -5.5 | 1e-06 | 22/40 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.692×** | -5.4 | 2e-06 | 20/41 (LoVo, RPMI-7951, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.498×** | -5.4 | 2e-06 | 24/41 (NCI-H460, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9645. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 120 | 0 | 34 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0583× (z -35.4) |
| [[NCI-H1573 (line)]] | alt | 119 | 12 | 14 (5 ⚠) | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 4.21× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.0428× (z -32.5) |
| [[Hs 766T (line)]] | wt | 66.5 | 13 | 5 | [[Budesonide (drug)]] 5 µM 4.26× (z +11.7) | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -15.9) |
| [[A549 (line)]] | wt | 120 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0696× (z -16.9) |
| [[HOP62 (line)]] | alt | 36.6 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -16.0) |
| [[H4 (line)]] | wt | 65.5 | 0 | 10 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0562× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0633× (z -15.3) |
| [[A498 (line)]] | wt | 36.1 | 4 (3 ⚠) | 5 | [[Ixazomib citrate (drug)]] 0.5 µM 5.06× (z +15.2) | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -23.8) |
| [[LoVo (line)]] | wt | 40.3 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -20.7) |
| [[NCI-H1792 (line)]] | alt | 79.4 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0780× (z -25.9) |
| [[RKO (line)]] | wt | 47.4 | 0 | 9 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -17.9) |
| [[CFPAC-1 (line)]] | alt | 74.9 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -17.8) |
| [[AsPC-1 (line)]] | alt | 51.8 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -23.5) |
| [[NCI-H23 (line)]] | alt | 27.2 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -13.3) |
| [[A-172 (line)]] | wt | 44.5 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.103× (z -19.9) |
| [[J82 (line)]] | alt | 26.0 | 1 (1 ⚠) | 4 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.29× (z +8.9) ⚠ cell-cycle shift, explains ~46% of this change | [[Panobinostat (drug)]] 5 µM 0.244× (z -11.1) |
| [[LS 180 (line)]] | wt | 34.3 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -15.5) |
| [[MIA PaCa-2 (line)]] | alt | 31.9 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.121× (z -12.6) |
| [[SNU-423 (line)]] | alt | 29.7 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0610× (z -17.1) |
| [[SW480 (line)]] | alt | 20.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -12.3) |
| [[COLO 205 (line)]] | alt | 31.1 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0422× (z -17.3) |
| [[KATO III (line)]] | alt | 19.2 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.134× (z -11.7) |
| [[SW 900 (line)]] | alt | 18.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 17.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.250× (z -9.7) |
| [[HS-578T (line)]] | alt | 16.6 | 1 | 2 | [[Ixazomib citrate (drug)]] 0.5 µM 4.06× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -15.4) |
| [[hTERT-HPNE (line)]] | wt | 24.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0416× (z -17.1) |
| [[LOX-IMVI (line)]] | wt | 22.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -14.1) |
| [[NCI-H2030 (line)]] | alt | 47.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -17.1) |
| [[RPMI-7951 (line)]] | alt | 25.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -15.2) |
| [[Panc 03.27 (line)]] | alt | 16.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 9.80 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.0878× (z -8.6) |
| [[HT-29 (line)]] | alt | 13.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.107× (z -12.2) |
| [[SHP-77 (line)]] | alt | 10.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.140× (z -8.9) |
| [[SW48 (line)]] | wt | 18.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.109× (z -9.9) |
| [[A-427 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.57 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.08 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.51 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.36 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.48 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.37 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9645), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSBPL5]] | +0.57 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[TLR2]] | +0.56 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[IL18R1]] | +0.56 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[SQOR]] | +0.53 | +0.52 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[GAB3]] | +0.53 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[VSTM2L]] | +0.52 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[KRT6A]] | +0.52 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[PTPN1]] | +0.52 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[MT1A]] | +0.51 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[CLMP]] | +0.50 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[IL4R]] | +0.49 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[ADGRE2]] | +0.48 | +0.49 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR0B1]] | -0.49 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[GALNT7]] | -0.44 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[SYTL2]] | -0.43 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[CLIP4]] | -0.42 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[ATF3]] | -0.40 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[RFLNA]] | -0.40 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[TUFT1]] | -0.39 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[ZBTB20]] | -0.39 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[DUSP8]] | -0.38 | -0.42 / -0.37 | both halves | 7e-05 |  |
| [[IDS]] | -0.38 | -0.23 / -0.40 | both halves | 5e-04 |  |
| [[DUSP10]] | -0.38 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[CCDC92]] | -0.38 | -0.36 / -0.41 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PI3]] | B | PI3 activity raises MLKL's level | lines that do not express PI3 (27) vs lines expressing it (23) | 2.37× lower at baseline in the lines without PI3 | 0.003 | ⚠ within organs, on part of the lines; also absent: IL33, LINC01133, IL1A |
| [[NR0B1]] | B | NR0B1 activity raises MLKL's level | lines that do not express NR0B1 (38) vs lines expressing it (12) | 1.92× lower at baseline in the lines without NR0B1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, CDH19, TBXT |
| [[CLMP]] | B | CLMP activity raises MLKL's level | lines that do not express CLMP (25) vs lines expressing it (25) | 2.05× lower at baseline in the lines without CLMP | 0.033 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10 |
| [[LTBR]] | B | LTBR activity raises MLKL's level | lines that do not express LTBR (8) vs lines expressing it (42) | 1.65× lower at baseline in the lines without LTBR | 0.054 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |
| [[HS3ST3B1]] | B | HS3ST3B1 activity raises MLKL's level | lines that do not express HS3ST3B1 (18) vs lines expressing it (32) | 1.81× lower at baseline in the lines without HS3ST3B1 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |
| [[IL18R1]] | B | IL18R1 activity raises MLKL's level | lines that do not express IL18R1 (15) vs lines expressing it (35) | 1.61× lower at baseline in the lines without IL18R1 | 0.073 | ⚠ within organs, on part of the lines; also absent: JCAD |
| [[NPAS2]] | B | NPAS2 activity raises MLKL's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without NPAS2 | 0.080 | ⚠ within organs, on part of the lines |
| [[RGS2]] | B | RGS2 activity raises MLKL's level | lines that do not express RGS2 (17) vs lines expressing it (33) | 1.97× lower at baseline in the lines without RGS2 | 0.087 | ⚠ within organs, on part of the lines; also absent: LINC01393, P2RY1, MEF2C-AS1; maybe low, not absent |
| [[GLRX]] | B | GLRX activity raises MLKL's level | lines that do not express GLRX (10) vs lines expressing it (40) | 2.27× lower at baseline in the lines without GLRX | 0.089 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[NIBAN2]] | B | NIBAN2 activity raises MLKL's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 2.72× lower at baseline in the lines without NIBAN2 | 0.089 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[OAF]] | C | OAF activity raises MLKL's level | lines that do not express OAF (4) vs lines expressing it (46) | 3.24× lower at baseline in the lines without OAF | 0.028 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL3, LRP1, ALPK1; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1RL-AS1]] | B | MLKL activity raises C1RL-AS1's level | lines that do not express MLKL (7) vs lines expressing it (43) | 4.47× lower at baseline in the lines without MLKL | 0.053 | ⚠ within organs, on part of the lines; also absent: PSD4; maybe low, not absent |
| [[LTBR]] | B | MLKL activity raises LTBR's level | lines that do not express MLKL (7) vs lines expressing it (43) | 2.18× lower at baseline in the lines without MLKL | 0.073 | ⚠ within organs, on part of the lines; also absent: PSD4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.431). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.1, 14.8); signed map (17.5, 34.7). **Vector** length 116, 36.1% of its response variance represented; |z| ≥ 3 in 1,419 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | +6.4 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +6.0 | +1.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.1 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.9 | +0.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.7 | +3.9 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +4.0 | +3.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.7 | +4.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.3 | +3.1 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -4.9 | -5.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.8 | -4.0 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.7 | -4.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.7 | -8.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.8 | -4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.8 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | mixed lineage kinase domain like pseudokinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.1 — chr16:74,671,855-74,700,960 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ34389 |
| Gene groups (HGNC) | Pseudokinases |
| Reactome | 14 pathways, smallest: Microbial modulation of RIPK1-mediated regulated necrosis; Defective RIPK1-mediated regulated necrosis; TRP channels |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NB16](https://www.uniprot.org/uniprotkb/Q8NB16) (Mixed lineage kinase domain-like protein):

> Pseudokinase that acts as an executor of necroptosis, a programmed cell death process. Activated following phosphorylation by RIPK3, leading to homooligomerization, localization to the plasma membrane and execution of programmed necroptosis characterized by calcium influx and plasma membrane damage. Phosphorylated MLKL can also mediate an alternate form of necroptosis, which promotes MLKL localization to the mitochondrial membrane, leading to mitochondrial membrane damage, release of …

**Summary**, from NCBI Gene [197259](https://www.ncbi.nlm.nih.gov/gene/197259):

> This gene belongs to the protein kinase superfamily. The encoded protein contains a protein kinase-like domain; however, is thought to be inactive because it lacks several residues required for activity. This protein plays a critical role in tumor necrosis factor (TNF)-induced necroptosis, a programmed cell death process, via interaction with receptor-interacting protein 3 (RIP3), which is a key signaling molecule in necroptosis pathway. Inhibitor studies and knockdown of this gene inhibited …

**Accessions** — [HGNC:26617](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26617) · Entrez [197259](https://www.ncbi.nlm.nih.gov/gene/197259) · UniProt [Q8NB16](https://www.uniprot.org/uniprotkb/Q8NB16) · Ensembl [ENSG00000168404](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168404)

## Data

Gene col 9645: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9645); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9645, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9645]; `tensor/DDL_lfc|DDL_z.npy` [9645]; `embed/gene_vectors.npy` [9645]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9645 or target_col == 9645). Every well: [[MLKL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MLKL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
