---
symbol: "CPSF1"
type: "gene"
col: 995
ensembl_id: "ENSG00000071894"
name: "cleavage and polyadenylation specific factor 1"
location: "8q24.3"
module: 2
arm: "+"
pooled_cpm: 25.5
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CPSF1

*cleavage and polyadenylation specific factor 1* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.71× (z +9.8, q 4e-20, up in 26 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.48× (z +7.4, q 1e-11, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.801× (z -6.0, q 1e-06, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZDHHC8]] (+0.79, fdr 7e-06), [[TUBGCP6]] (+0.77, fdr 7e-06), [[INTS11]] (+0.75, fdr 7e-06); moves opposite to [[MPLKIP]] (-0.60, fdr 1e-05), [[IFNAR1]] (-0.59, fdr 1e-05), [[TAF7]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MLPH]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 995.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +9.8 | 4e-20 | 26/37 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.65×** | +9.5 | 6e-19 | 34/43 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.51×** | +7.8 | 2e-12 | 30/48 (RKO, COLO 205, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.48×** | +7.4 | 1e-11 | 28/48 (COLO 205, RKO, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.39×** | +5.8 | 8e-07 | 22/39 (LS 180, CFPAC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.31×** | +5.1 | 3e-05 | 20/47 (COLO 205, LoVo, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +4.1 | 0.003 | 13/47 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.23×** | +3.8 | 0.012 | 17/46 (RKO, KATO III, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.31×** | +3.6 | 0.019 | 11/48 (NCI-H460, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.041 | 12/46 (HCT15, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.12 | 5/47 (A-427, NCI-H2030, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 995.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.801×** | -6.0 | 1e-06 | 26/47 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.810×** | -5.7 | 4e-06 | 23/48 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.763×** | -5.1 | 5e-05 | 24/47 (SW48, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.761×** | -5.0 | 8e-05 | 20/46 (hTERT-HPNE, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.821×** | -3.8 | 0.020 | 19/47 (CHP-212, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **0.824×** | -3.7 | 0.022 | 10/48 (COLO 205, HT-29, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.836× | -3.4 | 0.051 | 17/48 (A498, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -3.3 | 0.069 | 13/48 (A498, C32, …) | two highest doses | position effect removed |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 0.845× | -3.2 | 0.069 | 9/47 (CFPAC-1, A-172, …) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | 0.839× | -3.2 | 0.069 | 16/47 (AN3 CA, A498, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -3.2 | 0.069 | 14/48 (SW 900, AsPC-1, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 995. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 23.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +10.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 29.9 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.101× (z -9.2) |
| [[C-33 A (line)]] | alt | 31.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.218× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[COLO 205 (line)]] | alt | 22.7 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.86× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 36.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.291× (z -11.2) |
| [[J82 (line)]] | alt | 23.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -9.5) |
| [[LoVo (line)]] | wt | 23.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.20× (z +9.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 23.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2030 (line)]] | alt | 37.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.391× (z -8.6) |
| [[PANC-1 (line)]] | alt | 26.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.00× (z +11.3) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 36.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.70× (z +9.8) ⚠ toxic; cell-cycle shift, explains ~27% of this change | — |
| [[SW48 (line)]] | wt | 34.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0315× (z -19.5) |
| [[A-172 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 995), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC8]] | +0.79 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[TUBGCP6]] | +0.77 | +0.69 / +0.75 | both halves | 7e-06 | STRING 450 |
| [[INTS11]] | +0.75 | +0.69 / +0.67 | both halves | 7e-06 | same gene group; STRING 808 |
| [[DPH7]] | +0.74 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[ATAD3A]] | +0.73 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[TCF3]] | +0.72 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[KLHL17]] | +0.72 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[ABHD17A]] | +0.71 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[MSTO2P]] | +0.71 | +0.70 / +0.58 | both halves | 8e-06 |  |
| [[ABCA2]] | +0.71 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[CEP131]] | +0.70 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ATAD3B]] | +0.70 | +0.66 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPLKIP]] | -0.60 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[IFNAR1]] | -0.59 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[TAF7]] | -0.58 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[LINC02307]] | -0.58 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[MED13]] | -0.57 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[PNRC1]] | -0.57 | -0.49 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MLPH]] | B | MLPH activity lowers CPSF1's level | lines that do not express MLPH (13) vs lines expressing it (37) | 1.18× higher at baseline in the lines without MLPH | 0.075 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |
| [[HDAC6]] | B | HDAC6 activity lowers CPSF1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.743). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-8.0, -24.1); signed map (-44.8, -10.9). **Vector** length 84.9, 16.5% of its response variance represented; |z| ≥ 3 in 777 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +4.3 | +9.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.2 | +7.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +3.3 | +5.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +3.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.9 | +3.6 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +1.9 | +1.8 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.8 | +2.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -4.5 | -3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -3.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | -6.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.9 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -3.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | cleavage and polyadenylation specific factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,393,229-144,409,335 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CPSF160 |
| Gene groups (HGNC) | Cleavage and polyadenylation specific factor subunits; MicroRNA protein coding host genes |
| Reactome | 15 pathways, smallest: Processing of Intronless Pre-mRNAs; Processing of Capped Intronless Pre-mRNA; RNA Polymerase II Transcription Termination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q10570](https://www.uniprot.org/uniprotkb/Q10570) (Cleavage and polyadenylation specificity factor subunit 1):

> Component of the cleavage and polyadenylation specificity factor (CPSF) complex that plays a key role in pre-mRNA 3'-end formation, recognizing the AAUAAA signal sequence and interacting with poly(A) polymerase and other factors to bring about cleavage and poly(A) addition. This subunit is involved in the RNA recognition step of the polyadenylation reaction. May play a role in eye morphogenesis and the development of retinal ganglion cell projections to the midbrain (By similarity).

**Summary**, from NCBI Gene [29894](https://www.ncbi.nlm.nih.gov/gene/29894):

> Cleavage and polyadenylation specificity factor (CPSF) is a multisubunit complex that plays a central role in 3-prime processing of pre-mRNAs. CPSF recognizes the AAUAAA signal in the pre-mRNA and interacts with other proteins to facilitate both RNA cleavage and poly(A) synthesis. CPSF1 is the largest subunit of the CPSF complex (Murthy and Manley, 1995 [PubMed 7590244]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:2324](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2324) · Entrez [29894](https://www.ncbi.nlm.nih.gov/gene/29894) · UniProt [Q10570](https://www.uniprot.org/uniprotkb/Q10570) · Ensembl [ENSG00000071894](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071894)

## Data

Gene col 995: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 995); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 995, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 995]; `tensor/DDL_lfc|DDL_z.npy` [995]; `embed/gene_vectors.npy` [995]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 995 or target_col == 995). Every well: [[CPSF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPSF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
