---
symbol: "RPL26"
type: "gene"
col: 8466
ensembl_id: "ENSG00000161970"
name: "ribosomal protein L26"
location: "17p13.1"
module: 43
arm: "+"
pooled_cpm: 412.85
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPL26

*ribosomal protein L26* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.85× (z +6.2, q 4e-07, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (Hs 766T 3.84×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.33×).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.617× (z -4.5, q 0.004, down in 41 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (C-33 A 0.306×, SNU-1 0.333×, RKO 0.365×, SHP-77 0.392×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL35A]] (+0.97, fdr 7e-06), [[RPL34]] (+0.97, fdr 7e-06), [[RPL31]] (+0.97, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8466.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (Hs 766T 3.84×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.33×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.85×** | +6.2 | 4e-07 | 49/49 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.31×** | +5.3 | 3e-05 | 42/44 (Hs 766T, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.96×** | +4.5 | 0.001 | 47/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +3.5 | 0.055 | 40/47 (CFPAC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.77×** | +3.5 | 0.055 | 38/45 (Hs 766T, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | 1.65× | +3.2 | 0.13 | 38/47 (COLO 205, Hs 766T, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.40× | +3.1 | 0.13 | 30/49 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | 1.59× | +3.1 | 0.15 | 36/48 (NCI-H460, NCI-H1792, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8466.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (C-33 A 0.306×, SNU-1 0.333×, RKO 0.365×, SHP-77 0.392×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.617×** | -4.5 | 0.004 | 41/48 (C-33 A, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8466. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 445 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -11.3) |
| [[Hs 766T (line)]] | wt | 305 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.84× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2347 (line)]] | alt | 297 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +8.5) | — |
| [[RKO (line)]] | wt | 563 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -9.1) |
| [[SHP-77 (line)]] | alt | 398 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -8.9) |
| [[SNU-1 (line)]] | wt | 522 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -10.0) |
| [[A-172 (line)]] | wt | 266 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 425 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 453 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 582 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 427 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 368 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 201 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 228 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 377 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 223 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 439 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 392 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 456 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 276 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 385 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 361 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 345 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 326 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 479 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 745 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 501 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 540 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 569 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 412 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 373 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 525 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 608 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 481 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 355 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 356 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 357 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 448 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 266 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 365 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 467 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 323 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 686 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 617 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8466), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 23 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL35A]] | +0.97 | +0.96 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.97 | +0.96 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL31]] | +0.97 | +0.95 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL23]] | +0.97 | +0.96 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL17]] | +0.97 | +0.95 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS17]] ⚠ | +0.97 | +0.94 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 998; ⚠ in the vector space only through flagged drug-doses |
| [[RPL13]] | +0.97 | +0.95 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL9]] ⚠ | +0.97 | +0.95 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS8]] | +0.96 | +0.94 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL35]] ⚠ | +0.96 | +0.91 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS3]] ⚠ | +0.96 | +0.93 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS14]] | +0.95 | +0.93 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS12]] | +0.95 | +0.92 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL12]] | +0.95 | +0.93 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL11]] | +0.95 | +0.95 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL19]] | +0.95 | +0.90 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.982). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.4, -27.6); signed map (-60.1, -4.3). **Vector** length 97.1, 64.5% of its response variance represented; |z| ≥ 3 in 483 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.82 to 19); *Translation initiation complex formation* (reactome, mean cos +0.79 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.79 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +1.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.0 | -0.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.8 | +2.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.5 | +0.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.5 | +1.5 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.5 | +1.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -6.8 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -6.7 | +3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -6.4 | +5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.5 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -0.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.5 | -0.2 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.4 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L26 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:8,377,516-8,383,213 (-) |
| Ensembl biotype | protein_coding |
| Also known as | L26, uL24 |
| Gene groups (HGNC) | L ribosomal proteins |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P61254](https://www.uniprot.org/uniprotkb/P61254) (Large ribosomal subunit protein uL24):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6154](https://www.ncbi.nlm.nih.gov/gene/6154):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L24P family of ribosomal proteins. It is located in the cytoplasm. As is typical for genes encoding ribosomal proteins, there are multiple processed pseudogenes of this …

**Accessions** — [HGNC:10327](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10327) · Entrez [6154](https://www.ncbi.nlm.nih.gov/gene/6154) · UniProt [P61254](https://www.uniprot.org/uniprotkb/P61254) · Ensembl [ENSG00000161970](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161970)

## Data

Gene col 8466: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8466); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8466, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8466]; `tensor/DDL_lfc|DDL_z.npy` [8466]; `embed/gene_vectors.npy` [8466]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8466 or target_col == 8466). Every well: [[RPL26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
