---
symbol: "RPL37"
type: "gene"
col: 7006
ensembl_id: "ENSG00000145592"
name: "ribosomal protein L37"
location: "5p13.1"
module: 43
arm: "+"
pooled_cpm: 355.92
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# RPL37

*ribosomal protein L37* — 5p13.1

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.86× (z +7.9, q 2e-12, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H1573 4.21×, LoVo 3.41×, NCI-H460 3.71×, A549 3.90×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 3.41×, C-33 A 3.22×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.24×).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.465×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS17]] (+0.95, fdr 7e-06, ⚠ RPS17 in the vector space only through flagged drug-doses), [[RPL26]] (+0.94, fdr 7e-06), [[RPL31]] (+0.94, fdr 7e-06), [[RPL19]] (+0.94, fdr 7e-06); moves opposite to [[POGLUT3]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7006.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H1573 4.21×, LoVo 3.41×, NCI-H460 3.71×, A549 3.90×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 3.41×, C-33 A 3.22×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.24×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.86×** | +7.9 | 2e-12 | 49/49 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.33×** | +6.7 | 8e-09 | 43/44 (LoVo, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.86×** | +5.1 | 8e-05 | 47/48 (SW 900, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.05×** | +4.4 | 0.001 | 42/45 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +4.4 | 0.001 | 42/47 (HepG2/C3A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.57×** | +3.7 | 0.019 | 40/48 (NCI-H460, COLO 205, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +3.3 | 0.093 | 0/50 | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.465×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7006. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 648 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.41× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 302 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +8.5) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 324 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.22× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 307 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 463 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 393 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +8.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 374 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -8.8) |
| [[A-172 (line)]] | wt | 178 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 418 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 315 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 391 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 351 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 279 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 157 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 313 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 313 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 310 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 287 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 267 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 366 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 299 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 437 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 293 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 381 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 291 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 368 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 214 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 416 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 342 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 438 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 313 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 413 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 309 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 710 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 398 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 383 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 462 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 316 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 339 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 302 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 332 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 307 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 281 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 364 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 328 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 387 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 417 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7006), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 21 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS17]] ⚠ | +0.95 | +0.88 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL26]] | +0.94 | +0.90 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL31]] | +0.94 | +0.89 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL19]] | +0.94 | +0.87 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.94 | +0.88 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL23]] | +0.93 | +0.91 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL30]] ⚠ | +0.93 | +0.88 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL9]] ⚠ | +0.93 | +0.89 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL35A]] | +0.93 | +0.88 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL11]] | +0.92 | +0.87 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.92 | +0.88 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS3]] ⚠ | +0.92 | +0.88 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL17]] | +0.92 | +0.87 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 997 |
| [[RPL13]] | +0.92 | +0.86 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL24]] | +0.91 | +0.85 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL5]] | +0.91 | +0.86 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGLUT3]] | -0.68 | -0.65 / -0.67 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.960). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-45.2, -28.1); signed map (-60.1, -4.8). **Vector** length 84.3, 52.7% of its response variance represented; |z| ≥ 3 in 457 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.80 to 19); *Translation initiation complex formation* (reactome, mean cos +0.77 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.77 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +1.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +1.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.5 | +2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.5 | +0.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.4 | +0.5 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.3 | +0.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.2 | +0.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.7 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.2 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.9 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -0.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | +0.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.4 | -0.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.2 | +0.1 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.1 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L37 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.1 — chr5:40,825,262-40,835,222 (-) |
| Ensembl biotype | protein_coding |
| Also known as | L37, eL37 |
| Gene groups (HGNC) | L ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P61927](https://www.uniprot.org/uniprotkb/P61927) (Large ribosomal subunit protein eL37):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6167](https://www.ncbi.nlm.nih.gov/gene/6167):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L37E family of ribosomal proteins. It is located in the cytoplasm. The protein contains a C2C2-type zinc finger-like motif. As is typical for genes encoding ribosomal …

**Accessions** — [HGNC:10347](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10347) · Entrez [6167](https://www.ncbi.nlm.nih.gov/gene/6167) · UniProt [P61927](https://www.uniprot.org/uniprotkb/P61927) · Ensembl [ENSG00000145592](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145592)

## Data

Gene col 7006: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7006); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7006, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7006]; `tensor/DDL_lfc|DDL_z.npy` [7006]; `embed/gene_vectors.npy` [7006]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7006 or target_col == 7006). Every well: [[RPL37 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL37.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
