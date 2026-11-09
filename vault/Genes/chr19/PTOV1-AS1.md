---
symbol: "PTOV1-AS1"
type: "gene"
col: 15585
ensembl_id: "ENSG00000268006"
name: "PTOV1 antisense RNA 1"
location: "19q13.33"
module: 26
arm: "+"
pooled_cpm: 3.28
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 10
n_dd_up_clean: 12
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# PTOV1-AS1

*PTOV1 antisense RNA 1* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 7.36× (z +22.0, q 0e+00, up in 40 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.465× (z -8.4, q 2e-14, down in 26 of 45 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.530× (z -7.0, q 9e-10, down in 24 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PARD6G-AS1]] (+0.81, fdr 7e-06), [[ZFHX2-AS1]] (+0.78, fdr 7e-06), [[FBXL19-AS1]] (+0.78, fdr 7e-06); moves opposite to [[SDHAF3]] (-0.66, fdr 1e-05), [[SLC35A1]] (-0.63, fdr 1e-05), [[KIF3A]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MTMR9LP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15585.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **7.36×** | +22.0 | 0e+00 | 40/43 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.68×** | +15.3 | 0e+00 | 25/36 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.45×** | +13.9 | 6e-42 | 31/34 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +9.3 | 2e-18 | 1/3 (HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.34×** | +8.6 | 6e-16 | 3/6 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.89×** | +7.0 | 3e-10 | 6/17 (SW1417, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.84×** | +6.3 | 2e-08 | 20/42 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +5.8 | 5e-07 | 13/35 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.65×** | +5.6 | 1e-06 | 3/9 (SW1417, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.1 | 2e-05 | 8/45 (HOP62, SW1417, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +5.1 | 2e-05 | 13/44 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Orlistat (drug)]] 0.05 µM |  | **1.52×** | +4.2 | 0.001 | 6/36 (A549, SW480, …) | inconsistent across doses |  |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.44×** | +4.0 | 0.003 | 8/40 (RKO, KATO III, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.91×** | +3.7 | 0.008 | 0/37 | top dose only | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.016 | 10/34 (NCI-H460, C-33 A, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.023 | 2/38 (HT-29, HOP62) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15585.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.465×** | -8.4 | 2e-14 | 26/45 (HEC-1-A, J82, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.530×** | -7.0 | 9e-10 | 24/40 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.547×** | -6.6 | 7e-09 | 22/45 (C32, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.552×** | -6.5 | 1e-08 | 20/45 (NCI-H1792, SW480, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.579×** | -6.0 | 2e-07 | 17/45 (SNU-423, LS 180, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.654×** | -4.7 | 3e-04 | 13/44 (SW480, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.755×** | -4.4 | 0.001 | 14/45 (SK-MEL-2, KATO III, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.762×** | -4.2 | 0.002 | 11/44 (Panc 03.27, SW 900, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.488×** | -4.1 | 0.002 | 9/42 (A498, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.750×** | -3.2 | 0.092 | 9/42 (SW480, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15585. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 4.60 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.108× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 2.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +12.5) | — |
| [[C32 (line)]] | wt | 4.81 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.45× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 7.61 | 1 | 0 | [[Auranofin (drug)]] 5 µM 14.1× (z +12.1) | — |
| [[HS-578T (line)]] | alt | 3.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.0× (z +13.8) | — |
| [[HT-29 (line)]] | alt | 3.99 | 1 | 0 | [[Auranofin (drug)]] 5 µM 31.4× (z +12.3) | — |
| [[hTERT-HPNE (line)]] | wt | 2.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 2.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.34× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 2.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +13.4) | — |
| [[RPMI-7951 (line)]] | alt | 5.91 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.7× (z +13.2) | — |
| [[SK-MEL-2 (line)]] | alt | 5.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +12.4) | — |
| [[SNU-423 (line)]] | alt | 2.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 5.01 | 1 | 0 | [[Auranofin (drug)]] 5 µM 14.4× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 4.22 | 1 | 0 | [[Auranofin (drug)]] 5 µM 11.8× (z +9.0) | — |
| [[SW480 (line)]] | alt | 4.15 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.10× (z +11.4) | — |
| [[A-172 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15585), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARD6G-AS1]] | +0.81 | +0.77 / +0.69 | both halves | 7e-06 | same gene group |
| [[ZFHX2-AS1]] | +0.78 | +0.67 / +0.67 | both halves | 7e-06 | same gene group |
| [[FBXL19-AS1]] | +0.78 | +0.65 / +0.73 | both halves | 7e-06 | same gene group |
| [[ZNF546]] | +0.77 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[NQO1-DT]] | +0.77 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[LINC01618]] | +0.76 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[CELF6]] | +0.76 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[C2orf49-DT]] | +0.76 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[CCDC90B-AS1]] | +0.74 | +0.68 / +0.62 | both halves | 7e-06 | same gene group |
| [[YIPF7]] | +0.74 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[UBE2D3-AS1]] | +0.74 | +0.69 / +0.55 | both halves | 1e-05 | same gene group |
| [[NEB]] | +0.74 | +0.70 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAF3]] | -0.66 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[SLC35A1]] | -0.63 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[KIF3A]] | -0.63 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTMR9LP]] | B | MTMR9LP activity lowers PTOV1-AS1's level | lines that do not express MTMR9LP (9) vs lines expressing it (41) | 1.20× higher at baseline in the lines without MTMR9LP | 0.070 | ⚠ within organs, on part of the lines; also absent: SMAD7, TNFRSF21, TNFRSF14; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises PTOV1-AS1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises PTOV1-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.766). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (10.3, 12.6); signed map (22.4, -2.3). **Vector** length 74.1, 11.8% of its response variance represented; |z| ≥ 3 in 1,289 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.8 | +22.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.7 | +15.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +13.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +5.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +3.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.8 | +1.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.0 | -8.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.7 | -6.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | -4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -3.1 | -6.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.0 | -7.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -4.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -2.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | PTOV1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19q13.33 — chr19:49,838,639-49,851,676 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44174](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44174) · Entrez [100506033](https://www.ncbi.nlm.nih.gov/gene/100506033) · Ensembl [ENSG00000268006](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000268006)

## Data

Gene col 15585: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15585); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15585, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15585]; `tensor/DDL_lfc|DDL_z.npy` [15585]; `embed/gene_vectors.npy` [15585]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15585 or target_col == 15585). Every well: [[PTOV1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTOV1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
