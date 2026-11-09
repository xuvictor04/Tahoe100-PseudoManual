---
symbol: "ALDH16A1"
type: "gene"
col: 8442
ensembl_id: "ENSG00000161618"
name: "aldehyde dehydrogenase 16 family member A1"
location: "19q13.33"
module: 148
arm: "+"
pooled_cpm: 4.38
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# ALDH16A1

*aldehyde dehydrogenase 16 family member A1* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.28× (z +13.7, q 6e-40, up in 22 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.44× (z +5.9, q 4e-07, up in 18 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.547× (z -7.0, q 1e-09, down in 23 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FIZ1]] (+0.73, fdr 1e-05), [[MEPCE]] (+0.67, fdr 4e-05), [[PMF1]] (+0.65, fdr 3e-05); moves opposite to [[RPS5]] (-0.63, fdr 2e-05), [[RPL11]] (-0.61, fdr 1e-05), [[STX7]] (-0.59, fdr 4e-05).
> It sits in the **+** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8442.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.28×** | +13.7 | 6e-40 | 22/23 (NCI-H460, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.00×** | +11.7 | 3e-29 | 10/12 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.85×** | +11.6 | 5e-29 | 8/9 (CFPAC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +6.9 | 5e-10 | 13/23 (HT-29, A-427, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.44×** | +5.9 | 4e-07 | 21/38 (COLO 205, LS 180, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.9 | 4e-07 | 18/39 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +4.8 | 1e-04 | 7/44 (HT-29, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.50×** | +4.4 | 6e-04 | 9/44 (NCI-H460, COLO 205, …) | rises with dose | composition shift |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +3.7 | 0.013 | 2/11 (SW480, HEC-1-A) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.36×** | +3.6 | 0.021 | 8/24 (HEC-1-A, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.86×** | +3.4 | 0.033 | 1/12 (SW1417) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.033 | 7/43 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.065 | 6/34 (KATO III, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.065 | 4/37 (LS 180, CFPAC-1, …) | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.065 | 3/41 (SK-MEL-2, SW1417, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.44×** | +3.0 | 0.098 | 4/22 (SW480, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8442.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.547×** | -7.0 | 1e-09 | 23/46 (NCI-H2030, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.556×** | -6.8 | 2e-09 | 24/45 (LS 180, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.566×** | -6.6 | 7e-09 | 21/47 (COLO 205, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.620×** | -5.6 | 4e-06 | 23/45 (NCI-H2347, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.678×** | -4.5 | 7e-04 | 17/41 (NCI-H1792, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.503×** | -3.8 | 0.014 | 8/42 (NCI-H23, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.811×** | -3.5 | 0.041 | 11/45 (LS 180, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8442. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 5.62 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 3.68 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0820× (z -9.5) |
| [[LS 180 (line)]] | wt | 5.12 | 0 | 1 | — | [[Rifaximin (drug)]] 0.05 µM 0.0410× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 2.49 | 0 | 1 | — | [[Menadione (drug)]] 0.5 µM 0.0634× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 4.82 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.68× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8442), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FIZ1]] | +0.73 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[MEPCE]] | +0.67 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[PMF1]] | +0.65 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[ZNF689]] | +0.65 | +0.67 / +0.43 | both halves | 3e-05 |  |
| [[HNRNPL]] | +0.64 | +0.70 / +0.39 | both halves | 5e-05 |  |
| [[MIS12]] | +0.64 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[GTF3C6]] | +0.63 | +0.61 / +0.37 | both halves | 9e-05 |  |
| [[C19orf54]] | +0.63 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[USP11]] | +0.63 | +0.59 / +0.37 | both halves | 7e-05 |  |
| [[AFG3L1P]] | +0.63 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[MLH1]] | +0.63 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[MUTYH]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS5]] | -0.63 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[RPL11]] | -0.61 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[STX7]] | -0.59 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[RACK1]] | -0.59 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[HEBP1]] | -0.59 | -0.68 / -0.24 | both halves | 5e-04 |  |
| [[COX6A1]] | -0.58 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[RPL26]] | -0.56 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[RPLP0]] | -0.56 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[RPL27]] | -0.56 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[SGTB]] | -0.56 | -0.55 / -0.40 | both halves | 4e-05 |  |
| [[RPL7]] | -0.55 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[RPS25]] | -0.55 | -0.53 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ALDH16A1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **+** arm (projection on the module's main direction 0.578). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-8.9, 5.9); signed map (15.9, -23.8). **Vector** length 52.5, 6.70% of its response variance represented; |z| ≥ 3 in 891 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +11.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.7 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +11.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +3.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.3 | +3.2 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -2.8 | -7.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.5 | -4.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -3.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.2 | -6.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -1.6 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -0.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | aldehyde dehydrogenase 16 family member A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,453,225-49,471,050 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10204 |
| Gene groups (HGNC) | Aldehyde dehydrogenases |
| Matched by | ensembl_id |

UniProt [Q8IZ83](https://www.uniprot.org/uniprotkb/Q8IZ83) carries no function annotation.

**Summary**, from NCBI Gene [126133](https://www.ncbi.nlm.nih.gov/gene/126133):

> This gene encodes a member of the aldehyde dehydrogenase superfamily. The family members act on aldehyde substrates and use nicotinamide adenine dinucleotide phosphate (NADP) as a cofactor. This gene is conserved in chimpanzee, dog, cow, mouse, rat, and zebrafish. The protein encoded by this gene interacts with maspardin, a protein that when truncated is responsible for Mast syndrome. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided …

**Accessions** — [HGNC:28114](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28114) · Entrez [126133](https://www.ncbi.nlm.nih.gov/gene/126133) · UniProt [Q8IZ83](https://www.uniprot.org/uniprotkb/Q8IZ83) · Ensembl [ENSG00000161618](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161618)

## Data

Gene col 8442: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8442); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8442, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8442]; `tensor/DDL_lfc|DDL_z.npy` [8442]; `embed/gene_vectors.npy` [8442]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8442 or target_col == 8442). Every well: [[ALDH16A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALDH16A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
