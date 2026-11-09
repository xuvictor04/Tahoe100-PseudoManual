---
symbol: "SH3TC1"
type: "gene"
col: 4585
ensembl_id: "ENSG00000125089"
name: "SH3 domain and tetratricopeptide repeats 1"
location: "4p16.1"
module: 98
arm: "+"
pooled_cpm: 10.86
n_lines_expressing: 40
n_dd_up: 25
n_dd_down: 19
n_dd_up_clean: 21
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 16
direction_downstream: 20
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# SH3TC1

*SH3 domain and tetratricopeptide repeats 1* — 4p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.05 µM: 2.87× (z +11.2, q 3e-26, up in 37 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.382× (z -14.9, q 0e+00, down in 34 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGPP2]] (+0.67, fdr 1e-05), [[MT1M]] (+0.60, fdr 1e-05), [[TLR2]] (+0.58, fdr 1e-05); moves opposite to [[EDIL3]] (-0.46, fdr 5e-05), [[STMP1]] (-0.46, fdr 4e-05), [[GJA1]] (-0.45, fdr 6e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[TRIM29]] → it (grade B ⚠); 20 go from it, the strongest it → [[KIF13B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4585.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.05 µM |  | **2.87×** | +11.2 | 3e-26 | 37/38 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **2.33×** | +9.3 | 4e-18 | 33/37 (HEC-1-A, SW1417, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.95×** | +7.1 | 3e-10 | 21/37 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.84×** | +6.7 | 3e-09 | 24/37 (HEC-1-A, LS 180, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.63×** | +5.4 | 9e-06 | 16/37 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.52×** | +4.6 | 3e-04 | 15/37 (AsPC-1, H4, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.34×** | +4.6 | 3e-04 | 16/37 (AsPC-1, Panc 03.27, …) | all doses, stronger at high dose | position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **1.47×** | +4.2 | 0.002 | 17/37 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | **1.46×** | +4.2 | 0.002 | 17/37 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.45×** | +4.1 | 0.002 | 16/37 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.014 | 17/36 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.015 | 11/36 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.47×** | +3.4 | 0.029 | 15/37 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.24×** | +3.4 | 0.029 | 13/38 (HEC-1-A, LS 180, …) | all doses, flat | low cells (technical?) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.23×** | +3.3 | 0.036 | 8/38 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.36×** | +3.2 | 0.054 | 12/36 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.42×** | +3.1 | 0.061 | 10/38 (CFPAC-1, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.061 | 6/38 (AsPC-1, NCI-H1792, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4585.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.382×** | -14.9 | 0e+00 | 34/37 (HT-29, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.353×** | -11.4 | 1e-27 | 24/29 (NCI-H2347, Hs 766T, …) | all doses, flat | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.398×** | -10.1 | 1e-21 | 33/37 (LoVo, SNU-423, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.429×** | -9.3 | 3e-18 | 30/37 (KATO III, HT-29, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.406×** | -9.1 | 1e-17 | 20/23 (HT-29, KATO III, …) | all doses, flat | composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.422×** | -9.1 | 1e-17 | 24/35 (RPMI-7951, KATO III, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.437×** | -8.7 | 3e-16 | 26/36 (Hs 766T, HT-29, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.440×** | -8.6 | 4e-16 | 14/18 (SW480, HT-29, …) | all doses, flat | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.456×** | -8.6 | 7e-16 | 29/37 (LoVo, KATO III, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.705×** | -5.4 | 4e-06 | 23/38 (Hs 766T, CFPAC-1, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.612×** | -5.1 | 1e-05 | 14/32 (LoVo, Hs 766T, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.626×** | -5.1 | 2e-05 | 17/37 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.642×** | -4.8 | 6e-05 | 17/36 (C32, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.900× | -4.2 | 0.001 | 9/38 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.694×** | -4.0 | 0.003 | 14/37 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.695×** | -3.7 | 0.009 | 11/37 (NCI-H1573, C32, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.740×** | -3.3 | 0.032 | 14/37 (CFPAC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.764×** | -2.9 | 0.100 | 12/37 (HS-578T, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4585. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 59.6 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -14.9) |
| [[HT-29 (line)]] | alt | 26.4 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.119× (z -17.6) |
| [[LoVo (line)]] | wt | 21.1 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0892× (z -16.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -13.1) |
| [[KATO III (line)]] | alt | 26.3 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0818× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -9.9) |
| [[H4 (line)]] | wt | 12.0 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -9.1) |
| [[HOP62 (line)]] | alt | 13.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 13.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0864× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0720× (z -10.0) |
| [[SW480 (line)]] | alt | 16.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0951× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 17.2 | 1 | 1 | [[Triamcinolone (drug)]] 5 µM 3.79× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -8.8) |
| [[C32 (line)]] | wt | 12.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0223× (z -15.7) |
| [[LS 180 (line)]] | wt | 15.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -8.7) |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 2 (2 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0660× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 30.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 7.02 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HepG2_C3A (line)]] | wt | 15.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 4.25 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0678× (z -8.5) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H1573 (line)]] | alt | 6.33 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 16.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0894× (z -15.2) |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 5.88 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0374× (z -12.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW1417 (line)]] | alt | 5.45 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.540 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.735 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.940 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.662 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.897 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.790 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.80 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4585), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGPP2]] | +0.67 | +0.56 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[MT1M]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[TLR2]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[FGD4]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[MAOA]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[MT1F]] | +0.58 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[FKBP5]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 | same gene group |
| [[SCNN1A]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[ARL4D]] | +0.56 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[CNKSR1]] | +0.56 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[BATF]] | +0.56 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[DUSP15]] | +0.56 | +0.41 / +0.61 | both halves | 4e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EDIL3]] | -0.46 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[STMP1]] | -0.46 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[GJA1]] | -0.45 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[FSTL1]] | -0.45 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[NHS]] | -0.43 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[FAM227A]] | -0.43 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[MTCL1]] | -0.43 | -0.34 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM29]] | B | TRIM29 activity raises SH3TC1's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 2.39× lower at baseline in the lines without TRIM29 | 0.010 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[TNS4]] | B | TNS4 activity raises SH3TC1's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 2.54× lower at baseline in the lines without TNS4 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[STK32A]] | B | STK32A activity raises SH3TC1's level | lines that do not express STK32A (23) vs lines expressing it (27) | 2.11× lower at baseline in the lines without STK32A | 0.012 | ⚠ within organs, on part of the lines; also absent: CHSY3, FRMPD4, SAA1 |
| [[BATF]] | B | BATF activity raises SH3TC1's level | lines that do not express BATF (33) vs lines expressing it (17) | 2.38× lower at baseline in the lines without BATF | 0.017 | ⚠ within organs, on part of the lines; also absent: KRT23, WFDC2, TACSTD2 |
| [[TOP2A]] | B | TOP2A activity raises SH3TC1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[S100P]] | B | S100P activity raises SH3TC1's level | lines that do not express S100P (34) vs lines expressing it (16) | 2.35× lower at baseline in the lines without S100P | 0.040 | ⚠ within organs, on part of the lines; also absent: POF1B, ENSG00000287426, CEACAM6 |
| [[FOXQ1]] | B | FOXQ1 activity raises SH3TC1's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 2.23× lower at baseline in the lines without FOXQ1 | 0.042 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |
| [[PPARG]] | B | PPARG activity raises SH3TC1's level | lines that do not express PPARG (20) vs lines expressing it (30) | 2.07× lower at baseline in the lines without PPARG | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[TLR2]] | B | TLR2 activity raises SH3TC1's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 1.82× lower at baseline in the lines without TLR2 | 0.045 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |
| [[NR3C1]] | B | NR3C1 activity raises SH3TC1's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[SGPP2]] | B | SGPP2 activity raises SH3TC1's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 2.02× lower at baseline in the lines without SGPP2 | 0.071 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[SAA1]] | B | SAA1 activity raises SH3TC1's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 1.84× lower at baseline in the lines without SAA1 | 0.075 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11 |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 20, C 0. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF13B]] | B | SH3TC1 activity raises KIF13B's level | lines that do not express SH3TC1 (10) vs lines expressing it (40) | 2.29× lower at baseline in the lines without SH3TC1 | 0.003 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[STK32A]] | B | SH3TC1 activity raises STK32A's level | lines that do not express SH3TC1 (10) vs lines expressing it (40) | 2.86× lower at baseline in the lines without SH3TC1 | 0.032 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[PCDH1]] | B | SH3TC1 activity raises PCDH1's level | lines that do not express SH3TC1 (10) vs lines expressing it (40) | 2.66× lower at baseline in the lines without SH3TC1 | 0.034 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[DUSP1]] | B | SH3TC1 activity raises DUSP1's level | lines that do not express SH3TC1 (10) vs lines expressing it (40) | 2.30× lower at baseline in the lines without SH3TC1 | 0.043 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[MTCL1]] | B | SH3TC1 activity lowers MTCL1's level | lines that do not express SH3TC1 (10) vs lines expressing it (40) | 1.90× higher at baseline in the lines without SH3TC1 | 0.046 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[TNS4]] | B | SH3TC1 activity raises TNS4's level | lines that do not express SH3TC1 (10) vs lines expressing it (40) | 3.28× lower at baseline in the lines without SH3TC1 | 0.052 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[SAA2]] | B | SH3TC1 activity raises SAA2's level | lines that do not express SH3TC1 (10) vs lines expressing it (40) | 3.13× lower at baseline in the lines without SH3TC1 | 0.063 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[SAA2-SAA4]] | B | SH3TC1 activity raises SAA2-SAA4's level | lines that do not express SH3TC1 (10) vs lines expressing it (40) | 2.77× lower at baseline in the lines without SH3TC1 | 0.065 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[ZC3H12A]] | B | SH3TC1 activity raises ZC3H12A's level | lines that do not express SH3TC1 (10) vs lines expressing it (40) | 2.43× lower at baseline in the lines without SH3TC1 | 0.070 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| cells under [[Trifluridine (drug)]] 5 µM | B | SH3TC1 activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express SH3TC1 (10) vs lines expressing it (38) | the lines without SH3TC1: 0.90× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[LPAR5]] | B | SH3TC1 activity raises LPAR5's level | lines that do not express SH3TC1 (10) vs lines expressing it (40) | 1.87× lower at baseline in the lines without SH3TC1 | 0.076 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[SCNN1A]] | B | SH3TC1 activity raises SCNN1A's level | lines that do not express SH3TC1 (10) vs lines expressing it (40) | 2.83× lower at baseline in the lines without SH3TC1 | 0.079 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.594). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.9, 14.6); signed map (16.1, 30.4). **Vector** length 105, 27.6% of its response variance represented; |z| ≥ 3 in 1,013 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.4 | +7.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +5.2 | +3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.6 | +1.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.4 | +6.7 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +4.4 | +11.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.0 | +3.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +4.0 | +4.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.9 | +3.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.8 | +4.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.8 | +9.3 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -5.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.2 | -9.1 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.2 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -2.7 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.7 | -0.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.6 | -1.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | SH3 domain and tetratricopeptide repeats 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.1 — chr4:8,182,072-8,241,803 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20356 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; SH3 domain containing |
| Matched by | ensembl_id |

UniProt [Q8TE82](https://www.uniprot.org/uniprotkb/Q8TE82) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26009](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26009) · Entrez [54436](https://www.ncbi.nlm.nih.gov/gene/54436) · UniProt [Q8TE82](https://www.uniprot.org/uniprotkb/Q8TE82) · Ensembl [ENSG00000125089](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125089)

## Data

Gene col 4585: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4585); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4585, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4585]; `tensor/DDL_lfc|DDL_z.npy` [4585]; `embed/gene_vectors.npy` [4585]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4585 or target_col == 4585). Every well: [[SH3TC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3TC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
