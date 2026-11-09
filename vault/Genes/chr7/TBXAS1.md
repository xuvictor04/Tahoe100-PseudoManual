---
symbol: "TBXAS1"
type: "gene"
col: 672
ensembl_id: "ENSG00000059377"
name: "thromboxane A synthase 1"
location: "7q34"
module: 98
arm: "+"
pooled_cpm: 10.32
n_lines_expressing: 42
n_dd_up: 24
n_dd_down: 17
n_dd_up_clean: 18
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 11
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# TBXAS1

*thromboxane A synthase 1* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.79× (z +22.8, q 0e+00, up in 29 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.544× (z -7.3, q 1e-10, down in 22 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STXBP5-AS1]] (+0.73, fdr 7e-06), [[TOP1]] (+0.65, fdr 7e-06), [[B3GNT5]] (+0.63, fdr 1e-05); moves opposite to [[TTBK2]] (-0.50, fdr 9e-05), [[ZNF624]] (-0.49, fdr 5e-05), [[OPTN]] (-0.49, fdr 3e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC02405]] → it (grade B ⚠); 11 go from it, the strongest it → [[HIPK2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 672.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.79×** | +22.8 | 0e+00 | 29/36 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.62×** | +11.2 | 9e-27 | 15/19 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.23×** | +9.7 | 4e-20 | 24/38 (HEC-1-A, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.20×** | +9.5 | 2e-19 | 14/27 (A498, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.31×** | +9.4 | 8e-19 | 9/20 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.86×** | +7.5 | 5e-12 | 20/36 (A498, HS-578T, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +7.1 | 1e-10 | 19/39 (A498, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.83×** | +7.1 | 1e-10 | 18/36 (C32, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.74×** | +6.4 | 8e-09 | 17/33 (A-172, SNU-423, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.64×** | +6.0 | 1e-07 | 18/37 (HS-578T, hTERT-HPNE, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +5.7 | 8e-07 | 15/38 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +5.5 | 2e-06 | 11/39 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.6 | 2e-04 | 17/39 (A498, HS-578T, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.42×** | +4.3 | 8e-04 | 15/38 (HS-578T, A-172, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.38×** | +3.9 | 0.003 | 13/39 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.39×** | +3.7 | 0.008 | 15/36 (A-172, H4, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.018 | 10/38 (HS-578T, NCI-H1792, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.021 | 13/37 (HS-578T, A-172, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.024 | 17/39 (A-172, HS-578T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.041 | 15/39 (HS-578T, A-172, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 672.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.544×** | -7.3 | 1e-10 | 22/39 (SW 900, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.684×** | -6.5 | 3e-08 | 20/36 (SW 900, HT-29, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.576×** | -6.4 | 3e-08 | 20/38 (H4, LS 180, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.591×** | -6.3 | 3e-08 | 22/39 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.602×** | -6.1 | 1e-07 | 20/36 (H4, LS 180, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.633×** | -5.5 | 3e-06 | 20/38 (LS 180, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.650×** | -5.2 | 2e-05 | 18/38 (H4, LS 180, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.781×** | -4.2 | 0.002 | 15/38 (LS 180, CFPAC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.725×** | -3.9 | 0.007 | 15/39 (HT-29, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.722×** | -3.7 | 0.012 | 12/40 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.744×** | -3.6 | 0.020 | 20/39 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.747×** | -3.5 | 0.021 | 15/33 (LOX-IMVI, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.814×** | -3.5 | 0.021 | 9/39 (SW480, C-33 A, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.758×** | -3.3 | 0.035 | 14/38 (HepG2/C3A, SW480, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.759×** | -3.3 | 0.035 | 10/39 (A498, SK-MEL-2, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.797×** | -3.1 | 0.058 | 10/37 (HT-29, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Tadalafil (drug)]] 5 µM |  | **0.763×** | -3.1 | 0.058 | 6/37 (NCI-H2347, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 672. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 39.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -16.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0889× (z -14.4) |
| [[LS 180 (line)]] | wt | 26.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -16.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 9.01 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.0741× (z -12.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 22.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0718× (z -17.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0459× (z -14.7) |
| [[SW480 (line)]] | alt | 6.74 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +10.5) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0961× (z -12.4) |
| [[A498 (line)]] | wt | 32.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +8.6) | — |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 2 (1 ⚠) | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0672× (z -9.0) |
| [[H4 (line)]] | wt | 26.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0420× (z -13.6) |
| [[HOP62 (line)]] | alt | 11.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.157× (z -9.1) |
| [[LoVo (line)]] | wt | 5.59 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.61× (z +11.1) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0317× (z -15.9) |
| [[A-172 (line)]] | wt | 5.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.78× (z +9.9) | — |
| [[A549 (line)]] | wt | 14.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -11.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[C32 (line)]] | wt | 5.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 38.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -15.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HEC-1-A (line)]] | alt | 6.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +11.1) | — |
| [[KATO III (line)]] | alt | 6.31 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0767× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 2.70 | 0 | 1 | — | [[Asciminib (drug)]] 5 µM 0.0502× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 7.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 4.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.66× (z +9.4) | — |
| [[A-427 (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 672), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STXBP5-AS1]] | +0.73 | +0.64 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[TOP1]] | +0.65 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[B3GNT5]] | +0.63 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[TMEM164]] | +0.62 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[ITGA10]] | +0.60 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[HIPK2]] | +0.59 | +0.63 / +0.50 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ELOVL6]] | +0.59 | +0.44 / +0.60 | both halves | 3e-05 | pathway: Fatty acid metabolism |
| [[PTPRG]] | +0.58 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[SH3RF3]] | +0.57 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[TRABD2A]] | +0.56 | +0.39 / +0.60 | both halves | 6e-05 |  |
| [[ADAMTS9]] | +0.56 | +0.56 / +0.50 | both halves | 1e-05 | pathway: Diseases of metabolism |
| [[LINC00607]] | +0.55 | +0.39 / +0.49 | both halves | 6e-05 |  |
| [[LAMB1]] | +0.54 | +0.46 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTBK2]] | -0.50 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[ZNF624]] | -0.49 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[OPTN]] | -0.49 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[ZCRB1]] | -0.49 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[HSDL1]] | -0.48 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[CYRIA]] | -0.48 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[CCDC127]] | -0.48 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[GPRC5B]] | -0.48 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[ZSCAN16]] | -0.47 | -0.25 / -0.49 | both halves | 4e-04 |  |
| [[TUBB2B]] | -0.46 | -0.28 / -0.37 | both halves | 3e-04 |  |
| [[SAT2]] | -0.46 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[NUB1]] | -0.46 | -0.44 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02405]] | B | LINC02405 activity raises TBXAS1's level | lines that do not express LINC02405 (27) vs lines expressing it (23) | 1.99× lower at baseline in the lines without LINC02405 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000286016, ENSG00000278266, LINC02360 |
| [[TOP2A]] | B | TOP2A activity lowers TBXAS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NRP1]] | B | NRP1 activity raises TBXAS1's level | lines that do not express NRP1 (16) vs lines expressing it (34) | 2.04× lower at baseline in the lines without NRP1 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: BDKRB2, MX2, FAM107B |
| [[HIPK2]] | B | HIPK2 activity raises TBXAS1's level | lines that do not express HIPK2 (5) vs lines expressing it (45) | 2.86× lower at baseline in the lines without HIPK2 | 0.066 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HIPK2]] | B | TBXAS1 activity raises HIPK2's level | lines that do not express TBXAS1 (8) vs lines expressing it (42) | 3.24× lower at baseline in the lines without TBXAS1 | 0.004 | ⚠ within organs, on part of the lines; also absent: OSBPL7, PYROXD2, SESTD1; maybe low, not absent |
| [[ABLIM3]] | B | TBXAS1 activity raises ABLIM3's level | lines that do not express TBXAS1 (8) vs lines expressing it (42) | 2.54× lower at baseline in the lines without TBXAS1 | 0.033 | ⚠ within organs, on part of the lines; also absent: OSBPL7, PYROXD2, SESTD1; maybe low, not absent |
| [[FAH]] | B | TBXAS1 activity raises FAH's level | lines that do not express TBXAS1 (8) vs lines expressing it (42) | 1.38× lower at baseline in the lines without TBXAS1 | 0.046 | ⚠ within organs, on part of the lines; also absent: OSBPL7, PYROXD2, SESTD1; maybe low, not absent |
| [[ACOT7]] | B | TBXAS1 activity lowers ACOT7's level | lines that do not express TBXAS1 (8) vs lines expressing it (42) | 1.74× higher at baseline in the lines without TBXAS1 | 0.049 | ⚠ within organs, on part of the lines; also absent: OSBPL7, PYROXD2, SESTD1; maybe low, not absent |
| [[GPX4]] | B | TBXAS1 activity lowers GPX4's level | lines that do not express TBXAS1 (8) vs lines expressing it (42) | 1.57× higher at baseline in the lines without TBXAS1 | 0.065 | ⚠ within organs, on part of the lines; also absent: OSBPL7, PYROXD2, SESTD1; maybe low, not absent |
| [[LINC01950]] | B | TBXAS1 activity raises LINC01950's level | lines that do not express TBXAS1 (8) vs lines expressing it (42) | 1.57× lower at baseline in the lines without TBXAS1 | 0.078 | ⚠ within organs, on part of the lines; also absent: OSBPL7, PYROXD2, SESTD1; maybe low, not absent |
| [[PIGW]] | B | TBXAS1 activity lowers PIGW's level | lines that do not express TBXAS1 (8) vs lines expressing it (42) | 1.20× higher at baseline in the lines without TBXAS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: OSBPL7, PYROXD2, SESTD1; maybe low, not absent |
| [[NPR3]] | B | TBXAS1 activity raises NPR3's level | lines that do not express TBXAS1 (8) vs lines expressing it (42) | 1.74× lower at baseline in the lines without TBXAS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: OSBPL7, PYROXD2, SESTD1; maybe low, not absent |
| [[LINC02405]] | B | TBXAS1 activity raises LINC02405's level | lines that do not express TBXAS1 (8) vs lines expressing it (42) | 3.28× lower at baseline in the lines without TBXAS1 | 0.096 | ⚠ within organs, on part of the lines; also absent: OSBPL7, PYROXD2, SESTD1; maybe low, not absent |
| [[NRP1]] | B | TBXAS1 activity raises NRP1's level | lines that do not express TBXAS1 (8) vs lines expressing it (42) | 2.51× lower at baseline in the lines without TBXAS1 | 0.098 | ⚠ within organs, on part of the lines; also absent: OSBPL7, PYROXD2, SESTD1; maybe low, not absent |
| [[HIPK2]] | C | TBXAS1 activity strengthens HIPK2's drug response | lines that do not express TBXAS1 (4) vs lines expressing it (41) | the lines without TBXAS1 respond 0.57× as strongly (z diff +2.94); strongest at Topotecan (hydrochloride) 5 µM: 0.97x vs 0.59x (z diff +5.7) | 0.020 | ⚠ within organs, on part of the lines; also absent: OSBPL7, PYROXD2, SESTD1; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.574). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.8, 14.9); signed map (17.1, 33.6). **Vector** length 88.8, 19.0% of its response variance represented; |z| ≥ 3 in 1,065 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +22.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.6 | +9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.1 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +9.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.9 | +7.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.0 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +5.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.0 | +0.9 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.4 | -3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.5 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | thromboxane A synthase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:139,777,051-140,020,325 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CYP5, CYP5A1, THAS, TXS, TXAS, TS |
| Gene groups (HGNC) | Cytochrome P450 family 5; Hydroperoxy icosatetraenoate dehydratases |
| Reactome | 10 pathways, smallest: Eicosanoids; Synthesis of Prostaglandins (PG) and Thromboxanes (TX); Metabolic disorders of biological oxidation enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [P24557](https://www.uniprot.org/uniprotkb/P24557) (Thromboxane-A synthase):

> Catalyzes the conversion of prostaglandin H2 (PGH2) to thromboxane A2 (TXA2), a potent inducer of blood vessel constriction and platelet aggregation. Also cleaves PGH2 to 12-hydroxy-heptadecatrienoicacid (12-HHT) and malondialdehyde, which is known to act as a mediator of DNA damage. 12-HHT and malondialdehyde are formed stoichiometrically in the same amounts as TXA2. Additionally, displays dehydratase activity, toward (15S)-hydroperoxy-(5Z,8Z,11Z,13E)-eicosatetraenoate (15(S)-HPETE) producing …

**Summary**, from NCBI Gene [6916](https://www.ncbi.nlm.nih.gov/gene/6916):

> This gene encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. However, this protein is considered a member of the cytochrome P450 superfamily on the basis of sequence similarity rather than functional similarity. This endoplasmic reticulum membrane protein catalyzes the conversion of prostglandin H2 to thromboxane A2, a …

**Accessions** — [HGNC:11609](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11609) · Entrez [6916](https://www.ncbi.nlm.nih.gov/gene/6916) · UniProt [P24557](https://www.uniprot.org/uniprotkb/P24557) · Ensembl [ENSG00000059377](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000059377)

## Data

Gene col 672: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 672); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 672, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 672]; `tensor/DDL_lfc|DDL_z.npy` [672]; `embed/gene_vectors.npy` [672]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 672 or target_col == 672). Every well: [[TBXAS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBXAS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
