---
symbol: "CSTF2T"
type: "gene"
col: 10841
ensembl_id: "ENSG00000177613"
name: "cleavage stimulation factor subunit 2 tau variant"
location: "10q21.1"
module: 16
arm: "+"
pooled_cpm: 7.75
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 10
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# CSTF2T

*cleavage stimulation factor subunit 2 tau variant* — 10q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 2.97× (z +11.7, q 1e-28, up in 40 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.664× (z -4.6, q 0.003, down in 19 of 45 measured lines) ⚠ unreliable plate only; position not correctable. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.775× (z -4.0, q 0.011, down in 19 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS18A]] (+0.79, fdr 7e-06), [[ZNF620]] (+0.79, fdr 7e-06), [[ZNF268]] (+0.78, fdr 7e-06); moves opposite to [[RAB6A]] (-0.71, fdr 7e-06), [[GNRH1]] (-0.69, fdr 7e-06), [[SMG1P5]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[STARD13]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10841.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **2.97×** | +11.7 | 1e-28 | 40/44 (SNU-423, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.94×** | +10.5 | 4e-23 | 30/40 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.46×** | +10.0 | 3e-21 | 40/44 (A-427, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.21×** | +8.8 | 2e-16 | 31/41 (SW 900, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.19×** | +8.1 | 8e-14 | 18/24 (LoVo, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.71×** | +7.6 | 2e-12 | 36/45 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.84×** | +6.4 | 1e-08 | 27/45 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.69×** | +5.9 | 3e-07 | 23/45 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.66×** | +5.6 | 1e-06 | 23/45 (LoVo, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.71×** | +5.5 | 2e-06 | 23/41 (RKO, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.2 | 9e-06 | 21/46 (HOP62, A498, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.42×** | +3.9 | 0.005 | 9/45 (LOX-IMVI, BT-474, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.93×** | +3.8 | 0.005 | 14/41 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +3.2 | 0.048 | 10/36 (SW 900, NCI-H1573, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here); position effect removed |
| [[Busulfan (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.049 | 7/46 (SNU-1, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.098 | 5/45 (KATO III, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10841.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.664×** | -4.6 | 0.003 | 19/45 (NCI-H1573, HEC-1-A, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.673×** | -4.2 | 0.006 | 15/38 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.775×** | -4.0 | 0.011 | 19/45 (NCI-H1573, H4, …) | rises with dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.711×** | -3.8 | 0.019 | 16/46 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | **0.713×** | -3.8 | 0.019 | 12/45 (NCI-H2347, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.709×** | -3.7 | 0.022 | 5/15 (HEC-1-A, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.742×** | -3.3 | 0.069 | 17/42 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tazarotene (drug)]] 0.05 µM |  | **0.744×** | -3.3 | 0.069 | 9/45 (SNU-423, AN3 CA, …) | inconsistent across doses |  |
| [[Tetracycline (hydrochloride) (drug)]] 0.5 µM |  | **0.748×** | -3.2 | 0.076 | 11/45 (NCI-H1573, H4, …) | inconsistent across doses | position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.820×** | -3.1 | 0.096 | 12/45 (NCI-H2347, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10841. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 7.25 | 0 | 2 | — | [[Sinomenine (drug)]] 0.05 µM 0.0618× (z -10.7) |
| [[A-427 (line)]] | wt | 13.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0988× (z -12.3) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 5.63 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0754× (z -10.8) |
| [[COLO 205 (line)]] | alt | 8.59 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0603× (z -8.9) |
| [[LoVo (line)]] | wt | 9.18 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0689× (z -15.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 5.65 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.05 µM 0.0781× (z -9.6) |
| [[SHP-77 (line)]] | alt | 9.64 | 0 | 1 | — | [[Pemigatinib (drug)]] 0.05 µM 0.118× (z -8.7) |
| [[A-172 (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10841), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS18A]] | +0.79 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[ZNF620]] | +0.79 | +0.80 / +0.75 | both halves | 7e-06 |  |
| [[ZNF268]] | +0.78 | +0.81 / +0.74 | both halves | 7e-06 |  |
| [[PABIR1]] | +0.76 | +0.76 / +0.78 | both halves | 7e-06 |  |
| [[RTL6]] | +0.76 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[ZBTB6]] | +0.75 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[DDX20]] | +0.75 | +0.76 / +0.71 | both halves | 7e-06 | STRING 429 |
| [[ZNF629]] | +0.74 | +0.80 / +0.64 | both halves | 7e-06 |  |
| [[ZNF502]] | +0.74 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[C7orf25]] | +0.74 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[ZNF776]] | +0.73 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[DCLRE1A]] | +0.73 | +0.73 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB6A]] | -0.71 | -0.73 / -0.68 | both halves | 7e-06 |  |
| [[GNRH1]] | -0.69 | -0.68 / -0.62 | both halves | 7e-06 |  |
| [[SMG1P5]] | -0.68 | -0.72 / -0.63 | both halves | 7e-06 |  |
| [[SLC37A3]] | -0.68 | -0.73 / -0.60 | both halves | 7e-06 |  |
| [[CBFA2T2]] | -0.67 | -0.70 / -0.69 | both halves | 7e-06 |  |
| [[TMEM50B]] | -0.66 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[GET1-SH3BGR]] | -0.65 | -0.57 / -0.70 | both halves | 9e-06 |  |
| [[SRP54-AS1]] | -0.65 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[SGK3]] | -0.64 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[SDHAP4-1]] | -0.64 | -0.64 / -0.64 | both halves | 7e-06 |  |
| [[PIK3C2A]] | -0.64 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[MAX]] | -0.64 | -0.58 / -0.63 | both halves | 8e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD13]] | B | STARD13 activity raises CSTF2T's level | lines that do not express STARD13 (7) vs lines expressing it (43) | 1.35× lower at baseline in the lines without STARD13 | 0.010 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.872). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-33.2, 12.0); signed map (1.4, -29.4). **Vector** length 74.9, 12.8% of its response variance represented; |z| ≥ 3 in 1,004 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.1 | +10.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +11.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.6 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +8.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.7 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +5.2 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.4 | +1.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.2 | -4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.2 | -0.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.9 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -4.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -2.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -1.1 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | cleavage stimulation factor subunit 2 tau variant |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.1 — chr10:51,695,486-51,699,595 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434C1013, KIAA0689, CstF-64T, tauCstF-64 |
| Gene groups (HGNC) | RNA binding motif containing; Cleavage stimulation factor subunits |
| Reactome | 10 pathways, smallest: Processing of Intronless Pre-mRNAs; Processing of Capped Intronless Pre-mRNA; RNA Polymerase II Transcription Termination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0L4](https://www.uniprot.org/uniprotkb/Q9H0L4) (Cleavage stimulation factor subunit 2 tau variant):

> May play a significant role in AAUAAA-independent mRNA polyadenylation in germ cells. Directly involved in the binding to pre-mRNAs (By similarity).

**Summary**, from NCBI Gene [23283](https://www.ncbi.nlm.nih.gov/gene/23283):

> Enables RNA binding activity. Predicted to be involved in mRNA 3'-end processing. Predicted to be located in nucleoplasm. Predicted to be part of mRNA cleavage and polyadenylation specificity factor complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17086](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17086) · Entrez [23283](https://www.ncbi.nlm.nih.gov/gene/23283) · UniProt [Q9H0L4](https://www.uniprot.org/uniprotkb/Q9H0L4) · Ensembl [ENSG00000177613](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177613)

## Data

Gene col 10841: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10841); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10841, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10841]; `tensor/DDL_lfc|DDL_z.npy` [10841]; `embed/gene_vectors.npy` [10841]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10841 or target_col == 10841). Every well: [[CSTF2T — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSTF2T.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
