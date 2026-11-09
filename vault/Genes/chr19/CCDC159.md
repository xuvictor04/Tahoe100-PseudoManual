---
symbol: "CCDC159"
type: "gene"
col: 11399
ensembl_id: "ENSG00000183401"
name: "coiled-coil domain containing 159"
location: "19p13.2"
module: 68
arm: "+"
pooled_cpm: 4.37
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# CCDC159

*coiled-coil domain containing 159* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.66× (z +8.3, q 8e-14, up in 17 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.616× (z -5.6, q 1e-05, down in 16 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.639× (z -5.2, q 7e-05, down in 16 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPR108]] (+0.58, fdr 1e-05), [[THBS3]] (+0.58, fdr 1e-05), [[COG4]] (+0.58, fdr 1e-05); moves opposite to [[FBXW11]] (-0.55, fdr 1e-05), [[RAP1GDS1]] (-0.54, fdr 4e-05), [[SIMC1]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11399.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +8.3 | 8e-14 | 17/39 (AsPC-1, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.96×** | +7.8 | 2e-12 | 15/24 (NCI-H2030, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +7.2 | 1e-10 | 4/7 (NCI-H2030, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +5.4 | 1e-05 | 4/12 (NCI-H2030, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +5.2 | 3e-05 | 15/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +4.4 | 0.001 | 13/42 (PANC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.54×** | +3.6 | 0.029 | 4/33 (A-172, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.058 | 6/46 (HS-578T, AN3 CA, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | 1.29× | +3.1 | 0.12 | 3/46 (NCI-H2030, HCT15, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11399.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.616×** | -5.6 | 1e-05 | 16/36 (SNU-423, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.639×** | -5.2 | 7e-05 | 16/45 (NCI-H1792, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.669×** | -4.6 | 7e-04 | 18/47 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.673×** | -4.6 | 7e-04 | 15/45 (A549, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.689×** | -4.3 | 0.002 | 20/45 (HS-578T, SW 1271, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.690×** | -4.3 | 0.002 | 16/46 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.739×** | -3.5 | 0.038 | 8/46 (SW 1271, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.744×** | -3.4 | 0.040 | 13/44 (C-33 A, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.744×** | -3.4 | 0.040 | 13/40 (hTERT-HPNE, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.734×** | -3.4 | 0.040 | 13/44 (SK-MEL-2, A-172, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.748×** | -3.4 | 0.040 | 6/46 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.604× | -3.0 | 0.11 | 9/37 (NCI-H460, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11399. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 3.73 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0718× (z -9.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[AsPC-1 (line)]] | alt | 2.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.89× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 9.78 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0844× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 4.65 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.228× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 7.00 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0491× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 3.16 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.05 µM 0.0706× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 6.51 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0968× (z -8.5) |
| [[SNU-423 (line)]] | alt | 8.14 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.150× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11399), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR108]] | +0.58 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[THBS3]] | +0.58 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[COG4]] | +0.58 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[ETFRF1]] | +0.57 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[PAN2]] | +0.57 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[GALT]] | +0.56 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[CHMP4A]] | +0.56 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[CIRBP]] | +0.56 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[RING1]] | +0.55 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[DXO]] | +0.55 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[THAP9]] | +0.54 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[YY1AP1]] | +0.54 | +0.40 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW11]] | -0.55 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[RAP1GDS1]] | -0.54 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[SIMC1]] | -0.54 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[COP1]] | -0.54 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[NUDCD1]] | -0.53 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[CMTM8]] | -0.52 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[CDC123]] | -0.51 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[BRI3BP]] | -0.50 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[POP1]] | -0.50 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[EVI5]] | -0.50 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[KIF2A]] | -0.49 | -0.57 / -0.33 | both halves | 1e-04 |  |
| [[HACD3]] | -0.49 | -0.54 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises CCDC159's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.383). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-3.5, -31.5); signed map (11.1, -20.1). **Vector** length 54.0, 6.64% of its response variance represented; |z| ≥ 3 in 998 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +7.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +8.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.7 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +5.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +3.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.1 | +2.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.1 | +1.1 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.1 | +1.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.0 | +1.4 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.1 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.3 | -3.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -5.2 |
|  | [[EX229 (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 159 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:11,344,684-11,354,944 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [P0C7I6](https://www.uniprot.org/uniprotkb/P0C7I6) (Coiled-coil domain-containing protein 159):

> Functions during spermatid development; may participate in the centrosome reduction procedure of spermatids and is required for the formation of the connecting piece/sperm head-tail coupling apparatus (HTCA) and the correct and tight attachment of the flagellum to the nuclear envelope.

**Summary**, from NCBI Gene [126075](https://www.ncbi.nlm.nih.gov/gene/126075):

> Predicted to be involved in spermatid development. Predicted to act upstream of or within several processes, including regulation of phosphatase activity; single fertilization; and sperm flagellum assembly. Predicted to be located in sperm head-tail coupling apparatus. [provided by Alliance of Genome Resources, Apr 2025]

**Accessions** — [HGNC:26996](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26996) · Entrez [126075](https://www.ncbi.nlm.nih.gov/gene/126075) · UniProt [P0C7I6](https://www.uniprot.org/uniprotkb/P0C7I6) · Ensembl [ENSG00000183401](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183401)

## Data

Gene col 11399: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11399); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11399, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11399]; `tensor/DDL_lfc|DDL_z.npy` [11399]; `embed/gene_vectors.npy` [11399]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11399 or target_col == 11399). Every well: [[CCDC159 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC159.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
