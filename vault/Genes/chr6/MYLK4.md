---
symbol: "MYLK4"
type: "gene"
col: 7046
ensembl_id: "ENSG00000145949"
name: "myosin light chain kinase family member 4"
location: "6p25.2"
module: 35
arm: "+"
pooled_cpm: 2.79
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# MYLK4

*myosin light chain kinase family member 4* — 6p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.24× (z +23.6, q 0e+00, up in 35 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.598× (z -4.7, q 0.002, down in 11 of 45 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Brivudine (drug)]] 5 µM: 0.400× (z -4.3, q 0.004, down in 10 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SIAH2-AS1]] (+0.83, fdr 7e-06), [[CPEB2-DT]] (+0.79, fdr 1e-05), [[FAM174B]] (+0.78, fdr 1e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7046.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.24×** | +23.6 | 0e+00 | 35/35 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.44×** | +10.4 | 7e-23 | 7/7 (MIA PaCa-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.13×** | +10.0 | 3e-21 | 2/5 (PANC-1, NCI-H2347) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.16×** | +7.0 | 3e-10 | 6/15 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.11×** | +6.8 | 1e-09 | 22/41 (NCI-H460, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +6.7 | 2e-09 | 16/35 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +6.7 | 2e-09 | 10/27 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.48×** | +5.0 | 3e-05 | 11/43 (PANC-1, NCI-H23, …) | top dose only | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +5.0 | 4e-05 | 4/16 (NCI-H1573, SHP-77, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.9 | 5e-05 | 11/44 (HEC-1-A, NCI-H2347, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.51×** | +3.8 | 0.009 | 3/41 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.015 | 10/44 (NCI-H1792, KATO III, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.044 | 3/46 (SW48, MIA PaCa-2, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.072 | 5/43 (hTERT-HPNE, NCI-H23, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.43×** | +3.1 | 0.072 | 1/42 (Panc 03.27) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7046.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.598×** | -4.7 | 0.002 | 11/45 (NCI-H23, BT-474, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.400×** | -4.3 | 0.004 | 10/40 (NCI-H1792, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.648×** | -3.9 | 0.016 | 12/44 (A-172, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.673×** | -3.6 | 0.042 | 13/45 (BT-474, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.659×** | -3.6 | 0.042 | 10/41 (KATO III, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.488×** | -3.4 | 0.063 | 9/38 (NCI-H23, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7046. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 8.45 | 0 | 2 | — | [[Silodosin (drug)]] 5 µM 0.0579× (z -11.2) |
| [[SW480 (line)]] | alt | 2.85 | 0 | 2 (1 ⚠) | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0917× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 3.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.42× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 2.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.96× (z +10.5) | — |
| [[LoVo (line)]] | wt | 2.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.64× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 3.50 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.5 µM 0.0568× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 2.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.21× (z +11.1) | — |
| [[PANC-1 (line)]] | alt | 2.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.97× (z +10.5) | — |
| [[A-172 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7046), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIAH2-AS1]] | +0.83 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CPEB2-DT]] | +0.79 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[FAM174B]] | +0.78 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[PSMD7-DT]] | +0.78 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[ALG1L9P]] | +0.78 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CIBAR1-DT]] | +0.78 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[PBLD]] | +0.78 | +0.63 / +0.40 | both halves | 5e-05 |  |
| [[PKN2-AS1]] | +0.77 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[MAMDC2-AS1]] | +0.77 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[RNPC3-DT]] | +0.77 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[C2orf88]] | +0.77 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[SAXO1]] | +0.76 | +0.54 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MYLK4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises MYLK4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.776). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (10.7, 19.0); signed map (25.9, -3.3). **Vector** length 57.2, 7.52% of its response variance represented; |z| ≥ 3 in 1,094 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +23.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +10.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +10.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +4.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +3.1 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -3.3 | -3.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -0.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.8 | -3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -1.7 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.2 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | myosin light chain kinase family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.2 — chr6:2,663,629-2,770,330 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SgK085 |
| Gene groups (HGNC) | Myosin light chain kinase family |
| Matched by | ensembl_id |

UniProt [Q86YV6](https://www.uniprot.org/uniprotkb/Q86YV6) carries no function annotation.

**Summary**, from NCBI Gene [340156](https://www.ncbi.nlm.nih.gov/gene/340156):

> Predicted to enable myosin light chain kinase activity. Predicted to be involved in signal transduction. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27972](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27972) · Entrez [340156](https://www.ncbi.nlm.nih.gov/gene/340156) · UniProt [Q86YV6](https://www.uniprot.org/uniprotkb/Q86YV6) · Ensembl [ENSG00000145949](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145949)

## Data

Gene col 7046: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7046); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7046, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7046]; `tensor/DDL_lfc|DDL_z.npy` [7046]; `embed/gene_vectors.npy` [7046]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7046 or target_col == 7046). Every well: [[MYLK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYLK4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
