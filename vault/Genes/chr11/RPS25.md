---
symbol: "RPS25"
type: "gene"
col: 3967
ensembl_id: "ENSG00000118181"
name: "ribosomal protein S25"
location: "11q23.3"
module: 131
arm: "+"
pooled_cpm: 294.25
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# RPS25

*ribosomal protein S25* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.10× (z +6.7, q 1e-08, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 6.63×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.525× (z -6.4, q 7e-08, down in 43 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (SNU-1 0.187×, A-427 0.252×, AN3 CA 0.296×, SW480 0.335×, …).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS21]] (+0.96, fdr 7e-06), [[RPL32]] (+0.95, fdr 7e-06), [[RPL7A]] (+0.95, fdr 7e-06); moves opposite to [[MIS12]] (-0.69, fdr 7e-06), [[DCLRE1A]] (-0.66, fdr 1e-05).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3967.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 6.63×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.10×** | +6.7 | 1e-08 | 49/49 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.28×** | +5.6 | 6e-06 | 43/44 (A-172, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.97×** | +4.8 | 3e-04 | 44/48 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.02×** | +4.2 | 0.004 | 42/45 (A-172, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +3.4 | 0.066 | 39/47 (CFPAC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.59×** | +3.3 | 0.094 | 42/48 (NCI-H460, NCI-H1573, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3967.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (SNU-1 0.187×, A-427 0.252×, AN3 CA 0.296×, SW480 0.335×, …).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.525×** | -6.4 | 7e-08 | 43/48 (SNU-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.641× | -3.1 | 0.48 | 35/48 (SNU-1, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3967. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 217 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -12.6) |
| [[AN3 CA (line)]] | alt | 295 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -10.1) |
| [[COLO 205 (line)]] | alt | 139 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.63× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[H4 (line)]] | wt | 263 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -8.6) |
| [[LS 180 (line)]] | wt | 347 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 399 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 383 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 287 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 361 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -9.0) |
| [[SNU-1 (line)]] | wt | 357 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -15.7) |
| [[SW480 (line)]] | alt | 341 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -10.1) |
| [[A-172 (line)]] | wt | 97.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 168 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 210 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 282 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 286 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 86.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 308 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 256 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 281 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 260 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 278 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 329 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 227 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 345 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 256 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 472 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 580 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 426 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 303 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 388 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 320 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 264 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 393 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 339 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 273 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 348 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 399 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3967), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 22 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS21]] | +0.96 | +0.91 / +0.96 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL32]] | +0.95 | +0.91 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL7A]] | +0.95 | +0.92 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPLP2]] | +0.95 | +0.91 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS16]] ⚠ | +0.95 | +0.90 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS10]] | +0.94 | +0.88 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL13]] | +0.94 | +0.91 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL36A]] | +0.94 | +0.91 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 995 |
| [[RPS24]] | +0.94 | +0.93 / +0.94 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL28]] | +0.94 | +0.90 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS5]] | +0.93 | +0.93 / +0.91 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL31]] | +0.93 | +0.89 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.93 | +0.89 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIS12]] | -0.69 | -0.67 / -0.59 | both halves | 7e-06 |  |
| [[DCLRE1A]] | -0.66 | -0.67 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.960). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-46.8, -27.4); signed map (-61.3, -3.6). **Vector** length 95.2, 57.9% of its response variance represented; |z| ≥ 3 in 453 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.93 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +1.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.7 | -0.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.6 | +0.8 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.6 | +1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.5 | -6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -6.1 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -6.0 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -5.8 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | +1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -1.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:119,015,712-119,018,691 (-) |
| Ensembl biotype | protein_coding |
| Also known as | S25, eS25 |
| Gene groups (HGNC) | S ribosomal proteins |
| Reactome | 51 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P62851](https://www.uniprot.org/uniprotkb/P62851) (Small ribosomal subunit protein eS25):

> Component of the small ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6230](https://www.ncbi.nlm.nih.gov/gene/6230):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 40S subunit. The protein belongs to the S25E family of ribosomal proteins. It is located in the cytoplasm. As is typical for genes encoding ribosomal proteins, there are multiple processed pseudogenes of this …

**Accessions** — [HGNC:10413](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10413) · Entrez [6230](https://www.ncbi.nlm.nih.gov/gene/6230) · UniProt [P62851](https://www.uniprot.org/uniprotkb/P62851) · Ensembl [ENSG00000118181](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118181)

## Data

Gene col 3967: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3967); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3967, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3967]; `tensor/DDL_lfc|DDL_z.npy` [3967]; `embed/gene_vectors.npy` [3967]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3967 or target_col == 3967). Every well: [[RPS25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
