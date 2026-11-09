---
symbol: "RPS12"
type: "gene"
col: 3354
ensembl_id: "ENSG00000112306"
name: "ribosomal protein S12"
location: "6q23.2"
module: 43
arm: "+"
pooled_cpm: 496.53
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPS12

*ribosomal protein S12* — 6q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.56× (z +6.5, q 4e-08, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.54× (z +3.9, q 0.011, up in 38 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.51×).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C-33 A 0.303×, RKO 0.369×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPLP1]] (+0.96, fdr 7e-06), [[RPL35A]] (+0.96, fdr 7e-06), [[RPS8]] (+0.96, fdr 7e-06); moves opposite to [[CEP41]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3354.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.51×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.56×** | +6.5 | 4e-08 | 48/49 (A-172, LoVo, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.80×** | +6.2 | 1e-07 | 43/44 (LoVo, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.96×** | +4.2 | 0.004 | 43/48 (SW 900, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.16×** | +4.2 | 0.005 | 42/45 (A-172, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +4.0 | 0.006 | 45/47 (MIA PaCa-2, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +3.9 | 0.011 | 38/49 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.73×** | +3.5 | 0.044 | 40/48 (COLO 205, NCI-H460, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3354.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C-33 A 0.303×, RKO 0.369×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.682× | -3.3 | 0.46 | 34/48 (C-33 A, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Folic acid (drug)]] 5 µM |  | 0.705× | -3.1 | 0.65 | 46/48 (AsPC-1, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3354. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 473 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 475 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +8.6) | — |
| [[RKO (line)]] | wt | 664 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -8.7) |
| [[A-172 (line)]] | wt | 193 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 634 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 301 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 388 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 509 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 404 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 290 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 321 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 341 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 440 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 345 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 403 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 448 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 786 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 339 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 390 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 351 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 606 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 475 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 424 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1,267 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 711 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 686 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 562 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 403 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 405 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 679 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 445 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 463 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 618 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 582 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 555 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 463 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 542 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 309 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 262 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 403 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 437 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 734 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 305 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 430 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 470 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 474 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 701 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 581 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3354), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 23 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPLP1]] | +0.96 | +0.94 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL35A]] | +0.96 | +0.93 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.96 | +0.91 / +0.97 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL26]] | +0.95 | +0.92 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS27]] | +0.95 | +0.91 / +0.96 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS17]] ⚠ | +0.95 | +0.94 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS3]] ⚠ | +0.95 | +0.94 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL9]] ⚠ | +0.95 | +0.90 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS19]] | +0.95 | +0.91 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL31]] | +0.95 | +0.90 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.94 | +0.88 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL37A]] ⚠ | +0.94 | +0.89 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL23]] | +0.93 | +0.90 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL12]] | +0.93 | +0.87 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL19]] | +0.93 | +0.85 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL36]] | +0.92 | +0.87 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 999 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP41]] | -0.68 | -0.52 / -0.69 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.957). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.1, -27.4); signed map (-59.7, -4.2). **Vector** length 87.6, 59.4% of its response variance represented; |z| ≥ 3 in 455 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.86 to 34); *MYC targets v1* (hallmark, mean cos +0.66 to 17); *oxidative phosphorylation* (hallmark, mean cos +0.69 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +1.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +0.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | -0.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.2 | +1.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.2 | +0.4 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +2.1 | -0.4 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -7.3 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -7.1 | +4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -7.0 | +6.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | -3.8 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | +0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | +0.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.1 | +0.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.0 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.2 — chr6:132,814,569-132,817,564 (+) |
| Ensembl biotype | protein_coding |
| Also known as | S12, eS12 |
| Gene groups (HGNC) | S ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Hallmark sets | P53_PATHWAY |
| Reactome | 51 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P25398](https://www.uniprot.org/uniprotkb/P25398) (Small ribosomal subunit protein eS12):

> Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal RNA by the RNA exosome. Subunit of the 40S ribosomal complex (By similarity).

**Summary**, from NCBI Gene [6206](https://www.ncbi.nlm.nih.gov/gene/6206):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 40S subunit. The protein belongs to the S12E family of ribosomal proteins. It is located in the cytoplasm. Increased expression of this gene in colorectal cancers compared to matched normal colonic mucosa has …

**Accessions** — [HGNC:10385](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10385) · Entrez [6206](https://www.ncbi.nlm.nih.gov/gene/6206) · UniProt [P25398](https://www.uniprot.org/uniprotkb/P25398) · Ensembl [ENSG00000112306](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112306)

## Data

Gene col 3354: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3354); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3354, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3354]; `tensor/DDL_lfc|DDL_z.npy` [3354]; `embed/gene_vectors.npy` [3354]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3354 or target_col == 3354). Every well: [[RPS12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
