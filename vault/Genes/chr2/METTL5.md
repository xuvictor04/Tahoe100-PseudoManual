---
symbol: "METTL5"
type: "gene"
col: 6165
ensembl_id: "ENSG00000138382"
name: "methyltransferase 5, N6-adenosine"
location: "2q31.1"
module: 17
arm: "+"
pooled_cpm: 30.52
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# METTL5

*methyltransferase 5, N6-adenosine* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.92× (z +10.1, q 3e-21, up in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.50× (z +3.9, q 0.013, up in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H460 5.10×, HOP62 6.43×, SW 900 8.81×, A498 4.01×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 4.37×, HOP62 6.00×, A498 4.17×, LoVo 4.45×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.611× (z -6.6, q 3e-08, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJC19]] (+0.72, fdr 2e-05), [[COMMD2]] (+0.72, fdr 1e-05), [[ESD]] (+0.68, fdr 3e-05); moves opposite to [[SRSF5]] (-0.62, fdr 2e-05), [[RBM15-AS1]] (-0.60, fdr 1e-04), [[HCFC1]] (-0.59, fdr 2e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[STING1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6165.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H460 5.10×, HOP62 6.43×, SW 900 8.81×, A498 4.01×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 4.37×, HOP62 6.00×, A498 4.17×, LoVo 4.45×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.92×** | +10.1 | 3e-21 | 42/44 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.94×** | +9.8 | 3e-20 | 31/36 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +5.4 | 1e-05 | 31/41 (SW 900, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.57×** | +4.3 | 0.002 | 28/46 (SW1417, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +3.9 | 0.013 | 32/48 (SW480, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6165.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.611×** | -6.6 | 3e-08 | 35/47 (NCI-H2030, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.699×** | -4.8 | 6e-04 | 31/47 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.675×** | -3.7 | 0.041 | 27/48 (NCI-H2030, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.684×** | -3.6 | 0.051 | 25/48 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **0.505×** | -3.4 | 0.087 | 27/47 (RKO, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6165. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 37.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +10.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 23.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.43× (z +11.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 16.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.42× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 28.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -11.8) |
| [[SW480 (line)]] | alt | 41.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.37× (z +11.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 39.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.218× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 25.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 32.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.45× (z +9.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 34.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.255× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 44.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -9.4) |
| [[PANC-1 (line)]] | alt | 38.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +9.4) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 33.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -9.2) |
| [[SNU-423 (line)]] | alt | 21.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 18.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.81× (z +10.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6165), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC19]] | +0.72 | +0.46 / +0.72 | both halves | 2e-05 | STRING 484 |
| [[COMMD2]] | +0.72 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[ESD]] | +0.68 | +0.46 / +0.71 | both halves | 3e-05 |  |
| [[FAM241B]] | +0.65 | +0.41 / +0.70 | both halves | 4e-05 |  |
| [[IRAK1BP1]] | +0.64 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[NDUFA12]] | +0.64 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[POLR2I]] | +0.64 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[MRPL21]] | +0.64 | +0.39 / +0.67 | both halves | 5e-05 |  |
| [[NOL7]] ⚠ | +0.63 | +0.47 / +0.65 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MNAT1]] | +0.63 | +0.37 / +0.61 | both halves | 8e-05 |  |
| [[LYPLAL1]] | +0.63 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[NDUFA8]] | +0.62 | +0.33 / +0.64 | both halves | 1e-04 |  |
| [[ZNF30]] | +0.62 | +0.46 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF5]] | -0.62 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[RBM15-AS1]] | -0.60 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[HCFC1]] | -0.59 | -0.31 / -0.63 | both halves | 2e-04 |  |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | -0.59 | -0.27 / -0.55 | both halves | 3e-04 |  |
| [[CFL1]] | -0.57 | -0.35 / -0.64 | both halves | 1e-04 |  |
| [[STARD4-AS1]] | -0.57 | -0.23 / -0.51 | both halves | 5e-04 |  |
| [[PIPOX]] | -0.56 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[GUCD1]] | -0.56 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[ATXN1L]] | -0.56 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[TRPV1]] | -0.55 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[CCNT2-AS1]] | -0.53 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[XNDC1N]] | -0.53 | -0.22 / -0.56 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STING1]] | B | STING1 activity lowers METTL5's level | lines that do not express STING1 (17) vs lines expressing it (33) | 1.21× higher at baseline in the lines without STING1 | 0.071 | ⚠ within organs, on part of the lines; also absent: MANCR, SATB1, NLRP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.627). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.6, -3.7); signed map (-22.6, -13.3). **Vector** length 69.0, 17.9% of its response variance represented; |z| ≥ 3 in 537 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.8 | +3.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +1.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.7 | +1.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | -0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.3 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +1.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.6 | -6.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -2.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -2.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -3.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.2 | +0.8 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.0 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | methyltransferase 5, N6-adenosine |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:169,810,081-169,824,931 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC133 |
| Gene groups (HGNC) | 7BS N6-adenosine DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRN9](https://www.uniprot.org/uniprotkb/Q9NRN9) (rRNA N(6)-adenosine-methyltransferase METTL5):

> Catalytic subunit of a heterodimer with TRMT112, which specifically methylates the 6th position of adenine in position 1832 of 18S rRNA. N6-methylation of adenine(1832) in 18S rRNA resides in the decoding center of 18S rRNA and is required for translation and embryonic stem cells (ESCs) pluripotency and differentiation.

**Summary**, from NCBI Gene [29081](https://www.ncbi.nlm.nih.gov/gene/29081):

> Enables S-adenosyl-L-methionine binding activity and rRNA (adenine-N6-)-methyltransferase activity. Involved in positive regulation of translation and rRNA methylation. Located in several cellular components, including fibrillar center; postsynapse; and presynapse. Implicated in autosomal recessive intellectual developmental disorder 72. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25006](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25006) · Entrez [29081](https://www.ncbi.nlm.nih.gov/gene/29081) · UniProt [Q9NRN9](https://www.uniprot.org/uniprotkb/Q9NRN9) · Ensembl [ENSG00000138382](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138382)

## Data

Gene col 6165: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6165); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6165, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6165]; `tensor/DDL_lfc|DDL_z.npy` [6165]; `embed/gene_vectors.npy` [6165]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6165 or target_col == 6165). Every well: [[METTL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METTL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
