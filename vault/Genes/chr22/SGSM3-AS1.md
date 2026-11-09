---
symbol: "SGSM3-AS1"
type: "gene"
col: 13729
ensembl_id: "ENSG00000229999"
name: "SGSM3 antisense RNA 1"
location: "22q13.1"
module: 47
arm: "+"
pooled_cpm: 2.11
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# SGSM3-AS1

*SGSM3 antisense RNA 1* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.76× (z +15.8, q 0e+00, up in 23 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.576× (z -4.6, q 0.002, down in 17 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP50]] (+0.81, fdr 7e-06), [[GARIN1B]] (+0.80, fdr 7e-06), [[CPNE9]] (+0.79, fdr 7e-06).
> It is in [[Module 047]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13729.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.76×** | +15.8 | 0e+00 | 23/32 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +8.7 | 1e-15 | 19/29 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.72×** | +8.1 | 8e-14 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.54×** | +7.9 | 4e-13 | 6/10 (CFPAC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.36×** | +6.7 | 2e-09 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.10×** | +6.3 | 3e-08 | 17/30 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.49×** | +3.4 | 0.052 | 2/22 (HepG2/C3A, HEC-1-A) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.52×** | +3.4 | 0.052 | 0/39 | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +3.3 | 0.052 | 4/43 (NCI-H1573, H4, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.48×** | +3.3 | 0.052 | 4/28 (NCI-H2347, A-427, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +3.3 | 0.053 | 6/45 (KATO III, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.45×** | +3.1 | 0.079 | 3/21 (HOP62, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Rosiglitazone (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.081 | 5/32 (HEC-1-A, CFPAC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.093 | 3/45 (A498, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13729.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.576×** | -4.6 | 0.002 | 17/45 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 5 µM |  | **0.681×** | -4.5 | 0.002 | 13/44 (SW1417, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.656×** | -3.5 | 0.078 | 14/43 (NCI-H23, COLO 205, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.665×** | -3.4 | 0.089 | 11/40 (RPMI-7951, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.680× | -3.2 | 0.14 | 8/45 (NCI-H1573, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.686× | -3.2 | 0.15 | 11/39 (J82, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13729. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 2.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.46× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 1.46 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +9.7) | — |
| [[SW480 (line)]] | alt | 1.65 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.5 µM 0.0782× (z -8.6) |
| [[A-172 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13729), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP50]] | +0.81 | +0.86 / +0.79 | both halves | 7e-06 |  |
| [[GARIN1B]] | +0.80 | +0.80 / +0.80 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.79 | +0.79 / +0.76 | both halves | 7e-06 |  |
| [[OIT3]] | +0.79 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.78 | +0.80 / +0.79 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.78 | +0.80 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[PITRM1-AS1]] | +0.78 | +0.78 / +0.70 | both halves | 7e-06 | same gene group |
| [[TMEM25]] | +0.78 | +0.74 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[L3MBTL2-AS1]] | +0.77 | +0.84 / +0.61 | both halves | 7e-06 | same gene group |
| [[LINC02133]] | +0.77 | +0.73 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[KIF17]] | +0.76 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[PILRA]] | +0.76 | +0.76 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.817). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.3, -14.6); signed map (18.2, 11.3). **Vector** length 53.1, 6.82% of its response variance represented; |z| ≥ 3 in 1,121 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +15.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.3 | +6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +8.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +2.7 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.4 | +1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.3 | +3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.1 | +1.4 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -1.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -3.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.0 | -2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -4.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | SGSM3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 22q13.1 — chr22:40,372,664-40,388,290 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:41088](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41088) · Entrez [107985538](https://www.ncbi.nlm.nih.gov/gene/107985538) · Ensembl [ENSG00000229999](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229999)

## Data

Gene col 13729: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13729); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13729, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13729]; `tensor/DDL_lfc|DDL_z.npy` [13729]; `embed/gene_vectors.npy` [13729]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13729 or target_col == 13729). Every well: [[SGSM3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SGSM3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
