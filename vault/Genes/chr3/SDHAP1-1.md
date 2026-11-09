---
symbol: "SDHAP1-1"
type: "gene"
col: 16503
ensembl_id: "ENSG00000290763"
name: ""
location: ""
module: 40
arm: "+"
pooled_cpm: 3.57
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# SDHAP1-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.67× (z +4.7, q 0.001, up in 0 of 8 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.534× (z -6.0, q 1e-06, down in 19 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H2347 0.0639×, CFPAC-1 0.0814×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A498 0.112×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (RPMI-7951 0.0458×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (J82 0.0811×); [[Betamethasone dipropionate (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0736×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDHAP1]] (+0.76, fdr 7e-06, ⚠ same locus), [[NPRL2]] (+0.75, fdr 7e-06), [[ARFGAP1]] (+0.74, fdr 7e-06), [[SDHAP2]] (+0.74, fdr 7e-06); moves opposite to [[TASOR]] (-0.65, fdr 1e-05), [[CPSF2]] (-0.64, fdr 1e-05), [[IL6ST]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[SDHAP1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16503.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +4.7 | 0.001 | 0/8 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.7 | 0.053 | 6/24 (NCI-H1573, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.65× | +3.4 | 0.11 | 10/29 (SW 900, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16503.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H2347 0.0639×, CFPAC-1 0.0814×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A498 0.112×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (RPMI-7951 0.0458×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (J82 0.0811×); [[Betamethasone dipropionate (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0736×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.534×** | -6.0 | 1e-06 | 19/43 (RPMI-7951, A498, …) | two highest doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.612×** | -4.5 | 0.002 | 17/38 (RPMI-7951, A-172, …) | two highest doses | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 0.692× | -3.4 | 0.13 | 13/40 (HCT15, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.681× | -3.1 | 0.29 | 5/41 (A498, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16503. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.91 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.112× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 5.97 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0458× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 4.37 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0814× (z -8.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 4.26 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0736× (z -8.6) |
| [[HS-578T (line)]] | alt | 4.83 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0886× (z -8.6) |
| [[J82 (line)]] | alt | 5.05 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0811× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 4.72 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0639× (z -10.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.773 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16503), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP1]] | +0.76 | +0.64 / +0.79 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[NPRL2]] | +0.75 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[ARFGAP1]] | +0.74 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[SDHAP2]] | +0.74 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.72 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[GDPD3]] | +0.66 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[TULP3]] | +0.66 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[ZFPL1]] | +0.66 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[DPH7]] | +0.65 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[CLEC4A]] | +0.65 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[GPR107]] | +0.65 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[SGSM3]] | +0.64 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[OSBPL7]] | +0.64 | +0.50 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TASOR]] | -0.65 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[CPSF2]] | -0.64 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[IL6ST]] | -0.60 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[HNRNPK]] | -0.59 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[LEPROT]] | -0.59 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[KRT8P12]] | -0.59 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[UTP20]] | -0.59 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[MED1]] | -0.58 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[TRIP12]] | -0.58 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[TFAM]] | -0.58 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[TCF12]] | -0.58 | -0.38 / -0.58 | both halves | 7e-05 |  |
| [[C6orf120]] | -0.58 | -0.45 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SDHAP1]] | C | SDHAP1-1's natural level strengthens SDHAP1's drug response | SDHAP1-1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.75, reverse -0.03; direction clear | 0.003 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.692). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (0.1, -17.9); signed map (-36.8, 2.2). **Vector** length 42.8, 4.92% of its response variance represented; |z| ≥ 3 in 717 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.3 | +1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.3 | +2.5 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +1.2 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.0 | +1.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.0 | +1.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.0 | +1.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +1.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.5 | -4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -0.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.3 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.3 | -0.6 |

## What is on record

> [!warning] No registry record
> SDHAP1-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16503: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16503); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16503, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16503]; `tensor/DDL_lfc|DDL_z.npy` [16503]; `embed/gene_vectors.npy` [16503]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16503 or target_col == 16503). Every well: [[SDHAP1-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDHAP1-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
