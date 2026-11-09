---
symbol: "RPS8"
type: "gene"
col: 6666
ensembl_id: "ENSG00000142937"
name: "ribosomal protein S8"
location: "1p34.1"
module: 43
arm: "+"
pooled_cpm: 570.62
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

# RPS8

*ribosomal protein S8* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.83× (z +6.2, q 4e-07, up in 42 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.591× (z -4.5, q 0.004, down in 39 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (C-33 A 0.330×, SW480 0.334×, LS 180 0.353×, SNU-1 0.352×, …).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL9]] (+0.97, fdr 7e-06, ⚠ RPL9 in the vector space only through flagged drug-doses), [[RPL34]] (+0.97, fdr 7e-06), [[RPL35A]] (+0.96, fdr 7e-06), [[RPL26]] (+0.96, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6666.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.83×** | +6.2 | 4e-07 | 42/44 (CHP-212, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **3.31×** | +5.8 | 2e-06 | 49/49 (COLO 205, A549, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +4.1 | 0.007 | 46/47 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.94×** | +3.8 | 0.023 | 38/45 (SNU-423, CHP-212, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.81×** | +3.7 | 0.027 | 44/48 (SW1417, SW 900, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6666.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (C-33 A 0.330×, SW480 0.334×, LS 180 0.353×, SNU-1 0.352×, …).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.591×** | -4.5 | 0.004 | 39/48 (C-33 A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6666. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 644 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -9.4) |
| [[LS 180 (line)]] | wt | 733 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -8.9) |
| [[SHP-77 (line)]] | alt | 351 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -8.5) |
| [[SNU-1 (line)]] | wt | 813 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -8.9) |
| [[SW480 (line)]] | alt | 590 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -9.3) |
| [[A-172 (line)]] | wt | 306 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 604 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 553 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 493 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 657 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 434 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 330 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 315 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 600 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 293 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 276 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 639 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 713 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 629 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 682 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 535 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 600 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 706 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 683 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 536 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 383 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 479 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1,058 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 680 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 831 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 410 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 398 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 679 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 459 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 615 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 646 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 607 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 616 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 573 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 684 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 516 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 772 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 396 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 364 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 587 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 452 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 323 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 338 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 340 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 837 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6666), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 23 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL9]] ⚠ | +0.97 | +0.94 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL34]] | +0.97 | +0.95 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL35A]] | +0.96 | +0.94 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL26]] | +0.96 | +0.94 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS12]] | +0.96 | +0.91 / +0.97 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL31]] | +0.96 | +0.93 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS3]] ⚠ | +0.95 | +0.91 / +0.96 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL23]] | +0.95 | +0.93 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS27]] | +0.95 | +0.92 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS6]] ⚠ | +0.95 | +0.93 / +0.94 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS27A]] ⚠ | +0.95 | +0.90 / +0.96 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL13]] | +0.94 | +0.92 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPLP1]] | +0.94 | +0.91 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL19]] | +0.94 | +0.89 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS14]] | +0.94 | +0.89 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL12]] | +0.93 | +0.91 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.973). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.5, -27.5); signed map (-60.2, -4.2). **Vector** length 86.5, 64.3% of its response variance represented; |z| ≥ 3 in 394 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.88 to 34); *MYC targets v1* (hallmark, mean cos +0.69 to 17); *oxidative phosphorylation* (hallmark, mean cos +0.69 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +0.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.6 | -0.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +1.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.3 | +0.4 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.2 | +0.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.1 | +1.9 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | -7.9 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.5 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -7.4 | +3.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | -3.5 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -0.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.1 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:44,775,251-44,778,779 (+) |
| Ensembl biotype | protein_coding |
| Also known as | S8, eS8 |
| Gene groups (HGNC) | S ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Reactome | 51 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P62241](https://www.uniprot.org/uniprotkb/P62241) (Small ribosomal subunit protein eS8):

> Component of the small ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and …

**Summary**, from NCBI Gene [6202](https://www.ncbi.nlm.nih.gov/gene/6202):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 40S subunit. The protein belongs to the S8E family of ribosomal proteins. It is located in the cytoplasm. Increased expression of this gene in colorectal tumors and colon polyps compared to matched normal colonic …

**Accessions** — [HGNC:10441](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10441) · Entrez [6202](https://www.ncbi.nlm.nih.gov/gene/6202) · UniProt [P62241](https://www.uniprot.org/uniprotkb/P62241) · Ensembl [ENSG00000142937](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142937)

## Data

Gene col 6666: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6666); `tables/drug_effects.parquet` (6 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6666, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6666]; `tensor/DDL_lfc|DDL_z.npy` [6666]; `embed/gene_vectors.npy` [6666]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6666 or target_col == 6666). Every well: [[RPS8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
