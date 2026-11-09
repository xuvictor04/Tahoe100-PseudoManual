---
symbol: "SLC35B1"
type: "gene"
col: 4253
ensembl_id: "ENSG00000121073"
name: "solute carrier family 35 member B1"
location: "17q21.33"
module: 49
arm: "+"
pooled_cpm: 16.66
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# SLC35B1

*solute carrier family 35 member B1* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.87× (z +10.0, q 1e-20, up in 34 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.09× (z +8.0, q 2e-13, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.699× (z -5.5, q 3e-05, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Tadalafil (drug)]] 5 µM in 1 line (SNU-423 0.135×); [[Orlistat (drug)]] 0.05 µM in 1 line (SW48 0.0857×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FICD]] (+0.64, fdr 1e-05), [[DERL2]] (+0.63, fdr 1e-05), [[UBE2J1]] (+0.62, fdr 1e-05); moves opposite to [[HPSE]] (-0.53, fdr 5e-05), [[GLB1L2]] (-0.45, fdr 2e-04).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4253.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.87×** | +10.0 | 1e-20 | 34/38 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.88×** | +9.6 | 2e-19 | 37/47 (HEC-1-A, SW480, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +9.0 | 4e-17 | 29/31 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.09×** | +8.0 | 2e-13 | 40/47 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.74×** | +5.6 | 3e-06 | 18/34 (A549, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.64×** | +5.2 | 2e-05 | 33/47 (COLO 205, HOP62, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.54×** | +4.7 | 2e-04 | 24/46 (NCI-H23, PANC-1, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +4.4 | 7e-04 | 29/47 (A-172, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.4 | 7e-04 | 24/44 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.46×** | +4.1 | 0.002 | 23/44 (A-172, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.028 | 22/48 (SNU-423, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.034 | 16/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.39×** | +3.1 | 0.071 | 19/48 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **1.34×** | +3.1 | 0.087 | 15/43 (A549, BT-474, …) | top dose only |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.091 | 15/48 (HEC-1-A, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4253.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Tadalafil (drug)]] 5 µM in 1 line (SNU-423 0.135×); [[Orlistat (drug)]] 0.05 µM in 1 line (SW48 0.0857×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.699×** | -5.5 | 3e-05 | 34/48 (KATO III, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4253. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +10.4) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 17.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +9.2) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H1573 (line)]] | alt | 19.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.84× (z +11.2) | — |
| [[PANC-1 (line)]] | alt | 17.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +8.5) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[SNU-423 (line)]] | alt | 10.1 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.135× (z -9.4) |
| [[SW48 (line)]] | wt | 14.3 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0857× (z -8.8) |
| [[A-172 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4253), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FICD]] | +0.64 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[DERL2]] | +0.63 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[UBE2J1]] | +0.62 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[CYB561]] | +0.62 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[SEC23B]] | +0.61 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[SLC33A1]] | +0.61 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[DXO]] | +0.60 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[UFL1]] | +0.59 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[MTO1]] | +0.59 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ALG12]] | +0.58 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[XBP1]] | +0.58 | +0.69 / +0.46 | both halves | 2e-05 |  |
| [[LSM1]] | +0.58 | +0.48 / +0.64 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HPSE]] | -0.53 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[GLB1L2]] | -0.45 | -0.54 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.530). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.4, -39.3); signed map (-56.7, 12.8). **Vector** length 64.8, 12.6% of its response variance represented; |z| ≥ 3 in 666 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +6.3 | +9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +9.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +3.1 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +0.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.5 | +0.6 |
|  | [[Belumosudil (mesylate) (drug)]] 5 µM |  | +1.5 | +1.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +1.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.3 | -0.5 |
|  | [[Busulfan (drug)]] 5 µM |  | -1.2 | -1.8 |
|  | [[Norepinephrine (hydrochloride) (drug)]] 5 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:49,700,934-49,709,014 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UGTREL1, AXER |
| Gene groups (HGNC) | Solute carrier family 35 |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [P78383](https://www.uniprot.org/uniprotkb/P78383) (Solute carrier family 35 member B1):

> ATP:ADP antiporter that catalyzes the exchange of ATP and ADP across the endoplasmic reticulum (ER) membrane. Imports ATP from the cytosol to the ER lumen and exports ADP in the opposite direction. Regulates ER energy metabolism and protein biogenesis. Appears to be part of a calcium-dependent ER to cytosol low energy response axis, where calcium efflux from ER to the cytosol triggers ATP import into the ER lumen to maintain sufficient ATP supply. Provides ATP to ER chaperone HSPA5 that drives …

**Summary**, from NCBI Gene [10237](https://www.ncbi.nlm.nih.gov/gene/10237):

> This gene encodes a nucleotide sugar transporter which is a member of solute carrier family 35. The transporters in this family are highly conserved hydrophobic proteins with multiple transmembrane domains. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:20798](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20798) · Entrez [10237](https://www.ncbi.nlm.nih.gov/gene/10237) · UniProt [P78383](https://www.uniprot.org/uniprotkb/P78383) · Ensembl [ENSG00000121073](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121073)

## Data

Gene col 4253: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4253); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4253, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4253]; `tensor/DDL_lfc|DDL_z.npy` [4253]; `embed/gene_vectors.npy` [4253]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4253 or target_col == 4253). Every well: [[SLC35B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
