---
symbol: "ZFP1"
type: "gene"
col: 11548
ensembl_id: "ENSG00000184517"
name: "ZFP1 zinc finger protein"
location: "16q23.1"
module: 16
arm: "+"
pooled_cpm: 12.78
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 17
n_dd_up_clean: 4
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZFP1

*ZFP1 zinc finger protein* — 16q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.49× (z +6.8, q 8e-09, up in 21 of 43 measured lines) ⚠ toxic. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.30× (z +4.6, q 0.001, up in 12 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.586× (z -13.2, q 4e-37, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF615]] (+0.66, fdr 7e-06), [[ZNF22]] (+0.63, fdr 3e-05), [[ZNF845]] (+0.61, fdr 1e-05); moves opposite to [[EHBP1-AS1]] (-0.57, fdr 4e-05), [[CCNO-DT]] (-0.53, fdr 4e-05), [[CDK13]] (-0.51, fdr 5e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FSD1L]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11548.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +6.8 | 8e-09 | 21/43 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.6 | 0.001 | 12/48 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +4.2 | 0.005 | 10/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mozavaptan (drug)]] 0.05 µM |  | **1.28×** | +4.0 | 0.009 | 5/46 (PANC-1, A-427, …) | inconsistent across doses | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.015 | 7/48 (HS-578T, NCI-H460, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.8 | 0.015 | 12/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.22×** | +3.5 | 0.038 | 6/47 (SW1417, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.13× | +3.0 | 0.17 | 13/48 (Hs 766T, C-33 A, …) | top dose only | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11548.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.586×** | -13.2 | 4e-37 | 36/48 (Panc 03.27, SNU-423, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.490×** | -12.0 | 1e-30 | 31/46 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.571×** | -9.4 | 9e-19 | 32/48 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.470×** | -6.9 | 7e-10 | 20/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.702×** | -6.2 | 8e-08 | 19/45 (KATO III, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.705×** | -5.6 | 2e-06 | 14/29 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.737×** | -5.3 | 8e-06 | 22/39 (SW480, NCI-H2030, …) | all doses, flat | composition shift |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.768×** | -4.6 | 3e-04 | 12/44 (HCT15, NCI-H1792, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.692×** | -4.6 | 3e-04 | 14/44 (AN3 CA, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.779×** | -4.4 | 7e-04 | 16/47 (NCI-H23, C-33 A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.842× | -4.2 | 0.001 | 14/47 (MIA PaCa-2, LOX-IMVI, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.793×** | -4.1 | 0.002 | 16/46 (C-33 A, SNU-423, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.801×** | -3.7 | 0.009 | 8/25 (NCI-H2030, HEC-1-A, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **0.807×** | -3.6 | 0.013 | 17/43 (HOP62, NCI-H460, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.823×** | -3.4 | 0.023 | 9/47 (SW 1271, A-427, …) | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 0.05 µM |  | **0.810×** | -3.4 | 0.023 | 13/46 (RPMI-7951, CHP-212, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.699×** | -3.3 | 0.034 | 14/44 (LOX-IMVI, RPMI-7951, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | 0.837× | -3.1 | 0.054 | 10/47 (SW48, HCT15, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.839× | -3.1 | 0.061 | 13/46 (Hs 766T, H4, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | 0.840× | -3.0 | 0.063 | 10/48 (SNU-423, SW1417, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.836× | -3.0 | 0.064 | 5/47 (NCI-H23, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11548. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 13.0 | 0 | 3 | — | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM 0.165× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 18.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -12.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0724× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 19.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -13.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -11.3) |
| [[SNU-423 (line)]] | alt | 16.1 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -10.4) |
| [[C32 (line)]] | wt | 10.6 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0677× (z -13.0) |
| [[HOP62 (line)]] | alt | 16.0 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 11.2 | 0 | 2 | — | [[Orlistat (drug)]] 0.05 µM 0.112× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 20.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H460 (line)]] | wt | 16.0 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -8.7) |
| [[SW480 (line)]] | alt | 19.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.230× (z -13.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 16.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0561× (z -18.0) |
| [[CFPAC-1 (line)]] | alt | 7.94 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -8.6) |
| [[H4 (line)]] | wt | 13.7 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0779× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 9.56 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -9.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 11.8 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0804× (z -10.3) |
| [[HS-578T (line)]] | alt | 12.4 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.160× (z -10.8) |
| [[J82 (line)]] | alt | 14.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -8.5) |
| [[KATO III (line)]] | alt | 9.62 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.194× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -11.7) ⚠ cell-cycle shift, explains ~40% of this change |
| [[Panc 03.27 (line)]] | alt | 6.65 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -12.2) |
| [[PANC-1 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -9.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 15.6 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -12.0) |
| [[RPMI-7951 (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SHP-77 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11548), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF615]] | +0.66 | +0.58 / +0.68 | both halves | 7e-06 | same gene group |
| [[ZNF22]] | +0.63 | +0.45 / +0.67 | both halves | 3e-05 | same gene group |
| [[ZNF845]] | +0.61 | +0.53 / +0.70 | both halves | 1e-05 | same gene group |
| [[FEM1B]] | +0.60 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[KLHL9]] | +0.59 | +0.42 / +0.67 | both halves | 4e-05 |  |
| [[ZNF624]] | +0.59 | +0.49 / +0.59 | both halves | 1e-05 | same gene group |
| [[ZFP37]] | +0.59 | +0.49 / +0.64 | both halves | 1e-05 | same gene group |
| [[KBTBD6]] | +0.58 | +0.37 / +0.62 | both halves | 8e-05 |  |
| [[ZBTB39]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 | same gene group |
| [[HUS1]] | +0.58 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[ZNF445]] | +0.57 | +0.45 / +0.58 | both halves | 3e-05 | same gene group |
| [[ZNF484]] | +0.57 | +0.43 / +0.67 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHBP1-AS1]] | -0.57 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[CCNO-DT]] | -0.53 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[CDK13]] | -0.51 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[NCK1-DT]] | -0.51 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[BIRC6-AS2-1]] | -0.50 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[TICAM2-AS1]] | -0.50 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[GOLGA8B]] | -0.50 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[C2]] | -0.49 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[CATSPER2P1]] | -0.49 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[HOXB-AS3]] | -0.49 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[C12orf73]] | -0.49 | -0.37 / -0.49 | both halves | 9e-05 |  |
| [[ARIH2]] | -0.49 | -0.37 / -0.51 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSD1L]] | C | FSD1L activity raises ZFP1's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 2.13× lower at baseline in the lines without FSD1L | 0.042 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |
| [[CATSPER2P1]] | C | CATSPER2P1 activity raises ZFP1's level | lines that do not express CATSPER2P1 (3) vs lines expressing it (47) | 1.32× lower at baseline in the lines without CATSPER2P1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FAM182B, SLFNL1-AS1, ENSG00000287400; maybe low, not absent; its own permutation p |
| [[TBC1D19]] | C | TBC1D19 activity raises ZFP1's level | lines that do not express TBC1D19 (4) vs lines expressing it (46) | 1.82× lower at baseline in the lines without TBC1D19 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.516). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-34.2, 10.7); signed map (-0.6, -28.3). **Vector** length 74.6, 12.3% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.1 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.4 | +6.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.0 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +0.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +3.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +1.5 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -12.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -13.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -3.5 | -5.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.2 | -4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -2.1 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.7 | -4.6 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.6 | -1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | ZFP1 zinc finger protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.1 — chr16:75,148,494-75,172,236 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PITA, FLJ34243, ZNF475 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P2D0](https://www.uniprot.org/uniprotkb/Q6P2D0) (Zinc finger protein 1 homolog):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [162239](https://www.ncbi.nlm.nih.gov/gene/162239):

> This gene belongs to the zinc finger protein family. Some members of this family bind to DNA by zinc-mediated secondary structures called zinc fingers, and are involved in transcriptional regulation. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:23328](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23328) · Entrez [162239](https://www.ncbi.nlm.nih.gov/gene/162239) · UniProt [Q6P2D0](https://www.uniprot.org/uniprotkb/Q6P2D0) · Ensembl [ENSG00000184517](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184517)

## Data

Gene col 11548: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11548); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11548, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11548]; `tensor/DDL_lfc|DDL_z.npy` [11548]; `embed/gene_vectors.npy` [11548]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11548 or target_col == 11548). Every well: [[ZFP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
