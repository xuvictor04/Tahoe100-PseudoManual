---
symbol: "NDUFAF4"
type: "gene"
col: 4441
ensembl_id: "ENSG00000123545"
name: "NADH:ubiquinone oxidoreductase complex assembly factor 4"
location: "6q16.1"
module: 1
arm: "+"
pooled_cpm: 7.71
n_lines_expressing: 50
n_dd_up: 45
n_dd_down: 0
n_dd_up_clean: 27
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# NDUFAF4

*NADH:ubiquinone oxidoreductase complex assembly factor 4* — 6q16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 45 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.64× (z +13.4, q 5e-38, up in 40 of 44 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 3.63× (z +11.7, q 2e-29, up in 43 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.495×; ⚠ position not correctable); [[Vortioxetine (drug)]] 0.5 µM in 1 line (BT-474 0.0430×); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.269×; ⚠ cell-cycle shift, explains ~31% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRS1]] (+0.79, fdr 7e-06), [[NIP7]] (+0.74, fdr 7e-06), [[MRTO4]] (+0.71, fdr 7e-06); moves opposite to [[GNAS]] (-0.59, fdr 7e-06), [[NUCB2]] (-0.58, fdr 1e-05), [[KDELR1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 18 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 45 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4441.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.64×** | +13.4 | 5e-38 | 40/44 (PANC-1, J82, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **3.63×** | +11.7 | 2e-29 | 43/46 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.32×** | +11.7 | 3e-29 | 38/40 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.95×** | +10.5 | 7e-24 | 42/47 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.86×** | +9.6 | 1e-19 | 27/35 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.80×** | +9.4 | 8e-19 | 29/32 (LOX-IMVI, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **2.48×** | +8.3 | 1e-14 | 9/12 (NCI-H460, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **2.31×** | +8.1 | 3e-14 | 25/30 (NCI-H1792, HT-29, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.28×** | +7.4 | 7e-12 | 16/20 (NCI-H460, Hs 766T, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.99×** | +7.1 | 1e-10 | 36/45 (PANC-1, A-427, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.06×** | +7.0 | 1e-10 | 32/47 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.05×** | +7.0 | 1e-10 | 29/47 (HOP62, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +6.4 | 6e-09 | 27/42 (Hs 766T, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.92×** | +6.3 | 9e-09 | 30/47 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.92×** | +6.3 | 1e-08 | 26/47 (A-172, HOP62, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.23×** | +6.0 | 8e-08 | 21/41 (NCI-H2030, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.75×** | +5.4 | 2e-06 | 24/47 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.75×** | +5.1 | 1e-05 | 19/45 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.71×** | +4.9 | 2e-05 | 19/44 (HOP62, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.65×** | +4.8 | 3e-05 | 20/44 (NCI-H1792, RKO, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.003 | 9/47 (C32, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **2.05×** | +3.7 | 0.005 | 7/39 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.98×** | +3.5 | 0.009 | 6/40 (PANC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4441.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.495×; ⚠ position not correctable); [[Vortioxetine (drug)]] 0.5 µM in 1 line (BT-474 0.0430×); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.269×; ⚠ cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.674× | -3.7 | 0.13 | 13/47 (NCI-H23, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Resveratrol (drug)]] 0.5 µM |  | 0.712× | -3.4 | 0.20 | 15/44 (SW1417, C-33 A, …) | inconsistent across doses |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.703× | -3.3 | 0.20 | 11/47 (H4, A-172, …) | top dose only | plate-row cell shift |
| [[Trametinib (drug)]] 0.05 µM |  | 0.805× | -3.0 | 0.38 | 17/47 (HepG2/C3A, A-427, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4441. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 12.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +12.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 7.75× (z +12.3) | — |
| [[BT-474 (line)]] | alt | 6.73 | 0 | 1 | — | [[Vortioxetine (drug)]] 0.5 µM 0.0430× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 7.33 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +8.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[J82 (line)]] | alt | 6.49 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +8.7) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 9.71 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.495× (z -10.2) ⚠ position not correctable |
| [[RKO (line)]] | wt | 16.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -9.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4441), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRS1]] | +0.79 | +0.79 / +0.78 | both halves | 7e-06 |  |
| [[NIP7]] | +0.74 | +0.70 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[MRTO4]] | +0.71 | +0.73 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[PAK1IP1]] | +0.71 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[SCO1]] | +0.70 | +0.69 / +0.70 | both halves | 7e-06 | same gene group; pathway: Aerobic respiration and respiratory electron transport |
| [[BYSL]] | +0.70 | +0.69 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[MAK16]] | +0.69 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[GPATCH4]] | +0.69 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[IFRD2]] | +0.68 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[MRPL15]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[COA7]] | +0.68 | +0.77 / +0.64 | both halves | 7e-06 | same gene group |
| [[NOP16]] | +0.67 | +0.70 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.59 | -0.61 / -0.72 | both halves | 7e-06 |  |
| [[NUCB2]] | -0.58 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[KDELR1]] | -0.58 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[HDAC6]] | -0.57 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[SEPTIN2]] | -0.56 | -0.62 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.719). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.7, -37.4); signed map (-0.6, -43.8). **Vector** length 70.1, 13.1% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.51 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.52 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.52 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.7 | +10.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.6 | +11.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +11.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +6.0 |
| fall | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -1.9 | -3.7 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | -1.7 | +3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.5 | -0.8 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -1.5 | -3.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase complex assembly factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q16.1 — chr6:96,889,315-96,897,891 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC125, bA22L21.1, My013, HRPAP20; previously C6orf66 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Hallmark sets | MYC_TARGETS_V2 |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P032](https://www.uniprot.org/uniprotkb/Q9P032) (NADH dehydrogenase):

> Involved in the assembly of mitochondrial NADH:ubiquinone oxidoreductase complex (complex I). May be involved in cell proliferation and survival of hormone-dependent tumor cells. May be a regulator of breast tumor cell invasion.

**Summary**, from NCBI Gene [29078](https://www.ncbi.nlm.nih.gov/gene/29078):

> NADH:ubiquinone oxidoreductase (complex I) catalyzes the transfer of electrons from NADH to ubiquinone (coenzyme Q) in the first step of the mitochondrial respiratory chain, resulting in the translocation of protons across the inner mitochondrial membrane. This gene encodes a complex I assembly factor. Mutations in this gene are a cause of mitochondrial complex I deficiency. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:21034](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21034) · Entrez [29078](https://www.ncbi.nlm.nih.gov/gene/29078) · UniProt [Q9P032](https://www.uniprot.org/uniprotkb/Q9P032) · Ensembl [ENSG00000123545](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123545)

## Data

Gene col 4441: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4441); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4441, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4441]; `tensor/DDL_lfc|DDL_z.npy` [4441]; `embed/gene_vectors.npy` [4441]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4441 or target_col == 4441). Every well: [[NDUFAF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFAF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
