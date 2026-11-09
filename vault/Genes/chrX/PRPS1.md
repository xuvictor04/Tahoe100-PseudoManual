---
symbol: "PRPS1"
type: "gene"
col: 7163
ensembl_id: "ENSG00000147224"
name: "phosphoribosyl pyrophosphate synthetase 1"
location: "Xq22.3"
module: 4
arm: "+"
pooled_cpm: 16.82
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# PRPS1

*phosphoribosyl pyrophosphate synthetase 1* — Xq22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (20 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.53× (z +20.9, q 0e+00, up in 38 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 2.35× (z +10.4, q 3e-23, up in 41 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.385×, NCI-H2030 0.416×; ⚠ cell-cycle shift, explains ~0% of this change); [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (SNU-1 0.0964×); [[Ipatasertib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.152×); [[Saquinavir (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0765×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELAC2]] (+0.81, fdr 7e-06), [[PPP5C]] (+0.78, fdr 7e-06), [[RPE]] (+0.77, fdr 7e-06); moves opposite to [[TERF2IP]] (-0.71, fdr 7e-06), [[ZMYM5]] (-0.69, fdr 7e-06), [[ACAP1]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CDCA7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 20 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7163.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **5.53×** | +20.9 | 0e+00 | 38/38 (PANC-1, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **5.10×** | +19.1 | 0e+00 | 21/21 (SNU-423, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.96×** | +18.1 | 0e+00 | 25/26 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.35×** | +10.4 | 3e-23 | 41/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.27×** | +10.0 | 2e-21 | 39/47 (SK-MEL-2, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.07×** | +8.4 | 6e-15 | 35/46 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.81×** | +7.2 | 4e-11 | 26/47 (KATO III, HT-29, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.80×** | +7.2 | 5e-11 | 30/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.76×** | +6.9 | 3e-10 | 26/47 (KATO III, HT-29, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.69×** | +6.4 | 7e-09 | 32/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.69×** | +6.4 | 9e-09 | 27/47 (KATO III, SNU-423, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.66×** | +6.2 | 3e-08 | 24/47 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **1.65×** | +5.9 | 2e-07 | 28/39 (SNU-423, A549, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.57×** | +5.5 | 2e-06 | 24/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.51×** | +4.8 | 5e-05 | 20/46 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.42×** | +4.1 | 0.001 | 16/47 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.90×** | +4.1 | 0.001 | 18/45 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.63×** | +3.1 | 0.043 | 6/46 (NCI-H460, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +2.9 | 0.070 | 14/48 (J82, HOP62, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.29×** | +2.9 | 0.078 | 14/45 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7163.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.385×, NCI-H2030 0.416×; ⚠ cell-cycle shift, explains ~0% of this change); [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (SNU-1 0.0964×); [[Ipatasertib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.152×); [[Saquinavir (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0765×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 0.817× | -3.5 | 0.28 | 16/48 (MIA PaCa-2, H4, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 0.827× | -3.3 | 0.30 | 19/46 (SW1417, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Rifaximin (drug)]] 5 µM |  | 0.768× | -3.1 | 0.36 | 12/46 (H4, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.65 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7163. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 21.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.65× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Ipatasertib (drug)]] 0.5 µM 0.152× (z -9.0) |
| [[PANC-1 (line)]] | alt | 41.7 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.67× (z +16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.90× (z +9.3) | — |
| [[A498 (line)]] | wt | 37.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.31× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[J82 (line)]] | alt | 31.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.63× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LOX-IMVI (line)]] | wt | 12.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.32× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2030 (line)]] | alt | 22.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.98× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 17.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.41× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SNU-423 (line)]] | alt | 19.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.6× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW480 (line)]] | alt | 29.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-427 (line)]] | wt | 30.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 13.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.49× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HEC-1-A (line)]] | alt | 13.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HOP62 (line)]] | alt | 12.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.21× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 6.41 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.5× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[KATO III (line)]] | alt | 11.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.2× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LS 180 (line)]] | wt | 5.79 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 10.1× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.108× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~75% of this change |
| [[C32 (line)]] | wt | 9.94 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.112× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 8.57 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0879× (z -8.7) |
| [[HS-578T (line)]] | alt | 9.84 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.32× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 6.92 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.6× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LoVo (line)]] | wt | 6.01 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.42× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1792 (line)]] | alt | 6.84 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.8× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[RPMI-7951 (line)]] | alt | 7.79 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0765× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 29.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SNU-1 (line)]] | wt | 13.1 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0964× (z -9.6) |
| [[A-172 (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7163), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELAC2]] | +0.81 | +0.78 / +0.80 | both halves | 7e-06 |  |
| [[PPP5C]] | +0.78 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[RPE]] | +0.77 | +0.73 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 600 |
| [[MTHFD1]] | +0.75 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[GOT2]] | +0.74 | +0.69 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[PRPF19]] | +0.74 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[USP5]] | +0.72 | +0.78 / +0.60 | both halves | 7e-06 |  |
| [[WDR77]] | +0.70 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[PRKDC]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[PSMG1]] | +0.69 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[NUP155]] | +0.68 | +0.64 / +0.69 | both halves | 7e-06 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[PFKM]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TERF2IP]] | -0.71 | -0.67 / -0.69 | both halves | 7e-06 |  |
| [[ZMYM5]] | -0.69 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[ACAP1]] | -0.68 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[RSRP1]] | -0.67 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[SPATC1]] | -0.66 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[TNRC6C]] | -0.65 | -0.66 / -0.57 | both halves | 1e-05 |  |
| [[ARID4B]] | -0.65 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[LINC00685]] | -0.65 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[OFD1]] | -0.65 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[DCTN6-DT]] | -0.65 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[FKBP2]] ⚠ | -0.64 | -0.63 / -0.69 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG9]] | -0.62 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[GCC2]] | -0.61 | -0.65 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDCA7]] | B | CDCA7 activity raises PRPS1's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 1.84× lower at baseline in the lines without CDCA7 | 0.066 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[OCRL]] | C | OCRL's natural level strengthens PRPS1's drug response | OCRL's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.46; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.745). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-23.5, -34.3); signed map (-16.0, -45.4). **Vector** length 89.5, 19.8% of its response variance represented; |z| ≥ 3 in 1,041 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.56 to 4); *Prefoldin mediated transfer of substrate  to CCT/TriC* (reactome, mean cos +0.52 to 5); *Cooperation of Prefoldin and TriC/CCT  in actin and tubulin folding* (reactome, mean cos +0.52 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +7.6 | +20.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +7.5 | +19.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +18.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.6 | +10.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.6 | +10.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +4.1 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.1 | -0.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -3.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -2.5 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | +0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.9 | -1.0 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.8 | -2.5 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.7 | -2.5 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -1.7 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | phosphoribosyl pyrophosphate synthetase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.3 — chrX:107,628,428-107,651,993 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CMTX5, DFNX1, PRS-I, PPRibP; previously DFN2 |
| Gene groups (HGNC) | Phosphoribosyl pyrophosphate synthetase family |
| Hallmark sets | GLYCOLYSIS, E2F_TARGETS |
| Reactome | 2 pathways, smallest: Pentose phosphate pathway; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P60891](https://www.uniprot.org/uniprotkb/P60891) (Ribose-phosphate pyrophosphokinase 1):

> Catalyzes the synthesis of phosphoribosylpyrophosphate (PRPP) that is essential for nucleotide synthesis.

**Summary**, from NCBI Gene [5631](https://www.ncbi.nlm.nih.gov/gene/5631):

> This gene encodes an enzyme that catalyzes the phosphoribosylation of ribose 5-phosphate to 5-phosphoribosyl-1-pyrophosphate, which is necessary for purine metabolism and nucleotide biosynthesis. Defects in this gene are a cause of phosphoribosylpyrophosphate synthetase superactivity, Charcot-Marie-Tooth disease X-linked recessive type 5 and Arts Syndrome. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:9462](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9462) · Entrez [5631](https://www.ncbi.nlm.nih.gov/gene/5631) · UniProt [P60891](https://www.uniprot.org/uniprotkb/P60891) · Ensembl [ENSG00000147224](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147224)

## Data

Gene col 7163: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7163); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7163, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7163]; `tensor/DDL_lfc|DDL_z.npy` [7163]; `embed/gene_vectors.npy` [7163]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7163 or target_col == 7163). Every well: [[PRPS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRPS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
