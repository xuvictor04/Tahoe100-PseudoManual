---
symbol: "SEC61G"
type: "gene"
col: 5319
ensembl_id: "ENSG00000132432"
name: "SEC61 translocon subunit gamma"
location: "7p11.2"
module: 48
arm: "+"
pooled_cpm: 127.18
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# SEC61G

*SEC61 translocon subunit gamma* — 7p11.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.435× (z -7.1, q 5e-10, down in 46 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (SNU-1 0.136×, NCI-H2347 0.238×, SK-MEL-2 0.268×, H4 0.276×, …); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SW 1271 0.0615×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.177×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMTOR5]] (+0.80, fdr 7e-06), [[ATP5MK]] (+0.79, fdr 7e-06), [[ROMO1]] (+0.79, fdr 7e-06); moves opposite to [[SGPL1]] (-0.68, fdr 4e-05), [[FGD5-AS1]] (-0.67, fdr 7e-06), [[EWSR1]] (-0.66, fdr 9e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5319.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | 1.65× | +3.1 | 0.95 | 34/48 (PANC-1, HCT15, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5319.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (SNU-1 0.136×, NCI-H2347 0.238×, SK-MEL-2 0.268×, H4 0.276×, …); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SW 1271 0.0615×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.177×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.435×** | -7.1 | 5e-10 | 46/48 (SNU-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | 0.557× | -3.6 | 0.11 | 36/48 (AsPC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | 0.351× | -3.3 | 0.12 | 42/50 (NCI-H2030, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.351× | -3.3 | 0.12 | 40/49 (A-427, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.357× | -3.3 | 0.12 | 43/49 (HEC-1-A, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.74 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5319. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 102 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -14.8) |
| [[CFPAC-1 (line)]] | alt | 107 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -8.6) |
| [[H4 (line)]] | wt | 328 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -10.0) |
| [[HS-578T (line)]] | alt | 172 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -9.6) |
| [[J82 (line)]] | alt | 103 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 116 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 89.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 200 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 117 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -10.4) |
| [[SW 1271 (line)]] | alt | 99.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0615× (z -9.2) ⚠ toxic |
| [[A-172 (line)]] | wt | 215 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 89.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 138 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 94.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 126 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 96.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 75.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 130 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 67.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 132 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 98.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 92.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 193 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 174 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 99.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 545 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 97.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 79.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 99.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 93.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 118 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5319), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 15 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMTOR5]] | +0.80 | +0.76 / +0.81 | both halves | 7e-06 |  |
| [[ATP5MK]] | +0.79 | +0.69 / +0.81 | both halves | 7e-06 |  |
| [[ROMO1]] | +0.79 | +0.68 / +0.81 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.78 | +0.63 / +0.80 | both halves | 7e-06 |  |
| [[RPL36AL]] ⚠ | +0.78 | +0.67 / +0.79 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 897; ⚠ in the vector space only through flagged drug-doses |
| [[TMEM258]] | +0.78 | +0.68 / +0.82 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 896 |
| [[COX6B1]] | +0.77 | +0.62 / +0.78 | both halves | 7e-06 |  |
| [[NUDT22]] | +0.76 | +0.55 / +0.85 | both halves | 1e-05 |  |
| [[SSR4]] | +0.76 | +0.71 / +0.80 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 961 |
| [[NDUFA1]] | +0.75 | +0.64 / +0.81 | both halves | 7e-06 |  |
| [[MYDGF]] | +0.75 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[ATP5MJ]] | +0.74 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[RABAC1]] | +0.73 | +0.58 / +0.80 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGPL1]] | -0.68 | -0.42 / -0.75 | both halves | 4e-05 |  |
| [[FGD5-AS1]] | -0.67 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[EWSR1]] | -0.66 | -0.37 / -0.75 | both halves | 9e-05 |  |
| [[NELFCD]] | -0.66 | -0.41 / -0.72 | both halves | 4e-05 |  |
| [[SFPQ]] | -0.64 | -0.43 / -0.70 | both halves | 3e-05 |  |
| [[GMFB]] | -0.63 | -0.46 / -0.67 | both halves | 3e-05 |  |
| [[LIN7C]] | -0.63 | -0.40 / -0.72 | both halves | 5e-05 |  |
| [[CAPRIN1]] | -0.63 | -0.42 / -0.67 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.787). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-44.0, -21.7); signed map (-32.9, 10.0). **Vector** length 97.9, 50.9% of its response variance represented; |z| ≥ 3 in 388 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.59 to 31); *Respiratory electron transport* (reactome, mean cos +0.57 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.60 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +0.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +0.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +0.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | -1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +1.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +1.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.8 | +1.9 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | +1.7 | +0.9 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -6.9 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.9 | +1.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.7 | -0.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.8 | -1.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.2 | -1.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -3.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | -0.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.8 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | SEC61 translocon subunit gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p11.2 — chr7:54,752,250-54,759,974 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SSS1 |
| Gene groups (HGNC) | Sec61 complex subunits |
| Reactome | 7 pathways, smallest: Insertion of tail-anchored proteins into the endoplasmic reticulum membrane; ER-Phagosome pathway; Antigen processing-Cross presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [P60059](https://www.uniprot.org/uniprotkb/P60059) (Protein transport protein Sec61 subunit gamma):

> Component of SEC61 channel-forming translocon complex that mediates transport of signal peptide-containing precursor polypeptides across the endoplasmic reticulum (ER) (By similarity). Forms a ribosome receptor and a gated pore in the ER membrane, both functions required for cotranslational translocation of nascent polypeptides (By similarity). The SEC61 channel is also involved in ER membrane insertion of transmembrane proteins: it mediates membrane insertion of the first few transmembrane …

**Summary**, from NCBI Gene [23480](https://www.ncbi.nlm.nih.gov/gene/23480):

> The Sec61 complex is the central component of the protein translocation apparatus of the endoplasmic reticulum (ER) membrane. Oligomers of the Sec61 complex form a transmembrane channel where proteins are translocated across and integrated into the ER membrane. This complex consists of three membrane proteins- alpha, beta, and gamma. This gene encodes the gamma-subunit protein. Alternatively spliced transcript variants encoding the same protein have been identified. [provided by RefSeq, Jul …

**Accessions** — [HGNC:18277](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18277) · Entrez [23480](https://www.ncbi.nlm.nih.gov/gene/23480) · UniProt [P60059](https://www.uniprot.org/uniprotkb/P60059) · Ensembl [ENSG00000132432](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132432)

## Data

Gene col 5319: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5319); `tables/drug_effects.parquet` (6 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5319, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5319]; `tensor/DDL_lfc|DDL_z.npy` [5319]; `embed/gene_vectors.npy` [5319]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5319 or target_col == 5319). Every well: [[SEC61G — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC61G.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
