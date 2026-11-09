---
symbol: "DUSP23"
type: "gene"
col: 8185
ensembl_id: "ENSG00000158716"
name: "dual specificity phosphatase 23"
location: "1q23.2"
module: 58
arm: "+"
pooled_cpm: 8.1
n_lines_expressing: 36
n_dd_up: 5
n_dd_down: 6
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# DUSP23

*dual specificity phosphatase 23* — 1q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.14× (z +7.8, q 5e-12, up in 20 of 23 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.463× (z -5.9, q 2e-06, down in 23 of 29 measured lines).
> Its strongest partners by |cos| (68 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 37 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAC3]] (+0.69, fdr 2e-05), [[MICOS13]] (+0.68, fdr 7e-05), [[POLR2I]] (+0.66, fdr 3e-04); moves opposite to [[TUG1]] (-0.56, fdr 5e-04), [[EIF4G2]] (-0.55, fdr 8e-04, ⚠ one half only (not replicated)), [[U2AF2]] (-0.55, fdr 0.002, ⚠ one half only (not replicated)), [[ERAP1]] (-0.54, fdr 5e-04), [[ELK4]] (-0.54, fdr 1e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → [[ERAP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 8 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8185.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **4.14×** | +7.8 | 5e-12 | 20/23 (NCI-H1573, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.55×** | +6.7 | 8e-09 | 9/11 (A498, J82, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.21×** | +4.3 | 0.003 | 23/33 (NCI-H1573, HOP62, …) | all doses, flat | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **2.15×** | +4.2 | 0.004 | 16/22 (A-427, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +3.9 | 0.013 | 13/27 (NCI-H2030, A498, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | 1.88× | +3.2 | 0.13 | 9/16 (NCI-H1573, A498, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 1.76× | +3.1 | 0.15 | 11/33 (HOP62, A-172, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | 1.78× | +3.0 | 0.16 | 11/28 (NCI-H1573, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8185.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.463×** | -5.9 | 2e-06 | 23/29 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.213×** | -4.4 | 0.002 | 24/29 (C32, NCI-H23, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.446×** | -4.4 | 0.002 | 22/33 (SW1417, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.518×** | -3.6 | 0.050 | 18/33 (KATO III, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.533×** | -3.4 | 0.071 | 16/28 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.307×** | -3.4 | 0.073 | 18/31 (NCI-H23, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.561× | -3.1 | 0.14 | 14/32 (NCI-H1792, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8185. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 105 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0982× (z -14.5) |
| [[NCI-H2030 (line)]] | alt | 18.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -12.0) |
| [[PANC-1 (line)]] | alt | 5.92 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0790× (z -14.1) |
| [[A-172 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.615 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.843 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.528 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.826 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.86 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8185), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 34 of them with an alert (⚠; 29 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAC3]] | +0.69 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[MICOS13]] | +0.68 | +0.37 / +0.67 | both halves | 7e-05 |  |
| [[POLR2I]] | +0.66 | +0.28 / +0.64 | both halves | 3e-04 |  |
| [[MTLN]] ⚠ | +0.66 | +0.35 / +0.71 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[OCEL1]] | +0.65 | +0.34 / +0.60 | both halves | 1e-04 |  |
| [[ANTKMT]] | +0.65 | +0.35 / +0.59 | both halves | 1e-04 |  |
| [[MRPL41]] ⚠ | +0.63 | +0.25 / +0.63 | both halves | 4e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[TRAPPC5]] | +0.63 | +0.29 / +0.64 | both halves | 2e-04 |  |
| [[MT1X]] | +0.62 | +0.36 / +0.61 | both halves | 1e-04 |  |
| [[C4orf48]] | +0.62 | +0.25 / +0.65 | both halves | 4e-04 |  |
| [[ATP5F1D]] ⚠ | +0.61 | +0.29 / +0.58 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM256]] | +0.61 | +0.27 / +0.58 | both halves | 3e-04 |  |
| [[RPP21]] | +0.61 | +0.29 / +0.64 | both halves | 3e-04 |  |
| [[FAM222B]] | +0.61 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[TMEM276]] | +0.61 | +0.37 / +0.57 | both halves | 8e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUG1]] | -0.56 | -0.23 / -0.56 | both halves | 5e-04 |  |
| [[EIF4G2]] | -0.55 | -0.19 / -0.52 | ⚠ one half (not replicated) | 8e-04 |  |
| [[U2AF2]] | -0.55 | -0.11 / -0.57 | ⚠ one half (not replicated) | 0.002 |  |
| [[ERAP1]] | -0.54 | -0.24 / -0.54 | both halves | 5e-04 |  |
| [[ELK4]] | -0.54 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[SDCBP2-AS1]] | -0.53 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[MOB1A]] | -0.53 | -0.23 / -0.59 | both halves | 5e-04 |  |
| [[PRKAR1A]] | -0.53 | -0.24 / -0.50 | both halves | 5e-04 |  |
| [[PSME3IP1]] | -0.52 | -0.23 / -0.47 | both halves | 5e-04 |  |
| [[LINC01355]] | -0.51 | -0.24 / -0.46 | both halves | 5e-04 |  |
| [[FGD5-AS1]] | -0.51 | -0.19 / -0.52 | ⚠ one half (not replicated) | 8e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERAP1]] | B | DUSP23 activity raises ERAP1's level | lines that do not express DUSP23 (14) vs lines expressing it (36) | 1.55× lower at baseline in the lines without DUSP23 | 0.088 | ⚠ within organs, on part of the lines; also absent: HLA-F, SH2D4A, RARRES1 |
| cells under [[palbociclib (drug)]] 5 µM | B | DUSP23 activity raises the cells' numbers under palbociclib 5 µM (protects the cells) | lines that do not express DUSP23 (14) vs lines expressing it (34) | the lines without DUSP23: 0.80× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: HLA-F, SH2D4A, RARRES1 |
| cells under [[Gemcitabine (drug)]] 5 µM | B | DUSP23 activity raises the cells' numbers under Gemcitabine 5 µM (protects the cells) | lines that do not express DUSP23 (14) vs lines expressing it (34) | the lines without DUSP23: 0.85× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: HLA-F, SH2D4A, RARRES1 |

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.718). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-46.1, -15.1); signed map (-32.9, 5.7). **Vector** length 54.2, 13.4% of its response variance represented; |z| ≥ 3 in 468 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +2.6 | +4.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +2.2 | +3.1 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.7 | +1.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.6 | +1.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.4 | +2.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.4 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.0 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -3.6 |
|  | [[Ivermectin (drug)]] 5 µM |  | -1.1 | -2.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | dual specificity phosphatase 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.2 — chr1:159,780,932-159,782,543 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20442, DUSP25 |
| Gene groups (HGNC) | Atypical dual specificity phosphatases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVJ7](https://www.uniprot.org/uniprotkb/Q9BVJ7) (Dual specificity protein phosphatase 23):

> Protein phosphatase that mediates dephosphorylation of proteins phosphorylated on Tyr and Ser/Thr residues. In vitro, it can dephosphorylate p44-ERK1 (MAPK3) but not p54 SAPK-beta (MAPK10) in vitro. Able to enhance activation of JNK and p38 (MAPK14).

**Summary**, from NCBI Gene [54935](https://www.ncbi.nlm.nih.gov/gene/54935):

> Enables protein tyrosine/serine/threonine phosphatase activity. Involved in dephosphorylation. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21480](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21480) · Entrez [54935](https://www.ncbi.nlm.nih.gov/gene/54935) · UniProt [Q9BVJ7](https://www.uniprot.org/uniprotkb/Q9BVJ7) · Ensembl [ENSG00000158716](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158716)

## Data

Gene col 8185: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8185); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8185, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8185]; `tensor/DDL_lfc|DDL_z.npy` [8185]; `embed/gene_vectors.npy` [8185]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8185 or target_col == 8185). Every well: [[DUSP23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUSP23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
