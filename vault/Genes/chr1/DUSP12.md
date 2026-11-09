---
symbol: "DUSP12"
type: "gene"
col: 1322
ensembl_id: "ENSG00000081721"
name: "dual specificity phosphatase 12"
location: "1q23.3"
module: 17
arm: "+"
pooled_cpm: 15.61
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# DUSP12

*dual specificity phosphatase 12* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (16 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 2.30× (z +8.1, q 3e-13, up in 35 of 43 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 2.04× (z +7.2, q 6e-11, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.764× (z -3.8, q 0.077, down in 27 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Temsirolimus (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0755×); [[Pimozide (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0914×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RTCA]] (+0.62, fdr 1e-05), [[NEPRO]] (+0.62, fdr 1e-05), [[SLC2A11]] (+0.61, fdr 3e-05); moves opposite to [[CFL1]] (-0.54, fdr 4e-05), [[BZW1]] (-0.51, fdr 4e-05), [[ACTR2]] (-0.48, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LRP3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 16 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1322.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.30×** | +8.1 | 3e-13 | 35/43 (LoVo, SHP-77, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.16×** | +7.8 | 1e-12 | 38/48 (NCI-H460, LS 180, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.16×** | +7.8 | 1e-12 | 37/46 (NCI-H460, KATO III, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.66×** | +7.3 | 4e-11 | 34/47 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.04×** | +7.2 | 6e-11 | 42/47 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.99×** | +7.0 | 2e-10 | 37/47 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.91×** | +6.5 | 5e-09 | 30/42 (HOP62, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.86×** | +6.0 | 2e-07 | 32/47 (CFPAC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.81×** | +5.8 | 4e-07 | 19/27 (HOP62, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.69×** | +5.4 | 5e-06 | 30/43 (NCI-H2347, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +5.1 | 2e-05 | 28/43 (NCI-H2030, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.66×** | +5.0 | 3e-05 | 31/46 (SW480, A-427, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.63×** | +5.0 | 3e-05 | 28/47 (A-427, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +4.5 | 3e-04 | 19/34 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.34×** | +4.5 | 3e-04 | 26/48 (NCI-H1573, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.002 | 24/48 (Panc 03.27, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.64×** | +3.4 | 0.018 | 13/46 (LoVo, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.63×** | +3.4 | 0.020 | 16/46 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.020 | 17/45 (Panc 03.27, HepG2/C3A, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.023 | 18/48 (CFPAC-1, Hs 766T, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.051 | 12/48 (HEC-1-A, NCI-H460, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.55×** | +3.0 | 0.057 | 5/46 (KATO III, HCT15, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.53×** | +2.9 | 0.067 | 9/44 (LoVo, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.52×** | +2.9 | 0.075 | 13/48 (PANC-1, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.33×** | +2.8 | 0.099 | 10/48 (C32, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1322.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Temsirolimus (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0755×); [[Pimozide (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0914×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.764×** | -3.8 | 0.077 | 27/46 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.704× | -3.5 | 0.10 | 14/47 (AsPC-1, C32, …) | inconsistent across doses |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.699× | -3.5 | 0.10 | 20/47 (C32, COLO 205, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1322. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.2 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.57× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 2 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0755× (z -9.7) |
| [[KATO III (line)]] | alt | 9.84 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.10× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[LS 180 (line)]] | wt | 16.7 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.24× (z +10.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HOP62 (line)]] | alt | 14.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[LoVo (line)]] | wt | 9.39 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 8.61× (z +10.5) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1322), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTCA]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[NEPRO]] | +0.62 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[SLC2A11]] | +0.61 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[MRPL21]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[PYROXD1]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[NELFA]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[MRPL22]] | +0.58 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[IRAK1BP1]] | +0.58 | +0.46 / +0.67 | both halves | 2e-05 |  |
| [[METTL17]] | +0.58 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[SARNP]] | +0.57 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[PRPF39]] | +0.57 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[HSF2]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFL1]] | -0.54 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[BZW1]] | -0.51 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[ACTR2]] | -0.48 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[TLN1]] | -0.48 | -0.29 / -0.59 | both halves | 3e-04 |  |
| [[CYCS]] | -0.48 | -0.36 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRP3]] | B | LRP3 activity raises DUSP12's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without LRP3 | 0.014 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.543). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-23.6, -3.4); signed map (-24.8, -11.6). **Vector** length 66.4, 14.0% of its response variance represented; |z| ≥ 3 in 762 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.6 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.9 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +7.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.7 | +0.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.4 | +0.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.9 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -0.7 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -1.4 | -3.5 |
|  | [[Decitabine (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.2 | -0.7 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | dual specificity phosphatase 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:161,749,758-161,757,238 (+) |
| Ensembl biotype | protein_coding |
| Also known as | YVH1, DUSP1 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Atypical dual specificity phosphatases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNI6](https://www.uniprot.org/uniprotkb/Q9UNI6) (Dual specificity protein phosphatase 12):

> Dual specificity phosphatase; can dephosphorylate both phosphotyrosine and phosphoserine or phosphothreonine residues. Can dephosphorylate glucokinase (in vitro) (By similarity). Has phosphatase activity with the synthetic substrate 6,8-difluoro-4-methylumbelliferyl phosphate and other in vitro substrates.

**Summary**, from NCBI Gene [11266](https://www.ncbi.nlm.nih.gov/gene/11266):

> The protein encoded by this gene is a member of the dual specificity protein phosphatase subfamily. These phosphatases inactivate their target kinases by dephosphorylating both the phosphoserine/threonine and phosphotyrosine residues. They negatively regulate members of the mitogen-activated protein (MAP) kinase superfamily (MAPK/ERK, SAPK/JNK, p38), which is associated with cellular proliferation and differentiation. Different members of the family of dual specificity phosphatases show …

**Accessions** — [HGNC:3067](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3067) · Entrez [11266](https://www.ncbi.nlm.nih.gov/gene/11266) · UniProt [Q9UNI6](https://www.uniprot.org/uniprotkb/Q9UNI6) · Ensembl [ENSG00000081721](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081721)

## Data

Gene col 1322: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1322); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1322, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1322]; `tensor/DDL_lfc|DDL_z.npy` [1322]; `embed/gene_vectors.npy` [1322]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1322 or target_col == 1322). Every well: [[DUSP12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUSP12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
