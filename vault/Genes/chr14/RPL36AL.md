---
symbol: "RPL36AL"
type: "gene"
col: 9133
ensembl_id: "ENSG00000165502"
name: "ribosomal protein L36a like"
location: "14q21.3"
module: 24
arm: "+"
pooled_cpm: 93.86
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/024", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# RPL36AL

*ribosomal protein L36a like* — 14q21.3

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.50× (z +5.4, q 3e-05, up in 45 of 47 measured lines) ⚠ toxic. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 0.353×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 25 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM26]] (+0.87, fdr 7e-06, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[LAMTOR5]] (+0.87, fdr 7e-06), [[RPL18]] (+0.86, fdr 7e-06, ⚠ RPL18 in the vector space only through flagged drug-doses), [[ATP5MK]] (+0.85, fdr 7e-06), [[COMMD6]] (+0.85, fdr 7e-06); moves opposite to [[LIN7C]] (-0.76, fdr 1e-05), [[PNPO]] (-0.73, fdr 7e-06), [[DHFR]] (-0.72, fdr 1e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TRAPPC2B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9133.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.50×** | +5.4 | 3e-05 | 45/47 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.95×** | +4.1 | 0.012 | 44/48 (PANC-1, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.90×** | +3.9 | 0.015 | 41/48 (SW 900, HS-578T, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9133.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 0.353×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.700× | -3.1 | 0.35 | 29/48 (NCI-H2347, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.581× | -3.1 | 0.35 | 44/48 (A498, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9133. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 146 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -9.2) |
| [[A-172 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 90.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 79.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 80.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 71.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 58.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 63.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 85.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 104 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 149 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 66.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 93.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 82.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 97.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 114 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 77.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 96.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9133), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 25 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM26]] ⚠ | +0.87 | +0.67 / +0.92 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[LAMTOR5]] | +0.87 | +0.75 / +0.88 | both halves | 7e-06 | pathway: Cellular response to starvation |
| [[RPL18]] ⚠ | +0.86 | +0.81 / +0.86 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 995; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MK]] | +0.85 | +0.81 / +0.84 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.85 | +0.74 / +0.88 | both halves | 7e-06 |  |
| [[RPL36]] | +0.84 | +0.82 / +0.84 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 997 |
| [[ATP5MJ]] | +0.84 | +0.73 / +0.89 | both halves | 7e-06 |  |
| [[TMEM258]] | +0.84 | +0.78 / +0.86 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |
| [[COX6B1]] | +0.83 | +0.76 / +0.83 | both halves | 7e-06 |  |
| [[ROMO1]] | +0.83 | +0.75 / +0.84 | both halves | 7e-06 |  |
| [[EMC6]] | +0.82 | +0.56 / +0.88 | both halves | 1e-05 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |
| [[TOMM7]] | +0.82 | +0.76 / +0.83 | both halves | 7e-06 | pathway: Protein localization; STRING 452 |
| [[RPS27]] | +0.80 | +0.69 / +0.83 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 997 |
| [[RPL35A]] | +0.80 | +0.74 / +0.81 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN7C]] | -0.76 | -0.52 / -0.81 | both halves | 1e-05 |  |
| [[PNPO]] | -0.73 | -0.75 / -0.63 | both halves | 7e-06 |  |
| [[DHFR]] | -0.72 | -0.34 / -0.79 | both halves | 1e-04 |  |
| [[CAPRIN1]] | -0.72 | -0.54 / -0.74 | both halves | 1e-05 |  |
| [[IPO5]] | -0.71 | -0.54 / -0.76 | both halves | 1e-05 | pathway: Influenza Infection |
| [[TWF1]] | -0.70 | -0.55 / -0.72 | both halves | 1e-05 |  |
| [[EMC1]] | -0.70 | -0.51 / -0.76 | both halves | 1e-05 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |
| [[MOB1A]] | -0.70 | -0.48 / -0.77 | both halves | 2e-05 |  |
| [[DARS2]] | -0.69 | -0.61 / -0.64 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRAPPC2B]] | B | TRAPPC2B activity lowers RPL36AL's level | lines that do not express TRAPPC2B (7) vs lines expressing it (43) | 1.48× higher at baseline in the lines without TRAPPC2B | 0.039 | ⚠ within organs, on part of the lines; also absent: ZNF547, ZNF548, ZNF530 |
| [[NDUFA13]] | C | NDUFA13's natural level strengthens RPL36AL's drug response | NDUFA13's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.02; direction not clear | 0.082 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.823). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-43.6, -20.9); signed map (-32.5, 8.8). **Vector** length 100, 51.8% of its response variance represented; |z| ≥ 3 in 300 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.53 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +3.2 | +4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.5 | +1.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.4 | +2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +0.7 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +2.0 | +1.6 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.0 | +2.0 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.9 | +2.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -11.1 | -0.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -10.9 | +0.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -10.8 | +1.3 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -3.4 | -0.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.5 | +1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.3 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | +1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -1.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L36a like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.3 — chr14:49,618,530-49,620,626 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously RPL36A, RPL36AP42 |
| Gene groups (HGNC) | L ribosomal proteins |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

UniProt [Q969Q0](https://www.uniprot.org/uniprotkb/Q969Q0) carries no function annotation.

**Summary**, from NCBI Gene [6166](https://www.ncbi.nlm.nih.gov/gene/6166):

> Cytoplasmic ribosomes, organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein, which shares sequence similarity with yeast ribosomal protein L44, belongs to the L44E (L36AE) family of ribosomal proteins. This gene and the human gene officially named …

**Accessions** — [HGNC:10346](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10346) · Entrez [6166](https://www.ncbi.nlm.nih.gov/gene/6166) · UniProt [Q969Q0](https://www.uniprot.org/uniprotkb/Q969Q0) · Ensembl [ENSG00000165502](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165502)

## Data

Gene col 9133: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9133); `tables/drug_effects.parquet` (5 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9133, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9133]; `tensor/DDL_lfc|DDL_z.npy` [9133]; `embed/gene_vectors.npy` [9133]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9133 or target_col == 9133). Every well: [[RPL36AL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL36AL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
