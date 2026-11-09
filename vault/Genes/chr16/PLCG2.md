---
symbol: "PLCG2"
type: "gene"
col: 12493
ensembl_id: "ENSG00000197943"
name: "phospholipase C gamma 2"
location: "16q24.1"
module: 115
arm: "+"
pooled_cpm: 22.87
n_lines_expressing: 40
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# PLCG2

*phospholipase C gamma 2* — 16q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.94× (z +22.7, q 0e+00, up in 37 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.484× (z -6.3, q 2e-07, down in 17 of 38 measured lines).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DOP1B]] (+0.58, fdr 3e-05), [[MLXIPL]] (+0.54, fdr 5e-05), [[SGSM1]] (+0.53, fdr 2e-04); moves opposite to [[SCGB2B2]] (-0.55, fdr 2e-04), [[WDR33]] (-0.51, fdr 1e-04), [[PNISR-AS1]] (-0.50, fdr 0.001, ⚠ one half only (not replicated)), [[DNAAF10]] (-0.49, fdr 3e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ARHGEF4]] → it (grade B ⚠); 6 go from it, the strongest it → [[PRR5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12493.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.94×** | +22.7 | 0e+00 | 37/38 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.00×** | +18.2 | 0e+00 | 36/38 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.44×** | +14.8 | 0e+00 | 32/38 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +10.8 | 8e-25 | 30/38 (SW480, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +8.3 | 1e-14 | 29/38 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +7.5 | 7e-12 | 20/37 (NCI-H2030, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.26×** | +7.1 | 1e-10 | 25/38 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.10×** | +6.4 | 8e-09 | 15/31 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +5.8 | 3e-07 | 21/38 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +4.9 | 5e-05 | 17/38 (J82, HOP62, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.014 | 10/38 (NCI-H460, AsPC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.26×** | +3.6 | 0.016 | 14/38 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.16× | +3.5 | 0.018 | 9/38 (NCI-H1573, A-427, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.23×** | +3.5 | 0.018 | 6/38 (SW480, NCI-H1573, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.020 | 5/38 (SW1417, PANC-1, …) | top dose only | plate-row cell shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.062 | 12/38 (LoVo, J82, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.062 | 10/38 (MIA PaCa-2, A498, …) | top dose only |  |
| [[Encorafenib (drug)]] 5 µM |  | **1.41×** | +3.0 | 0.083 | 4/38 (NCI-H2030, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12493.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.484×** | -6.3 | 2e-07 | 17/38 (MIA PaCa-2, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.705×** | -5.8 | 2e-06 | 21/38 (SK-MEL-2, RKO, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **0.757×** | -4.4 | 0.002 | 13/38 (COLO 205, AN3 CA, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.778×** | -4.1 | 0.005 | 17/38 (A549, KATO III, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.791×** | -3.9 | 0.012 | 16/38 (LoVo, A-172, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.660×** | -3.6 | 0.031 | 12/38 (SK-MEL-2, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | 0.761× | -3.2 | 0.11 | 10/38 (Hs 766T, LS 180, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | 0.815× | -3.1 | 0.11 | 13/27 (SW480, A-427, …) | inconsistent across doses | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~95% of this change | 0.828× | -3.1 | 0.11 | 14/35 (HEC-1-A, BT-474, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12493. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 19.8 | 6 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 7.06× (z +17.9) | [[Dinaciclib (drug)]] 0.05 µM 0.256× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[NCI-H2030 (line)]] | alt | 54.4 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.78× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -9.9) ⚠ cell-cycle shift, explains ~78% of this change |
| [[KATO III (line)]] | alt | 8.55 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 16.5× (z +13.1) | — |
| [[LoVo (line)]] | wt | 30.0 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.11× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[LS 180 (line)]] | wt | 29.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.89× (z +12.1) | — |
| [[PANC-1 (line)]] | alt | 12.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.42× (z +14.7) | — |
| [[A498 (line)]] | wt | 13.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.55× (z +12.5) | — |
| [[A549 (line)]] | wt | 23.6 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.12× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.188× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 12.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.10× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 12.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.10× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 70.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 30.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.07× (z +11.1) | — |
| [[A-172 (line)]] | wt | 33.0 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -11.7) ⚠ cell-cycle shift, explains ~78% of this change |
| [[A-427 (line)]] | wt | 38.3 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.76× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[AN3 CA (line)]] | alt | 37.0 | 0 | 2 | — | [[Pemigatinib (drug)]] 0.05 µM 0.0755× (z -9.8) |
| [[BT-474 (line)]] | alt | 12.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +9.8) | [[Silodosin (drug)]] 5 µM 0.0928× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 36.2 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.24× (z +8.8) | [[TAK-901 (drug)]] 5 µM 0.0764× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 8.01 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 12.8× (z +11.0) | — |
| [[SK-MEL-2 (line)]] | alt | 22.3 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 4.38× (z +8.9) | [[PH-797804 (drug)]] 5 µM 0.0359× (z -10.5) |
| [[SW 900 (line)]] | alt | 10.6 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 9.35× (z +9.6) | [[Bosentan (hydrate) (drug)]] 5 µM 0.0778× (z -10.6) |
| [[C32 (line)]] | wt | 5.76 | 0 | 1 | — | [[Silodosin (drug)]] 0.05 µM 0.0852× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 30.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.07× (z +8.9) | — |
| [[J82 (line)]] | alt | 22.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.94× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 24.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.20× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 26.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -12.6) |
| [[Panc 03.27 (line)]] | alt | 30.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.52× (z +8.7) | — |
| [[RKO (line)]] | wt | 25.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.217× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~54% of this change |
| [[RPMI-7951 (line)]] | alt | 6.69 | 0 | 1 | — | [[Ponatinib (drug)]] 0.5 µM 0.0654× (z -8.7) |
| [[SNU-1 (line)]] | wt | 18.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -10.4) |
| [[SW48 (line)]] | wt | 20.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0997× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.30 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.03 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 81.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.46 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.45 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 37.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12493), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOP1B]] | +0.58 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[MLXIPL]] | +0.54 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[SGSM1]] | +0.53 | +0.30 / +0.46 | both halves | 2e-04 |  |
| [[ARHGAP8]] | +0.51 | +0.24 / +0.35 | both halves | 4e-04 |  |
| [[SH3KBP1]] | +0.50 | +0.31 / +0.47 | both halves | 2e-04 | same gene group; pathway: Antigen activates B Cell Receptor (BCR) leading to generation of second messengers; STRING 688 |
| [[FAM102A]] | +0.50 | +0.38 / +0.45 | both halves | 7e-05 |  |
| [[MGAT4A]] | +0.50 | +0.34 / +0.42 | both halves | 1e-04 |  |
| [[RALGPS1]] | +0.49 | +0.22 / +0.52 | both halves | 6e-04 |  |
| [[GPRIN1]] | +0.49 | +0.23 / +0.44 | both halves | 5e-04 |  |
| [[RBM11]] | +0.49 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[CLIP2]] | +0.49 | +0.42 / +0.35 | both halves | 1e-04 |  |
| [[OTUD7A]] | +0.48 | +0.26 / +0.55 | both halves | 4e-04 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCGB2B2]] | -0.55 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[WDR33]] | -0.51 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[PNISR-AS1]] | -0.50 | -0.17 / -0.52 | ⚠ one half (not replicated) | 0.001 |  |
| [[DNAAF10]] | -0.49 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[NIFK-AS1]] | -0.48 | -0.22 / -0.36 | both halves | 6e-04 |  |
| [[TCEANC2]] | -0.48 | -0.26 / -0.40 | both halves | 4e-04 |  |
| [[C12orf60]] | -0.47 | -0.17 / -0.21 | ⚠ not reproduced | 0.001 |  |
| [[FAM120C]] | -0.47 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[ZNF717]] | -0.47 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[POLR1HASP]] | -0.45 | -0.29 / -0.37 | both halves | 2e-04 |  |
| [[UBA6-DT]] | -0.45 | -0.25 / -0.29 | both halves | 4e-04 |  |
| [[ZNF785]] | -0.45 | -0.18 / -0.35 | ⚠ not reproduced | 9e-04 |  |
| [[PTGR3]] | -0.44 | -0.22 / -0.41 | both halves | 6e-04 |  |
| [[SPRY3]] | -0.44 | -0.21 / -0.31 | both halves | 6e-04 |  |
| [[CENPL]] | -0.44 | -0.21 / -0.36 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGEF4]] | B | ARHGEF4 activity raises PLCG2's level | lines that do not express ARHGEF4 (15) vs lines expressing it (35) | 2.39× lower at baseline in the lines without ARHGEF4 | 0.015 | ⚠ within organs, on part of the lines; also absent: GALNT12, RBM47, NR2E3 |
| [[GALNT12]] | B | GALNT12 activity raises PLCG2's level | lines that do not express GALNT12 (10) vs lines expressing it (40) | 3.35× lower at baseline in the lines without GALNT12 | 0.057 | ⚠ within organs, on part of the lines; also absent: ARHGEF4, TUBA4A, ALS2CL |
| [[LPCAT2]] | B | LPCAT2 activity strengthens PLCG2's drug response | lines that do not express LPCAT2 (7) vs lines expressing it (31) | the lines without LPCAT2 respond 0.70× as strongly (z diff +1.01); strongest at Tucidinostat 5 µM: 1.21x vs 1.86x (z diff +2.8) | 0.096 | ⚠ within organs, on part of the lines; also absent: E2F7, PARD3B; target measured in part of the lines; artifact flags |
| [[RTN4R]] | C | RTN4R activity raises PLCG2's level | lines that do not express RTN4R (4) vs lines expressing it (46) | 3.97× lower at baseline in the lines without RTN4R | 0.031 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MMP15, RASSF7, ZDHHC11B; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRR5]] | B | PLCG2 activity raises PRR5's level | lines that do not express PLCG2 (10) vs lines expressing it (40) | 1.89× lower at baseline in the lines without PLCG2 | 0.026 | ⚠ within organs, on part of the lines; also absent: CRACD; maybe low, not absent |
| [[KIF21B]] | B | PLCG2 activity weakens KIF21B's drug response | lines that do not express PLCG2 (7) vs lines expressing it (30) | the lines without PLCG2 respond 0.96× as strongly (z diff -0.16); strongest at Panobinostat 0.5 µM: 7.31x vs 3.76x (z diff -1.9) | 0.044 | ⚠ within organs, on part of the lines; also absent: CRACD; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[GALNT12]] | B | PLCG2 activity raises GALNT12's level | lines that do not express PLCG2 (10) vs lines expressing it (40) | 2.81× lower at baseline in the lines without PLCG2 | 0.074 | ⚠ within organs, on part of the lines; also absent: CRACD; maybe low, not absent |
| [[ABCB1]] | B | PLCG2 activity lowers ABCB1's level | lines that do not express PLCG2 (10) vs lines expressing it (40) | 2.10× higher at baseline in the lines without PLCG2 | 0.081 | ⚠ within organs, on part of the lines; also absent: CRACD; maybe low, not absent |
| [[PGBD5]] | B | PLCG2 activity lowers PGBD5's level | lines that do not express PLCG2 (10) vs lines expressing it (40) | 1.61× higher at baseline in the lines without PLCG2 | 0.083 | ⚠ within organs, on part of the lines; also absent: CRACD; maybe low, not absent |
| [[ARHGEF4]] | B | PLCG2 activity raises ARHGEF4's level | lines that do not express PLCG2 (10) vs lines expressing it (40) | 2.12× lower at baseline in the lines without PLCG2 | 0.088 | ⚠ within organs, on part of the lines; also absent: CRACD; maybe low, not absent |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.499). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.5, 3.3); signed map (-20.8, 31.5). **Vector** length 77.0, 14.9% of its response variance represented; |z| ≥ 3 in 963 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.5 | -0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.1 | -0.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +5.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.8 | +22.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +1.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.8 | +2.0 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.5 | +1.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.7 | -6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -5.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -1.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase C gamma 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.1 — chr16:81,779,279-81,962,685 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phospholipases; SH2 domain containing; C2 domain containing phospholipases; SH3 domain containing |
| Reactome | 36 pathways, smallest: Erythropoietin activates Phospholipase C gamma (PLCG); Rituximab:MS4A1 (rituximab:CD20) targets B cells for antibody-dependent cellular cytotoxicity by NK cells; Generation of second messenger molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [P16885](https://www.uniprot.org/uniprotkb/P16885) (1-phosphatidylinositol 4,5-bisphosphate phosphodiesterase gamma-2):

> The production of the second messenger molecules diacylglycerol (DAG) and inositol 1,4,5-trisphosphate (IP3) is mediated by activated phosphatidylinositol-specific phospholipase C enzymes. It is a crucial enzyme in transmembrane signaling.

**Summary**, from NCBI Gene [5336](https://www.ncbi.nlm.nih.gov/gene/5336):

> The protein encoded by this gene is a transmembrane signaling enzyme that catalyzes the conversion of 1-phosphatidyl-1D-myo-inositol 4,5-bisphosphate to 1D-myo-inositol 1,4,5-trisphosphate (IP3) and diacylglycerol (DAG) using calcium as a cofactor. IP3 and DAG are second messenger molecules important for transmitting signals from growth factor receptors and immune system receptors across the cell membrane. Mutations in this gene have been found in autoinflammation, antibody deficiency, and …

**Accessions** — [HGNC:9066](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9066) · Entrez [5336](https://www.ncbi.nlm.nih.gov/gene/5336) · UniProt [P16885](https://www.uniprot.org/uniprotkb/P16885) · Ensembl [ENSG00000197943](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197943)

## Data

Gene col 12493: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12493); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12493, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12493]; `tensor/DDL_lfc|DDL_z.npy` [12493]; `embed/gene_vectors.npy` [12493]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12493 or target_col == 12493). Every well: [[PLCG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLCG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
