---
symbol: "SRRM2-AS1"
type: "gene"
col: 13022
ensembl_id: "ENSG00000205913"
name: "SRRM2 antisense RNA 1"
location: "16p13.3"
module: 35
arm: "+"
pooled_cpm: 2.4
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# SRRM2-AS1

*SRRM2 antisense RNA 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.01× (z +9.1, q 4e-17, up in 21 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.512× (z -6.2, q 2e-07, down in 23 of 45 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C2orf49-DT]] (+0.76, fdr 1e-05), [[PJVK]] (+0.74, fdr 7e-06), [[PBLD]] (+0.72, fdr 2e-05); moves opposite to [[STX7]] (-0.61, fdr 4e-04), [[NBPF3]] (-0.60, fdr 2e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13022.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +9.1 | 4e-17 | 21/28 (HEC-1-A, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.50×** | +7.8 | 1e-12 | 1/2 (A498) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +6.5 | 2e-08 | 1/2 (PANC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +5.2 | 3e-05 | 4/13 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.60×** | +4.3 | 0.002 | 4/10 (HEC-1-A, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.37×** | +4.1 | 0.003 | 3/44 (LoVo, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +4.1 | 0.004 | 9/40 (HEC-1-A, SW48, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.020 | 5/43 (HCT15, BT-474, …) | rises with dose |  |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.47×** | +3.6 | 0.022 | 5/35 (CFPAC-1, SNU-1, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.025 | 0/45 | top dose only | position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.070 | 7/33 (HEC-1-A, BT-474, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.070 | 7/26 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.071 | 4/43 (AsPC-1, RKO, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13022.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.512×** | -6.2 | 2e-07 | 23/45 (A-172, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.536×** | -5.8 | 2e-06 | 20/42 (PANC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.553×** | -5.5 | 7e-06 | 19/43 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.559×** | -5.4 | 8e-06 | 19/45 (CFPAC-1, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.695×** | -3.4 | 0.078 | 6/19 (PANC-1, BT-474, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.716× | -3.1 | 0.17 | 9/44 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Gefitinib (drug)]] 5 µM |  | 0.720× | -3.1 | 0.17 | 5/46 (RKO, A-427, …) | top dose only |  |
| [[Bexarotene (drug)]] 0.05 µM |  | 0.725× | -3.0 | 0.17 | 5/42 (HCT15, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13022. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.986 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.893 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.944 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.736 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.936 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13022), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2orf49-DT]] | +0.76 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[PJVK]] | +0.74 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[PBLD]] | +0.72 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[MZF1-AS1]] | +0.71 | +0.72 / +0.43 | both halves | 3e-05 | same gene group |
| [[LINC00863]] | +0.71 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[PPP3CB-AS1]] | +0.71 | +0.70 / +0.45 | both halves | 3e-05 | same gene group |
| [[ZCWPW1]] | +0.71 | +0.70 / +0.37 | both halves | 8e-05 |  |
| [[FAM174B]] | +0.70 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[DENND5B-AS1]] | +0.70 | +0.64 / +0.42 | both halves | 4e-05 | same gene group |
| [[FIZ1]] | +0.69 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[PSMG3-AS1]] | +0.69 | +0.72 / +0.50 | both halves | 1e-05 | same gene group |
| [[RNPC3-DT]] | +0.68 | +0.62 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX7]] | -0.61 | -0.62 / -0.26 | both halves | 4e-04 |  |
| [[NBPF3]] | -0.60 | -0.60 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SRRM2-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC00466]] | B | LINC00466 activity raises SRRM2-AS1's level | lines that do not express LINC00466 (15) vs lines expressing it (35) | 1.26× lower at baseline in the lines without LINC00466 | 0.067 | ⚠ within organs, on part of the lines; also absent: FAM124A, NTN1, SSPOP; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SRRM2-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.769). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (8.4, 20.3); signed map (25.7, -5.7). **Vector** length 44.2, 4.96% of its response variance represented; |z| ≥ 3 in 949 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +7.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.1 | +1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +1.7 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.0 | +1.9 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.5 | -5.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.2 | -3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.2 | -5.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | SRRM2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16p13.3 — chr16:2,737,076-2,752,600 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44162](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44162) · Entrez [100128788](https://www.ncbi.nlm.nih.gov/gene/100128788) · Ensembl [ENSG00000205913](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205913)

## Data

Gene col 13022: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13022); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13022, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13022]; `tensor/DDL_lfc|DDL_z.npy` [13022]; `embed/gene_vectors.npy` [13022]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13022 or target_col == 13022). Every well: [[SRRM2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRRM2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
