---
symbol: "ERCC6L"
type: "gene"
col: 11866
ensembl_id: "ENSG00000186871"
name: "ERCC excision repair 6 like DNA helicase"
location: "Xq13.1"
module: 22
arm: "+"
pooled_cpm: 12.04
n_lines_expressing: 49
n_dd_up: 27
n_dd_down: 16
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# ERCC6L

*ERCC excision repair 6 like DNA helicase* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (22 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.36× (z +11.5, q 1e-27, up in 41 of 46 measured lines) ⚠ cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.05 µM: 1.42× (z +4.4, q 4e-04, up in 15 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.722× (z -6.2, q 4e-07, down in 23 of 47 measured lines) ⚠ cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.788× (z -4.5, q 7e-04, down in 17 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO5]] (+0.84, fdr 7e-06), [[PLK4]] (+0.84, fdr 7e-06), [[NCAPG]] (+0.83, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 24 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11866.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **2.36×** | +11.5 | 1e-27 | 41/46 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **2.31×** | +11.2 | 2e-26 | 40/46 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **2.05×** | +9.6 | 2e-19 | 33/46 (SW480, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.64×** | +9.3 | 2e-18 | 29/45 (A498, NCI-H1792, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.75×** | +7.5 | 9e-12 | 23/46 (PANC-1, NCI-H23, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.35×** | +6.0 | 2e-07 | 21/46 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~75% of this change | **1.56×** | +5.9 | 3e-07 | 16/36 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.54×** | +5.8 | 6e-07 | 21/46 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.36×** | +5.7 | 7e-07 | 21/47 (NCI-H23, NCI-H2347, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.50×** | +5.4 | 4e-06 | 18/45 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.32×** | +5.2 | 1e-05 | 20/44 (LoVo, C32, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.44×** | +4.9 | 5e-05 | 19/43 (PANC-1, SNU-1, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.9 | 5e-05 | 6/47 (A-172, RKO, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.44×** | +4.8 | 5e-05 | 15/45 (PANC-1, SNU-423, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.42×** | +4.6 | 1e-04 | 13/46 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.42×** | +4.4 | 4e-04 | 15/43 (MIA PaCa-2, AsPC-1, …) | all doses, flat | low cells (technical?) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.32×** | +3.7 | 0.006 | 13/47 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.64×** | +3.4 | 0.014 | 5/42 (A498, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.27×** | +2.9 | 0.068 | 11/46 (SW 900, C32, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.24×** | +2.8 | 0.092 | 8/46 (HOP62, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11866.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.722×** | -6.2 | 4e-07 | 23/47 (SW480, HT-29, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.638×** | -6.0 | 5e-07 | 25/44 (A498, NCI-H460, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.628×** | -5.9 | 8e-07 | 21/45 (A-427, LS 180, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.675×** | -5.3 | 2e-05 | 21/36 (NCI-H2030, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.679×** | -5.0 | 7e-05 | 8/21 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.788×** | -4.5 | 7e-04 | 17/47 (HCT15, RKO, …) | rises with dose | position effect removed |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.717×** | -4.4 | 7e-04 | 16/44 (CFPAC-1, COLO 205, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.728×** | -4.2 | 0.002 | 16/47 (Hs 766T, NCI-H460, …) | all doses, flat |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.654×** | -4.1 | 0.003 | 13/47 (LOX-IMVI, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.815×** | -3.9 | 0.006 | 23/46 (A498, A-427, …) | all doses, flat | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.675×** | -3.8 | 0.009 | 18/41 (SW48, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Cepharanthine (drug)]] 0.5 µM |  | **0.767×** | -3.6 | 0.018 | 13/44 (SNU-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.760×** | -3.5 | 0.023 | 9/47 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.765×** | -3.3 | 0.037 | 12/27 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Rapamycin (drug)]] 5 µM |  | 0.847× | -3.1 | 0.063 | 11/47 (RPMI-7951, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.818×** | -3.1 | 0.063 | 13/46 (A-427, AN3 CA, …) | rises with dose | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 0.850× | -3.1 | 0.066 | 6/47 (Hs 766T, SW 900, …) | rises with dose | position effect removed |
| [[palbociclib (drug)]] 5 µM |  | **0.646×** | -3.1 | 0.067 | 9/43 (HOP62, SW480, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.70 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11866. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 14.4 | 0 | 3 (3 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0754× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 10.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.97× (z +14.0) ⚠ cell-cycle shift, explains ~30% of this change | [[Selinexor (drug)]] 5 µM 0.178× (z -15.1) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 11.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0595× (z -9.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.149× (z -9.1) |
| [[J82 (line)]] | alt | 15.2 | 0 | 2 (1 ⚠) | — | [[Thymol (drug)]] 0.5 µM 0.168× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 8.11 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW480 (line)]] | alt | 19.3 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 3.27× (z +9.0) ⚠ cell-cycle shift, explains ~52% of this change | [[Thymol (drug)]] 0.5 µM 0.301× (z -9.1) |
| [[A-427 (line)]] | wt | 24.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.301× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 3.69 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.13× (z +9.1) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[C32 (line)]] | wt | 8.04 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HEC-1-A (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -13.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 13.9 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.335× (z -8.8) |
| [[LoVo (line)]] | wt | 4.92 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.92× (z +12.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1792 (line)]] | alt | 3.56 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.60× (z +9.1) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2030 (line)]] | alt | 7.86 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0794× (z -12.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 7.97 | 0 | 1 | — | [[Adenosine (drug)]] 0.05 µM 0.0599× (z -8.5) |
| [[SW48 (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0539× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11866), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO5]] | +0.84 | +0.82 / +0.85 | both halves | 7e-06 | pathway: Mitotic Metaphase and Anaphase; STRING 575 |
| [[PLK4]] | +0.84 | +0.82 / +0.84 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 562 |
| [[NCAPG]] | +0.83 | +0.86 / +0.80 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 716 |
| [[KIFC1]] | +0.83 | +0.80 / +0.81 | both halves | 7e-06 | STRING 476 |
| [[MKI67]] | +0.82 | +0.84 / +0.79 | both halves | 7e-06 | STRING 485 |
| [[NCAPH]] | +0.82 | +0.85 / +0.80 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 709 |
| [[CDCA5]] | +0.82 | +0.79 / +0.82 | both halves | 7e-06 | pathway: Mitotic Anaphase; STRING 652 |
| [[SKA3]] | +0.82 | +0.88 / +0.78 | both halves | 7e-06 | STRING 743 |
| [[POLQ]] | +0.82 | +0.83 / +0.77 | both halves | 7e-06 | STRING 486 |
| [[AURKB]] | +0.81 | +0.81 / +0.77 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 614 |
| [[KIF11]] | +0.81 | +0.83 / +0.80 | both halves | 7e-06 | STRING 650 |
| [[SHCBP1]] | +0.81 | +0.79 / +0.80 | both halves | 7e-06 | STRING 580 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises ERCC6L's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.24× lower at baseline in the lines without CDC25A | 0.014 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises ERCC6L's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.43× lower at baseline in the lines without E2F8 | 0.018 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises ERCC6L's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.60× lower at baseline in the lines without TCF19 | 0.023 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[PIMREG]] | B | PIMREG activity raises ERCC6L's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.42× lower at baseline in the lines without PIMREG | 0.024 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises ERCC6L's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.49× lower at baseline in the lines without NDC80 | 0.035 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises ERCC6L's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.77× lower at baseline in the lines without AURKB | 0.049 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[SAPCD2]] | C | SAPCD2 activity raises ERCC6L's level | lines that do not express SAPCD2 (3) vs lines expressing it (47) | 2.38× lower at baseline in the lines without SAPCD2 | 0.067 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent |
| [[PBK]] | C | PBK activity raises ERCC6L's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.65× lower at baseline in the lines without PBK | 0.072 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises ERCC6L's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.32× lower at baseline in the lines without MCM10 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[C21orf58]], [[SKA3]] | C | C21orf58, SKA3 activity raises ERCC6L's level | lines that do not express C21orf58, SKA3 (3) vs lines expressing them (47) | 2.90× lower at baseline in the lines without C21orf58, SKA3 | 0.097 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.788). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.9, -52.2); signed map (-45.7, -43.9). **Vector** length 108, 26.1% of its response variance represented; |z| ≥ 3 in 1,118 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.64 to 60); *DREAM G2/M down* (control, mean cos +0.67 to 28); *E2F targets* (hallmark, mean cos +0.61 to 46).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~75% of this change | +4.5 | +5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.7 | +9.3 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | +3.6 | +5.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +3.4 | +11.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +3.3 | +11.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.6 | +3.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +4.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.0 | +1.6 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.0 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +1.5 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.9 | -6.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | -4.5 | -5.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.9 | -3.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.3 | -4.5 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~86% of this change | -3.2 | -4.2 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -2.5 | -3.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | -2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -3.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | ERCC excision repair 6 like DNA helicase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:72,204,657-72,239,027 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20105, PICH, RAD26L |
| Gene groups (HGNC) | SNF2 related family |
| Reactome | 17 pathways, smallest: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores; EML4 and NUDC in mitotic spindle formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2NKX8](https://www.uniprot.org/uniprotkb/Q2NKX8) (DNA excision repair protein ERCC-6-like):

> DNA helicase that acts as a tension sensor that associates with catenated DNA which is stretched under tension until it is resolved during anaphase. Functions as ATP-dependent DNA translocase. Can promote Holliday junction branch migration (in vitro).

**Summary**, from NCBI Gene [54821](https://www.ncbi.nlm.nih.gov/gene/54821):

> This gene encodes a member of the SWItch/Sucrose Non-Fermentable (SWI/SNF2) family of proteins, and contains a SNF2-like ATPase domain and a PICH family domain. One distinguishing feature of this SWI/SNF protein family member is that during interphase, the protein is excluded from the nucleus, and only associates with chromatin after the nuclear envelope has broken down. This protein is a DNA translocase that is thought to bind double-stranded DNA that is exposed to stretching forces, such as …

**Accessions** — [HGNC:20794](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20794) · Entrez [54821](https://www.ncbi.nlm.nih.gov/gene/54821) · UniProt [Q2NKX8](https://www.uniprot.org/uniprotkb/Q2NKX8) · Ensembl [ENSG00000186871](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186871)

## Data

Gene col 11866: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11866); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11866, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11866]; `tensor/DDL_lfc|DDL_z.npy` [11866]; `embed/gene_vectors.npy` [11866]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11866 or target_col == 11866). Every well: [[ERCC6L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERCC6L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
