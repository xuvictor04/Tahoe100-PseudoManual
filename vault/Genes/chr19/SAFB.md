---
symbol: "SAFB"
type: "gene"
col: 8363
ensembl_id: "ENSG00000160633"
name: "scaffold attachment factor B"
location: "19p13.3"
module: 184
arm: "-"
pooled_cpm: 108.91
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 12
n_dd_up_clean: 14
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/184"]
generated_by: "tahoemap"
---

# SAFB

*scaffold attachment factor B* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.76× (z +14.0, q 2e-41, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.605× (z -8.9, q 4e-16, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF362]] (+0.64, fdr 4e-05), [[BRD1]] (+0.61, fdr 4e-05), [[WDR33]] (+0.60, fdr 4e-05); moves opposite to [[SH3BGRL3]] (-0.64, fdr 2e-05), [[EHD4]] (-0.59, fdr 1e-04), [[CAP1]] (-0.58, fdr 4e-05).
> It sits in the **-** arm of [[Module 184]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PLEK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8363.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +14.0 | 2e-41 | 46/48 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.19×** | +13.7 | 2e-40 | 47/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +11.2 | 9e-27 | 45/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.06×** | +10.3 | 1e-22 | 45/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **3.03×** | +10.2 | 3e-22 | 47/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.68×** | +9.1 | 8e-18 | 44/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.65×** | +8.8 | 1e-16 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.64×** | +8.4 | 4e-15 | 41/48 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +6.8 | 7e-10 | 37/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +6.5 | 4e-09 | 37/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.29×** | +4.4 | 6e-04 | 25/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +4.3 | 6e-04 | 24/48 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +4.3 | 8e-04 | 30/48 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.27×** | +4.2 | 0.001 | 25/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.036 | 25/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.042 | 21/48 (SNU-423, LS 180, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8363.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.605×** | -8.9 | 4e-16 | 47/48 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.653×** | -7.5 | 1e-11 | 42/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.658×** | -7.4 | 3e-11 | 41/48 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.758×** | -7.0 | 5e-10 | 37/48 (SW480, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.737×** | -5.4 | 7e-06 | 40/48 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.765×** | -4.6 | 5e-04 | 27/44 (C32, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.784×** | -4.3 | 0.001 | 27/49 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.816×** | -3.6 | 0.019 | 24/49 (RKO, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.752×** | -3.6 | 0.019 | 27/48 (BT-474, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.684×** | -3.5 | 0.024 | 27/49 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.827×** | -3.4 | 0.036 | 24/49 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.772×** | -3.3 | 0.050 | 25/48 (A-427, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.788× | -3.0 | 0.11 | 23/47 (A549, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8363. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 97.6 | 9 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +17.5) | [[Panobinostat (drug)]] 5 µM 0.460× (z -10.2) |
| [[LoVo (line)]] | wt | 110 | 9 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.54× (z +22.1) | [[Belinostat (drug)]] 5 µM 0.516× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 89.0 | 10 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +15.2) | — |
| [[SW480 (line)]] | alt | 132 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +19.6) | — |
| [[COLO 205 (line)]] | alt | 73.7 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.84× (z +12.3) | — |
| [[NCI-H1792 (line)]] | alt | 98.0 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +13.2) | — |
| [[RKO (line)]] | wt | 134 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -11.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 134 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +11.5) | [[Belinostat (drug)]] 5 µM 0.512× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 88.2 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +12.0) | — |
| [[BT-474 (line)]] | alt | 98.4 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.60× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 84.1 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +10.8) | — |
| [[KATO III (line)]] | alt | 77.5 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +12.6) | — |
| [[LS 180 (line)]] | wt | 116 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.74× (z +15.1) | — |
| [[NCI-H1573 (line)]] | alt | 74.0 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.21× (z +12.2) | — |
| [[SW48 (line)]] | wt | 168 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -8.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 89.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 137 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +11.5) | — |
| [[NCI-H23 (line)]] | alt | 121 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +9.8) | — |
| [[A-427 (line)]] | wt | 127 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.7) | — |
| [[HEC-1-A (line)]] | alt | 118 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +13.9) | — |
| [[Panc 03.27 (line)]] | alt | 99.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.7) | — |
| [[A498 (line)]] | wt | 113 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +9.5) | — |
| [[A549 (line)]] | wt | 81.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +12.9) | — |
| [[AN3 CA (line)]] | alt | 165 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0909× (z -9.3) ⚠ toxic |
| [[C32 (line)]] | wt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.316× (z -9.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 68.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.3) | — |
| [[H4 (line)]] | wt | 97.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 122 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 138 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 5.03× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 155 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 112 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +12.9) | — |
| [[SHP-77 (line)]] | alt | 125 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +9.0) | — |
| [[SNU-1 (line)]] | wt | 136 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.68× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 100 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 127 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.426× (z -9.1) |
| [[A-172 (line)]] | wt | 99.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 151 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 178 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 108 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 77.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 95.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 93.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 138 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8363), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF362]] | +0.64 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[BRD1]] | +0.61 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[WDR33]] | +0.60 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[CCAR1]] | +0.59 | +0.37 / +0.42 | both halves | 8e-05 |  |
| [[OXA1L-DT]] | +0.59 | +0.34 / +0.30 | both halves | 2e-04 |  |
| [[UBTF]] | +0.59 | +0.36 / +0.42 | both halves | 9e-05 |  |
| [[LUC7L2]] | +0.58 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[RPRD2]] | +0.58 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[HDGF]] | +0.58 | +0.36 / +0.48 | both halves | 1e-04 |  |
| [[SRSF4]] | +0.58 | +0.40 / +0.63 | both halves | 5e-05 | same gene group; STRING 413 |
| [[OARD1]] | +0.57 | +0.32 / +0.42 | both halves | 2e-04 |  |
| [[STRN4]] | +0.57 | +0.37 / +0.53 | both halves | 8e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3BGRL3]] | -0.64 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[EHD4]] | -0.59 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[CAP1]] | -0.58 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[LYPD3]] | -0.58 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[C3orf52]] | -0.58 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[LRRFIP1]] | -0.57 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[FLNB]] | -0.56 | -0.29 / -0.43 | both halves | 2e-04 |  |
| [[LPCAT2]] | -0.56 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[PIP4K2A]] | -0.55 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[AGPAT4]] | -0.55 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[GDPD5]] | -0.55 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[TPMT]] | -0.55 | -0.33 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEK2]] | B | PLEK2 activity lowers SAFB's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 1.16× higher at baseline in the lines without PLEK2 | 0.058 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[TUBA1A]] | B | TUBA1A activity raises SAFB's level | lines that do not express TUBA1A (10) vs lines expressing it (40) | 1.14× lower at baseline in the lines without TUBA1A | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000289516, GABBR1, CHST10 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 184]]; 20 genes; this gene is in the **-** arm (projection on the module's main direction -0.724). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-3.5, 14.1); signed map (26.9, -25.3). **Vector** length 72.3, 20.8% of its response variance represented; |z| ≥ 3 in 1,181 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +14.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | -1.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | -0.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | -4.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | -3.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.0 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | -0.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.4 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | -2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.2 | -1.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.0 | -7.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.5 | -5.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.2 | -7.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | +9.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | +3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -1.7 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.9 | -0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | scaffold attachment factor B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:5,623,035-5,668,478 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HET, SAFB1 |
| Gene groups (HGNC) | RNA binding motif containing; Scaffold attachment factor B family |
| Reactome | 3 pathways, smallest: SUMOylation of transcription cofactors; SUMO E3 ligases SUMOylate target proteins; SUMOylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15424](https://www.uniprot.org/uniprotkb/Q15424) (Scaffold attachment factor B1):

> Binds to scaffold/matrix attachment region (S/MAR) DNA and forms a molecular assembly point to allow the formation of a 'transcriptosomal' complex (consisting of SR proteins and RNA polymerase II) coupling transcription and RNA processing. Functions as an estrogen receptor corepressor and can also bind to the HSP27 promoter and decrease its transcription. Thereby acts as a negative regulator of cell proliferation. When associated with RBMX, binds to and stimulates transcription from the SREBF1 …

**Summary**, from NCBI Gene [6294](https://www.ncbi.nlm.nih.gov/gene/6294):

> This gene encodes a DNA-binding protein which has high specificity for scaffold or matrix attachment region DNA elements (S/MAR DNA). This protein is thought to be involved in attaching the base of chromatin loops to the nuclear matrix but there is conflicting evidence as to whether this protein is a component of chromatin or a nuclear matrix protein. Scaffold attachment factors are a specific subset of nuclear matrix proteins (NMP) that specifically bind to S/MAR. The encoded protein is …

**Accessions** — [HGNC:10520](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10520) · Entrez [6294](https://www.ncbi.nlm.nih.gov/gene/6294) · UniProt [Q15424](https://www.uniprot.org/uniprotkb/Q15424) · Ensembl [ENSG00000160633](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160633)

## Data

Gene col 8363: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8363); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8363, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8363]; `tensor/DDL_lfc|DDL_z.npy` [8363]; `embed/gene_vectors.npy` [8363]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8363 or target_col == 8363). Every well: [[SAFB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAFB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
