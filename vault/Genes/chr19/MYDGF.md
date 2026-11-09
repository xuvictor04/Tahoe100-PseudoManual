---
symbol: "MYDGF"
type: "gene"
col: 1093
ensembl_id: "ENSG00000074842"
name: "myeloid derived growth factor"
location: "19p13.3"
module: 49
arm: "+"
pooled_cpm: 69.39
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 4
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# MYDGF

*myeloid derived growth factor* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.71× (z +4.1, q 0.024, up in 34 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change.
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.497× (z -8.5, q 1e-14, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC61B]] (+0.87, fdr 7e-06), [[HM13]] (+0.82, fdr 7e-06), [[SSR2]] (+0.80, fdr 7e-06).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1093.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.71×** | +4.1 | 0.024 | 34/49 (SNU-1, SNU-423, …) | two highest doses | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | 1.49× | +3.3 | 0.26 | 26/42 (SNU-423, C32, …) | two highest doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1093.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.497×** | -8.5 | 1e-14 | 44/48 (J82, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.644×** | -3.6 | 0.071 | 29/48 (H4, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.750×** | -3.5 | 0.071 | 30/48 (A549, HS-578T, …) | top dose only | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **0.666×** | -3.5 | 0.071 | 29/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1093. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 115 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -10.2) |
| [[A-427 (line)]] | wt | 45.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -13.1) |
| [[A498 (line)]] | wt | 123 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -12.4) |
| [[H4 (line)]] | wt | 117 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -11.0) |
| [[HS-578T (line)]] | alt | 171 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -10.3) |
| [[J82 (line)]] | alt | 72.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -13.8) |
| [[MIA PaCa-2 (line)]] | alt | 54.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 77.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -12.6) |
| [[RKO (line)]] | wt | 67.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 119 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 53.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -8.5) |
| [[SNU-1 (line)]] | wt | 51.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -9.3) |
| [[SW 1088 (line)]] | alt | 126 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0657× (z -10.7) |
| [[A549 (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 65.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 79.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 108 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 82.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 83.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 61.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 53.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1093), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC61B]] | +0.87 | +0.80 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[HM13]] | +0.82 | +0.82 / +0.80 | both halves | 7e-06 |  |
| [[SSR2]] | +0.80 | +0.77 / +0.84 | both halves | 7e-06 |  |
| [[TMED9]] | +0.80 | +0.85 / +0.80 | both halves | 7e-06 | STRING 607 |
| [[PGM3]] | +0.77 | +0.69 / +0.80 | both halves | 7e-06 |  |
| [[KDELR2]] | +0.76 | +0.79 / +0.73 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.75 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[SEC61G]] | +0.75 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.75 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[SDF2L1]] | +0.74 | +0.74 / +0.73 | both halves | 7e-06 | STRING 637 |
| [[SERP1]] | +0.74 | +0.67 / +0.76 | both halves | 7e-06 | pathway: IRE1alpha activates chaperones |
| [[TXNDC11]] | +0.74 | +0.71 / +0.75 | both halves | 7e-06 | STRING 531 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.754). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.4, -34.5); signed map (-50.1, 11.4). **Vector** length 100, 39.4% of its response variance represented; |z| ≥ 3 in 467 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cotranslational targeting of proteins to the endoplasmic reticulum* (reactome, mean cos +0.67 to 8); *unfolded protein response* (hallmark, mean cos +0.55 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +2.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.0 | +2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.9 | +2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +0.6 |
|  | [[EX229 (drug)]] 0.5 µM |  | +2.3 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +2.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.5 | -3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.7 | -8.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.5 | -2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.1 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | myeloid derived growth factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:4,641,374-4,670,362 (-) |
| Ensembl biotype | protein_coding |
| Also known as | R33729_1, IL25, SF20, IL-25, IL-27; previously IL27, IL27w, C19orf10 |
| Reactome | 5 pathways, smallest: XBP1(S) activates chaperone genes; IRE1alpha activates chaperones; Unfolded Protein Response (UPR) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969H8](https://www.uniprot.org/uniprotkb/Q969H8) (Myeloid-derived growth factor):

> Bone marrow-derived monocyte and paracrine-acting protein that promotes cardiac myocyte survival and adaptive angiogenesis for cardiac protection and/or repair after myocardial infarction (MI). Stimulates endothelial cell proliferation through a MAPK1/3-, STAT3- and CCND1-mediated signaling pathway. Inhibits cardiac myocyte apoptosis in a PI3K/AKT-dependent signaling pathway (By similarity). Involved in endothelial cell proliferation and angiogenesis.

**Summary**, from NCBI Gene [56005](https://www.ncbi.nlm.nih.gov/gene/56005):

> The protein encoded by this gene was previously thought to support proliferation of lymphoid cells and was considered an interleukin. However, this activity has not been reproducible and the function of this protein is currently unknown. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16948](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16948) · Entrez [56005](https://www.ncbi.nlm.nih.gov/gene/56005) · UniProt [Q969H8](https://www.uniprot.org/uniprotkb/Q969H8) · Ensembl [ENSG00000074842](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074842)

## Data

Gene col 1093: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1093); `tables/drug_effects.parquet` (6 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1093, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1093]; `tensor/DDL_lfc|DDL_z.npy` [1093]; `embed/gene_vectors.npy` [1093]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1093 or target_col == 1093). Every well: [[MYDGF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYDGF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
