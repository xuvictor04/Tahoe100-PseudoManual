---
symbol: "PSMB7"
type: "gene"
col: 5939
ensembl_id: "ENSG00000136930"
name: "proteasome 20S subunit beta 7"
location: "9q33.3"
module: 60
arm: "+"
pooled_cpm: 112.16
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# PSMB7

*proteasome 20S subunit beta 7* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 3.28× (z +25.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.825× (z -6.0, q 1e-06, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.636×, PANC-1 0.645×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.486×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMB2]] (+0.74, fdr 7e-06), [[HSP90AA2P]] (+0.68, fdr 7e-06), [[PSMD14]] (+0.66, fdr 7e-06); moves opposite to [[TXNIP]] (-0.57, fdr 1e-05), [[NFYB]] (-0.57, fdr 1e-05), [[ZC3H6]] (-0.56, fdr 7e-06).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TALDO1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5939.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.28×** | +25.8 | 0e+00 | 48/48 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.06×** | +24.2 | 0e+00 | 48/48 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.99×** | +22.4 | 0e+00 | 48/48 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.11×** | +16.0 | 0e+00 | 47/49 (RKO, KATO III, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.86×** | +13.5 | 2e-39 | 46/48 (C32, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.77×** | +12.3 | 9e-33 | 45/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.04×** | +11.0 | 4e-26 | 47/49 (HT-29, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.53×** | +10.5 | 6e-24 | 40/48 (KATO III, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.43×** | +10.0 | 7e-22 | 44/45 (KATO III, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +10.0 | 9e-22 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +9.0 | 9e-18 | 36/45 (LoVo, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +8.0 | 7e-14 | 40/47 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +7.7 | 6e-13 | 36/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +7.6 | 1e-12 | 37/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.74×** | +6.3 | 1e-08 | 25/38 (NCI-H2347, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +6.1 | 3e-08 | 31/48 (COLO 205, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +4.3 | 5e-04 | 13/49 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.054 | 16/48 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.054 | 17/48 (Panc 03.27, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 5 µM |  | 1.16× | +3.0 | 0.059 | 13/48 (NCI-H1573, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5939.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.636×, PANC-1 0.645×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.486×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.825×** | -6.0 | 1e-06 | 26/48 (HEC-1-A, J82, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.841× | -3.8 | 0.034 | 22/48 (RKO, NCI-H23, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.873× | -3.7 | 0.034 | 12/48 (RKO, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.840× | -3.6 | 0.034 | 18/50 (NCI-H23, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.891× | -3.6 | 0.034 | 14/49 (RKO, PANC-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.844× | -3.6 | 0.034 | 22/47 (RKO, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.851× | -3.5 | 0.034 | 18/48 (SW1417, SK-MEL-2, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -3.5 | 0.036 | 13/48 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.740×** | -3.4 | 0.038 | 20/49 (RKO, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.854× | -3.3 | 0.064 | 19/48 (RKO, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.900× | -3.2 | 0.068 | 7/48 (SW 1088, LoVo, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.902× | -3.1 | 0.082 | 10/49 (LS 180, NCI-H2347, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.868× | -3.1 | 0.082 | 11/48 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.869× | -3.1 | 0.087 | 16/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.871× | -3.0 | 0.092 | 14/47 (AsPC-1, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5939. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 96.7 | 12 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.77× (z +23.5) | — |
| [[LoVo (line)]] | wt | 86.9 | 12 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.97× (z +22.3) | — |
| [[NCI-H460 (line)]] | wt | 134 | 12 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.74× (z +19.3) | — |
| [[SW480 (line)]] | alt | 104 | 10 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.40× (z +23.6) | — |
| [[NCI-H23 (line)]] | alt | 108 | 8 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.19× (z +14.0) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.36× (z +10.8) | — |
| [[COLO 205 (line)]] | alt | 85.8 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.96× (z +20.5) | — |
| [[HT-29 (line)]] | alt | 78.1 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.72× (z +22.4) | — |
| [[LS 180 (line)]] | wt | 107 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.00× (z +20.3) | — |
| [[PANC-1 (line)]] | alt | 84.8 | 6 (2 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.07× (z +16.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.645× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 251 | 5 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.98× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.486× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[SW 900 (line)]] | alt | 105 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.91× (z +11.6) | — |
| [[HEC-1-A (line)]] | alt | 99.5 | 6 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.37× (z +20.0) | — |
| [[HOP62 (line)]] | alt | 92.2 | 6 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.78× (z +16.5) | — |
| [[LOX-IMVI (line)]] | wt | 112 | 6 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.16× (z +15.7) | — |
| [[NCI-H1792 (line)]] | alt | 94.8 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.89× (z +14.5) | — |
| [[SW48 (line)]] | wt | 135 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.59× (z +13.6) | — |
| [[A-172 (line)]] | wt | 157 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.78× (z +13.8) | — |
| [[AsPC-1 (line)]] | alt | 89.6 | 5 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +11.7) | — |
| [[C32 (line)]] | wt | 113 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.90× (z +15.9) | — |
| [[Panc 03.27 (line)]] | alt | 96.9 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.81× (z +16.4) | — |
| [[RPMI-7951 (line)]] | alt | 108 | 5 | 0 | [[TAK-901 (drug)]] 5 µM 8.05× (z +12.0) | — |
| [[SHP-77 (line)]] | alt | 112 | 5 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.99× (z +13.2) | — |
| [[SW1417 (line)]] | alt | 110 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.01× (z +12.9) | — |
| [[A498 (line)]] | wt | 169 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.75× (z +13.0) | — |
| [[Hs 766T (line)]] | wt | 117 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.76× (z +15.2) | — |
| [[HS-578T (line)]] | alt | 96.5 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.72× (z +12.0) | — |
| [[J82 (line)]] | alt | 170 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.44× (z +13.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 116 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.26× (z +14.5) | — |
| [[NCI-H1573 (line)]] | alt | 61.4 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.58× (z +16.6) | — |
| [[A549 (line)]] | wt | 132 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.61× (z +11.3) | — |
| [[BT-474 (line)]] | alt | 143 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.23× (z +14.0) | — |
| [[CFPAC-1 (line)]] | alt | 73.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.31× (z +12.6) | — |
| [[H4 (line)]] | wt | 134 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 4.02× (z +11.8) | — |
| [[HCT15 (line)]] | alt | 98.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.36× (z +15.8) | — |
| [[HepG2_C3A (line)]] | wt | 97.4 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.23× (z +13.5) | — |
| [[hTERT-HPNE (line)]] | wt | 102 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.98× (z +13.4) | — |
| [[NCI-H2030 (line)]] | alt | 112 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.61× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 99.1 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.80× (z +13.1) | — |
| [[SK-MEL-2 (line)]] | alt | 134 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.58× (z +11.7) | — |
| [[SNU-1 (line)]] | wt | 112 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.59× (z +16.5) | — |
| [[SNU-423 (line)]] | alt | 149 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.93× (z +13.1) | — |
| [[A-427 (line)]] | wt | 93.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.70× (z +11.2) | — |
| [[C-33 A (line)]] | alt | 94.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.17× (z +11.2) | — |
| [[AN3 CA (line)]] | alt | 133 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.33× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 83.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 135 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5939), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMB2]] | +0.74 | +0.75 / +0.74 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[HSP90AA2P]] | +0.68 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[PSMD14]] | +0.66 | +0.64 / +0.68 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMD1]] | +0.64 | +0.63 / +0.63 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 998 |
| [[PSMD2]] | +0.64 | +0.72 / +0.59 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMD12]] | +0.63 | +0.59 / +0.67 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMA1]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[AHSA1]] | +0.62 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[VTI1A]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[PSMC4]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 998 |
| [[CCT4]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 | STRING 515 |
| [[MTPN]] | +0.62 | +0.66 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNIP]] | -0.57 | -0.54 / -0.58 | both halves | 1e-05 | pathway: Cellular response to chemical stress |
| [[NFYB]] | -0.57 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[ZC3H6]] | -0.56 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[SAP30]] | -0.52 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[PWWP2A]] | -0.51 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[TAPT1]] | -0.51 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[PURA]] | -0.51 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[NBPF19]] | -0.50 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[CEBPD]] | -0.50 | -0.60 / -0.43 | both halves | 4e-05 |  |
| [[SCAF11]] | -0.50 | -0.68 / -0.30 | both halves | 2e-04 |  |
| [[PER2]] | -0.50 | -0.49 / -0.41 | both halves | 4e-05 | pathway: Circadian clock |
| [[ZFP36L2]] | -0.50 | -0.58 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TALDO1]] | C | TALDO1's natural level weakens PSMB7's drug response | TALDO1's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.64, reverse -0.09; direction not clear | 0.046 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.707). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-19.1, -12.4); signed map (-27.7, -29.0). **Vector** length 97.1, 32.0% of its response variance represented; |z| ≥ 3 in 1,287 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mTORC1 signaling* (hallmark, mean cos +0.50 to 13); *Folding of actin by CCT/TriC* (reactome, mean cos +0.55 to 4); *MYC targets v1* (hallmark, mean cos +0.52 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.8 | +24.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.8 | +25.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.6 | +22.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.1 | +13.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.9 | +10.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +2.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.8 | +11.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | +3.0 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.3 | -2.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.6 | -0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.7 | +12.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.7 | +7.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -6.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.1 | -0.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.8 | +0.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | +1.5 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 20S subunit beta 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:124,353,465-124,415,444 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Z |
| Gene groups (HGNC) | Proteasome |
| Reactome | 171 pathways, smallest: Antigen processing: Ub, ATP-independent proteasomal degradation; Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99436](https://www.uniprot.org/uniprotkb/Q99436) (Proteasome subunit beta type-7):

> Component of the 20S core proteasome complex involved in the proteolytic degradation of most intracellular proteins. This complex plays numerous essential roles within the cell by associating with different regulatory particles. Associated with two 19S regulatory particles, forms the 26S proteasome and thus participates in the ATP-dependent degradation of ubiquitinated proteins. The 26S proteasome plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged …

**Summary**, from NCBI Gene [5695](https://www.ncbi.nlm.nih.gov/gene/5695):

> The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent process in a non-lysosomal pathway. The encoded protein is a member of the proteasome B-type family, …

**Accessions** — [HGNC:9544](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9544) · Entrez [5695](https://www.ncbi.nlm.nih.gov/gene/5695) · UniProt [Q99436](https://www.uniprot.org/uniprotkb/Q99436) · Ensembl [ENSG00000136930](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136930)

## Data

Gene col 5939: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5939); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5939, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5939]; `tensor/DDL_lfc|DDL_z.npy` [5939]; `embed/gene_vectors.npy` [5939]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5939 or target_col == 5939). Every well: [[PSMB7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMB7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
