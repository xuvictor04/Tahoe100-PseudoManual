---
symbol: "MAP1LC3B2"
type: "gene"
col: 15086
ensembl_id: "ENSG00000258102"
name: "microtubule associated protein 1 light chain 3 beta 2"
location: "12q24.22"
module: 150
arm: "+"
pooled_cpm: 4.04
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 20
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/150"]
generated_by: "tahoemap"
---

# MAP1LC3B2

*microtubule associated protein 1 light chain 3 beta 2* — 12q24.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.26× (z +16.5, q 0e+00, up in 35 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Doxycycline (monohydrate) (drug)]] 5 µM: 0.673× (z -3.8, q 0.081, down in 9 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRID2]] (+0.63, fdr 1e-05), [[PACRG]] (+0.62, fdr 7e-06), [[SYNM-AS1]] (+0.61, fdr 1e-05); moves opposite to [[INO80E]] (-0.54, fdr 5e-05), [[ORC5]] (-0.51, fdr 6e-05), [[AGK]] (-0.49, fdr 1e-04).
> It is in [[Module 150]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15086.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.26×** | +16.5 | 0e+00 | 35/38 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.22×** | +11.2 | 2e-26 | 22/39 (NCI-H1573, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.93×** | +10.2 | 3e-22 | 3/7 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.78×** | +10.1 | 7e-22 | 31/43 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +9.0 | 2e-17 | 13/22 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.43×** | +8.8 | 1e-16 | 32/46 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.59×** | +8.7 | 2e-16 | 7/10 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.77×** | +8.0 | 1e-13 | 23/45 (NCI-H460, CFPAC-1, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.09×** | +7.3 | 2e-11 | 26/46 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.78×** | +5.7 | 8e-07 | 18/46 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.68×** | +5.1 | 2e-05 | 7/45 (SK-MEL-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.65×** | +4.9 | 4e-05 | 15/46 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +4.9 | 4e-05 | 16/41 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.63×** | +4.8 | 6e-05 | 11/44 (NCI-H2030, MIA PaCa-2, …) | two highest doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +4.7 | 1e-04 | 9/33 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +4.6 | 2e-04 | 12/45 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.4 | 3e-04 | 10/46 (HOP62, SW1417, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +4.2 | 9e-04 | 11/38 (SW1417, HOP62, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +4.0 | 0.002 | 14/38 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15086.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | **0.673×** | -3.8 | 0.081 | 9/43 (AsPC-1, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15086. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 7.38 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 3.77× (z +13.7) ⚠ position not correctable | — |
| [[PANC-1 (line)]] | alt | 4.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +8.7) | — |
| [[A-172 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15086), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRID2]] | +0.63 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[PACRG]] | +0.62 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[SYNM-AS1]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CSMD1]] | +0.59 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.59 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[SNAP25-AS1]] | +0.58 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[RYR1]] | +0.57 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[NDUFV2-AS1]] | +0.56 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[GSTM3]] | +0.56 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[SPTBN4]] | +0.56 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[ATP8A2]] | +0.56 | +0.42 / +0.67 | both halves | 4e-05 |  |
| [[CDH23]] | +0.55 | +0.50 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INO80E]] | -0.54 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[ORC5]] | -0.51 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[AGK]] | -0.49 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[LCLAT1]] | -0.48 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[PDSS1]] | -0.48 | -0.38 / -0.41 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MAP1LC3B2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00173]] | B | LINC00173 activity raises MAP1LC3B2's level | lines that do not express LINC00173 (18) vs lines expressing it (32) | 1.48× lower at baseline in the lines without LINC00173 | 0.056 | ⚠ within organs, on part of the lines; also absent: GBX1, RAB3C, NOVA2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 150]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.560). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.4, 31.4); signed map (30.6, 10.6). **Vector** length 52.6, 6.67% of its response variance represented; |z| ≥ 3 in 1,019 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +16.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +10.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +4.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +0.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +0.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -0.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +2.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -0.5 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.2 | -2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated protein 1 light chain 3 beta 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.22 — chr12:116,548,105-116,576,606 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ATG8G |
| Gene groups (HGNC) | Autophagy related; Microtubule associated protein 1 light chain 3 family |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NCE7](https://www.uniprot.org/uniprotkb/A6NCE7) (Microtubule-associated protein 1 light chain 3 beta 2):

> Ubiquitin-like modifier involved in formation of autophagosomal vacuoles (autophagosomes). Plays a role in mitophagy which contributes to regulate mitochondrial quantity and quality by eliminating the mitochondria to a basal level to fulfill cellular energy requirements and preventing excess ROS production. In response to cellular stress and upon mitochondria fission, binds C-18 ceramides and anchors autophagolysosomes to outer mitochondrial membranes to eliminate damaged mitochondria. While …

**Summary**, from NCBI Gene [643246](https://www.ncbi.nlm.nih.gov/gene/643246):

> Predicted to enable microtubule binding activity; phosphatidylethanolamine binding activity; and ubiquitin protein ligase binding activity. Predicted to be involved in cellular response to nitrogen starvation and macroautophagy. Predicted to be located in several cellular components, including autophagosome; cytoplasmic vesicle; and microtubule. Predicted to be active in autophagosome membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:34390](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34390) · Entrez [643246](https://www.ncbi.nlm.nih.gov/gene/643246) · UniProt [A6NCE7](https://www.uniprot.org/uniprotkb/A6NCE7) · Ensembl [ENSG00000258102](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258102)

## Data

Gene col 15086: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15086); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15086, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15086]; `tensor/DDL_lfc|DDL_z.npy` [15086]; `embed/gene_vectors.npy` [15086]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15086 or target_col == 15086). Every well: [[MAP1LC3B2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP1LC3B2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
