---
symbol: "ARMC1"
type: "gene"
col: 2462
ensembl_id: "ENSG00000104442"
name: "armadillo repeat containing 1"
location: "8q13.1"
module: 17
arm: "+"
pooled_cpm: 43.45
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 11
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ARMC1

*armadillo repeat containing 1* — 8q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.09× (z +17.0, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.642× (z -10.2, q 8e-22, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GEMIN2]] (+0.66, fdr 1e-05), [[TRAPPC11]] (+0.65, fdr 7e-06), [[ZYG11B]] (+0.65, fdr 1e-05); moves opposite to [[ITGA7]] (-0.54, fdr 3e-05), [[LHX4]] (-0.54, fdr 4e-05), [[CELF6]] (-0.53, fdr 6e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EBF4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2462.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.09×** | +17.0 | 0e+00 | 46/48 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.06×** | +16.7 | 0e+00 | 44/48 (A498, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.95×** | +15.4 | 0e+00 | 44/48 (A498, HS-578T, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +10.4 | 3e-23 | 32/48 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.52×** | +9.3 | 1e-18 | 23/38 (Panc 03.27, PANC-1, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.47×** | +8.7 | 4e-16 | 32/48 (HS-578T, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +8.0 | 9e-14 | 34/48 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.24×** | +7.1 | 1e-10 | 26/48 (HS-578T, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +7.1 | 1e-10 | 33/48 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **1.37×** | +7.1 | 1e-10 | 26/47 (HS-578T, C-33 A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change | **1.31×** | +6.2 | 3e-08 | 27/48 (A498, C-33 A, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +6.1 | 4e-08 | 31/48 (A549, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +5.2 | 8e-06 | 18/48 (RKO, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.24×** | +5.0 | 3e-05 | 18/48 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Furosemide (drug)]] 0.5 µM |  | **1.23×** | +4.7 | 8e-05 | 20/48 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.22×** | +4.6 | 1e-04 | 20/48 (J82, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +4.4 | 3e-04 | 15/48 (HOP62, KATO III, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.22×** | +4.3 | 5e-04 | 17/47 (HOP62, A-427, …) | all doses, flat | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +4.2 | 7e-04 | 13/48 (AsPC-1, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.013 | 10/48 (HOP62, PANC-1, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 1.17× | +3.4 | 0.014 | 8/48 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.16× | +3.3 | 0.017 | 13/48 (NCI-H23, LOX-IMVI, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 1.10× | +3.1 | 0.035 | 6/48 (A549, hTERT-HPNE, …) | top dose only |  |
| [[Sonidegib (drug)]] 0.5 µM |  | 1.19× | +2.9 | 0.066 | 5/48 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2462.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.642×** | -10.2 | 8e-22 | 38/48 (SW 1271, SHP-77, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.661×** | -9.6 | 4e-19 | 32/48 (AsPC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.667×** | -9.4 | 2e-18 | 31/47 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.758×** | -6.4 | 2e-08 | 31/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.776×** | -5.9 | 5e-07 | 24/48 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.777×** | -5.8 | 6e-07 | 27/48 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.632×** | -5.5 | 2e-06 | 23/49 (SHP-77, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.664×** | -4.9 | 5e-05 | 22/48 (RPMI-7951, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.810×** | -4.6 | 3e-04 | 20/48 (SW48, A498, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.831×** | -4.1 | 0.002 | 18/47 (NCI-H460, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.851× | -3.7 | 0.010 | 20/48 (HCT15, KATO III, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.760×** | -3.3 | 0.043 | 14/48 (CFPAC-1, hTERT-HPNE, …) | top dose only | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2462. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 46.1 | 4 (2 ⚠) | 4 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.07× (z +9.8) | [[Digitoxin (drug)]] 5 µM 0.414× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.443× (z -11.0) |
| [[HS-578T (line)]] | alt | 56.4 | 6 (4 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.91× (z +12.8) | — |
| [[A498 (line)]] | wt | 76.8 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.62× (z +12.8) | — |
| [[HOP62 (line)]] | alt | 53.7 | 4 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +10.5) | — |
| [[A549 (line)]] | wt | 38.4 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.95× (z +11.0) | — |
| [[AsPC-1 (line)]] | alt | 25.5 | 2 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 3.18× (z +9.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.351× (z -8.5) |
| [[SHP-77 (line)]] | alt | 58.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.401× (z -8.6) |
| [[A-427 (line)]] | wt | 56.2 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.243× (z -20.5) |
| [[BT-474 (line)]] | alt | 37.9 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.86× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 37.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.299× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 31.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.250× (z -8.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 41.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.37× (z +8.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LS 180 (line)]] | wt | 42.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.392× (z -8.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 50.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[SW 1271 (line)]] | alt | 61.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0441× (z -12.2) |
| [[SW48 (line)]] | wt | 32.0 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.174× (z -9.4) |
| [[A-172 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2462), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GEMIN2]] | +0.66 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[TRAPPC11]] | +0.65 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[ZYG11B]] | +0.65 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[CEPT1]] | +0.62 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[SUPT20H]] | +0.61 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[NIPSNAP2]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[NUP37]] | +0.59 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[NEDD1]] | +0.58 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[ELP3]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[ACTL6A]] | +0.58 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[FAM220A]] | +0.57 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[RAD17]] | +0.56 | +0.52 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA7]] | -0.54 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[LHX4]] | -0.54 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[CELF6]] | -0.53 | -0.22 / -0.57 | both halves | 6e-04 |  |
| [[LINC01033]] | -0.53 | -0.23 / -0.51 | both halves | 5e-04 |  |
| [[DNAJB6]] | -0.52 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[SARM1]] | -0.52 | -0.27 / -0.53 | both halves | 3e-04 |  |
| [[SFXN5]] | -0.51 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[MYO1F]] | -0.51 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[ZBTB46]] | -0.51 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[SLC8A2]] | -0.50 | -0.24 / -0.52 | both halves | 5e-04 |  |
| [[IL3RA]] | -0.50 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[SEC1P]] | -0.50 | -0.21 / -0.50 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EBF4]] | B | EBF4 activity raises ARMC1's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 1.24× lower at baseline in the lines without EBF4 | 0.015 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.469). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.8, -2.0); signed map (-21.0, -13.7). **Vector** length 82.8, 18.2% of its response variance represented; |z| ≥ 3 in 1,072 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.6 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +8.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +4.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +2.1 | +15.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.8 | +1.0 |
|  | [[Bexarotene (drug)]] 5 µM |  | +1.8 | +0.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +2.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.1 | -10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.6 | -0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -0.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -1.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.7 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | +0.8 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -2.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | armadillo repeat containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q13.1 — chr8:65,602,458-65,634,217 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10511, Arcp |
| Gene groups (HGNC) | Armadillo repeat containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVT9](https://www.uniprot.org/uniprotkb/Q9NVT9) (Armadillo repeat-containing protein 1):

> In association with mitochondrial contact site and cristae organizing system (MICOS) complex components and mitochondrial outer membrane sorting assembly machinery (SAM) complex components may regulate mitochondrial dynamics playing a role in determining mitochondrial length, distribution and motility.

**Summary**, from NCBI Gene [55156](https://www.ncbi.nlm.nih.gov/gene/55156):

> Predicted to enable metal ion binding activity. Involved in intracellular distribution of mitochondria. Located in cytosol and mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17684](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17684) · Entrez [55156](https://www.ncbi.nlm.nih.gov/gene/55156) · UniProt [Q9NVT9](https://www.uniprot.org/uniprotkb/Q9NVT9) · Ensembl [ENSG00000104442](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104442)

## Data

Gene col 2462: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2462); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2462, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2462]; `tensor/DDL_lfc|DDL_z.npy` [2462]; `embed/gene_vectors.npy` [2462]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2462 or target_col == 2462). Every well: [[ARMC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARMC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
