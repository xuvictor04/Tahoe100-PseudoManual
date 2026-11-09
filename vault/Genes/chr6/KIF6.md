---
symbol: "KIF6"
type: "gene"
col: 8976
ensembl_id: "ENSG00000164627"
name: "kinesin family member 6"
location: "6p21.2"
module: 90
arm: "+"
pooled_cpm: 2.73
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# KIF6

*kinesin family member 6* — 6p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.45× (z +15.5, q 0e+00, up in 24 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00861]] (+0.74, fdr 7e-06), [[GRM7]] (+0.71, fdr 7e-06), [[G2E3-AS1]] (+0.71, fdr 7e-06).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[LINC01611]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8976.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.45×** | +15.5 | 0e+00 | 24/30 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.33×** | +13.0 | 4e-36 | 9/10 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.26×** | +12.4 | 8e-33 | 3/3 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.89×** | +8.0 | 2e-13 | 10/30 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.99×** | +6.1 | 1e-07 | 14/38 (HOP62, BT-474, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.32×** | +5.9 | 4e-07 | 1/3 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +5.4 | 6e-06 | 6/25 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +5.2 | 2e-05 | 8/42 (hTERT-HPNE, SHP-77, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.63×** | +4.3 | 9e-04 | 18/44 (A498, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +4.2 | 0.002 | 6/28 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.57×** | +4.0 | 0.003 | 13/42 (A498, HEC-1-A, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.011 | 6/43 (HEC-1-A, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.51×** | +3.6 | 0.011 | 10/41 (A498, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.35×** | +3.6 | 0.011 | 4/43 (SK-MEL-2, SW480, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.42×** | +3.1 | 0.069 | 4/34 (NCI-H1573, A-427, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +3.1 | 0.069 | 6/38 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.1 | 0.069 | 13/36 (HOP62, COLO 205, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.069 | 1/35 (NCI-H460) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Decitabine (drug)]] 0.5 µM |  | **1.40×** | +3.0 | 0.077 | 8/33 (A-172, SW 900, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.42×** | +3.0 | 0.077 | 7/35 (SK-MEL-2, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8976.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | 0.671× | -3.5 | 0.12 | 9/37 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | 0.672× | -3.5 | 0.12 | 3/39 (HepG2/C3A, C-33 A, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8976. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8976), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00861]] | +0.74 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[GRM7]] | +0.71 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[G2E3-AS1]] | +0.71 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[LRIG2-DT]] | +0.71 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[LINC01414]] | +0.70 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[CNTN5]] | +0.70 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[PPP1R9A-AS1]] | +0.69 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[CHODL]] | +0.69 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[LRRN3]] | +0.69 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.69 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[LINC02208]] | +0.68 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[GRID2]] | +0.68 | +0.60 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01611]] | B | LINC01611 activity raises KIF6's level | lines that do not express LINC01611 (34) vs lines expressing it (16) | 1.70× lower at baseline in the lines without LINC01611 | 0.010 | ⚠ within organs, on part of the lines; also absent: CDH13, ENSG00000248973, LINC02377 |
| [[POU3F2]] | B | POU3F2 activity raises KIF6's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 1.68× lower at baseline in the lines without POU3F2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC |
| [[HTR2C]] | B | HTR2C activity raises KIF6's level | lines that do not express HTR2C (22) vs lines expressing it (28) | 1.65× lower at baseline in the lines without HTR2C | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, KCNJ6, PTPRN; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers KIF6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01905]] | B | LINC01905 activity raises KIF6's level | lines that do not express LINC01905 (35) vs lines expressing it (15) | 1.67× lower at baseline in the lines without LINC01905 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000267327, ENSG00000267284, SLC25A24P1 |
| [[NIHCOLE]] | B | NIHCOLE activity raises KIF6's level | lines that do not express NIHCOLE (22) vs lines expressing it (28) | 1.35× lower at baseline in the lines without NIHCOLE | 0.043 | ⚠ within organs, on part of the lines; also absent: RORC, TSPAN1, VIL1 |
| [[MIR2052HG]] | B | MIR2052HG activity raises KIF6's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 1.54× lower at baseline in the lines without MIR2052HG | 0.068 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent |
| [[SERPINF1]] | B | SERPINF1 activity raises KIF6's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.25× lower at baseline in the lines without SERPINF1 | 0.094 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent |
| [[SLC25A24P1]] | B | SLC25A24P1 activity raises KIF6's level | lines that do not express SLC25A24P1 (40) vs lines expressing it (10) | 1.73× lower at baseline in the lines without SLC25A24P1 | 0.094 | ⚠ within organs, on part of the lines; also absent: LINC01425, ENSG00000275016, MAGEB2 |
| [[GRIK2]] | B | GRIK2 activity raises KIF6's level | lines that do not express GRIK2 (19) vs lines expressing it (31) | 1.44× lower at baseline in the lines without GRIK2 | 0.095 | ⚠ within organs, on part of the lines; also absent: MIR9-3HG, PCDH10, PLEKHG4B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.762). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.2, 28.2); signed map (35.1, 13.8). **Vector** length 42.0, 5.03% of its response variance represented; |z| ≥ 3 in 912 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +15.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +2.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -0.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | +1.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -1.1 | -1.7 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.2 — chr6:39,329,990-39,725,408 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1043E3.1, MGC33317, dJ137F1.4, dJ188D3.1, DKFZp451I2418; previously C6orf102 |
| Gene groups (HGNC) | Kinesins |
| Reactome | 8 pathways, smallest: Kinesins; COPI-dependent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

UniProt [Q6ZMV9](https://www.uniprot.org/uniprotkb/Q6ZMV9) carries no function annotation.

**Summary**, from NCBI Gene [221458](https://www.ncbi.nlm.nih.gov/gene/221458):

> This gene encodes a member of a family of molecular motors which are involved in intracellular transport of protein complexes, membrane organelles, and messenger ribonucleic acid along microtubules. Kinesins function as homodimeric molecules with two N-terminal head domains that move along microtubules and two C-terminal tail domains that interact with the transported cargo, either directly or indirectly, through adapter molecules. This gene is ubiquitously expressed in coronary arteries and …

**Accessions** — [HGNC:21202](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21202) · Entrez [221458](https://www.ncbi.nlm.nih.gov/gene/221458) · UniProt [Q6ZMV9](https://www.uniprot.org/uniprotkb/Q6ZMV9) · Ensembl [ENSG00000164627](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164627)

## Data

Gene col 8976: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8976); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8976, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8976]; `tensor/DDL_lfc|DDL_z.npy` [8976]; `embed/gene_vectors.npy` [8976]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8976 or target_col == 8976). Every well: [[KIF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
