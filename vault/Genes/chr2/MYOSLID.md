---
symbol: "MYOSLID"
type: "gene"
col: 13712
ensembl_id: "ENSG00000229647"
name: "myocardin-induced smooth muscle lncRNA, inducer of differentiation"
location: "2q33.3"
module: 54
arm: "-"
pooled_cpm: 3.58
n_lines_expressing: 39
n_dd_up: 12
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# MYOSLID

*myocardin-induced smooth muscle lncRNA, inducer of differentiation* — 2q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 5.17× (z +12.8, q 6e-35, up in 7 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.45× (z +10.7, q 2e-24, up in 18 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.562× (z -4.8, q 7e-04, down in 17 of 34 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.627× (z -3.9, q 0.013, down in 6 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KRT8P12]] (+0.64, fdr 1e-05), [[UBE2D3-AS1]] (+0.63, fdr 1e-05), [[PRECSIT]] (+0.62, fdr 1e-05); moves opposite to [[DPY30]] (-0.60, fdr 2e-05), [[MALSU1]] (-0.60, fdr 3e-05), [[SDHAF1]] (-0.59, fdr 1e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DOCK2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LINC02966]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13712.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.17×** | +12.8 | 6e-35 | 7/8 (HS-578T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.56×** | +10.7 | 2e-24 | 12/14 (HS-578T, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.45×** | +10.7 | 2e-24 | 18/26 (HS-578T, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +9.0 | 4e-17 | 17/26 (A498, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.47×** | +7.3 | 2e-11 | 3/7 (HS-578T, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.92×** | +5.5 | 3e-06 | 12/30 (A-172, LoVo, …) | rises with dose | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.63×** | +4.2 | 0.003 | 7/33 (PANC-1, SNU-423, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +4.0 | 0.005 | 10/27 (HS-578T, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.24×** | +3.6 | 0.022 | 1/7 (A498) | top dose only | noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.48×** | +3.4 | 0.045 | 4/24 (RPMI-7951, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.47×** | +3.3 | 0.054 | 4/30 (LOX-IMVI, H4, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +3.1 | 0.090 | 5/29 (A-172, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13712.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.562×** | -4.8 | 7e-04 | 17/34 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.588×** | -4.2 | 0.008 | 13/33 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.616×** | -4.1 | 0.009 | 9/34 (C-33 A, SHP-77, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.627×** | -3.9 | 0.013 | 6/33 (HOP62, LOX-IMVI, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | **0.723×** | -3.8 | 0.014 | 10/31 (C-33 A, SHP-77, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **0.642×** | -3.7 | 0.019 | 8/33 (HCT15, CFPAC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.645×** | -3.7 | 0.019 | 12/33 (LOX-IMVI, J82, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.659×** | -3.3 | 0.066 | 9/28 (SNU-423, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13712. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 5.73 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +12.4) | — |
| [[A498 (line)]] | wt | 1.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.65× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 1.81 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +10.3) | — |
| [[A-172 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.769 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.511 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.533 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.436 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.334 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.492 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.434 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.695 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.460 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.816 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13712), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRT8P12]] | +0.64 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[UBE2D3-AS1]] | +0.63 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[PRECSIT]] | +0.62 | +0.56 / +0.54 | both halves | 1e-05 | same gene group |
| [[FSIP1]] | +0.61 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[LINC00702]] | +0.61 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[CCDC200]] | +0.60 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[ITPR2-AS1]] | +0.59 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[MAPRE1]] | +0.59 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[SSPN]] | +0.58 | +0.62 / +0.39 | both halves | 5e-05 |  |
| [[PIGV]] | +0.58 | +0.56 / +0.25 | both halves | 4e-04 |  |
| [[WAKMAR2]] | +0.57 | +0.50 / +0.41 | both halves | 4e-05 | same gene group |
| [[LPXN]] | +0.57 | +0.50 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPY30]] | -0.60 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[MALSU1]] | -0.60 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[SDHAF1]] | -0.59 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[KLHL8]] | -0.59 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[CAPN7]] | -0.58 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[CDK5RAP1]] | -0.57 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[KLHDC10]] | -0.57 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[SDHAP2]] | -0.56 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[LCMT1]] | -0.56 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[PRKRA]] | -0.55 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[SMYD4]] | -0.55 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[LSM7]] | -0.55 | -0.49 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DOCK2]] | B | DOCK2 activity raises MYOSLID's level | lines that do not express DOCK2 (21) vs lines expressing it (29) | 2.29× lower at baseline in the lines without DOCK2 | 0.059 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, KCTD16; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises MYOSLID's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02966]] | B | MYOSLID activity lowers LINC02966's level | lines that do not express MYOSLID (11) vs lines expressing it (39) | 1.30× higher at baseline in the lines without MYOSLID | 0.083 | ⚠ within organs, on part of the lines; also absent: KLF7, CTSF, LINC01725 |

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (15.9, 12.9); signed map (24.4, 5.0). **Vector** length 56.2, 9.75% of its response variance represented; |z| ≥ 3 in 838 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +12.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +10.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.1 | -0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.1 | +4.2 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +0.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -1.8 | -3.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -1.7 | +0.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -3.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -0.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.1 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | myocardin-induced smooth muscle lncRNA, inducer of differentiation |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q33.3 — chr2:207,166,120-207,248,668 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51821](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51821) · Entrez [105373853](https://www.ncbi.nlm.nih.gov/gene/105373853) · Ensembl [ENSG00000229647](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229647)

## Data

Gene col 13712: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13712); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13712, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13712]; `tensor/DDL_lfc|DDL_z.npy` [13712]; `embed/gene_vectors.npy` [13712]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13712 or target_col == 13712). Every well: [[MYOSLID — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYOSLID.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
