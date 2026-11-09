---
symbol: "NCKAP1"
type: "gene"
col: 701
ensembl_id: "ENSG00000061676"
name: "NCK associated protein 1"
location: "2q32.1"
module: 25
arm: "+"
pooled_cpm: 245.45
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# NCKAP1

*NCK associated protein 1* — 2q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.29× (z +13.0, q 8e-36, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.437× (z -13.0, q 8e-36, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBQLN1]] (+0.79, fdr 7e-06), [[RAD23B]] (+0.72, fdr 7e-06), [[TNPO1]] (+0.68, fdr 7e-06); moves opposite to [[DIABLO]] (-0.72, fdr 7e-06), [[ZKSCAN5]] (-0.66, fdr 7e-06), [[NOSIP]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 701.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.29×** | +13.0 | 8e-36 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +11.1 | 2e-26 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.87×** | +9.8 | 1e-20 | 46/48 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +9.6 | 9e-20 | 44/47 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.77×** | +8.9 | 5e-17 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.66×** | +8.0 | 1e-13 | 45/48 (NCI-H460, H4, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.67×** | +7.6 | 2e-12 | 45/48 (H4, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +7.0 | 1e-10 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.20×** | +6.5 | 7e-09 | 43/48 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.02×** | +5.8 | 4e-07 | 37/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +4.8 | 7e-05 | 41/45 (NCI-H1792, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.29×** | +4.0 | 0.003 | 33/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.27×** | +3.7 | 0.009 | 26/49 (NCI-H1792, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.040 | 29/49 (NCI-H460, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.045 | 26/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.1 | 0.063 | 15/49 (CFPAC-1, COLO 205, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 701.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.437×** | -13.0 | 8e-36 | 47/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.451×** | -12.5 | 2e-33 | 47/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.551×** | -9.4 | 1e-18 | 47/48 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.730×** | -7.0 | 3e-10 | 38/49 (A549, BT-474, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.680×** | -5.8 | 6e-07 | 41/47 (HepG2/C3A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.699×** | -5.6 | 2e-06 | 40/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.809×** | -3.3 | 0.070 | 29/48 (AsPC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.811×** | -3.3 | 0.071 | 27/48 (BT-474, A549, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.815×** | -3.2 | 0.081 | 27/48 (A549, SK-MEL-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.821× | -3.1 | 0.11 | 25/48 (NCI-H2347, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 701. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 265 | 10 (2 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 5.23× (z +20.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.05× (z +19.7) | [[Panobinostat (drug)]] 0.5 µM 0.395× (z -11.3) |
| [[SW480 (line)]] | alt | 208 | 9 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +18.3) | [[Panobinostat (drug)]] 5 µM 0.333× (z -17.4) |
| [[H4 (line)]] | wt | 206 | 9 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.15× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.403× (z -8.9) |
| [[BT-474 (line)]] | alt | 223 | 4 (1 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.240× (z -18.6) |
| [[LoVo (line)]] | wt | 225 | 6 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +14.5) | [[Panobinostat (drug)]] 5 µM 0.399× (z -11.7) |
| [[PANC-1 (line)]] | alt | 223 | 6 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.64× (z +17.6) | [[Panobinostat (drug)]] 5 µM 0.475× (z -10.2) |
| [[COLO 205 (line)]] | alt | 143 | 7 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.83× (z +16.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.25× (z +13.0) | — |
| [[HOP62 (line)]] | alt | 203 | 5 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.367× (z -12.3) |
| [[KATO III (line)]] | alt | 170 | 4 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.15× (z +18.0) | [[Panobinostat (drug)]] 5 µM 0.382× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 270 | 3 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -12.8) |
| [[NCI-H1573 (line)]] | alt | 279 | 4 (2 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.98× (z +13.4) | [[Panobinostat (drug)]] 0.5 µM 0.312× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 234 | 5 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.452× (z -9.7) |
| [[Hs 766T (line)]] | wt | 175 | 3 (2 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.433× (z -9.5) |
| [[LS 180 (line)]] | wt | 235 | 3 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.68× (z +13.7) | [[Panobinostat (drug)]] 0.5 µM 0.340× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 168 | 5 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.09× (z +11.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +11.0) | — |
| [[A549 (line)]] | wt | 235 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -15.5) |
| [[HepG2_C3A (line)]] | wt | 249 | 2 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.406× (z -9.4) |
| [[RKO (line)]] | wt | 324 | 2 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -9.9) |
| [[SW 900 (line)]] | alt | 187 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +11.2) | — |
| [[SW1417 (line)]] | alt | 334 | 2 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.399× (z -10.4) |
| [[HS-578T (line)]] | alt | 214 | 1 | 2 | [[Ixazomib citrate (drug)]] 5 µM 2.30× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.417× (z -9.6) |
| [[HT-29 (line)]] | alt | 251 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.489× (z -8.7) |
| [[J82 (line)]] | alt | 252 | 1 | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.372× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 250 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.286× (z -14.6) |
| [[SHP-77 (line)]] | alt | 217 | 2 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.97× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.424× (z -9.2) |
| [[SW48 (line)]] | wt | 297 | 2 | 1 | [[TAK-901 (drug)]] 0.05 µM 3.09× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.380× (z -8.6) |
| [[C32 (line)]] | wt | 195 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.15× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 215 | 1 | 1 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.96× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.418× (z -8.5) |
| [[HCT15 (line)]] | alt | 223 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.62× (z +10.1) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.30× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 293 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 232 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.403× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 358 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.370× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 242 | 1 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.22× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.440× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 326 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.330× (z -13.3) |
| [[SK-MEL-2 (line)]] | alt | 240 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.426× (z -10.6) |
| [[SNU-423 (line)]] | alt | 230 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.388× (z -10.6) |
| [[A-172 (line)]] | wt | 264 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.423× (z -10.7) |
| [[A-427 (line)]] | wt | 214 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 254 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.447× (z -9.2) |
| [[AN3 CA (line)]] | alt | 275 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 243 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.71× (z +9.7) | — |
| [[SNU-1 (line)]] | wt | 376 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.387× (z -8.9) |
| [[C-33 A (line)]] | alt | 215 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 190 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 343 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 283 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 270 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 427 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 224 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 701), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBQLN1]] | +0.79 | +0.76 / +0.84 | both halves | 7e-06 |  |
| [[RAD23B]] | +0.72 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[TNPO1]] | +0.68 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[FECH]] | +0.66 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[NAA50]] | +0.65 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[MAPK9]] | +0.65 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[SGPL1]] | +0.65 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[NAE1]] | +0.64 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[GSR]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ATL3]] | +0.64 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[ARPP19]] | +0.63 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[EMB]] | +0.63 | +0.51 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIABLO]] | -0.72 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[ZKSCAN5]] | -0.66 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[NOSIP]] | -0.65 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[ISG20L2]] | -0.64 | -0.61 / -0.70 | both halves | 7e-06 |  |
| [[MFAP1]] | -0.64 | -0.72 / -0.66 | both halves | 7e-06 |  |
| [[BLZF1]] | -0.61 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[ATG101]] | -0.60 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[DNTTIP1]] | -0.60 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[SPTY2D1]] | -0.60 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[ZNF324]] | -0.60 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[INAFM1]] | -0.59 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[DDX50]] | -0.59 | -0.53 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises NCKAP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.678). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-26.5, -15.7); signed map (-15.9, -41.5). **Vector** length 115, 51.9% of its response variance represented; |z| ≥ 3 in 1,207 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +12.5 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +11.7 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +9.9 | +2.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +8.1 | +1.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.5 | +9.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.7 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.6 | +8.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.1 | +2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +4.1 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +0.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -0.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.8 | +5.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.3 | -12.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.9 | -0.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.5 | -0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -2.8 |
|  | [[Vilanterol (drug)]] 5 µM |  | -2.4 | -1.0 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -2.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | NCK associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.1 — chr2:182,909,115-183,038,858 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Nap1, HEM2, NAP125 |
| Gene groups (HGNC) | SCAR/WAVE complex |
| Reactome | 19 pathways, smallest: RHO GTPases Activate WASPs and WAVEs; FCGR3A-mediated phagocytosis; Leishmania phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2A7](https://www.uniprot.org/uniprotkb/Q9Y2A7) (Nck-associated protein 1):

> Part of the WAVE complex that regulates lamellipodia formation. The WAVE complex regulates actin filament reorganization via its interaction with the Arp2/3 complex. Actin remodeling activity is regulated by RAC1. As component of the WAVE1 complex, required for BDNF-NTRK2 endocytic trafficking and signaling from early endosomes.

**Summary**, from NCBI Gene [10787](https://www.ncbi.nlm.nih.gov/gene/10787):

> Contributes to small GTPase binding activity. Involved in Rac protein signal transduction; positive regulation of Arp2/3 complex-mediated actin nucleation; and positive regulation of lamellipodium assembly. Located in extracellular exosome and focal adhesion. Part of SCAR complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7666](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7666) · Entrez [10787](https://www.ncbi.nlm.nih.gov/gene/10787) · UniProt [Q9Y2A7](https://www.uniprot.org/uniprotkb/Q9Y2A7) · Ensembl [ENSG00000061676](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000061676)

## Data

Gene col 701: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 701); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 701, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 701]; `tensor/DDL_lfc|DDL_z.npy` [701]; `embed/gene_vectors.npy` [701]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 701 or target_col == 701). Every well: [[NCKAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCKAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
