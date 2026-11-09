---
symbol: "FGF1"
type: "gene"
col: 3475
ensembl_id: "ENSG00000113578"
name: "fibroblast growth factor 1"
location: "5q31.3"
module: 116
arm: "+"
pooled_cpm: 3.11
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# FGF1

*fibroblast growth factor 1* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.92× (z +10.0, q 1e-20, up in 10 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.73× (z +7.2, q 9e-11, up in 18 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.663× (z -3.8, q 0.071, down in 11 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.270×; ⚠ position not correctable); [[Cobimetinib (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0679×); [[Harringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.123×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZPLD1]] (+0.69, fdr 7e-06), [[LTBP2]] (+0.69, fdr 7e-06), [[LINC01204]] (+0.68, fdr 7e-06).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[RGS4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3475.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.92×** | +10.0 | 1e-20 | 10/15 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.79×** | +9.2 | 1e-17 | 4/5 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +7.2 | 9e-11 | 18/32 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.26×** | +7.0 | 4e-10 | 4/6 (LOX-IMVI, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.44×** | +4.3 | 0.002 | 3/7 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.39×** | +4.3 | 0.002 | 10/33 (LoVo, RPMI-7951, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +4.2 | 0.002 | 5/24 (NCI-H2030, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.09×** | +3.6 | 0.024 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.49×** | +3.6 | 0.024 | 10/43 (A-172, NCI-H460, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **2.06×** | +3.5 | 0.025 | 2/17 (LOX-IMVI, SNU-423) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.028 | 8/44 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.65×** | +3.3 | 0.041 | 5/27 (MIA PaCa-2, A-172, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3475.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.270×; ⚠ position not correctable); [[Cobimetinib (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0679×); [[Harringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.123×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.663×** | -3.8 | 0.071 | 11/45 (SK-MEL-2, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.909× | -3.5 | 0.094 | 14/47 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.734×** | -3.5 | 0.094 | 8/44 (MIA PaCa-2, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.684× | -3.3 | 0.12 | 12/44 (HepG2/C3A, MIA PaCa-2, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.783× | -3.2 | 0.12 | 12/44 (PANC-1, A-172, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | 0.748× | -3.2 | 0.12 | 7/45 (MIA PaCa-2, SHP-77, …) | rises with dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Penfluridol (drug)]] 5 µM |  | 0.701× | -3.2 | 0.12 | 7/41 (hTERT-HPNE, A549, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.723× | -3.0 | 0.17 | 7/44 (RPMI-7951, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3475. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 11.4 | 0 | 3 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.270× (z -19.1) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 0.0679× (z -10.8) |
| [[HS-578T (line)]] | alt | 2.96 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0507× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3475), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZPLD1]] | +0.69 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[LTBP2]] | +0.69 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[LINC01204]] | +0.68 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[DELEC1]] | +0.66 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[CCDC190]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[ROBO4]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[PLXNA4]] | +0.64 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[DIRC3-AS1]] | +0.63 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ADAMTSL1]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[LINC01592]] | +0.61 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[DOCK2]] | +0.60 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[MARCHF4]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGS4]] | B | RGS4 activity raises FGF1's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 1.77× lower at baseline in the lines without RGS4 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486 |
| [[ROBO4]] | B | ROBO4 activity raises FGF1's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 1.78× lower at baseline in the lines without ROBO4 | 0.025 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[LINC01151]] | B | LINC01151 activity raises FGF1's level | lines that do not express LINC01151 (19) vs lines expressing it (31) | 1.51× lower at baseline in the lines without LINC01151 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, DNER, ENSG00000225330; maybe low, not absent |
| [[LINC01812]] | B | LINC01812 activity raises FGF1's level | lines that do not express LINC01812 (35) vs lines expressing it (15) | 1.48× lower at baseline in the lines without LINC01812 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235495, ENSG00000224865, ENSG00000287622 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.702). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.9, 10.9); signed map (14.0, 45.4). **Vector** length 53.2, 6.82% of its response variance represented; |z| ≥ 3 in 1,009 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +4.7 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +2.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.6 | +3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.5 | +3.6 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -3.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -3.5 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.4 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | fibroblast growth factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:142,592,178-142,698,070 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AFGF, ECGF, ECGFA, ECGFB, HBGF1, ECGF-beta, FGF-alpha, GLIO703; previously FGFA |
| Gene groups (HGNC) | Receptor ligands; Fibroblast growth factor family |
| Reactome | 68 pathways, smallest: FGFR2b ligand binding and activation; FGFR1b ligand binding and activation; FGFR3b ligand binding and activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P05230](https://www.uniprot.org/uniprotkb/P05230) (Fibroblast growth factor 1):

> Plays an important role in the regulation of cell survival, cell division, angiogenesis, cell differentiation and cell migration. Functions as a potent mitogen in vitro. Acts as a ligand for FGFR1 and integrins. Binds to FGFR1 in the presence of heparin leading to FGFR1 dimerization and activation via sequential autophosphorylation on tyrosine residues which act as docking sites for interacting proteins, leading to the activation of several signaling cascades. Binds to integrin ITGAV:ITGB3. Its …

**Summary**, from NCBI Gene [2246](https://www.ncbi.nlm.nih.gov/gene/2246):

> The protein encoded by this gene is a member of the fibroblast growth factor (FGF) family. FGF family members possess broad mitogenic and cell survival activities, and are involved in a variety of biological processes, including embryonic development, cell growth, morphogenesis, tissue repair, tumor growth and invasion. This protein functions as a modifier of endothelial cell migration and proliferation, as well as an angiogenic factor. It acts as a mitogen for a variety of mesoderm- and …

**Accessions** — [HGNC:3665](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3665) · Entrez [2246](https://www.ncbi.nlm.nih.gov/gene/2246) · UniProt [P05230](https://www.uniprot.org/uniprotkb/P05230) · Ensembl [ENSG00000113578](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113578)

## Data

Gene col 3475: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3475); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3475, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3475]; `tensor/DDL_lfc|DDL_z.npy` [3475]; `embed/gene_vectors.npy` [3475]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3475 or target_col == 3475). Every well: [[FGF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
