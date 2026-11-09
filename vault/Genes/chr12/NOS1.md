---
symbol: "NOS1"
type: "gene"
col: 1581
ensembl_id: "ENSG00000089250"
name: "nitric oxide synthase 1"
location: "12q24.22"
module: 165
arm: "+"
pooled_cpm: 4.4
n_lines_expressing: 47
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# NOS1

*nitric oxide synthase 1* — 12q24.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.53× (z +14.0, q 1e-41, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.90× (z +12.8, q 3e-35, up in 20 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A549 0.102×, SHP-77 0.164×); [[Dexamethasone (drug)]] 0.05 µM in 1 line (A549 0.0747×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.226×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASIC2]] (+0.72, fdr 7e-06), [[MTUS2]] (+0.71, fdr 7e-06), [[PTPRT]] (+0.68, fdr 7e-06).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CACNG6]] → it (grade B ⚠); 3 go from it, the strongest it → [[CLVS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1581.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.53×** | +14.0 | 1e-41 | 1/3 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.82×** | +13.4 | 3e-38 | 8/11 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.90×** | +12.8 | 3e-35 | 20/30 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.74×** | +10.4 | 5e-23 | 1/5 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.11×** | +9.0 | 3e-17 | 14/29 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.85×** | +7.4 | 1e-11 | 17/40 (SW480, C-33 A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +4.4 | 8e-04 | 4/16 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.64×** | +4.1 | 0.004 | 9/37 (J82, HS-578T, …) | rises with dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.51×** | +3.5 | 0.029 | 0/8 | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.2 | 0.067 | 1/9 (NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.099 | 2/27 (HOP62, LOX-IMVI) | inconsistent across doses | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1581.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A549 0.102×, SHP-77 0.164×); [[Dexamethasone (drug)]] 0.05 µM in 1 line (A549 0.0747×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.226×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.880× | -4.0 | 0.032 | 12/44 (NCI-H23, NCI-H1792, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.681× | -3.2 | 0.43 | 6/28 (LoVo, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1581. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 16.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -12.5) |
| [[SHP-77 (line)]] | alt | 123 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 1.81 | 0 | 1 | — | [[Berbamine (drug)]] 0.5 µM 0.0400× (z -8.8) |
| [[A-172 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1581), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASIC2]] | +0.72 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[MTUS2]] | +0.71 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[PTPRT]] | +0.68 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[RBFOX3]] | +0.66 | +0.56 / +0.68 | both halves | 1e-05 | STRING 474 |
| [[CNTNAP5]] | +0.65 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[RYR3]] | +0.64 | +0.47 / +0.67 | both halves | 2e-05 | pathway: Cardiac conduction; STRING 918 |
| [[LINC01579]] | +0.63 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[CHRM5]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[PECAM1]] | +0.61 | +0.51 / +0.64 | both halves | 1e-05 | pathway: Platelet homeostasis |
| [[PRKCA-AS1]] | +0.61 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[LINC00578]] | +0.61 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[BMAL2-AS1]] | +0.61 | +0.46 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNG6]] | B | CACNG6 activity lowers NOS1's level | lines that do not express CACNG6 (18) vs lines expressing it (32) | 1.20× higher at baseline in the lines without CACNG6 | 0.021 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, RAB31, CYP27C1 |
| [[CALCA]] | B | CALCA activity raises NOS1's level | lines that do not express CALCA (45) vs lines expressing it (5) | 3.46× lower at baseline in the lines without CALCA | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[MYT1L]] | C | MYT1L's natural level weakens NOS1's drug response | MYT1L's natural level across 39 lines (lineage-adjusted; a glimpse) | r -0.72, reverse -0.81; direction not clear | 0.060 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLVS1]] | C | NOS1's natural level weakens CLVS1's drug response | NOS1's natural level across 42 lines (lineage-adjusted; a glimpse) | r -0.78, reverse -0.44; direction clear | 0.004 | ⚠ tissue can mimic it; precision caveat |
| [[CHRM5]] | C | NOS1's natural level weakens CHRM5's drug response | NOS1's natural level across 41 lines (lineage-adjusted; a glimpse) | r -0.75, reverse -0.47; direction clear | 0.016 | ⚠ tissue can mimic it; precision caveat |
| [[MYT1L]] | C | NOS1's natural level weakens MYT1L's drug response | NOS1's natural level across 34 lines (lineage-adjusted; a glimpse) | r -0.81, reverse -0.72; direction not clear | 0.022 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.658). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.0, 31.3); signed map (30.6, 17.3). **Vector** length 44.5, 5.56% of its response variance represented; |z| ≥ 3 in 880 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +10.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +13.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +14.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.2 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -2.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -2.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.3 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | nitric oxide synthase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.22 — chr12:117,208,142-117,452,170 (-) |
| Ensembl biotype | protein_coding |
| Also known as | nNOS; previously NOS |
| Gene groups (HGNC) | PDZ domain containing; Flavoproteins; Nitric oxide synthase family |
| Hallmark sets | SPERMATOGENESIS, KRAS_SIGNALING_DN, MYOGENESIS |
| Reactome | 8 pathways, smallest: Nitric oxide stimulates guanylate cyclase; ROS and RNS production in phagocytes; Ion homeostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [P29475](https://www.uniprot.org/uniprotkb/P29475) (Nitric oxide synthase 1):

> Produces nitric oxide (NO) which is a messenger molecule with diverse functions throughout the body. In the brain and peripheral nervous system, NO displays many properties of a neurotransmitter. Probably has nitrosylase activity and mediates cysteine S-nitrosylation of cytoplasmic target proteins such SRR.

**Summary**, from NCBI Gene [4842](https://www.ncbi.nlm.nih.gov/gene/4842):

> The protein encoded by this gene belongs to the family of nitric oxide synthases, which synthesize nitric oxide from L-arginine. Nitric oxide is a reactive free radical, which acts as a biologic mediator in several processes, including neurotransmission, and antimicrobial and antitumoral activities. In the brain and peripheral nervous system, nitric oxide displays many properties of a neurotransmitter, and has been implicated in neurotoxicity associated with stroke and neurodegenerative …

**Accessions** — [HGNC:7872](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7872) · Entrez [4842](https://www.ncbi.nlm.nih.gov/gene/4842) · UniProt [P29475](https://www.uniprot.org/uniprotkb/P29475) · Ensembl [ENSG00000089250](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089250)

## Data

Gene col 1581: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1581); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1581, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1581]; `tensor/DDL_lfc|DDL_z.npy` [1581]; `embed/gene_vectors.npy` [1581]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1581 or target_col == 1581). Every well: [[NOS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
