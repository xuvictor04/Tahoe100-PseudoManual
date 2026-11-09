---
symbol: "SORD"
type: "gene"
col: 6380
ensembl_id: "ENSG00000140263"
name: "sorbitol dehydrogenase"
location: "15q21.1"
module: 18
arm: "+"
pooled_cpm: 10.63
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# SORD

*sorbitol dehydrogenase* — 15q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.80× (z +7.9, q 2e-12, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.445× (z -10.4, q 1e-22, down in 29 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAT2]] (+0.71, fdr 7e-06), [[EEF1E1]] (+0.69, fdr 7e-06), [[EBPL]] (+0.68, fdr 7e-06); moves opposite to [[SMIM14]] (-0.63, fdr 7e-06), [[SHOC2]] (-0.61, fdr 1e-05), [[ZRANB1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MCOLN2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6380.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.80×** | +7.9 | 2e-12 | 30/47 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.69×** | +6.6 | 9e-09 | 28/45 (NCI-H460, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.59×** | +6.2 | 1e-07 | 25/47 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.52×** | +5.4 | 1e-05 | 21/40 (NCI-H2030, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +4.9 | 9e-05 | 18/47 (COLO 205, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.29×** | +4.8 | 1e-04 | 15/48 (H4, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +4.1 | 0.003 | 12/22 (HT-29, LoVo, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.72×** | +3.8 | 0.010 | 12/43 (A498, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.018 | 17/47 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Afatinib (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.029 | 13/48 (SNU-1, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.63×** | +3.4 | 0.032 | 9/42 (SK-MEL-2, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.58×** | +3.2 | 0.062 | 4/45 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.58×** | +3.2 | 0.062 | 5/34 (HOP62, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.1 | 0.077 | 3/18 (NCI-H2347, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +3.0 | 0.087 | 7/18 (CFPAC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[EX229 (drug)]] 0.05 µM |  | **1.27×** | +3.0 | 0.093 | 6/46 (NCI-H460, RPMI-7951, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.093 | 5/47 (AsPC-1, PANC-1, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.53×** | +3.0 | 0.093 | 5/40 (HEC-1-A, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6380.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.445×** | -10.4 | 1e-22 | 29/46 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.601×** | -9.6 | 2e-19 | 33/46 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.861× | -6.8 | 3e-09 | 23/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.664×** | -5.5 | 6e-06 | 24/43 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.694×** | -4.9 | 1e-04 | 19/46 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.592×** | -3.7 | 0.023 | 16/46 (NCI-H460, hTERT-HPNE, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.776×** | -3.4 | 0.055 | 15/46 (SW48, J82, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.781×** | -3.3 | 0.067 | 13/47 (NCI-H1792, RKO, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6380. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 20.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -12.1) ⚠ cell-cycle shift, explains ~45% of this change |
| [[RKO (line)]] | wt | 20.7 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.190× (z -8.9) |
| [[A549 (line)]] | wt | 6.24 | 0 | 1 | — | [[ERK5-IN-2 (drug)]] 0.5 µM 0.0518× (z -8.6) |
| [[H4 (line)]] | wt | 13.8 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.105× (z -8.5) |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0984× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[J82 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.164× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[LOX-IMVI (line)]] | wt | 14.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -11.5) ⚠ cell-cycle shift, explains ~45% of this change |
| [[LS 180 (line)]] | wt | 10.4 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0782× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 5.02 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.126× (z -9.4) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 13.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.260× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -9.5) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SW48 (line)]] | wt | 24.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6380), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAT2]] | +0.71 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[EEF1E1]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[EBPL]] | +0.68 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[GARNL3]] | +0.67 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[SFXN4]] | +0.67 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[POP1]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[TUBGCP4]] | +0.67 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[SLC19A1]] | +0.66 | +0.61 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[DFFB]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[POLR3G]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[DTD2]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[CHRNA5]] | +0.64 | +0.58 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM14]] | -0.63 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[SHOC2]] | -0.61 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[ZRANB1]] | -0.61 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[AVIL]] | -0.60 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[TNRC6C]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[RSF1]] | -0.59 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[SIX5]] | -0.59 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[MTHFR]] | -0.58 | -0.63 / -0.55 | both halves | 1e-05 | same gene group |
| [[METTL25B]] | -0.58 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[PPP1R12A]] | -0.57 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[NBR1]] | -0.57 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[SGO1-AS1]] | -0.57 | -0.57 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCOLN2]] | B | MCOLN2 activity raises SORD's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.22× lower at baseline in the lines without MCOLN2 | 0.067 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.713). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-9.3, -38.3); signed map (-6.8, -54.6). **Vector** length 88.8, 17.6% of its response variance represented; |z| ≥ 3 in 857 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | +5.6 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.4 | +7.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.4 | +6.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.1 | +6.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | +4.3 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.8 | +4.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.0 | +3.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.6 | +2.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.5 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.9 | -10.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -4.3 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.7 | -5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -4.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -6.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | +0.3 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | sorbitol dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.1 — chr15:45,023,147-45,077,185 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SDH, XDH |
| Gene groups (HGNC) | Oxidoreductases |
| Hallmark sets | MYC_TARGETS_V2, ANDROGEN_RESPONSE, ESTROGEN_RESPONSE_LATE, MTORC1_SIGNALING |
| Reactome | 3 pathways, smallest: Fructose metabolism; Formation of xylulose-5-phosphate; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00796](https://www.uniprot.org/uniprotkb/Q00796) (Sorbitol dehydrogenase):

> Polyol dehydrogenase that catalyzes the reversible NAD(+)-dependent oxidation of various sugar alcohols. Is mostly active with D-sorbitol (D-glucitol), L-threitol, xylitol and ribitol as substrates, leading to the C2-oxidized products D-fructose, L-erythrulose, D-xylulose, and D-ribulose, respectively. Is a key enzyme in the polyol pathway that interconverts glucose and fructose via sorbitol, which constitutes an important alternate route for glucose metabolism. The polyol pathway is believed …

**Summary**, from NCBI Gene [6652](https://www.ncbi.nlm.nih.gov/gene/6652):

> Sorbitol dehydrogenase (SORD; EC 1.1.1.14) catalyzes the interconversion of polyols and their corresponding ketoses, and together with aldose reductase (ALDR1; MIM 103880), makes up the sorbitol pathway that is believed to play an important role in the development of diabetic complications (summarized by Carr and Markham, 1995 [PubMed 8535074]). The first reaction of the pathway (also called the polyol pathway) is the reduction of glucose to sorbitol by ALDR1 with NADPH as the cofactor. SORD …

**Accessions** — [HGNC:11184](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11184) · Entrez [6652](https://www.ncbi.nlm.nih.gov/gene/6652) · UniProt [Q00796](https://www.uniprot.org/uniprotkb/Q00796) · Ensembl [ENSG00000140263](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140263)

## Data

Gene col 6380: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6380); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6380, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6380]; `tensor/DDL_lfc|DDL_z.npy` [6380]; `embed/gene_vectors.npy` [6380]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6380 or target_col == 6380). Every well: [[SORD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SORD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
