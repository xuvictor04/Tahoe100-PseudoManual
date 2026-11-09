---
symbol: "FNBP1P1"
type: "gene"
col: 15065
ensembl_id: "ENSG00000257800"
name: "formin binding protein 1 pseudogene 1"
location: "2p13.1"
module: 16
arm: "+"
pooled_cpm: 4.07
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# FNBP1P1

*formin binding protein 1 pseudogene 1* — 2p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.26× (z +13.8, q 1e-40, up in 28 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.573× (z -6.6, q 2e-08, down in 20 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC3H4]] (+0.73, fdr 8e-06), [[ANKRD31]] (+0.73, fdr 7e-06), [[ZBED9]] (+0.73, fdr 7e-06); moves opposite to [[DCUN1D2]] (-0.67, fdr 2e-05), [[HEBP1]] (-0.63, fdr 8e-05), [[INTS10]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RIMS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15065.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.26×** | +13.8 | 1e-40 | 28/36 (HS-578T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.96×** | +11.4 | 1e-27 | 28/46 (SW480, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +9.7 | 7e-20 | 1/4 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +7.9 | 3e-13 | 6/9 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +7.0 | 2e-10 | 14/37 (NCI-H2030, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +7.0 | 2e-10 | 12/22 (HT-29, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.51×** | +5.0 | 5e-05 | 15/40 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.6 | 3e-04 | 8/44 (A498, MIA PaCa-2, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +4.5 | 4e-04 | 9/41 (HOP62, RKO, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.04×** | +4.5 | 4e-04 | 10/40 (NCI-H460, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +4.3 | 0.001 | 15/41 (A-427, RKO, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.003 | 10/43 (A-427, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.34×** | +3.5 | 0.018 | 4/44 (C-33 A, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.018 | 6/40 (SW480, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.090 | 4/41 (SW480, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15065.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.573×** | -6.6 | 2e-08 | 20/46 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.635×** | -5.1 | 1e-04 | 16/41 (J82, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.661×** | -4.9 | 2e-04 | 18/45 (SK-MEL-2, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.890× | -4.5 | 0.001 | 16/47 (HEC-1-A, SNU-423, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.714×** | -4.0 | 0.008 | 14/42 (LoVo, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~5% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.733×** | -3.7 | 0.023 | 12/35 (LoVo, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.740×** | -3.5 | 0.031 | 13/42 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.750×** | -3.4 | 0.049 | 10/45 (NCI-H23, SW 1271, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.768× | -3.1 | 0.12 | 13/41 (NCI-H23, LoVo, …) | all doses, flat | cell-cycle shift (explains ~4% here); position effect removed |
| [[Simotinib (drug)]] 0.05 µM |  | 0.755× | -3.1 | 0.13 | 6/37 (RKO, J82, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15065. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 4.48 | 0 | 1 | — | [[Auranofin (drug)]] 0.5 µM 0.0784× (z -8.9) |
| [[A498 (line)]] | wt | 2.98 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0887× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 2.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.42× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 8.73 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0573× (z -13.3) |
| [[A-172 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15065), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H4]] | +0.73 | +0.75 / +0.58 | both halves | 8e-06 |  |
| [[ANKRD31]] | +0.73 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[ZBED9]] | +0.73 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[GDAP1]] | +0.72 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[C22orf46]] | +0.72 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[TRAM2-AS1]] | +0.71 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[PGBD4]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[PDCL3P4]] | +0.70 | +0.77 / +0.44 | both halves | 3e-05 |  |
| [[ZNF620]] | +0.70 | +0.77 / +0.43 | both halves | 3e-05 |  |
| [[KRT8P12]] | +0.69 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[TRMO]] | +0.69 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[KRBA2]] | +0.69 | +0.74 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCUN1D2]] | -0.67 | -0.72 / -0.47 | both halves | 2e-05 |  |
| [[HEBP1]] | -0.63 | -0.66 / -0.37 | both halves | 8e-05 |  |
| [[INTS10]] | -0.63 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[MTM1]] | -0.60 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[EEF1AKMT4]] | -0.60 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[SLC31A1]] | -0.60 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[PRKRA]] | -0.59 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[UQCRH]] | -0.59 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[PPP1R12B]] | -0.58 | -0.52 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RIMS2]] | B | RIMS2 activity raises FNBP1P1's level | lines that do not express RIMS2 (23) vs lines expressing it (27) | 1.30× lower at baseline in the lines without RIMS2 | 0.042 | ⚠ within organs, on part of the lines; also absent: TWIST1, SLC6A17, RUNX3 |
| [[MIR1915HG]] | B | MIR1915HG activity raises FNBP1P1's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 1.42× lower at baseline in the lines without MIR1915HG | 0.093 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.701). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-27.6, 13.0); signed map (12.8, -23.4). **Vector** length 55.9, 7.42% of its response variance represented; |z| ≥ 3 in 1,002 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.9 | +11.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +13.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +4.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +2.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -4.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.4 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -2.1 | -3.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.0 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -2.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | +0.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -0.6 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.0 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | formin binding protein 1 pseudogene 1 |
| Locus type | pseudogene |
| Location | 2p13.1 — chr2:74,120,680-74,123,218 (+) |
| Ensembl biotype | processed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44528](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44528) · Entrez [100533642](https://www.ncbi.nlm.nih.gov/gene/100533642) · Ensembl [ENSG00000257800](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257800)

## Data

Gene col 15065: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15065); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15065, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15065]; `tensor/DDL_lfc|DDL_z.npy` [15065]; `embed/gene_vectors.npy` [15065]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15065 or target_col == 15065). Every well: [[FNBP1P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FNBP1P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
