---
symbol: "ZNF354A"
type: "gene"
col: 9759
ensembl_id: "ENSG00000169131"
name: "zinc finger protein 354A"
location: "5q35.3"
module: 1
arm: "+"
pooled_cpm: 19.19
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 9
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# ZNF354A

*zinc finger protein 354A* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.92× (z +16.4, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.651× (z -7.7, q 1e-11, down in 27 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.655× (z -7.5, q 1e-11, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF354B]] (+0.68, fdr 7e-06), [[ZSWIM7]] (+0.61, fdr 7e-06), [[MIOS]] (+0.60, fdr 1e-05); moves opposite to [[SLC39A9]] (-0.58, fdr 1e-05), [[MLEC]] (-0.58, fdr 1e-05), [[RELCH]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[KLKP1-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9759.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.92×** | +16.4 | 0e+00 | 41/48 (Panc 03.27, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.01×** | +12.4 | 6e-33 | 38/48 (Panc 03.27, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.90×** | +11.4 | 6e-28 | 27/41 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +10.5 | 2e-23 | 18/29 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.76×** | +9.7 | 3e-20 | 28/48 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +7.9 | 2e-13 | 29/43 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +7.2 | 6e-11 | 29/48 (Hs 766T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +6.6 | 4e-09 | 21/48 (SW1417, SW480, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.46×** | +6.2 | 3e-08 | 18/34 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.38×** | +5.8 | 4e-07 | 22/48 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.7 | 1e-04 | 1/48 (J82) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.29×** | +4.5 | 3e-04 | 16/47 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.19× | +4.5 | 3e-04 | 15/48 (A498, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +4.4 | 4e-04 | 18/47 (BT-474, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.27×** | +4.2 | 0.001 | 14/47 (Panc 03.27, J82, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.002 | 19/48 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +4.0 | 0.002 | 14/48 (SNU-423, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.002 | 17/47 (Hs 766T, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.008 | 14/47 (NCI-H23, COLO 205, …) | top dose only |  |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.009 | 8/47 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.011 | 9/47 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9759.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.651×** | -7.7 | 1e-11 | 27/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.655×** | -7.5 | 1e-11 | 27/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.508×** | -6.3 | 5e-08 | 25/48 (A498, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.552×** | -5.5 | 4e-06 | 25/47 (LOX-IMVI, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.740×** | -5.4 | 9e-06 | 19/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.737×** | -5.2 | 1e-05 | 20/48 (SK-MEL-2, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.825×** | -4.9 | 1e-04 | 21/48 (A-427, MIA PaCa-2, …) | top dose only |  |
| [[crizotinib (drug)]] 5 µM |  | **0.807×** | -3.7 | 0.017 | 9/48 (SW1417, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.812×** | -3.6 | 0.022 | 18/47 (SNU-423, SK-MEL-2, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.882× | -3.2 | 0.081 | 7/48 (RKO, SNU-1, …) | rises with dose | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.838× | -3.2 | 0.081 | 8/47 (HOP62, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.841× | -3.1 | 0.095 | 13/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | 0.724× | -3.0 | 0.11 | 15/44 (HS-578T, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9759. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 31.2 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.3× (z +25.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 14.3 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.187× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -10.5) |
| [[PANC-1 (line)]] | alt | 36.2 | 3 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +12.1) | [[Digitoxin (drug)]] 5 µM 0.451× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.454× (z -9.6) |
| [[SW 900 (line)]] | alt | 27.8 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.3× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.49× (z +13.8) | — |
| [[CFPAC-1 (line)]] | alt | 8.77 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.7× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 5.99× (z +12.1) | — |
| [[Panc 03.27 (line)]] | alt | 41.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +15.0) | — |
| [[SK-MEL-2 (line)]] | alt | 47.0 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -11.5) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -8.9) |
| [[SNU-423 (line)]] | alt | 21.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +12.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -11.6) ⚠ cell-cycle shift, explains ~23% of this change |
| [[HOP62 (line)]] | alt | 15.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.47× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.69× (z +9.3) | — |
| [[SW480 (line)]] | alt | 11.0 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.227× (z -11.1) |
| [[A-172 (line)]] | wt | 5.66 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.124× (z -8.7) |
| [[A-427 (line)]] | wt | 41.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -9.4) ⚠ cell-cycle shift, explains ~23% of this change |
| [[A498 (line)]] | wt | 12.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.79× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -9.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 10.6 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.0966× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 11.7 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0951× (z -10.0) |
| [[Hs 766T (line)]] | wt | 16.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +11.2) | — |
| [[hTERT-HPNE (line)]] | wt | 10.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0989× (z -8.8) |
| [[J82 (line)]] | alt | 20.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +11.6) | — |
| [[KATO III (line)]] | alt | 9.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.192× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -9.8) ⚠ cell-cycle shift, explains ~23% of this change |
| [[NCI-H2347 (line)]] | alt | 14.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 15.4 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0801× (z -13.7) |
| [[AN3 CA (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.12 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9759), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF354B]] | +0.68 | +0.71 / +0.72 | both halves | 7e-06 | same gene group |
| [[ZSWIM7]] | +0.61 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[MIOS]] | +0.60 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[TYW5]] | +0.60 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[ZNF197]] | +0.59 | +0.73 / +0.53 | both halves | 1e-05 | same gene group |
| [[PEX1]] | +0.58 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[MAP7D3]] | +0.58 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[TATDN1]] | +0.58 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[POGK]] | +0.58 | +0.53 / +0.52 | both halves | 1e-05 | same gene group |
| [[COA7]] | +0.57 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[HUS1]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[NT5C]] | +0.56 | +0.69 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC39A9]] | -0.58 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[MLEC]] | -0.58 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[RELCH]] | -0.55 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[SAR1A]] | -0.55 | -0.68 / -0.48 | both halves | 2e-05 |  |
| [[ATP5PF]] | -0.54 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[RPN2]] | -0.54 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[TMED4]] | -0.53 | -0.66 / -0.46 | both halves | 2e-05 |  |
| [[TPI1]] | -0.53 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[SNHG30]] | -0.53 | -0.62 / -0.36 | both halves | 1e-04 |  |
| [[EED]] | -0.53 | -0.56 / -0.40 | both halves | 5e-05 | pathway: Epigenetic regulation of gene expression |
| [[CA5BP1]] | -0.52 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[DDOST]] | -0.52 | -0.61 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLKP1-1]] | B | KLKP1-1 activity lowers ZNF354A's level | lines that do not express KLKP1-1 (11) vs lines expressing it (39) | 1.45× higher at baseline in the lines without KLKP1-1 | 0.048 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, ENSG00000286263, MILR1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises ZNF354A's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CA9]] | B | CA9 activity lowers ZNF354A's level | lines that do not express CA9 (19) vs lines expressing it (31) | 1.50× higher at baseline in the lines without CA9 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.493). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-29.0, 4.4); signed map (4.5, -23.7). **Vector** length 91.4, 18.9% of its response variance represented; |z| ≥ 3 in 1,011 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.0 | +16.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.8 | +12.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.4 | +9.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +11.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.4 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.3 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +3.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.8 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +6.6 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -5.3 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -4.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.8 | -6.3 |
|  | [[NG25 (drug)]] 5 µM |  | -2.7 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -5.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.8 | -0.9 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 354A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:178,711,512-178,730,659 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KID-1, EZNF, HKL1, KID1; previously TCF17 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Reactome | 3 pathways, smallest: Regulation of endogenous retroelements by KRAB-ZFP proteins; Regulation of endogenous retroelements; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

UniProt [O60765](https://www.uniprot.org/uniprotkb/O60765) carries no function annotation.

**Summary**, from NCBI Gene [6940](https://www.ncbi.nlm.nih.gov/gene/6940):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Located in nucleolus and nucleoplasm. Biomarker of in situ carcinoma and seminoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11628](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11628) · Entrez [6940](https://www.ncbi.nlm.nih.gov/gene/6940) · UniProt [O60765](https://www.uniprot.org/uniprotkb/O60765) · Ensembl [ENSG00000169131](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169131)

## Data

Gene col 9759: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9759); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9759, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9759]; `tensor/DDL_lfc|DDL_z.npy` [9759]; `embed/gene_vectors.npy` [9759]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9759 or target_col == 9759). Every well: [[ZNF354A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF354A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
