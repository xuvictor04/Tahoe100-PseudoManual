---
symbol: "GPM6B"
type: "gene"
col: 506
ensembl_id: "ENSG00000046653"
name: "glycoprotein M6B"
location: "Xp22.2"
module: 102
arm: "+"
pooled_cpm: 4.43
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# GPM6B

*glycoprotein M6B* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.03× (z +14.7, q 0e+00, up in 13 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.58× (z +14.1, q 4e-43, up in 24 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 11 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.0789×; ⚠ cell-cycle shift, explains ~25% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.0491×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.202×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (AN3 CA 0.205×); [[PH-797804 (drug)]] 5 µM in 1 line (AN3 CA 0.0524×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NKAIN1]] (+0.66, fdr 7e-06), [[SPATA21]] (+0.64, fdr 1e-05), [[DLGAP2]] (+0.63, fdr 4e-05).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC01203]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 506.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.03×** | +14.7 | 0e+00 | 13/16 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.18×** | +14.5 | 3e-45 | 1/3 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.58×** | +14.1 | 4e-43 | 24/33 (A549, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.15×** | +11.2 | 5e-27 | 4/5 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +6.9 | 4e-10 | 20/44 (A-427, PANC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.68×** | +5.4 | 5e-06 | 1/13 (C32) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +4.9 | 9e-05 | 4/43 (C32, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.38×** | +4.8 | 1e-04 | 8/34 (LoVo, SHP-77, …) | top dose only | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.29×** | +4.6 | 3e-04 | 1/4 (C32) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +4.5 | 5e-04 | 13/35 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +4.1 | 0.002 | 2/14 (NCI-H1573, BT-474) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.8 | 0.007 | 8/34 (SK-MEL-2, C32, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.024 | 5/30 (SK-MEL-2, BT-474, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.036 | 1/21 (NCI-H2347) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.2 | 0.056 | 7/33 (A-427, C32, …) | top dose only | position effect removed |
| [[Saquinavir (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.065 | 3/36 (CFPAC-1, A-427, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 506.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 11 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.0789×; ⚠ cell-cycle shift, explains ~25% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.0491×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.202×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (AN3 CA 0.205×); [[PH-797804 (drug)]] 5 µM in 1 line (AN3 CA 0.0524×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.880× | -4.8 | 8e-04 | 13/47 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.754× | -3.0 | 0.72 | 2/44 (KATO III, SW 900) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 506. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 218 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0789× (z -20.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -13.2) |
| [[C32 (line)]] | wt | 58.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.11× (z +9.5) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 33.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.110× (z -10.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 7.89 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.411× (z -12.0) ⚠ position not correctable |
| [[A-172 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.98 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 506), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NKAIN1]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.64 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[DLGAP2]] | +0.63 | +0.42 / +0.75 | both halves | 4e-05 |  |
| [[USH2A]] | +0.62 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[SGCZ]] | +0.62 | +0.43 / +0.74 | both halves | 3e-05 |  |
| [[CDH23]] | +0.62 | +0.46 / +0.69 | both halves | 2e-05 |  |
| [[TP53TG5]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[CNTNAP5]] | +0.61 | +0.39 / +0.69 | both halves | 6e-05 |  |
| [[TMEM266]] | +0.61 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[LINC02511]] | +0.61 | +0.42 / +0.75 | both halves | 4e-05 |  |
| [[PTPRT]] | +0.61 | +0.43 / +0.69 | both halves | 3e-05 |  |
| [[GALNT17]] | +0.61 | +0.43 / +0.70 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01203]] | B | LINC01203 activity raises GPM6B's level | lines that do not express LINC01203 (37) vs lines expressing it (13) | 2.07× lower at baseline in the lines without LINC01203 | 0.024 | ⚠ within organs, on part of the lines; also absent: SIM1, BMP10, LINC02643; maybe low, not absent |
| [[BMP10]] | C | BMP10 activity raises GPM6B's level | lines that do not express BMP10 (47) vs lines expressing it (3) | 1.68× lower at baseline in the lines without BMP10 | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC02099, APOB, TBXT; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.634). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.2, 34.7); signed map (29.5, 21.3). **Vector** length 39.3, 3.78% of its response variance represented; |z| ≥ 3 in 1,018 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +14.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +11.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +14.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +14.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +2.4 |
|  | [[EX229 (drug)]] 5 µM |  | +1.1 | +1.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +1.3 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | glycoprotein M6B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:13,770,939-13,938,638 (-) |
| Ensembl biotype | protein_coding |
| Also known as | M6B, MGC17150, MGC54284 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13491](https://www.uniprot.org/uniprotkb/Q13491) (Neuronal membrane glycoprotein M6-b):

> May be involved in neural development. Involved in regulation of osteoblast function and bone formation. Involved in matrix vesicle release by osteoblasts; this function seems to involve maintenance of the actin cytoskeleton. May be involved in cellular trafficking of SERT and thereby in regulation of serotonin uptake.

**Summary**, from NCBI Gene [2824](https://www.ncbi.nlm.nih.gov/gene/2824):

> This gene encodes a membrane glycoprotein that belongs to the proteolipid protein family. Proteolipid protein family members are expressed in most brain regions and are thought to be involved in cellular housekeeping functions such as membrane trafficking and cell-to-cell communication. This protein may also be involved in osteoblast differentiation. Alternate splicing results in multiple transcript variants. Pseudogenes of this gene are located on chromosomes Y and 22. [provided by RefSeq, Jan …

**Accessions** — [HGNC:4461](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4461) · Entrez [2824](https://www.ncbi.nlm.nih.gov/gene/2824) · UniProt [Q13491](https://www.uniprot.org/uniprotkb/Q13491) · Ensembl [ENSG00000046653](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000046653)

## Data

Gene col 506: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 506); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 506, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 506]; `tensor/DDL_lfc|DDL_z.npy` [506]; `embed/gene_vectors.npy` [506]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 506 or target_col == 506). Every well: [[GPM6B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPM6B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
