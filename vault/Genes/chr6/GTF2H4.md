---
symbol: "GTF2H4"
type: "gene"
col: 13136
ensembl_id: "ENSG00000213780"
name: "general transcription factor IIH subunit 4"
location: "6p21.33"
module: 127
arm: "+"
pooled_cpm: 5.5
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# GTF2H4

*general transcription factor IIH subunit 4* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.79× (z +8.8, q 7e-16, up in 30 of 47 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.60× (z +7.1, q 1e-10, up in 18 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (SW1417 0.0832×); [[BI-78D3 (drug)]] 0.05 µM in 1 line (SHP-77 0.0909×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCAR2]] (+0.59, fdr 1e-05), [[CSTF2]] (+0.59, fdr 1e-05), [[PHB1]] (+0.58, fdr 2e-05); moves opposite to [[EIF1]] (-0.61, fdr 3e-05), [[EIF1B]] (-0.57, fdr 2e-05), [[CYP20A1]] (-0.51, fdr 4e-05).
> It is in [[Module 127]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 15 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13136.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.79×** | +8.8 | 7e-16 | 30/47 (LS 180, COLO 205, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +8.5 | 4e-15 | 21/33 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.74×** | +8.3 | 1e-14 | 25/47 (C32, COLO 205, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.63×** | +7.4 | 2e-11 | 21/46 (Panc 03.27, HCT15, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.60×** | +7.1 | 1e-10 | 18/43 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +6.6 | 3e-09 | 10/47 (A-172, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +6.0 | 2e-07 | 12/33 (SNU-423, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.11×** | +5.9 | 2e-07 | 14/41 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +5.8 | 3e-07 | 8/47 (SNU-423, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.51×** | +5.7 | 6e-07 | 5/16 (SW480, A498, …) | inconsistent across doses | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.43×** | +5.2 | 1e-05 | 5/11 (PANC-1, A498, …) | inconsistent across doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +4.6 | 2e-04 | 9/46 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.24×** | +4.6 | 2e-04 | 11/40 (NCI-H2030, LoVo, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.4 | 4e-04 | 3/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +4.4 | 4e-04 | 9/47 (RKO, Panc 03.27, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.002 | 9/38 (SHP-77, PANC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.6 | 0.013 | 5/47 (SW1417, NCI-H2030, …) | top dose only |  |
| [[Belinostat (drug)]] 0.05 µM |  | **1.25×** | +3.4 | 0.022 | 6/46 (J82, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.044 | 3/38 (J82, PANC-1, …) | inconsistent across doses |  |
| [[Bicalutamide (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.047 | 2/45 (KATO III, MIA PaCa-2) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.049 | 5/44 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Aprepitant (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.055 | 0/45 | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.46×** | +3.0 | 0.058 | 1/31 (PANC-1) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.058 | 9/45 (AN3 CA, NCI-H23, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.45×** | +3.0 | 0.062 | 1/44 (SNU-423) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13136.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (SW1417 0.0832×); [[BI-78D3 (drug)]] 0.05 µM in 1 line (SHP-77 0.0909×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Furosemide (drug)]] 0.5 µM |  | 0.797× | -3.4 | 0.35 | 5/44 (SW480, HOP62, …) | inconsistent across doses |  |
| [[Decitabine (drug)]] 0.5 µM |  | 0.808× | -3.2 | 0.36 | 6/45 (CHP-212, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | 0.807× | -3.0 | 0.51 | 10/41 (HCT15, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13136. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 7.52 | 0 | 1 | — | [[BI-78D3 (drug)]] 0.05 µM 0.0909× (z -9.0) |
| [[SW1417 (line)]] | alt | 5.85 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0832× (z -10.2) |
| [[A-172 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13136), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCAR2]] | +0.59 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[CSTF2]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[PHB1]] | +0.58 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[INTS11]] | +0.56 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[STK36]] | +0.55 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[KAT2A]] | +0.55 | +0.44 / +0.61 | both halves | 3e-05 | pathway: Epigenetic regulation of gene expression |
| [[TBL3]] | +0.55 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[TATDN2]] | +0.54 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[CIPC]] | +0.54 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[MEN1]] | +0.54 | +0.36 / +0.50 | both halves | 1e-04 | pathway: Epigenetic regulation of gene expression |
| [[PEX5]] | +0.53 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[DLAT]] | +0.53 | +0.48 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF1]] | -0.61 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[EIF1B]] | -0.57 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[CYP20A1]] | -0.51 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[XIAP]] | -0.50 | -0.59 / -0.27 | both halves | 3e-04 |  |
| [[NBPF10]] | -0.50 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[FAM193A]] | -0.49 | -0.46 / -0.32 | both halves | 1e-04 |  |
| [[SMIM14]] | -0.49 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[LRCH3]] | -0.48 | -0.61 / -0.24 | both halves | 4e-04 |  |
| [[CCDC186]] | -0.48 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[GPX4]] | -0.48 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[NOTCH2NLB]] | -0.46 | -0.41 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.591). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.7, -26.5); signed map (-14.5, -46.9). **Vector** length 41.8, 4.17% of its response variance represented; |z| ≥ 3 in 829 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.8 | +6.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.4 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.4 | +8.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.3 | +7.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +5.9 |
|  | [[EX229 (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.2 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +3.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.1 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | +1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.2 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | -0.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.9 | -0.4 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -0.8 | -1.4 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -0.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | general transcription factor IIH subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:30,908,207-30,914,106 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TFB2, TFIIH, P52 |
| Gene groups (HGNC) | Nucleotide excision repair; General transcription factor IIH complex subunits |
| Reactome | 42 pathways, smallest: RNA Pol II CTD phosphorylation and interaction with CE during HIV infection; RNA Pol II CTD phosphorylation and interaction with CE; mRNA Capping |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92759](https://www.uniprot.org/uniprotkb/Q92759) (General transcription factor IIH subunit 4):

> Component of the general transcription and DNA repair factor IIH (TFIIH) core complex, which is involved in general and transcription-coupled nucleotide excision repair (NER) of damaged DNA and, when complexed to CAK, in RNA transcription by RNA polymerase II. In NER, TFIIH acts by opening DNA around the lesion to allow the excision of the damaged oligonucleotide and its replacement by a new DNA fragment. In transcription, TFIIH has an essential role in transcription initiation. When the …

**Summary**, from NCBI Gene [2968](https://www.ncbi.nlm.nih.gov/gene/2968):

> Enables RNA polymerase II general transcription initiation factor activity. Involved in transcription by RNA polymerase II. Located in nuclear speck. Part of core TFIIH complex portion of holo TFIIH complex and transcription factor TFIID complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:4658](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4658) · Entrez [2968](https://www.ncbi.nlm.nih.gov/gene/2968) · UniProt [Q92759](https://www.uniprot.org/uniprotkb/Q92759) · Ensembl [ENSG00000213780](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213780)

## Data

Gene col 13136: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13136); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13136, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13136]; `tensor/DDL_lfc|DDL_z.npy` [13136]; `embed/gene_vectors.npy` [13136]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13136 or target_col == 13136). Every well: [[GTF2H4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF2H4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
