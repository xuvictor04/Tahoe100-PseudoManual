---
symbol: "ESRRA"
type: "gene"
col: 10346
ensembl_id: "ENSG00000173153"
name: "estrogen related receptor alpha"
location: "11q13.1"
module: 28
arm: "-"
pooled_cpm: 21.58
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# ESRRA

*estrogen related receptor alpha* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.85× (z +8.9, q 3e-16, up in 37 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.389× (z -5.1, q 2e-04, down in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (Panc 03.27 0.232×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (HS-578T 0.300×; ⚠ cell-cycle shift, explains ~54% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SW48 0.199×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AXIN1]] (+0.67, fdr 1e-05), [[FAM89A]] (+0.63, fdr 1e-05), [[TSEN54]] (+0.60, fdr 2e-05); moves opposite to [[NDUFA5]] (-0.59, fdr 3e-05), [[HMGN2]] (-0.58, fdr 8e-05), [[SF3B1]] (-0.57, fdr 4e-05).
> It sits in the **-** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAPK14]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10346.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +8.9 | 3e-16 | 37/46 (HEC-1-A, A549, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.14×** | +7.5 | 2e-11 | 32/41 (HCT15, J82, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.99×** | +7.0 | 4e-10 | 33/47 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.97×** | +6.9 | 6e-10 | 39/47 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.01×** | +6.9 | 8e-10 | 24/33 (HepG2/C3A, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.90×** | +6.6 | 4e-09 | 39/48 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +5.3 | 9e-06 | 34/44 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +4.1 | 0.003 | 28/45 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.47×** | +3.9 | 0.005 | 24/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.50×** | +3.8 | 0.007 | 19/35 (Hs 766T, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.47×** | +3.8 | 0.008 | 21/42 (MIA PaCa-2, HS-578T, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.74×** | +3.8 | 0.008 | 22/44 (SW480, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +3.5 | 0.018 | 19/42 (SW480, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[EX229 (drug)]] 5 µM |  | **1.92×** | +3.5 | 0.019 | 19/46 (Hs 766T, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.41×** | +3.4 | 0.024 | 20/46 (NCI-H2030, C32, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.65×** | +3.4 | 0.024 | 18/48 (SW480, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.81×** | +3.2 | 0.045 | 16/47 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +3.1 | 0.050 | 20/47 (SNU-423, AsPC-1, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.56×** | +3.0 | 0.075 | 14/45 (LS 180, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.55×** | +3.0 | 0.083 | 13/47 (NCI-H460, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +2.9 | 0.083 | 17/48 (SNU-423, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10346.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (Panc 03.27 0.232×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (HS-578T 0.300×; ⚠ cell-cycle shift, explains ~54% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SW48 0.199×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.389×** | -5.1 | 2e-04 | 36/48 (Panc 03.27, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.478×** | -4.0 | 0.020 | 24/44 (C32, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.714×** | -3.5 | 0.090 | 19/47 (Hs 766T, COLO 205, …) | inconsistent across doses |  |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.713× | -3.4 | 0.11 | 22/47 (NCI-H2030, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10346. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 17.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +11.5) | — |
| [[HEC-1-A (line)]] | alt | 13.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.30× (z +12.9) | — |
| [[HS-578T (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.300× (z -9.1) ⚠ cell-cycle shift, explains ~54% of this change |
| [[KATO III (line)]] | alt | 34.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 35.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 57.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10346), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AXIN1]] | +0.67 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[FAM89A]] | +0.63 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[TSEN54]] | +0.60 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[TMEM120B]] | +0.58 | +0.35 / +0.68 | both halves | 1e-04 |  |
| [[KLF16]] | +0.58 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[SCLY]] | +0.57 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[LMBR1]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[PAM16]] | +0.56 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[ZBED4]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[CCNQ]] | +0.56 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[CSNK1G2]] | +0.56 | +0.33 / +0.62 | both halves | 1e-04 |  |
| [[DEXI]] | +0.56 | +0.37 / +0.62 | both halves | 9e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA5]] | -0.59 | -0.44 / -0.57 | both halves | 3e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[HMGN2]] | -0.58 | -0.37 / -0.62 | both halves | 8e-05 |  |
| [[SF3B1]] | -0.57 | -0.42 / -0.64 | both halves | 4e-05 |  |
| [[ZNF436]] | -0.53 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[PMPCB]] | -0.52 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[ZBED8]] | -0.52 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[CUL4B]] | -0.51 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[POGLUT3]] | -0.51 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[SRP9]] | -0.51 | -0.30 / -0.66 | both halves | 2e-04 |  |
| [[FBXO8]] | -0.51 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[IFT81]] | -0.51 | -0.39 / -0.52 | both halves | 6e-05 | pathway: Organelle biogenesis and maintenance |
| [[SPAG16]] | -0.50 | -0.42 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAPK14]] | B | MAPK14 activity raises ESRRA's level | compounds that target MAPK14: 2 of 2 lower it (PH-797804, Ralimetinib dimesylate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **-** arm (projection on the module's main direction -0.415). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-15.2, 3.4); signed map (-44.7, -1.6). **Vector** length 78.7, 18.4% of its response variance represented; |z| ≥ 3 in 815 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.3 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +8.9 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.6 | +3.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.2 | +3.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.9 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +2.7 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.0 | -5.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -2.6 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -1.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -4.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.8 | -1.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.5 | -1.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.5 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | estrogen related receptor alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:64,305,497-64,316,743 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ERR1, ERRalpha, NR3B1, ERRa; previously ESRL1 |
| Gene groups (HGNC) | Estrogen related receptors |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 9 pathways, smallest: Nuclear Receptor transcription pathway; Transcriptional activation of mitochondrial biogenesis; Regulation of RUNX2 expression and activity |
| Matched by | ensembl_id |

**Function**, from UniProt [P11474](https://www.uniprot.org/uniprotkb/P11474) (Steroid hormone receptor ERR1):

> Binds to an ERR-alpha response element (ERRE) containing a single consensus half-site, 5'-TNAAGGTCA-3'. Can bind to the medium-chain acyl coenzyme A dehydrogenase (MCAD) response element NRRE-1 and may act as an important regulator of MCAD promoter. Binds to the C1 region of the lactoferrin gene promoter. Requires dimerization and the coactivator, PGC-1A, for full activity. The ERRalpha/PGC1alpha complex is a regulator of energy metabolism. Induces the expression of PERM1 in the skeletal muscle.

**Summary**, from NCBI Gene [2101](https://www.ncbi.nlm.nih.gov/gene/2101):

> The protein encoded by this gene is a nuclear receptor that is most closely related to the estrogen receptor. This protein acts as a site-specific transcription factor and interacts with members of the PGC-1 family of transcription cofactors to regulate the expression of most genes involved in cellular energy production as well as in the process of mitochondrial biogenesis. A processed pseudogene of ESRRA is located on chromosome 13q12.1. [provided by RefSeq, Jun 2019]

**Accessions** — [HGNC:3471](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3471) · Entrez [2101](https://www.ncbi.nlm.nih.gov/gene/2101) · UniProt [P11474](https://www.uniprot.org/uniprotkb/P11474) · Ensembl [ENSG00000173153](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173153)

## Data

Gene col 10346: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10346); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10346, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10346]; `tensor/DDL_lfc|DDL_z.npy` [10346]; `embed/gene_vectors.npy` [10346]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10346 or target_col == 10346). Every well: [[ESRRA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ESRRA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
