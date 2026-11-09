---
symbol: "RPL9"
type: "gene"
col: 8751
ensembl_id: "ENSG00000163682"
name: "ribosomal protein L9"
location: "4p14"
module: 43
arm: "+"
pooled_cpm: 281.34
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

# RPL9

*ribosomal protein L9* — 4p14

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.51× (z +6.7, q 1e-08, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 6.49×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL35A]] (+0.97, fdr 7e-06), [[RPS3]] (+0.97, fdr 7e-06, ⚠ RPS3 in the vector space only through flagged drug-doses), [[RPL23]] (+0.97, fdr 7e-06), [[RPS8]] (+0.97, fdr 7e-06); moves opposite to [[PNPO]] (-0.72, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8751.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 6.49×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.51×** | +6.7 | 1e-08 | 48/49 (COLO 205, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.62×** | +5.5 | 9e-06 | 42/44 (A549, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **2.10×** | +4.4 | 0.002 | 45/48 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.97×** | +4.0 | 0.007 | 46/48 (COLO 205, NCI-H1573, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.03×** | +3.9 | 0.009 | 38/45 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +3.9 | 0.009 | 44/47 (HepG2/C3A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8751.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.646× | -3.7 | 0.15 | 34/48 (C-33 A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8751. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 154 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.49× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-172 (line)]] | wt | 155 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 294 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 269 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 254 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 205 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 277 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 151 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 334 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 212 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 321 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 332 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 345 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 320 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 193 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 201 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 376 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 286 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 277 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 482 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 289 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 424 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 273 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 262 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 433 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 354 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 305 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 270 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 461 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 368 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 324 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 259 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 336 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 444 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 312 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8751), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 23 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL35A]] | +0.97 | +0.95 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS3]] ⚠ | +0.97 | +0.96 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL23]] | +0.97 | +0.96 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS17]] ⚠ | +0.97 | +0.92 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS8]] | +0.97 | +0.94 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL26]] | +0.97 | +0.95 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL31]] | +0.96 | +0.93 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.96 | +0.92 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS27A]] ⚠ | +0.96 | +0.92 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS6]] ⚠ | +0.95 | +0.93 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL13]] | +0.95 | +0.90 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS12]] | +0.95 | +0.90 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL36]] | +0.94 | +0.91 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS14]] | +0.94 | +0.88 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL17]] | +0.94 | +0.89 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS27]] | +0.93 | +0.90 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNPO]] | -0.72 | -0.62 / -0.71 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.966). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-45.4, -27.3); signed map (-60.0, -4.0). **Vector** length 88.0, 60.3% of its response variance represented; |z| ≥ 3 in 461 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.80 to 19); *Translation initiation complex formation* (reactome, mean cos +0.76 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.76 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +0.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.7 | -0.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.4 | +0.3 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.3 | +0.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +2.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -7.9 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -7.7 | +3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -7.6 | +5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.9 | -3.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | -3.4 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | +2.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.3 | +0.1 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.2 | -0.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.0 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p14 — chr4:39,452,587-39,458,931 (-) |
| Ensembl biotype | protein_coding |
| Also known as | L9, uL6 |
| Gene groups (HGNC) | L ribosomal proteins |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P32969](https://www.uniprot.org/uniprotkb/P32969) (Large ribosomal subunit protein uL6):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6133](https://www.ncbi.nlm.nih.gov/gene/6133):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L6P family of ribosomal proteins. It is located in the cytoplasm. As is typical for genes encoding ribosomal proteins, there are multiple processed pseudogenes of this gene …

**Accessions** — [HGNC:10369](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10369) · Entrez [6133](https://www.ncbi.nlm.nih.gov/gene/6133) · UniProt [P32969](https://www.uniprot.org/uniprotkb/P32969) · Ensembl [ENSG00000163682](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163682)

## Data

Gene col 8751: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8751); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8751, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8751]; `tensor/DDL_lfc|DDL_z.npy` [8751]; `embed/gene_vectors.npy` [8751]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8751 or target_col == 8751). Every well: [[RPL9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
