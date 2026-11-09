---
symbol: "CIAO2B"
type: "gene"
col: 9337
ensembl_id: "ENSG00000166595"
name: "cytosolic iron-sulfur assembly component 2B"
location: "16q22.1"
module: 3
arm: "+"
pooled_cpm: 27.67
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CIAO2B

*cytosolic iron-sulfur assembly component 2B* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.92× (z +5.0, q 3e-04, up in 21 of 33 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Bendamustine (drug)]] 5 µM: 1.53× (z +3.2, q 0.088, up in 30 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 5.29×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.339× (z -4.5, q 0.003, down in 35 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.285×, RKO 0.241×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GUK1]] (+0.78, fdr 7e-06), [[LAMTOR5]] (+0.78, fdr 7e-06), [[COMMD6]] (+0.77, fdr 7e-06); moves opposite to [[EWSR1]] (-0.77, fdr 1e-05), [[HNRNPL]] (-0.74, fdr 1e-05), [[ILF3]] (-0.74, fdr 7e-06).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 8 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9337.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 5.29×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.92×** | +5.0 | 3e-04 | 21/33 (A-427, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.07×** | +4.9 | 3e-04 | 37/43 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.81×** | +4.7 | 4e-04 | 32/45 (HOP62, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.73×** | +4.4 | 0.002 | 35/48 (HOP62, SW480, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +4.2 | 0.004 | 35/45 (NCI-H2030, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +4.1 | 0.004 | 11/48 (NCI-H1792, RPMI-7951, …) | inconsistent across doses |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.53×** | +3.2 | 0.088 | 30/47 (SW 900, A498, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.55×** | +3.2 | 0.088 | 19/39 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 1.46× | +3.0 | 0.16 | 20/48 (SW480, SNU-1, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9337.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.285×, RKO 0.241×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.339×** | -4.5 | 0.003 | 35/46 (A-427, SW48, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.652× | -3.4 | 0.17 | 24/48 (SW 900, NCI-H460, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.648× | -3.3 | 0.19 | 26/47 (BT-474, NCI-H2347, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.472× | -3.1 | 0.23 | 21/48 (A-427, SW 900, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.767× | -3.0 | 0.29 | 23/47 (A-427, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9337. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 35.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.29× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -10.2) |
| [[RKO (line)]] | wt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -9.9) |
| [[A-172 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 36.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9337), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 11 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GUK1]] | +0.78 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[LAMTOR5]] | +0.78 | +0.64 / +0.77 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.77 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[MPG]] | +0.77 | +0.56 / +0.77 | both halves | 1e-05 |  |
| [[MIEN1]] | +0.77 | +0.59 / +0.75 | both halves | 7e-06 |  |
| [[ATP5MK]] | +0.76 | +0.64 / +0.77 | both halves | 7e-06 |  |
| [[MRPL41]] ⚠ | +0.75 | +0.58 / +0.71 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[CIB1]] | +0.75 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[RNF181]] | +0.73 | +0.59 / +0.75 | both halves | 7e-06 |  |
| [[ATP5MJ]] | +0.73 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[C19orf81]] | +0.73 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[C19orf53]] | +0.72 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[B3GAT3]] | +0.71 | +0.50 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EWSR1]] | -0.77 | -0.50 / -0.79 | both halves | 1e-05 |  |
| [[HNRNPL]] | -0.74 | -0.55 / -0.71 | both halves | 1e-05 |  |
| [[ILF3]] | -0.74 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[ZMYND11]] | -0.74 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[HNRNPM]] | -0.70 | -0.55 / -0.69 | both halves | 1e-05 |  |
| [[YWHAE]] | -0.69 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[CAPRIN1]] | -0.67 | -0.46 / -0.71 | both halves | 2e-05 |  |
| [[HNRNPA2B1]] | -0.67 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[U2AF2]] | -0.65 | -0.32 / -0.63 | both halves | 2e-04 |  |
| [[HNRNPD]] | -0.65 | -0.49 / -0.70 | both halves | 1e-05 |  |
| [[DARS2]] | -0.65 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[TASOR]] | -0.65 | -0.54 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.816). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-39.3, -24.1); signed map (-31.2, 9.8). **Vector** length 67.2, 19.3% of its response variance represented; |z| ≥ 3 in 438 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +2.2 | +4.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +1.9 | +3.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +2.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +1.7 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +1.2 | +2.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +1.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.1 | +1.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.1 | +2.1 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | -5.2 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | -5.0 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | -4.6 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -4.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.8 | -3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -0.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.0 | -1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -3.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | cytosolic iron-sulfur assembly component 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:66,932,065-66,934,423 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-128, MIP18, CIA2B; previously FAM96B |
| Gene groups (HGNC) | Cytosolic iron-sulfur assembly components |
| Reactome | 1 pathways, smallest: Cytosolic iron-sulfur cluster assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3D0](https://www.uniprot.org/uniprotkb/Q9Y3D0) (Cytosolic iron-sulfur assembly component 2B):

> Component of the cytosolic iron-sulfur protein assembly (CIA) complex, a multiprotein complex that mediates the incorporation of iron-sulfur cluster into extramitochondrial Fe/S proteins. As a CIA complex component and in collaboration with CIAO1 and MMS19, binds to and facilitates the assembly of most cytosolic-nuclear Fe/S proteins. As part of the mitotic spindle-associated MMXD complex it plays a role in chromosome segregation, probably by facilitating iron-sulfur cluster assembly into …

**Summary**, from NCBI Gene [51647](https://www.ncbi.nlm.nih.gov/gene/51647):

> Involved in chromosome segregation and protein maturation. Located in cytosol; nucleoplasm; and spindle. Part of MMXD complex and cytosolic [4Fe-4S] assembly targeting complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24261](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24261) · Entrez [51647](https://www.ncbi.nlm.nih.gov/gene/51647) · UniProt [Q9Y3D0](https://www.uniprot.org/uniprotkb/Q9Y3D0) · Ensembl [ENSG00000166595](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166595)

## Data

Gene col 9337: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9337); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9337, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9337]; `tensor/DDL_lfc|DDL_z.npy` [9337]; `embed/gene_vectors.npy` [9337]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9337 or target_col == 9337). Every well: [[CIAO2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CIAO2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
