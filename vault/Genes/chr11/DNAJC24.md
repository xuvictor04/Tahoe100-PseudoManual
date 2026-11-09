---
symbol: "DNAJC24"
type: "gene"
col: 10030
ensembl_id: "ENSG00000170946"
name: "DnaJ heat shock protein family (Hsp40) member C24"
location: "11p13"
module: 30
arm: "+"
pooled_cpm: 43.92
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# DNAJC24

*DnaJ heat shock protein family (Hsp40) member C24* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.79× (z +14.9, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.780× (z -6.1, q 4e-07, down in 27 of 47 measured lines) ⚠ toxic.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW48 0.0827×, A-427 0.427×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SNU-1 0.172×, SW480 0.493×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (Panc 03.27 0.349×, A549 0.418×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change); [[Sonidegib (drug)]] 5 µM in 1 line (C-33 A 0.0594×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMF1]] (+0.68, fdr 7e-06), [[TTC14]] (+0.63, fdr 3e-05), [[GTF3C3]] (+0.62, fdr 1e-05); moves opposite to [[ERF]] (-0.59, fdr 1e-05), [[USP43]] (-0.56, fdr 2e-05), [[FBXO48]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 030]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10030.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.79×** | +14.9 | 0e+00 | 41/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.73×** | +14.0 | 5e-42 | 42/48 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +11.4 | 6e-28 | 38/48 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.48×** | +9.7 | 5e-20 | 34/47 (C32, Panc 03.27, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.26×** | +8.5 | 2e-15 | 30/48 (A-427, A549, …) | rises with dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +6.7 | 1e-09 | 22/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.30×** | +6.6 | 3e-09 | 25/48 (A-427, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.25×** | +5.6 | 1e-06 | 23/48 (SW480, A-427, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.26×** | +5.5 | 3e-06 | 22/48 (RKO, PANC-1, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +5.3 | 6e-06 | 21/44 (RKO, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.23×** | +5.3 | 7e-06 | 18/48 (LOX-IMVI, CFPAC-1, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.47×** | +5.1 | 1e-05 | 18/48 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.22×** | +5.1 | 2e-05 | 21/48 (J82, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.44×** | +4.8 | 5e-05 | 17/48 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.20× | +4.6 | 1e-04 | 15/47 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 0.001 | 12/48 (NCI-H1792, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.16× | +3.9 | 0.004 | 18/48 (HOP62, RKO, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.16× | +3.8 | 0.005 | 18/48 (RKO, A-172, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.006 | 8/48 (LOX-IMVI, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.015 | 10/47 (MIA PaCa-2, SW480, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.037 | 10/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.042 | 8/48 (A549, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.061 | 7/48 (HT-29, A549, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.12× | +3.0 | 0.065 | 5/48 (BT-474, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10030.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW48 0.0827×, A-427 0.427×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SNU-1 0.172×, SW480 0.493×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (Panc 03.27 0.349×, A549 0.418×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change); [[Sonidegib (drug)]] 5 µM in 1 line (C-33 A 0.0594×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.780×** | -6.1 | 4e-07 | 27/47 (NCI-H460, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.892× | -4.2 | 0.009 | 18/47 (A-427, RKO, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.956× | -3.9 | 0.019 | 1/48 (NCI-H661) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.876× | -3.2 | 0.22 | 13/46 (AsPC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.921× | -3.0 | 0.30 | 16/48 (A-427, SW1417, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10030. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 60.0 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 30.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.98× (z +9.8) | — |
| [[SW480 (line)]] | alt | 62.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.487× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change |
| [[A549 (line)]] | wt | 45.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.418× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[AN3 CA (line)]] | alt | 50.4 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0858× (z -11.5) ⚠ toxic |
| [[C-33 A (line)]] | alt | 53.3 | 0 | 1 | — | [[Sonidegib (drug)]] 5 µM 0.0594× (z -12.5) |
| [[Panc 03.27 (line)]] | alt | 47.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.349× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[PANC-1 (line)]] | alt | 54.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.84× (z +8.7) | — |
| [[RKO (line)]] | wt | 69.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.21× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | — |
| [[SNU-1 (line)]] | wt | 62.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[SW48 (line)]] | wt | 47.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0827× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 58.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 51.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 57.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10030), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMF1]] | +0.68 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[TTC14]] | +0.63 | +0.46 / +0.71 | both halves | 3e-05 |  |
| [[GTF3C3]] | +0.62 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[CDK5RAP1]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[GPR89A]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[DYNC2LI1]] | +0.59 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[ATPAF1]] | +0.58 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[SLC30A6]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[EDEM2]] | +0.57 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[SAMM50]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[MAFIP]] | +0.57 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[RINT1]] | +0.57 | +0.47 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERF]] | -0.59 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[USP43]] | -0.56 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[FBXO48]] | -0.54 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[PKNOX1]] | -0.53 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[GPR137C]] | -0.53 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[ZFHX3]] | -0.53 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[TSC22D1]] | -0.52 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[CDC42EP4]] | -0.52 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[SGO1-AS1]] | -0.51 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[BAHCC1]] | -0.51 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[WEE1]] | -0.51 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[GSE1]] | -0.50 | -0.43 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.442). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-23.4, -8.5); signed map (-31.2, -26.1). **Vector** length 84.2, 16.5% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | +5.7 | +9.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.9 | +8.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +3.4 | +5.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.4 | +5.6 |
|  | [[EX229 (drug)]] 5 µM |  | +3.0 | +5.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.7 | +4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.6 | +2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +3.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.4 | -4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.6 | -3.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.9 | -6.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | -4.7 | -2.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | -3.8 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -0.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.1 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | +1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member C24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:31,369,840-31,432,835 (+) |
| Ensembl biotype | protein_coding |
| Also known as | JJJ3; previously ZCSL3, DPH4 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins; Diphthamide biosynthesis genes |
| Reactome | 2 pathways, smallest: Synthesis of diphthamide-EEF2; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P3W2](https://www.uniprot.org/uniprotkb/Q6P3W2) (DnaJ homolog subfamily C member 24):

> Stimulates the ATPase activity of several Hsp70-type chaperones. This ability is enhanced by iron-binding. The iron-bound form is redox-active and can function as electron carrier. Plays a role in the diphthamide biosynthesis, a post-translational modification of histidine which occurs in translation elongation factor 2 (EEF2) which can be ADP-ribosylated by diphtheria toxin and by Pseudomonas exotoxin A (Eta).

**Summary**, from NCBI Gene [120526](https://www.ncbi.nlm.nih.gov/gene/120526):

> Diphthamide is a unique posttranslationally modified histidine found only in translation elongation factor-2 (EEF2; MIM 130610). This modification is conserved from archaebacteria to humans and serves as the target for ADP-ribosylation and inactivation of EEF2 by diphtheria toxin (DT) and Pseudomonas exotoxin A. DPH4 is 1 of several enzymes involved in synthesis of diphthamide in EEF2 (Liu et al., 2004 [PubMed 15485916]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:26979](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26979) · Entrez [120526](https://www.ncbi.nlm.nih.gov/gene/120526) · UniProt [Q6P3W2](https://www.uniprot.org/uniprotkb/Q6P3W2) · Ensembl [ENSG00000170946](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170946)

## Data

Gene col 10030: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10030); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10030, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10030]; `tensor/DDL_lfc|DDL_z.npy` [10030]; `embed/gene_vectors.npy` [10030]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10030 or target_col == 10030). Every well: [[DNAJC24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
