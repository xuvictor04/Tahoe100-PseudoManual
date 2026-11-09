---
symbol: "RPL37A"
type: "gene"
col: 12455
ensembl_id: "ENSG00000197756"
name: "ribosomal protein L37a"
location: "2q35"
module: 43
arm: "+"
pooled_cpm: 454.05
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# RPL37A

*ribosomal protein L37a* — 2q35

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.38× (z +7.5, q 3e-11, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (COLO 205 4.99×, SW480 4.16×, LoVo 4.51×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (COLO 205 4.70×; ⚠ toxic; cell-cycle shift, explains ~32% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS17]] (+0.95, fdr 7e-06, ⚠ RPS17 in the vector space only through flagged drug-doses), [[RPL35A]] (+0.95, fdr 7e-06), [[RPS3]] (+0.94, fdr 7e-06, ⚠ RPS3 in the vector space only through flagged drug-doses), [[RPS12]] (+0.94, fdr 7e-06), [[RPL31]] (+0.93, fdr 7e-06); moves opposite to [[PSME3]] (-0.73, fdr 7e-06), [[PNPO]] (-0.71, fdr 7e-06), [[SF3B4]] (-0.69, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12455.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (COLO 205 4.99×, SW480 4.16×, LoVo 4.51×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (COLO 205 4.70×; ⚠ toxic; cell-cycle shift, explains ~32% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.38×** | +7.5 | 3e-11 | 49/49 (COLO 205, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.41×** | +5.4 | 1e-05 | 42/44 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.13×** | +4.9 | 2e-04 | 48/48 (COLO 205, NCI-H460, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.99×** | +4.4 | 0.001 | 46/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.08×** | +4.4 | 0.002 | 42/45 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.86×** | +3.8 | 0.012 | 43/47 (COLO 205, SHP-77, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +3.4 | 0.057 | 43/47 (CFPAC-1, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12455.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Folic acid (drug)]] 5 µM |  | 0.701× | -3.2 | 0.44 | 47/48 (NCI-H1792, NCI-H661, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12455. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 232 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LoVo (line)]] | wt | 722 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW480 (line)]] | alt | 529 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 325 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 449 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 357 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 471 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 397 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 486 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 400 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 462 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 322 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 415 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 516 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 518 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 466 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 370 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 715 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 405 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 305 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 371 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 405 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 479 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 357 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 626 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 522 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 518 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 466 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 343 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 555 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 417 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 553 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 475 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 557 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 546 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 327 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 485 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 430 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 613 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 327 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 406 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 301 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 474 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 516 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 404 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 331 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 431 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 448 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 611 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12455), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 22 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS17]] ⚠ | +0.95 | +0.90 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL35A]] | +0.95 | +0.89 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS3]] ⚠ | +0.94 | +0.90 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS12]] | +0.94 | +0.89 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL9]] ⚠ | +0.94 | +0.87 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS27A]] ⚠ | +0.93 | +0.88 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL31]] | +0.93 | +0.86 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL36]] | +0.93 | +0.90 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS19]] | +0.92 | +0.89 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.92 | +0.82 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL26]] | +0.91 | +0.84 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL23]] | +0.91 | +0.84 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS27]] | +0.91 | +0.85 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS29]] | +0.90 | +0.83 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.90 | +0.81 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPLP1]] | +0.90 | +0.86 / +0.91 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3]] | -0.73 | -0.60 / -0.77 | both halves | 7e-06 |  |
| [[PNPO]] | -0.71 | -0.61 / -0.68 | both halves | 7e-06 |  |
| [[SF3B4]] | -0.69 | -0.57 / -0.71 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.917). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-45.0, -27.0); signed map (-59.5, -3.8). **Vector** length 90.2, 61.4% of its response variance represented; |z| ≥ 3 in 531 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.75 to 19); *Translation initiation complex formation* (reactome, mean cos +0.71 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.71 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +0.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.2 | +0.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.4 | +1.2 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +2.1 | +2.7 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +2.1 | -0.6 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +2.0 | +0.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -5.7 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -5.6 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -5.3 | +5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | +1.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | -3.1 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -0.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.6 | -0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | +2.2 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.2 | -0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L37a |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:216,498,825-216,579,180 (+) |
| Ensembl biotype | protein_coding |
| Also known as | L37A, eL43 |
| Gene groups (HGNC) | L ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P61513](https://www.uniprot.org/uniprotkb/P61513) (Large ribosomal subunit protein eL43):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6168](https://www.ncbi.nlm.nih.gov/gene/6168):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L37AE family of ribosomal proteins. It is located in the cytoplasm. The protein contains a C4-type zinc finger-like domain. As is typical for genes encoding ribosomal …

**Accessions** — [HGNC:10348](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10348) · Entrez [6168](https://www.ncbi.nlm.nih.gov/gene/6168) · UniProt [P61513](https://www.uniprot.org/uniprotkb/P61513) · Ensembl [ENSG00000197756](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197756)

## Data

Gene col 12455: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12455); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12455, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12455]; `tensor/DDL_lfc|DDL_z.npy` [12455]; `embed/gene_vectors.npy` [12455]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12455 or target_col == 12455). Every well: [[RPL37A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL37A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
