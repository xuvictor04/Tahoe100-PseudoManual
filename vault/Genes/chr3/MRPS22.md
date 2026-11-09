---
symbol: "MRPS22"
type: "gene"
col: 10564
ensembl_id: "ENSG00000175110"
name: "mitochondrial ribosomal protein S22"
location: "3q23"
module: 20
arm: "+"
pooled_cpm: 28.09
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# MRPS22

*mitochondrial ribosomal protein S22* — 3q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.85× (z +17.7, q 0e+00, up in 43 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.224×, HCT15 0.182×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.0777×; ⚠ toxic).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1D]] (+0.66, fdr 1e-05), [[RAE1]] (+0.64, fdr 1e-05), [[SDHD]] (+0.62, fdr 1e-05); moves opposite to [[SMARCA4]] (-0.56, fdr 4e-05), [[SMC6]] (-0.52, fdr 3e-05), [[EIF5B]] (-0.48, fdr 5e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10564.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +17.7 | 0e+00 | 43/48 (HEC-1-A, BT-474, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.40×** | +9.3 | 4e-18 | 41/48 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +9.0 | 6e-17 | 35/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.49×** | +8.1 | 5e-14 | 31/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +7.3 | 3e-11 | 23/40 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +6.2 | 5e-08 | 26/48 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +5.2 | 2e-05 | 21/48 (NCI-H1573, C32, …) | rises with dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.55×** | +4.6 | 2e-04 | 20/47 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.5 | 4e-04 | 15/48 (A-172, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 5e-04 | 17/48 (NCI-H1792, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.24×** | +4.3 | 8e-04 | 20/44 (NCI-H23, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.24×** | +4.3 | 9e-04 | 17/38 (MIA PaCa-2, KATO III, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.23×** | +4.2 | 0.001 | 18/48 (NCI-H1573, PANC-1, …) | inconsistent across doses | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.011 | 14/44 (SHP-77, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | 1.19× | +3.5 | 0.021 | 16/46 (Hs 766T, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.040 | 14/48 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +3.2 | 0.040 | 16/48 (LoVo, SHP-77, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.042 | 9/45 (LOX-IMVI, NCI-H23, …) | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10564.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.224×, HCT15 0.182×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.0777×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cepharanthine (drug)]] 5 µM |  | 0.893× | -3.3 | 0.55 | 11/48 (HT-29, SW 1271, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10564. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 48.5 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.62× (z +12.1) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[RPMI-7951 (line)]] | alt | 76.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +15.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +10.2) | — |
| [[A-172 (line)]] | wt | 20.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 36.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[A549 (line)]] | wt | 17.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 29.7 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0777× (z -9.7) ⚠ toxic |
| [[BT-474 (line)]] | alt | 24.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +13.1) | — |
| [[C32 (line)]] | wt | 16.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +9.4) | — |
| [[HCT15 (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[HEC-1-A (line)]] | alt | 30.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +14.0) | — |
| [[HOP62 (line)]] | alt | 21.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +11.1) | — |
| [[LOX-IMVI (line)]] | wt | 20.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 20.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +10.6) | — |
| [[NCI-H23 (line)]] | alt | 34.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[NCI-H460 (line)]] | wt | 18.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 28.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +12.3) | — |
| [[A498 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10564), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1D]] | +0.66 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[RAE1]] | +0.64 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[SDHD]] | +0.62 | +0.54 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[C18orf25]] | +0.61 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[MED6]] | +0.58 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[DERL1]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[NAXD]] | +0.58 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[OTUB1]] | +0.57 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[VIPAS39]] | +0.57 | +0.65 / +0.39 | both halves | 5e-05 |  |
| [[VDAC2]] | +0.57 | +0.63 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[KLHL3]] | +0.56 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[TMEM183A]] | +0.55 | +0.61 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMARCA4]] | -0.56 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[SMC6]] | -0.52 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[EIF5B]] | -0.48 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[NPIPB5]] | -0.48 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[PILRB]] | -0.48 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[PFN1]] | -0.47 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[WWC2]] | -0.47 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[CREB1]] | -0.47 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[CCDC88A]] | -0.47 | -0.43 / -0.37 | both halves | 7e-05 |  |
| [[PKP4]] | -0.46 | -0.58 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.347). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-19.7, -15.7); signed map (-18.5, -29.8). **Vector** length 72.5, 12.6% of its response variance represented; |z| ≥ 3 in 828 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +17.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.9 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | +3.3 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +8.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +3.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | +0.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | +0.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -2.8 | +3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.6 | +4.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -0.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | +0.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.2 | -2.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.1 | +0.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q23 — chr3:139,005,806-139,360,497 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRP-S22, GK002, C3orf5, GIBT, mS22 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Small subunit mitochondrial ribosomal proteins |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [P82650](https://www.uniprot.org/uniprotkb/P82650) carries no function annotation.

**Summary**, from NCBI Gene [56945](https://www.ncbi.nlm.nih.gov/gene/56945):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14508](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14508) · Entrez [56945](https://www.ncbi.nlm.nih.gov/gene/56945) · UniProt [P82650](https://www.uniprot.org/uniprotkb/P82650) · Ensembl [ENSG00000175110](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175110)

## Data

Gene col 10564: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10564); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10564, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10564]; `tensor/DDL_lfc|DDL_z.npy` [10564]; `embed/gene_vectors.npy` [10564]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10564 or target_col == 10564). Every well: [[MRPS22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
