---
symbol: "DSG2"
type: "gene"
col: 503
ensembl_id: "ENSG00000046604"
name: "desmoglein 2"
location: "18q12.1"
module: 111
arm: "+"
pooled_cpm: 209.62
n_lines_expressing: 39
n_dd_up: 8
n_dd_down: 19
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 7
direction_downstream: 8
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# DSG2

*desmoglein 2* — 18q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.29× (z +13.2, q 5e-37, up in 37 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Sinomenine (drug)]] 0.5 µM: 1.29× (z +4.0, q 0.007, up in 28 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.314× (z -18.4, q 0e+00, down in 36 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DSC2]] (+0.69, fdr 7e-06), [[YWHAZ]] (+0.62, fdr 7e-06), [[SBDS]] (+0.61, fdr 3e-05); moves opposite to [[SEMA4C]] (-0.57, fdr 2e-05), [[CCDC107]] (-0.56, fdr 1e-04), [[TMEM258]] (-0.53, fdr 5e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[MYO5B]] → it (grade B ⚠); 8 go from it, the strongest it → [[DCTN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 503.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.29×** | +13.2 | 5e-37 | 37/38 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +11.6 | 1e-28 | 31/35 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +7.4 | 2e-11 | 31/36 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sinomenine (drug)]] 0.5 µM |  | **1.29×** | +4.0 | 0.007 | 28/37 (HOP62, HEC-1-A, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.020 | 20/37 (SW480, SW48, …) | two highest doses | low cells (technical?) |
| [[Imiquimod (maleate) (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.029 | 29/37 (SW480, J82, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.25×** | +3.6 | 0.029 | 19/37 (COLO 205, HT-29, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.25×** | +3.5 | 0.030 | 21/38 (LS 180, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 1.21× | +3.1 | 0.13 | 18/37 (COLO 205, KATO III, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.21× | +3.0 | 0.13 | 17/37 (COLO 205, HT-29, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 503.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.314×** | -18.4 | 0e+00 | 36/37 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.455×** | -17.7 | 0e+00 | 35/37 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.354×** | -16.5 | 0e+00 | 36/37 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.374×** | -15.6 | 0e+00 | 37/37 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.520×** | -10.4 | 4e-23 | 29/37 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.651×** | -9.6 | 6e-20 | 26/38 (LoVo, KATO III, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.631×** | -7.3 | 2e-11 | 32/37 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.642×** | -6.8 | 1e-09 | 28/37 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.649×** | -6.6 | 3e-09 | 31/38 (BT-474, SW 900, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.672×** | -6.3 | 2e-08 | 31/37 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.688×** | -5.9 | 2e-07 | 31/37 (NCI-H1792, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.708×** | -5.5 | 2e-06 | 30/37 (NCI-H1792, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.828×** | -4.2 | 0.001 | 24/37 (LoVo, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.792×** | -3.7 | 0.010 | 21/37 (NCI-H1792, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.793×** | -3.7 | 0.010 | 23/37 (NCI-H1792, SW480, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.660×** | -3.4 | 0.021 | 22/38 (AsPC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.693×** | -3.0 | 0.073 | 20/38 (KATO III, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 503. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 162 | 3 (3 ⚠) | 7 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -21.7) |
| [[SW480 (line)]] | alt | 101 | 2 (2 ⚠) | 8 | [[Dinaciclib (drug)]] 5 µM 2.13× (z +10.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.145× (z -26.5) |
| [[A-427 (line)]] | wt | 186 | 3 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 0.05 µM 2.67× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 585 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -21.5) |
| [[Hs 766T (line)]] | wt | 249 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -22.4) |
| [[NCI-H1573 (line)]] | alt | 208 | 1 (1 ⚠) | 7 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -23.0) |
| [[NCI-H460 (line)]] | wt | 127 | 2 (2 ⚠) | 6 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -20.1) |
| [[SW1417 (line)]] | alt | 221 | 3 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +12.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.324× (z -14.0) |
| [[A-172 (line)]] | wt | 241 | 1 (1 ⚠) | 6 | [[Trametinib (drug)]] 5 µM 1.96× (z +9.8) ⚠ cell-cycle shift, explains ~35% of this change | [[Panobinostat (drug)]] 5 µM 0.345× (z -14.4) |
| [[AsPC-1 (line)]] | alt | 832 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.118× (z -27.5) |
| [[KATO III (line)]] | alt | 386 | 1 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 5 µM 2.30× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -22.9) |
| [[LS 180 (line)]] | wt | 394 | 1 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 2.06× (z +8.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.174× (z -21.5) |
| [[NCI-H1792 (line)]] | alt | 153 | 1 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -14.9) |
| [[NCI-H2347 (line)]] | alt | 507 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -18.3) |
| [[Panc 03.27 (line)]] | alt | 862 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -20.9) |
| [[A549 (line)]] | wt | 135 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +14.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.292× (z -13.6) |
| [[COLO 205 (line)]] | alt | 171 | 2 (1 ⚠) | 4 | [[Peretinoin (drug)]] 5 µM 2.96× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -19.8) |
| [[H4 (line)]] | wt | 134 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -19.0) |
| [[HEC-1-A (line)]] | alt | 455 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -19.5) |
| [[HT-29 (line)]] | alt | 172 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.54× (z +9.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.227× (z -16.1) |
| [[J82 (line)]] | alt | 124 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +10.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.305× (z -13.7) |
| [[LoVo (line)]] | wt | 419 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.111× (z -26.7) |
| [[HCT15 (line)]] | alt | 283 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -20.0) |
| [[HepG2_C3A (line)]] | wt | 203 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.238× (z -15.3) |
| [[RKO (line)]] | wt | 145 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -19.6) |
| [[BT-474 (line)]] | alt | 188 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.256× (z -13.1) |
| [[NCI-H23 (line)]] | alt | 94.0 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +10.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.352× (z -9.9) |
| [[SW48 (line)]] | wt | 291 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.174× (z -18.7) |
| [[A498 (line)]] | wt | 157 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +12.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 60.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.287× (z -10.9) |
| [[C32 (line)]] | wt | 66.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 206 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.331× (z -11.9) |
| [[HS-578T (line)]] | alt | 55.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +10.0) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 123 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -9.2) |
| [[NCI-H596 (line)]] | alt | 159 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.0960× (z -8.9) |
| [[AN3 CA (line)]] | alt | 30.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 20.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.2 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.7 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 51.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 33.2 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 47.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 43.0 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 18.7 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 503), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DSC2]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 | same gene group; pathway: Formation of the cornified envelope; STRING 999 |
| [[YWHAZ]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 | pathway: Apoptosis |
| [[SBDS]] | +0.61 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[PERP]] | +0.61 | +0.59 / +0.60 | both halves | 7e-06 | pathway: Formation of the cornified envelope; STRING 717 |
| [[SPTAN1]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 | pathway: Apoptosis |
| [[ANXA2]] | +0.59 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[ARPP19]] | +0.59 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[ARPC5]] | +0.59 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[GOLM1]] | +0.58 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[ANXA1]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[NRAS]] | +0.55 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[IQGAP1]] | +0.55 | +0.59 / +0.59 | both halves | 7e-06 | pathway: RAC2 GTPase cycle; STRING 522 |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA4C]] | -0.57 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[CCDC107]] | -0.56 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[TMEM258]] | -0.53 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[SNHG9]] | -0.51 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[LSM7]] | -0.51 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[CDK10]] | -0.50 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[SNU13]] | -0.50 | -0.37 / -0.51 | both halves | 9e-05 |  |
| [[PPP1R35]] ⚠ | -0.50 | -0.47 / -0.44 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SELENOH]] | -0.50 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[TARS2]] | -0.49 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[ALYREF]] | -0.49 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[SIVA1]] | -0.49 | -0.24 / -0.59 | both halves | 5e-04 |  |
| [[SMPD4BP]] | -0.49 | -0.35 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO5B]] | B | MYO5B activity raises DSG2's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 3.55× lower at baseline in the lines without MYO5B | 0.001 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[DSC2]] | B | DSC2 activity raises DSG2's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 3.62× lower at baseline in the lines without DSC2 | 0.006 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |
| [[LMO7]] | B | LMO7 activity raises DSG2's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 3.50× lower at baseline in the lines without LMO7 | 0.007 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[TMEM30B]] | B | TMEM30B activity raises DSG2's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 3.48× lower at baseline in the lines without TMEM30B | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |
| [[CEACAM6]] | B | CEACAM6 activity raises DSG2's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 3.39× lower at baseline in the lines without CEACAM6 | 0.021 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17 |
| [[STON2]] | B | STON2 activity raises DSG2's level | lines that do not express STON2 (19) vs lines expressing it (31) | 2.00× lower at baseline in the lines without STON2 | 0.086 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| [[KRT8]] | C | KRT8 activity raises DSG2's level | lines that do not express KRT8 (13) vs lines expressing it (37) | 4.52× lower at baseline in the lines without KRT8 | 0.059 | ⚠ within organs, on part of the lines; also absent: KRT18, PKP2, CHMP4C; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCTN1]] | B | DSG2 activity lowers DCTN1's level | lines that do not express DSG2 (11) vs lines expressing it (39) | 1.35× higher at baseline in the lines without DSG2 | 0.026 | ⚠ within organs, on part of the lines; also absent: KITLG, COBLL1, ETS2 |
| [[VCPKMT]] | B | DSG2 activity lowers VCPKMT's level | lines that do not express DSG2 (11) vs lines expressing it (39) | 1.14× higher at baseline in the lines without DSG2 | 0.038 | ⚠ within organs, on part of the lines; also absent: KITLG, COBLL1, ETS2 |
| [[MAPRE1]] | B | DSG2 activity lowers MAPRE1's level | lines that do not express DSG2 (11) vs lines expressing it (39) | 1.18× higher at baseline in the lines without DSG2 | 0.064 | ⚠ within organs, on part of the lines; also absent: KITLG, COBLL1, ETS2 |
| [[DSC2]] | B | DSG2 activity raises DSC2's level | lines that do not express DSG2 (11) vs lines expressing it (39) | 4.80× lower at baseline in the lines without DSG2 | 0.067 | ⚠ within organs, on part of the lines; also absent: KITLG, COBLL1, ETS2 |
| [[DSP]] | B | DSG2 activity raises DSP's level | lines that do not express DSG2 (11) vs lines expressing it (39) | 4.47× lower at baseline in the lines without DSG2 | 0.068 | ⚠ within organs, on part of the lines; also absent: KITLG, COBLL1, ETS2 |
| [[DYNC1H1]] | B | DSG2 activity lowers DYNC1H1's level | lines that do not express DSG2 (11) vs lines expressing it (39) | 1.29× higher at baseline in the lines without DSG2 | 0.084 | ⚠ within organs, on part of the lines; also absent: KITLG, COBLL1, ETS2 |
| [[STON2]] | B | DSG2 activity raises STON2's level | lines that do not express DSG2 (11) vs lines expressing it (39) | 2.73× lower at baseline in the lines without DSG2 | 0.093 | ⚠ within organs, on part of the lines; also absent: KITLG, COBLL1, ETS2 |
| [[DSC3]] | B | DSG2 activity raises DSC3's level | lines that do not express DSG2 (11) vs lines expressing it (39) | 2.57× lower at baseline in the lines without DSG2 | 0.094 | ⚠ within organs, on part of the lines; also absent: KITLG, COBLL1, ETS2 |

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.9, -18.1); signed map (-10.0, 33.6). **Vector** length 108, 34.6% of its response variance represented; |z| ≥ 3 in 1,074 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *RHOV GTPase cycle* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.0 | +11.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +1.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.1 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.0 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.5 | +3.8 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.1 | +1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.9 | +2.3 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -3.5 | -2.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.5 | -5.9 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -2.8 | -2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.5 | -6.6 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.4 | -0.8 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -2.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | desmoglein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.1 — chr18:31,497,624-31,551,351 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CDHF5 |
| Gene groups (HGNC) | Desmosomal cadherins |
| Reactome | 13 pathways, smallest: Apoptotic cleavage of cell adhesion  proteins; Apoptotic cleavage of cellular proteins; Formation of the cornified envelope |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14126](https://www.uniprot.org/uniprotkb/Q14126) (Desmoglein-2):

> A component of desmosome cell-cell junctions which are required for positive regulation of cellular adhesion. Involved in the interaction of plaque proteins and intermediate filaments mediating cell-cell adhesion. Required for proliferation and viability of embryonic stem cells in the blastocyst, thereby crucial for progression of post-implantation embryonic development (By similarity). Maintains pluripotency by regulating epithelial to mesenchymal transition/mesenchymal to epithelial …

**Summary**, from NCBI Gene [1829](https://www.ncbi.nlm.nih.gov/gene/1829):

> This gene encodes a member of the desmoglein family and cadherin cell adhesion molecule superfamily of proteins. Desmogleins are calcium-binding transmembrane glycoprotein components of desmosomes, cell-cell junctions between epithelial, myocardial, and other cell types. The encoded preproprotein is proteolytically processed to generate the mature glycoprotein. This gene is present in a gene cluster with other desmoglein gene family members on chromosome 18. Mutations in this gene have been …

**Accessions** — [HGNC:3049](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3049) · Entrez [1829](https://www.ncbi.nlm.nih.gov/gene/1829) · UniProt [Q14126](https://www.uniprot.org/uniprotkb/Q14126) · Ensembl [ENSG00000046604](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000046604)

## Data

Gene col 503: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 503); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 503, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 503]; `tensor/DDL_lfc|DDL_z.npy` [503]; `embed/gene_vectors.npy` [503]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 503 or target_col == 503). Every well: [[DSG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DSG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
