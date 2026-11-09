---
symbol: "RPS27A"
type: "gene"
col: 6825
ensembl_id: "ENSG00000143947"
name: "ribosomal protein S27a"
location: "2p16.1"
module: 43
arm: "+"
pooled_cpm: 329.95
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

# RPS27A

*ribosomal protein S27a* — 2p16.1

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.83× (z +6.3, q 1e-07, up in 43 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 4.28×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS17]] (+0.96, fdr 7e-06, ⚠ RPS17 in the vector space only through flagged drug-doses), [[RPL35A]] (+0.96, fdr 7e-06), [[RPL9]] (+0.96, fdr 7e-06, ⚠ RPL9 in the vector space only through flagged drug-doses), [[RPL31]] (+0.95, fdr 7e-06), [[RPS8]] (+0.95, fdr 7e-06); moves opposite to [[PNPO]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6825.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 4.28×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.83×** | +6.3 | 1e-07 | 43/44 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.28×** | +6.2 | 2e-07 | 48/49 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.22×** | +5.0 | 9e-05 | 48/48 (COLO 205, NCI-H460, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **2.06×** | +4.6 | 7e-04 | 46/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.08×** | +4.3 | 0.002 | 39/45 (C-33 A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +4.2 | 0.003 | 47/47 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | 1.64× | +3.0 | 0.19 | 37/47 (H4, COLO 205, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6825. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 391 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.28× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[A-172 (line)]] | wt | 199 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 451 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 335 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 431 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 313 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 310 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 267 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 155 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 329 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 271 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 321 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 323 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 339 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 457 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 297 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 265 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 237 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 353 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 261 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 289 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 594 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 445 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 384 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 357 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 293 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 446 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 267 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 337 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 366 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 364 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 305 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 380 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 342 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 366 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 247 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 238 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 340 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 298 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 291 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 329 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 412 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 379 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6825), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 23 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS17]] ⚠ | +0.96 | +0.90 / +0.98 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL35A]] | +0.96 | +0.91 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL9]] ⚠ | +0.96 | +0.92 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL31]] | +0.95 | +0.88 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.95 | +0.90 / +0.96 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS3]] ⚠ | +0.94 | +0.89 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS29]] | +0.94 | +0.93 / +0.94 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS13]] ⚠ | +0.94 | +0.91 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL23]] | +0.94 | +0.88 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL36]] | +0.93 | +0.89 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL37A]] ⚠ | +0.93 | +0.88 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPLP2]] | +0.93 | +0.90 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.93 | +0.86 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS12]] | +0.93 | +0.87 / +0.94 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS27]] | +0.92 | +0.87 / +0.94 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS19]] | +0.92 | +0.90 / +0.93 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL26]] | +0.92 | +0.86 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNPO]] | -0.70 | -0.59 / -0.68 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.938). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-45.5, -26.9); signed map (-60.1, -3.6). **Vector** length 79.8, 55.3% of its response variance represented; |z| ≥ 3 in 438 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v1* (hallmark, mean cos +0.63 to 17); *oxidative phosphorylation* (hallmark, mean cos +0.71 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +0.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.6 | +0.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.1 | +0.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +2.0 | +5.0 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +1.9 | +0.5 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +1.8 | -0.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -6.5 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.0 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | -6.0 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | +0.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.9 | +0.3 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.9 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S27a |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.1 — chr2:55,231,903-55,235,853 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UBCEP80, Uba80, S27A, eS31 |
| Gene groups (HGNC) | S ribosomal proteins; Ubiquitins |
| Reactome | 446 pathways, smallest: Maturation of protein E_9683683; Maturation of protein E_9694493; FLT3 signaling by CBL mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [P62979](https://www.uniprot.org/uniprotkb/P62979) (Ubiquitin-ribosomal protein eS31 fusion protein):

> [Ubiquitin]: Exists either covalently attached to another protein, or free (unanchored). When covalently bound, it is conjugated to target proteins via an isopeptide bond either as a monomer (monoubiquitin), a polymer linked via different Lys residues of the ubiquitin (polyubiquitin chains) or a linear polymer linked via the initiator Met of the ubiquitin (linear polyubiquitin chains). Polyubiquitin chains, when attached to a target protein, have different functions depending on the Lys residue …

**Summary**, from NCBI Gene [6233](https://www.ncbi.nlm.nih.gov/gene/6233):

> Ubiquitin, a highly conserved protein that has a major role in targeting cellular proteins for degradation by the 26S proteosome, is synthesized as a precursor protein consisting of either polyubiquitin chains or a single ubiquitin fused to an unrelated protein. This gene encodes a fusion protein consisting of ubiquitin at the N terminus and ribosomal protein S27a at the C terminus. When expressed in yeast, the protein is post-translationally processed, generating free ubiquitin monomer and …

**Accessions** — [HGNC:10417](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10417) · Entrez [6233](https://www.ncbi.nlm.nih.gov/gene/6233) · UniProt [P62979](https://www.uniprot.org/uniprotkb/P62979) · Ensembl [ENSG00000143947](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143947)

## Data

Gene col 6825: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6825); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6825, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6825]; `tensor/DDL_lfc|DDL_z.npy` [6825]; `embed/gene_vectors.npy` [6825]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6825 or target_col == 6825). Every well: [[RPS27A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS27A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
