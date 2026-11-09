---
symbol: "SSPOP"
type: "gene"
col: 12416
ensembl_id: "ENSG00000197558"
name: "SCO-spondin, pseudogene"
location: "7q36.1"
module: 10
arm: "+"
pooled_cpm: 2.44
n_lines_expressing: 37
n_dd_up: 19
n_dd_down: 24
n_dd_up_clean: 15
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 12
direction_downstream: 19
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# SSPOP

*SCO-spondin, pseudogene* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.48× (z +8.9, q 3e-16, up in 20 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.359× (z -7.1, q 7e-10, down in 22 of 31 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.393× (z -6.5, q 3e-08, down in 19 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ID2-AS1]] (+0.67, fdr 7e-06), [[ERICH6-AS1]] (+0.58, fdr 1e-05), [[ADAMTS13]] (+0.57, fdr 1e-05); moves opposite to [[C1orf109]] (-0.48, fdr 3e-04), [[ABRAXAS2]] (-0.47, fdr 8e-05), [[PHC3]] (-0.46, fdr 5e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[TMEM170B]] → it (grade B ⚠); 19 go from it, the strongest it → [[RDM1P5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12416.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.48×** | +8.9 | 3e-16 | 20/30 (SW480, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.86×** | +7.0 | 6e-10 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.67×** | +6.8 | 2e-09 | 16/25 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.53×** | +6.5 | 2e-08 | 18/31 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.34×** | +5.5 | 5e-06 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.09×** | +5.1 | 3e-05 | 14/32 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +5.0 | 4e-05 | 7/21 (LoVo, A549, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.0 | 0.004 | 6/30 (A498, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.77×** | +4.0 | 0.005 | 8/28 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +3.6 | 0.015 | 1/11 (SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.67×** | +3.6 | 0.018 | 9/29 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +3.5 | 0.025 | 6/18 (A498, A549, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.64×** | +3.3 | 0.041 | 10/22 (HOP62, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.63×** | +3.3 | 0.041 | 4/17 (LoVo, SW480, …) | top dose only | position effect removed |
| [[Orlistat (drug)]] 0.05 µM |  | **1.62×** | +3.1 | 0.072 | 3/15 (A549, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.55×** | +3.0 | 0.084 | 5/28 (A498, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.54×** | +3.0 | 0.084 | 7/30 (A-427, LoVo, …) | top dose only |  |
| [[Arbutin (drug)]] 0.5 µM |  | **1.53×** | +3.0 | 0.094 | 6/29 (NCI-H460, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12416.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.359×** | -7.1 | 7e-10 | 22/31 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.393×** | -6.5 | 3e-08 | 19/30 (NCI-H23, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~18% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.398×** | -6.4 | 3e-08 | 19/31 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.415×** | -6.1 | 1e-07 | 19/26 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.418×** | -6.0 | 2e-07 | 18/29 (A549, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.440×** | -5.7 | 1e-06 | 17/17 (NCI-H23, A-172, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.467×** | -5.0 | 5e-05 | 15/23 (NCI-H460, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.520×** | -4.4 | 1e-03 | 13/24 (NCI-H23, SW480, …) | two highest doses | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.547×** | -4.2 | 0.002 | 14/32 (H4, A549, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.535×** | -4.2 | 0.002 | 12/30 (LOX-IMVI, SNU-1, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.553×** | -4.1 | 0.002 | 9/29 (NCI-H460, H4, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.566×** | -3.9 | 0.004 | 12/25 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.592×** | -3.6 | 0.012 | 7/32 (SNU-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.600×** | -3.5 | 0.016 | 8/30 (HOP62, C32, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.610×** | -3.4 | 0.023 | 12/24 (NCI-H23, A498, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.634×** | -3.1 | 0.049 | 13/25 (A549, MIA PaCa-2, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.642×** | -3.1 | 0.058 | 15/26 (NCI-H23, A498, …) | rises with dose |  |
| [[Relugolix (drug)]] 0.5 µM |  | **0.642×** | -3.1 | 0.058 | 2/30 (LoVo, MIA PaCa-2) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.431×** | -3.1 | 0.058 | 8/23 (A-427, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.624×** | -3.0 | 0.062 | 7/27 (NCI-H2030, MIA PaCa-2, …) | all doses, flat |  |
| [[Ixazomib (drug)]] 0.05 µM |  | **0.643×** | -2.9 | 0.091 | 6/22 (A498, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.81 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12416. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 15.7 | 0 | 9 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0341× (z -14.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.105× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 3.55 | 0 | 3 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0610× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 3.06 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -10.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0637× (z -8.9) |
| [[A-427 (line)]] | wt | 6.00 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0620× (z -8.6) ⚠ cell-cycle shift, explains ~51% of this change |
| [[HT-29 (line)]] | alt | 3.15 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0929× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 2.71 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0295× (z -9.5) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 2.22 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0590× (z -8.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A-172 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.983 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.889 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.836 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.986 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.477 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.254 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.376 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.831 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.305 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.592 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.863 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.711 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.703 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12416), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ID2-AS1]] | +0.67 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[ERICH6-AS1]] | +0.58 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ADAMTS13]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 | pathway: Defective B3GALTL causes PpS |
| [[KNDC1]] | +0.56 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[MIR1915HG]] | +0.56 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[B4GAT1-DT]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[PPEF1]] | +0.55 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[LMNTD2]] | +0.54 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[DANT1]] | +0.54 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[FAM66C]] | +0.54 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[TMEM198B]] | +0.53 | +0.55 / +0.48 | both halves | 2e-05 | same gene group |
| [[LINC00205]] | +0.53 | +0.55 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1orf109]] | -0.48 | -0.29 / -0.55 | both halves | 3e-04 |  |
| [[ABRAXAS2]] | -0.47 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[PHC3]] | -0.46 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[MRPL2]] | -0.46 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[NUP37]] | -0.45 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[METTL15]] | -0.45 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[TIMM9]] | -0.44 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[BLOC1S5]] | -0.44 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[FCF1]] | -0.44 | -0.25 / -0.51 | both halves | 4e-04 |  |
| [[ARMC1]] | -0.43 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[SPRYD7]] | -0.43 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[MRPL58]] | -0.43 | -0.30 / -0.45 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 8, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM170B]] | B | TMEM170B activity raises SSPOP's level | lines that do not express TMEM170B (8) vs lines expressing it (42) | 1.56× lower at baseline in the lines without TMEM170B | 0.014 | ⚠ within organs, on part of the lines; also absent: KCNK13, KDM2B-DT, LINC02609 |
| [[SRCIN1]] | B | SRCIN1 activity raises SSPOP's level | lines that do not express SRCIN1 (9) vs lines expressing it (41) | 2.07× lower at baseline in the lines without SRCIN1 | 0.016 | ⚠ within organs, on part of the lines; also absent: TSPAN33, PRKN |
| [[TLCD3B]] | B | TLCD3B activity raises SSPOP's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 2.11× lower at baseline in the lines without TLCD3B | 0.042 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[RDM1P5]] | B | RDM1P5 activity raises SSPOP's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 2.03× lower at baseline in the lines without RDM1P5 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[LINC02026]] | B | LINC02026 activity raises SSPOP's level | lines that do not express LINC02026 (8) vs lines expressing it (42) | 1.83× lower at baseline in the lines without LINC02026 | 0.058 | ⚠ within organs, on part of the lines; also absent: ASRGL1, ENSG00000256673 |
| [[MIR1915HG]] | B | MIR1915HG activity raises SSPOP's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 1.71× lower at baseline in the lines without MIR1915HG | 0.079 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[KLRC4-KLRK1]] | B | KLRC4-KLRK1 activity raises SSPOP's level | lines that do not express KLRC4-KLRK1 (29) vs lines expressing it (21) | 1.48× lower at baseline in the lines without KLRC4-KLRK1 | 0.089 | ⚠ within organs, on part of the lines; co-absent genes; also absent: KLRC3, KLRC2, PIP5K1B |
| [[RFPL1S]] | B | RFPL1S activity raises SSPOP's level | lines that do not express RFPL1S (16) vs lines expressing it (34) | 2.01× lower at baseline in the lines without RFPL1S | 0.0995 | ⚠ within organs, on part of the lines; also absent: RASSF2, PHF21B, CECR2; maybe low, not absent |
| [[FAM66C]] | C | FAM66C activity raises SSPOP's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 2.09× lower at baseline in the lines without FAM66C | 0.008 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent; co-absent with the target |
| [[LINC00466]] | C | LINC00466 activity raises SSPOP's level | lines that do not express LINC00466 (15) vs lines expressing it (35) | 1.97× lower at baseline in the lines without LINC00466 | 0.013 | ⚠ within organs, on part of the lines; also absent: FAM124A, NTN1, SSPOP; maybe low, not absent; co-absent with the target |
| [[LRRC4B]] | C | LRRC4B activity raises SSPOP's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 2.15× lower at baseline in the lines without LRRC4B | 0.021 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent; co-absent with the target |
| [[SLC9A3-AS1]] | C | SLC9A3-AS1 activity lowers SSPOP's level | lines that do not express SLC9A3-AS1 (4) vs lines expressing it (46) | 1.51× higher at baseline in the lines without SLC9A3-AS1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 16, C 3. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RDM1P5]] | B | SSPOP activity raises RDM1P5's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 2.12× lower at baseline in the lines without SSPOP | 0.006 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |
| [[LINC00205]] | B | SSPOP activity raises LINC00205's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 1.71× lower at baseline in the lines without SSPOP | 0.011 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |
| [[BRPF3-AS1]] | B | SSPOP activity raises BRPF3-AS1's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 1.62× lower at baseline in the lines without SSPOP | 0.018 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |
| [[LINC02026]] | B | SSPOP activity raises LINC02026's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 1.73× lower at baseline in the lines without SSPOP | 0.024 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |
| [[MAP3K14-AS1]] | B | SSPOP activity raises MAP3K14-AS1's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 1.48× lower at baseline in the lines without SSPOP | 0.027 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |
| [[MYO1F]] | B | SSPOP activity raises MYO1F's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 1.24× lower at baseline in the lines without SSPOP | 0.032 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |
| [[KAZALD1]] | B | SSPOP activity raises KAZALD1's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 1.46× lower at baseline in the lines without SSPOP | 0.038 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |
| [[ASIC4]] | B | SSPOP activity raises ASIC4's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 1.68× lower at baseline in the lines without SSPOP | 0.039 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |
| [[MIR1915HG]] | B | SSPOP activity raises MIR1915HG's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 2.12× lower at baseline in the lines without SSPOP | 0.042 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |
| [[SRCIN1]] | B | SSPOP activity raises SRCIN1's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 2.17× lower at baseline in the lines without SSPOP | 0.056 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |
| [[GAL3ST2]] | B | SSPOP activity raises GAL3ST2's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 1.43× lower at baseline in the lines without SSPOP | 0.064 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |
| [[ACBD4]] | B | SSPOP activity raises ACBD4's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 1.22× lower at baseline in the lines without SSPOP | 0.069 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.251). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.2, 29.7); signed map (37.5, -7.9). **Vector** length 51.3, 9.43% of its response variance represented; |z| ≥ 3 in 841 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +6.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +2.8 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.3 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +0.6 |
|  | [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | +1.1 | +2.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | -2.9 | -4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.6 | -6.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -2.0 | -3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.8 | -6.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -3.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -3.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | SCO-spondin, pseudogene |
| Locus type | pseudogene |
| Location | 7q36.1 — chr7:149,776,042-149,833,829 (+) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | SCO-spondin, KIAA0543, FLJ36112; previously SSPO |
| Gene groups (HGNC) | Unitary pseudogenes |
| Reactome | 6 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [A2VEC9](https://www.uniprot.org/uniprotkb/A2VEC9) (SCO-spondin):

> Involved in the modulation of neuronal aggregation (By similarity). May be involved in developmental events during the formation of the central nervous system (By similarity).

**Summary**, from NCBI Gene [23145](https://www.ncbi.nlm.nih.gov/gene/23145):

> Predicted to be an extracellular matrix structural constituent. Predicted to be involved in cell adhesion. Predicted to be located in cytoplasm. Predicted to be active in extracellular matrix and obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21998](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21998) · Entrez [23145](https://www.ncbi.nlm.nih.gov/gene/23145) · UniProt [A2VEC9](https://www.uniprot.org/uniprotkb/A2VEC9) · Ensembl [ENSG00000197558](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197558)

## Data

Gene col 12416: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12416); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12416, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12416]; `tensor/DDL_lfc|DDL_z.npy` [12416]; `embed/gene_vectors.npy` [12416]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12416 or target_col == 12416). Every well: [[SSPOP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SSPOP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
