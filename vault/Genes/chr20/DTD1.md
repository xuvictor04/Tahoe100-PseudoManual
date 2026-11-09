---
symbol: "DTD1"
type: "gene"
col: 4668
ensembl_id: "ENSG00000125821"
name: "D-aminoacyl-tRNA deacylase 1"
location: "20p11.23"
module: 63
arm: "+"
pooled_cpm: 49.78
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 20
n_dd_up_clean: 3
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# DTD1

*D-aminoacyl-tRNA deacylase 1* — 20p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.66× (z +13.1, q 2e-36, up in 38 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[5-Azacytidine (drug)]] 5 µM: 1.35× (z +7.8, q 1e-12, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.423× (z -22.3, q 0e+00, down in 45 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.551× (z -21.9, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELMOD2]] (+0.63, fdr 1e-05), [[ZDHHC21]] (+0.62, fdr 1e-05), [[ATP13A2]] (+0.60, fdr 2e-05); moves opposite to [[C2]] (-0.59, fdr 7e-05), [[MEIS2]] (-0.57, fdr 3e-05), [[GPRC5C]] (-0.56, fdr 2e-04).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4668.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.66×** | +13.1 | 2e-36 | 38/47 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +10.1 | 2e-21 | 29/40 (A549, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +9.8 | 3e-20 | 30/44 (A498, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.35×** | +7.8 | 1e-12 | 29/47 (CFPAC-1, HEC-1-A, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.19× | +6.3 | 4e-08 | 19/47 (HEC-1-A, SNU-1, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +5.9 | 4e-07 | 12/47 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +5.7 | 8e-07 | 15/47 (COLO 205, BT-474, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +5.6 | 2e-06 | 20/47 (SNU-423, COLO 205, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +4.9 | 5e-05 | 17/47 (SW480, A498, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.19× | +4.5 | 4e-04 | 17/47 (LoVo, hTERT-HPNE, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.18× | +4.2 | 0.001 | 15/47 (HEC-1-A, RKO, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | 1.18× | +4.2 | 0.001 | 18/47 (NCI-H460, hTERT-HPNE, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.17× | +4.1 | 0.002 | 16/47 (BT-474, COLO 205, …) | rises with dose |  |
| [[Belumosudil (mesylate) (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.011 | 9/47 (RPMI-7951, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.14× | +3.5 | 0.020 | 12/46 (LS 180, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.13× | +3.1 | 0.069 | 8/47 (LS 180, NCI-H460, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.08× | +2.9 | 0.097 | 7/48 (SNU-1, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4668.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.423×** | -22.3 | 0e+00 | 45/47 (PANC-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.551×** | -21.9 | 0e+00 | 44/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.463×** | -20.0 | 0e+00 | 43/47 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.607×** | -18.3 | 0e+00 | 36/47 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.538×** | -16.1 | 0e+00 | 39/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.590×** | -13.1 | 2e-37 | 40/47 (HS-578T, PANC-1, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.626×** | -12.1 | 5e-32 | 35/47 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.624×** | -11.8 | 4e-30 | 39/47 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.725×** | -8.0 | 6e-14 | 35/47 (SK-MEL-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.816×** | -7.5 | 5e-12 | 28/47 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.577×** | -7.5 | 5e-12 | 25/47 (RPMI-7951, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.752×** | -7.0 | 1e-10 | 30/46 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.774×** | -6.7 | 1e-09 | 26/47 (HOP62, HS-578T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.806×** | -5.6 | 8e-07 | 23/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.813×** | -5.4 | 3e-06 | 21/47 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.705×** | -4.7 | 8e-05 | 20/46 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.872× | -3.6 | 0.010 | 19/47 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4668. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 44.7 | 1 (1 ⚠) | 12 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.96× (z +8.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -17.1) |
| [[PANC-1 (line)]] | alt | 38.4 | 0 | 11 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -19.8) |
| [[HS-578T (line)]] | alt | 78.4 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -16.6) |
| [[HOP62 (line)]] | alt | 38.4 | 0 | 8 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.324× (z -12.1) |
| [[SNU-1 (line)]] | wt | 91.3 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -15.2) |
| [[SW480 (line)]] | alt | 47.3 | 1 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +12.1) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.306× (z -15.6) |
| [[BT-474 (line)]] | alt | 39.7 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.228× (z -12.0) |
| [[HT-29 (line)]] | alt | 42.1 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -12.7) |
| [[A549 (line)]] | wt | 83.0 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.75× (z +12.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -13.0) |
| [[SHP-77 (line)]] | alt | 105 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.301× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -11.0) |
| [[SNU-423 (line)]] | alt | 63.1 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.48× (z +9.3) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.336× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.470× (z -11.8) |
| [[LoVo (line)]] | wt | 32.7 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.239× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.281× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 62.1 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -13.7) |
| [[LS 180 (line)]] | wt | 58.4 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -18.9) |
| [[A498 (line)]] | wt | 52.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +11.4) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 82.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -11.5) |
| [[J82 (line)]] | alt | 44.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -13.7) |
| [[MIA PaCa-2 (line)]] | alt | 78.4 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -13.8) |
| [[RKO (line)]] | wt | 78.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -13.8) |
| [[SW1417 (line)]] | alt | 32.2 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.228× (z -12.9) |
| [[SW48 (line)]] | wt | 70.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.111× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.186× (z -12.9) |
| [[AN3 CA (line)]] | alt | 74.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -8.5) |
| [[C-33 A (line)]] | alt | 39.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.189× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.307× (z -8.5) |
| [[C32 (line)]] | wt | 38.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 48.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -9.3) |
| [[H4 (line)]] | wt | 57.1 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.290× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 44.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.390× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.539× (z -8.9) |
| [[A-172 (line)]] | wt | 79.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -11.0) |
| [[A-427 (line)]] | wt | 42.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.49× (z +9.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 59.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -13.3) |
| [[HepG2_C3A (line)]] | wt | 72.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 45.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.485× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 41.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 89.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -13.4) |
| [[SK-MEL-2 (line)]] | alt | 61.8 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -13.6) |
| [[SW 900 (line)]] | alt | 30.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.320× (z -8.5) |
| [[CHP-212 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.63 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 72.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4668), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELMOD2]] | +0.63 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[ZDHHC21]] | +0.62 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[ATP13A2]] | +0.60 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[MTG1]] | +0.59 | +0.39 / +0.54 | both halves | 6e-05 |  |
| [[MYO5A]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[RSU1]] | +0.58 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[TCEA1]] | +0.58 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[MAPKAPK3]] | +0.57 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[ANK2]] | +0.57 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[EPRS1]] | +0.57 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[GPD1L]] | +0.56 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[AKTIP]] | +0.56 | +0.48 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2]] | -0.59 | -0.55 / -0.38 | both halves | 7e-05 |  |
| [[MEIS2]] | -0.57 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[GPRC5C]] | -0.56 | -0.32 / -0.58 | both halves | 2e-04 |  |
| [[ARID4B]] | -0.56 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[B9D2]] | -0.55 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[ASH1L]] | -0.55 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[EPS15-AS1]] | -0.54 | -0.51 / -0.29 | both halves | 2e-04 |  |
| [[UNK]] | -0.53 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[SNHG31]] | -0.53 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[DLEU2]] | -0.52 | -0.54 / -0.37 | both halves | 9e-05 |  |
| [[NAA38]] | -0.52 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[RBBP6]] | -0.52 | -0.42 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DTD1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.549). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.4, 4.0); signed map (-34.3, -32.6). **Vector** length 110, 28.8% of its response variance represented; |z| ≥ 3 in 1,276 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.4 | +13.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +9.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.7 | +5.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.5 | +7.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +5.3 | +5.9 |
|  | [[Neratinib (drug)]] 5 µM |  | +4.0 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.8 | +2.1 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.1 | -22.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -21.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -11.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.5 | -20.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.4 | -16.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -7.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.5 | -2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -2.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | D-aminoacyl-tRNA deacylase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.23 — chr20:18,587,942-18,766,644 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DUEB, MGC119131, MGC41905, bA379J5.3, bA555E18.1, pqn-68; previously C20orf88, HARS2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TEA8](https://www.uniprot.org/uniprotkb/Q8TEA8) (D-aminoacyl-tRNA deacylase 1):

> Possible ATPase involved in DNA replication, may facilitate loading of CDC45 onto pre-replication complexes.; An aminoacyl-tRNA editing enzyme that deacylates mischarged D-aminoacyl-tRNAs. Also deacylates mischarged glycyl-tRNA(Ala), protecting cells against glycine mischarging by AlaRS. Acts via tRNA-based rather than protein-based catalysis; rejects L-amino acids rather than detecting D-amino acids in the active site. By recycling D-aminoacyl-tRNA to D-amino acids and free tRNA molecules, …

**Summary**, from NCBI Gene [92675](https://www.ncbi.nlm.nih.gov/gene/92675):

> The protein encoded by this gene is similar in sequence to histidyl-tRNA synthetase, which hydrolyzes D-tyrosyl-tRNA(Tyr) into D-tyrosine and free tRNA(Tyr). The encoded protein binds the DNA unwinding element and plays a role in the initiation of DNA replication. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:16219](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16219) · Entrez [92675](https://www.ncbi.nlm.nih.gov/gene/92675) · UniProt [Q8TEA8](https://www.uniprot.org/uniprotkb/Q8TEA8) · Ensembl [ENSG00000125821](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125821)

## Data

Gene col 4668: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4668); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4668, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4668]; `tensor/DDL_lfc|DDL_z.npy` [4668]; `embed/gene_vectors.npy` [4668]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4668 or target_col == 4668). Every well: [[DTD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DTD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
