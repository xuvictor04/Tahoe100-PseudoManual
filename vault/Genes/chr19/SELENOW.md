---
symbol: "SELENOW"
type: "gene"
col: 10983
ensembl_id: "ENSG00000178980"
name: "selenoprotein W"
location: "19q13.33"
module: 1
arm: "-"
pooled_cpm: 35.49
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SELENOW

*selenoprotein W* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.08× (z +10.8, q 3e-24, up in 40 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.61× (z +6.2, q 7e-08, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.461× (z -3.9, q 0.045, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DALRD3]] (+0.60, fdr 1e-05), [[GTF2B]] (+0.60, fdr 7e-06), [[DPM1]] (+0.56, fdr 4e-05); moves opposite to [[ANKRD40]] (-0.61, fdr 1e-05), [[CHTOP]] (-0.61, fdr 3e-05), [[RUVBL1]] (-0.59, fdr 1e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10983.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.08×** | +10.8 | 3e-24 | 40/45 (HT-29, A498, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.28×** | +7.3 | 4e-11 | 38/41 (LoVo, HOP62, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.21×** | +7.3 | 4e-11 | 27/38 (KATO III, NCI-H460, …) | all doses, flat | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +6.2 | 7e-08 | 38/48 (NCI-H2030, AsPC-1, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +5.2 | 2e-05 | 39/46 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +4.2 | 0.002 | 27/48 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +3.8 | 0.013 | 2/48 (NCI-H661, SW 1271) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.047 | 26/48 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.094 | 18/48 (J82, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.39×** | +3.1 | 0.094 | 21/48 (LoVo, SW1417, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.38×** | +3.1 | 0.094 | 22/48 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.38×** | +3.1 | 0.097 | 22/48 (SW1417, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.39×** | +3.1 | 0.097 | 25/48 (MIA PaCa-2, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10983.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.461×** | -3.9 | 0.045 | 28/47 (SNU-1, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.675×** | -3.8 | 0.045 | 31/48 (HEC-1-A, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.482×** | -3.7 | 0.047 | 30/49 (SK-MEL-2, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.693×** | -3.5 | 0.062 | 28/47 (LOX-IMVI, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.728× | -3.1 | 0.24 | 25/48 (SW 1088, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.712× | -3.0 | 0.24 | 28/48 (J82, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10983. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 34.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A549 (line)]] | wt | 26.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[C32 (line)]] | wt | 38.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HOP62 (line)]] | alt | 27.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HT-29 (line)]] | alt | 77.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[KATO III (line)]] | alt | 70.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[LoVo (line)]] | wt | 24.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.67× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 37.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 14.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.26× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-427 (line)]] | wt | 34.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 34.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +10.6) | — |
| [[HCT15 (line)]] | alt | 37.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.63× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[Hs 766T (line)]] | wt | 41.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1792 (line)]] | alt | 23.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.17× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[PANC-1 (line)]] | alt | 24.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[RPMI-7951 (line)]] | alt | 44.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SW480 (line)]] | alt | 36.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 52.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 62.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10983), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DALRD3]] | +0.60 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[GTF2B]] | +0.60 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[DPM1]] | +0.56 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[LMBR1L]] | +0.56 | +0.36 / +0.58 | both halves | 9e-05 |  |
| [[ARPC3]] | +0.56 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[SDF2]] | +0.55 | +0.36 / +0.64 | both halves | 1e-04 |  |
| [[AAMDC]] | +0.55 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[WDR47]] | +0.55 | +0.52 / +0.39 | both halves | 5e-05 |  |
| [[POR]] | +0.54 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[RASA4B]] | +0.54 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[TOR1B]] | +0.54 | +0.38 / +0.54 | both halves | 7e-05 |  |
| [[SIRT6]] | +0.54 | +0.46 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD40]] | -0.61 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[CHTOP]] | -0.61 | -0.43 / -0.65 | both halves | 3e-05 |  |
| [[RUVBL1]] | -0.59 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[ATIC]] | -0.59 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[HNRNPF]] | -0.58 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[LTV1]] | -0.57 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[ANAPC7]] | -0.57 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[COG8]] | -0.57 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[PFAS]] | -0.57 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[RIOX2]] | -0.57 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[ZNF507]] | -0.57 | -0.40 / -0.58 | both halves | 4e-05 |  |
| [[NOP14]] | -0.56 | -0.35 / -0.59 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.572). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-20.5, -35.6); signed map (-16.9, 16.2). **Vector** length 66.4, 16.0% of its response variance represented; |z| ≥ 3 in 648 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.4 | +3.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +4.2 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.8 | +0.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.8 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.4 | +0.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +2.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -0.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.0 | +0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -0.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -2.5 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | selenoprotein W |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:47,778,677-47,784,686 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SELW; previously SEPW1 |
| Gene groups (HGNC) | Selenoproteins |
| Hallmark sets | UV_RESPONSE_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [P63302](https://www.uniprot.org/uniprotkb/P63302) (Selenoprotein W):

> Plays a role as a glutathione (GSH)-dependent antioxidant. May be involved in a redox-related process. May play a role in the myopathies of selenium deficiency (By similarity).

**Summary**, from NCBI Gene [6415](https://www.ncbi.nlm.nih.gov/gene/6415):

> This gene encodes a selenoprotein containing a selenocysteine (Sec) residue, which is encoded by the UGA codon that normally signals translation termination. The 3' UTRs of selenoprotein mRNAs contain a conserved stem-loop structure, the Sec insertion sequence (SECIS) element that is necessary for the recognition of UGA as a Sec codon rather than as a stop signal. This protein is highly expressed in skeletal muscle, heart and brain. It belongs to the SelWTH family, which possesses a …

**Accessions** — [HGNC:10752](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10752) · Entrez [6415](https://www.ncbi.nlm.nih.gov/gene/6415) · UniProt [P63302](https://www.uniprot.org/uniprotkb/P63302) · Ensembl [ENSG00000178980](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178980)

## Data

Gene col 10983: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10983); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10983, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10983]; `tensor/DDL_lfc|DDL_z.npy` [10983]; `embed/gene_vectors.npy` [10983]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10983 or target_col == 10983). Every well: [[SELENOW — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SELENOW.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
