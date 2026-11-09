---
symbol: "NKAIN3"
type: "gene"
col: 11755
ensembl_id: "ENSG00000185942"
name: "sodium/potassium transporting ATPase interacting 3"
location: "8q12.3"
module: 9
arm: "+"
pooled_cpm: 34.18
n_lines_expressing: 16
n_dd_up: 31
n_dd_down: 1
n_dd_up_clean: 21
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# NKAIN3

*sodium/potassium transporting ATPase interacting 3* — 8q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.08× (z +24.7, q 0e+00, up in 10 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.739× (z -3.8, q 0.097, down in 3 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EGFEM1P]] (+0.63, fdr 1e-05), [[HMCN1]] (+0.61, fdr 1e-05), [[PIEZO2]] (+0.59, fdr 1e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11755.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.08×** | +24.7 | 0e+00 | 10/14 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.04×** | +13.8 | 7e-41 | 3/13 (NCI-H1792, SW480, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.08×** | +12.9 | 1e-35 | 13/14 (SW 900, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.98×** | +12.5 | 8e-34 | 10/13 (A549, C32, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.97×** | +11.9 | 2e-30 | 6/14 (J82, SW 900, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +9.1 | 1e-17 | 6/14 (SW 900, HS-578T, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +8.8 | 9e-17 | 5/13 (NCI-H1792, C32, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.88×** | +7.8 | 3e-13 | 8/14 (C32, NCI-H1792, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.56×** | +7.8 | 4e-13 | 7/14 (J82, A549, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.86×** | +7.7 | 8e-13 | 9/14 (NCI-H2030, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.84×** | +7.6 | 2e-12 | 7/14 (A549, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.73×** | +6.5 | 3e-09 | 6/14 (SW 900, J82, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +6.5 | 4e-09 | 5/14 (HS-578T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +5.9 | 2e-07 | 7/14 (NCI-H23, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +5.6 | 1e-06 | 5/14 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.44×** | +4.3 | 5e-04 | 5/14 (NCI-H23, A549, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.002 | 2/14 (J82, HS-578T) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +3.8 | 0.004 | 8/14 (NCI-H1792, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.005 | 4/14 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11755.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.739×** | -3.8 | 0.097 | 3/14 (SW 900, HS-578T, …) | all doses, flat |  |
| [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | 0.770× | -3.3 | 0.20 | 0/14 | inconsistent across doses |  |
| [[Quinestrol (drug)]] 5 µM |  | 0.836× | -3.2 | 0.20 | 1/14 (H4) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | 0.776× | -3.2 | 0.20 | 3/14 (HS-578T, SW 900, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.781× | -3.1 | 0.21 | 3/14 (HS-578T, SW 900, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11755. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 9.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 14.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +11.8) | — |
| [[A-172 (line)]] | wt | 3.31 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.53 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.58 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.82 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.30 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.41 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1,106 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.31 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.32 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 7.28 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.26 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.11 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.51 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.68 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.63 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 43.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11755), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGFEM1P]] | +0.63 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[HMCN1]] | +0.61 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[PIEZO2]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ZNF804A]] | +0.59 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[FMN2]] | +0.58 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[ADAMTS3]] | +0.57 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[EPHA5]] | +0.57 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[LINC01695]] | +0.57 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[LINC02328]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[CDH18]] | +0.57 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[NTNG1]] | +0.57 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[NOVA1]] | +0.56 | +0.59 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 1, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NKAIN3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EPHA5]] | C | EPHA5 activity raises NKAIN3's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 3.23× lower at baseline in the lines without EPHA5 | 0.042 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[ATRNL1]] | C | ATRNL1 activity raises NKAIN3's level | lines that do not express ATRNL1 (21) vs lines expressing it (29) | 2.50× lower at baseline in the lines without ATRNL1 | 0.051 | ⚠ within organs, on part of the lines; also absent: CAMK4, BVES, NEGR1; maybe low, not absent; co-absent with the target |
| [[EPHA5-AS1]] | C | EPHA5-AS1 activity raises NKAIN3's level | lines that do not express EPHA5-AS1 (28) vs lines expressing it (22) | 3.10× lower at baseline in the lines without EPHA5-AS1 | 0.062 | ⚠ within organs, on part of the lines; also absent: EPHA5, ADAM23, TRPC4; co-absent with the target |
| [[FGF14]] | C | FGF14 activity raises NKAIN3's level | lines that do not express FGF14 (28) vs lines expressing it (22) | 2.03× lower at baseline in the lines without FGF14 | 0.075 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, PTPRD, KCNT2; co-absent with the target |
| [[NTNG2]] | C | NTNG2 activity raises NKAIN3's level | lines that do not express NTNG2 (19) vs lines expressing it (31) | 2.49× lower at baseline in the lines without NTNG2 | 0.091 | ⚠ within organs, on part of the lines; also absent: FSD1, ANTXR1, RASSF8; co-absent with the target |
| [[SOX5]] | C | SOX5 activity raises NKAIN3's level | lines that do not express SOX5 (24) vs lines expressing it (26) | 2.28× lower at baseline in the lines without SOX5 | 0.093 | ⚠ within organs, on part of the lines; also absent: CTHRC1, MOXD1, AK5; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.598). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.2, 29.5); signed map (39.9, 31.0). **Vector** length 46.6, 14.4% of its response variance represented; |z| ≥ 3 in 366 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +24.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +13.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +12.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +12.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +7.8 |
|  | [[EX229 (drug)]] 5 µM |  | +1.2 | +2.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +0.8 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -3.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.4 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | sodium/potassium transporting ATPase interacting 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q12.3 — chr8:62,248,591-63,014,000 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ39630; previously FAM77D, NKAIN3-IT1 |
| Gene groups (HGNC) | Na+/K+ transporting ATPase interacting |
| Matched by | ensembl_id |

UniProt [Q8N8D7](https://www.uniprot.org/uniprotkb/Q8N8D7) carries no function annotation.

**Summary**, from NCBI Gene [286183](https://www.ncbi.nlm.nih.gov/gene/286183):

> NKAIN3 is a member of a family of mammalian proteins (see NKAIN1; MIM 612871) with similarity to Drosophila Nkain (Gorokhova et al., 2007 [PubMed 17606467]).[supplied by OMIM, Jun 2009]

**Accessions** — [HGNC:26829](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26829) · Entrez [286183](https://www.ncbi.nlm.nih.gov/gene/286183) · UniProt [Q8N8D7](https://www.uniprot.org/uniprotkb/Q8N8D7) · Ensembl [ENSG00000185942](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185942)

## Data

Gene col 11755: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11755); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11755, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11755]; `tensor/DDL_lfc|DDL_z.npy` [11755]; `embed/gene_vectors.npy` [11755]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11755 or target_col == 11755). Every well: [[NKAIN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NKAIN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
