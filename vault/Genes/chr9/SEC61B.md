---
symbol: "SEC61B"
type: "gene"
col: 2808
ensembl_id: "ENSG00000106803"
name: "SEC61 translocon subunit beta"
location: "9q22.33"
module: 49
arm: "+"
pooled_cpm: 58.38
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# SEC61B

*SEC61 translocon subunit beta* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.53× (z +4.4, q 0.003, up in 36 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 3.14×; ⚠ cell-cycle shift, explains ~61% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 0.380×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYDGF]] (+0.87, fdr 7e-06), [[SSR2]] (+0.84, fdr 7e-06), [[ACBD3]] (+0.80, fdr 7e-06).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SNHG18]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2808.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 3.14×; ⚠ cell-cycle shift, explains ~61% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.53×** | +4.4 | 0.003 | 36/49 (PANC-1, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.62×** | +4.4 | 0.003 | 38/48 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +3.8 | 0.029 | 32/48 (C-33 A, SK-MEL-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | 1.96× | +3.2 | 0.21 | 24/48 (RKO, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | 1.90× | +3.0 | 0.27 | 31/48 (NCI-H1792, LoVo, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2808.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 0.380×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.716× | -3.0 | 0.75 | 31/48 (AsPC-1, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2808. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 54.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.14× (z +9.1) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[NCI-H2347 (line)]] | alt | 55.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 88.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 86.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 80.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 78.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 71.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 55.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 96.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 54.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2808), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYDGF]] | +0.87 | +0.80 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[SSR2]] | +0.84 | +0.79 / +0.84 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 996 |
| [[ACBD3]] | +0.80 | +0.73 / +0.81 | both halves | 7e-06 |  |
| [[TMED9]] | +0.79 | +0.76 / +0.80 | both halves | 7e-06 | STRING 470 |
| [[HM13]] | +0.78 | +0.73 / +0.76 | both halves | 7e-06 | STRING 434 |
| [[SELENOS]] | +0.76 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[SRP54]] | +0.74 | +0.70 / +0.72 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 824 |
| [[SERP1]] | +0.73 | +0.71 / +0.76 | both halves | 7e-06 | same gene group; pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 746 |
| [[OSBP]] | +0.73 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.73 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[EIF2AK3]] | +0.72 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[COG3]] | +0.72 | +0.70 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNHG18]] | B | SNHG18 activity raises SEC61B's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.32× lower at baseline in the lines without SNHG18 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |
| [[KCNK6]] | B | KCNK6 activity raises SEC61B's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 1.36× lower at baseline in the lines without KCNK6 | 0.081 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.790). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.3, -35.1); signed map (-50.1, 11.9). **Vector** length 102, 37.1% of its response variance represented; |z| ≥ 3 in 496 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *XBP1(S) activates chaperone genes* (reactome, mean cos +0.61 to 8); *IRE1alpha activates chaperones* (reactome, mean cos +0.61 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.61 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +2.9 | +4.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.8 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.7 | +1.9 |
|  | [[EX229 (drug)]] 0.5 µM |  | +2.5 | +2.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | +0.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.6 | -1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.6 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -2.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | SEC61 translocon subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.33 — chr9:99,222,064-99,230,615 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sec61 complex subunits |
| Reactome | 7 pathways, smallest: Insertion of tail-anchored proteins into the endoplasmic reticulum membrane; ER-Phagosome pathway; Antigen processing-Cross presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [P60468](https://www.uniprot.org/uniprotkb/P60468) (Protein transport protein Sec61 subunit beta):

> Component of SEC61 channel-forming translocon complex that mediates transport of signal peptide-containing precursor polypeptides across the endoplasmic reticulum (ER). Forms a ribosome receptor and a gated pore in the ER membrane, both functions required for cotranslational translocation of nascent polypeptides. The SEC61 channel is also involved in ER membrane insertion of transmembrane proteins: it mediates membrane insertion of the first few transmembrane segments of proteins, while …

**Summary**, from NCBI Gene [10952](https://www.ncbi.nlm.nih.gov/gene/10952):

> The Sec61 complex is the central component of the protein translocation apparatus of the endoplasmic reticulum (ER) membrane. Oligomers of the Sec61 complex form a transmembrane channel where proteins are translocated across and integrated into the ER membrane. This complex consists of three membrane proteins- alpha, beta, and gamma. This gene encodes the beta-subunit protein. The Sec61 subunits are also observed in the post-ER compartment, suggesting that these proteins can escape the ER and …

**Accessions** — [HGNC:16993](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16993) · Entrez [10952](https://www.ncbi.nlm.nih.gov/gene/10952) · UniProt [P60468](https://www.uniprot.org/uniprotkb/P60468) · Ensembl [ENSG00000106803](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106803)

## Data

Gene col 2808: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2808); `tables/drug_effects.parquet` (6 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2808, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2808]; `tensor/DDL_lfc|DDL_z.npy` [2808]; `embed/gene_vectors.npy` [2808]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2808 or target_col == 2808). Every well: [[SEC61B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC61B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
