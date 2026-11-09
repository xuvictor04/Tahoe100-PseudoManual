---
symbol: "PLPP6"
type: "gene"
col: 13013
ensembl_id: "ENSG00000205808"
name: "phospholipid phosphatase 6"
location: "9p24.1"
module: 7
arm: "+"
pooled_cpm: 2.15
n_lines_expressing: 48
n_dd_up: 7
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# PLPP6

*phospholipid phosphatase 6* — 9p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.68× (z +7.5, q 3e-11, up in 0 of 0 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.78× (z +6.5, q 2e-08, up in 12 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.437× (z -6.6, q 3e-08, down in 25 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL20-AS1]] (+0.73, fdr 7e-06), [[HERPUD2-AS1]] (+0.68, fdr 7e-06), [[HPS6]] (+0.67, fdr 7e-06); moves opposite to [[SLC31A1]] (-0.48, fdr 3e-05), [[SEPTIN2]] (-0.47, fdr 4e-05), [[ODF2]] (-0.47, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13013.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.68×** | +7.5 | 3e-11 | 0/0 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.78×** | +6.5 | 2e-08 | 12/40 (NCI-H460, A498, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.31×** | +6.2 | 1e-07 | 1/1 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +4.3 | 0.002 | 2/11 (LS 180, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.045 | 6/43 (A498, A549, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.31×** | +3.5 | 0.045 | 2/2 (LoVo, HEC-1-A) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.50×** | +3.2 | 0.095 | 8/34 (HT-29, RKO, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.51× | +3.1 | 0.12 | 6/34 (PANC-1, NCI-H1573, …) | rises with dose | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.75× | +3.1 | 0.13 | 6/13 (LoVo, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13013.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.437×** | -6.6 | 3e-08 | 25/43 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.569×** | -4.5 | 0.002 | 17/38 (LoVo, A-427, …) | two highest doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.573×** | -4.4 | 0.002 | 13/37 (LoVo, HT-29, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.695×** | -4.1 | 0.006 | 15/27 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.650×** | -3.4 | 0.062 | 11/36 (MIA PaCa-2, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.635×** | -3.4 | 0.062 | 13/29 (HT-29, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.682× | -3.0 | 0.19 | 6/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13013. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 5.01 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -10.1) |
| [[A-172 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.659 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.764 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.948 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.617 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.660 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13013), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL20-AS1]] | +0.73 | +0.72 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[HERPUD2-AS1]] | +0.68 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[HPS6]] | +0.67 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[B3GALT9]] | +0.65 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[SFT2D3]] | +0.65 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[DDX28]] | +0.64 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[ZNF629]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[B3GALT6]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[TMEM250]] | +0.61 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[TTC30A]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[MED11]] | +0.60 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[MOCS3]] | +0.59 | +0.56 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC31A1]] | -0.48 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[SEPTIN2]] | -0.47 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[ODF2]] | -0.47 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[KDELR2]] | -0.47 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[TTC3]] | -0.46 | -0.48 / -0.37 | both halves | 7e-05 |  |
| [[VDAC1P8]] | -0.46 | -0.35 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises PLPP6's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[EID2]] | C | EID2 activity raises PLPP6's level | lines that do not express EID2 (3) vs lines expressing it (47) | 2.04× lower at baseline in the lines without EID2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, ITPR2-AS1, ENSG00000261341; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.499). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-36.4, 17.9); signed map (-1.8, -30.6). **Vector** length 38.0, 4.32% of its response variance represented; |z| ≥ 3 in 847 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.7 | +6.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | +0.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.5 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +2.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.0 | +2.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -1.6 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.5 | -3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.1 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -4.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -1.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -1.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -1.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -0.8 | -2.4 |
|  | [[Tomivosertib (drug)]] 5 µM |  | -0.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | phospholipid phosphatase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.1 — chr9:4,662,294-4,665,258 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ90191, FLJ46512, PDP1; previously PPAPDC2 |
| Gene groups (HGNC) | Phospholipid phosphatases |
| Reactome | 4 pathways, smallest: Lanosterol biosynthesis; Cholesterol biosynthesis; Metabolism of steroids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IY26](https://www.uniprot.org/uniprotkb/Q8IY26) (Polyisoprenoid diphosphate/phosphate phosphohydrolase PLPP6):

> Magnesium-independent polyisoprenoid diphosphatase that catalyzes the sequential dephosphorylation of presqualene, farnesyl, geranyl and geranylgeranyl diphosphates. Functions in the innate immune response through the dephosphorylation of presqualene diphosphate which acts as a potent inhibitor of the signaling pathways contributing to polymorphonuclear neutrophils activation. May regulate the biosynthesis of cholesterol and related sterols by dephosphorylating presqualene and farnesyl …

**Summary**, from NCBI Gene [403313](https://www.ncbi.nlm.nih.gov/gene/403313):

> Enables isoprenoid diphosphate phosphatase activity and phosphatase activity. Involved in several processes, including phospholipid dephosphorylation; phospholipid metabolic process; and positive regulation of neutrophil activation. Located in endoplasmic reticulum membrane and nuclear membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23682](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23682) · Entrez [403313](https://www.ncbi.nlm.nih.gov/gene/403313) · UniProt [Q8IY26](https://www.uniprot.org/uniprotkb/Q8IY26) · Ensembl [ENSG00000205808](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205808)

## Data

Gene col 13013: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13013); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13013, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13013]; `tensor/DDL_lfc|DDL_z.npy` [13013]; `embed/gene_vectors.npy` [13013]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13013 or target_col == 13013). Every well: [[PLPP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLPP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
