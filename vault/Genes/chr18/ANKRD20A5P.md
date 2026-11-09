---
symbol: "ANKRD20A5P"
type: "gene"
col: 11821
ensembl_id: "ENSG00000186481"
name: "ankyrin repeat domain 20 family member A5, pseudogene"
location: "18p11.21"
module: 68
arm: "+"
pooled_cpm: 22.6
n_lines_expressing: 34
n_dd_up: 25
n_dd_down: 13
n_dd_up_clean: 18
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# ANKRD20A5P

*ankyrin repeat domain 20 family member A5, pseudogene* — 18p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.77× (z +22.1, q 0e+00, up in 27 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.666× (z -6.2, q 3e-07, down in 16 of 32 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLA2G4C]] (+0.66, fdr 7e-06), [[RIPK2-DT]] (+0.64, fdr 1e-05), [[ZNF702P]] (+0.63, fdr 1e-05); moves opposite to [[EFNA3]] (-0.60, fdr 1e-05), [[ATRN]] (-0.59, fdr 6e-05), [[EFNA4]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[GPR39]] → it (grade B ⚠); 2 go from it, the strongest it → [[WDR5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11821.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.77×** | +22.1 | 0e+00 | 27/30 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.53×** | +14.2 | 1e-43 | 24/29 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +13.0 | 1e-36 | 18/24 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.27×** | +12.0 | 3e-31 | 14/21 (SW1417, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.08×** | +10.4 | 3e-23 | 14/22 (SW 900, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.92×** | +9.6 | 8e-20 | 20/32 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +9.0 | 1e-17 | 23/32 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +6.8 | 5e-10 | 21/32 (NCI-H2347, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +6.6 | 2e-09 | 15/32 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +5.6 | 1e-06 | 16/31 (NCI-H2347, NCI-H1573, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +5.3 | 5e-06 | 12/31 (J82, LoVo, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.45×** | +5.2 | 1e-05 | 10/30 (HT-29, COLO 205, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +4.9 | 4e-05 | 15/30 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +4.5 | 3e-04 | 11/25 (PANC-1, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.8 | 0.005 | 9/31 (A-427, SW480, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.19× | +3.8 | 0.005 | 11/31 (J82, hTERT-HPNE, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.006 | 12/29 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.009 | 9/30 (J82, A-427, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.55×** | +3.5 | 0.013 | 8/26 (PANC-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.056 | 8/30 (HS-578T, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11821.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.666×** | -6.2 | 3e-07 | 16/32 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.690×** | -5.7 | 4e-06 | 18/32 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.524×** | -5.2 | 5e-05 | 16/31 (LS 180, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.743×** | -4.5 | 8e-04 | 10/29 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.755×** | -4.3 | 0.002 | 12/27 (SW480, NCI-H1792, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.586×** | -4.3 | 0.002 | 15/28 (SW480, LS 180, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.760×** | -4.2 | 0.002 | 10/30 (hTERT-HPNE, NCI-H1792, …) | all doses, flat |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.761×** | -4.2 | 0.002 | 5/31 (NCI-H2347, LS 180, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.768×** | -4.0 | 0.003 | 12/32 (NCI-H1792, SNU-423, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.925× | -4.0 | 0.003 | 2/32 (C-33 A, H4) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.770×** | -4.0 | 0.003 | 16/32 (SW480, COLO 205, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.794×** | -3.5 | 0.021 | 12/31 (NCI-H1792, SNU-423, …) | all doses, flat |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.852× | -3.4 | 0.025 | 9/32 (PANC-1, NCI-H2030, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.800×** | -3.4 | 0.027 | 13/32 (SW480, PANC-1, …) | top dose only | composition shift |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.788×** | -3.4 | 0.029 | 10/30 (hTERT-HPNE, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11821. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 50.9 | 3 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +20.8) | [[Panobinostat (drug)]] 0.5 µM 0.297× (z -13.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.313× (z -12.8) |
| [[A-427 (line)]] | wt | 160 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +16.4) | [[Ixazomib citrate (drug)]] 5 µM 0.260× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 21.0 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +14.4) | [[Digitoxin (drug)]] 5 µM 0.238× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 20.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +13.8) | — |
| [[J82 (line)]] | alt | 68.1 | 3 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 3.98× (z +9.2) | — |
| [[COLO 205 (line)]] | alt | 32.3 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -12.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.270× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 24.9 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.308× (z -9.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 18.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +14.0) | — |
| [[SW1417 (line)]] | alt | 17.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.11× (z +8.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.97× (z +8.6) | — |
| [[A549 (line)]] | wt | 55.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.235× (z -9.6) |
| [[HCT15 (line)]] | alt | 8.90 | 0 | 1 (1 ⚠) | — | [[OTS514 (drug)]] 0.05 µM 0.0777× (z -8.6) ⚠ transcription drop |
| [[LoVo (line)]] | wt | 17.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.223× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 42.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.334× (z -8.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H2030 (line)]] | alt | 48.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 6.60 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.89× (z +10.1) | — |
| [[A-172 (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.70 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.09 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.22 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.02 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11821), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLA2G4C]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[RIPK2-DT]] | +0.64 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[ZNF702P]] | +0.63 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[LPXN]] | +0.63 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[TSGA10]] | +0.62 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[HDAC9]] | +0.61 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[ANKRD18A]] | +0.60 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[RNF103-CHMP3]] | +0.59 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[LACC1]] | +0.57 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[PATL2]] | +0.57 | +0.59 / +0.35 | both halves | 1e-04 |  |
| [[ANKRD18B]] | +0.57 | +0.47 / +0.39 | both halves | 6e-05 |  |
| [[PPP1R1C]] | +0.57 | +0.57 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFNA3]] | -0.60 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[ATRN]] | -0.59 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[EFNA4]] | -0.57 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[INPP5B]] | -0.57 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[TAF5L]] | -0.57 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[KATNB1]] | -0.57 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[PACSIN2]] | -0.56 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[SMARCD2]] | -0.56 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[HDGFL2]] | -0.56 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[AP2S1]] | -0.56 | -0.53 / -0.32 | both halves | 1e-04 |  |
| [[CABIN1]] | -0.55 | -0.59 / -0.35 | both halves | 1e-04 |  |
| [[SLC9A6]] | -0.55 | -0.55 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR39]] | B | GPR39 activity raises ANKRD20A5P's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 3.26× lower at baseline in the lines without GPR39 | 0.044 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[LINC01186]] | B | LINC01186 activity raises ANKRD20A5P's level | lines that do not express LINC01186 (12) vs lines expressing it (38) | 2.91× lower at baseline in the lines without LINC01186 | 0.064 | ⚠ within organs, on part of the lines; also absent: LINC01836, STXBP2, EEPD1 |
| [[LINC00705]] | B | LINC00705 activity raises ANKRD20A5P's level | lines that do not express LINC00705 (8) vs lines expressing it (42) | 1.35× lower at baseline in the lines without LINC00705 | 0.084 | ⚠ within organs, on part of the lines; also absent: SMAD3; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WDR5]] | B | ANKRD20A5P activity lowers WDR5's level | lines that do not express ANKRD20A5P (16) vs lines expressing it (34) | 1.15× higher at baseline in the lines without ANKRD20A5P | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000283294, SH3RF2 |
| [[SLAMF7]] | B | ANKRD20A5P activity raises SLAMF7's level | lines that do not express ANKRD20A5P (16) vs lines expressing it (34) | 1.60× lower at baseline in the lines without ANKRD20A5P | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000283294, SH3RF2 |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.647). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (16.7, 11.9); signed map (26.8, 5.5). **Vector** length 89.3, 22.1% of its response variance represented; |z| ≥ 3 in 847 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.1 | +12.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.5 | +22.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.4 | +13.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.0 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.5 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +9.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.3 | +2.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.3 | +1.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -4.8 | -4.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.3 | -5.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.2 | -6.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.0 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -4.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.7 | -4.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.4 | -4.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 20 family member A5, pseudogene |
| Locus type | pseudogene |
| Location | 18p11.21 — chr18:14,179,395-14,244,811 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | MGC26718; previously ANKRD20A5 |
| Matched by | ensembl_id |

UniProt [A0PJZ0](https://www.uniprot.org/uniprotkb/A0PJZ0) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:33833](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33833) · Entrez [440482](https://www.ncbi.nlm.nih.gov/gene/440482) · UniProt [A0PJZ0](https://www.uniprot.org/uniprotkb/A0PJZ0) · Ensembl [ENSG00000186481](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186481)

## Data

Gene col 11821: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11821); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11821, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11821]; `tensor/DDL_lfc|DDL_z.npy` [11821]; `embed/gene_vectors.npy` [11821]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11821 or target_col == 11821). Every well: [[ANKRD20A5P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD20A5P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
