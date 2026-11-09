---
symbol: "ARL8A"
type: "gene"
col: 6816
ensembl_id: "ENSG00000143862"
name: "ARF like GTPase 8A"
location: "1q32.1"
module: 3
arm: "+"
pooled_cpm: 26.06
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# ARL8A

*ARF like GTPase 8A* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.60× (z +6.0, q 9e-07, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.463× (z -9.8, q 5e-20, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAHD1]] (+0.78, fdr 7e-06), [[DSTYK]] (+0.67, fdr 1e-05), [[SIRT7]] (+0.66, fdr 1e-05); moves opposite to [[CBX5]] (-0.65, fdr 7e-06), [[HNRNPC]] (-0.65, fdr 3e-05), [[SRP9]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6816.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.60×** | +6.0 | 9e-07 | 31/47 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.61×** | +5.8 | 2e-06 | 31/48 (C32, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.49×** | +5.1 | 6e-05 | 33/48 (C32, NCI-H460, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.68×** | +4.7 | 3e-04 | 30/46 (A-172, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +4.5 | 8e-04 | 24/47 (C32, SW480, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +4.4 | 0.001 | 27/46 (SHP-77, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.54×** | +4.0 | 0.006 | 24/47 (KATO III, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.48×** | +3.6 | 0.023 | 18/48 (A-172, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.027 | 21/48 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.47×** | +3.5 | 0.027 | 16/48 (A-172, C32, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.031 | 15/47 (HEC-1-A, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.4 | 0.036 | 16/47 (A-172, NCI-H1573, …) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.077 | 11/47 (C32, A498, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.082 | 10/48 (C32, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.27×** | +3.1 | 0.082 | 17/46 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6816.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.463×** | -9.8 | 5e-20 | 44/48 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.487×** | -9.2 | 1e-17 | 42/48 (A-172, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.611×** | -8.9 | 1e-16 | 33/47 (NCI-H1792, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.546×** | -7.4 | 1e-11 | 26/36 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.589×** | -6.8 | 2e-09 | 32/47 (LoVo, A-172, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.735×** | -3.9 | 0.008 | 22/42 (C32, A-172, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.814×** | -3.7 | 0.017 | 19/48 (HOP62, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.751×** | -3.6 | 0.018 | 21/47 (A-427, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.752×** | -3.6 | 0.018 | 19/48 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6816. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 64.5 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.234× (z -14.1) |
| [[C32 (line)]] | wt | 51.4 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.75× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.163× (z -14.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 26.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.209× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 32.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.238× (z -10.2) |
| [[SW48 (line)]] | wt | 34.9 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.195× (z -9.4) |
| [[LS 180 (line)]] | wt | 25.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.142× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 22.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -16.1) |
| [[A-427 (line)]] | wt | 19.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.207× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 25.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -9.7) |
| [[H4 (line)]] | wt | 19.4 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.154× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 28.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0848× (z -18.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -9.5) |
| [[Hs 766T (line)]] | wt | 35.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.282× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.105× (z -8.5) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 47.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -10.6) |
| [[SHP-77 (line)]] | alt | 15.4 | 0 | 1 | — | [[Ciclopirox (drug)]] 0.05 µM 0.140× (z -10.0) |
| [[A498 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6816), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 5 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAHD1]] | +0.78 | +0.71 / +0.78 | both halves | 7e-06 |  |
| [[DSTYK]] | +0.67 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[SIRT7]] | +0.66 | +0.50 / +0.77 | both halves | 1e-05 |  |
| [[VPS37D]] | +0.65 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[FAM182B]] | +0.65 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[IL17RA]] | +0.65 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[SAP30L]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CCDC126]] | +0.65 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[MRPL32]] | +0.64 | +0.38 / +0.65 | both halves | 6e-05 |  |
| [[CAMLG]] | +0.64 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[SLC26A11]] | +0.64 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[FLYWCH1]] | +0.64 | +0.71 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBX5]] | -0.65 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[HNRNPC]] | -0.65 | -0.45 / -0.70 | both halves | 3e-05 |  |
| [[SRP9]] | -0.63 | -0.43 / -0.63 | both halves | 3e-05 |  |
| [[AKAP11]] | -0.63 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[ERLIN2]] | -0.62 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[XRCC5]] | -0.59 | -0.37 / -0.66 | both halves | 7e-05 |  |
| [[POGLUT3]] | -0.59 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[ARL5B]] | -0.59 | -0.46 / -0.58 | both halves | 2e-05 | same gene group |
| [[YWHAE]] | -0.58 | -0.56 / -0.54 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[HNRNPUL1]] | -0.58 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[LIN7C]] | -0.57 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[ECT2]] | -0.57 | -0.39 / -0.61 | both halves | 6e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ARL8A's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.633). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-38.7, -16.7); signed map (-22.9, 6.0). **Vector** length 99.6, 24.4% of its response variance represented; |z| ≥ 3 in 781 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.0 | +6.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.3 | +5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.4 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +4.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +4.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.0 | +1.0 |
|  | [[Neratinib (drug)]] 5 µM |  | +3.0 | +2.3 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | -4.8 | -3.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | -4.2 | -1.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.4 | -8.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.0 | -2.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.7 | -2.6 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.6 | -2.0 |
|  | [[BI-78D3 (drug)]] 5 µM |  | -1.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 8A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:202,133,404-202,144,743 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ45195, Gie2; previously ARL10B |
| Gene groups (HGNC) | ARF GTPase family |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BM9](https://www.uniprot.org/uniprotkb/Q96BM9) (ADP-ribosylation factor-like protein 8A):

> Plays a role in lysosome motility (By similarity). In neurons, mediates the anterograde axonal long-range transport of presynaptic lysosome-related vesicles required for presynaptic biogenesis and synaptic function (By similarity). May play a role in chromosome segregation (By similarity).

**Summary**, from NCBI Gene [127829](https://www.ncbi.nlm.nih.gov/gene/127829):

> Enables GTP binding activity. Predicted to be involved in anterograde axonal transport and chromosome segregation. Located in cytoplasm; midbody; and spindle midzone. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25192](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25192) · Entrez [127829](https://www.ncbi.nlm.nih.gov/gene/127829) · UniProt [Q96BM9](https://www.uniprot.org/uniprotkb/Q96BM9) · Ensembl [ENSG00000143862](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143862)

## Data

Gene col 6816: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6816); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6816, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6816]; `tensor/DDL_lfc|DDL_z.npy` [6816]; `embed/gene_vectors.npy` [6816]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6816 or target_col == 6816). Every well: [[ARL8A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL8A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
