---
symbol: "ZNF84"
type: "gene"
col: 12517
ensembl_id: "ENSG00000198040"
name: "zinc finger protein 84"
location: "12q24.33"
module: 17
arm: "+"
pooled_cpm: 43.91
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ZNF84

*zinc finger protein 84* — 12q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.20× (z +7.3, q 2e-10, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.460× (z -14.7, q 0e+00, down in 34 of 40 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (NCI-H23 0.112×, SK-MEL-2 0.186×, NCI-H460 0.299×, J82 0.248×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 5 µM in 6 lines (MIA PaCa-2 0.0784×, A549 0.0759×, A-427 0.141×, NCI-H460 0.332×, …; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.283×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF12]] (+0.61, fdr 3e-05), [[ZNF112]] (+0.55, fdr 3e-05), [[TRIT1]] (+0.54, fdr 4e-05); moves opposite to [[PSME4]] (-0.51, fdr 3e-05), [[PDLIM5]] (-0.46, fdr 5e-05), [[TJP1]] (-0.44, fdr 6e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[ZNF71]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12517.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.20×** | +7.3 | 2e-10 | 32/48 (NCI-H460, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.89×** | +5.9 | 1e-06 | 25/47 (MIA PaCa-2, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.20×** | +5.1 | 6e-05 | 17/47 (A498, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.5 | 0.001 | 18/47 (A498, NCI-H1573, …) | rises with dose |  |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.23×** | +4.1 | 0.004 | 19/47 (SNU-423, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.23×** | +4.1 | 0.004 | 19/47 (C32, NCI-H460, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.1 | 0.004 | 14/35 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Roxadustat (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.004 | 20/47 (C32, NCI-H460, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.013 | 15/47 (LoVo, HOP62, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +3.7 | 0.013 | 19/47 (RKO, A-427, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.21×** | +3.6 | 0.015 | 18/46 (NCI-H2030, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.023 | 9/47 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.4 | 0.034 | 16/47 (J82, NCI-H1792, …) | two highest doses |  |
| [[Erlotinib (drug)]] 5 µM |  | 1.19× | +3.3 | 0.043 | 16/46 (HEC-1-A, BT-474, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 1.17× | +3.1 | 0.080 | 11/47 (A498, SK-MEL-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12517.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (NCI-H23 0.112×, SK-MEL-2 0.186×, NCI-H460 0.299×, J82 0.248×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 5 µM in 6 lines (MIA PaCa-2 0.0784×, A549 0.0759×, A-427 0.141×, NCI-H460 0.332×, …; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.283×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.460×** | -14.7 | 0e+00 | 34/40 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.506×** | -13.4 | 2e-38 | 38/47 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.683×** | -7.2 | 1e-10 | 31/46 (C32, AN3 CA, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.920× | -5.5 | 7e-06 | 0/48 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.811×** | -4.0 | 0.009 | 18/47 (C-33 A, LOX-IMVI, …) | top dose only | composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.795× | -3.2 | 0.12 | 11/47 (SHP-77, AN3 CA, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.851× | -3.2 | 0.12 | 11/47 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.895× | -3.0 | 0.19 | 15/47 (MIA PaCa-2, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12517. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 70.1 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[C-33 A (line)]] | alt | 82.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[C32 (line)]] | wt | 44.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[CFPAC-1 (line)]] | alt | 37.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[CHP-212 (line)]] | wt | 68.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change |
| [[J82 (line)]] | alt | 53.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 84.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0784× (z -27.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 80.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.413× (z -10.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 67.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 77.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 38.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 56.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -19.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 22.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -11.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 41.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0759× (z -23.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 35.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1573 (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 41.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.66× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | — |
| [[NCI-H23 (line)]] | alt | 65.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -21.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 47.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[RPMI-7951 (line)]] | alt | 52.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 82.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SNU-1 (line)]] | wt | 36.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[AN3 CA (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 40.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12517), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF12]] | +0.61 | +0.46 / +0.67 | both halves | 3e-05 | same gene group |
| [[ZNF112]] | +0.55 | +0.44 / +0.56 | both halves | 3e-05 | same gene group |
| [[TRIT1]] | +0.54 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[ZNF790]] | +0.53 | +0.37 / +0.54 | both halves | 8e-05 | same gene group |
| [[EIF3D]] | +0.51 | +0.49 / +0.39 | both halves | 5e-05 |  |
| [[ZNF14]] | +0.51 | +0.50 / +0.54 | both halves | 1e-05 | same gene group |
| [[WDR89]] | +0.50 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[ZNF571]] | +0.50 | +0.39 / +0.54 | both halves | 6e-05 | same gene group |
| [[TRIM32]] | +0.50 | +0.35 / +0.54 | both halves | 1e-04 |  |
| [[FOXO3B]] | +0.50 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[ZNF383]] | +0.49 | +0.42 / +0.42 | both halves | 4e-05 | same gene group |
| [[CLK2]] | +0.49 | +0.46 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME4]] | -0.51 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[PDLIM5]] | -0.46 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[TJP1]] | -0.44 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[SLC30A7]] | -0.44 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[CLEC16A]] | -0.41 | -0.23 / -0.40 | both halves | 5e-04 |  |
| [[ARHGAP26]] | -0.41 | -0.33 / -0.33 | both halves | 1e-04 |  |
| [[NUMB]] | -0.41 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[ZSWIM6]] | -0.41 | -0.38 / -0.38 | both halves | 6e-05 |  |
| [[TAOK3]] | -0.41 | -0.31 / -0.37 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF71]] | B | ZNF71 activity raises ZNF84's level | lines that do not express ZNF71 (15) vs lines expressing it (35) | 1.91× lower at baseline in the lines without ZNF71 | 0.004 | ⚠ within organs, on part of the lines; also absent: ZIM2-AS1, ZNF470, ZFP28 |
| [[ZNF891]] | B | ZNF891 activity raises ZNF84's level | lines that do not express ZNF891 (7) vs lines expressing it (43) | 2.35× lower at baseline in the lines without ZNF891 | 0.020 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KMT2D; also absent: ENSG00000256825, ZNF140, CEP126 |
| [[ZFP30]] | B | ZFP30 activity raises ZNF84's level | lines that do not express ZFP30 (9) vs lines expressing it (41) | 2.22× lower at baseline in the lines without ZFP30 | 0.022 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF420, ZNF461 |
| [[ZNF461]] | B | ZNF461 activity raises ZNF84's level | lines that do not express ZNF461 (7) vs lines expressing it (43) | 2.56× lower at baseline in the lines without ZNF461 | 0.043 | ⚠ within organs, on part of the lines; also absent: ZNF567, ZNF529-AS1, ZNF571 |
| [[ZNF571]] | B | ZNF571 activity raises ZNF84's level | lines that do not express ZNF571 (6) vs lines expressing it (44) | 2.64× lower at baseline in the lines without ZNF571 | 0.051 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF420, ZNF850, ZNF540 |
| [[ZNF567]] | B | ZNF567 activity raises ZNF84's level | lines that do not express ZNF567 (5) vs lines expressing it (45) | 2.81× lower at baseline in the lines without ZNF567 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF529, ZFP14; its own permutation p |
| [[ZNF566]] | B | ZNF566 activity raises ZNF84's level | lines that do not express ZNF566 (5) vs lines expressing it (45) | 2.98× lower at baseline in the lines without ZNF566 | 0.070 | ⚠ within organs, on part of the lines; also absent: ZFP14, MPP1, ZNF540 |
| [[ZNF808]] | B | ZNF808 activity raises ZNF84's level | lines that do not express ZNF808 (6) vs lines expressing it (44) | 1.27× lower at baseline in the lines without ZNF808 | 0.098 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF468, ZNF28, ZNF888 |
| [[ZNF527]] | C | ZNF527 activity raises ZNF84's level | lines that do not express ZNF527 (3) vs lines expressing it (47) | 4.39× lower at baseline in the lines without ZNF527 | 2e-04 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: NME4, ZFP14, ZNF221 |
| [[ZNF551]] | C | ZNF551 activity raises ZNF84's level | lines that do not express ZNF551 (4) vs lines expressing it (46) | 2.42× lower at baseline in the lines without ZNF551 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF550, ZNF160, ZNF234; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.297). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-40.8, 15.3); signed map (-16.3, -17.7). **Vector** length 78.7, 14.8% of its response variance represented; |z| ≥ 3 in 825 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.2 | +7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +3.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.7 | +5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +5.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +3.6 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | -2.4 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.7 | -7.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.7 | -4.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -2.1 | -13.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -2.5 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -1.5 | -1.9 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | -1.3 | -0.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | +0.4 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | -1.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 84 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.33 — chr12:133,037,292-133,063,304 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HPF2 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P51523](https://www.uniprot.org/uniprotkb/P51523) (Zinc finger protein 84):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7637](https://www.ncbi.nlm.nih.gov/gene/7637):

> Predicted to enable DNA binding activity and zinc ion binding activity. Predicted to be involved in DNA-templated transcription and regulation of DNA-templated transcription. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13159](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13159) · Entrez [7637](https://www.ncbi.nlm.nih.gov/gene/7637) · UniProt [P51523](https://www.uniprot.org/uniprotkb/P51523) · Ensembl [ENSG00000198040](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198040)

## Data

Gene col 12517: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12517); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12517, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12517]; `tensor/DDL_lfc|DDL_z.npy` [12517]; `embed/gene_vectors.npy` [12517]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12517 or target_col == 12517). Every well: [[ZNF84 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF84.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
