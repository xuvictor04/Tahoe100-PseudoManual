---
symbol: "PIK3C2B"
type: "gene"
col: 5407
ensembl_id: "ENSG00000133056"
name: "phosphatidylinositol-4-phosphate 3-kinase catalytic subunit type 2 beta"
location: "1q32.1"
module: 44
arm: "+"
pooled_cpm: 24.41
n_lines_expressing: 47
n_dd_up: 27
n_dd_down: 46
n_dd_up_clean: 25
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 24
direction_downstream: 3
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# PIK3C2B

*phosphatidylinositol-4-phosphate 3-kinase catalytic subunit type 2 beta* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (2 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.87× (z +10.4, q 1e-22, up in 31 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 46 drug-doses (13 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.453× (z -13.1, q 1e-36, down in 32 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP3K8]] (+0.68, fdr 7e-06), [[PLAAT3]] (+0.67, fdr 1e-05), [[CYP2S1]] (+0.66, fdr 7e-06); moves opposite to [[CLMP]] (-0.55, fdr 1e-05), [[TFPI]] (-0.55, fdr 1e-05), [[PDK1-AS1]] (-0.53, fdr 1e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[RNF43]] → it (grade B ⚠); 3 go from it, the strongest it → cells under [[Filgotinib (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5407.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.87×** | +10.4 | 1e-22 | 31/44 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.40×** | +7.9 | 7e-13 | 27/45 (AsPC-1, NCI-H1792, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +7.8 | 1e-12 | 26/45 (NCI-H2347, HOP62, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.58×** | +7.6 | 5e-12 | 25/44 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +7.4 | 2e-11 | 21/44 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +6.8 | 1e-09 | 26/43 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.53×** | +6.2 | 3e-08 | 23/42 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.86×** | +5.4 | 6e-06 | 19/45 (J82, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.28×** | +4.9 | 6e-05 | 16/45 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.33×** | +4.7 | 1e-04 | 17/44 (PANC-1, A549, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.35×** | +4.6 | 2e-04 | 19/43 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.27×** | +4.6 | 2e-04 | 17/45 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.33×** | +4.5 | 3e-04 | 16/44 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.31×** | +4.4 | 4e-04 | 15/44 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.36×** | +4.4 | 5e-04 | 9/44 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +4.2 | 9e-04 | 19/42 (NCI-H460, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 46 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5407.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.453×** | -13.1 | 1e-36 | 32/44 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.598×** | -12.1 | 5e-31 | 32/44 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.505×** | -11.3 | 2e-27 | 26/43 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.496×** | -10.8 | 7e-25 | 20/33 (Panc 03.27, A-172, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.569×** | -9.4 | 9e-19 | 28/43 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.577×** | -9.1 | 6e-18 | 28/44 (HT-29, RPMI-7951, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.591×** | -8.7 | 2e-16 | 28/44 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.604×** | -8.4 | 4e-15 | 30/43 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.705×** | -8.2 | 1e-14 | 23/44 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.636×** | -7.5 | 4e-12 | 23/36 (LoVo, SW48, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.616×** | -7.1 | 5e-11 | 21/29 (KATO III, HEC-1-A, …) | all doses, flat | composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.666×** | -6.7 | 7e-10 | 25/44 (HT-29, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.635×** | -6.7 | 1e-09 | 25/43 (Panc 03.27, LS 180, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.670×** | -6.6 | 1e-09 | 23/42 (KATO III, SW 900, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.757×** | -6.5 | 3e-09 | 23/45 (HT-29, KATO III, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.649×** | -6.4 | 7e-09 | 23/44 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.652×** | -6.3 | 1e-08 | 23/43 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.703×** | -5.8 | 1e-07 | 23/44 (AsPC-1, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.704×** | -5.8 | 2e-07 | 23/44 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.709×** | -5.7 | 3e-07 | 23/44 (LS 180, HT-29, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.630×** | -5.5 | 1e-06 | 19/41 (Panc 03.27, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5407. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 52.8 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -31.4) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0449× (z -31.3) |
| [[LS 180 (line)]] | wt | 91.9 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -23.7) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -15.1) |
| [[HT-29 (line)]] | alt | 44.5 | 0 | 9 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.157× (z -15.0) |
| [[KATO III (line)]] | alt | 41.8 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -18.0) |
| [[SW480 (line)]] | alt | 24.1 | 0 | 8 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.184× (z -15.2) |
| [[COLO 205 (line)]] | alt | 88.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -19.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.105× (z -15.8) |
| [[NCI-H460 (line)]] | wt | 13.0 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.195× (z -10.9) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.204× (z -10.6) |
| [[SW1417 (line)]] | alt | 36.2 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -14.0) |
| [[C32 (line)]] | wt | 52.6 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -12.2) |
| [[CFPAC-1 (line)]] | alt | 35.0 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +15.9) ⚠ cell-cycle shift, explains ~45% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.218× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.265× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 29.1 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.169× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 33.7 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -15.6) |
| [[SW48 (line)]] | wt | 48.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0677× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[NCI-H1573 (line)]] | alt | 18.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -10.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.234× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 13.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0889× (z -17.8) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0977× (z -12.1) |
| [[PANC-1 (line)]] | alt | 12.6 | 1 (1 ⚠) | 1 | [[Harringtonine (drug)]] 0.5 µM 3.41× (z +9.0) ⚠ cell-cycle shift, explains ~20% of this change | [[Bortezomib (drug)]] 0.05 µM 0.261× (z -9.4) |
| [[RKO (line)]] | wt | 16.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0549× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -8.8) |
| [[A-172 (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0934× (z -12.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 49.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[HCT15 (line)]] | alt | 34.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.171× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[J82 (line)]] | alt | 10.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +8.7) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 9.25 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.88× (z +10.2) ⚠ position not correctable | — |
| [[NCI-H2030 (line)]] | alt | 8.80 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.136× (z -9.1) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 26.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 9.38 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0605× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 8.10 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0897× (z -9.1) |
| [[A-427 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.81 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.78 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5407), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP3K8]] | +0.68 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[PLAAT3]] | +0.67 | +0.68 / +0.55 | both halves | 1e-05 | pathway: Phospholipid metabolism |
| [[CYP2S1]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[ARHGEF16]] | +0.65 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[PLEKHG6]] | +0.64 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[ATP8B1]] | +0.64 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[LRRC1]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[PKDCC]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[SLC11A2]] | +0.61 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[ST3GAL4]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[IL22RA1]] | +0.60 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[ADGRB2]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLMP]] | -0.55 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[TFPI]] | -0.55 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[PDK1-AS1]] | -0.53 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[RPSAP52]] | -0.53 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[KPNA4]] | -0.53 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[HCG18]] | -0.52 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[ERVK13-1]] | -0.52 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[AVEN]] | -0.52 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[FAM120B]] | -0.50 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[OSMR-DT]] | -0.50 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[WDR27]] | -0.50 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[ST3GAL3]] | -0.50 | -0.56 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 24, C 0. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF43]] | B | RNF43 activity raises PIK3C2B's level | lines that do not express RNF43 (26) vs lines expressing it (24) | 2.09× lower at baseline in the lines without RNF43 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1 |
| [[ANO9]] | B | ANO9 activity raises PIK3C2B's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 1.82× lower at baseline in the lines without ANO9 | 0.001 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[ANKRD22]] | B | ANKRD22 activity raises PIK3C2B's level | lines that do not express ANKRD22 (34) vs lines expressing it (16) | 2.37× lower at baseline in the lines without ANKRD22 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises PIK3C2B's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 2.32× lower at baseline in the lines without TMPRSS2 | 0.004 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[TC2N]] | B | TC2N activity raises PIK3C2B's level | lines that do not express TC2N (28) vs lines expressing it (22) | 2.22× lower at baseline in the lines without TC2N | 0.007 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |
| [[PRR15L]] | B | PRR15L activity raises PIK3C2B's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 2.44× lower at baseline in the lines without PRR15L | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881 |
| [[CLDN3]] | B | CLDN3 activity raises PIK3C2B's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 2.15× lower at baseline in the lines without CLDN3 | 0.012 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[FAM221A]] | B | FAM221A activity raises PIK3C2B's level | lines that do not express FAM221A (13) vs lines expressing it (37) | 2.34× lower at baseline in the lines without FAM221A | 0.012 | ⚠ within organs, on part of the lines; also absent: TRIM2, MICE |
| [[SLC52A3]] | B | SLC52A3 activity raises PIK3C2B's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 2.12× lower at baseline in the lines without SLC52A3 | 0.015 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[TJP2]] | B | TJP2 activity raises PIK3C2B's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 1.52× lower at baseline in the lines without TJP2 | 0.024 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[PLEKHG6]] | B | PLEKHG6 activity raises PIK3C2B's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 1.94× lower at baseline in the lines without PLEKHG6 | 0.036 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[HNF1B]] | B | HNF1B activity raises PIK3C2B's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 1.77× lower at baseline in the lines without HNF1B | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Filgotinib (drug)]] 0.05 µM | C | [[LINC03015]], PIK3C2B activity lowers the cells' numbers under Filgotinib 0.05 µM (makes them more sensitive) | lines that do not express LINC03015, PIK3C2B (3) vs lines expressing them (45) | the lines without LINC03015, PIK3C2B: 1.34× the cells of the other lines | 0.055 | ⚠ few lines (3 vs 47); across organs; also absent: MCF2L2, CYB561, PTPN3; maybe low, not absent; co-absent genes |
| cells under [[Posaconazole (drug)]] 5 µM | C | [[LINC03015]], PIK3C2B activity lowers the cells' numbers under Posaconazole 5 µM (makes them more sensitive) | lines that do not express LINC03015, PIK3C2B (3) vs lines expressing them (45) | the lines without LINC03015, PIK3C2B: 1.32× the cells of the other lines | 0.068 | ⚠ few lines (3 vs 47); across organs; also absent: MCF2L2, CYB561, PTPN3; maybe low, not absent; co-absent genes |
| [[EPB41]] | C | PIK3C2B activity raises EPB41's level | lines that do not express PIK3C2B (3) vs lines expressing it (47) | 2.65× lower at baseline in the lines without PIK3C2B | 0.099 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: MCF2L2, CYB561, PTPN3; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.4, 52.8); signed map (50.3, 2.7). **Vector** length 114, 31.4% of its response variance represented; |z| ≥ 3 in 1,290 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glucuronidation* (reactome, mean cos +0.53 to 4); *Aspirin ADME* (reactome, mean cos +0.53 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +7.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +6.2 | +7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +6.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.8 | +7.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.5 | +10.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.8 | +5.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +6.2 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -4.4 | -5.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -9.1 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -3.6 | -6.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.6 | -2.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.6 | -6.4 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol-4-phosphate 3-kinase catalytic subunit type 2 beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:204,422,628-204,494,805 (-) |
| Ensembl biotype | protein_coding |
| Also known as | C2-PI3K, PI3K-C2beta |
| Gene groups (HGNC) | Phosphatidylinositol 3-kinase family |
| Reactome | 4 pathways, smallest: Synthesis of PIPs at the plasma membrane; PI Metabolism; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O00750](https://www.uniprot.org/uniprotkb/O00750) (Phosphatidylinositol 4-phosphate 3-kinase C2 domain-containing subunit beta):

> Phosphorylates PtdIns and PtdIns4P with a preference for PtdIns. Does not phosphorylate PtdIns(4,5)P2. May be involved in EGF and PDGF signaling cascades.

**Summary**, from NCBI Gene [5287](https://www.ncbi.nlm.nih.gov/gene/5287):

> The protein encoded by this gene belongs to the phosphoinositide 3-kinase (PI3K) family. PI3-kinases play roles in signaling pathways involved in cell proliferation, oncogenic transformation, cell survival, cell migration, and intracellular protein trafficking. This protein contains a lipid kinase catalytic domain as well as a C-terminal C2 domain, a characteristic of class II PI3-kinases. C2 domains act as calcium-dependent phospholipid binding motifs that mediate translocation of proteins to …

**Accessions** — [HGNC:8972](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8972) · Entrez [5287](https://www.ncbi.nlm.nih.gov/gene/5287) · UniProt [O00750](https://www.uniprot.org/uniprotkb/O00750) · Ensembl [ENSG00000133056](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133056)

## Data

Gene col 5407: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5407); `tables/drug_effects.parquet` (84 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5407, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5407]; `tensor/DDL_lfc|DDL_z.npy` [5407]; `embed/gene_vectors.npy` [5407]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5407 or target_col == 5407). Every well: [[PIK3C2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIK3C2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
