---
symbol: "FAHD1"
type: "gene"
col: 11085
ensembl_id: "ENSG00000180185"
name: "FAH domain containing oxaloacetate decarboxylase 1"
location: "16p13.3"
module: 16
arm: "+"
pooled_cpm: 11.18
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# FAHD1

*FAH domain containing oxaloacetate decarboxylase 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.85× (z +9.9, q 2e-20, up in 34 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.655× (z -4.9, q 6e-04, down in 23 of 45 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (SW480 0.242×, COLO 205 0.126×; ⚠ toxic; transcription drop); [[Verteporfin (drug)]] 5 µM in 1 line (HS-578T 0.0636×); [[AZD2858 (drug)]] 0.5 µM in 1 line (A-427 0.106×; ⚠ toxic); [[Auranofin (drug)]] 0.05 µM in 1 line (AsPC-1 0.119×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C6orf120]] (+0.65, fdr 7e-06), [[PURB]] (+0.62, fdr 1e-05), [[MOCS3]] (+0.61, fdr 9e-06); moves opposite to [[CLEC4A]] (-0.51, fdr 2e-05), [[SDHAP1-1]] (-0.51, fdr 5e-05), [[FHIP2B]] (-0.50, fdr 5e-05).
> It sits in the **+** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11085.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +9.9 | 2e-20 | 34/45 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.95×** | +7.6 | 7e-12 | 35/47 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +6.8 | 2e-09 | 29/48 (A-427, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.81×** | +6.5 | 9e-09 | 16/23 (NCI-H2030, J82, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.76×** | +6.4 | 1e-08 | 29/47 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.74×** | +6.3 | 2e-08 | 28/47 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +5.5 | 4e-06 | 22/46 (HEC-1-A, HS-578T, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.45×** | +5.4 | 6e-06 | 21/47 (NCI-H23, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.65×** | +5.3 | 8e-06 | 22/32 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.58×** | +5.2 | 9e-06 | 25/45 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.57×** | +5.2 | 1e-05 | 21/37 (LOX-IMVI, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.0 | 3e-05 | 24/48 (NCI-H2030, J82, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +4.1 | 0.002 | 20/41 (Panc 03.27, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +4.0 | 0.002 | 19/47 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.43×** | +3.9 | 0.003 | 18/45 (RKO, NCI-H1792, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.87×** | +3.7 | 0.007 | 12/44 (SW480, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.34×** | +3.3 | 0.028 | 10/48 (A498, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.051 | 10/46 (SW 900, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **1.31×** | +3.0 | 0.065 | 10/47 (CFPAC-1, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11085.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (SW480 0.242×, COLO 205 0.126×; ⚠ toxic; transcription drop); [[Verteporfin (drug)]] 5 µM in 1 line (HS-578T 0.0636×); [[AZD2858 (drug)]] 0.5 µM in 1 line (A-427 0.106×; ⚠ toxic); [[Auranofin (drug)]] 0.05 µM in 1 line (AsPC-1 0.119×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.655×** | -4.9 | 6e-04 | 23/45 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.762× | -3.1 | 0.39 | 13/46 (NCI-H1792, CFPAC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.830× | -3.1 | 0.39 | 12/48 (HEC-1-A, SK-MEL-2, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11085. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 16.3 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.106× (z -10.4) ⚠ toxic |
| [[A498 (line)]] | wt | 8.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +8.8) | — |
| [[AsPC-1 (line)]] | alt | 7.65 | 0 | 1 | — | [[Auranofin (drug)]] 0.05 µM 0.119× (z -8.5) |
| [[COLO 205 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -8.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 7.21 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0636× (z -11.4) |
| [[MIA PaCa-2 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -8.5) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H23 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.169× (z -8.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 9.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +8.6) | — |
| [[SW480 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.242× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11085), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C6orf120]] | +0.65 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[PURB]] | +0.62 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[MOCS3]] | +0.61 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[SMCR8]] | +0.59 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[TRUB2]] | +0.57 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[TMEM69]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[RRAGA]] | +0.56 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[SUMF1]] | +0.55 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[ZNF629]] | +0.54 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[NELFE]] | +0.54 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[GBA1]] | +0.54 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[MGAT2]] | +0.54 | +0.54 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLEC4A]] | -0.51 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[SDHAP1-1]] | -0.51 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[FHIP2B]] | -0.50 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[GOLGA6L9]] | -0.49 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[RPL37A]] ⚠ | -0.49 | -0.48 / -0.42 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NKTR]] | -0.49 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[SGK3]] | -0.47 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[SNHG12]] | -0.46 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[PLA2G4B]] | -0.46 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[SEC22A]] | -0.46 | -0.48 / -0.40 | both halves | 4e-05 |  |
| [[ENY2]] | -0.45 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[HEATR5A]] | -0.45 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[SNHG8]] | -0.45 | -0.29 / -0.38 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.430). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-37.6, 15.7); signed map (-2.0, -29.3). **Vector** length 75.2, 14.1% of its response variance represented; |z| ≥ 3 in 850 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.4 | +5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.8 | +3.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.4 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.9 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +2.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.2 | +3.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -2.7 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | -1.7 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | -2.1 | -2.5 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | FAH domain containing oxaloacetate decarboxylase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:1,826,967-1,840,207 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP566J2046; previously C16orf36 |
| Gene groups (HGNC) | Decarboxylases |
| Reactome | 2 pathways, smallest: Pyruvate metabolism; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P587](https://www.uniprot.org/uniprotkb/Q6P587) (Oxaloacetate tautomerase FAHD1, mitochondrial):

> Tautomerase that converts enol-oxaloacetate, a strong inhibitor of succinate dehydrogenase, to the physiological keto form of oxaloacetate. It is thereby required to maximize aerobic respiration efficiency by preventing succinate dehydrogenase inhibition. Also acts as a weak oxaloacetate decarboxylase (ODx), catalyzing the decarboxylation of oxaloacetate (OAA) to pyruvate and CO(2), and as such is likely a regulatory enzyme in the TCA cycle. Also displays acylpyruvase activity, being able to …

**Summary**, from NCBI Gene [81889](https://www.ncbi.nlm.nih.gov/gene/81889):

> Enables hydrolase activity, acting on carbon-carbon bonds, in ketonic substances; oxaloacetate decarboxylase activity; and oxaloacetate tautomerase activity. Involved in oxaloacetate metabolic process. Located in cytosol; mitochondrion; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14169](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14169) · Entrez [81889](https://www.ncbi.nlm.nih.gov/gene/81889) · UniProt [Q6P587](https://www.uniprot.org/uniprotkb/Q6P587) · Ensembl [ENSG00000180185](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180185)

## Data

Gene col 11085: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11085); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11085, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11085]; `tensor/DDL_lfc|DDL_z.npy` [11085]; `embed/gene_vectors.npy` [11085]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11085 or target_col == 11085). Every well: [[FAHD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAHD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
