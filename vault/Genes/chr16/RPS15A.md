---
symbol: "RPS15A"
type: "gene"
col: 5559
ensembl_id: "ENSG00000134419"
name: "ribosomal protein S15a"
location: "16p12.3"
module: 43
arm: "+"
pooled_cpm: 76.01
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPS15A

*ribosomal protein S15a* — 16p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.86× (z +8.2, q 2e-13, up in 46 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Peretinoin (drug)]] 0.05 µM: 1.75× (z +3.7, q 0.020, up in 40 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.0970×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL11]] (+0.87, fdr 7e-06), [[RPL5]] (+0.86, fdr 7e-06), [[RPL32]] (+0.86, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5559.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.86×** | +8.2 | 2e-13 | 46/48 (LoVo, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.24×** | +6.0 | 5e-07 | 33/44 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.85×** | +4.8 | 3e-04 | 37/48 (LS 180, NCI-H460, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.79×** | +4.3 | 0.002 | 41/47 (COLO 205, LoVo, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.91×** | +4.2 | 0.003 | 35/45 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.70×** | +4.1 | 0.004 | 40/47 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.75×** | +3.7 | 0.020 | 40/48 (SW480, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.59×** | +3.6 | 0.024 | 36/48 (A-172, COLO 205, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.58×** | +3.6 | 0.024 | 37/48 (HT-29, KATO III, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.53×** | +3.3 | 0.059 | 27/48 (LS 180, KATO III, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.52×** | +3.2 | 0.060 | 39/48 (COLO 205, A-172, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +3.2 | 0.061 | 32/48 (KATO III, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.51×** | +3.2 | 0.062 | 37/48 (C32, NCI-H23, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.1 | 0.072 | 33/47 (MIA PaCa-2, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.14×** | +3.0 | 0.088 | 27/48 (SW48, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.0970×; ⚠ cell-cycle shift, explains ~0% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5559. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 80.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[AN3 CA (line)]] | alt | 86.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0970× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 123 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[RKO (line)]] | wt | 94.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SW480 (line)]] | alt | 80.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A-172 (line)]] | wt | 57.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 72.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 81.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 89.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 94.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 78.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 114 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 73.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 64.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 95.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 83.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 90.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 86.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 110 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5559), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 21 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL11]] | +0.87 | +0.80 / +0.87 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL5]] | +0.86 | +0.79 / +0.88 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL32]] | +0.86 | +0.82 / +0.85 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL21]] ⚠ | +0.86 | +0.82 / +0.87 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL17]] | +0.86 | +0.83 / +0.83 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 997 |
| [[RPS10]] | +0.85 | +0.80 / +0.84 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL34]] | +0.85 | +0.78 / +0.84 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL13A]] | +0.85 | +0.85 / +0.81 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 998 |
| [[RPL13]] | +0.84 | +0.79 / +0.82 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 998 |
| [[RPL37]] ⚠ | +0.84 | +0.77 / +0.85 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 998; ⚠ in the vector space only through flagged drug-doses |
| [[RPL26]] | +0.84 | +0.76 / +0.84 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL38]] | +0.83 | +0.78 / +0.82 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL27]] | +0.83 | +0.77 / +0.81 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS24]] | +0.83 | +0.77 / +0.81 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.854). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.2, -28.7); signed map (-61.4, -4.9). **Vector** length 79.3, 30.6% of its response variance represented; |z| ≥ 3 in 554 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.79 to 34); *MYC targets v1* (hallmark, mean cos +0.62 to 17); *oxidative phosphorylation* (hallmark, mean cos +0.56 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +1.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +0.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.8 | +0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +2.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +2.5 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +3.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.1 | +0.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -0.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | +1.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | +1.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -0.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.9 | +0.3 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.9 | -0.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.9 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S15a |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.3 — chr16:18,781,295-18,790,383 (-) |
| Ensembl biotype | protein_coding |
| Also known as | S15A, uS8 |
| Gene groups (HGNC) | S ribosomal proteins |
| Reactome | 51 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P62244](https://www.uniprot.org/uniprotkb/P62244) (Small ribosomal subunit protein uS8):

> Component of the small ribosomal subunit. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal RNA by the RNA exosome. Required for proper …

**Summary**, from NCBI Gene [6210](https://www.ncbi.nlm.nih.gov/gene/6210):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 40S subunit. The protein belongs to the S8P family of ribosomal proteins. It is located in the cytoplasm. As is typical for genes encoding ribosomal proteins, there are multiple processed pseudogenes of this gene …

**Accessions** — [HGNC:10389](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10389) · Entrez [6210](https://www.ncbi.nlm.nih.gov/gene/6210) · UniProt [P62244](https://www.uniprot.org/uniprotkb/P62244) · Ensembl [ENSG00000134419](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134419)

## Data

Gene col 5559: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5559); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5559, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5559]; `tensor/DDL_lfc|DDL_z.npy` [5559]; `embed/gene_vectors.npy` [5559]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5559 or target_col == 5559). Every well: [[RPS15A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS15A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
