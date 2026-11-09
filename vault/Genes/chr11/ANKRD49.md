---
symbol: "ANKRD49"
type: "gene"
col: 9713
ensembl_id: "ENSG00000168876"
name: "ankyrin repeat domain 49"
location: "11q21"
module: 149
arm: "+"
pooled_cpm: 13.03
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/149"]
generated_by: "tahoemap"
---

# ANKRD49

*ankyrin repeat domain 49* — 11q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.92× (z +6.5, q 5e-08, up in 28 of 40 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.79× (z +6.0, q 4e-07, up in 27 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.593× (z -5.4, q 3e-05, down in 28 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Finasteride (drug)]] 5 µM in 1 line (H4 0.0486×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NKAPD1]] (+0.79, fdr 7e-06), [[CCDC174]] (+0.78, fdr 7e-06), [[SNW1]] (+0.75, fdr 7e-06); moves opposite to [[PRPS2]] (-0.68, fdr 7e-06), [[TFRC]] (-0.66, fdr 7e-06), [[FKBP1A]] (-0.66, fdr 7e-06).
> It is in [[Module 149]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[N4BP2L2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9713.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +6.5 | 5e-08 | 28/40 (HT-29, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +6.0 | 4e-07 | 27/44 (LS 180, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +5.5 | 9e-06 | 20/35 (HEC-1-A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +5.3 | 2e-05 | 19/29 (NCI-H1573, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +4.9 | 1e-04 | 25/46 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +4.8 | 2e-04 | 12/22 (HEC-1-A, SW1417, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.37×** | +4.6 | 3e-04 | 24/47 (NCI-H1573, NCI-H2030, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.5 | 4e-04 | 24/46 (PANC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.002 | 23/48 (A498, HT-29, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.47×** | +3.9 | 0.005 | 20/47 (LS 180, A549, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +3.6 | 0.014 | 16/46 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.40×** | +3.5 | 0.024 | 21/47 (HS-578T, HOP62, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.85×** | +3.3 | 0.038 | 14/47 (NCI-H1573, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.070 | 11/47 (HT-29, LoVo, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.074 | 17/47 (LOX-IMVI, SW480, …) | top dose only | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9713.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Finasteride (drug)]] 5 µM in 1 line (H4 0.0486×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.593×** | -5.4 | 3e-05 | 28/47 (SW480, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.721× | -3.4 | 0.19 | 15/47 (SW480, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9713. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 9.99 | 0 | 1 | — | [[Finasteride (drug)]] 5 µM 0.0486× (z -9.6) |
| [[HT-29 (line)]] | alt | 21.3 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.97× (z +8.7) ⚠ toxic | — |
| [[PANC-1 (line)]] | alt | 20.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +9.0) | — |
| [[A-172 (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.59 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 26.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9713), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NKAPD1]] | +0.79 | +0.81 / +0.73 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.78 | +0.79 / +0.73 | both halves | 7e-06 | STRING 461 |
| [[SNW1]] | +0.75 | +0.79 / +0.62 | both halves | 7e-06 |  |
| [[PPIG]] | +0.74 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[ZNF830]] | +0.72 | +0.78 / +0.61 | both halves | 7e-06 | STRING 446 |
| [[SLC4A1AP]] | +0.71 | +0.76 / +0.58 | both halves | 7e-06 |  |
| [[MAU2]] | +0.70 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[TTF1]] | +0.70 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.70 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[ALKBH1]] | +0.70 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[BRAP]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[TRIM4]] | +0.69 | +0.73 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPS2]] | -0.68 | -0.64 / -0.64 | both halves | 7e-06 |  |
| [[TFRC]] | -0.66 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[FKBP1A]] | -0.66 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[TXNDC5]] | -0.66 | -0.70 / -0.68 | both halves | 7e-06 |  |
| [[AHCY]] | -0.65 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[SIGMAR1]] | -0.64 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[MDH2]] | -0.63 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[PPAT]] | -0.62 | -0.59 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[N4BP2L2]] | C | ANKRD49's natural level strengthens N4BP2L2's drug response | ANKRD49's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.65, reverse -0.21; direction not clear | 0.042 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 149]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.801). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.5, 3.0); signed map (0.3, -16.2). **Vector** length 68.8, 13.5% of its response variance represented; |z| ≥ 3 in 590 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.2 | +6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +3.1 | +4.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.1 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +1.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.6 | +1.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -2.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -2.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.9 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.7 | +5.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.4 | +0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -0.2 |
|  | [[Lopinavir (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -0.4 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -1.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 49 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q21 — chr11:94,493,979-94,499,578 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20189, FGIF, GBIF |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVL7](https://www.uniprot.org/uniprotkb/Q8WVL7) (Ankyrin repeat domain-containing protein 49):

> Induces HBG1 expression. May have a role in spermatogenesis where it promotes autophagy in response to serum starvation, via the NF-kappaB pathway (By similarity).

**Summary**, from NCBI Gene [54851](https://www.ncbi.nlm.nih.gov/gene/54851):

> Involved in positive regulation of DNA-templated transcription. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25970](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25970) · Entrez [54851](https://www.ncbi.nlm.nih.gov/gene/54851) · UniProt [Q8WVL7](https://www.uniprot.org/uniprotkb/Q8WVL7) · Ensembl [ENSG00000168876](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168876)

## Data

Gene col 9713: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9713); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9713, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9713]; `tensor/DDL_lfc|DDL_z.npy` [9713]; `embed/gene_vectors.npy` [9713]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9713 or target_col == 9713). Every well: [[ANKRD49 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD49.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
