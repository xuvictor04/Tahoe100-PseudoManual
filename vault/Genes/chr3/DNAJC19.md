---
symbol: "DNAJC19"
type: "gene"
col: 13027
ensembl_id: "ENSG00000205981"
name: "DnaJ heat shock protein family (Hsp40) member C19"
location: "3q26.33"
module: 17
arm: "+"
pooled_cpm: 14.31
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 9
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# DNAJC19

*DnaJ heat shock protein family (Hsp40) member C19* — 3q26.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.87× (z +9.5, q 2e-18, up in 36 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.38× (z +4.4, q 0.001, up in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 4.56×, SW480 3.95×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (Panc 03.27 4.26×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.472× (z -10.4, q 2e-22, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPY30]] (+0.77, fdr 1e-05), [[NDUFA12]] (+0.73, fdr 1e-05), [[METTL5]] (+0.72, fdr 2e-05); moves opposite to [[SLC9A5]] (-0.61, fdr 3e-05), [[CPEB2-DT]] (-0.58, fdr 7e-05), [[SECISBP2]] (-0.57, fdr 2e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ENPP4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13027.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 4.56×, SW480 3.95×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (Panc 03.27 4.26×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.87×** | +9.5 | 2e-18 | 36/38 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.53×** | +8.7 | 7e-16 | 22/23 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +5.5 | 8e-06 | 25/32 (NCI-H2030, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.61×** | +4.7 | 4e-04 | 24/42 (SW480, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +4.4 | 0.001 | 25/48 (HS-578T, SW 900, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.40× | +3.2 | 0.12 | 13/48 (KATO III, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13027.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.472×** | -10.4 | 2e-22 | 42/46 (A-427, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.535×** | -6.1 | 3e-07 | 34/47 (Panc 03.27, SW 1271, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.660×** | -5.7 | 2e-06 | 28/46 (MIA PaCa-2, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.347×** | -5.4 | 1e-05 | 30/43 (A-427, Hs 766T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.584×** | -5.2 | 2e-05 | 31/47 (PANC-1, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.640×** | -4.3 | 0.001 | 24/46 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.667×** | -3.9 | 0.007 | 21/47 (HT-29, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.677×** | -3.8 | 0.011 | 19/46 (SW480, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.691×** | -3.5 | 0.030 | 17/47 (A498, J82, …) | inconsistent across doses | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.730× | -3.0 | 0.13 | 16/47 (AN3 CA, SW480, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13027. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 36.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.56× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -14.6) |
| [[COLO 205 (line)]] | alt | 11.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -9.5) |
| [[A498 (line)]] | wt | 17.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -11.4) |
| [[HOP62 (line)]] | alt | 8.97 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 15.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 19.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 11.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 17.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 9.27 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 21.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +8.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 21.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -10.5) |
| [[SW480 (line)]] | alt | 16.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.95× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13027), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPY30]] | +0.77 | +0.50 / +0.77 | both halves | 1e-05 |  |
| [[NDUFA12]] | +0.73 | +0.54 / +0.66 | both halves | 1e-05 | STRING 495 |
| [[METTL5]] | +0.72 | +0.46 / +0.72 | both halves | 2e-05 | STRING 484 |
| [[COMMD2]] | +0.71 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[THYN1]] | +0.71 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[MRPS31P4]] | +0.68 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[SCRN2]] | +0.66 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[POLR2I]] | +0.66 | +0.32 / +0.66 | both halves | 2e-04 |  |
| [[MRPL21]] | +0.65 | +0.38 / +0.71 | both halves | 7e-05 | STRING 430 |
| [[FRG1CP]] | +0.65 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[MED30]] | +0.65 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[NDUFB10]] | +0.65 | +0.28 / +0.65 | both halves | 3e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A5]] | -0.61 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[CPEB2-DT]] | -0.58 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[SECISBP2]] | -0.57 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[LINC00393]] | -0.57 | -0.50 / -0.36 | both halves | 9e-05 |  |
| [[SAXO1]] | -0.56 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[GPR137]] | -0.56 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[LINC01135]] | -0.56 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[CCNT2-AS1]] | -0.56 | -0.48 / -0.37 | both halves | 9e-05 |  |
| [[MYH15]] | -0.56 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[DDX5]] | -0.55 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[MPDU1]] | -0.55 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[PCBP1-AS1]] | -0.55 | -0.39 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENPP4]] | B | ENPP4 activity raises DNAJC19's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 1.30× lower at baseline in the lines without ENPP4 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.731). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.4, -3.9); signed map (-22.9, -13.0). **Vector** length 54.3, 9.23% of its response variance represented; |z| ≥ 3 in 685 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.9 | +4.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +0.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +1.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | -0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.1 | +1.6 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.0 | +2.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.0 | +1.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.0 | -10.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -0.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.3 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -0.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.5 | -0.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -1.7 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member C19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.33 — chr3:180,983,697-180,989,774 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TIMM14, Tim14, Pam18 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins; TIM23 complex |
| Reactome | 2 pathways, smallest: Mitochondrial protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DA6](https://www.uniprot.org/uniprotkb/Q96DA6) (Mitochondrial import inner membrane translocase subunit TIM14):

> Mitochondrial co-chaperone which forms a complex with prohibitins to regulate cardiolipin remodeling (By similarity). May be a component of the PAM complex, a complex required for the translocation of transit peptide-containing proteins from the inner membrane into the mitochondrial matrix in an ATP-dependent manner. May act as a co-chaperone that stimulate the ATP-dependent activity (By similarity).

**Summary**, from NCBI Gene [131118](https://www.ncbi.nlm.nih.gov/gene/131118):

> The protein encoded by this gene is thought to be part of a complex involved in the ATP-dependent transport of transit peptide-containing proteins from the inner cell membrane to the mitochondrial matrix. Defects in this gene are a cause of 3-methylglutaconic aciduria type 5 (MGA5), also known as dilated cardiomyopathy with ataxia (DCMA). Alternative splicing of this gene results in multiple transcript variants. Related pseudogenes have been identified on chromosomes 1, 2, 6, 10, 14 and 19. …

**Accessions** — [HGNC:30528](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30528) · Entrez [131118](https://www.ncbi.nlm.nih.gov/gene/131118) · UniProt [Q96DA6](https://www.uniprot.org/uniprotkb/Q96DA6) · Ensembl [ENSG00000205981](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205981)

## Data

Gene col 13027: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13027); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13027, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13027]; `tensor/DDL_lfc|DDL_z.npy` [13027]; `embed/gene_vectors.npy` [13027]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13027 or target_col == 13027). Every well: [[DNAJC19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
