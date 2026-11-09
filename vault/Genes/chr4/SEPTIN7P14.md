---
symbol: "SEPTIN7P14"
type: "gene"
col: 14451
ensembl_id: "ENSG00000245958"
name: "septin 7 pseudogene 14"
location: "4q26"
module: 42
arm: "+"
pooled_cpm: 2.45
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# SEPTIN7P14

*septin 7 pseudogene 14* — 4q26

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 1.69× (z +3.8, q 0.047, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.60× (z +3.7, q 0.047, up in 5 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.829× (z -5.0, q 3e-04, down in 24 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.540× (z -4.8, q 6e-04, down in 13 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 0.0429×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.0691×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.0953×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 5 µM in 1 line (A498 0.0969×); [[Larotrectinib (drug)]] 0.05 µM in 1 line (NCI-H460 0.0586×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSTO2P]] (+0.74, fdr 7e-06), [[NOMO2]] (+0.69, fdr 7e-06), [[TM9SF2]] (+0.67, fdr 7e-06); moves opposite to [[JMJD1C]] (-0.62, fdr 4e-05), [[EIF4EBP3]] (-0.62, fdr 5e-05), [[FDX2]] (-0.61, fdr 3e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14451.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +3.8 | 0.047 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +3.7 | 0.047 | 0/2 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +3.7 | 0.047 | 5/46 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 1.54× | +3.4 | 0.11 | 8/28 (J82, LoVo, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | 1.48× | +3.1 | 0.25 | 2/45 (CFPAC-1, LOX-IMVI) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14451.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 0.0429×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.0691×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.0953×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 5 µM in 1 line (A498 0.0969×); [[Larotrectinib (drug)]] 0.05 µM in 1 line (NCI-H460 0.0586×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.829×** | -5.0 | 3e-04 | 24/47 (SW48, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.540×** | -4.8 | 6e-04 | 13/45 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.559×** | -4.3 | 0.003 | 18/42 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.601×** | -3.8 | 0.022 | 5/21 (NCI-H2347, NCI-H460, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[5-Fluorouracil (drug)]] 0.5 µM |  | 0.657× | -3.2 | 0.14 | 12/42 (SW1417, SHP-77, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.5 µM |  | 0.669× | -3.1 | 0.19 | 12/39 (Panc 03.27, RKO, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.664× | -3.0 | 0.19 | 1/38 (PANC-1) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14451. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 5.50 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0429× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0969× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 3.65 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0691× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 1.84 | 0 | 1 | — | [[Larotrectinib (drug)]] 0.05 µM 0.0586× (z -9.0) |
| [[A-172 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.931 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.994 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.918 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14451), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSTO2P]] | +0.74 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[NOMO2]] | +0.69 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[TM9SF2]] | +0.67 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[SEPTIN7P13]] | +0.67 | +0.54 / +0.75 | both halves | 1e-05 |  |
| [[NUDT21]] | +0.65 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[SEC61A1]] | +0.65 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[STT3A]] | +0.65 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[GGCX]] | +0.61 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[STRAP]] | +0.61 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[SDHAP4]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[IER3IP1]] | +0.60 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[ORMDL3]] | +0.60 | +0.63 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JMJD1C]] | -0.62 | -0.43 / -0.58 | both halves | 4e-05 |  |
| [[EIF4EBP3]] | -0.62 | -0.39 / -0.63 | both halves | 5e-05 |  |
| [[FDX2]] | -0.61 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[LINC02307]] | -0.60 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[PPP1R12A]] | -0.60 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[EID2]] | -0.60 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[HDAC9]] | -0.60 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[RPP25L]] | -0.60 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[ZNF341-AS1]] | -0.59 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[MED13]] | -0.59 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[METTL18]] | -0.59 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[MARCHF7]] | -0.59 | -0.29 / -0.55 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.674). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.3, -28.4); signed map (-54.7, 2.4). **Vector** length 36.3, 3.35% of its response variance represented; |z| ≥ 3 in 991 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Unfolded Protein Response (UPR)* (reactome, mean cos +0.51 to 9); *IRE1alpha activates chaperones* (reactome, mean cos +0.53 to 7); *unfolded protein response* (hallmark, mean cos +0.51 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +0.8 | +3.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +0.7 | +1.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +0.6 | +3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.6 | +2.3 |
|  | [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift | +0.6 | +0.9 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | +0.5 | +2.2 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +0.5 | +0.5 |
|  | [[Budesonide (drug)]] 5 µM |  | +0.5 | +2.4 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +0.5 | +1.6 |
|  | [[Asciminib (drug)]] 0.05 µM |  | +0.5 | +1.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.2 | -4.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.2 | -0.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | septin 7 pseudogene 14 |
| Locus type | pseudogene |
| Location | 4q26 — chr4:119,457,968-119,461,864 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44219](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44219) · Entrez [645513](https://www.ncbi.nlm.nih.gov/gene/645513) · Ensembl [ENSG00000245958](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245958)

## Data

Gene col 14451: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14451); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14451, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14451]; `tensor/DDL_lfc|DDL_z.npy` [14451]; `embed/gene_vectors.npy` [14451]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14451 or target_col == 14451). Every well: [[SEPTIN7P14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEPTIN7P14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
