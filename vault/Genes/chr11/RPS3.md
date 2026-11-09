---
symbol: "RPS3"
type: "gene"
col: 7359
ensembl_id: "ENSG00000149273"
name: "ribosomal protein S3"
location: "11q13.4"
module: 43
arm: "+"
pooled_cpm: 511.27
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# RPS3

*ribosomal protein S3* — 11q13.4

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.05× (z +7.0, q 1e-09, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 6.45×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL9]] (+0.97, fdr 7e-06, ⚠ RPL9 in the vector space only through flagged drug-doses), [[RPL35A]] (+0.96, fdr 7e-06), [[RPS17]] (+0.96, fdr 7e-06, ⚠ RPS17 in the vector space only through flagged drug-doses), [[RPL31]] (+0.96, fdr 7e-06), [[RPL26]] (+0.96, fdr 7e-06); moves opposite to [[PSME3]] (-0.70, fdr 1e-05), [[PNPO]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7359.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 6.45×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.05×** | +7.0 | 1e-09 | 48/49 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.38×** | +5.4 | 2e-05 | 42/44 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.86×** | +4.0 | 0.010 | 45/48 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.94×** | +4.0 | 0.010 | 42/45 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.83×** | +3.9 | 0.010 | 44/48 (NCI-H460, NCI-H1573, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7359.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.698× | -3.2 | 0.41 | 34/48 (A-427, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7359. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 221 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.45× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 279 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 565 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 245 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 493 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 447 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 495 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 659 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 440 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 233 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 456 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 419 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 374 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 492 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 409 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 436 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 329 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 448 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 395 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 719 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 361 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 338 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 621 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 792 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 728 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 521 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 521 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 684 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 297 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 455 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 375 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 717 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 615 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 465 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 572 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 357 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 661 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 620 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 669 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 269 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 468 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 926 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 486 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 548 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 273 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 421 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 313 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 516 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 732 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 665 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7359), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 23 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL9]] ⚠ | +0.97 | +0.96 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL35A]] | +0.96 | +0.93 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS17]] ⚠ | +0.96 | +0.94 / +0.96 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL31]] | +0.96 | +0.91 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL26]] | +0.96 | +0.93 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL23]] | +0.96 | +0.94 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.95 | +0.91 / +0.96 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL18]] ⚠ | +0.95 | +0.92 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS12]] | +0.95 | +0.94 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL37A]] ⚠ | +0.94 | +0.90 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS27A]] ⚠ | +0.94 | +0.89 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL13]] | +0.94 | +0.89 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.94 | +0.88 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[RPL36]] | +0.94 | +0.89 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL17]] | +0.93 | +0.87 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS14]] | +0.93 | +0.85 / +0.94 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL5]] | +0.93 | +0.88 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3]] | -0.70 | -0.51 / -0.76 | both halves | 1e-05 |  |
| [[PNPO]] | -0.68 | -0.56 / -0.67 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.963). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-45.3, -27.5); signed map (-60.0, -4.1). **Vector** length 88.5, 61.6% of its response variance represented; |z| ≥ 3 in 478 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.86 to 34); *oxidative phosphorylation* (hallmark, mean cos +0.72 to 9); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.65 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +1.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +1.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.4 | +1.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.4 | +0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | -0.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +2.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -7.2 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -6.9 | +4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -6.9 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.6 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | +1.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.2 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | +0.4 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.0 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:75,399,515-75,422,280 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ26283, FLJ27450, MGC87870, S3, uS3 |
| Gene groups (HGNC) | S ribosomal proteins; Small nucleolar RNA protein coding host genes; DNA-(apurinic or apyrimidinic site) lyases |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 51 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P23396](https://www.uniprot.org/uniprotkb/P23396) (Small ribosomal subunit protein uS3):

> Component of the small ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. Has endonuclease activity and plays a role in repair of damaged DNA. Cleaves phosphodiester bonds of DNAs containing altered bases with broad specificity and cleaves supercoiled DNA more efficiently than relaxed DNA. Displays high binding affinity for 7,8-dihydro-8-oxoguanine (8-oxoG), a common DNA lesion caused by reactive oxygen species (ROS). Has …

**Summary**, from NCBI Gene [6188](https://www.ncbi.nlm.nih.gov/gene/6188):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 40S subunit, where it forms part of the domain where translation is initiated. The protein belongs to the S3P family of ribosomal proteins. Studies of the mouse and rat proteins have demonstrated that the protein …

**Accessions** — [HGNC:10420](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10420) · Entrez [6188](https://www.ncbi.nlm.nih.gov/gene/6188) · UniProt [P23396](https://www.uniprot.org/uniprotkb/P23396) · Ensembl [ENSG00000149273](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149273)

## Data

Gene col 7359: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7359); `tables/drug_effects.parquet` (6 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7359, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7359]; `tensor/DDL_lfc|DDL_z.npy` [7359]; `embed/gene_vectors.npy` [7359]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7359 or target_col == 7359). Every well: [[RPS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
