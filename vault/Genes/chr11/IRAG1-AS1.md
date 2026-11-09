---
symbol: "IRAG1-AS1"
type: "gene"
col: 10793
ensembl_id: "ENSG00000177112"
name: "IRAG1 antisense RNA 1"
location: "11p15.4"
module: 53
arm: "+"
pooled_cpm: 4.36
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# IRAG1-AS1

*IRAG1 antisense RNA 1* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.07× (z +9.5, q 2e-18, up in 18 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.358× (z -9.5, q 2e-18, down in 28 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SELPLG]] (+0.79, fdr 7e-06), [[KIF17]] (+0.73, fdr 7e-06), [[FNDC7]] (+0.73, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[IMPA1P1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10793.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.07×** | +9.5 | 2e-18 | 18/36 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +7.6 | 7e-12 | 16/35 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +6.6 | 7e-09 | 11/23 (SW480, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.01×** | +6.4 | 2e-08 | 20/40 (A-172, H4, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +6.4 | 2e-08 | 22/43 (SW480, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.00×** | +6.4 | 2e-08 | 17/39 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.77×** | +5.3 | 1e-05 | 19/44 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.74×** | +5.1 | 2e-05 | 18/42 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +5.0 | 4e-05 | 1/11 (NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.3 | 9e-04 | 5/43 (PANC-1, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +4.3 | 0.001 | 11/43 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.49×** | +3.6 | 0.013 | 9/41 (A498, SW480, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10793.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.358×** | -9.5 | 2e-18 | 28/40 (COLO 205, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.363×** | -9.3 | 3e-18 | 31/45 (RPMI-7951, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.448×** | -7.4 | 2e-11 | 24/39 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.501×** | -6.4 | 3e-08 | 23/45 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.574×** | -5.1 | 3e-05 | 17/39 (A549, J82, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.577×** | -5.1 | 4e-05 | 20/32 (SW480, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[NG25 (drug)]] 5 µM |  | **0.386×** | -4.6 | 4e-04 | 11/31 (HS-578T, AsPC-1, …) | top dose only | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.716×** | -4.4 | 9e-04 | 10/45 (Hs 766T, LOX-IMVI, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.634×** | -4.2 | 0.002 | 16/43 (CFPAC-1, PANC-1, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.480×** | -3.5 | 0.023 | 8/27 (NCI-H1792, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.692×** | -3.4 | 0.035 | 17/42 (C-33 A, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cysteamine (hydrochloride) (drug)]] 0.5 µM |  | 0.722× | -3.0 | 0.12 | 5/35 (BT-474, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10793. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 9.57 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0325× (z -12.1) |
| [[LoVo (line)]] | wt | 4.85 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +10.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.112× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 24.4 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0305× (z -11.9) |
| [[SW480 (line)]] | alt | 4.37 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0428× (z -15.4) ⚠ transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.124× (z -10.2) |
| [[A498 (line)]] | wt | 3.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +8.5) | — |
| [[C32 (line)]] | wt | 1.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 170× (z +14.4) | — |
| [[HS-578T (line)]] | alt | 13.3 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM 0.0583× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.1× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 8.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.5× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 2.16 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 6.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +9.0) | — |
| [[A-172 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.885 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10793), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELPLG]] | +0.79 | +0.80 / +0.68 | both halves | 7e-06 |  |
| [[KIF17]] | +0.73 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.73 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[TMEM25]] | +0.73 | +0.76 / +0.59 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.72 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.72 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[ROPN1L]] | +0.71 | +0.78 / +0.55 | both halves | 1e-05 |  |
| [[TRIM72]] | +0.71 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[MIR9-1HG]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[AXDND1]] | +0.71 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.70 | +0.72 / +0.62 | both halves | 7e-06 | same gene group |
| [[TMPRSS9]] | +0.70 | +0.77 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IMPA1P1]] | B | IMPA1P1 activity raises IRAG1-AS1's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 1.81× lower at baseline in the lines without IMPA1P1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.786). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.0, -15.5); signed map (17.6, 12.4). **Vector** length 64.4, 9.51% of its response variance represented; |z| ≥ 3 in 1,204 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.6 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +6.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.1 | +1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.7 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.9 | -9.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.7 | -7.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.5 | -9.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.0 | -5.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | +1.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -4.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -0.9 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | IRAG1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11p15.4 — chr11:10,541,258-10,599,939 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously MRVI1-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:43434](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43434) · Entrez [100129827](https://www.ncbi.nlm.nih.gov/gene/100129827) · Ensembl [ENSG00000177112](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177112)

## Data

Gene col 10793: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10793); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10793, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10793]; `tensor/DDL_lfc|DDL_z.npy` [10793]; `embed/gene_vectors.npy` [10793]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10793 or target_col == 10793). Every well: [[IRAG1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IRAG1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
