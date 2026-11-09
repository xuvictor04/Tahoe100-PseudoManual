---
symbol: "MED25"
type: "gene"
col: 2534
ensembl_id: "ENSG00000104973"
name: "mediator complex subunit 25"
location: "19q13.33"
module: 76
arm: "+"
pooled_cpm: 27.84
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 10
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# MED25

*mediator complex subunit 25* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.22× (z +4.7, q 0.002, up in 22 of 48 measured lines) ⚠ cell-cycle shift, explains ~5% of this change.
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.688× (z -8.8, q 1e-15, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LMF2]] (+0.62, fdr 1e-05), [[TCTN2]] (+0.62, fdr 1e-05), [[ATG14]] (+0.59, fdr 9e-06); moves opposite to [[NIPAL1]] (-0.56, fdr 1e-05), [[ZNF562]] (-0.55, fdr 2e-05), [[DUSP5-DT]] (-0.55, fdr 2e-05).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2534.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.22×** | +4.7 | 0.002 | 22/48 (H4, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.3 | 0.23 | 10/48 (AsPC-1, A-427, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.21× | +3.2 | 0.23 | 9/48 (AsPC-1, SW480, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | 1.44× | +3.2 | 0.23 | 10/45 (H4, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2534.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.688×** | -8.8 | 1e-15 | 29/47 (A-427, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.640×** | -7.4 | 4e-11 | 30/47 (COLO 205, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.733×** | -7.3 | 6e-11 | 34/48 (NCI-H1792, Panc 03.27, …) | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.730×** | -5.2 | 2e-05 | 24/47 (MIA PaCa-2, SW48, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.737×** | -5.1 | 5e-05 | 28/47 (H4, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.769×** | -4.2 | 0.003 | 22/48 (NCI-H1573, SNU-423, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.786×** | -3.8 | 0.013 | 11/48 (PANC-1, A549, …) | inconsistent across doses | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.650×** | -3.7 | 0.013 | 17/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.666×** | -3.5 | 0.024 | 16/47 (MIA PaCa-2, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.808×** | -3.5 | 0.024 | 13/48 (NCI-H2030, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.875× | -3.1 | 0.094 | 13/48 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2534. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 22.5 | 0 | 4 (2 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.133× (z -10.8) |
| [[COLO 205 (line)]] | alt | 27.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -9.0) |
| [[A-172 (line)]] | wt | 40.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.405× (z -8.9) |
| [[A-427 (line)]] | wt | 37.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -17.9) |
| [[A549 (line)]] | wt | 38.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.343× (z -9.0) |
| [[C-33 A (line)]] | alt | 59.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 22.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -11.9) |
| [[CHP-212 (line)]] | wt | 34.6 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0843× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 1 | — | [[Tranilast (drug)]] 0.05 µM 0.0662× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW 900 (line)]] | alt | 33.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A498 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2534), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMF2]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[TCTN2]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[ATG14]] | +0.59 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[RETREG2]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[UBAC1]] | +0.58 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[ATF6B]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[MAPK3]] | +0.57 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[UBXN6]] | +0.56 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[BAG4]] | +0.56 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[GET3]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[KLHDC3]] | +0.56 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[MKRN1]] | +0.56 | +0.60 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIPAL1]] | -0.56 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[ZNF562]] | -0.55 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[DUSP5-DT]] | -0.55 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[SOWAHC]] | -0.53 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[ADTRP]] | -0.53 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[C11orf91]] | -0.53 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[ZNF121]] | -0.52 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[SERPINB8]] | -0.52 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[BICD1]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[LINC00513]] | -0.52 | -0.65 / -0.36 | both halves | 1e-04 |  |
| [[BLZF2P]] | -0.51 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[NAV3]] | -0.51 | -0.49 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.593). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.0, -16.1); signed map (-20.1, 5.8). **Vector** length 95.6, 21.1% of its response variance represented; |z| ≥ 3 in 712 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | +4.6 | +4.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.4 | +2.5 |
|  | [[NG25 (drug)]] 5 µM |  | +3.0 | +3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.9 | +3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +2.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.5 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +0.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.8 | -7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.5 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -7.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.0 | -5.2 |
|  | [[EX229 (drug)]] 5 µM |  | -3.3 | -3.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.1 | -3.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.8 | -2.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.7 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,818,282-49,840,383 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARC92, ACID1, TCBAP0758, DKFZp434K0512 |
| Gene groups (HGNC) | Mediator complex; MicroRNA protein coding host genes |
| Reactome | 8 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Adipogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q71SY5](https://www.uniprot.org/uniprotkb/Q71SY5) (Mediator of RNA polymerase II transcription subunit 25):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [81857](https://www.ncbi.nlm.nih.gov/gene/81857):

> This gene encodes a component of the transcriptional coactivator complex termed the Mediator complex. This complex is required for transcription of most RNA polymerase II-dependent genes. The encoded protein plays a role in chromatin modification and in preinitiation complex assembly. Mutations in this gene are associated with Charcot-Marie-Tooth disease type 2B2. [provided by RefSeq, Apr 2010]

**Accessions** — [HGNC:28845](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28845) · Entrez [81857](https://www.ncbi.nlm.nih.gov/gene/81857) · UniProt [Q71SY5](https://www.uniprot.org/uniprotkb/Q71SY5) · Ensembl [ENSG00000104973](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104973)

## Data

Gene col 2534: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2534); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2534, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2534]; `tensor/DDL_lfc|DDL_z.npy` [2534]; `embed/gene_vectors.npy` [2534]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2534 or target_col == 2534). Every well: [[MED25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
