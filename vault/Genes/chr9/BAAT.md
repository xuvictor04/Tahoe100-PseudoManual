---
symbol: "BAAT"
type: "gene"
col: 5931
ensembl_id: "ENSG00000136881"
name: "bile acid-CoA:amino acid N-acyltransferase"
location: "9q31.1"
module: 39
arm: "+"
pooled_cpm: 2.09
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# BAAT

*bile acid-CoA:amino acid N-acyltransferase* — 9q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.45× (z +19.1, q 0e+00, up in 28 of 28 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bosentan (hydrate) (drug)]] 5 µM in 2 lines (SW480 0.0917×, NCI-H460 0.111×); [[Triclosan (drug)]] 0.5 µM in 1 line (RKO 0.0561×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSH4]] (+0.83, fdr 7e-06), [[SMIM15-AS1]] (+0.83, fdr 7e-06), [[LINC00486]] (+0.80, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5931.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.45×** | +19.1 | 0e+00 | 28/28 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.37×** | +13.7 | 3e-40 | 26/32 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **5.34×** | +12.9 | 1e-35 | 10/11 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **2.29×** | +9.3 | 2e-18 | 24/42 (NCI-H2347, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.35×** | +9.3 | 2e-18 | 0/0 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.95×** | +8.6 | 7e-16 | 25/34 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.00×** | +8.1 | 5e-14 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.00×** | +7.8 | 5e-13 | 11/44 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **2.54×** | +7.4 | 7e-12 | 19/35 (NCI-H460, SK-MEL-2, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **2.33×** | +6.7 | 9e-10 | 21/46 (NCI-H460, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.28×** | +6.5 | 3e-09 | 2/11 (SW480, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.16×** | +5.9 | 2e-07 | 10/20 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.90×** | +4.9 | 5e-05 | 12/37 (LoVo, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +4.9 | 5e-05 | 12/31 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.83×** | +4.8 | 6e-05 | 13/45 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.88×** | +4.7 | 8e-05 | 11/37 (A-172, A549, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.59×** | +3.6 | 0.008 | 2/39 (HEC-1-A, BT-474) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ivermectin (drug)]] 0.5 µM |  | **1.51×** | +3.3 | 0.032 | 3/30 (A-172, CFPAC-1, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.46×** | +3.0 | 0.080 | 5/37 (J82, A-172, …) | all doses, flat |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.49×** | +2.9 | 0.090 | 0/19 | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bosentan (hydrate) (drug)]] 5 µM in 2 lines (SW480 0.0917×, NCI-H460 0.111×); [[Triclosan (drug)]] 0.5 µM in 1 line (RKO 0.0561×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5931. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.91 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +9.6) | [[Bosentan (hydrate) (drug)]] 5 µM 0.111× (z -8.9) |
| [[LoVo (line)]] | wt | 1.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.25× (z +8.7) | — |
| [[RKO (line)]] | wt | 5.74 | 0 | 1 | — | [[Triclosan (drug)]] 0.5 µM 0.0561× (z -8.9) |
| [[SW480 (line)]] | alt | 3.03 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0917× (z -9.6) |
| [[A-172 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.927 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.996 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.875 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.852 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.715 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.848 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.717 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5931), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSH4]] | +0.83 | +0.81 / +0.67 | both halves | 7e-06 |  |
| [[SMIM15-AS1]] | +0.83 | +0.82 / +0.62 | both halves | 7e-06 |  |
| [[LINC00486]] | +0.80 | +0.82 / +0.68 | both halves | 7e-06 |  |
| [[LINC01030]] | +0.78 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[MYH3]] | +0.77 | +0.80 / +0.65 | both halves | 7e-06 |  |
| [[GRK7]] | +0.77 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[CPEB2-DT]] | +0.77 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[MYOCOS]] | +0.77 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[GLIPR1-AS1]] | +0.76 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[ANKDD1B]] | +0.76 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[ARL9]] | +0.76 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[YIPF7]] | +0.75 | +0.68 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BAAT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.807). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.8, -12.2); signed map (17.2, 3.6). **Vector** length 58.3, 8.28% of its response variance represented; |z| ≥ 3 in 1,132 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +19.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +13.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +9.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +12.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +7.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.6 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +7.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +2.0 |
| fall | [[Brivudine (drug)]] 5 µM |  | -2.8 | -0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +0.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | -0.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | bile acid-CoA:amino acid N-acyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.1 — chr9:101,354,182-101,385,400 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BAT, BACAT |
| Gene groups (HGNC) | Thioester hydrolases; Acyltransferases |
| Reactome | 8 pathways, smallest: Recycling of bile acids and salts; Synthesis of bile acids and bile salts via 7alpha-hydroxycholesterol; Synthesis of bile acids and bile salts |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14032](https://www.uniprot.org/uniprotkb/Q14032) (Bile acid-CoA:amino acid N-acyltransferase):

> Catalyzes the amidation of bile acids (BAs) with the amino acids taurine and glycine. More than 95% of the BAs are N-acyl amidates with glycine and taurine. Amidation of BAs in the liver with glycine or taurine prior to their excretion into bile is an important biochemical event in bile acid metabolism. This conjugation (or amidation) plays several important biological roles in that it promotes the secretion of BAs and cholesterol into bile and increases the detergent properties of BAs in the …

**Summary**, from NCBI Gene [570](https://www.ncbi.nlm.nih.gov/gene/570):

> The protein encoded by this gene is a liver enzyme that catalyzes the transfer of C24 bile acids from the acyl-CoA thioester to either glycine or taurine, the second step in the formation of bile acid-amino acid conjugates. The bile acid conjugates then act as a detergent in the gastrointestinal tract, which enhances lipid and fat-soluble vitamin absorption. Defects in this gene are a cause of familial hypercholanemia (FHCA). Two transcript variants encoding the same protein have been found for …

**Accessions** — [HGNC:932](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:932) · Entrez [570](https://www.ncbi.nlm.nih.gov/gene/570) · UniProt [Q14032](https://www.uniprot.org/uniprotkb/Q14032) · Ensembl [ENSG00000136881](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136881)

## Data

Gene col 5931: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5931); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5931, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5931]; `tensor/DDL_lfc|DDL_z.npy` [5931]; `embed/gene_vectors.npy` [5931]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5931 or target_col == 5931). Every well: [[BAAT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BAAT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
