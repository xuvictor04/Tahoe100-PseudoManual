---
symbol: "RPL35A"
type: "gene"
col: 11339
ensembl_id: "ENSG00000182899"
name: "ribosomal protein L35a"
location: "3q29"
module: 43
arm: "+"
pooled_cpm: 447.63
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPL35A

*ribosomal protein L35a* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.03× (z +6.2, q 3e-07, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.542× (z -4.9, q 6e-04, down in 42 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 0.310×, SNU-1 0.314×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL31]] (+0.98, fdr 7e-06), [[RPL9]] (+0.97, fdr 7e-06, ⚠ RPL9 in the vector space only through flagged drug-doses), [[RPL26]] (+0.97, fdr 7e-06), [[RPL34]] (+0.97, fdr 7e-06); moves opposite to [[PNPO]] (-0.73, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CSTB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11339.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.03×** | +6.2 | 3e-07 | 48/49 (A549, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.35×** | +4.7 | 8e-04 | 43/44 (C-33 A, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.91×** | +3.7 | 0.044 | 45/48 (A-172, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | 1.79× | +3.3 | 0.11 | 40/48 (NCI-H460, COLO 205, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | 1.87× | +3.3 | 0.11 | 39/45 (SNU-423, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.80× | +3.2 | 0.12 | 43/47 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11339.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 0.310×, SNU-1 0.314×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.542×** | -4.9 | 6e-04 | 42/48 (RKO, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11339. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 557 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -8.8) |
| [[SNU-1 (line)]] | wt | 540 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -8.6) |
| [[A-172 (line)]] | wt | 246 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 445 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 386 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 297 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 362 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 352 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 359 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 247 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 189 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 429 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 429 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 319 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 442 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 473 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 550 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 404 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 370 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 280 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 467 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 465 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 380 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 433 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 564 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 625 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 524 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 523 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 605 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 378 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 334 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 366 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 360 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 409 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 619 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 399 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 480 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 378 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 631 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 577 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 339 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 403 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 379 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 308 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 323 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 341 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 501 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 650 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 639 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11339), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 23 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL31]] | +0.98 | +0.95 / +0.98 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL9]] ⚠ | +0.97 | +0.95 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL26]] | +0.97 | +0.96 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.97 | +0.96 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS17]] ⚠ | +0.97 | +0.93 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL23]] | +0.97 | +0.95 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS3]] ⚠ | +0.96 | +0.93 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS8]] | +0.96 | +0.94 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS12]] | +0.96 | +0.93 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS27]] | +0.96 | +0.93 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS27A]] ⚠ | +0.96 | +0.91 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL36]] | +0.95 | +0.91 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS14]] | +0.95 | +0.91 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPLP1]] | +0.95 | +0.94 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL17]] | +0.94 | +0.90 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS19]] | +0.94 | +0.93 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNPO]] | -0.73 | -0.67 / -0.72 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSTB]] | B | CSTB activity raises RPL35A's level | lines that do not express CSTB (8) vs lines expressing it (42) | 1.43× lower at baseline in the lines without CSTB | 0.047 | ⚠ within organs, on part of the lines; also absent: PLAUR, PLS3, ADGRE5; maybe low, not absent |
| [[FAM111A]] | C | FAM111A activity raises RPL35A's level | lines that do not express FAM111A (3) vs lines expressing it (47) | 1.79× lower at baseline in the lines without FAM111A | 0.019 | ⚠ few lines (3 vs 47); across organs; also absent: FXYD5, ACCS, TFAP2A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.971). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.1, -27.1); signed map (-59.8, -4.0). **Vector** length 89.8, 60.8% of its response variance represented; |z| ≥ 3 in 345 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.80 to 19); *Translation initiation complex formation* (reactome, mean cos +0.76 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.76 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +1.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.8 | -0.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.7 | +1.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.2 | +1.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.1 | +0.4 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.1 | +0.7 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -6.9 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -6.9 | +3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -6.7 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.5 | -4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | +1.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.4 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -0.0 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.2 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L35a |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:197,950,190-197,956,610 (+) |
| Ensembl biotype | protein_coding |
| Also known as | L35A, eL33, GIG33 |
| Gene groups (HGNC) | L ribosomal proteins |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P18077](https://www.uniprot.org/uniprotkb/P18077) (Large ribosomal subunit protein eL33):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. Required for the proliferation and viability of hematopoietic cells.

**Summary**, from NCBI Gene [6165](https://www.ncbi.nlm.nih.gov/gene/6165):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L35AE family of ribosomal proteins. It is located in the cytoplasm. The rat protein has been shown to bind to both initiator and elongator tRNAs, and thus, it is located at …

**Accessions** — [HGNC:10345](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10345) · Entrez [6165](https://www.ncbi.nlm.nih.gov/gene/6165) · UniProt [P18077](https://www.uniprot.org/uniprotkb/P18077) · Ensembl [ENSG00000182899](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182899)

## Data

Gene col 11339: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11339); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11339, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11339]; `tensor/DDL_lfc|DDL_z.npy` [11339]; `embed/gene_vectors.npy` [11339]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11339 or target_col == 11339). Every well: [[RPL35A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL35A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
