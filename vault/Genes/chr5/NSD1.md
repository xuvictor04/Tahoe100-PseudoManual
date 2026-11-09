---
symbol: "NSD1"
type: "gene"
col: 9162
ensembl_id: "ENSG00000165671"
name: "nuclear receptor binding SET domain protein 1"
location: "5q35.3"
module: 194
arm: "+"
pooled_cpm: 140.0
n_lines_expressing: 48
n_dd_up: 5
n_dd_down: 19
n_dd_up_clean: 5
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/194"]
generated_by: "tahoemap"
---

# NSD1

*nuclear receptor binding SET domain protein 1* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 1.41× (z +6.5, q 4e-08, up in 39 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.255× (z -25.6, q 0e+00, down in 46 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED1]] (+0.73, fdr 7e-06), [[ZMYND11]] (+0.72, fdr 1e-05), [[ZNF532]] (+0.71, fdr 7e-06); moves opposite to [[ASMTL]] (-0.64, fdr 2e-05), [[FCHO1]] (-0.63, fdr 4e-05), [[RADX]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 194]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PRDM5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9162.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +6.5 | 4e-08 | 39/46 (RKO, H4, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.34×** | +5.6 | 7e-06 | 34/46 (HEC-1-A, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +5.3 | 2e-05 | 26/46 (RKO, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.23×** | +3.9 | 0.014 | 22/46 (RKO, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.14× | +3.6 | 0.034 | 17/46 (LoVo, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.039 | 27/45 (H4, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 1.18× | +3.1 | 0.18 | 17/46 (HOP62, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9162.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.255×** | -25.6 | 0e+00 | 46/46 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.261×** | -25.2 | 0e+00 | 46/46 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.262×** | -25.1 | 0e+00 | 46/46 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.489×** | -13.4 | 7e-39 | 46/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.592×** | -9.8 | 1e-20 | 44/46 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.717×** | -8.8 | 1e-16 | 42/46 (SW480, LoVo, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.450×** | -7.8 | 4e-13 | 43/47 (SK-MEL-2, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.749×** | -7.6 | 2e-12 | 28/46 (J82, NCI-H460, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.670×** | -7.5 | 4e-12 | 42/47 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.684×** | -7.1 | 7e-11 | 29/46 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.686×** | -6.5 | 3e-09 | 26/43 (NCI-H23, NCI-H460, …) | inconsistent across doses | composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.602×** | -5.0 | 3e-05 | 35/46 (SW480, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.759×** | -4.9 | 3e-05 | 27/45 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.923× | -4.5 | 3e-04 | 0/48 | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.651×** | -4.2 | 0.001 | 23/36 (Panc 03.27, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.832×** | -3.4 | 0.018 | 19/47 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.799×** | -3.0 | 0.075 | 21/46 (NCI-H661, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.800×** | -3.0 | 0.075 | 18/46 (HT-29, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.854× | -2.9 | 0.080 | 19/46 (NCI-H23, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9162. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 194 | 0 | 19 (12 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.208× (z -23.7) |
| [[LOX-IMVI (line)]] | wt | 173 | 0 | 11 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.194× (z -20.5) |
| [[SK-MEL-2 (line)]] | alt | 144 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -20.0) |
| [[C32 (line)]] | wt | 145 | 0 | 9 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.147× (z -24.0) |
| [[NCI-H23 (line)]] | alt | 218 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -28.8) |
| [[SW48 (line)]] | wt | 207 | 2 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.17× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.109× (z -24.5) |
| [[J82 (line)]] | alt | 175 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -21.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.257× (z -17.2) |
| [[LoVo (line)]] | wt | 188 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -31.3) |
| [[NCI-H1573 (line)]] | alt | 132 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.202× (z -16.5) |
| [[PANC-1 (line)]] | alt | 124 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.300× (z -16.3) |
| [[SW480 (line)]] | alt | 168 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -30.3) |
| [[A-427 (line)]] | wt | 193 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.184× (z -24.3) |
| [[BT-474 (line)]] | alt | 162 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.199× (z -17.9) |
| [[HOP62 (line)]] | alt | 103 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -18.1) |
| [[Panc 03.27 (line)]] | alt | 221 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.148× (z -24.3) |
| [[RKO (line)]] | wt | 148 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.23× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -16.7) |
| [[A-172 (line)]] | wt | 198 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.274× (z -17.9) |
| [[C-33 A (line)]] | alt | 175 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -18.8) |
| [[KATO III (line)]] | alt | 97.1 | 1 | 4 | [[Homoharringtonine (drug)]] 0.5 µM 2.12× (z +9.1) | [[Belinostat (drug)]] 5 µM 0.266× (z -16.1) |
| [[NCI-H1792 (line)]] | alt | 74.7 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.158× (z -18.1) |
| [[SNU-423 (line)]] | alt | 104 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.205× (z -16.0) |
| [[COLO 205 (line)]] | alt | 112 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -12.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.349× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 203 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.238× (z -22.2) |
| [[HT-29 (line)]] | alt | 117 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.284× (z -15.2) |
| [[MIA PaCa-2 (line)]] | alt | 217 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.137× (z -24.6) |
| [[SNU-1 (line)]] | wt | 205 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.364× (z -11.7) |
| [[SW1417 (line)]] | alt | 150 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -20.4) |
| [[A498 (line)]] | wt | 105 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.310× (z -13.1) |
| [[A549 (line)]] | wt | 104 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.198× (z -15.6) |
| [[AN3 CA (line)]] | alt | 218 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -13.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.287× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 84.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -10.8) |
| [[CHP-212 (line)]] | wt | 132 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.231× (z -10.7) |
| [[H4 (line)]] | wt | 159 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.419× (z -8.5) |
| [[HCT15 (line)]] | alt | 209 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -16.4) |
| [[Hs 766T (line)]] | wt | 88.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.219× (z -15.2) |
| [[HS-578T (line)]] | alt | 92.5 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.281× (z -13.2) |
| [[hTERT-HPNE (line)]] | wt | 76.8 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.182× (z -13.7) |
| [[LS 180 (line)]] | wt | 153 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.210× (z -21.2) |
| [[NCI-H2030 (line)]] | alt | 124 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.182× (z -15.8) |
| [[NCI-H2347 (line)]] | alt | 84.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.232× (z -15.9) |
| [[SW 900 (line)]] | alt | 158 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.194× (z -16.3) |
| [[AsPC-1 (line)]] | alt | 47.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.307× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 83.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.370× (z -8.8) |
| [[SW 1271 (line)]] | alt | 196 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -8.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HepG2_C3A (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 110 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9162), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED1]] | +0.73 | +0.68 / +0.61 | both halves | 7e-06 | STRING 423 |
| [[ZMYND11]] | +0.72 | +0.68 / +0.57 | both halves | 1e-05 | same gene group |
| [[ZNF532]] | +0.71 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CPSF2]] | +0.70 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ZNF629]] | +0.69 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[PRDM5]] | +0.68 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ZFP91]] | +0.68 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ZSCAN29]] | +0.68 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ZFX]] | +0.68 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[ZNF507]] | +0.67 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ASXL2]] | +0.66 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[FAIM]] | +0.66 | +0.56 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASMTL]] | -0.64 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[FCHO1]] | -0.63 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[RADX]] | -0.62 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[HSPB11]] | -0.62 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[AHDC1]] | -0.62 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[SLC27A1]] | -0.60 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[TMEM41B]] | -0.60 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[TBC1D10A]] | -0.60 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[CBLB]] | -0.59 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[ETHE1]] | -0.59 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[LTBP4]] | -0.59 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[AKR1A1]] | -0.58 | -0.59 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRDM5]] | B | PRDM5 activity raises NSD1's level | lines that do not express PRDM5 (13) vs lines expressing it (37) | 1.33× lower at baseline in the lines without PRDM5 | 0.089 | ⚠ within organs, on part of the lines; also absent: UBE2E2, JHY, SSPN |
| [[CHST3]] | C | CHST3 activity raises NSD1's level | lines that do not express CHST3 (4) vs lines expressing it (46) | 1.54× lower at baseline in the lines without CHST3 | 0.005 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HOMER3, RGS10, ENSG00000290876 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 194]]; 17 genes; this gene is in the **+** arm (projection on the module's main direction 0.792). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-6.0, 4.4); signed map (18.2, -29.7). **Vector** length 132, 46.9% of its response variance represented; |z| ≥ 3 in 1,248 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +10.6 | +6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +10.5 | +5.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +7.5 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.9 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +5.7 | +3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.3 | +5.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.7 | +2.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -10.5 | -8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -9.9 | -7.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -7.3 | -13.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.1 | -25.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.0 | -9.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -4.0 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.9 | -7.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.8 | -3.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor binding SET domain protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:177,131,830-177,300,213 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARA267, FLJ22263, KMT3B; previously STO |
| Gene groups (HGNC) | PHD finger proteins; Histone lysine methyltransferases; PWWP domain containing; SET domain containing |
| Reactome | 3 pathways, smallest: PKMTs methylate histone lysines; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96L73](https://www.uniprot.org/uniprotkb/Q96L73) (Histone-lysine N-methyltransferase, H3 lysine-36 specific):

> Histone methyltransferase that dimethylates Lys-36 of histone H3 (H3K36me2). Transcriptional intermediary factor capable of both negatively or positively influencing transcription, depending on the cellular context.

**Summary**, from NCBI Gene [64324](https://www.ncbi.nlm.nih.gov/gene/64324):

> This gene encodes a protein containing a SET domain, 2 LXXLL motifs, 3 nuclear translocation signals (NLSs), 4 plant homeodomain (PHD) finger regions, and a proline-rich region. The encoded protein enhances androgen receptor (AR) transactivation, and this enhancement can be increased further in the presence of other androgen receptor associated coregulators. This protein may act as a nucleus-localized, basic transcriptional factor and also as a bifunctional transcriptional regulator. Mutations …

**Accessions** — [HGNC:14234](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14234) · Entrez [64324](https://www.ncbi.nlm.nih.gov/gene/64324) · UniProt [Q96L73](https://www.uniprot.org/uniprotkb/Q96L73) · Ensembl [ENSG00000165671](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165671)

## Data

Gene col 9162: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9162); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9162, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9162]; `tensor/DDL_lfc|DDL_z.npy` [9162]; `embed/gene_vectors.npy` [9162]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9162 or target_col == 9162). Every well: [[NSD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
