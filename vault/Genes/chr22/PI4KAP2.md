---
symbol: "PI4KAP2"
type: "gene"
col: 11411
ensembl_id: "ENSG00000183506"
name: "phosphatidylinositol 4-kinase alpha pseudogene 2"
location: "22q11.21"
module: 88
arm: "-"
pooled_cpm: 5.12
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 6
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# PI4KAP2

*phosphatidylinositol 4-kinase alpha pseudogene 2* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.71× (z +7.4, q 1e-10, up in 27 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.736× (z -5.9, q 2e-06, down in 17 of 40 measured lines) ⚠ cell-cycle shift, explains ~23% of this change. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 0.681× (z -3.7, q 0.015, down in 10 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (MIA PaCa-2 0.0637×, LoVo 0.160×, NCI-H460 0.160×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.115×; ⚠ toxic; transcription drop); [[Ataluren (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0620×); [[ETC-206 (drug)]] 0.05 µM in 1 line (Hs 766T 0.0699×); [[Mozavaptan (drug)]] 5 µM in 1 line (A549 0.0748×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PI4KAP1]] (+0.85, fdr 7e-06), [[HIC2]] (+0.67, fdr 1e-05, ⚠ same locus), [[CBFA2T2]] (+0.65, fdr 5e-05), [[PI4KAP1-1]] (+0.62, fdr 3e-05); moves opposite to [[MCTS1]] (-0.66, fdr 3e-05), [[TASOR]] (-0.66, fdr 3e-05), [[ARMT1]] (-0.66, fdr 3e-05).
> It sits in the **-** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11411.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +7.4 | 1e-10 | 27/46 (Panc 03.27, SW1417, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +6.9 | 2e-09 | 21/45 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +6.0 | 3e-07 | 17/45 (SW1417, A498, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +5.8 | 1e-06 | 16/45 (PANC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +5.4 | 6e-06 | 13/45 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.33×** | +3.9 | 0.011 | 5/43 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +3.6 | 0.025 | 8/40 (SW1417, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.053 | 7/45 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.071 | 1/46 (NCI-H1573) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11411.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (MIA PaCa-2 0.0637×, LoVo 0.160×, NCI-H460 0.160×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.115×; ⚠ toxic; transcription drop); [[Ataluren (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0620×); [[ETC-206 (drug)]] 0.05 µM in 1 line (Hs 766T 0.0699×); [[Mozavaptan (drug)]] 5 µM in 1 line (A549 0.0748×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.736×** | -5.9 | 2e-06 | 17/40 (A-172, NCI-H23, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.701×** | -4.8 | 4e-04 | 15/26 (MIA PaCa-2, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.681×** | -4.8 | 4e-04 | 12/15 (MIA PaCa-2, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.915× | -4.4 | 0.002 | 10/47 (HEC-1-A, HepG2/C3A, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.749×** | -3.9 | 0.009 | 14/34 (HOP62, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.681×** | -3.7 | 0.015 | 10/39 (Hs 766T, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.760×** | -3.7 | 0.015 | 14/43 (RPMI-7951, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11411. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 9.64 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0637× (z -14.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 5.66 | 0 | 2 | — | [[Neratinib (drug)]] 0.05 µM 0.0710× (z -9.6) |
| [[A-427 (line)]] | wt | 4.25 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0885× (z -8.7) |
| [[A549 (line)]] | wt | 4.70 | 0 | 1 | — | [[Mozavaptan (drug)]] 5 µM 0.0748× (z -9.8) |
| [[Hs 766T (line)]] | wt | 7.57 | 0 | 1 | — | [[ETC-206 (drug)]] 0.05 µM 0.0699× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 6.67 | 0 | 1 | — | [[Ataluren (drug)]] 0.5 µM 0.0620× (z -9.9) |
| [[LoVo (line)]] | wt | 7.64 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 4.61 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.811 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11411), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PI4KAP1]] | +0.85 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[HIC2]] | +0.67 | +0.56 / +0.69 | both halves | 1e-05 | ⚠ same locus (21.6 kb: neighbours can correlate without regulation) |
| [[CBFA2T2]] | +0.65 | +0.69 / +0.40 | both halves | 5e-05 |  |
| [[PI4KAP1-1]] | +0.62 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[GIT1]] | +0.62 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[RALGDS]] | +0.60 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[FAM118A]] | +0.60 | +0.66 / +0.27 | both halves | 3e-04 |  |
| [[SDHAP2]] | +0.60 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[CD81]] | +0.60 | +0.63 / +0.39 | both halves | 6e-05 |  |
| [[ATAT1]] | +0.60 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[KLHL7]] | +0.59 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[SS18L1]] | +0.59 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[ZFPM1]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCTS1]] | -0.66 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[TASOR]] | -0.66 | -0.69 / -0.45 | both halves | 3e-05 |  |
| [[ARMT1]] | -0.66 | -0.68 / -0.46 | both halves | 3e-05 |  |
| [[RGS5]] | -0.66 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[LEKR1]] | -0.65 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[PPP2CA]] | -0.65 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[CLHC1]] | -0.63 | -0.65 / -0.35 | both halves | 1e-04 |  |
| [[ANAPC13]] | -0.63 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[LINC00886]] | -0.63 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[ZXDB]] | -0.62 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[CENPBD1P]] | -0.62 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[ZNF260]] | -0.61 | -0.60 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers PI4KAP2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **-** arm (projection on the module's main direction -0.637). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (-6.9, 1.3); signed map (-33.0, 13.8). **Vector** length 44.3, 4.42% of its response variance represented; |z| ≥ 3 in 971 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +2.2 | +7.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.1 | +6.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.6 | +5.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.5 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.0 | +1.6 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +0.9 | +0.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +0.9 | +3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +0.8 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -3.9 | -5.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -0.5 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -1.0 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol 4-kinase alpha pseudogene 2 |
| Locus type | pseudogene |
| Location | 22q11.21 — chr22:21,473,059-21,488,358 (-) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Matched by | ensembl_id |

UniProt [A4QPH2](https://www.uniprot.org/uniprotkb/A4QPH2) carries no function annotation.

**Summary**, from NCBI Gene [375133](https://www.ncbi.nlm.nih.gov/gene/375133):

> Predicted to enable kinase activity. Predicted to be involved in phosphatidylinositol phosphate biosynthetic process. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33577](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33577) · Entrez [375133](https://www.ncbi.nlm.nih.gov/gene/375133) · UniProt [A4QPH2](https://www.uniprot.org/uniprotkb/A4QPH2) · Ensembl [ENSG00000183506](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183506)

## Data

Gene col 11411: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11411); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11411, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11411]; `tensor/DDL_lfc|DDL_z.npy` [11411]; `embed/gene_vectors.npy` [11411]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11411 or target_col == 11411). Every well: [[PI4KAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PI4KAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
