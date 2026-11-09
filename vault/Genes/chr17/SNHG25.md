---
symbol: "SNHG25"
type: "gene"
col: 15489
ensembl_id: "ENSG00000266402"
name: "small nucleolar RNA host gene 25"
location: "17q23.3"
module: 131
arm: "+"
pooled_cpm: 31.13
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# SNHG25

*small nucleolar RNA host gene 25* — 17q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 7.22× (z +8.4, q 3e-14, up in 44 of 44 measured lines) ⚠ toxic. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 3.91× (z +3.8, q 0.012, up in 43 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 4 lines (SW480 11.5×, LS 180 9.99×, MIA PaCa-2 9.48×, KATO III 9.04×; ⚠ toxic).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.480× (z -4.6, q 0.003, down in 38 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (CHP-212 0.114×, NCI-H2030 0.187×); [[Relugolix (drug)]] 5 µM in 1 line (NCI-H2122 0.550×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS29]] (+0.89, fdr 7e-06), [[RPL36A]] (+0.88, fdr 7e-06), [[RPL38]] (+0.87, fdr 7e-06); moves opposite to [[PDAP1]] (-0.74, fdr 7e-06), [[EIF4G1]] (-0.71, fdr 7e-06), [[PSMC3]] (-0.68, fdr 7e-06).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TRPC4AP]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15489.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 4 lines (SW480 11.5×, LS 180 9.99×, MIA PaCa-2 9.48×, KATO III 9.04×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **7.22×** | +8.4 | 3e-14 | 44/44 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.26×** | +6.4 | 4e-08 | 39/41 (HCT15, LoVo, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.84×** | +4.6 | 8e-04 | 37/45 (SW48, SW480, …) | top dose only | cell-cycle shift (explains ~24% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.75×** | +4.3 | 0.002 | 28/35 (LoVo, PANC-1, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.43×** | +3.9 | 0.010 | 36/45 (Panc 03.27, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.58×** | +3.9 | 0.010 | 30/37 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **3.91×** | +3.8 | 0.012 | 43/45 (SW480, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +3.4 | 0.046 | 30/47 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 2.03× | +3.1 | 0.11 | 38/46 (NCI-H23, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15489.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (CHP-212 0.114×, NCI-H2030 0.187×); [[Relugolix (drug)]] 5 µM in 1 line (NCI-H2122 0.550×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.480×** | -4.6 | 0.003 | 38/46 (CHP-212, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Demeclocycline (drug)]] 5 µM |  | 0.615× | -3.0 | 0.54 | 30/47 (PANC-1, SNU-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15489. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 65.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -10.2) |
| [[KATO III (line)]] | alt | 69.0 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 9.04× (z +8.7) ⚠ toxic | — |
| [[LS 180 (line)]] | wt | 48.2 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 9.99× (z +8.8) ⚠ toxic | — |
| [[MIA PaCa-2 (line)]] | alt | 34.0 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 9.48× (z +8.7) ⚠ toxic | — |
| [[NCI-H2030 (line)]] | alt | 88.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -8.9) |
| [[NCI-H2122 (line)]] | alt | 29.5 | 0 | 1 | — | [[Relugolix (drug)]] 5 µM 0.550× (z -8.7) |
| [[SW480 (line)]] | alt | 28.2 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 11.5× (z +9.4) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.38 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 80.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15489), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 21 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS29]] | +0.89 | +0.86 / +0.87 | both halves | 7e-06 |  |
| [[RPL36A]] | +0.88 | +0.82 / +0.88 | both halves | 7e-06 |  |
| [[RPL38]] | +0.87 | +0.84 / +0.84 | both halves | 7e-06 |  |
| [[RPLP2]] | +0.87 | +0.84 / +0.86 | both halves | 7e-06 |  |
| [[RPS21]] | +0.86 | +0.84 / +0.86 | both halves | 7e-06 |  |
| [[RPS10]] | +0.85 | +0.82 / +0.86 | both halves | 7e-06 |  |
| [[RPS11]] | +0.85 | +0.84 / +0.80 | both halves | 7e-06 |  |
| [[RPS13]] ⚠ | +0.84 | +0.79 / +0.85 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG19]] | +0.84 | +0.76 / +0.88 | both halves | 7e-06 | same gene group |
| [[RPS15]] ⚠ | +0.83 | +0.78 / +0.83 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS23]] | +0.83 | +0.81 / +0.80 | both halves | 7e-06 |  |
| [[RPL36]] | +0.83 | +0.74 / +0.86 | both halves | 7e-06 |  |
| [[DCTN6-DT]] | +0.82 | +0.73 / +0.86 | both halves | 7e-06 |  |
| [[RPS25]] | +0.82 | +0.76 / +0.84 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDAP1]] | -0.74 | -0.64 / -0.75 | both halves | 7e-06 |  |
| [[EIF4G1]] | -0.71 | -0.67 / -0.70 | both halves | 7e-06 |  |
| [[PSMC3]] | -0.68 | -0.63 / -0.69 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRPC4AP]] | C | TRPC4AP's natural level weakens SNHG25's drug response | TRPC4AP's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.67, reverse +0.01; direction clear | 0.040 | ⚠ tissue can mimic it; precision caveat |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.903). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-42.0, -23.1); signed map (-61.4, -2.4). **Vector** length 90.0, 36.3% of its response variance represented; |z| ≥ 3 in 468 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Termination* (reactome, mean cos +0.82 to 20); *Peptide chain elongation* (reactome, mean cos +0.82 to 19); *PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA* (reactome, mean cos +0.82 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.9 | +3.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +4.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.6 | +0.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.4 | +1.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +3.1 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -4.4 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -2.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.0 | +6.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -1.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.4 | -0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.4 | -1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | small nucleolar RNA host gene 25 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q23.3 — chr17:64,145,937-64,146,476 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [105376843](https://www.ncbi.nlm.nih.gov/gene/105376843):

> Predicted to be involved in RNA processing. Predicted to be located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:51534](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51534) · Entrez [105376843](https://www.ncbi.nlm.nih.gov/gene/105376843) · Ensembl [ENSG00000266402](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000266402)

## Data

Gene col 15489: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15489); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15489, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15489]; `tensor/DDL_lfc|DDL_z.npy` [15489]; `embed/gene_vectors.npy` [15489]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15489 or target_col == 15489). Every well: [[SNHG25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNHG25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
