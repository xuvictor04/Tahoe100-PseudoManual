---
symbol: "ARL9"
type: "gene"
col: 12222
ensembl_id: "ENSG00000196503"
name: "ARF like GTPase 9"
location: "4q12"
module: 38
arm: "+"
pooled_cpm: 5.14
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# ARL9

*ARF like GTPase 9* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.86× (z +10.9, q 5e-25, up in 30 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.609× (z -3.7, q 0.087, down in 19 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[NG25 (drug)]] 5 µM: 0.392× (z -3.6, q 0.087, down in 8 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Radotinib (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0475×); [[Fluvoxamine (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0605×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (RKO 0.0769×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FNDC7]] (+0.88, fdr 7e-06), [[MYOCOS]] (+0.88, fdr 7e-06), [[IDI2-AS1]] (+0.84, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12222.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.86×** | +10.9 | 5e-25 | 30/41 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.72×** | +10.4 | 6e-23 | 38/40 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.78×** | +9.4 | 9e-19 | 21/25 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.32×** | +8.2 | 4e-14 | 10/13 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.98×** | +8.0 | 1e-13 | 26/39 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.65×** | +7.2 | 7e-11 | 30/45 (SW480, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +5.3 | 8e-06 | 3/6 (NCI-H1792, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.88×** | +4.6 | 3e-04 | 9/23 (NCI-H2347, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +4.2 | 0.002 | 13/45 (NCI-H2347, SNU-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.70×** | +3.9 | 0.006 | 16/46 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.59×** | +3.7 | 0.013 | 8/41 (NCI-H460, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +3.5 | 0.019 | 12/38 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.41×** | +3.4 | 0.030 | 4/11 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.54×** | +3.2 | 0.061 | 14/45 (NCI-H460, HCT15, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.70×** | +3.1 | 0.078 | 8/45 (A498, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tranilast (drug)]] 0.5 µM |  | **1.52×** | +3.1 | 0.078 | 6/45 (CFPAC-1, SW48, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **2.19×** | +3.0 | 0.084 | 1/37 (NCI-H2347) | rises with dose | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12222.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Radotinib (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0475×); [[Fluvoxamine (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0605×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (RKO 0.0769×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.609×** | -3.7 | 0.087 | 19/39 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[NG25 (drug)]] 5 µM |  | **0.392×** | -3.6 | 0.087 | 8/32 (RKO, SNU-423, …) | top dose only | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.630× | -3.4 | 0.12 | 12/45 (RKO, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.564× | -3.3 | 0.13 | 8/42 (NCI-H1573, HS-578T, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Erlotinib (drug)]] 5 µM |  | 0.644× | -3.1 | 0.20 | 12/44 (CFPAC-1, LS 180, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.664× | -3.0 | 0.23 | 16/45 (J82, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12222. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 5.93 | 0 | 2 | — | [[Radotinib (drug)]] 0.5 µM 0.0475× (z -10.7) |
| [[J82 (line)]] | alt | 3.01 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0453× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 9.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +9.3) | — |
| [[RKO (line)]] | wt | 12.8 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0769× (z -9.6) |
| [[A-172 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12222), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FNDC7]] | +0.88 | +0.88 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[MYOCOS]] | +0.88 | +0.89 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[IDI2-AS1]] | +0.84 | +0.83 / +0.78 | both halves | 7e-06 |  |
| [[USP50]] | +0.82 | +0.83 / +0.77 | both halves | 7e-06 |  |
| [[HCLS1]] | +0.82 | +0.83 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[GABRR2]] | +0.82 | +0.78 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[PYGM]] | +0.82 | +0.80 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[RFPL3S]] | +0.82 | +0.86 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[PILRA]] | +0.81 | +0.81 / +0.76 | both halves | 7e-06 |  |
| [[ISY1-RAB43]] | +0.80 | +0.79 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[RRH]] | +0.80 | +0.76 / +0.78 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.80 | +0.84 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.885). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.9, -16.0); signed map (15.8, 9.6). **Vector** length 92.6, 18.8% of its response variance represented; |z| ≥ 3 in 1,120 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +10.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +10.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.0 | +9.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.6 | +3.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.6 | +3.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +2.4 | +1.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.7 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.7 | -3.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -1.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.6 | -3.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.2 | -3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.4 | -2.8 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | -2.3 | -2.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:56,505,209-56,524,959 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | ARF GTPase family |
| Matched by | ensembl_id |

UniProt [Q6T311](https://www.uniprot.org/uniprotkb/Q6T311) carries no function annotation.

**Summary**, from NCBI Gene [132946](https://www.ncbi.nlm.nih.gov/gene/132946):

> ARL9 is a member of the small GTPase protein family with a high degree of similarity to ARF (MIM 103180) proteins of the RAS superfamily.[supplied by OMIM, Nov 2008]

**Accessions** — [HGNC:23592](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23592) · Entrez [132946](https://www.ncbi.nlm.nih.gov/gene/132946) · UniProt [Q6T311](https://www.uniprot.org/uniprotkb/Q6T311) · Ensembl [ENSG00000196503](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196503)

## Data

Gene col 12222: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12222); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12222, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12222]; `tensor/DDL_lfc|DDL_z.npy` [12222]; `embed/gene_vectors.npy` [12222]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12222 or target_col == 12222). Every well: [[ARL9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
