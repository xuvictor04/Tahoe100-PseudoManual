---
symbol: "RPS19"
type: "gene"
col: 2590
ensembl_id: "ENSG00000105372"
name: "ribosomal protein S19"
location: "19q13.2"
module: 43
arm: "+"
pooled_cpm: 409.81
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPS19

*ribosomal protein S19* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.39× (z +6.3, q 1e-07, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.574× (z -4.3, q 0.011, down in 38 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.327×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS27]] (+0.95, fdr 7e-06), [[RPS12]] (+0.95, fdr 7e-06), [[RPL35A]] (+0.94, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[APOC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2590.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.39×** | +6.3 | 1e-07 | 48/49 (COLO 205, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.38×** | +4.6 | 0.001 | 42/44 (SW480, AsPC-1, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.26×** | +4.3 | 0.003 | 47/47 (SW 900, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.13×** | +4.2 | 0.004 | 48/48 (NCI-H460, COLO 205, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **2.04×** | +3.9 | 0.009 | 44/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.11×** | +3.8 | 0.012 | 41/45 (C-33 A, SW480, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2590.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.327×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.574×** | -4.3 | 0.011 | 38/48 (C-33 A, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.551× | -3.0 | 0.58 | 46/48 (Hs 766T, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2590. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 321 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -8.6) |
| [[A-172 (line)]] | wt | 244 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 419 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 373 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 907 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 379 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 278 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 257 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 347 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 327 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 392 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 340 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 475 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 436 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 393 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 345 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 355 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 610 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 362 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 460 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 830 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 536 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 555 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 544 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 394 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 435 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 349 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 368 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 470 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 421 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 435 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 310 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 508 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 271 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 505 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 305 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 453 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 306 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 328 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 358 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 636 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 484 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2590), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 23 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS27]] | +0.95 | +0.92 / +0.97 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS12]] | +0.95 | +0.91 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL35A]] | +0.94 | +0.93 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL36]] | +0.94 | +0.93 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL9]] ⚠ | +0.93 | +0.92 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPLP1]] | +0.93 | +0.93 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.93 | +0.89 / +0.94 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS17]] ⚠ | +0.93 | +0.90 / +0.94 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL31]] | +0.93 | +0.92 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL23]] | +0.92 | +0.90 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS27A]] ⚠ | +0.92 | +0.90 / +0.93 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL37A]] ⚠ | +0.92 | +0.89 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS29]] | +0.92 | +0.89 / +0.93 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL26]] | +0.91 | +0.90 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.91 | +0.90 / +0.92 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPLP2]] | +0.90 | +0.89 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APOC1]] | B | APOC1 activity raises RPS19's level | lines that do not express APOC1 (17) vs lines expressing it (33) | 1.33× lower at baseline in the lines without APOC1 | 0.078 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, MAP3K15 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.920). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.1, -26.6); signed map (-59.5, -3.7). **Vector** length 89.1, 64.5% of its response variance represented; |z| ≥ 3 in 434 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.82 to 34); *MYC targets v1* (hallmark, mean cos +0.58 to 17); *oxidative phosphorylation* (hallmark, mean cos +0.68 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +1.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +0.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.0 | +1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | -0.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +2.0 | +4.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.0 | +1.1 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +2.0 | -0.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.9 | +0.1 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -7.3 | +6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -6.8 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -6.5 | +3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | +0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -0.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.1 | +0.6 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.9 | +0.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:41,860,255-41,872,925 (+) |
| Ensembl biotype | protein_coding |
| Also known as | S19, eS19, DBA; previously LOH19CR1 |
| Gene groups (HGNC) | S ribosomal proteins; MicroRNA protein coding host genes |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 51 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P39019](https://www.uniprot.org/uniprotkb/P39019) (Small ribosomal subunit protein eS19):

> Component of the small ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. Required for pre-rRNA processing and maturation of 40S ribosomal subunits. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and …

**Summary**, from NCBI Gene [6223](https://www.ncbi.nlm.nih.gov/gene/6223):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 40S subunit. The protein belongs to the S19E family of ribosomal proteins. It is located in the cytoplasm. Mutations in this gene cause Diamond-Blackfan anemia (DBA), a constitutional erythroblastopenia …

**Accessions** — [HGNC:10402](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10402) · Entrez [6223](https://www.ncbi.nlm.nih.gov/gene/6223) · UniProt [P39019](https://www.uniprot.org/uniprotkb/P39019) · Ensembl [ENSG00000105372](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105372)

## Data

Gene col 2590: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2590); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2590, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2590]; `tensor/DDL_lfc|DDL_z.npy` [2590]; `embed/gene_vectors.npy` [2590]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2590 or target_col == 2590). Every well: [[RPS19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
