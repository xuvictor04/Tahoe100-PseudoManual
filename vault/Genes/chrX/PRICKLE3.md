---
symbol: "PRICKLE3"
type: "gene"
col: 255
ensembl_id: "ENSG00000012211"
name: "prickle planar cell polarity protein 3"
location: "Xp11.23"
module: 59
arm: "+"
pooled_cpm: 9.66
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 5
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# PRICKLE3

*prickle planar cell polarity protein 3* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.45× (z +7.9, q 2e-12, up in 20 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.704× (z -5.3, q 7e-05, down in 17 of 33 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.633× (z -3.6, q 0.045, down in 16 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 0.150×, PANC-1 0.194×, SW480 0.343×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 0.259×, MIA PaCa-2 0.256×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.0776×; ⚠ cell-cycle shift, explains ~67% of this change); [[Neratinib (drug)]] 0.05 µM in 1 line (COLO 205 0.0740×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APBA3]] (+0.60, fdr 1e-05), [[GLIS2]] (+0.58, fdr 1e-05), [[IER5L]] (+0.56, fdr 1e-05); moves opposite to [[IPO7]] (-0.47, fdr 3e-05), [[ELK3]] (-0.47, fdr 4e-05), [[APPL2]] (-0.46, fdr 4e-04).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SCEL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 255.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +7.9 | 2e-12 | 20/43 (HEC-1-A, A549, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +6.5 | 2e-08 | 19/45 (SW480, NCI-H460, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +5.1 | 5e-05 | 19/41 (PANC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.005 | 16/43 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.24× | +3.2 | 0.17 | 7/46 (NCI-H460, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.23× | +3.1 | 0.17 | 12/39 (J82, AsPC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 255.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 0.150×, PANC-1 0.194×, SW480 0.343×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 0.259×, MIA PaCa-2 0.256×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.0776×; ⚠ cell-cycle shift, explains ~67% of this change); [[Neratinib (drug)]] 0.05 µM in 1 line (COLO 205 0.0740×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.704×** | -5.3 | 7e-05 | 17/33 (PANC-1, MIA PaCa-2, …) | all doses, flat | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.773×** | -3.9 | 0.031 | 15/46 (A-427, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.786×** | -3.6 | 0.045 | 10/45 (A-427, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.633×** | -3.6 | 0.045 | 16/44 (NCI-H460, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **0.783×** | -3.5 | 0.045 | 13/17 (NCI-H460, PANC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | 0.813× | -3.1 | 0.17 | 11/46 (NCI-H23, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 255. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 20.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.194× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[NCI-H460 (line)]] | wt | 11.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.150× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[A-172 (line)]] | wt | 2.59 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 0.05 µM 0.0631× (z -8.6) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 12.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +11.6) | — |
| [[C32 (line)]] | wt | 6.93 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0776× (z -9.7) ⚠ cell-cycle shift, explains ~67% of this change |
| [[COLO 205 (line)]] | alt | 6.71 | 0 | 1 | — | [[Neratinib (drug)]] 0.05 µM 0.0740× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 6.22 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +13.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[SW480 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.343× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[A-427 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 255), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APBA3]] | +0.60 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[GLIS2]] | +0.58 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[IER5L]] | +0.56 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[PPFIA3]] | +0.56 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[UAP1L1]] | +0.56 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[KREMEN2]] | +0.53 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[SOX12]] | +0.52 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[GRINA]] | +0.52 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[DVL2]] | +0.51 | +0.50 / +0.49 | both halves | 1e-05 | STRING 970 |
| [[S1PR2]] | +0.50 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[THAP3]] | +0.50 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[ZNF57]] | +0.48 | +0.46 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO7]] | -0.47 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[ELK3]] | -0.47 | -0.40 / -0.44 | both halves | 4e-05 |  |
| [[APPL2]] | -0.46 | -0.25 / -0.55 | both halves | 4e-04 |  |
| [[PARN]] | -0.46 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[TM9SF3]] | -0.45 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[XRCC5]] | -0.44 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[RPRD1A]] | -0.44 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[EIF3H]] | -0.44 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[CD226]] | -0.44 | -0.38 / -0.37 | both halves | 7e-05 |  |
| [[POLA1]] | -0.43 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[ACTL6A]] | -0.43 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[RECQL]] | -0.43 | -0.39 / -0.45 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCEL]] | B | SCEL activity lowers PRICKLE3's level | lines that do not express SCEL (35) vs lines expressing it (15) | 1.11× higher at baseline in the lines without SCEL | 0.067 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.503). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (24.8, -4.8); signed map (-3.5, 13.6). **Vector** length 63.7, 9.55% of its response variance represented; |z| ≥ 3 in 827 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.2 | +4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.0 | +7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +6.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.4 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.3 | +1.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | -5.3 | -5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.5 | -2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | -4.5 | -3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -1.9 | -2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.4 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | prickle planar cell polarity protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:49,174,802-49,186,528 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously LMO6 |
| Gene groups (HGNC) | Prickle planar cell polarity proteins; LIM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O43900](https://www.uniprot.org/uniprotkb/O43900) (Prickle planar cell polarity protein 3):

> Involved in the planar cell polarity (PCP) pathway that is essential for the polarization of epithelial cells during morphogenetic processes, including gastrulation and neurulation (By similarity). PCP is maintained by two molecular modules, the global and the core modules, PRICKLE3 being part of the core module (By similarity). Distinct complexes of the core module segregate to opposite sides of the cell, where they interact with the opposite complex in the neighboring cell at or near the …

**Summary**, from NCBI Gene [4007](https://www.ncbi.nlm.nih.gov/gene/4007):

> LIM domain only 6 is a three LIM domain-containing protein. The LIM domain is a cysteine-rich sequence motif that binds zinc atoms to form a specific protein-binding interface for protein-protein interactions. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6645](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6645) · Entrez [4007](https://www.ncbi.nlm.nih.gov/gene/4007) · UniProt [O43900](https://www.uniprot.org/uniprotkb/O43900) · Ensembl [ENSG00000012211](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000012211)

## Data

Gene col 255: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 255); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 255, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 255]; `tensor/DDL_lfc|DDL_z.npy` [255]; `embed/gene_vectors.npy` [255]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 255 or target_col == 255). Every well: [[PRICKLE3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRICKLE3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
