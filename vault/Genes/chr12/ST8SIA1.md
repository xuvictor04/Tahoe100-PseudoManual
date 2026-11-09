---
symbol: "ST8SIA1"
type: "gene"
col: 3272
ensembl_id: "ENSG00000111728"
name: "ST8 alpha-N-acetyl-neuraminide alpha-2,8-sialyltransferase 1"
location: "12p12.1"
module: 166
arm: "+"
pooled_cpm: 3.18
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/166"]
generated_by: "tahoemap"
---

# ST8SIA1

*ST8 alpha-N-acetyl-neuraminide alpha-2,8-sialyltransferase 1* — 12p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.92× (z +17.5, q 0e+00, up in 23 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (LOX-IMVI 0.0579×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCC]] (+0.83, fdr 7e-06), [[SGCD]] (+0.79, fdr 7e-06), [[LINC02208]] (+0.77, fdr 7e-06).
> It is in [[Module 166]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CCDC144A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3272.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.92×** | +17.5 | 0e+00 | 23/31 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.18×** | +10.5 | 2e-23 | 9/15 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.90×** | +9.3 | 3e-18 | 2/5 (NCI-H2347, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.93×** | +8.5 | 3e-15 | 23/42 (SW480, A-427, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.92×** | +8.4 | 6e-15 | 16/34 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.43×** | +7.5 | 7e-12 | 2/6 (SK-MEL-2, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.89×** | +5.8 | 6e-07 | 1/8 (LoVo) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.77×** | +5.2 | 2e-05 | 16/36 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +4.9 | 5e-05 | 7/43 (C32, SW 900, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +4.9 | 6e-05 | 8/34 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.68×** | +4.7 | 1e-04 | 7/40 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.5 | 3e-04 | 4/16 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.50×** | +3.7 | 0.009 | 13/45 (H4, A-427, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.50×** | +3.7 | 0.009 | 15/40 (H4, A-427, …) | all doses, stronger at high dose | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.009 | 7/40 (C32, SK-MEL-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.018 | 5/42 (HOP62, SW480, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3272.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (LOX-IMVI 0.0579×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ranolazine (drug)]] 0.5 µM |  | 0.695× | -3.3 | 0.28 | 4/41 (BT-474, NCI-H2347, …) | inconsistent across doses |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 0.682× | -3.3 | 0.28 | 10/36 (HOP62, LS 180, …) | inconsistent across doses |  |
| [[Vortioxetine (drug)]] 0.5 µM |  | 0.702× | -3.2 | 0.28 | 5/43 (SW480, NCI-H2030, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.713× | -3.0 | 0.30 | 7/43 (J82, LOX-IMVI, …) | top dose only |  |
| [[Folic acid (drug)]] 5 µM |  | 0.789× | -3.0 | 0.30 | 7/45 (J82, NCI-H460, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3272. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 41.0 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 9.68× (z +9.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SW480 (line)]] | alt | 2.33 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 9.12× (z +11.0) | — |
| [[A-427 (line)]] | wt | 1.80 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 14.2× (z +9.2) | — |
| [[A498 (line)]] | wt | 1.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.12× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 9.21 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0579× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3272), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCC]] | +0.83 | +0.75 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[SGCD]] | +0.79 | +0.77 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[LINC02208]] | +0.77 | +0.70 / +0.78 | both halves | 7e-06 |  |
| [[SORCS1]] | +0.76 | +0.73 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[OBI1-AS1]] | +0.74 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[CNTN5]] | +0.74 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[CNTN4]] | +0.73 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[USH2A]] | +0.72 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[PTPRT]] | +0.70 | +0.47 / +0.77 | both halves | 2e-05 |  |
| [[CNTNAP4]] | +0.70 | +0.43 / +0.77 | both halves | 3e-05 |  |
| [[ESR1]] | +0.70 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[THSD7B]] | +0.69 | +0.54 / +0.75 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC144A]] | B | CCDC144A activity raises ST8SIA1's level | lines that do not express CCDC144A (18) vs lines expressing it (32) | 1.36× lower at baseline in the lines without CCDC144A | 0.054 | ⚠ within organs, on part of the lines; also absent: CCDC144BP, MCOLN3, ENSG00000266302; maybe low, not absent |
| [[ZNF521]] | B | ZNF521 activity raises ST8SIA1's level | lines that do not express ZNF521 (27) vs lines expressing it (23) | 1.77× lower at baseline in the lines without ZNF521 | 0.089 | ⚠ within organs, on part of the lines; also absent: LEF1, SNAI2, ITGA4 |
| [[TOP2A]] | B | TOP2A activity lowers ST8SIA1's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CASC20]] | B | CASC20 activity raises ST8SIA1's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 1.57× lower at baseline in the lines without CASC20 | 0.096 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 166]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.846). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.7, 28.2); signed map (32.3, 15.4). **Vector** length 48.8, 6.09% of its response variance represented; |z| ≥ 3 in 1,003 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +17.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +1.8 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | +0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | ST8 alpha-N-acetyl-neuraminide alpha-2,8-sialyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.1 — chr12:22,063,773-22,437,041 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SIAT8, SIAT8A |
| Gene groups (HGNC) | Sialyltransferases |
| Reactome | 4 pathways, smallest: Sialic acid metabolism; Synthesis of substrates in N-glycan biosythesis; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92185](https://www.uniprot.org/uniprotkb/Q92185) (Alpha-N-acetylneuraminide alpha-2,8-sialyltransferase):

> Catalyzes the addition of sialic acid in alpha 2,8-linkage to the sialic acid moiety of the ganglioside GM3 to form ganglioside GD3; gangliosides are a subfamily of complex glycosphingolipds that contain one or more residues of sialic acid. Can catalyze the addition of a second alpha-2,8-sialic acid to GD3 to form GT3. Can use GM1b, GD1a and GT1b as acceptor substrates to synthesize GD1c, GT1a and GQ1b respectively. Can synthesize unusual tetra- and pentasialylated lactosylceramide derivatives …

**Summary**, from NCBI Gene [6489](https://www.ncbi.nlm.nih.gov/gene/6489):

> Gangliosides are membrane-bound glycosphingolipids containing sialic acid. Ganglioside GD3 is known to be important for cell adhesion and growth of cultured malignant cells. The protein encoded by this gene is a type II membrane protein that catalyzes the transfer of sialic acid from CMP-sialic acid to GM3 to produce gangliosides GD3 and GT3. The encoded protein may be found in the Golgi apparatus and is a member of glycosyltransferase family 29. Alternatively spliced transcript variants have …

**Accessions** — [HGNC:10869](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10869) · Entrez [6489](https://www.ncbi.nlm.nih.gov/gene/6489) · UniProt [Q92185](https://www.uniprot.org/uniprotkb/Q92185) · Ensembl [ENSG00000111728](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111728)

## Data

Gene col 3272: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3272); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3272, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3272]; `tensor/DDL_lfc|DDL_z.npy` [3272]; `embed/gene_vectors.npy` [3272]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3272 or target_col == 3272). Every well: [[ST8SIA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ST8SIA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
