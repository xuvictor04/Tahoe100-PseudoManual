---
symbol: "ZZZ3"
type: "gene"
col: 438
ensembl_id: "ENSG00000036549"
name: "zinc finger ZZ-type containing 3"
location: "1p31.1"
module: 1
arm: "+"
pooled_cpm: 150.96
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# ZZZ3

*zinc finger ZZ-type containing 3* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 2.08× (z +5.7, q 6e-06, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.574× (z -15.3, q 0e+00, down in 48 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METAP1D]] (+0.76, fdr 7e-06), [[ACBD6]] (+0.74, fdr 7e-06), [[RBM26]] (+0.71, fdr 1e-05); moves opposite to [[MXD1]] (-0.66, fdr 1e-05), [[PNPLA8]] (-0.63, fdr 4e-05), [[SERINC2]] (-0.59, fdr 6e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 438.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **2.08×** | +5.7 | 6e-06 | 34/48 (C32, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.93×** | +5.1 | 8e-05 | 36/49 (COLO 205, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +4.6 | 9e-04 | 31/48 (AsPC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.019 | 32/48 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | 1.18× | +3.3 | 0.12 | 16/48 (A498, HS-578T, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.2 | 0.12 | 0/50 | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.2 | 0.12 | 18/48 (NCI-H2030, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.14 | 21/48 (NCI-H1573, NCI-H2030, …) | rises with dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 438.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.574×** | -15.3 | 0e+00 | 48/49 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.516×** | -12.9 | 2e-35 | 46/48 (SW480, SNU-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.519×** | -12.7 | 7e-35 | 46/49 (PANC-1, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.539×** | -12.0 | 4e-31 | 43/48 (SK-MEL-2, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.539×** | -12.0 | 4e-31 | 44/48 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.560×** | -10.8 | 2e-25 | 38/44 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.586×** | -10.4 | 2e-23 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.590×** | -9.5 | 2e-19 | 35/45 (HEC-1-A, C32, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.672×** | -7.4 | 7e-12 | 37/48 (LOX-IMVI, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.678×** | -7.3 | 2e-11 | 36/50 (MIA PaCa-2, C32, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.709×** | -6.7 | 1e-09 | 41/48 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.709×** | -6.7 | 1e-09 | 41/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 0.850× | -4.5 | 3e-04 | 25/48 (SW 900, SW480, …) | top dose only | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.806×** | -4.0 | 0.002 | 27/47 (MIA PaCa-2, RKO, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **0.817×** | -3.9 | 0.003 | 29/48 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.824×** | -3.8 | 0.006 | 26/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.877× | -3.6 | 0.011 | 18/48 (HOP62, SNU-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.844× | -3.3 | 0.031 | 19/48 (SW48, AN3 CA, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.892× | -3.2 | 0.048 | 16/48 (SW 900, NCI-H460, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.855× | -3.0 | 0.066 | 15/47 (LS 180, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 438. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 230 | 0 | 11 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.349× (z -13.3) ⚠ toxic; cell-cycle shift, explains ~27% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -12.9) |
| [[SW480 (line)]] | alt | 202 | 0 | 11 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -16.1) |
| [[NCI-H2030 (line)]] | alt | 157 | 2 (2 ⚠) | 8 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.332× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 196 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -14.8) |
| [[LOX-IMVI (line)]] | wt | 190 | 1 | 7 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.01× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -13.8) |
| [[PANC-1 (line)]] | alt | 197 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.349× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -14.3) |
| [[C32 (line)]] | wt | 154 | 0 | 7 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.272× (z -15.5) |
| [[LoVo (line)]] | wt | 163 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 174 | 0 | 6 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.196× (z -19.6) |
| [[C-33 A (line)]] | alt | 180 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -9.6) |
| [[LS 180 (line)]] | wt | 189 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.615× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 121 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -12.2) |
| [[RKO (line)]] | wt | 196 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -15.9) |
| [[SNU-423 (line)]] | alt | 138 | 0 | 5 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -12.0) |
| [[H4 (line)]] | wt | 119 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -11.8) |
| [[SNU-1 (line)]] | wt | 182 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.258× (z -14.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.303× (z -12.4) |
| [[SW48 (line)]] | wt | 153 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.58× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -10.8) |
| [[A-427 (line)]] | wt | 132 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.426× (z -11.1) |
| [[A549 (line)]] | wt | 98.0 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -16.9) |
| [[HOP62 (line)]] | alt | 110 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.362× (z -13.1) |
| [[HT-29 (line)]] | alt | 159 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.365× (z -12.5) |
| [[NCI-H23 (line)]] | alt | 203 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.438× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 194 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.364× (z -11.9) |
| [[SW 900 (line)]] | alt | 131 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -11.4) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.446× (z -10.0) |
| [[SW1417 (line)]] | alt | 71.6 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.356× (z -11.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.403× (z -10.3) |
| [[A-172 (line)]] | wt | 76.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -11.4) |
| [[A498 (line)]] | wt | 143 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -16.4) |
| [[AN3 CA (line)]] | alt | 198 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -8.8) |
| [[HCT15 (line)]] | alt | 215 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.315× (z -12.4) |
| [[hTERT-HPNE (line)]] | wt | 125 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -10.2) |
| [[J82 (line)]] | alt | 152 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -13.0) |
| [[NCI-H1792 (line)]] | alt | 162 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.349× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H2347 (line)]] | alt | 113 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +8.7) ⚠ cell-cycle shift, explains ~69% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 146 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.114× (z -10.5) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 87.0 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.451× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 151 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.399× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HS-578T (line)]] | alt | 179 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.600× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 127 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[BT-474 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 132 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 120 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 438), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METAP1D]] | +0.76 | +0.62 / +0.76 | both halves | 7e-06 |  |
| [[ACBD6]] | +0.74 | +0.58 / +0.76 | both halves | 7e-06 |  |
| [[RBM26]] | +0.71 | +0.50 / +0.79 | both halves | 1e-05 |  |
| [[TGFBRAP1]] | +0.70 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[USP24]] | +0.68 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[LTV1]] | +0.67 | +0.48 / +0.72 | both halves | 2e-05 |  |
| [[PUM2]] | +0.67 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[MTPAP]] | +0.67 | +0.44 / +0.71 | both halves | 3e-05 |  |
| [[DUS3L]] | +0.65 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[MDN1]] | +0.65 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[MRRF]] | +0.65 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[LUC7L2]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXD1]] | -0.66 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[PNPLA8]] | -0.63 | -0.42 / -0.70 | both halves | 4e-05 |  |
| [[SERINC2]] | -0.59 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[CCNYL1]] | -0.58 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[TMEM184B]] | -0.57 | -0.33 / -0.62 | both halves | 1e-04 |  |
| [[GIPR]] | -0.57 | -0.39 / -0.58 | both halves | 5e-05 |  |
| [[F11R]] | -0.56 | -0.30 / -0.61 | both halves | 2e-04 |  |
| [[CIB1]] | -0.56 | -0.36 / -0.55 | both halves | 9e-05 |  |
| [[ULBP2]] | -0.55 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[SELENOK]] | -0.55 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[MYO9B]] | -0.54 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[PTPRH]] | -0.54 | -0.37 / -0.56 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ZZZ3's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SERINC2]] | B | SERINC2 activity lowers ZZZ3's level | lines that do not express SERINC2 (6) vs lines expressing it (44) | 1.19× higher at baseline in the lines without SERINC2 | 0.074 | ⚠ within organs, on part of the lines; also absent: SLC9A3, TESK2, LITAF |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.660). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.7, 3.1); signed map (5.6, -40.0). **Vector** length 104, 35.6% of its response variance represented; |z| ≥ 3 in 1,094 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | +2.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.4 | +4.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.6 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.6 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +5.7 |
|  | [[EX229 (drug)]] 5 µM |  | +3.9 | +1.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.8 | +1.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.3 | -12.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.5 | -6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -15.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -4.2 | -0.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.4 | -6.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.4 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -2.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger ZZ-type containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:77,562,416-77,683,419 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564I052, ATAC1 |
| Gene groups (HGNC) | Zinc fingers ZZ-type; Myb/SANT domain containing; ATAC complex |
| Reactome | 6 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; HATs acetylate histones; Epigenetic regulation by WDR5-containing histone modifying complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYH5](https://www.uniprot.org/uniprotkb/Q8IYH5) (ZZ-type zinc finger-containing protein 3):

> Histone H3 reader that is required for the ATAC complex-mediated maintenance of histone acetylation and gene activation. Component of the ATAC complex, a complex with histone acetyltransferase activity on histones H3 and H4.

**Summary**, from NCBI Gene [26009](https://www.ncbi.nlm.nih.gov/gene/26009):

> Enables histone binding activity. Involved in several processes, including regulation of cell division; regulation of transcription by RNA polymerase II; and regulation of tubulin deacetylation. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24523](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24523) · Entrez [26009](https://www.ncbi.nlm.nih.gov/gene/26009) · UniProt [Q8IYH5](https://www.uniprot.org/uniprotkb/Q8IYH5) · Ensembl [ENSG00000036549](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000036549)

## Data

Gene col 438: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 438); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 438, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 438]; `tensor/DDL_lfc|DDL_z.npy` [438]; `embed/gene_vectors.npy` [438]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 438 or target_col == 438). Every well: [[ZZZ3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZZZ3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
