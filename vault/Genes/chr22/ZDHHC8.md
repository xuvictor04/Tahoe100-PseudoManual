---
symbol: "ZDHHC8"
type: "gene"
col: 1827
ensembl_id: "ENSG00000099904"
name: "zDHHC palmitoyltransferase 8"
location: "22q11.21"
module: 2
arm: "+"
pooled_cpm: 5.84
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ZDHHC8

*zDHHC palmitoyltransferase 8* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.87× (z +7.0, q 2e-09, up in 7 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.58× (z +5.3, q 3e-05, up in 16 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.635× (z -7.5, q 3e-11, down in 24 of 40 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.515× (z -7.5, q 3e-11, down in 28 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPSF1]] (+0.79, fdr 7e-06), [[KLHL17]] (+0.78, fdr 7e-06), [[INTS11]] (+0.77, fdr 7e-06); moves opposite to [[TAF7]] (-0.64, fdr 1e-05), [[BAZ2B]] (-0.63, fdr 1e-05), [[C11orf58]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1827.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +7.0 | 2e-09 | 7/12 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.58×** | +5.3 | 3e-05 | 16/41 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +5.0 | 1e-04 | 16/47 (NCI-H1792, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +4.9 | 2e-04 | 19/47 (NCI-H1792, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.38×** | +3.8 | 0.020 | 12/42 (C32, MIA PaCa-2, …) | two highest doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +3.7 | 0.022 | 8/18 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.35×** | +3.5 | 0.041 | 9/47 (HS-578T, SW480, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.35×** | +3.4 | 0.041 | 11/36 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1827.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.635×** | -7.5 | 3e-11 | 24/40 (Panc 03.27, NCI-H2030, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.515×** | -7.5 | 3e-11 | 28/44 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.562×** | -6.7 | 3e-09 | 26/46 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.633×** | -5.4 | 1e-05 | 20/40 (PANC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.637×** | -5.3 | 2e-05 | 16/46 (HEC-1-A, HT-29, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.644×** | -5.1 | 3e-05 | 19/47 (KATO III, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.679×** | -4.5 | 5e-04 | 19/41 (J82, LOX-IMVI, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.766× | -3.1 | 0.13 | 15/46 (KATO III, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | 0.771× | -3.0 | 0.15 | 5/46 (A-172, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1827. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 6.87 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -10.9) ⚠ cell-cycle shift, explains ~43% of this change |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -12.8) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A498 (line)]] | wt | 6.44 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.203× (z -9.0) |
| [[C32 (line)]] | wt | 4.98 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 5 µM 0.0610× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 7.22 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0608× (z -9.6) |
| [[J82 (line)]] | alt | 6.46 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[LoVo (line)]] | wt | 5.01 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -10.2) ⚠ cell-cycle shift, explains ~43% of this change |
| [[MIA PaCa-2 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 3.09 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0590× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 4.28 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0835× (z -8.7) |
| [[PANC-1 (line)]] | alt | 4.93 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.108× (z -11.5) |
| [[SW1417 (line)]] | alt | 8.16 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -8.5) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A-172 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.51 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1827), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPSF1]] | +0.79 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[KLHL17]] | +0.78 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[INTS11]] | +0.77 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[TRABD]] | +0.75 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[ST6GALNAC6]] | +0.75 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[TCF3]] | +0.74 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[IMPDH1]] | +0.73 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[UCKL1]] | +0.72 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[ZNF598]] | +0.72 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[WDR5]] | +0.70 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[ABCA2]] | +0.69 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[ABHD17A]] | +0.69 | +0.65 / +0.61 | both halves | 7e-06 | STRING 458 |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF7]] | -0.64 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[BAZ2B]] | -0.63 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[C11orf58]] | -0.61 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[ERCC6L2]] | -0.59 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[OTUD6B-AS1]] | -0.58 | -0.67 / -0.42 | both halves | 4e-05 |  |
| [[ZNF518A]] | -0.58 | -0.54 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ZDHHC8's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ANKRD13B]] | C | ANKRD13B activity raises ZDHHC8's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 2.00× lower at baseline in the lines without ANKRD13B | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.826). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-7.6, -23.3); signed map (-44.8, -10.1). **Vector** length 63.1, 9.14% of its response variance represented; |z| ≥ 3 in 873 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +3.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.1 | +0.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.0 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -7.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -6.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -2.7 | -7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.1 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -1.6 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.8 | -1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.5 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | zDHHC palmitoyltransferase 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:20,129,456-20,148,007 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF378, KIAA1292, DHHC8 |
| Gene groups (HGNC) | Zinc fingers DHHC-type |
| Reactome | 10 pathways, smallest: HDL assembly; Plasma lipoprotein assembly; Maturation of spike protein_9694548 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULC8](https://www.uniprot.org/uniprotkb/Q9ULC8) (Palmitoyltransferase ZDHHC8):

> Palmitoyltransferase that catalyzes the addition of palmitate onto various protein substrates and therefore functions in several unrelated biological processes. Through the palmitoylation of ABCA1 regulates the localization of the transporter to the plasma membrane and thereby regulates its function in cholesterol and phospholipid efflux. Could also pamitoylate the D(2) dopamine receptor DRD2 and regulate its stability and localization to the plasma membrane. Could also play a role in …

**Summary**, from NCBI Gene [29801](https://www.ncbi.nlm.nih.gov/gene/29801):

> This gene encodes a four transmembrane protein that is a member of the zinc finger DHHC domain-containing protein family. The encoded protein may function as a palmitoyltransferase. Defects in this gene may be associated with a susceptibility to schizophrenia. Alternate splicing of this gene results in multiple transcript variants. A pseudogene of this gene is found on chromosome 22.[provided by RefSeq, May 2010]

**Accessions** — [HGNC:18474](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18474) · Entrez [29801](https://www.ncbi.nlm.nih.gov/gene/29801) · UniProt [Q9ULC8](https://www.uniprot.org/uniprotkb/Q9ULC8) · Ensembl [ENSG00000099904](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099904)

## Data

Gene col 1827: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1827); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1827, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1827]; `tensor/DDL_lfc|DDL_z.npy` [1827]; `embed/gene_vectors.npy` [1827]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1827 or target_col == 1827). Every well: [[ZDHHC8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZDHHC8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
