---
symbol: "RPLP1"
type: "gene"
col: 6075
ensembl_id: "ENSG00000137818"
name: "ribosomal protein lateral stalk subunit P1"
location: "15q23"
module: 43
arm: "+"
pooled_cpm: 488.72
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPLP1

*ribosomal protein lateral stalk subunit P1* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.34× (z +7.6, q 2e-11, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.49× (z +3.4, q 0.057, up in 38 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 4.13×, C-33 A 4.51×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 6.49×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.552× (z -4.9, q 4e-04, down in 41 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SNU-1 0.255×, C-33 A 0.303×, H4 0.295×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS12]] (+0.96, fdr 7e-06), [[RPL35A]] (+0.95, fdr 7e-06), [[RPL26]] (+0.94, fdr 7e-06); moves opposite to [[SLC35A4]] (-0.72, fdr 7e-06), [[CEP41]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6075.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 4.13×, C-33 A 4.51×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 6.49×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **4.34×** | +7.6 | 2e-11 | 49/49 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.35×** | +6.9 | 1e-09 | 44/44 (KATO III, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.45×** | +4.9 | 2e-04 | 45/45 (KATO III, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +4.8 | 2e-04 | 47/47 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **2.24×** | +4.8 | 2e-04 | 47/48 (SW 900, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.02×** | +4.2 | 0.003 | 46/48 (NCI-H460, COLO 205, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.057 | 38/49 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6075.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SNU-1 0.255×, C-33 A 0.303×, H4 0.295×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.552×** | -4.9 | 4e-04 | 41/48 (SNU-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6075. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 490 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.51× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -9.8) |
| [[H4 (line)]] | wt | 460 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -9.3) |
| [[KATO III (line)]] | alt | 454 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.13× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1573 (line)]] | alt | 451 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.49× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SNU-1 (line)]] | wt | 457 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -10.8) |
| [[A-172 (line)]] | wt | 221 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 412 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 368 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 665 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 544 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 349 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 334 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 520 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 464 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 247 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 383 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 375 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 489 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 506 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 383 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 279 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 722 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 482 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 277 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1,421 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 570 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 560 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 385 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 491 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 583 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 443 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 398 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 612 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 611 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 548 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 424 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 513 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 529 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 605 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 421 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 405 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 372 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 296 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 516 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 322 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 456 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 640 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 456 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6075), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 22 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS12]] | +0.96 | +0.94 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL35A]] | +0.95 | +0.94 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL26]] | +0.94 | +0.92 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 998 |
| [[RPS8]] | +0.94 | +0.91 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.93 | +0.91 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL9]] ⚠ | +0.93 | +0.90 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS27]] | +0.93 | +0.90 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL31]] | +0.93 | +0.92 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS19]] | +0.93 | +0.93 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS17]] ⚠ | +0.93 | +0.90 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL12]] | +0.93 | +0.90 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS20]] | +0.92 | +0.89 / +0.92 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS14]] | +0.92 | +0.91 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL13]] | +0.91 | +0.90 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35A4]] | -0.72 | -0.71 / -0.63 | both halves | 7e-06 |  |
| [[CEP41]] | -0.69 | -0.58 / -0.71 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.947). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.3, -27.3); signed map (-59.7, -4.4). **Vector** length 91.3, 64.0% of its response variance represented; |z| ≥ 3 in 465 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.80 to 19); *Translation initiation complex formation* (reactome, mean cos +0.75 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.75 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.5 | +0.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.4 | +1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +0.4 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +2.1 | -0.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.1 | +0.3 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -7.7 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -7.4 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -7.3 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | -2.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -0.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.9 | +1.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.3 | +1.9 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein lateral stalk subunit P1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:69,452,814-69,456,205 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LP1, P1 |
| Gene groups (HGNC) | L ribosomal proteins |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P05386](https://www.uniprot.org/uniprotkb/P05386) (Large ribosomal subunit protein P1):

> Plays an important role in the elongation step of protein synthesis.

**Summary**, from NCBI Gene [6176](https://www.ncbi.nlm.nih.gov/gene/6176):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal phosphoprotein that is a component of the 60S subunit. The protein, which is a functional equivalent of the E. coli L7/L12 ribosomal protein, belongs to the L12P family of ribosomal proteins. It plays an important role in the elongation step of …

**Accessions** — [HGNC:10372](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10372) · Entrez [6176](https://www.ncbi.nlm.nih.gov/gene/6176) · UniProt [P05386](https://www.uniprot.org/uniprotkb/P05386) · Ensembl [ENSG00000137818](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137818)

## Data

Gene col 6075: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6075); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6075, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6075]; `tensor/DDL_lfc|DDL_z.npy` [6075]; `embed/gene_vectors.npy` [6075]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6075 or target_col == 6075). Every well: [[RPLP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPLP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
