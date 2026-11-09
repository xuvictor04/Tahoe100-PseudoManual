---
symbol: "UTY"
type: "gene"
col: 11470
ensembl_id: "ENSG00000183878"
name: "ubiquitously transcribed tetratricopeptide repeat containing, Y-linked"
location: "Yq11.221"
module: 177
arm: "+"
pooled_cpm: 62.63
n_lines_expressing: 19
n_dd_up: 21
n_dd_down: 36
n_dd_up_clean: 15
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 18
direction_downstream: 22
tags: ["gene", "module/177"]
generated_by: "tahoemap"
---

# UTY

*ubiquitously transcribed tetratricopeptide repeat containing, Y-linked* — Yq11.221

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.87× (z +10.7, q 9e-24, up in 0 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Verteporfin (drug)]] 0.5 µM: 1.44× (z +6.2, q 1e-07, up in 0 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.514× (z -11.3, q 6e-27, down in 17 of 17 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.644× (z -6.9, q 4e-10, down in 0 of 17 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP9Y]] (+0.69, fdr 7e-06), [[FAM230C]] (+0.69, fdr 7e-06), [[KDM5D]] (+0.67, fdr 1e-05); moves opposite to [[OSBPL3]] (-0.44, fdr 2e-04).
> It is in [[Module 177]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[DDX3Y]], [[KDM5D]] → it (grade C ⚠); 22 go from it, the strongest it → [[LINC02398]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11470.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +10.7 | 9e-24 | 0/18 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +6.4 | 5e-08 | 0/15 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.44×** | +6.2 | 1e-07 | 0/18 | all doses, stronger at high dose | position effect removed |
| [[Dorzolamide (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +5.3 | 1e-05 | 0/18 | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.33×** | +4.7 | 3e-04 | 0/18 | all doses, stronger at high dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.6 | 4e-04 | 0/19 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +4.5 | 7e-04 | 3/17 (SNU-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +4.2 | 0.002 | 4/17 (A-427, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +4.1 | 0.002 | 1/17 (SW 1088) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.27×** | +4.1 | 0.002 | 0/17 | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | **1.27×** | +4.1 | 0.002 | 0/17 | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.27×** | +3.7 | 0.009 | 0/15 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.50×** | +3.6 | 0.012 | 13/18 (COLO 205, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.5 | 0.017 | 1/14 (A-427) | top dose only | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.030 | 0/17 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.030 | 0/17 | inconsistent across doses |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.042 | 0/17 | top dose only |  |
| [[Tazarotene (drug)]] 0.05 µM |  | **1.20×** | +3.1 | 0.053 | 0/18 | inconsistent across doses | position effect removed |
| [[Arbutin (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.053 | 3/17 (HCT15, C32, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.20×** | +3.0 | 0.072 | 10/16 (A549, C32, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.081 | 0/17 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11470.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.514×** | -11.3 | 6e-27 | 17/17 (COLO 205, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.556×** | -10.0 | 4e-21 | 16/17 (COLO 205, H4, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.587×** | -9.1 | 2e-17 | 17/17 (COLO 205, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.584×** | -8.8 | 2e-16 | 16/16 (SNU-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.606×** | -8.5 | 2e-15 | 17/17 (NCI-H460, COLO 205, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.644×** | -6.9 | 4e-10 | 0/17 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.671×** | -6.8 | 8e-10 | 12/17 (HCT15, COLO 205, …) | rises with dose |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.711×** | -5.4 | 6e-06 | 0/17 | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.552×** | -5.3 | 7e-06 | 14/17 (NCI-H460, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.727×** | -5.0 | 3e-05 | 0/17 | inconsistent across doses |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.737×** | -4.9 | 5e-05 | 0/17 | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.586×** | -4.8 | 9e-05 | 15/17 (A549, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.760×** | -4.7 | 1e-04 | 6/17 (SK-MEL-2, COLO 205, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.763×** | -4.6 | 2e-04 | 7/17 (A549, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Tucatinib (drug)]] 0.5 µM |  | **0.633×** | -4.5 | 2e-04 | 0/17 | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.763×** | -4.3 | 5e-04 | 2/17 (LoVo, SNU-1) | inconsistent across doses |  |
| [[Relugolix (drug)]] 5 µM |  | 0.837× | -4.3 | 6e-04 | 0/18 | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.627×** | -4.2 | 1e-03 | 10/17 (NCI-H460, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.776×** | -4.2 | 1e-03 | 4/17 (NCI-H460, A549, …) | top dose only |  |
| [[Tirabrutinib (drug)]] 0.05 µM |  | **0.772×** | -4.1 | 0.001 | 0/17 | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.776×** | -4.0 | 0.002 | 0/17 | inconsistent across doses |  |
| [[MK-8353 (drug)]] 0.5 µM |  | **0.675×** | -3.9 | 0.002 | 0/17 | inconsistent across doses | noisy plate (z scaled) |
| [[Tadalafil (drug)]] 5 µM |  | **0.797×** | -3.7 | 0.005 | 0/17 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11470. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 299 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -18.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 192 | 2 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +13.2) ⚠ cell-cycle shift, explains ~54% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.0966× (z -23.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 388 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -19.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 194 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -20.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 233 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.4) ⚠ cell-cycle shift, explains ~54% of this change | [[Dinaciclib (drug)]] 5 µM 0.173× (z -15.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 154 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.4) ⚠ cell-cycle shift, explains ~54% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -17.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 143 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0247× (z -31.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 255 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0394× (z -20.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 206 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0550× (z -23.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 323 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -22.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 181 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -19.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 197 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -17.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 215 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0904× (z -19.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -13.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 81.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -11.7) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 178 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0640× (z -10.6) |
| [[A498 (line)]] | wt | 4.28 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.38 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.64 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.20 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.22 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.16 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.37 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.65 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.26 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.05 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.38 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.68 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.39 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.42 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.02 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.41 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.04 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.57 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 91.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.28 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.45 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.26 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.29 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.70 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.85 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.46 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11470), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP9Y]] | +0.69 | +0.58 / +0.75 | both halves | 7e-06 | same gene group; STRING 999 |
| [[FAM230C]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[KDM5D]] | +0.67 | +0.51 / +0.75 | both halves | 1e-05 | same gene group; pathway: Chromatin modifying enzymes; STRING 999 |
| [[LINC02335]] | +0.67 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[TPTE]] | +0.66 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[BAGE2]] | +0.66 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[NLGN4Y]] | +0.64 | +0.57 / +0.64 | both halves | 9e-06 | STRING 894 |
| [[ZEB2]] | +0.63 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[LINC00470]] | +0.60 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[FBXL7]] | +0.59 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[LINC01320]] | +0.56 | +0.33 / +0.54 | both halves | 1e-04 |  |
| [[MAGI2]] | +0.54 | +0.54 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSBPL3]] | -0.44 | -0.31 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 0, C 18. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDX3Y]], [[KDM5D]] | C | DDX3Y, KDM5D activity raises UTY's level | lines that do not express DDX3Y, KDM5D (30) vs lines expressing them (20) | 24.64× lower at baseline in the lines without DDX3Y, KDM5D | 5e-07 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; co-absent with the target; co-absent genes |
| [[TTTY10]] | C | TTTY10 activity raises UTY's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 21.86× lower at baseline in the lines without TTTY10 | 2e-05 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |
| [[PRKY]], [[USP9Y]] | C | PRKY, USP9Y activity raises UTY's level | lines that do not express PRKY, USP9Y (30) vs lines expressing them (20) | 17.21× lower at baseline in the lines without PRKY, USP9Y | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZFY, KDM5D, RPS4Y1; co-absent with the target; co-absent genes |
| [[TTTY14]] | C | TTTY14 activity raises UTY's level | lines that do not express TTTY14 (26) vs lines expressing it (24) | 14.49× lower at baseline in the lines without TTTY14 | 5e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KDM5D, UTY, EIF1AY; co-absent with the target |
| [[ZFY]] | C | ZFY activity raises UTY's level | lines that do not express ZFY (29) vs lines expressing it (21) | 14.74× lower at baseline in the lines without ZFY | 6e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PRKY, RPS4Y1, LINC00278; co-absent with the target |
| [[NLGN4Y]] | C | NLGN4Y activity raises UTY's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 12.02× lower at baseline in the lines without NLGN4Y | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[MIR99AHG]] | C | MIR99AHG activity raises UTY's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 5.97× lower at baseline in the lines without MIR99AHG | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099; co-absent with the target |
| [[ZEB2]] | C | ZEB2 activity raises UTY's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 5.46× lower at baseline in the lines without ZEB2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16; co-absent with the target |
| [[CHL1]] | C | CHL1 activity raises UTY's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 7.18× lower at baseline in the lines without CHL1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168; co-absent with the target |
| [[LINC02941]] | C | LINC02941 activity raises UTY's level | lines that do not express LINC02941 (34) vs lines expressing it (16) | 4.88× lower at baseline in the lines without LINC02941 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, CHL1, COL19A1; co-absent with the target |
| [[COL5A2]] | C | COL5A2 activity raises UTY's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 3.74× lower at baseline in the lines without COL5A2 | 0.028 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2; co-absent with the target |
| [[PDE3A]] | C | PDE3A activity raises UTY's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 4.65× lower at baseline in the lines without PDE3A | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 3, C 19. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02398]] | B | UTY activity raises LINC02398's level | lines that do not express UTY (31) vs lines expressing it (19) | 2.31× lower at baseline in the lines without UTY | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY |
| [[KCNK2]] | B | UTY activity raises KCNK2's level | lines that do not express UTY (31) vs lines expressing it (19) | 1.90× lower at baseline in the lines without UTY | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY |
| [[RBMS3]] | B | UTY activity raises RBMS3's level | lines that do not express UTY (31) vs lines expressing it (19) | 3.45× lower at baseline in the lines without UTY | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY |
| [[DDX3Y]] | C | UTY activity raises DDX3Y's level | lines that do not express UTY (31) vs lines expressing it (19) | 19.46× lower at baseline in the lines without UTY | 6e-07 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY; co-absent with the target |
| [[KDM5D]] | C | UTY activity raises KDM5D's level | lines that do not express UTY (31) vs lines expressing it (19) | 15.30× lower at baseline in the lines without UTY | 1e-06 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY; co-absent with the target |
| [[PRKY]] | C | UTY activity raises PRKY's level | lines that do not express UTY (31) vs lines expressing it (19) | 13.41× lower at baseline in the lines without UTY | 9e-06 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY; co-absent with the target |
| [[USP9Y]] | C | UTY activity raises USP9Y's level | lines that do not express UTY (31) vs lines expressing it (19) | 18.21× lower at baseline in the lines without UTY | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY; co-absent with the target |
| [[TTTY14]] | C | UTY activity raises TTTY14's level | lines that do not express UTY (31) vs lines expressing it (19) | 6.76× lower at baseline in the lines without UTY | 6e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY; co-absent with the target |
| [[TTTY10]] | C | UTY activity raises TTTY10's level | lines that do not express UTY (31) vs lines expressing it (19) | 5.34× lower at baseline in the lines without UTY | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY; co-absent with the target |
| [[ZFY]] | C | UTY activity raises ZFY's level | lines that do not express UTY (31) vs lines expressing it (19) | 7.93× lower at baseline in the lines without UTY | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY; co-absent with the target |
| [[NLGN4Y]] | C | UTY activity raises NLGN4Y's level | lines that do not express UTY (31) vs lines expressing it (19) | 6.62× lower at baseline in the lines without UTY | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY; co-absent with the target |
| [[PDE3A]] | C | UTY activity raises PDE3A's level | lines that do not express UTY (31) vs lines expressing it (19) | 3.02× lower at baseline in the lines without UTY | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY; co-absent with the target |

## Where it sits

- **Module**: [[Module 177]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.771). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.4, 27.4); signed map (34.8, 38.0). **Vector** length 62.7, 21.0% of its response variance represented; |z| ≥ 3 in 441 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.9 | +10.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.9 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.6 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.7 | +2.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +4.2 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | -1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.7 | +0.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +3.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.3 | +1.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -8.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.2 | -4.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -2.1 | -3.6 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.0 | -5.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -2.0 | -5.0 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -2.0 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitously transcribed tetratricopeptide repeat containing, Y-linked |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Yq11.221 — chrY:13,234,577-13,480,673 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KDM6AL, KDM6C |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; Minor histocompatibility antigens; Lysine demethylase 6 family |
| Reactome | 3 pathways, smallest: HDMs demethylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [O14607](https://www.uniprot.org/uniprotkb/O14607) (Histone demethylase UTY):

> Male-specific histone demethylase that catalyzes trimethylated 'Lys-27' (H3K27me3) demethylation in histone H3. Has relatively low lysine demethylase activity.

**Summary**, from NCBI Gene [7404](https://www.ncbi.nlm.nih.gov/gene/7404):

> This gene encodes a protein containing tetratricopeptide repeats which are thought to be involved in protein-protein interactions. The encoded protein is also a minor histocompatibility antigen which may induce graft rejection of male stem cell grafts. A large number of alternatively spliced transcripts have been observed for this gene, but the full length nature of some of these variants has not been determined. [provided by RefSeq, Apr 2012]

**Accessions** — [HGNC:12638](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12638) · Entrez [7404](https://www.ncbi.nlm.nih.gov/gene/7404) · UniProt [O14607](https://www.uniprot.org/uniprotkb/O14607) · Ensembl [ENSG00000183878](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183878)

## Data

Gene col 11470: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11470); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11470, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11470]; `tensor/DDL_lfc|DDL_z.npy` [11470]; `embed/gene_vectors.npy` [11470]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11470 or target_col == 11470). Every well: [[UTY — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UTY.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
