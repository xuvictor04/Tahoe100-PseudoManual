---
symbol: "GALNTL6"
type: "gene"
col: 10497
ensembl_id: "ENSG00000174473"
name: "polypeptide N-acetylgalactosaminyltransferase like 6"
location: "4q34.1"
module: 140
arm: "+"
pooled_cpm: 3.68
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# GALNTL6

*polypeptide N-acetylgalactosaminyltransferase like 6* — 4q34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.61× (z +29.3, q 0e+00, up in 32 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Clofarabine (drug)]] 0.5 µM in 1 line (SNU-423 0.0539×); [[Isocorydine (drug)]] 0.5 µM in 1 line (SW480 0.0716×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC4C]] (+0.85, fdr 7e-06), [[THSD7B]] (+0.83, fdr 7e-06), [[LINC00861]] (+0.82, fdr 7e-06).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10497.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.61×** | +29.3 | 0e+00 | 32/35 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.30×** | +17.2 | 0e+00 | 28/36 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **4.73×** | +15.9 | 0e+00 | 33/40 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.08×** | +14.4 | 1e-44 | 10/13 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.79×** | +12.6 | 4e-34 | 5/8 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.05×** | +10.9 | 7e-26 | 3/4 (NCI-H2347, HOP62, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.96×** | +9.7 | 2e-20 | 27/45 (NCI-H1573, NCI-H2030, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +7.9 | 3e-13 | 18/37 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.65×** | +7.2 | 3e-11 | 15/45 (A549, A498, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.09×** | +7.2 | 3e-11 | 16/31 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.02×** | +6.9 | 3e-10 | 18/41 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +5.8 | 3e-07 | 13/33 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +5.3 | 5e-06 | 15/37 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +5.0 | 2e-05 | 14/39 (NCI-H1573, LOX-IMVI, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +4.6 | 2e-04 | 6/44 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +3.6 | 0.008 | 5/39 (HOP62, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.041 | 4/41 (NCI-H23, A-427, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.043 | 5/42 (KATO III, SNU-423, …) | two highest doses | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10497.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Clofarabine (drug)]] 0.5 µM in 1 line (SNU-423 0.0539×); [[Isocorydine (drug)]] 0.5 µM in 1 line (SW480 0.0716×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.892× | -4.1 | 0.027 | 10/48 (A549, A-427, …) | inconsistent across doses |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 0.723× | -3.1 | 0.47 | 9/39 (NCI-H1792, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10497. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 10.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.14× (z +11.6) | — |
| [[A-172 (line)]] | wt | 3.62 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.6× (z +11.8) | — |
| [[A498 (line)]] | wt | 1.72 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +11.9) | — |
| [[HEC-1-A (line)]] | alt | 5.69 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.85× (z +12.0) | — |
| [[LoVo (line)]] | wt | 2.45 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.8× (z +12.9) | — |
| [[SW480 (line)]] | alt | 1.80 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +12.6) | [[Isocorydine (drug)]] 0.5 µM 0.0716× (z -9.0) |
| [[A549 (line)]] | wt | 2.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.1× (z +11.6) | — |
| [[C32 (line)]] | wt | 3.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 2.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.9× (z +11.7) | — |
| [[KATO III (line)]] | alt | 2.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 2.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.6× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 2.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.70× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 2.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +11.3) | — |
| [[PANC-1 (line)]] | alt | 1.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 6.55 | 0 | 1 | — | [[Clofarabine (drug)]] 0.5 µM 0.0539× (z -9.3) |
| [[A-427 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10497), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC4C]] | +0.85 | +0.76 / +0.83 | both halves | 7e-06 |  |
| [[THSD7B]] | +0.83 | +0.76 / +0.81 | both halves | 7e-06 | pathway: O-linked glycosylation |
| [[LINC00861]] | +0.82 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[C8orf34]] | +0.81 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.81 | +0.76 / +0.83 | both halves | 7e-06 |  |
| [[GRIA4]] | +0.80 | +0.74 / +0.80 | both halves | 7e-06 |  |
| [[SCHLAP1]] | +0.80 | +0.73 / +0.85 | both halves | 7e-06 |  |
| [[SLC27A6]] | +0.80 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[USH2A]] | +0.80 | +0.73 / +0.83 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.80 | +0.79 / +0.88 | both halves | 7e-06 |  |
| [[FAT3]] | +0.79 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[LINC02208]] | +0.79 | +0.77 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GALNTL6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HTR2C]] | B | HTR2C activity raises GALNTL6's level | lines that do not express HTR2C (22) vs lines expressing it (28) | 1.58× lower at baseline in the lines without HTR2C | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, KCNJ6, PTPRN; maybe low, not absent |
| [[CD70]] | B | CD70 activity raises GALNTL6's level | lines that do not express CD70 (21) vs lines expressing it (29) | 1.38× lower at baseline in the lines without CD70 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, MEG8, MEG3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.879). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.3, 28.8); signed map (32.9, 14.3). **Vector** length 63.9, 9.91% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.1 | +29.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.6 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +14.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +17.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +5.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.6 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.1 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -4.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +0.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -1.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -2.0 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | polypeptide N-acetylgalactosaminyltransferase like 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q34.1 — chr4:171,812,254-173,041,559 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GALNT17, GalNAc-T6L |
| Gene groups (HGNC) | Polypeptide N-acetylgalactosaminyltransferases |
| Reactome | 2 pathways, smallest: O-linked glycosylation of mucins; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q49A17](https://www.uniprot.org/uniprotkb/Q49A17) (Polypeptide N-acetylgalactosaminyltransferase-like 6):

> Catalyzes the initial reaction in O-linked oligosaccharide biosynthesis, the transfer of an N-acetyl-D-galactosamine residue to a serine or threonine residue on the protein receptor.

**Summary**, from NCBI Gene [442117](https://www.ncbi.nlm.nih.gov/gene/442117):

> Enables polypeptide N-acetylgalactosaminyltransferase activity. Involved in protein O-linked glycosylation via N-acetyl-galactosamine. Predicted to be located in Golgi membrane. Predicted to be active in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:33844](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33844) · Entrez [442117](https://www.ncbi.nlm.nih.gov/gene/442117) · UniProt [Q49A17](https://www.uniprot.org/uniprotkb/Q49A17) · Ensembl [ENSG00000174473](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174473)

## Data

Gene col 10497: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10497); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10497, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10497]; `tensor/DDL_lfc|DDL_z.npy` [10497]; `embed/gene_vectors.npy` [10497]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10497 or target_col == 10497). Every well: [[GALNTL6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALNTL6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
