---
symbol: "EBAG9"
type: "gene"
col: 7211
ensembl_id: "ENSG00000147654"
name: "estrogen receptor binding site associated antigen 9"
location: "8q23.2"
module: 12
arm: "+"
pooled_cpm: 22.96
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# EBAG9

*estrogen receptor binding site associated antigen 9* — 8q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.77× (z +7.3, q 1e-10, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.439× (z -10.5, q 5e-23, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEX12]] (+0.80, fdr 7e-06), [[RP9]] (+0.80, fdr 7e-06), [[PPP4R2]] (+0.80, fdr 7e-06); moves opposite to [[MBOAT7]] (-0.67, fdr 7e-06), [[HCFC1]] (-0.63, fdr 7e-06), [[UFD1]] (-0.62, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7211.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.77×** | +7.3 | 1e-10 | 39/48 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.78×** | +7.1 | 3e-10 | 34/47 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.53×** | +5.5 | 9e-06 | 32/46 (A-427, NCI-H2347, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +5.0 | 8e-05 | 24/48 (J82, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.31×** | +4.9 | 1e-04 | 23/47 (RKO, A549, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.46×** | +4.9 | 1e-04 | 25/43 (HOP62, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +4.8 | 1e-04 | 26/48 (NCI-H2347, LoVo, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.34×** | +3.5 | 0.034 | 20/47 (A549, HS-578T, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.28× | +3.1 | 0.12 | 19/45 (HOP62, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | 1.27× | +3.1 | 0.12 | 19/42 (KATO III, LoVo, …) | rises with dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7211.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.439×** | -10.5 | 5e-23 | 42/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.460×** | -9.9 | 1e-20 | 41/46 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.498×** | -8.9 | 1e-16 | 38/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.514×** | -8.5 | 3e-15 | 44/48 (BT-474, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.575×** | -7.1 | 2e-10 | 36/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.656×** | -5.4 | 8e-06 | 26/47 (C32, SHP-77, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.693×** | -4.7 | 2e-04 | 21/47 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.709×** | -4.4 | 8e-04 | 25/48 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.725×** | -3.8 | 0.008 | 21/48 (HEC-1-A, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7211. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 23.4 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.183× (z -10.4) |
| [[PANC-1 (line)]] | alt | 23.9 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.268× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.284× (z -11.0) |
| [[C32 (line)]] | wt | 25.7 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -9.2) ⚠ cell-cycle shift, explains ~23% of this change |
| [[HepG2_C3A (line)]] | wt | 23.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.171× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.180× (z -8.9) |
| [[KATO III (line)]] | alt | 33.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.240× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.242× (z -10.7) |
| [[SNU-423 (line)]] | alt | 16.6 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0721× (z -14.7) ⚠ cell-cycle shift, explains ~23% of this change |
| [[SW480 (line)]] | alt | 22.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.320× (z -9.7) |
| [[A-427 (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -9.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[H4 (line)]] | wt | 14.1 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM 0.190× (z -9.2) |
| [[HCT15 (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -10.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 29.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.333× (z -9.1) |
| [[HOP62 (line)]] | alt | 21.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.306× (z -8.8) |
| [[HS-578T (line)]] | alt | 31.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.279× (z -9.8) |
| [[LoVo (line)]] | wt | 22.2 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.56× (z +8.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[LS 180 (line)]] | wt | 28.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.276× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 19.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.202× (z -9.3) |
| [[SHP-77 (line)]] | alt | 34.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SW1417 (line)]] | alt | 30.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.235× (z -10.8) |
| [[A-172 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7211), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX12]] | +0.80 | +0.82 / +0.75 | both halves | 7e-06 |  |
| [[RP9]] | +0.80 | +0.85 / +0.78 | both halves | 7e-06 |  |
| [[PPP4R2]] | +0.80 | +0.76 / +0.84 | both halves | 7e-06 |  |
| [[PHAX]] | +0.78 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[ASNSD1]] | +0.78 | +0.79 / +0.72 | both halves | 7e-06 |  |
| [[AGGF1]] | +0.78 | +0.79 / +0.73 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.77 | +0.82 / +0.75 | both halves | 7e-06 |  |
| [[SUPT20H]] | +0.77 | +0.80 / +0.68 | both halves | 7e-06 |  |
| [[MRPS31]] | +0.76 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[RIOK2]] | +0.76 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[SNHG11]] | +0.76 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[GEMIN2]] | +0.75 | +0.70 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBOAT7]] | -0.67 | -0.73 / -0.62 | both halves | 7e-06 |  |
| [[HCFC1]] | -0.63 | -0.69 / -0.64 | both halves | 7e-06 |  |
| [[UFD1]] | -0.62 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[ZNF731P]] | -0.61 | -0.63 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises EBAG9's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SDC1]] | B | SDC1 activity raises EBAG9's level | lines that do not express SDC1 (8) vs lines expressing it (42) | 1.24× lower at baseline in the lines without SDC1 | 0.087 | ⚠ within organs, on part of the lines; also absent: CARD10, MFNG, BMAL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.795). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-31.7, 3.2); signed map (2.1, -20.4). **Vector** length 95.4, 23.3% of its response variance represented; |z| ≥ 3 in 792 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.8 | +7.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +7.8 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +7.7 | +5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +5.9 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.9 | +4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +1.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -6.1 | -8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.4 | -8.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.3 | -10.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.1 | -9.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -0.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | estrogen receptor binding site associated antigen 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q23.2 — chr8:109,539,711-109,570,072 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EB9, RCAS1, PDAF |
| Reactome | 3 pathways, smallest: Estrogen-dependent gene expression; ESR-mediated signaling; Signaling by Nuclear Receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [O00559](https://www.uniprot.org/uniprotkb/O00559) (Receptor-binding cancer antigen expressed on SiSo cells):

> May participate in suppression of cell proliferation and induces apoptotic cell death through activation of interleukin-1-beta converting enzyme (ICE)-like proteases.

**Summary**, from NCBI Gene [9166](https://www.ncbi.nlm.nih.gov/gene/9166):

> This gene was identified as an estrogen-responsive gene. Regulation of transcription by estrogen is mediated by estrogen receptor, which binds to the estrogen-responsive element found in the 5'-flanking region of this gene. The encoded protein is a tumor-associated antigen that is expressed at high frequency in a variety of cancers. Alternate splicing results in multiple transcript variants. A pseudogene of this gene has been defined on chromosome 10. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:3123](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3123) · Entrez [9166](https://www.ncbi.nlm.nih.gov/gene/9166) · UniProt [O00559](https://www.uniprot.org/uniprotkb/O00559) · Ensembl [ENSG00000147654](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147654)

## Data

Gene col 7211: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7211); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7211, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7211]; `tensor/DDL_lfc|DDL_z.npy` [7211]; `embed/gene_vectors.npy` [7211]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7211 or target_col == 7211). Every well: [[EBAG9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EBAG9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
