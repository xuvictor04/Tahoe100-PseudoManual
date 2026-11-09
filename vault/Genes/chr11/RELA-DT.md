---
symbol: "RELA-DT"
type: "gene"
col: 16114
ensembl_id: "ENSG00000285533"
name: "RELA divergent transcript"
location: "11q13.1"
module: 35
arm: "+"
pooled_cpm: 2.11
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# RELA-DT

*RELA divergent transcript* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.89× (z +16.4, q 0e+00, up in 27 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.459× (z -6.7, q 1e-08, down in 17 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HEATR4]] (+0.74, fdr 7e-06), [[SPATC1]] (+0.72, fdr 7e-06), [[C11orf71]] (+0.72, fdr 7e-06).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[EFNA2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16114.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.89×** | +16.4 | 0e+00 | 27/27 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.49×** | +11.1 | 4e-26 | 18/32 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.83×** | +11.0 | 4e-26 | 1/1 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.08×** | +9.6 | 1e-19 | 8/9 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.78×** | +7.9 | 3e-13 | 1/1 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +5.9 | 4e-07 | 3/9 (A549, BT-474, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +5.8 | 6e-07 | 12/24 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.74×** | +4.7 | 2e-04 | 2/9 (NCI-H1573, A-427) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.35×** | +3.8 | 0.008 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +3.8 | 0.008 | 11/32 (HEC-1-A, LS 180, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.033 | 3/43 (PANC-1, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trifluridine (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.067 | 3/40 (BT-474, HT-29, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.45×** | +3.1 | 0.071 | 5/40 (CFPAC-1, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.68×** | +3.1 | 0.073 | 3/21 (HOP62, A-427, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16114.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.459×** | -6.7 | 1e-08 | 17/38 (NCI-H1573, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.500×** | -6.0 | 7e-07 | 17/33 (BT-474, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.568×** | -4.8 | 3e-04 | 17/44 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.613×** | -4.2 | 0.003 | 15/47 (LOX-IMVI, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16114. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.83 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.891 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.850 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.875 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.873 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.908 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16114), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEATR4]] | +0.74 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[SPATC1]] | +0.72 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[C11orf71]] | +0.72 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[TP53TG5]] | +0.71 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[SEC1P]] | +0.71 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[PRRT3]] | +0.69 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[LINC00863]] | +0.69 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[CTDSPL2-DT]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 | same gene group |
| [[CATSPERD]] | +0.69 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[NEK8]] | +0.69 | +0.77 / +0.57 | both halves | 9e-06 |  |
| [[DDX19A-DT]] | +0.68 | +0.72 / +0.59 | both halves | 7e-06 | same gene group |
| [[PSMG3-AS1]] | +0.68 | +0.74 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFNA2]] | B | EFNA2 activity raises RELA-DT's level | lines that do not express EFNA2 (8) vs lines expressing it (42) | 1.33× lower at baseline in the lines without EFNA2 | 0.090 | ⚠ within organs, on part of the lines; also absent: TFR2, USP43, BTG3-AS1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers RELA-DT's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CHKB-DT]] | C | CHKB-DT's natural level strengthens RELA-DT's drug response | CHKB-DT's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.65, reverse -0.09; direction not clear | 0.077 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.723). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (14.9, 23.7); signed map (30.2, 2.5). **Vector** length 44.1, 5.53% of its response variance represented; |z| ≥ 3 in 898 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +16.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.2 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.1 | +2.7 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.0 | +1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.0 | +1.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -6.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | -4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.9 | -6.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.4 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -4.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -0.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.1 | +0.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | RELA divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q13.1 — chr11:65,662,988-65,671,718 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54185](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54185) · Entrez [105369347](https://www.ncbi.nlm.nih.gov/gene/105369347) · Ensembl [ENSG00000285533](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000285533)

## Data

Gene col 16114: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16114); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16114, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16114]; `tensor/DDL_lfc|DDL_z.npy` [16114]; `embed/gene_vectors.npy` [16114]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16114 or target_col == 16114). Every well: [[RELA-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RELA-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
