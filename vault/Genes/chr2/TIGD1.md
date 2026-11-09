---
symbol: "TIGD1"
type: "gene"
col: 13320
ensembl_id: "ENSG00000221944"
name: "tigger transposable element derived 1"
location: "2q37.1"
module: 18
arm: "+"
pooled_cpm: 6.18
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# TIGD1

*tigger transposable element derived 1* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 1.72× (z +5.4, q 5e-05, up in 7 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.45× (z +4.0, q 0.010, up in 14 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[9-ING-41 (drug)]] 0.5 µM: 0.591× (z -4.0, q 0.034, down in 13 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0628×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (KATO III 0.0718×); [[Harringtonine (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0703×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RFT1]] (+0.72, fdr 1e-05), [[SPRYD4]] (+0.68, fdr 7e-06), [[LINC03009]] (+0.66, fdr 8e-06); moves opposite to [[ZSWIM6]] (-0.58, fdr 1e-05), [[FNBP1]] (-0.53, fdr 5e-05), [[TLE4]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13320.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +5.4 | 5e-05 | 7/15 (SW 900, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +5.2 | 5e-05 | 16/34 (CFPAC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.40×** | +5.0 | 8e-05 | 19/47 (A549, HOP62, …) | rises with dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +4.0 | 0.010 | 14/45 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +3.9 | 0.013 | 8/46 (HOP62, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.37×** | +3.3 | 0.087 | 7/44 (NCI-H2347, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.098 | 9/47 (A-172, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.35× | +3.2 | 0.11 | 5/47 (A498, A-427, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13320.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0628×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (KATO III 0.0718×); [[Harringtonine (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0703×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.591×** | -4.0 | 0.034 | 13/41 (HOP62, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.749× | -3.1 | 0.56 | 13/44 (HS-578T, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13320. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 5.61 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0718× (z -10.2) |
| [[LS 180 (line)]] | wt | 5.92 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0867× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 5.24 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0703× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 5.90 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0628× (z -11.0) |
| [[SW 900 (line)]] | alt | 7.17 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[A-172 (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13320), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFT1]] | +0.72 | +0.55 / +0.80 | both halves | 1e-05 |  |
| [[SPRYD4]] | +0.68 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[LINC03009]] | +0.66 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[RRN3P1]] | +0.66 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[CIPC]] | +0.65 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[ZBTB26]] | +0.63 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[ZNF852]] | +0.62 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[CCNY-AS1]] | +0.61 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[PMS2P1]] | +0.61 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[NAXD]] | +0.61 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[ZFP62]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[LY6G5B]] | +0.59 | +0.48 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSWIM6]] | -0.58 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[FNBP1]] | -0.53 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[TLE4]] | -0.52 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[NBPF10]] | -0.51 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[SHOC2]] | -0.51 | -0.34 / -0.54 | both halves | 1e-04 | same gene group |
| [[FAM53C]] | -0.51 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[ING2]] | -0.51 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[FER]] | -0.51 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[HECTD4]] | -0.50 | -0.41 / -0.46 | both halves | 4e-05 | same gene group |
| [[KLF2]] | -0.50 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[CLEC16A]] | -0.50 | -0.45 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.366). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-18.4, -3.8); signed map (-20.1, -34.2). **Vector** length 51.1, 6.37% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +3.9 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +5.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +1.9 | +3.3 |
|  | [[Gallic acid (drug)]] 0.05 µM |  | +1.2 | +1.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.2 | +0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.1 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -0.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.4 | -2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | +0.1 |
|  | [[Darolutamide (drug)]] 0.05 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | tigger transposable element derived 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:232,543,883-232,550,557 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EEYORE |
| Gene groups (HGNC) | Helix-turn-helix CENPB type domain family; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q96MW7](https://www.uniprot.org/uniprotkb/Q96MW7) carries no function annotation.

**Summary**, from NCBI Gene [200765](https://www.ncbi.nlm.nih.gov/gene/200765):

> The protein encoded by this gene belongs to the tigger subfamily of the pogo superfamily of DNA-mediated transposons in humans. These proteins are related to DNA transposons found in fungi and nematodes, and more distantly to the Tc1 and mariner transposases. They are also very similar to the major mammalian centromere protein B. The exact function of this gene is not known. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14523](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14523) · Entrez [200765](https://www.ncbi.nlm.nih.gov/gene/200765) · UniProt [Q96MW7](https://www.uniprot.org/uniprotkb/Q96MW7) · Ensembl [ENSG00000221944](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000221944)

## Data

Gene col 13320: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13320); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13320, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13320]; `tensor/DDL_lfc|DDL_z.npy` [13320]; `embed/gene_vectors.npy` [13320]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13320 or target_col == 13320). Every well: [[TIGD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIGD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
