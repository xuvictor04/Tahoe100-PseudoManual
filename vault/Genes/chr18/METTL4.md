---
symbol: "METTL4"
type: "gene"
col: 2154
ensembl_id: "ENSG00000101574"
name: "methyltransferase 4, N6-adenosine"
location: "18p11.32"
module: 15
arm: "+"
pooled_cpm: 24.1
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 20
n_dd_up_clean: 5
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# METTL4

*methyltransferase 4, N6-adenosine* — 18p11.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.41× (z +7.8, q 3e-12, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.315× (z -19.5, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HCFC1]] (+0.67, fdr 1e-05), [[TMEM11-DT]] (+0.67, fdr 1e-05), [[TCEANC2]] (+0.67, fdr 1e-05); moves opposite to [[ANKRD24]] (-0.63, fdr 1e-05), [[SYP]] (-0.63, fdr 3e-05), [[UGCG]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2154.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +7.8 | 3e-12 | 28/47 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +6.3 | 8e-08 | 26/48 (HOP62, SW1417, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.9 | 2e-04 | 20/47 (SW480, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.32×** | +4.4 | 0.002 | 17/48 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.007 | 19/47 (SW 900, J82, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.22×** | +3.3 | 0.076 | 11/47 (SW1417, HEC-1-A, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.076 | 12/48 (NCI-H2030, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2154.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.315×** | -19.5 | 0e+00 | 48/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.330×** | -18.7 | 0e+00 | 46/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.474×** | -17.3 | 0e+00 | 42/47 (A-427, A498, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.414×** | -14.9 | 0e+00 | 46/47 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.533×** | -10.2 | 2e-22 | 35/47 (COLO 205, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.575×** | -9.3 | 9e-19 | 34/47 (HT-29, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.598×** | -8.7 | 3e-16 | 40/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.682×** | -8.6 | 6e-16 | 38/48 (A-427, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.615×** | -8.2 | 1e-14 | 33/48 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.689×** | -6.3 | 2e-08 | 29/48 (SK-MEL-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.548×** | -5.3 | 6e-06 | 27/48 (SNU-1, Hs 766T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.731×** | -5.3 | 6e-06 | 23/46 (KATO III, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.717×** | -5.2 | 9e-06 | 21/39 (H4, hTERT-HPNE, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.563×** | -5.1 | 2e-05 | 21/46 (MIA PaCa-2, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.743×** | -5.0 | 2e-05 | 22/48 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.773×** | -4.2 | 9e-04 | 21/47 (NCI-H1573, MIA PaCa-2, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.694×** | -3.2 | 0.037 | 12/46 (NCI-H1573, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.05 µM |  | **0.830×** | -3.0 | 0.083 | 12/48 (HS-578T, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2154. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 24.4 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -16.6) |
| [[A-427 (line)]] | wt | 47.2 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -21.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.221× (z -14.2) |
| [[MIA PaCa-2 (line)]] | alt | 28.5 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.194× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 26.3 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -11.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.305× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 16.0 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -9.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.305× (z -9.3) |
| [[HT-29 (line)]] | alt | 32.0 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.215× (z -12.5) |
| [[H4 (line)]] | wt | 34.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -11.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.174× (z -10.5) |
| [[KATO III (line)]] | alt | 28.2 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.170× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.217× (z -12.3) |
| [[SW1417 (line)]] | alt | 19.9 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.246× (z -9.8) |
| [[HOP62 (line)]] | alt | 41.9 | 1 | 2 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.17× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.281× (z -11.0) |
| [[LoVo (line)]] | wt | 24.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -10.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.322× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 25.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -10.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 33.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0890× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.270× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 31.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.196× (z -11.7) |
| [[SW480 (line)]] | alt | 30.1 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.309× (z -11.3) |
| [[A498 (line)]] | wt | 14.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -17.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.220× (z -11.5) |
| [[BT-474 (line)]] | alt | 27.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -12.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Hydroxyurea (drug)]] 0.05 µM 0.219× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 24.0 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.309× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 26.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.249× (z -11.2) |
| [[LS 180 (line)]] | wt | 29.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.254× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 20.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.219× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 42.0 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.257× (z -11.2) |
| [[RKO (line)]] | wt | 23.8 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.244× (z -8.8) |
| [[SNU-1 (line)]] | wt | 31.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -9.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.223× (z -8.8) |
| [[A-172 (line)]] | wt | 22.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.256× (z -8.8) |
| [[COLO 205 (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.133× (z -10.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HepG2_C3A (line)]] | wt | 14.7 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.124× (z -8.9) |
| [[HS-578T (line)]] | alt | 20.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.259× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 19.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 21.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.246× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 18.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -9.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 22.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.240× (z -9.0) |
| [[A549 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2154), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCFC1]] | +0.67 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[TMEM11-DT]] | +0.67 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[TCEANC2]] | +0.67 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SAP30L-AS1]] | +0.67 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[GARS1-DT]] | +0.66 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[ZNF460-AS1]] | +0.66 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[PRDM10]] | +0.66 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[TIRAP]] | +0.63 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[LAMTOR5-AS1]] | +0.62 | +0.39 / +0.44 | both halves | 5e-05 |  |
| [[KMT2D]] | +0.62 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | +0.62 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[NBR2]] | +0.62 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD24]] | -0.63 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[SYP]] | -0.63 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[UGCG]] | -0.61 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[ZMIZ2]] | -0.61 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[TPPP]] | -0.61 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[POLM]] | -0.60 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[BAIAP3]] | -0.59 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[RING1]] | -0.59 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[CCDC85B]] | -0.57 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[DHRS2]] | -0.56 | -0.37 / -0.44 | both halves | 7e-05 |  |
| [[ATP5F1D]] ⚠ | -0.56 | -0.32 / -0.39 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[KCTD17]] | -0.56 | -0.22 / -0.45 | both halves | 6e-04 |  |
| [[PADI2]] | -0.56 | -0.34 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers METTL4's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers METTL4's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[DNAAF10]] | C | DNAAF10's natural level strengthens METTL4's drug response | DNAAF10's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.15; direction not clear | 0.085 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.550). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-3.2, 21.9); signed map (5.4, -1.2). **Vector** length 102, 25.0% of its response variance represented; |z| ≥ 3 in 1,134 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +7.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.6 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.9 | +1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +3.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.7 | -8.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.7 | -19.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.6 | -18.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.9 | -14.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.1 | -6.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.6 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -5.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | methyltransferase 4, N6-adenosine |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.32 — chr18:2,537,525-2,571,509 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23017, HsT661 |
| Gene groups (HGNC) | 7BS N6-adenosine DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N3J2](https://www.uniprot.org/uniprotkb/Q8N3J2) (N(6)-adenine-specific methyltransferase METTL4):

> N(6)-adenine-specific methyltransferase that can methylate both RNAs and DNA. Acts as a N(6)-adenine-specific RNA methyltransferase by catalyzing formation of N6,2'-O-dimethyladenosine (m6A(m)) on internal positions of U2 small nuclear RNA (snRNA): methylates the 6th position of adenine residues with a pre-deposited 2'-O-methylation. Internal m6A(m) methylation of snRNAs regulates RNA splicing. Also able to act as a N(6)-adenine-specific DNA methyltransferase by mediating methylation of DNA on …

**Summary**, from NCBI Gene [64863](https://www.ncbi.nlm.nih.gov/gene/64863):

> Enables RNA methyltransferase activity and site-specific DNA-methyltransferase (adenine-specific) activity. Contributes to mRNA N6-methyladenosine dioxygenase activity. Involved in regulation of gene expression; regulation of mitochondrial DNA replication; and snRNA (adenine-N6)-methylation. Located in cytosol; mitochondrial matrix; and nucleus. Part of RNA N6-methyladenosine methyltransferase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24726](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24726) · Entrez [64863](https://www.ncbi.nlm.nih.gov/gene/64863) · UniProt [Q8N3J2](https://www.uniprot.org/uniprotkb/Q8N3J2) · Ensembl [ENSG00000101574](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101574)

## Data

Gene col 2154: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2154); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2154, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2154]; `tensor/DDL_lfc|DDL_z.npy` [2154]; `embed/gene_vectors.npy` [2154]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2154 or target_col == 2154). Every well: [[METTL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METTL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
