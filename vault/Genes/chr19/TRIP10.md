---
symbol: "TRIP10"
type: "gene"
col: 4650
ensembl_id: "ENSG00000125733"
name: "thyroid hormone receptor interactor 10"
location: "19p13.3"
module: 31
arm: "+"
pooled_cpm: 46.34
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# TRIP10

*thyroid hormone receptor interactor 10* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.59× (z +11.6, q 4e-28, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.821× (z -4.9, q 4e-04, down in 22 of 48 measured lines) ⚠ cell-cycle shift, explains ~9% of this change. The strongest without an alert is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 0.776× (z -4.5, q 0.001, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (LS 180 0.339×, NCI-H23 0.365×, LoVo 0.454×, LOX-IMVI 0.486×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LoVo 0.224×, LS 180 0.250×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW48 0.144×, C-33 A 0.216×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCDH1]] (+0.59, fdr 1e-05), [[ANKRD33B]] (+0.56, fdr 1e-05), [[TPPP]] (+0.56, fdr 6e-05); moves opposite to [[LANCL2]] (-0.45, fdr 6e-05), [[ZNF254]] (-0.44, fdr 2e-04), [[ANXA2R-OT1]] (-0.44, fdr 1e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[FCHO1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4650.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +11.6 | 4e-28 | 28/47 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.68×** | +8.8 | 3e-16 | 30/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +7.6 | 4e-12 | 30/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.81×** | +5.5 | 6e-06 | 27/49 (PANC-1, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +4.9 | 1e-04 | 23/47 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +4.4 | 1e-03 | 17/48 (C-33 A, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.007 | 20/48 (NCI-H2347, Hs 766T, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.008 | 18/47 (HEC-1-A, SW 900, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.23×** | +3.3 | 0.053 | 14/41 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); composition shift |
| [[Dexamethasone (drug)]] 5 µM |  | 1.19× | +3.1 | 0.11 | 6/48 (NCI-H2347, LOX-IMVI, …) | top dose only | position effect removed |
| [[Decitabine (drug)]] 5 µM |  | 1.20× | +3.1 | 0.11 | 10/47 (AsPC-1, LS 180, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | 1.19× | +3.0 | 0.13 | 18/47 (PANC-1, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4650.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (LS 180 0.339×, NCI-H23 0.365×, LoVo 0.454×, LOX-IMVI 0.486×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LoVo 0.224×, LS 180 0.250×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW48 0.144×, C-33 A 0.216×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.821×** | -4.9 | 4e-04 | 22/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.760×** | -4.7 | 9e-04 | 22/47 (Panc 03.27, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.776×** | -4.5 | 0.001 | 25/48 (MIA PaCa-2, H4, …) | top dose only |  |
| [[Fostamatinib (disodium hexahydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.825×** | -3.4 | 0.081 | 5/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.820×** | -3.4 | 0.081 | 18/47 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.820×** | -3.3 | 0.082 | 13/47 (AN3 CA, A-172, …) | inconsistent across doses | position effect removed |
| [[Afatinib (drug)]] 0.5 µM |  | 0.879× | -3.2 | 0.12 | 3/49 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4650. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 35.6 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.70× (z +29.9) | — |
| [[A-172 (line)]] | wt | 58.8 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +16.1) | — |
| [[A498 (line)]] | wt | 90.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.10× (z +20.8) | — |
| [[A549 (line)]] | wt | 53.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.34× (z +21.8) | — |
| [[AsPC-1 (line)]] | alt | 122 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.331× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[HS-578T (line)]] | alt | 53.6 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.23× (z +11.2) | — |
| [[LoVo (line)]] | wt | 56.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.224× (z -14.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.454× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 21.5 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 8.01× (z +13.2) | — |
| [[NCI-H460 (line)]] | wt | 32.7 | 3 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.43× (z +11.0) | — |
| [[A-427 (line)]] | wt | 27.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +12.9) | — |
| [[CFPAC-1 (line)]] | alt | 54.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +12.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.381× (z -8.9) ⚠ toxic |
| [[HOP62 (line)]] | alt | 35.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +14.9) | — |
| [[hTERT-HPNE (line)]] | wt | 45.5 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 3.79× (z +9.7) | — |
| [[J82 (line)]] | alt | 47.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.76× (z +18.9) | — |
| [[LS 180 (line)]] | wt | 53.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -14.7) |
| [[NCI-H1573 (line)]] | alt | 44.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.50× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.343× (z -9.9) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 98.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.372× (z -10.6) ⚠ toxic |
| [[C-33 A (line)]] | alt | 33.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -10.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 52.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -8.7) ⚠ cell-cycle shift, explains ~9% of this change |
| [[HepG2_C3A (line)]] | wt | 41.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +13.7) | — |
| [[KATO III (line)]] | alt | 39.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -9.9) ⚠ cell-cycle shift, explains ~9% of this change |
| [[LOX-IMVI (line)]] | wt | 53.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 68.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.417× (z -8.5) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 53.9 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.09× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 39.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 38.2 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 4.95× (z +10.1) | — |
| [[SNU-423 (line)]] | alt | 30.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -9.4) ⚠ cell-cycle shift, explains ~9% of this change |
| [[SW 900 (line)]] | alt | 36.1 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.49× (z +8.6) | — |
| [[SW48 (line)]] | wt | 37.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -10.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 32.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4650), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCDH1]] | +0.59 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[ANKRD33B]] | +0.56 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[TPPP]] | +0.56 | +0.38 / +0.54 | both halves | 6e-05 |  |
| [[DENND3]] | +0.55 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[INF2]] | +0.55 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[NGFR]] | +0.55 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[TNIP2]] | +0.53 | +0.49 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CDC42EP5]] | +0.52 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[PIM1]] | +0.52 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[MAPK11]] | +0.51 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[ATP2B4]] | +0.50 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[ENTPD2]] | +0.50 | +0.43 / +0.37 | both halves | 9e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LANCL2]] | -0.45 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[ZNF254]] | -0.44 | -0.53 / -0.29 | both halves | 2e-04 |  |
| [[ANXA2R-OT1]] | -0.44 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[RCBTB2]] | -0.44 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[TAS2R14]] | -0.44 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[TMEM80]] | -0.43 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[C2orf42]] | -0.43 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[C12orf75-AS1]] | -0.42 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[RABL3]] | -0.42 | -0.39 / -0.28 | both halves | 3e-04 |  |
| [[ZNF93]] | -0.42 | -0.41 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FCHO1]] | B | FCHO1 activity raises TRIP10's level | lines that do not express FCHO1 (5) vs lines expressing it (45) | 1.66× lower at baseline in the lines without FCHO1 | 0.056 | ⚠ within organs, on part of the lines; also absent: AMOTL2; maybe low, not absent |
| [[ITGB4]] | B | ITGB4 activity raises TRIP10's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 1.32× lower at baseline in the lines without ITGB4 | 0.090 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[PIM1]] | C | PIM1 activity raises TRIP10's level | lines that do not express PIM1 (4) vs lines expressing it (46) | 1.88× lower at baseline in the lines without PIM1 | 0.060 | ⚠ few lines (4 vs 46); across organs; also absent: CLSTN3, HFE, HACD1; maybe low, not absent |
| [[GSN]] | C | GSN activity raises TRIP10's level | lines that do not express GSN (3) vs lines expressing it (47) | 1.68× lower at baseline in the lines without GSN | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYH16, PER3, IGF2BP2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.528). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.1, 31.8); signed map (-1.9, 21.7). **Vector** length 106, 26.1% of its response variance represented; |z| ≥ 3 in 869 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.7 | +8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +2.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.4 | +7.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.3 | +4.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.2 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +0.0 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +2.3 | +3.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.0 | +3.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +2.1 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.8 | -4.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | +1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | +0.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -3.3 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -2.0 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | thyroid hormone receptor interactor 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:6,737,925-6,751,530 (+) |
| Ensembl biotype | protein_coding |
| Also known as | STP, HSTP, CIP4; previously STOT |
| Gene groups (HGNC) | Minor histocompatibility antigens; F-BAR domain containing; SH3 domain containing |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 7 pathways, smallest: RHOQ GTPase cycle; Clathrin-mediated endocytosis; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15642](https://www.uniprot.org/uniprotkb/Q15642) (Cdc42-interacting protein 4):

> Required for translocation of GLUT4 to the plasma membrane in response to insulin signaling (By similarity). Required to coordinate membrane tubulation with reorganization of the actin cytoskeleton during endocytosis. Binds to lipids such as phosphatidylinositol 4,5-bisphosphate and phosphatidylserine and promotes membrane invagination and the formation of tubules. Also promotes CDC42-induced actin polymerization by recruiting WASL/N-WASP which in turn activates the Arp2/3 complex. Actin …

**Summary**, from NCBI Gene [9322](https://www.ncbi.nlm.nih.gov/gene/9322):

> Enables identical protein binding activity. Predicted to be involved in actin cytoskeleton organization and signal transduction. Located in extracellular exosome. Biomarker of Huntington's disease. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:12304](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12304) · Entrez [9322](https://www.ncbi.nlm.nih.gov/gene/9322) · UniProt [Q15642](https://www.uniprot.org/uniprotkb/Q15642) · Ensembl [ENSG00000125733](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125733)

## Data

Gene col 4650: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4650); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4650, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4650]; `tensor/DDL_lfc|DDL_z.npy` [4650]; `embed/gene_vectors.npy` [4650]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4650 or target_col == 4650). Every well: [[TRIP10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIP10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
