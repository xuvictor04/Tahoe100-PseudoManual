---
symbol: "RHOB"
type: "gene"
col: 6818
ensembl_id: "ENSG00000143878"
name: "ras homolog family member B"
location: "2p24.1"
module: 123
arm: "+"
pooled_cpm: 51.82
n_lines_expressing: 49
n_dd_up: 49
n_dd_down: 12
n_dd_up_clean: 48
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# RHOB

*ras homolog family member B* — 2p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 49 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.64× (z +20.3, q 0e+00, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.451× (z -12.6, q 1e-33, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JUND]] (+0.77, fdr 7e-06), [[KLF2]] (+0.77, fdr 7e-06), [[KLF6]] (+0.69, fdr 7e-06); moves opposite to [[HSPA14]] (-0.67, fdr 1e-05), [[DPY19L3]] (-0.54, fdr 2e-05), [[ITPKB]] (-0.53, fdr 9e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 49 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6818.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.64×** | +20.3 | 0e+00 | 42/46 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **4.99×** | +17.2 | 0e+00 | 46/46 (HOP62, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **3.92×** | +15.2 | 0e+00 | 44/46 (LS 180, hTERT-HPNE, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **3.23×** | +12.6 | 6e-34 | 39/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +9.4 | 1e-18 | 42/47 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.25×** | +9.0 | 2e-17 | 34/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.20×** | +8.8 | 1e-16 | 40/47 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.17×** | +8.6 | 5e-16 | 35/46 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.98×** | +7.6 | 2e-12 | 39/47 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.97×** | +7.6 | 2e-12 | 31/47 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Neratinib (drug)]] 5 µM |  | **1.96×** | +7.5 | 4e-12 | 39/47 (HEC-1-A, MIA PaCa-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | **1.98×** | +7.0 | 9e-11 | 36/46 (hTERT-HPNE, SW480, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.55×** | +6.9 | 2e-10 | 37/47 (LOX-IMVI, SW48, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +6.9 | 2e-10 | 32/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.78×** | +6.8 | 5e-10 | 33/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.62×** | +6.4 | 7e-09 | 33/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6818.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.451×** | -12.6 | 1e-33 | 41/48 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.467×** | -8.2 | 9e-14 | 38/47 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.589×** | -5.7 | 2e-06 | 32/49 (C32, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.608×** | -5.6 | 4e-06 | 37/47 (LS 180, SW48, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.422×** | -5.0 | 5e-05 | 27/46 (SNU-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.639×** | -5.0 | 5e-05 | 27/47 (SNU-1, RKO, …) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | **0.718×** | -3.7 | 0.017 | 27/47 (hTERT-HPNE, SW480, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.728×** | -3.6 | 0.026 | 20/47 (hTERT-HPNE, HS-578T, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.801×** | -3.5 | 0.028 | 24/47 (NCI-H2030, BT-474, …) | rises with dose | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.726×** | -3.4 | 0.032 | 21/48 (HepG2/C3A, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.740×** | -3.4 | 0.038 | 19/47 (CFPAC-1, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.815×** | -3.2 | 0.055 | 23/48 (HCT15, AsPC-1, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6818. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 182 | 14 (2 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.64× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -22.2) |
| [[RKO (line)]] | wt | 34.9 | 10 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 7.59× (z +16.8) | [[Auranofin (drug)]] 5 µM 0.156× (z -10.9) |
| [[PANC-1 (line)]] | alt | 14.7 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.3× (z +23.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 32.1 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.41× (z +17.8) | — |
| [[SW480 (line)]] | alt | 58.0 | 6 | 3 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 5.19× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -13.0) |
| [[HEC-1-A (line)]] | alt | 40.1 | 7 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +14.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -9.0) |
| [[SNU-1 (line)]] | wt | 83.3 | 6 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +16.6) | [[Auranofin (drug)]] 5 µM 0.142× (z -13.3) |
| [[C32 (line)]] | wt | 82.9 | 5 | 2 | [[Homoharringtonine (drug)]] 5 µM 23.0× (z +28.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -10.3) |
| [[LS 180 (line)]] | wt | 53.9 | 6 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +14.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 65.5 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +15.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -13.3) |
| [[HepG2_C3A (line)]] | wt | 159 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +15.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -17.5) |
| [[hTERT-HPNE (line)]] | wt | 64.6 | 4 | 2 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 7.49× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -12.2) |
| [[C-33 A (line)]] | alt | 83.1 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -11.0) |
| [[A-172 (line)]] | wt | 28.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.22× (z +14.3) | — |
| [[A-427 (line)]] | wt | 35.1 | 4 | 0 | [[Harringtonine (drug)]] 5 µM 5.32× (z +10.2) | — |
| [[A498 (line)]] | wt | 23.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.6× (z +22.9) | — |
| [[A549 (line)]] | wt | 77.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 45.9 | 3 | 1 | [[Pitavastatin (Calcium) (drug)]] 5 µM 7.24× (z +13.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -8.7) |
| [[HS-578T (line)]] | alt | 21.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +12.6) | — |
| [[LoVo (line)]] | wt | 63.8 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +11.2) | [[Auranofin (drug)]] 5 µM 0.268× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 90.3 | 3 (1 ⚠) | 1 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 6.52× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 28.1 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.30× (z +17.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 66.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +13.9) | — |
| [[CFPAC-1 (line)]] | alt | 69.7 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +19.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -14.0) |
| [[KATO III (line)]] | alt | 28.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 19.6 | 3 | 0 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 10.2× (z +10.9) | — |
| [[NCI-H23 (line)]] | alt | 16.4 | 3 | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 12.4× (z +10.8) | — |
| [[RPMI-7951 (line)]] | alt | 30.7 | 3 | 0 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 12.5× (z +13.3) | — |
| [[SW 900 (line)]] | alt | 51.4 | 2 | 1 | [[Pitavastatin (Calcium) (drug)]] 5 µM 4.87× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -13.6) |
| [[COLO 205 (line)]] | alt | 50.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +10.2) | — |
| [[H4 (line)]] | wt | 31.0 | 2 | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 17.7× (z +11.1) | — |
| [[HCT15 (line)]] | alt | 42.2 | 2 | 0 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 7.01× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 38.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.50× (z +15.5) | — |
| [[Panc 03.27 (line)]] | alt | 37.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.17× (z +17.8) | — |
| [[SHP-77 (line)]] | alt | 29.5 | 2 | 0 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 9.70× (z +11.6) | — |
| [[SNU-423 (line)]] | alt | 29.4 | 2 | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 5.62× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 54.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -12.6) |
| [[SW48 (line)]] | wt | 43.6 | 2 | 0 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 7.82× (z +10.2) | — |
| [[AN3 CA (line)]] | alt | 32.0 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.05 µM 0.0486× (z -10.4) |
| [[BT-474 (line)]] | alt | 112 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.6) | — |
| [[CHP-212 (line)]] | wt | 89.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -13.3) |
| [[J82 (line)]] | alt | 13.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.09× (z +13.2) | — |
| [[Hs 766T (line)]] | wt | 8.96 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6818), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUND]] | +0.77 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[KLF2]] | +0.77 | +0.75 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 401 |
| [[KLF6]] | +0.69 | +0.72 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[DUSP8]] | +0.69 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[EZR]] | +0.63 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[TUBB2A]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[KLF4]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[MRTFA]] | +0.62 | +0.50 / +0.64 | both halves | 1e-05 | pathway: RHO GTPase Effectors |
| [[ARL4A]] | +0.61 | +0.54 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[JUN]] | +0.59 | +0.59 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_APOPTOSIS; STRING 519 |
| [[LMNA]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_APOPTOSIS |
| [[KRTAP5-AS1]] | +0.58 | +0.54 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPA14]] | -0.67 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[DPY19L3]] | -0.54 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[ITPKB]] | -0.53 | -0.37 / -0.54 | both halves | 9e-05 |  |
| [[ZCCHC4]] | -0.53 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[GMPS]] | -0.52 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[BIVM]] | -0.52 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[SNHG30]] | -0.51 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[NAF1]] | -0.51 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[TCEANC2]] | -0.51 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[METTL21A]] | -0.51 | -0.37 / -0.44 | both halves | 9e-05 |  |
| [[DNAAF10]] | -0.50 | -0.25 / -0.48 | both halves | 4e-04 |  |
| [[SNRNP40]] | -0.50 | -0.56 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RHOB's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LZTS3]] | C | LZTS3's natural level strengthens RHOB's drug response | LZTS3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.13; direction not clear | 0.078 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.786). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.0, -0.3); signed map (-0.5, 22.8). **Vector** length 142, 44.5% of its response variance represented; |z| ≥ 3 in 1,742 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.5 | +9.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +9.5 | +17.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +8.5 | +15.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +8.1 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.1 | +20.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +7.6 | +6.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +6.0 | +5.6 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -10.2 | -8.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.4 | -12.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -8.0 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.8 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | -2.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.5 | -5.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.4 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | ras homolog family member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p24.1 — chr2:20,447,074-20,449,440 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RHOH6, MST081; previously ARH6, ARHB |
| Gene groups (HGNC) | Rho family GTPases |
| Hallmark sets | APOPTOSIS, UV_RESPONSE_UP, IL2_STAT5_SIGNALING, EPITHELIAL_MESENCHYMAL_TRANSITION, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 21 pathways, smallest: RHO GTPases Activate Rhotekin and Rhophilins; RHO GTPases Activate ROCKs; RHO GTPases activate CIT |
| Matched by | ensembl_id |

