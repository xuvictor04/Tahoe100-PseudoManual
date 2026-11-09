---
symbol: "DDX51"
type: "gene"
col: 11633
ensembl_id: "ENSG00000185163"
name: "DEAD-box helicase 51"
location: "12q24.33"
module: 5
arm: "+"
pooled_cpm: 9.51
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# DDX51

*DEAD-box helicase 51* — 12q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.20× (z +9.5, q 1e-18, up in 15 of 19 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.79× (z +7.3, q 3e-11, up in 31 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.681× (z -6.7, q 1e-08, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Simotinib (drug)]] 5 µM in 1 line (A549 0.0900×; ⚠ toxic); [[Capmatinib (drug)]] 0.05 µM in 1 line (Hs 766T 0.0530×); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (SNU-1 0.0628×); [[Benproperine (phosphate) (drug)]] 5 µM in 1 line (RPMI-7951 0.0594×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF276]] (+0.75, fdr 7e-06), [[SPOUT1]] (+0.68, fdr 7e-06), [[TRMT1]] (+0.66, fdr 7e-06); moves opposite to [[GGH]] (-0.56, fdr 1e-05), [[ADD3]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GSTM3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 17 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11633.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.20×** | +9.5 | 1e-18 | 15/19 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +8.2 | 5e-14 | 16/24 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.92×** | +8.2 | 6e-14 | 20/33 (LoVo, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +7.5 | 8e-12 | 26/39 (NCI-H1573, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +7.3 | 3e-11 | 31/44 (LOX-IMVI, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.41×** | +6.0 | 2e-07 | 24/46 (KATO III, SHP-77, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +5.4 | 5e-06 | 21/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.27×** | +5.4 | 5e-06 | 23/47 (SW480, KATO III, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.51×** | +5.2 | 1e-05 | 23/45 (NCI-H1573, J82, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.51×** | +5.2 | 1e-05 | 22/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.51×** | +5.2 | 1e-05 | 20/47 (NCI-H460, A549, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.45×** | +4.6 | 2e-04 | 16/47 (AsPC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.43×** | +4.5 | 3e-04 | 17/47 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.95×** | +4.4 | 5e-04 | 16/43 (MIA PaCa-2, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.2 | 9e-04 | 11/46 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.004 | 16/47 (NCI-H2347, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.49×** | +3.5 | 0.010 | 9/41 (A549, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.022 | 6/47 (LoVo, HCT15, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.30×** | +3.1 | 0.043 | 15/47 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11633.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Simotinib (drug)]] 5 µM in 1 line (A549 0.0900×; ⚠ toxic); [[Capmatinib (drug)]] 0.05 µM in 1 line (Hs 766T 0.0530×); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (SNU-1 0.0628×); [[Benproperine (phosphate) (drug)]] 5 µM in 1 line (RPMI-7951 0.0594×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.681×** | -6.7 | 1e-08 | 27/48 (A498, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.733×** | -3.9 | 0.022 | 14/47 (SW1417, A498, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.769× | -3.4 | 0.15 | 12/47 (AsPC-1, HEC-1-A, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.783× | -3.1 | 0.26 | 9/48 (NCI-H2030, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11633. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 13.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[RPMI-7951 (line)]] | alt | 8.32 | 0 | 2 | — | [[Benproperine (phosphate) (drug)]] 5 µM 0.0594× (z -10.5) |
| [[A549 (line)]] | wt | 9.28 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0900× (z -11.6) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 7.00 | 0 | 1 | — | [[Capmatinib (drug)]] 0.05 µM 0.0530× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 6.24 | 0 | 1 | — | [[Carbamazepine (drug)]] 0.05 µM 0.0719× (z -9.1) |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0628× (z -10.8) |
| [[A-172 (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.94 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11633), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF276]] | +0.75 | +0.72 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SPOUT1]] | +0.68 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[TRMT1]] | +0.66 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[NOM1]] | +0.66 | +0.71 / +0.57 | both halves | 9e-06 |  |
| [[DDX31]] | +0.65 | +0.66 / +0.65 | both halves | 7e-06 | same gene group; STRING 485 |
| [[PUS1]] | +0.64 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[C1orf109]] | +0.64 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[L3MBTL2]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[MRTO4]] | +0.63 | +0.69 / +0.62 | both halves | 7e-06 | STRING 512 |
| [[LTV1]] | +0.63 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[TRIM65]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[TRMT44]] | +0.63 | +0.55 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GGH]] | -0.56 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ADD3]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GSTM3]] | B | GSTM3 activity raises DDX51's level | lines that do not express GSTM3 (14) vs lines expressing it (36) | 1.11× lower at baseline in the lines without GSTM3 | 0.073 | ⚠ within organs, on part of the lines; also absent: ESYT3, CADM1, TGFB1I1 |
| [[ATP1B1]] | B | ATP1B1 activity lowers DDX51's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 1.32× higher at baseline in the lines without ATP1B1 | 0.099 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.626). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-16.8, -40.7); signed map (1.2, -47.8). **Vector** length 58.1, 8.58% of its response variance represented; |z| ≥ 3 in 748 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +5.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.5 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.2 | +7.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +4.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[EX229 (drug)]] 5 µM |  | +1.6 | +2.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.8 | -3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | +0.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 51 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.33 — chr12:132,136,594-132,144,319 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | DEAD-box helicases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N8A6](https://www.uniprot.org/uniprotkb/Q8N8A6) (ATP-dependent RNA helicase DDX51):

> ATP-binding RNA helicase involved in the biogenesis of 60S ribosomal subunits.

**Summary**, from NCBI Gene [317781](https://www.ncbi.nlm.nih.gov/gene/317781):

> Enables RNA binding activity. Predicted to be involved in rRNA processing. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20082](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20082) · Entrez [317781](https://www.ncbi.nlm.nih.gov/gene/317781) · UniProt [Q8N8A6](https://www.uniprot.org/uniprotkb/Q8N8A6) · Ensembl [ENSG00000185163](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185163)

## Data

Gene col 11633: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11633); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11633, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11633]; `tensor/DDL_lfc|DDL_z.npy` [11633]; `embed/gene_vectors.npy` [11633]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11633 or target_col == 11633). Every well: [[DDX51 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX51.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
