---
symbol: "AIFM2"
type: "gene"
col: 483
ensembl_id: "ENSG00000042286"
name: "AIF family member 2, ferroptosis suppressor"
location: "10q22.1"
module: 135
arm: "+"
pooled_cpm: 22.26
n_lines_expressing: 47
n_dd_up: 17
n_dd_down: 13
n_dd_up_clean: 13
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# AIFM2

*AIF family member 2, ferroptosis suppressor* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 1.98× (z +14.1, q 1e-42, up in 41 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.364× (z -20.9, q 0e+00, down in 41 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHBDD3]] (+0.67, fdr 5e-05), [[RCC1L]] (+0.66, fdr 4e-05), [[RNF6]] (+0.66, fdr 4e-05); moves opposite to [[EFHC1]] (-0.56, fdr 1e-04), [[HMGN3]] (-0.55, fdr 3e-05), [[GUSBP18]] (-0.55, fdr 1e-04).
> It sits in the **+** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NMRAL2P]] → it (grade B ⚠); 3 go from it, the strongest it → cells under [[Ouabain (Octahydrate) (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 483.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.98×** | +14.1 | 1e-42 | 41/43 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.73×** | +11.3 | 3e-27 | 36/44 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.76×** | +11.1 | 3e-26 | 33/44 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +10.2 | 2e-22 | 25/42 (BT-474, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +9.8 | 2e-20 | 31/43 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +6.1 | 1e-07 | 11/29 (NCI-H1792, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.5 | 2e-06 | 15/45 (A-172, HOP62, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +5.4 | 4e-06 | 22/44 (PANC-1, COLO 205, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.29×** | +5.3 | 6e-06 | 15/37 (J82, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +4.8 | 9e-05 | 16/44 (SW480, LoVo, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.17× | +4.5 | 3e-04 | 16/45 (SW480, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +4.5 | 3e-04 | 11/44 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.22×** | +4.2 | 0.001 | 15/44 (NCI-H2030, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.43×** | +3.8 | 0.005 | 8/42 (J82, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.20×** | +3.8 | 0.006 | 9/43 (LoVo, SW48, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.05 µM |  | 1.19× | +3.6 | 0.011 | 10/44 (SW 900, HS-578T, …) | all doses, stronger at high dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.013 | 3/43 (SK-MEL-2, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.20×** | +3.5 | 0.014 | 8/42 (NCI-H460, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.032 | 13/44 (BT-474, KATO III, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.050 | 3/43 (A-172, PANC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 483.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.364×** | -20.9 | 0e+00 | 41/45 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.379×** | -20.1 | 0e+00 | 39/45 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.423×** | -17.8 | 0e+00 | 36/44 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.694×** | -10.7 | 2e-24 | 27/43 (KATO III, SNU-1, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.651×** | -8.9 | 9e-17 | 26/45 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.690×** | -7.7 | 2e-12 | 27/43 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.710×** | -6.8 | 9e-10 | 25/44 (MIA PaCa-2, RKO, …) | top dose only | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.547×** | -6.5 | 5e-09 | 25/45 (SNU-1, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.733×** | -6.4 | 9e-09 | 20/42 (NCI-H460, SW480, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.742×** | -5.9 | 2e-07 | 20/43 (CHP-212, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.782×** | -5.1 | 2e-05 | 16/45 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.636×** | -4.9 | 5e-05 | 17/45 (KATO III, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.870× | -4.1 | 0.002 | 18/44 (SW480, SW48, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.836× | -3.4 | 0.025 | 5/44 (KATO III, LS 180, …) | inconsistent across doses |  |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | 0.840× | -3.4 | 0.025 | 3/45 (NCI-H2030, SW 1271, …) | inconsistent across doses | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.852× | -3.3 | 0.032 | 9/44 (SNU-423, SW 900, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.741×** | -3.2 | 0.040 | 11/41 (SW480, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib (drug)]] 0.05 µM |  | 0.855× | -3.1 | 0.068 | 2/43 (SW48, AN3 CA) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 483. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 19.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.158× (z -12.8) |
| [[LoVo (line)]] | wt | 27.3 | 2 | 3 | [[Ixazomib citrate (drug)]] 0.5 µM 2.87× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.198× (z -15.2) |
| [[NCI-H460 (line)]] | wt | 34.8 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +24.4) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 0.5 µM 0.379× (z -10.9) |
| [[RKO (line)]] | wt | 32.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -11.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.268× (z -10.2) |
| [[SW480 (line)]] | alt | 35.5 | 1 | 4 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.29× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.272× (z -17.7) |
| [[A549 (line)]] | wt | 30.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.285× (z -11.2) |
| [[KATO III (line)]] | alt | 41.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -14.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.188× (z -14.0) |
| [[LS 180 (line)]] | wt | 35.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -12.4) |
| [[COLO 205 (line)]] | alt | 20.9 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.99× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -10.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 17.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.211× (z -12.3) |
| [[HT-29 (line)]] | alt | 20.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.237× (z -9.8) |
| [[SNU-1 (line)]] | wt | 29.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -13.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Thymol (drug)]] 0.5 µM 0.217× (z -8.5) |
| [[SNU-423 (line)]] | alt | 23.1 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.151× (z -12.8) |
| [[SW1417 (line)]] | alt | 20.4 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0747× (z -18.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.313× (z -8.7) |
| [[SW48 (line)]] | wt | 58.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.247× (z -9.9) |
| [[A498 (line)]] | wt | 10.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 7.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.80× (z +11.7) | — |
| [[HCT15 (line)]] | alt | 31.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -11.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 25.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.351× (z -8.7) |
| [[HS-578T (line)]] | alt | 14.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.232× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 9.17 | 0 | 1 | — | [[Finasteride (drug)]] 0.05 µM 0.0702× (z -9.2) |
| [[J82 (line)]] | alt | 25.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -9.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1573 (line)]] | alt | 18.1 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.76× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 24.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.305× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -8.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[PANC-1 (line)]] | alt | 18.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.421× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.181× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 27.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -9.8) |
| [[A-172 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.51 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.73 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 483), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHBDD3]] | +0.67 | +0.60 / +0.39 | both halves | 5e-05 |  |
| [[RCC1L]] | +0.66 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[RNF6]] | +0.66 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[FBXO30]] | +0.65 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[BAG2]] | +0.65 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[DNAJA4]] | +0.65 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[EIF5]] | +0.62 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[HTATIP2]] | +0.61 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[KMT2D]] | +0.60 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[NSMAF]] | +0.60 | +0.56 / +0.39 | both halves | 5e-05 |  |
| [[EMG1]] | +0.60 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[TIRAP]] | +0.59 | +0.48 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFHC1]] | -0.56 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[HMGN3]] | -0.55 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[GUSBP18]] | -0.55 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[WDPCP]] | -0.54 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[PAFAH1B3]] | -0.54 | -0.33 / -0.28 | both halves | 3e-04 |  |
| [[ALAD]] | -0.54 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[CDKN2D]] | -0.53 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[ARL3]] | -0.53 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[DOP1A]] | -0.53 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[CKB]] | -0.52 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[INIP]] | -0.52 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[UGCG]] | -0.51 | -0.48 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NMRAL2P]] | B | NMRAL2P activity raises AIFM2's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 1.61× lower at baseline in the lines without NMRAL2P | 0.029 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Ouabain (Octahydrate) (drug)]] 0.05 µM | C | AIFM2 activity raises the cells' numbers under Ouabain (Octahydrate) 0.05 µM (protects the cells) | lines that do not express AIFM2 (3) vs lines expressing it (45) | the lines without AIFM2: 0.69× the cells of the other lines | 0.051 | ⚠ few lines (3 vs 47); across organs; also absent: FLVCR2, FUCA2, SLC9A3; maybe low, not absent |
| [[KMT2D]] | C | AIFM2 activity lowers KMT2D's level | lines that do not express AIFM2 (3) vs lines expressing it (47) | 1.71× higher at baseline in the lines without AIFM2 | 0.052 | ⚠ few lines (3 vs 47); across organs; also absent: FLVCR2, FUCA2, SLC9A3; maybe low, not absent |
| [[KIF21A]] | C | AIFM2 activity raises KIF21A's level | lines that do not express AIFM2 (3) vs lines expressing it (47) | 2.51× lower at baseline in the lines without AIFM2 | 0.067 | ⚠ few lines (3 vs 47); across organs; also absent: FLVCR2, FUCA2, SLC9A3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **+** arm (projection on the module's main direction 0.659). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-15.9, 10.5); signed map (22.0, -24.8). **Vector** length 96.1, 20.7% of its response variance represented; |z| ≥ 3 in 1,140 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +10.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.8 | +11.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.5 | +11.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.0 | +14.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.3 | +9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.5 | +5.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.9 | +4.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.2 | +2.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.6 | -17.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.0 | -20.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.5 | -20.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.3 | -4.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.1 | -7.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -6.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -3.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | AIF family member 2, ferroptosis suppressor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:70,098,223-70,132,934 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14497, PRG3, FSP1; previously AMID |
| Gene groups (HGNC) | Flavoproteins; AIF family |
| Reactome | 3 pathways, smallest: TP53 Regulates Transcription of Genes Involved in Cytochrome C Release; TP53 Regulates Transcription of Cell Death Genes; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRQ8](https://www.uniprot.org/uniprotkb/Q9BRQ8) (Ferroptosis suppressor protein 1):

> A NAD(P)H-dependent oxidoreductase that acts as a key inhibitor of ferroptosis. At the plasma membrane, catalyzes reduction of coenzyme Q/ubiquinone-10 to ubiquinol-10, a lipophilic radical-trapping antioxidant that prevents lipid oxidative damage and consequently ferroptosis. Acts in parallel to GPX4 to suppress phospholipid peroxidation and ferroptosis. This anti-ferroptotic function is independent of cellular glutathione levels. Also acts as a potent radical-trapping antioxidant by mediating …

**Summary**, from NCBI Gene [84883](https://www.ncbi.nlm.nih.gov/gene/84883):

> This gene encodes a flavoprotein oxidoreductase that binds single stranded DNA and is thought to contribute to apoptosis in the presence of bacterial and viral DNA. The expression of this gene is also found to be induced by tumor suppressor protein p53 in colon cancer cells. [provided by RefSeq, Nov 2010]

**Accessions** — [HGNC:21411](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21411) · Entrez [84883](https://www.ncbi.nlm.nih.gov/gene/84883) · UniProt [Q9BRQ8](https://www.uniprot.org/uniprotkb/Q9BRQ8) · Ensembl [ENSG00000042286](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000042286)

## Data

Gene col 483: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 483); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 483, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 483]; `tensor/DDL_lfc|DDL_z.npy` [483]; `embed/gene_vectors.npy` [483]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 483 or target_col == 483). Every well: [[AIFM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AIFM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