**Function**, from UniProt [P62745](https://www.uniprot.org/uniprotkb/P62745) (Rho-related GTP-binding protein RhoB):

> Mediates apoptosis in neoplastically transformed cells after DNA damage. Not essential for development but affects cell adhesion and growth factor signaling in transformed cells. Plays a negative role in tumorigenesis as deletion causes tumor formation. Involved in intracellular protein trafficking of a number of proteins. Targets PKN1 to endosomes and is involved in trafficking of the EGF receptor from late endosomes to lysosomes. Also required for stability and nuclear trafficking of AKT1/AKT …

**Summary**, from NCBI Gene [388](https://www.ncbi.nlm.nih.gov/gene/388):

> Predicted to enable GTP binding activity and GTPase activity. Involved in several processes, including cellular response to hydrogen peroxide; cellular response to ionizing radiation; and regulation of cell migration. Located in cleavage furrow and endosome membrane. Biomarker of breast cancer. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:668](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:668) · Entrez [388](https://www.ncbi.nlm.nih.gov/gene/388) · UniProt [P62745](https://www.uniprot.org/uniprotkb/P62745) · Ensembl [ENSG00000143878](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143878)

## Data

Gene col 6818: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6818); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6818, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6818]; `tensor/DDL_lfc|DDL_z.npy` [6818]; `embed/gene_vectors.npy` [6818]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6818 or target_col == 6818). Every well: [[RHOB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHOB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
