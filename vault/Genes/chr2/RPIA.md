---
symbol: "RPIA"
type: "gene"
col: 7731
ensembl_id: "ENSG00000153574"
name: "ribose 5-phosphate isomerase A"
location: "2p11.2"
module: 168
arm: "+"
pooled_cpm: 25.32
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/168"]
generated_by: "tahoemap"
---

# RPIA

*ribose 5-phosphate isomerase A* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.81× (z +13.1, q 2e-36, up in 40 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 4.01× (z +9.2, q 6e-18, up in 37 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.682× (z -6.9, q 4e-09, down in 27 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (PANC-1 0.387×, LOX-IMVI 0.331×, HOP62 0.415×, SW480 0.506×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 0.386×, SW1417 0.316×); [[Flutamide (drug)]] 0.5 µM in 1 line (AN3 CA 0.0870×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPD1L]] (+0.69, fdr 7e-06), [[CCNB1IP1]] (+0.66, fdr 1e-05), [[PEMT]] (+0.66, fdr 7e-06); moves opposite to [[TUBB4B]] (-0.59, fdr 1e-05), [[ATP6V0C]] (-0.56, fdr 8e-05), [[TUT7]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 168]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7731.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.81×** | +13.1 | 2e-36 | 40/43 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.64×** | +10.3 | 2e-22 | 37/41 (NCI-H1792, LS 180, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **4.01×** | +9.2 | 6e-18 | 37/46 (LS 180, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +9.1 | 1e-17 | 28/36 (LoVo, HT-29, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.52×** | +8.3 | 9e-15 | 40/48 (LS 180, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.82×** | +7.6 | 2e-12 | 42/48 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.81×** | +7.6 | 3e-12 | 38/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.69×** | +6.7 | 2e-09 | 37/47 (NCI-H2347, AsPC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +6.6 | 3e-09 | 33/47 (NCI-H1792, HT-29, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.56×** | +6.2 | 3e-08 | 21/25 (NCI-H2347, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.63×** | +6.2 | 4e-08 | 37/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +5.2 | 8e-06 | 25/46 (NCI-H1792, J82, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.50×** | +5.0 | 3e-05 | 26/46 (SW480, NCI-H23, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.6 | 2e-04 | 2/48 (KATO III, HCT15) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.001 | 26/48 (A498, NCI-H2030, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.77×** | +3.8 | 0.005 | 23/46 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.75×** | +3.7 | 0.006 | 21/47 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.012 | 21/47 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.077 | 7/45 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7731.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (PANC-1 0.387×, LOX-IMVI 0.331×, HOP62 0.415×, SW480 0.506×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 0.386×, SW1417 0.316×); [[Flutamide (drug)]] 0.5 µM in 1 line (AN3 CA 0.0870×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.682×** | -6.9 | 4e-09 | 27/47 (PANC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.675×** | -5.0 | 2e-04 | 27/48 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7731. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 29.8 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.51× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 10.6× (z +9.5) | — |
| [[SW480 (line)]] | alt | 29.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +13.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -8.5) |
| [[HOP62 (line)]] | alt | 18.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.0) |
| [[LoVo (line)]] | wt | 16.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.52× (z +14.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 33.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 21.9 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 28.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -13.1) |
| [[HT-29 (line)]] | alt | 18.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.05× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 34.8 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -8.9) |
| [[AN3 CA (line)]] | alt | 36.3 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.0870× (z -10.0) |
| [[C32 (line)]] | wt | 19.8 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 20.6× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 19.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +8.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 34.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 16.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.20× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 47.5 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 9.84× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 18.3 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.56× (z +8.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H460 (line)]] | wt | 24.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.69× (z +9.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 35.1 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 10.1× (z +8.9) | — |
| [[SW48 (line)]] | wt | 31.6 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 6.73× (z +10.0) | — |
| [[A-172 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7731), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPD1L]] | +0.69 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CCNB1IP1]] | +0.66 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[PEMT]] | +0.66 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[WDR3]] | +0.66 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[RPL6]] | +0.64 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[MRPS35]] | +0.63 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[MTRR]] | +0.62 | +0.65 / +0.55 | both halves | 1e-05 | pathway: Diseases of metabolism |
| [[TSFM]] | +0.62 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[ENOPH1]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[FOXJ3]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[SCAP]] | +0.61 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[MRS2]] | +0.61 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBB4B]] | -0.59 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[ATP6V0C]] | -0.56 | -0.66 / -0.37 | both halves | 8e-05 |  |
| [[TUT7]] | -0.53 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[BAZ2B]] | -0.52 | -0.55 / -0.37 | both halves | 9e-05 |  |
| [[ERVK3-1]] | -0.51 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[KANSL1L]] | -0.50 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[AKT1S1]] | -0.49 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[TCEAL9]] | -0.49 | -0.46 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 168]]; 25 genes; this gene is in the **+** arm (projection on the module's main direction 0.619). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-8.6, -15.5); signed map (-42.4, -16.2). **Vector** length 110, 30.0% of its response variance represented; |z| ≥ 3 in 862 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +6.8 | +9.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.8 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +13.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +9.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.5 | +3.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +3.2 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.3 | -6.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -6.2 | -5.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.0 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -2.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.1 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Filgotinib (drug)]] 0.05 µM |  | -1.8 | -2.9 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ribose 5-phosphate isomerase A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:88,691,673-88,750,929 (+) |
| Ensembl biotype | protein_coding |
| Reactome | 4 pathways, smallest: Pentose phosphate pathway; Diseases of carbohydrate metabolism; Diseases of metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P49247](https://www.uniprot.org/uniprotkb/P49247) (Ribose-5-phosphate isomerase):

> Catalyzes the reversible conversion of ribose-5-phosphate to ribulose 5-phosphate and participates in the first step of the non-oxidative branch of the pentose phosphate pathway.

**Summary**, from NCBI Gene [22934](https://www.ncbi.nlm.nih.gov/gene/22934):

> The protein encoded by this gene is an enzyme, which catalyzes the reversible conversion between ribose-5-phosphate and ribulose-5-phosphate in the pentose-phosphate pathway. This gene is highly conserved in most organisms. The enzyme plays an essential role in the carbohydrate metabolism. Mutations in this gene cause ribose 5-phosphate isomerase deficiency. A pseudogene is found on chromosome 18. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:10297](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10297) · Entrez [22934](https://www.ncbi.nlm.nih.gov/gene/22934) · UniProt [P49247](https://www.uniprot.org/uniprotkb/P49247) · Ensembl [ENSG00000153574](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153574)

## Data

Gene col 7731: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7731); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7731, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7731]; `tensor/DDL_lfc|DDL_z.npy` [7731]; `embed/gene_vectors.npy` [7731]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7731 or target_col == 7731). Every well: [[RPIA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPIA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
