---
symbol: "USP11"
type: "gene"
col: 2229
ensembl_id: "ENSG00000102226"
name: "ubiquitin specific peptidase 11"
location: "Xp11.3"
module: 159
arm: "+"
pooled_cpm: 57.92
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 19
n_dd_up_clean: 16
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# USP11

*ubiquitin specific peptidase 11* — Xp11.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.89× (z +13.4, q 4e-38, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.528× (z -9.5, q 1e-18, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MEPCE]] (+0.73, fdr 2e-05), [[LPXN]] (+0.73, fdr 1e-05), [[ZNF341-AS1]] (+0.70, fdr 2e-05); moves opposite to [[SERAC1]] (-0.69, fdr 3e-05), [[PACC1]] (-0.69, fdr 1e-05), [[ACTR5]] (-0.67, fdr 1e-05).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2229.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +13.4 | 4e-38 | 40/48 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.98×** | +10.1 | 1e-21 | 35/47 (NCI-H460, HEC-1-A, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.59×** | +9.7 | 4e-20 | 33/48 (J82, PANC-1, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +9.6 | 2e-19 | 40/49 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +8.1 | 9e-14 | 37/43 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.70×** | +7.5 | 5e-12 | 31/43 (AsPC-1, SW480, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.66×** | +7.2 | 4e-11 | 36/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +7.1 | 1e-10 | 38/48 (SNU-423, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +6.7 | 2e-09 | 29/48 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +6.1 | 4e-08 | 35/48 (NCI-H2347, Hs 766T, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +6.1 | 6e-08 | 30/48 (SW480, SNU-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +5.3 | 7e-06 | 33/48 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +4.6 | 2e-04 | 27/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.003 | 25/48 (NCI-H2347, SK-MEL-2, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.31×** | +3.9 | 0.003 | 26/48 (NCI-H460, HCT15, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.33×** | +3.9 | 0.004 | 25/48 (RPMI-7951, NCI-H2030, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.008 | 19/48 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.28×** | +3.5 | 0.016 | 19/48 (PANC-1, HOP62, …) | inconsistent across doses | position effect removed |
| [[Minodronic acid (drug)]] 5 µM |  | **1.53×** | +3.3 | 0.029 | 16/48 (CFPAC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.029 | 17/47 (LOX-IMVI, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2229.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.528×** | -9.5 | 1e-18 | 44/48 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.558×** | -8.7 | 1e-15 | 40/48 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.599×** | -7.6 | 5e-12 | 42/48 (C32, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.627×** | -6.9 | 6e-10 | 37/48 (C32, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.652×** | -6.4 | 2e-08 | 32/48 (NCI-H1573, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.695×** | -5.4 | 6e-06 | 30/48 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.542×** | -4.8 | 2e-04 | 27/48 (RPMI-7951, C32, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.730×** | -4.5 | 5e-04 | 25/48 (BT-474, NCI-H1573, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.740×** | -4.5 | 5e-04 | 27/48 (C32, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.758×** | -4.1 | 0.002 | 25/48 (NCI-H1792, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.589×** | -4.1 | 0.002 | 24/48 (A-427, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.769×** | -3.9 | 0.004 | 24/48 (CFPAC-1, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.770×** | -3.9 | 0.004 | 23/47 (H4, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.832×** | -3.9 | 0.004 | 22/49 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.632×** | -3.6 | 0.013 | 20/45 (SHP-77, H4, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.654×** | -3.3 | 0.035 | 24/49 (CFPAC-1, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.806×** | -3.2 | 0.043 | 15/48 (H4, HOP62, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2229. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 95.9 | 4 (4 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.5) ⚠ cell-cycle shift, explains ~31% of this change | [[Belinostat (drug)]] 5 µM 0.370× (z -10.6) |
| [[C32 (line)]] | wt | 113 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.128× (z -16.3) |
| [[HEC-1-A (line)]] | alt | 43.6 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +12.7) | — |
| [[NCI-H460 (line)]] | wt | 34.2 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +12.3) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[HS-578T (line)]] | alt | 44.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.276× (z -10.6) |
| [[J82 (line)]] | alt | 53.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +15.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +14.3) | — |
| [[NCI-H2347 (line)]] | alt | 44.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +13.3) | — |
| [[PANC-1 (line)]] | alt | 54.5 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +13.3) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SNU-423 (line)]] | alt | 64.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +12.1) | — |
| [[SW1417 (line)]] | alt | 67.5 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +11.8) | — |
| [[A-172 (line)]] | wt | 61.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +11.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.98× (z +9.1) | — |
| [[AsPC-1 (line)]] | alt | 31.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.62× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +8.8) | — |
| [[KATO III (line)]] | alt | 41.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +13.2) | — |
| [[NCI-H1573 (line)]] | alt | 81.3 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.277× (z -11.5) |
| [[NCI-H23 (line)]] | alt | 64.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.0377× (z -24.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 114 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.8) ⚠ cell-cycle shift, explains ~31% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.397× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 58.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +10.9) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[AN3 CA (line)]] | alt | 122 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.219× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 63.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.416× (z -8.9) |
| [[HOP62 (line)]] | alt | 59.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +12.1) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[Hs 766T (line)]] | wt | 33.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +8.7) | — |
| [[LoVo (line)]] | wt | 40.1 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.323× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 33.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.1) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 158 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 64.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +10.1) | — |
| [[RKO (line)]] | wt | 17.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.06× (z +9.6) | — |
| [[SW 1271 (line)]] | alt | 49.9 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0711× (z -9.3) ⚠ transcription drop |
| [[A-427 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 147 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 63.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 60.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 89.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2229), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEPCE]] | +0.73 | +0.75 / +0.47 | both halves | 2e-05 |  |
| [[LPXN]] | +0.73 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[ZNF341-AS1]] | +0.70 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[MMADHC-DT]] | +0.70 | +0.68 / +0.38 | both halves | 6e-05 |  |
| [[AP4S1]] | +0.70 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[SP2]] | +0.69 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[PBLD]] | +0.69 | +0.63 / +0.38 | both halves | 7e-05 |  |
| [[ATXN1L]] | +0.69 | +0.69 / +0.43 | both halves | 3e-05 |  |
| [[PKN2-AS1]] | +0.68 | +0.66 / +0.33 | both halves | 1e-04 |  |
| [[MED29]] | +0.68 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[UBE3B]] | +0.68 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[LINC01135]] | +0.67 | +0.63 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERAC1]] | -0.69 | -0.66 / -0.44 | both halves | 3e-05 |  |
| [[PACC1]] | -0.69 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[ACTR5]] | -0.67 | -0.60 / -0.53 | both halves | 1e-05 | pathway: Deubiquitination |
| [[ANKRD27]] | -0.66 | -0.60 / -0.39 | both halves | 6e-05 |  |
| [[C20orf27]] | -0.65 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[RSAD1]] | -0.65 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[SLC9A6]] | -0.64 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[METAP1]] | -0.64 | -0.65 / -0.38 | both halves | 7e-05 |  |
| [[GARNL3]] | -0.64 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[ST6GALNAC4]] | -0.64 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[SLC23A2]] | -0.64 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[STX7]] | -0.64 | -0.57 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers USP11's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[AP3B2]] | B | AP3B2 activity raises USP11's level | lines that do not express AP3B2 (15) vs lines expressing it (35) | 1.56× lower at baseline in the lines without AP3B2 | 0.027 | ⚠ within organs, on part of the lines; also absent: MAPK8IP2, MED12L, HRK; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction -0.726). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.3, 10.4); signed map (21.5, -6.3). **Vector** length 121, 36.7% of its response variance represented; |z| ≥ 3 in 1,088 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +12.3 | +9.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +9.8 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.6 | +13.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +9.2 | +6.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +6.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.8 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +1.7 |
| fall | [[Belinostat (drug)]] 5 µM |  | -7.4 | -9.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.9 | -8.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.8 | -7.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.2 | -4.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.2 | -4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.2 | -3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.4 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.4 | -3.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.3 — chrX:47,232,866-47,248,328 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UHX1 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Hallmark sets | COAGULATION, DNA_REPAIR |
| Reactome | 5 pathways, smallest: Association of TriC/CCT with target proteins during biosynthesis; Chaperonin-mediated protein folding; Protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [P51784](https://www.uniprot.org/uniprotkb/P51784) (Ubiquitin carboxyl-terminal hydrolase 11):

> Protease that can remove conjugated ubiquitin from target proteins and polyubiquitin chains. Inhibits the degradation of target proteins by the proteasome. Cleaves preferentially 'Lys-6' and 'Lys-63'-linked ubiquitin chains. Has lower activity with 'Lys-11' and 'Lys-33'-linked ubiquitin chains, and extremely low activity with 'Lys-27', 'Lys-29' and 'Lys-48'-linked ubiquitin chains (in vitro). Plays a role in the regulation of pathways leading to NF-kappa-B activation. Plays a role in the …

**Summary**, from NCBI Gene [8237](https://www.ncbi.nlm.nih.gov/gene/8237):

> Protein ubiquitination controls many intracellular processes, including cell cycle progression, transcriptional activation, and signal transduction. This dynamic process, involving ubiquitin conjugating enzymes and deubiquitinating enzymes, adds and removes ubiquitin. Deubiquitinating enzymes are cysteine proteases that specifically cleave ubiquitin from ubiquitin-conjugated protein substrates. This gene encodes a deubiquitinating enzyme which lies in a gene cluster on chromosome Xp11.23 …

**Accessions** — [HGNC:12609](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12609) · Entrez [8237](https://www.ncbi.nlm.nih.gov/gene/8237) · UniProt [P51784](https://www.uniprot.org/uniprotkb/P51784) · Ensembl [ENSG00000102226](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102226)

## Data

Gene col 2229: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2229); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2229, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2229]; `tensor/DDL_lfc|DDL_z.npy` [2229]; `embed/gene_vectors.npy` [2229]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2229 or target_col == 2229). Every well: [[USP11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
