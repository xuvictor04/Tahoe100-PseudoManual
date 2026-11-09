---
symbol: "TNFRSF11A"
type: "gene"
col: 6562
ensembl_id: "ENSG00000141655"
name: "TNF receptor superfamily member 11a"
location: "18q21.33"
module: 154
arm: "+"
pooled_cpm: 27.94
n_lines_expressing: 41
n_dd_up: 7
n_dd_down: 46
n_dd_up_clean: 7
n_dd_down_clean: 37
in_vector_space: true
direction_upstream: 14
direction_downstream: 27
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# TNFRSF11A

*TNF receptor superfamily member 11a* — 18q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.52× (z +8.7, q 3e-15, up in 32 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 46 drug-doses (9 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.420× (z -12.2, q 2e-31, down in 31 of 37 measured lines) ⚠ toxic. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.498× (z -9.8, q 4e-20, down in 27 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPR160]] (+0.71, fdr 7e-06), [[GALNT12]] (+0.66, fdr 7e-06), [[ANKRD37]] (+0.65, fdr 1e-05); moves opposite to [[DNAJC11]] (-0.60, fdr 1e-05), [[HECTD1]] (-0.60, fdr 1e-05), [[ZMYND11]] (-0.58, fdr 3e-05).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[NR3C2]] → it (grade B ⚠); 27 go from it, the strongest it → [[SEMA4B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6562.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +8.7 | 3e-15 | 32/39 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.66×** | +7.5 | 3e-11 | 24/38 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.49×** | +5.8 | 1e-06 | 22/39 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +5.8 | 1e-06 | 18/39 (NCI-H2030, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.3 | 2e-05 | 16/39 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +4.3 | 0.001 | 18/39 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +3.9 | 0.009 | 16/39 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | 1.51× | +3.1 | 0.12 | 14/38 (NCI-H2347, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM |  | 1.34× | +3.1 | 0.12 | 7/39 (NCI-H1792, A498, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.23× | +3.1 | 0.12 | 3/39 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Fumaric acid (drug)]] 5 µM |  | 1.24× | +3.0 | 0.14 | 8/39 (LS 180, PANC-1, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 46 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6562.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.420×** | -12.2 | 2e-31 | 31/37 (A-172, SW1417, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.498×** | -9.8 | 4e-20 | 27/39 (A549, C32, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.552×** | -8.0 | 2e-13 | 18/30 (SW1417, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.581×** | -7.9 | 3e-13 | 24/33 (C32, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.577×** | -7.7 | 1e-12 | 20/28 (SW1417, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.617×** | -7.0 | 2e-10 | 27/38 (KATO III, A498, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.638×** | -6.3 | 2e-08 | 21/38 (BT-474, C32, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.652×** | -6.0 | 1e-07 | 25/38 (A549, A498, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.655×** | -5.9 | 2e-07 | 20/38 (A549, A498, …) | all doses, flat |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.697×** | -5.3 | 8e-06 | 18/39 (A-172, A549, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.688×** | -5.2 | 9e-06 | 18/38 (SK-MEL-2, C32, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.681×** | -5.2 | 1e-05 | 19/38 (A498, A549, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.706×** | -5.1 | 2e-05 | 16/38 (HT-29, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.710×** | -5.0 | 2e-05 | 20/39 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.721×** | -4.8 | 8e-05 | 19/39 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.717×** | -4.7 | 1e-04 | 16/39 (A498, A549, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **0.728×** | -4.6 | 1e-04 | 17/39 (A498, A549, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.736×** | -4.5 | 3e-04 | 15/39 (A549, A498, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.812×** | -4.3 | 6e-04 | 18/39 (NCI-H2347, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6562. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 69.7 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -22.3) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.132× (z -15.9) |
| [[A498 (line)]] | wt | 38.6 | 0 | 10 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 5 µM 0.265× (z -9.9) |
| [[C32 (line)]] | wt | 53.1 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0918× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.127× (z -14.7) |
| [[NCI-H2347 (line)]] | alt | 51.8 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -14.0) |
| [[CFPAC-1 (line)]] | alt | 73.8 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0872× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -12.1) |
| [[A-172 (line)]] | wt | 35.3 | 0 | 5 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0610× (z -15.7) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.0848× (z -13.8) |
| [[BT-474 (line)]] | alt | 31.7 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0724× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -10.7) |
| [[KATO III (line)]] | alt | 90.1 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -19.4) |
| [[NCI-H1792 (line)]] | alt | 88.8 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -10.6) |
| [[SW1417 (line)]] | alt | 38.5 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0410× (z -25.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 29.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.217× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 11.5 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +11.9) | [[Bosentan (hydrate) (drug)]] 5 µM 0.160× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 29.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.1000× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.220× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 32.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0561× (z -18.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 26.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -10.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 98.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -14.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 9.83 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.07× (z +9.4) | — |
| [[H4 (line)]] | wt | 15.6 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.0531× (z -10.6) |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 1 | — | [[Silodosin (drug)]] 0.05 µM 0.0647× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 20.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -8.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 14.8 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.146× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 8.42 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.99× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 36.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -11.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 13.0 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0778× (z -9.7) |
| [[A-427 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.72 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.91 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.46 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.48 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.87 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.80 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.72 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6562), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR160]] | +0.71 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[GALNT12]] | +0.66 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[ANKRD37]] | +0.65 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[SH3GL3]] | +0.63 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[KHDRBS3]] | +0.63 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[UBA6]] | +0.63 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[CIB1]] | +0.62 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[SPNS2]] | +0.62 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[TMEM51]] | +0.61 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[SLC9A7]] | +0.61 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[NDRG1]] | +0.60 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[WNT7B]] | +0.60 | +0.58 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC11]] | -0.60 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[HECTD1]] | -0.60 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[ZMYND11]] | -0.58 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[STXBP5]] | -0.57 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[COMT]] | -0.56 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[MRRF]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[NNMT]] | -0.54 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[ZFX]] | -0.54 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[UTP20]] | -0.53 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[ST7L]] | -0.53 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[MCPH1]] | -0.53 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[LINC00886]] | -0.52 | -0.47 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C2]] | B | NR3C2 activity raises TNFRSF11A's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 2.68× lower at baseline in the lines without NR3C2 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[NXPH4]] | B | NXPH4 activity lowers TNFRSF11A's level | lines that do not express NXPH4 (13) vs lines expressing it (37) | 2.18× higher at baseline in the lines without NXPH4 | 0.020 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent |
| [[GPRC5A]] | B | GPRC5A activity raises TNFRSF11A's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 2.08× lower at baseline in the lines without GPRC5A | 0.037 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[CDK18]] | B | CDK18 activity raises TNFRSF11A's level | lines that do not express CDK18 (9) vs lines expressing it (41) | 2.26× lower at baseline in the lines without CDK18 | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC00511, ABCG2, CYP2J2; maybe low, not absent |
| [[FA2H]] | B | FA2H activity raises TNFRSF11A's level | lines that do not express FA2H (27) vs lines expressing it (23) | 1.66× lower at baseline in the lines without FA2H | 0.052 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[F11R]] | B | F11R activity raises TNFRSF11A's level | lines that do not express F11R (10) vs lines expressing it (40) | 2.86× lower at baseline in the lines without F11R | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000287306, LONRF3, TUBA4A |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers TNFRSF11A's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers TNFRSF11A's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TFF1]] | B | TFF1 activity raises TNFRSF11A's level | lines that do not express TFF1 (31) vs lines expressing it (19) | 2.15× lower at baseline in the lines without TFF1 | 0.063 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC |
| [[SPNS2]] | B | SPNS2 activity raises TNFRSF11A's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 1.79× lower at baseline in the lines without SPNS2 | 0.071 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N |
| [[SLC17A7]] | B | SLC17A7 activity lowers TNFRSF11A's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 2.59× higher at baseline in the lines without SLC17A7 | 0.071 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |
| [[BACE2]] | B | BACE2 activity raises TNFRSF11A's level | lines that do not express BACE2 (10) vs lines expressing it (40) | 1.96× lower at baseline in the lines without BACE2 | 0.082 | ⚠ within organs, on part of the lines; also absent: FBXO32, STAT5A, ETS2 |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 27, C 0. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA4B]] | B | TNFRSF11A activity raises SEMA4B's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 2.30× lower at baseline in the lines without TNFRSF11A | 0.003 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[CLMN]] | B | TNFRSF11A activity raises CLMN's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 3.00× lower at baseline in the lines without TNFRSF11A | 0.003 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[F11R]] | B | TNFRSF11A activity raises F11R's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 3.17× lower at baseline in the lines without TNFRSF11A | 0.009 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[MCM3AP]] | B | TNFRSF11A activity lowers MCM3AP's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 1.37× higher at baseline in the lines without TNFRSF11A | 0.011 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[GPRC5A]] | B | TNFRSF11A activity raises GPRC5A's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 2.74× lower at baseline in the lines without TNFRSF11A | 0.016 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[GDPGP1]] | B | TNFRSF11A activity raises GDPGP1's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 1.67× lower at baseline in the lines without TNFRSF11A | 0.018 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[IL1RAP]] | B | TNFRSF11A activity raises IL1RAP's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 2.90× lower at baseline in the lines without TNFRSF11A | 0.019 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[RHPN2]] | B | TNFRSF11A activity raises RHPN2's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 1.91× lower at baseline in the lines without TNFRSF11A | 0.021 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[WNT7B]] | B | TNFRSF11A activity raises WNT7B's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 2.65× lower at baseline in the lines without TNFRSF11A | 0.022 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[CD47]] | B | TNFRSF11A activity raises CD47's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 1.42× lower at baseline in the lines without TNFRSF11A | 0.023 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[ZFX]] | B | TNFRSF11A activity lowers ZFX's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 1.37× higher at baseline in the lines without TNFRSF11A | 0.023 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[CIB1]] | B | TNFRSF11A activity raises CIB1's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 1.81× lower at baseline in the lines without TNFRSF11A | 0.024 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.786). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.4, -1.7); signed map (-3.4, 49.0). **Vector** length 123, 34.6% of its response variance represented; |z| ≥ 3 in 1,188 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.3 | +8.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.2 | +7.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.4 | +5.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.4 | +3.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.1 | +5.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.7 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +3.1 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +2.0 | +0.6 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.5 | -12.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -5.1 | -6.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.9 | -9.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.4 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.3 | -3.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.8 | -3.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.7 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | TNF receptor superfamily member 11a |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.33 — chr18:62,325,287-62,391,288 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RANK, CD265, FEO, ODFR, TRANCE-R; previously PDB2, LOH18CR1 |
| Gene groups (HGNC) | CD molecules; Tumor necrosis factor receptor superfamily |
| Reactome | 3 pathways, smallest: TNF receptor superfamily (TNFSF) members mediating non-canonical NF-kB pathway; TNFR2 non-canonical NF-kB pathway; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6Q6](https://www.uniprot.org/uniprotkb/Q9Y6Q6) (Tumor necrosis factor receptor superfamily member 11A):

> Receptor for TNFSF11/RANKL/TRANCE/OPGL; essential for RANKL-mediated osteoclastogenesis. Its interaction with EEIG1 promotes osteoclastogenesis via facilitating the transcription of NFATC1 and activation of PLCG2 (By similarity). Involved in the regulation of interactions between T-cells and dendritic cells (By similarity).

**Summary**, from NCBI Gene [8792](https://www.ncbi.nlm.nih.gov/gene/8792):

> The protein encoded by this gene is a member of the TNF-receptor superfamily. This receptors can interact with various TRAF family proteins, through which this receptor induces the activation of NF-kappa B and MAPK8/JNK. This receptor and its ligand are important regulators of the interaction between T cells and dendritic cells. This receptor is also an essential mediator for osteoclast and lymph node development. Mutations at this locus have been associated with familial expansile osteolysis, …

**Accessions** — [HGNC:11908](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11908) · Entrez [8792](https://www.ncbi.nlm.nih.gov/gene/8792) · UniProt [Q9Y6Q6](https://www.uniprot.org/uniprotkb/Q9Y6Q6) · Ensembl [ENSG00000141655](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141655)

## Data

Gene col 6562: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6562); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6562, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6562]; `tensor/DDL_lfc|DDL_z.npy` [6562]; `embed/gene_vectors.npy` [6562]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6562 or target_col == 6562). Every well: [[TNFRSF11A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFRSF11A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
