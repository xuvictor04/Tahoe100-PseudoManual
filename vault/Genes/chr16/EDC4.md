---
symbol: "EDC4"
type: "gene"
col: 453
ensembl_id: "ENSG00000038358"
name: "enhancer of mRNA decapping 4"
location: "16q22.1"
module: 2
arm: "+"
pooled_cpm: 19.44
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 4
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# EDC4

*enhancer of mRNA decapping 4* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.12× (z +10.8, q 1e-24, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.830× (z -3.7, q 0.061, down in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.155×; ⚠ cell-cycle shift, explains ~28% of this change); [[Nafamostat (mesylate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.120×); [[Orlistat (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.101×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.270×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHOT2]] (+0.77, fdr 7e-06), [[TAF1C]] (+0.65, fdr 7e-06), [[USP19]] (+0.63, fdr 7e-06); moves opposite to [[TXN]] (-0.54, fdr 3e-05), [[RPL39]] (-0.48, fdr 1e-05), [[KTN1-AS1]] (-0.47, fdr 2e-04).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 453.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.12×** | +10.8 | 1e-24 | 44/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.63×** | +9.7 | 6e-20 | 36/47 (NCI-H1573, HOP62, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.68×** | +7.5 | 1e-11 | 35/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.68×** | +7.4 | 1e-11 | 35/48 (SW480, A549, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +6.7 | 3e-09 | 36/47 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.48×** | +5.7 | 1e-06 | 22/48 (SW480, NCI-H2030, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.42×** | +5.1 | 3e-05 | 22/46 (SW480, KATO III, …) | rises with dose |  |
| [[Trimetrexate (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.003 | 16/48 (HepG2/C3A, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | **1.32×** | +4.0 | 0.004 | 18/41 (HCT15, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.47×** | +4.0 | 0.004 | 19/46 (RKO, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.67×** | +3.9 | 0.005 | 13/48 (RKO, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.32×** | +3.9 | 0.005 | 18/47 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.32×** | +3.7 | 0.008 | 18/37 (PANC-1, SHP-77, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.28×** | +3.6 | 0.012 | 13/45 (RPMI-7951, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.034 | 16/45 (SHP-77, SNU-1, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.37×** | +3.2 | 0.045 | 16/44 (PANC-1, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Berberine (chloride hydrate) (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.054 | 8/48 (CFPAC-1, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.074 | 10/47 (Hs 766T, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 453.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.155×; ⚠ cell-cycle shift, explains ~28% of this change); [[Nafamostat (mesylate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.120×); [[Orlistat (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.101×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.270×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.830×** | -3.7 | 0.061 | 16/48 (Hs 766T, SNU-423, …) | rises with dose | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.773×** | -3.7 | 0.061 | 20/47 (RPMI-7951, NCI-H2347, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.776×** | -3.5 | 0.077 | 20/47 (NCI-H661, COLO 205, …) | rises with dose | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **0.784×** | -3.4 | 0.083 | 10/48 (PANC-1, C-33 A, …) | two highest doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -3.4 | 0.083 | 19/47 (MIA PaCa-2, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 453. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 33.6 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.11× (z +11.4) | — |
| [[HepG2_C3A (line)]] | wt | 15.7 | 0 | 2 | — | [[Nafamostat (mesylate) (drug)]] 0.5 µM 0.120× (z -10.7) |
| [[A-172 (line)]] | wt | 11.2 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.270× (z -10.1) |
| [[A-427 (line)]] | wt | 18.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -12.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 29.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +8.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[H4 (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0773× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 17.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +9.1) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[Hs 766T (line)]] | wt | 21.5 | 0 | 1 | — | [[Capmatinib (drug)]] 5 µM 0.0648× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 15.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +9.4) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1792 (line)]] | alt | 18.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +8.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[PANC-1 (line)]] | alt | 11.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.1) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SHP-77 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.118× (z -9.7) ⚠ toxic |
| [[A549 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 453), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHOT2]] | +0.77 | +0.75 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[TAF1C]] | +0.65 | +0.71 / +0.67 | both halves | 7e-06 | STRING 538 |
| [[USP19]] | +0.63 | +0.66 / +0.64 | both halves | 7e-06 | STRING 487 |
| [[TUBGCP6]] | +0.61 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[RPS6KB2]] | +0.61 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[CXXC1]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 487 |
| [[SKIC2]] | +0.60 | +0.55 / +0.51 | both halves | 1e-05 | pathway: Deadenylation-dependent mRNA decay |
| [[LRCH4]] | +0.60 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[BAP1]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[TCIRG1]] | +0.59 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[UCKL1]] | +0.59 | +0.39 / +0.63 | both halves | 6e-05 |  |
| [[GET4]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXN]] | -0.54 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[RPL39]] | -0.48 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[KTN1-AS1]] | -0.47 | -0.32 / -0.35 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.459). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-12.9, -24.8); signed map (-7.6, 20.2). **Vector** length 74.2, 13.5% of its response variance represented; |z| ≥ 3 in 746 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.1 | +10.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | +3.1 | +3.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.0 | +3.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +3.0 | +2.5 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +2.8 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +4.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.3 | +3.0 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.1 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.0 | -3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -4.2 | -3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +1.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.8 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.1 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | +0.7 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | enhancer of mRNA decapping 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,873,052-67,884,499 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RCD-8, Ge-1, HEDLS |
| Gene groups (HGNC) | WD repeat domain containing; RNA decapping and exonuclease complex subunits |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 3 pathways, smallest: mRNA decay by 5' to 3' exoribonuclease; Deadenylation-dependent mRNA decay; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P2E9](https://www.uniprot.org/uniprotkb/Q6P2E9) (Enhancer of mRNA-decapping protein 4):

> In the process of mRNA degradation, seems to play a role in mRNA decapping. Component of a complex containing DCP2 and DCP1A which functions in decapping of ARE-containing mRNAs. Promotes complex formation between DCP1A and DCP2. Enhances the catalytic activity of DCP2 (in vitro).

**Summary**, from NCBI Gene [23644](https://www.ncbi.nlm.nih.gov/gene/23644):

> Predicted to be involved in deadenylation-independent decapping of nuclear-transcribed mRNA. Located in P-body and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17157](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17157) · Entrez [23644](https://www.ncbi.nlm.nih.gov/gene/23644) · UniProt [Q6P2E9](https://www.uniprot.org/uniprotkb/Q6P2E9) · Ensembl [ENSG00000038358](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000038358)

## Data

Gene col 453: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 453); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 453, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 453]; `tensor/DDL_lfc|DDL_z.npy` [453]; `embed/gene_vectors.npy` [453]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 453 or target_col == 453). Every well: [[EDC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EDC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
