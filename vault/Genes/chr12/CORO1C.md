---
symbol: "CORO1C"
type: "gene"
col: 3174
ensembl_id: "ENSG00000110880"
name: "coronin 1C"
location: "12q24.11"
module: 78
arm: "+"
pooled_cpm: 211.3
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 16
n_dd_up_clean: 9
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# CORO1C

*coronin 1C* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.36× (z +9.2, q 2e-17, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.598× (z -10.6, q 2e-23, down in 37 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGB1]] (+0.72, fdr 7e-06), [[ACTN1]] (+0.71, fdr 7e-06), [[TPM4]] (+0.70, fdr 7e-06); moves opposite to [[ZCCHC10]] (-0.68, fdr 7e-06), [[CCDC59]] (-0.66, fdr 1e-05), [[CHKB]] (-0.66, fdr 1e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3174.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.36×** | +9.2 | 2e-17 | 44/49 (PANC-1, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.43×** | +6.7 | 5e-09 | 39/48 (HOP62, A-172, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +5.6 | 5e-06 | 38/48 (KATO III, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.42×** | +5.1 | 5e-05 | 37/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.28×** | +5.0 | 5e-05 | 31/49 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.38×** | +4.7 | 3e-04 | 41/48 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +4.7 | 3e-04 | 35/48 (PANC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.36×** | +4.4 | 7e-04 | 29/48 (KATO III, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.3 | 1e-03 | 28/48 (A-172, KATO III, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +3.9 | 0.004 | 30/48 (Hs 766T, Panc 03.27, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.9 | 0.005 | 24/38 (NCI-H1573, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.29×** | +3.7 | 0.011 | 31/48 (NCI-H460, PANC-1, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.26×** | +3.3 | 0.046 | 26/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.25×** | +3.2 | 0.048 | 26/48 (KATO III, A-172, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.26×** | +3.2 | 0.059 | 28/47 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.072 | 26/49 (HOP62, NCI-H1573, …) | top dose only | plate-row cell shift |
| [[Peretinoin (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.099 | 22/47 (NCI-H1573, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3174.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.598×** | -10.6 | 2e-23 | 37/49 (RKO, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.551×** | -8.3 | 2e-14 | 41/47 (RKO, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.751×** | -4.2 | 0.006 | 29/48 (RKO, H4, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.820×** | -4.1 | 0.006 | 26/48 (A549, NCI-H2030, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.752×** | -4.0 | 0.006 | 29/48 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.801×** | -4.0 | 0.006 | 24/48 (NCI-H23, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.829×** | -3.8 | 0.014 | 26/49 (CFPAC-1, NCI-H2347, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 5 µM |  | **0.781×** | -3.5 | 0.036 | 32/48 (NCI-H23, HEC-1-A, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.819×** | -3.4 | 0.040 | 23/48 (NCI-H23, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.793×** | -3.4 | 0.040 | 26/48 (A549, BT-474, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.850× | -3.4 | 0.041 | 17/48 (hTERT-HPNE, LoVo, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.735×** | -3.2 | 0.063 | 28/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.805×** | -3.2 | 0.066 | 25/48 (RPMI-7951, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.810×** | -3.1 | 0.079 | 26/48 (H4, SW 1088, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.744×** | -3.1 | 0.079 | 25/48 (HCT15, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.806×** | -3.0 | 0.088 | 28/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.816×** | -3.0 | 0.097 | 24/48 (RKO, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3174. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 107 | 8 (3 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 3.13× (z +14.5) | — |
| [[NCI-H460 (line)]] | wt | 179 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +11.1) | — |
| [[PANC-1 (line)]] | alt | 133 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.37× (z +13.3) | — |
| [[A-172 (line)]] | wt | 172 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 5.08× (z +9.2) | — |
| [[A-427 (line)]] | wt | 86.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.41× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 290 | 2 | 1 | [[PH-797804 (drug)]] 5 µM 6.54× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -15.1) |
| [[KATO III (line)]] | alt | 105 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.10× (z +11.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.75× (z +10.4) | — |
| [[SK-MEL-2 (line)]] | alt | 257 | 2 (2 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.27× (z +8.9) ⚠ toxic; cell-cycle shift, explains ~25% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -10.3) |
| [[A549 (line)]] | wt | 278 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 6.36× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -11.9) |
| [[C32 (line)]] | wt | 181 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.27× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 142 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 12.6× (z +13.0) | — |
| [[LoVo (line)]] | wt | 225 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.354× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 81.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 553 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -16.0) |
| [[SNU-423 (line)]] | alt | 263 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.31× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -8.8) |
| [[SW 900 (line)]] | alt | 236 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -9.0) |
| [[SW48 (line)]] | wt | 218 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -14.3) |
| [[A498 (line)]] | wt | 220 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 553 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -9.9) |
| [[C-33 A (line)]] | alt | 81.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | — |
| [[COLO 205 (line)]] | alt | 168 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 198 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -10.3) |
| [[HS-578T (line)]] | alt | 189 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -9.2) |
| [[J82 (line)]] | alt | 287 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 208 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.57× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 218 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -13.3) |
| [[RPMI-7951 (line)]] | alt | 259 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -12.2) |
| [[SHP-77 (line)]] | alt | 157 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -8.7) |
| [[SNU-1 (line)]] | wt | 249 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.326× (z -9.9) ⚠ toxic |
| [[SW1417 (line)]] | alt | 197 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.369× (z -10.5) ⚠ toxic |
| [[SW480 (line)]] | alt | 198 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.590× (z -9.2) |
| [[AN3 CA (line)]] | alt | 190 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 99.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 157 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 262 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 260 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 243 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 414 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 179 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 183 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3174), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGB1]] | +0.72 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[ACTN1]] | +0.71 | +0.72 / +0.68 | both halves | 7e-06 | STRING 529 |
| [[TPM4]] | +0.70 | +0.72 / +0.63 | both halves | 7e-06 | STRING 423 |
| [[MYH9]] | +0.69 | +0.56 / +0.72 | both halves | 1e-05 | STRING 404 |
| [[ACTN4]] | +0.67 | +0.59 / +0.68 | both halves | 7e-06 | STRING 563 |
| [[MICAL2]] | +0.65 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[CSRP1]] | +0.65 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[COTL1]] | +0.63 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[MSN]] | +0.63 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[ACTB]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 | STRING 698 |
| [[MIR222HG]] | +0.62 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[MACF1]] | +0.61 | +0.57 / +0.65 | both halves | 9e-06 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCCHC10]] | -0.68 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[CCDC59]] | -0.66 | -0.69 / -0.54 | both halves | 1e-05 |  |
| [[CHKB]] | -0.66 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[BTN2A1]] | -0.65 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[TMEM101]] | -0.65 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[TERF2IP]] | -0.64 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[LRRC37B]] | -0.64 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[RNF135]] | -0.64 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[GTF2IRD2B]] | -0.63 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[HOXA5]] | -0.63 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[RBM5]] | -0.62 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[WHAMM]] | -0.61 | -0.51 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CORO1C's level | compounds that target TOP2A: 3 of 5 lower it (Amsacrine, Doxorubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.758). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.4, 25.4); signed map (-7.7, 35.5). **Vector** length 138, 51.0% of its response variance represented; |z| ≥ 3 in 1,375 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *apical junction* (hallmark, mean cos +0.56 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +10.5 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +10.2 | +2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +9.6 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.8 | +4.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.9 | +5.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.2 | +5.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.0 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.4 | +2.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.1 | +2.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.4 | -8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -10.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -4.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.5 | -2.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.4 | -4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -3.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | coronin 1C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:108,645,109-108,731,526 (-) |
| Ensembl biotype | protein_coding |
| Also known as | coronin-3, HCRNN4 |
| Gene groups (HGNC) | WD repeat domain containing; Coronins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULV4](https://www.uniprot.org/uniprotkb/Q9ULV4) (Coronin-1C):

> Plays a role in directed cell migration by regulating the activation and subcellular location of RAC1. Increases the presence of activated RAC1 at the leading edge of migrating cells. Required for normal organization of the cytoskeleton, including the actin cytoskeleton, microtubules and the vimentin intermediate filaments (By similarity). Plays a role in endoplasmic reticulum-associated endosome fission: localizes to endosome membrane tubules and promotes recruitment of TMCC1, leading to …

**Summary**, from NCBI Gene [23603](https://www.ncbi.nlm.nih.gov/gene/23603):

> This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. Three transcript variants encoding two different isoforms have been found for …

**Accessions** — [HGNC:2254](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2254) · Entrez [23603](https://www.ncbi.nlm.nih.gov/gene/23603) · UniProt [Q9ULV4](https://www.uniprot.org/uniprotkb/Q9ULV4) · Ensembl [ENSG00000110880](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110880)

## Data

Gene col 3174: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3174); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3174, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3174]; `tensor/DDL_lfc|DDL_z.npy` [3174]; `embed/gene_vectors.npy` [3174]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3174 or target_col == 3174). Every well: [[CORO1C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CORO1C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
