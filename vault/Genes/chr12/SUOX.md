---
symbol: "SUOX"
type: "gene"
col: 6314
ensembl_id: "ENSG00000139531"
name: "sulfite oxidase"
location: "12q13.2"
module: 103
arm: "+"
pooled_cpm: 4.29
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 16
n_dd_up_clean: 14
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# SUOX

*sulfite oxidase* — 12q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.80× (z +19.0, q 0e+00, up in 35 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.474× (z -9.6, q 4e-19, down in 28 of 46 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IKZF4]] (+0.74, fdr 7e-06, ⚠ same locus), [[TNFSF12]] (+0.60, fdr 1e-05), [[RAB5B]] (+0.59, fdr 1e-04, ⚠ read-through risk), [[KLC4]] (+0.58, fdr 1e-05), [[SPAG4]] (+0.56, fdr 3e-05); moves opposite to [[CBX6]] (-0.52, fdr 1e-04), [[SERBP1]] (-0.51, fdr 3e-04), [[GNPNAT1]] (-0.51, fdr 2e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6314.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.80×** | +19.0 | 0e+00 | 35/38 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.53×** | +12.1 | 2e-31 | 40/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.21×** | +10.3 | 2e-22 | 33/46 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +8.0 | 2e-13 | 23/47 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +7.5 | 6e-12 | 16/40 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.7 | 1e-06 | 14/39 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.53×** | +5.4 | 6e-06 | 10/25 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.8 | 9e-05 | 12/47 (HEC-1-A, A-172, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.6 | 2e-04 | 11/34 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.26×** | +4.3 | 0.001 | 4/45 (NCI-H23, SW480, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.006 | 2/46 (SK-MEL-2, KATO III) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.20×** | +3.5 | 0.023 | 9/46 (AsPC-1, SW1417, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +3.5 | 0.023 | 0/7 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.042 | 4/46 (CHP-212, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.057 | 2/47 (SW1417, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.090 | 10/44 (AsPC-1, A498, …) | all doses, flat |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.090 | 4/33 (HT-29, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6314.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.474×** | -9.6 | 4e-19 | 28/46 (PANC-1, A-427, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.577×** | -7.2 | 2e-10 | 19/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.618×** | -6.3 | 7e-08 | 19/38 (PANC-1, SHP-77, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.637×** | -5.9 | 7e-07 | 15/46 (PANC-1, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~16% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.662×** | -5.2 | 3e-05 | 15/43 (SW 900, PANC-1, …) | two highest doses | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.681×** | -4.9 | 7e-05 | 21/44 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.699×** | -4.5 | 6e-04 | 15/31 (NCI-H2030, A549, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Entecavir (monohydrate) (drug)]] 0.05 µM |  | **0.698×** | -4.3 | 0.001 | 16/42 (A-172, NCI-H2030, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.537×** | -4.2 | 0.001 | 10/43 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.723×** | -4.2 | 0.001 | 7/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.728×** | -4.1 | 0.002 | 12/47 (J82, RKO, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.738×** | -3.9 | 0.004 | 11/44 (HepG2/C3A, NCI-H23, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.773×** | -3.3 | 0.038 | 11/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.776×** | -3.3 | 0.042 | 7/43 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.778×** | -3.2 | 0.044 | 7/42 (A-427, PANC-1, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.772×** | -3.2 | 0.054 | 9/43 (J82, SNU-423, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6314. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.10 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.232× (z -8.7) |
| [[J82 (line)]] | alt | 2.69 | 0 | 2 | — | [[Tubulin inhibitor 6 (drug)]] 0.05 µM 0.0608× (z -8.8) |
| [[LoVo (line)]] | wt | 4.53 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 5.50 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0753× (z -11.0) |
| [[SW480 (line)]] | alt | 7.25 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.63× (z +9.0) | — |
| [[A498 (line)]] | wt | 3.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +10.1) | — |
| [[A549 (line)]] | wt | 3.62 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0702× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 4.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 3.26 | 0 | 1 (1 ⚠) | — | [[Trifluridine (drug)]] 0.5 µM 0.0725× (z -8.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[KATO III (line)]] | alt | 3.20 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0634× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 5.37 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0895× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 5.90 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0650× (z -9.3) |
| [[SW1417 (line)]] | alt | 4.61 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0814× (z -9.0) |
| [[A-427 (line)]] | wt | 8.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6314), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 7 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IKZF4]] | +0.74 | +0.70 / +0.76 | both halves | 7e-06 | STRING 416; ⚠ same locus (1.0 kb, same strand: neighbours can correlate without regulation) |
| [[TNFSF12]] | +0.60 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[RAB5B]] | +0.59 | +0.36 / +0.59 | both halves | 1e-04 | STRING 601; ⚠ **readthrough risk**: this gene lies 0.5 kb 3′ of RAB5B on the same strand (can correlate by spillover, not regulation) |
| [[KLC4]] | +0.58 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[SPAG4]] | +0.56 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[RSPH9]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[ZNF446]] | +0.54 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[PBXIP1]] | +0.53 | +0.32 / +0.64 | both halves | 2e-04 |  |
| [[U2AF1L4]] | +0.52 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[CD27-AS1]] | +0.52 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[NRL]] | +0.52 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[OGFOD2]] | +0.51 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[PRRT1]] | +0.51 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[MYH7B]] | +0.51 | +0.48 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBX6]] | -0.52 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[SERBP1]] | -0.51 | -0.29 / -0.45 | both halves | 3e-04 |  |
| [[GNPNAT1]] | -0.51 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[DNAH14]] | -0.50 | -0.17 / -0.49 | ⚠ not reproduced | 0.001 |  |
| [[UBE2E2]] | -0.50 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[PCNX2]] | -0.49 | -0.20 / -0.46 | ⚠ not reproduced | 8e-04 |  |
| [[JPH1]] | -0.48 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[CEP83]] | -0.48 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[TACC1]] | -0.47 | -0.19 / -0.48 | ⚠ not reproduced | 8e-04 |  |
| [[CIAO1]] | -0.47 | -0.10 / -0.57 | ⚠ one half (not replicated) | 0.003 |  |
| [[DDX10]] | -0.46 | -0.26 / -0.49 | both halves | 4e-04 |  |
| [[AIG1]] | -0.46 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[CMSS1]] | -0.46 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[SACS]] | -0.45 | -0.27 / -0.53 | both halves | 3e-04 |  |
| [[ATIC]] | -0.44 | -0.24 / -0.52 | both halves | 4e-04 |  |
| [[CDK14]] | -0.44 | -0.31 / -0.49 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SUOX's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[F2]] | B | F2 activity raises SUOX's level | lines that do not express F2 (11) vs lines expressing it (39) | 1.27× lower at baseline in the lines without F2 | 0.041 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FGF11]] | B | FGF11 activity raises SUOX's level | lines that do not express FGF11 (9) vs lines expressing it (41) | 1.26× lower at baseline in the lines without FGF11 | 0.089 | ⚠ within organs, on part of the lines; also absent: C9orf64, CYB5A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.291). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.4, -31.7); signed map (2.1, 12.6). **Vector** length 48.3, 5.38% of its response variance represented; |z| ≥ 3 in 1,130 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +19.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.9 | +7.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | +1.7 | +5.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | +1.7 | +1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.7 | +3.5 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.5 | +4.3 |
|  | [[Saquinavir (drug)]] 0.5 µM |  | +1.0 | +0.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.0 | +0.8 |
|  | [[Berbamine (drug)]] 5 µM |  | +1.0 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +1.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.0 | -5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -1.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.3 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -1.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -9.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | +1.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | sulfite oxidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.2 — chr12:55,997,180-56,006,641 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cytochrome b5 domain containing; Oxidoreductases |
| Reactome | 4 pathways, smallest: Sulfide oxidation to sulfate; Degradation of cysteine and homocysteine; Sulfur amino acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P51687](https://www.uniprot.org/uniprotkb/P51687) (Sulfite oxidase, mitochondrial):

> Catalyzes the oxidation of sulfite to sulfate, the terminal reaction in the oxidative degradation of sulfur-containing amino acids (By similarity). Can run in reverse direction and reduce nitrite to nitric oxide under physiologically relevant conditions, such as hypoxia.

**Summary**, from NCBI Gene [6821](https://www.ncbi.nlm.nih.gov/gene/6821):

> Sulfite oxidase is a homodimeric protein localized to the intermembrane space of mitochondria. Each subunit contains a heme domain and a molybdopterin-binding domain. The enzyme catalyzes the oxidation of sulfite to sulfate, the final reaction in the oxidative degradation of the sulfur amino acids cysteine and methionine. Sulfite oxidase deficiency results in neurological abnormalities which are often fatal at an early age. Alternative splicing results in multiple transcript variants encoding …

**Accessions** — [HGNC:11460](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11460) · Entrez [6821](https://www.ncbi.nlm.nih.gov/gene/6821) · UniProt [P51687](https://www.uniprot.org/uniprotkb/P51687) · Ensembl [ENSG00000139531](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139531)

## Data

Gene col 6314: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6314); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6314, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6314]; `tensor/DDL_lfc|DDL_z.npy` [6314]; `embed/gene_vectors.npy` [6314]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6314 or target_col == 6314). Every well: [[SUOX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUOX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
