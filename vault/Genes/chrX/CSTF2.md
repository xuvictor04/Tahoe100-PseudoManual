---
symbol: "CSTF2"
type: "gene"
col: 2173
ensembl_id: "ENSG00000101811"
name: "cleavage stimulation factor subunit 2"
location: "Xq22.1"
module: 4
arm: "+"
pooled_cpm: 18.06
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# CSTF2

*cleavage stimulation factor subunit 2* — Xq22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.02× (z +9.5, q 1e-18, up in 23 of 26 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.52× (z +5.9, q 4e-07, up in 22 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.797× (z -4.5, q 0.004, down in 21 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.406×, LS 180 0.367×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.369×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.167×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change); [[Atazanavir (sulfate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0922×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUP155]] (+0.70, fdr 7e-06), [[FAM98B]] (+0.70, fdr 7e-06), [[EIPR1]] (+0.68, fdr 7e-06); moves opposite to [[EIF1]] (-0.63, fdr 1e-05), [[OSER1-DT]] (-0.60, fdr 1e-05), [[SMIM14]] (-0.60, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2173.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **2.02×** | +9.5 | 1e-18 | 23/26 (A498, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.94×** | +9.3 | 4e-18 | 34/42 (A498, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.65×** | +6.7 | 3e-09 | 27/43 (NCI-H2030, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.57×** | +6.3 | 3e-08 | 26/47 (NCI-H460, SK-MEL-2, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +5.9 | 4e-07 | 22/46 (LoVo, LOX-IMVI, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.12×** | +5.5 | 3e-06 | 24/48 (PANC-1, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.52×** | +5.4 | 5e-06 | 22/34 (A498, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +5.4 | 6e-06 | 19/48 (AsPC-1, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.46×** | +5.3 | 8e-06 | 19/47 (A498, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +4.9 | 7e-05 | 20/47 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.41×** | +4.8 | 8e-05 | 19/48 (A498, NCI-H1573, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.91×** | +4.7 | 1e-04 | 10/23 (HOP62, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +4.7 | 1e-04 | 23/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.5 | 2e-04 | 18/48 (NCI-H2030, NCI-H1573, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.25×** | +4.5 | 3e-04 | 16/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +4.2 | 8e-04 | 14/48 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.76×** | +4.2 | 0.001 | 18/45 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.005 | 7/48 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.63×** | +3.6 | 0.010 | 12/46 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.62×** | +3.5 | 0.010 | 13/45 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.61×** | +3.5 | 0.011 | 8/47 (NCI-H460, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.5 | 0.013 | 14/44 (PANC-1, LOX-IMVI, …) | all doses, flat | low cells (technical?) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.018 | 7/47 (A498, A549, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.018 | 10/47 (A549, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2173.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.406×, LS 180 0.367×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.369×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.167×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change); [[Atazanavir (sulfate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0922×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.797×** | -4.5 | 0.004 | 21/46 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 0.836× | -3.5 | 0.088 | 14/48 (RKO, LS 180, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -3.5 | 0.088 | 5/48 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.775×** | -3.4 | 0.088 | 16/46 (SNU-423, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.760× | -3.2 | 0.13 | 15/48 (LOX-IMVI, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.799× | -3.1 | 0.16 | 7/47 (A-427, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2173. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 24.9 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -12.3) |
| [[A498 (line)]] | wt | 11.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | — |
| [[HepG2_C3A (line)]] | wt | 9.38 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0922× (z -9.0) |
| [[LS 180 (line)]] | wt | 36.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[SK-MEL-2 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.104× (z -10.6) ⚠ toxic |
| [[A-172 (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 37.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2173), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP155]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[FAM98B]] | +0.70 | +0.70 / +0.68 | both halves | 7e-06 | pathway: tRNA processing |
| [[EIPR1]] | +0.68 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[ALKBH8]] | +0.68 | +0.61 / +0.69 | both halves | 7e-06 | same gene group; pathway: tRNA processing |
| [[SNRPD1]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 590 |
| [[PPP5C]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[EXOSC2]] | +0.66 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[DLAT]] | +0.65 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[COA1]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[GPAM]] | +0.63 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[SKP2]] | +0.63 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[PDSS1]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF1]] | -0.63 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[OSER1-DT]] | -0.60 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[SMIM14]] | -0.60 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[CATSPERG]] | -0.58 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[WBP1]] | -0.58 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[SHOC2]] | -0.58 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[RNASEK]] | -0.57 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[HLA-E]] | -0.57 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[STX5]] | -0.56 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[ZMYM5]] | -0.56 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[FAM177A1]] | -0.56 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[SELENOK]] | -0.56 | -0.49 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.686). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-24.3, -35.2); signed map (-14.5, -46.7). **Vector** length 80.6, 16.2% of its response variance represented; |z| ≥ 3 in 822 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Metabolism of non-coding RNA* (reactome, mean cos +0.50 to 7); *snRNP Assembly* (reactome, mean cos +0.50 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.6 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | +4.3 | +6.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.9 | +6.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.3 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.0 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.6 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +4.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +4.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | -1.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -2.3 | -3.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.0 | -3.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.8 | -1.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | cleavage stimulation factor subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.1 — chrX:100,820,391-100,841,520 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CstF-64 |
| Gene groups (HGNC) | RNA binding motif containing; Cleavage stimulation factor subunits |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 12 pathways, smallest: Processing of Intronless Pre-mRNAs; Processing of Capped Intronless Pre-mRNA; RNA Polymerase II Transcription Termination |
| Matched by | ensembl_id |

**Function**, from UniProt [P33240](https://www.uniprot.org/uniprotkb/P33240) (Cleavage stimulation factor subunit 2):

> One of the multiple factors required for polyadenylation and 3'-end cleavage of mammalian pre-mRNAs. This subunit is directly involved in the binding to pre-mRNAs.

**Summary**, from NCBI Gene [1478](https://www.ncbi.nlm.nih.gov/gene/1478):

> This gene encodes a nuclear protein with an RRM (RNA recognition motif) domain. The protein is a member of the cleavage stimulation factor (CSTF) complex that is involved in the 3' end cleavage and polyadenylation of pre-mRNAs. Specifically, this protein binds GU-rich elements within the 3'-untranslated region of mRNAs. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2484](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2484) · Entrez [1478](https://www.ncbi.nlm.nih.gov/gene/1478) · UniProt [P33240](https://www.uniprot.org/uniprotkb/P33240) · Ensembl [ENSG00000101811](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101811)

## Data

Gene col 2173: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2173); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2173, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2173]; `tensor/DDL_lfc|DDL_z.npy` [2173]; `embed/gene_vectors.npy` [2173]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2173 or target_col == 2173). Every well: [[CSTF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSTF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
