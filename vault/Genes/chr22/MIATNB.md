---
symbol: "MIATNB"
type: "gene"
col: 14411
ensembl_id: "ENSG00000244625"
name: "MIAT neighbor"
location: "22q12.1"
module: 17
arm: "-"
pooled_cpm: 24.33
n_lines_expressing: 47
n_dd_up: 3
n_dd_down: 21
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# MIATNB

*MIAT neighbor* — 22q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 1.38× (z +4.1, q 0.015, up in 21 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.417× (z -11.2, q 3e-26, down in 40 of 45 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF407]] (+0.69, fdr 7e-06), [[GLIPR1-AS1]] (+0.68, fdr 4e-05), [[SLC25A53]] (+0.66, fdr 1e-05); moves opposite to [[SUGT1P4-STRA6LP]] (-0.65, fdr 1e-05), [[ALAD]] (-0.65, fdr 1e-05), [[BBS5]] (-0.63, fdr 3e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[POU6F1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14411.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **1.38×** | +4.1 | 0.015 | 21/44 (A498, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.015 | 20/44 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.34×** | +3.5 | 0.077 | 12/44 (RKO, SW480, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 1.28× | +3.2 | 0.20 | 3/45 (NCI-H2030, Panc 03.27, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.27× | +3.1 | 0.22 | 8/45 (CFPAC-1, RKO, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 1.27× | +3.0 | 0.22 | 19/45 (C32, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14411.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.417×** | -11.2 | 3e-26 | 40/45 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.404×** | -11.1 | 3e-26 | 37/44 (NCI-H2030, A-427, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.428×** | -10.8 | 7e-25 | 40/45 (NCI-H1573, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.438×** | -10.5 | 1e-23 | 41/45 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.709×** | -6.2 | 7e-08 | 26/44 (A498, SW1417, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.599×** | -6.0 | 2e-07 | 23/35 (KATO III, SHP-77, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.645×** | -5.6 | 2e-06 | 29/45 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.638×** | -5.5 | 3e-06 | 24/42 (SW48, COLO 205, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.591×** | -5.3 | 6e-06 | 26/45 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **0.619×** | -4.9 | 6e-05 | 22/41 (KATO III, NCI-H460, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **0.692×** | -4.5 | 3e-04 | 18/31 (NCI-H1573, NCI-H2030, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.717×** | -4.2 | 0.001 | 23/44 (C-33 A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.795×** | -4.1 | 0.002 | 22/45 (RKO, LOX-IMVI, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.731×** | -4.0 | 0.003 | 21/44 (NCI-H2030, Panc 03.27, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.575×** | -3.7 | 0.009 | 18/45 (COLO 205, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.818×** | -3.6 | 0.011 | 21/45 (NCI-H2347, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.766×** | -3.4 | 0.024 | 19/45 (hTERT-HPNE, H4, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.768×** | -3.4 | 0.024 | 19/45 (Panc 03.27, NCI-H2030, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.765×** | -3.3 | 0.029 | 15/44 (AsPC-1, AN3 CA, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.840× | -3.1 | 0.048 | 15/45 (SW1417, RKO, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.825×** | -3.1 | 0.056 | 17/45 (A-427, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14411. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 60.3 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.231× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 43.5 | 0 | 5 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0828× (z -17.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H23 (line)]] | alt | 37.4 | 0 | 4 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -9.4) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.299× (z -8.8) |
| [[SW480 (line)]] | alt | 37.5 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.305× (z -10.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.328× (z -10.4) |
| [[A498 (line)]] | wt | 22.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -12.2) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.298× (z -8.7) |
| [[RKO (line)]] | wt | 39.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -11.2) |
| [[A549 (line)]] | wt | 16.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -9.1) ⚠ cell-cycle shift, explains ~75% of this change |
| [[HCT15 (line)]] | alt | 36.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[HEC-1-A (line)]] | alt | 21.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -9.9) ⚠ cell-cycle shift, explains ~75% of this change |
| [[hTERT-HPNE (line)]] | wt | 18.3 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0743× (z -11.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[KATO III (line)]] | alt | 34.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[MIA PaCa-2 (line)]] | alt | 17.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +8.8) | [[Harringtonine (drug)]] 5 µM 0.163× (z -10.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H460 (line)]] | wt | 27.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[Panc 03.27 (line)]] | alt | 47.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -9.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.275× (z -9.3) |
| [[SW48 (line)]] | wt | 16.7 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0737× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~37% of this change · without an alert: [[Omeprazole (drug)]] 0.5 µM 0.0984× (z -9.5) |
| [[A-427 (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0636× (z -16.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[C32 (line)]] | wt | 32.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[COLO 205 (line)]] | alt | 22.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.194× (z -8.8) |
| [[H4 (line)]] | wt | 24.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0809× (z -11.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HOP62 (line)]] | alt | 17.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.287× (z -8.8) |
| [[Hs 766T (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.124× (z -12.0) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 16.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.228× (z -8.8) |
| [[LS 180 (line)]] | wt | 36.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.302× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -8.5) ⚠ cell-cycle shift, explains ~75% of this change |
| [[RPMI-7951 (line)]] | alt | 27.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change |
| [[SHP-77 (line)]] | alt | 38.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SK-MEL-2 (line)]] | alt | 55.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SW1417 (line)]] | alt | 27.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -9.9) ⚠ cell-cycle shift, explains ~75% of this change |
| [[A-172 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.79 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14411), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF407]] | +0.69 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[GLIPR1-AS1]] | +0.68 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[SLC25A53]] | +0.66 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[PRDM15]] | +0.65 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[TMEM11-DT]] | +0.64 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[PDK1-AS1]] | +0.62 | +0.38 / +0.65 | both halves | 6e-05 |  |
| [[HCG18]] | +0.62 | +0.44 / +0.64 | both halves | 3e-05 | same gene group |
| [[TIMM23B-AGAP6]] | +0.61 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[PRDM10]] | +0.61 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[ENOX2]] | +0.60 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[MSRA]] | +0.60 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[HCFC1]] | +0.60 | +0.39 / +0.56 | both halves | 5e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUGT1P4-STRA6LP]] | -0.65 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[ALAD]] | -0.65 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[BBS5]] | -0.63 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[STRA6LP]] | -0.62 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[NDUFB10]] | -0.62 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[PRPF39]] | -0.60 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[MRPS31P4]] | -0.60 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[HPF1]] | -0.59 | -0.37 / -0.58 | both halves | 7e-05 |  |
| [[SKIC3]] | -0.58 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[EHMT2]] | -0.57 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[THYN1]] | -0.57 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[CAT]] | -0.57 | -0.44 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POU6F1]] | C | MIATNB activity raises POU6F1's level | lines that do not express MIATNB (3) vs lines expressing it (47) | 2.19× lower at baseline in the lines without MIATNB | 0.039 | ⚠ few lines (3 vs 47); across organs; also absent: MIAT, LRP1, KLF2 |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.655). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (8.9, 8.3); signed map (19.0, -2.1). **Vector** length 88.8, 20.1% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.5 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.1 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.5 | +0.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | +6.2 | -4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | +5.6 | -4.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | +1.6 | +2.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.8 | -11.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.6 | -11.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.9 | -5.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -3.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.5 | -4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -0.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | MIAT neighbor |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 22q12.1 — chr22:26,672,747-26,780,893 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50731](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50731) · Entrez [102724827](https://www.ncbi.nlm.nih.gov/gene/102724827) · Ensembl [ENSG00000244625](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244625)

## Data

Gene col 14411: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14411); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14411, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14411]; `tensor/DDL_lfc|DDL_z.npy` [14411]; `embed/gene_vectors.npy` [14411]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14411 or target_col == 14411). Every well: [[MIATNB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIATNB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
