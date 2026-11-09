---
symbol: "NKAPD1"
type: "gene"
col: 7461
ensembl_id: "ENSG00000150776"
name: "NKAP domain containing 1"
location: "11q23.1"
module: 149
arm: "+"
pooled_cpm: 28.7
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/149"]
generated_by: "tahoemap"
---

# NKAPD1

*NKAP domain containing 1* — 11q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.01× (z +12.3, q 3e-32, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.729× (z -5.5, q 2e-05, down in 40 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.198×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change); [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (SW 1271 0.0711×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD49]] (+0.79, fdr 7e-06), [[ZNF830]] (+0.77, fdr 7e-06), [[TTF1]] (+0.77, fdr 7e-06); moves opposite to [[LSM4]] (-0.65, fdr 9e-05), [[TFRC]] (-0.64, fdr 7e-06).
> It is in [[Module 149]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7461.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.01×** | +12.3 | 3e-32 | 42/47 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +7.7 | 5e-12 | 41/47 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +7.0 | 4e-10 | 43/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +6.5 | 1e-08 | 35/48 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +6.4 | 1e-08 | 34/47 (RPMI-7951, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.8 | 8e-07 | 30/48 (PANC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.89×** | +4.2 | 0.002 | 24/48 (RKO, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.37×** | +4.0 | 0.005 | 25/46 (hTERT-HPNE, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.016 | 19/48 (A498, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.068 | 18/47 (J82, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.29×** | +3.2 | 0.068 | 21/47 (SNU-423, C32, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | 1.29× | +3.0 | 0.11 | 19/48 (A498, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7461.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.198×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change); [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (SW 1271 0.0711×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.729×** | -5.5 | 2e-05 | 40/48 (SW480, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.701×** | -4.5 | 0.002 | 28/48 (C32, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7461. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 36.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.3) | — |
| [[A498 (line)]] | wt | 20.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +12.2) | — |
| [[RPMI-7951 (line)]] | alt | 33.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +11.8) | — |
| [[A-172 (line)]] | wt | 19.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.4) | — |
| [[C-33 A (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[C32 (line)]] | wt | 23.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 27.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 25.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +10.6) | — |
| [[J82 (line)]] | alt | 21.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +8.7) | — |
| [[KATO III (line)]] | alt | 60.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +11.3) | — |
| [[NCI-H2030 (line)]] | alt | 25.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +14.1) | — |
| [[NCI-H23 (line)]] | alt | 27.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 34.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.1) | — |
| [[SW 1271 (line)]] | alt | 63.4 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0711× (z -9.5) |
| [[A-427 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 44.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7461), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD49]] | +0.79 | +0.81 / +0.73 | both halves | 7e-06 |  |
| [[ZNF830]] | +0.77 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[TTF1]] | +0.77 | +0.74 / +0.84 | both halves | 7e-06 |  |
| [[ZNF189]] | +0.76 | +0.80 / +0.63 | both halves | 7e-06 |  |
| [[ZNF407-AS1]] | +0.74 | +0.81 / +0.63 | both halves | 7e-06 |  |
| [[CCDC59]] | +0.73 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.72 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[SLC4A1AP]] | +0.72 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.72 | +0.79 / +0.63 | both halves | 7e-06 |  |
| [[POLR3C]] | +0.71 | +0.78 / +0.53 | both halves | 1e-05 |  |
| [[SNW1]] | +0.70 | +0.76 / +0.54 | both halves | 1e-05 |  |
| [[TRIM4]] | +0.70 | +0.71 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSM4]] | -0.65 | -0.66 / -0.36 | both halves | 9e-05 |  |
| [[TFRC]] | -0.64 | -0.59 / -0.73 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 149]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.785). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-39.5, 5.7); signed map (-0.5, -16.1). **Vector** length 91.5, 22.6% of its response variance represented; |z| ≥ 3 in 656 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.2 | +12.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.4 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +7.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.3 | +3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.9 | +7.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.7 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.3 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +2.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.1 | -5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.4 | -4.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -0.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -1.4 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -0.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | NKAP domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.1 — chr11:112,074,086-112,085,150 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Ahed, FLJ10726; previously C11orf57 |
| Matched by | ensembl_id |

UniProt [Q6ZUT1](https://www.uniprot.org/uniprotkb/Q6ZUT1) carries no function annotation.

**Summary**, from NCBI Gene [55216](https://www.ncbi.nlm.nih.gov/gene/55216):

> Enables identical protein binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25569](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25569) · Entrez [55216](https://www.ncbi.nlm.nih.gov/gene/55216) · UniProt [Q6ZUT1](https://www.uniprot.org/uniprotkb/Q6ZUT1) · Ensembl [ENSG00000150776](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150776)

## Data

Gene col 7461: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7461); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7461, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7461]; `tensor/DDL_lfc|DDL_z.npy` [7461]; `embed/gene_vectors.npy` [7461]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7461 or target_col == 7461). Every well: [[NKAPD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NKAPD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
