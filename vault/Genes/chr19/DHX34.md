---
symbol: "DHX34"
type: "gene"
col: 5608
ensembl_id: "ENSG00000134815"
name: "DExH-box helicase 34"
location: "19q13.32"
module: 5
arm: "+"
pooled_cpm: 35.85
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# DHX34

*DExH-box helicase 34* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.73× (z +14.3, q 2e-43, up in 41 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.377×); [[AZD2858 (drug)]] 0.5 µM in 1 line (A-427 0.186×; ⚠ toxic); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.684×; ⚠ position not correctable); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (Hs 766T 0.184×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (Hs 766T 0.198×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF26]] (+0.67, fdr 7e-06), [[MRTO4]] (+0.67, fdr 7e-06), [[TRMT1]] (+0.67, fdr 1e-05); moves opposite to [[MPC2]] (-0.62, fdr 7e-06), [[MAPRE2]] (-0.57, fdr 3e-05), [[ADD3]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SESN3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5608.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +14.3 | 2e-43 | 41/48 (HT-29, KATO III, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.68×** | +13.5 | 6e-39 | 39/47 (NCI-H2030, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.93×** | +12.1 | 3e-31 | 38/47 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.93×** | +12.0 | 3e-31 | 43/48 (HT-29, BT-474, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.89×** | +11.7 | 1e-29 | 40/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.87×** | +11.5 | 8e-29 | 41/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +8.7 | 3e-16 | 41/46 (HT-29, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.17×** | +7.4 | 8e-12 | 35/49 (COLO 205, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +7.2 | 4e-11 | 29/48 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +7.1 | 9e-11 | 31/48 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.02×** | +6.7 | 9e-10 | 31/48 (RKO, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +6.4 | 5e-09 | 27/48 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +5.1 | 1e-05 | 24/43 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.33×** | +5.0 | 2e-05 | 22/47 (HOP62, HT-29, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +5.0 | 2e-05 | 25/48 (J82, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.002 | 19/48 (AsPC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +4.0 | 0.002 | 20/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.009 | 17/48 (COLO 205, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[ULK-101 (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.017 | 13/48 (MIA PaCa-2, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5608.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.377×); [[AZD2858 (drug)]] 0.5 µM in 1 line (A-427 0.186×; ⚠ toxic); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.684×; ⚠ position not correctable); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (Hs 766T 0.184×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (Hs 766T 0.198×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | 0.873× | -3.5 | 0.22 | 8/48 (RKO, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.842× | -3.2 | 0.24 | 5/48 (HCT15, NCI-H1792, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.867× | -3.1 | 0.24 | 15/48 (MIA PaCa-2, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.848× | -3.0 | 0.24 | 16/48 (MIA PaCa-2, SW 1088, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 0.732× | -3.0 | 0.24 | 10/46 (C-33 A, RKO, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5608. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 39.6 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +12.6) | — |
| [[SW480 (line)]] | alt | 40.9 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.58× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 19.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +10.6) | — |
| [[LoVo (line)]] | wt | 30.9 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.09× (z +10.6) | — |
| [[A-427 (line)]] | wt | 43.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -13.3) |
| [[AsPC-1 (line)]] | alt | 23.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +11.5) | — |
| [[HOP62 (line)]] | alt | 19.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +9.7) | — |
| [[Hs 766T (line)]] | wt | 16.8 | 0 | 2 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.184× (z -10.1) |
| [[KATO III (line)]] | alt | 37.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +12.1) | [[Digitoxin (drug)]] 5 µM 0.275× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 23.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +10.3) | — |
| [[NCI-H1792 (line)]] | alt | 32.4 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.44× (z +9.2) | — |
| [[NCI-H2347 (line)]] | alt | 20.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +10.0) | — |
| [[SW 900 (line)]] | alt | 27.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 55.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +11.2) | — |
| [[BT-474 (line)]] | alt | 45.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.94× (z +9.0) | — |
| [[COLO 205 (line)]] | alt | 25.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +10.0) | — |
| [[HCT15 (line)]] | alt | 37.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 64.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 41.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +11.7) | — |
| [[NCI-H460 (line)]] | wt | 25.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 30.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 35.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 38.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 19.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +10.0) | — |
| [[SW48 (line)]] | wt | 39.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5608), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF26]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[MRTO4]] | +0.67 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[TRMT1]] | +0.67 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[GTPBP4]] | +0.66 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[BRD9]] | +0.66 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[TWNK]] | +0.65 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[PDCD11]] | +0.65 | +0.73 / +0.68 | both halves | 7e-06 | STRING 466 |
| [[DHX37]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 | same gene group |
| [[MORC2]] | +0.64 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[WDR4]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[WDR81]] | +0.63 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[ERICH1]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPC2]] | -0.62 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[MAPRE2]] | -0.57 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[ADD3]] | -0.57 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[FAM102B]] | -0.56 | -0.64 / -0.37 | both halves | 7e-05 |  |
| [[CXADR]] | -0.56 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[CAT]] | -0.55 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[TWSG1]] | -0.55 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[MAP3K2]] | -0.54 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[GGH]] | -0.54 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[HMGN3]] | -0.54 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[MPP1]] | -0.53 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[MEGF9]] | -0.53 | -0.46 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SESN3]] | B | SESN3 activity strengthens DHX34's drug response | lines that do not express SESN3 (20) vs lines expressing it (29) | the lines without SESN3 respond 0.72× as strongly (z diff +1.16); strongest at Homoharringtonine 5 µM: 1.40x vs 1.82x (z diff +3.0) | 0.099 | ⚠ within organs, on part of the lines; also absent: EPHA4, GNG2, ST6GALNAC5; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TP53]] | C | TP53 activity weakens DHX34's drug response | recorded loss-of-function mutation of TP53 in 32 lines vs 17 not recorded | the TP53-altered lines respond 1.18× as strongly (z diff -0.78); strongest at Idarubicin (hydrochloride) 5 µM: 1.93x vs 1.46x (z diff -3.3) | 0.907 over the table, 0.086 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.669). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.7, -32.4); signed map (-0.0, -47.4). **Vector** length 103, 26.1% of its response variance represented; |z| ≥ 3 in 1,117 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.51 to 13); *rRNA processing* (reactome, mean cos +0.50 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.50 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.3 | +12.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +6.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.0 | +5.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.7 | +7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +4.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.1 | +2.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -2.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.6 | +1.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.4 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.3 | -0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.2 | -2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | DExH-box helicase 34 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:47,349,315-47,382,704 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0134; previously DDX34 |
| Gene groups (HGNC) | DEAH-box helicases; SURF complex; DECID complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14147](https://www.uniprot.org/uniprotkb/Q14147) (Probable ATP-dependent RNA helicase DHX34):

> Probable ATP-binding RNA helicase required for nonsense-mediated decay (NMD) degradation of mRNA transcripts containing premature stop codons. Promotes the phosphorylation of UPF1 along with its interaction with key NMD pathway proteins UPF2 and EIF4A3. Interaction with the RUVBL1-RUVBL2 complex results in loss of nucleotide binding ability and ATP hydrolysis of the complex. Negatively regulates the nucleotide binding ability and ATP hydrolysis of the RUVBL1-RUVBL2 complex via induction of …

**Summary**, from NCBI Gene [9704](https://www.ncbi.nlm.nih.gov/gene/9704):

> DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this DEAD box protein family are believed to be involved in embryogenesis, spermatogenesis, and cellular growth and division. …

**Accessions** — [HGNC:16719](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16719) · Entrez [9704](https://www.ncbi.nlm.nih.gov/gene/9704) · UniProt [Q14147](https://www.uniprot.org/uniprotkb/Q14147) · Ensembl [ENSG00000134815](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134815)

## Data

Gene col 5608: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5608); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5608, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5608]; `tensor/DDL_lfc|DDL_z.npy` [5608]; `embed/gene_vectors.npy` [5608]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5608 or target_col == 5608). Every well: [[DHX34 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHX34.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
