---
symbol: "EMC6"
type: "gene"
col: 4831
ensembl_id: "ENSG00000127774"
name: "ER membrane protein complex subunit 6"
location: "17p13.2"
module: 54
arm: "+"
pooled_cpm: 12.03
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# EMC6

*ER membrane protein complex subunit 6* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.29× (z +5.3, q 6e-05, up in 32 of 38 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.66× (z +4.8, q 3e-04, up in 28 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.138×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (Panc 03.27 0.232×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 25 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL36]] (+0.87, fdr 7e-06), [[RPL36AL]] (+0.82, fdr 1e-05, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[EXOSC4]] (+0.79, fdr 7e-06), [[SCAND1]] (+0.78, fdr 8e-06); moves opposite to [[DHFR]] (-0.70, fdr 4e-04), [[DPY19L4]] (-0.65, fdr 1e-04), [[SRSF1]] (-0.63, fdr 5e-04).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4831.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.29×** | +5.3 | 6e-05 | 32/38 (KATO III, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.10×** | +4.9 | 2e-04 | 39/47 (SW480, COLO 205, …) | two highest doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +4.8 | 3e-04 | 28/44 (A549, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **2.02×** | +4.7 | 4e-04 | 29/41 (J82, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.79×** | +3.9 | 0.011 | 32/47 (SNU-423, HOP62, …) | two highest doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.73×** | +3.7 | 0.022 | 27/47 (AsPC-1, HOP62, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 1.39× | +3.1 | 0.14 | 25/48 (PANC-1, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4831.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.138×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (Panc 03.27 0.232×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Erlotinib (drug)]] 0.05 µM |  | 0.597× | -3.1 | 0.63 | 17/47 (hTERT-HPNE, LoVo, …) | inconsistent across doses | position effect removed |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.607× | -3.0 | 0.63 | 16/47 (A-427, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4831. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4831), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 25 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL36]] | +0.87 | +0.68 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[RPL36AL]] ⚠ | +0.82 | +0.56 / +0.88 | both halves | 1e-05 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; ⚠ in the vector space only through flagged drug-doses |
| [[EXOSC4]] | +0.79 | +0.58 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[SF3B5]] ⚠ | +0.79 | +0.48 / +0.86 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SCAND1]] | +0.78 | +0.57 / +0.86 | both halves | 8e-06 |  |
| [[ZNF593]] | +0.78 | +0.50 / +0.87 | both halves | 1e-05 |  |
| [[MRPS12]] | +0.78 | +0.42 / +0.85 | both halves | 4e-05 | **novel candidate** |
| [[SMIM26]] ⚠ | +0.78 | +0.48 / +0.84 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CHCHD1]] | +0.77 | +0.33 / +0.86 | both halves | 1e-04 |  |
| [[NCBP2AS2]] | +0.77 | +0.53 / +0.81 | both halves | 1e-05 |  |
| [[POLR2J]] ⚠ | +0.76 | +0.62 / +0.82 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[UQCR10]] ⚠ | +0.76 | +0.62 / +0.83 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[C16orf91]] | +0.75 | +0.48 / +0.80 | both halves | 2e-05 |  |
| [[POP7]] | +0.74 | +0.31 / +0.82 | both halves | 2e-04 |  |
| [[GADD45GIP1]] | +0.74 | +0.36 / +0.84 | both halves | 1e-04 |  |
| [[C4orf48]] | +0.72 | +0.39 / +0.81 | both halves | 6e-05 |  |
| [[OXLD1]] | +0.72 | +0.34 / +0.84 | both halves | 1e-04 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHFR]] | -0.70 | -0.26 / -0.81 | both halves | 4e-04 |  |
| [[DPY19L4]] | -0.65 | -0.32 / -0.68 | both halves | 1e-04 |  |
| [[SRSF1]] | -0.63 | -0.23 / -0.70 | both halves | 5e-04 |  |
| [[HNRNPA3]] | -0.62 | -0.34 / -0.70 | both halves | 1e-04 |  |
| [[IPO5]] | -0.59 | -0.36 / -0.67 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers EMC6's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.710). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-43.7, -11.4); signed map (-12.1, -7.5). **Vector** length 62.5, 14.7% of its response variance represented; |z| ≥ 3 in 537 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial ribosome-associated quality control* (reactome, mean cos +0.58 to 9); *Mitochondrial translation* (reactome, mean cos +0.58 to 9); *Mitochondrial translation elongation* (reactome, mean cos +0.59 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +1.8 | +4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.8 | +5.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.7 | +2.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.4 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +2.9 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.1 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +2.1 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | +1.0 | +2.8 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.0 | +2.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.6 | -0.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.0 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | +2.2 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -1.6 | -0.9 |
|  | [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | +1.1 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -3.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ER membrane protein complex subunit 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:3,668,812-3,669,668 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2963, RAB5IFL; previously TMEM93 |
| Gene groups (HGNC) | ER membrane protein complex subunits |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BV81](https://www.uniprot.org/uniprotkb/Q9BV81) (ER membrane protein complex subunit 6):

> Part of the endoplasmic reticulum membrane protein complex (EMC) that enables the energy-independent insertion into endoplasmic reticulum membranes of newly synthesized membrane proteins. Preferentially accommodates proteins with transmembrane domains that are weakly hydrophobic or contain destabilizing features such as charged and aromatic residues. Involved in the cotranslational insertion of multi-pass membrane proteins in which stop-transfer membrane-anchor sequences become ER membrane …

**Summary**, from NCBI Gene [83460](https://www.ncbi.nlm.nih.gov/gene/83460):

> Contributes to membrane insertase activity. Involved in autophagosome assembly; protein insertion into ER membrane by stop-transfer membrane-anchor sequence; and tail-anchored membrane protein insertion into ER membrane. Located in endoplasmic reticulum membrane and omegasome membrane. Part of EMC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28430](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28430) · Entrez [83460](https://www.ncbi.nlm.nih.gov/gene/83460) · UniProt [Q9BV81](https://www.uniprot.org/uniprotkb/Q9BV81) · Ensembl [ENSG00000127774](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127774)

## Data

Gene col 4831: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4831); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4831, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4831]; `tensor/DDL_lfc|DDL_z.npy` [4831]; `embed/gene_vectors.npy` [4831]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4831 or target_col == 4831). Every well: [[EMC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EMC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
