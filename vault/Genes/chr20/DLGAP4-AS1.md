---
symbol: "DLGAP4-AS1"
type: "gene"
col: 13874
ensembl_id: "ENSG00000232907"
name: "DLGAP4 antisense RNA 1"
location: "20q11.23"
module: 35
arm: "+"
pooled_cpm: 8.6
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# DLGAP4-AS1

*DLGAP4 antisense RNA 1* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.81× (z +10.8, q 2e-24, up in 29 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.900× (z -4.6, q 0.003, down in 13 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.712× (z -4.4, q 0.003, down in 15 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZCWPW1]] (+0.72, fdr 1e-05), [[DDX19A-DT]] (+0.71, fdr 1e-05), [[PPP1R12A-AS2]] (+0.71, fdr 1e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13874.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +10.8 | 2e-24 | 29/44 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.04×** | +9.2 | 7e-18 | 23/35 (HT-29, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +7.2 | 9e-11 | 8/15 (HS-578T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.60×** | +6.1 | 2e-07 | 19/47 (RPMI-7951, NCI-H2030, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +6.0 | 3e-07 | 18/45 (Hs 766T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +4.9 | 1e-04 | 10/23 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.002 | 13/48 (A-427, SHP-77, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.013 | 14/42 (BT-474, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.078 | 2/45 (J82, A549) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.078 | 6/45 (HCT15, HT-29, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.078 | 11/43 (LOX-IMVI, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13874.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.900× | -4.6 | 0.003 | 13/48 (LS 180, HCT15, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.712×** | -4.4 | 0.003 | 15/47 (PANC-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.732×** | -4.0 | 0.011 | 15/47 (NCI-H23, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.754×** | -3.6 | 0.037 | 10/47 (PANC-1, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13874. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 4.34 | 0 | 2 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0986× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 47.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -10.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 7.94 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.105× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 31.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0759× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~19% of this change |
| [[LS 180 (line)]] | wt | 3.84 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM 0.0657× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 7.00 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.180× (z -8.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[RKO (line)]] | wt | 5.37 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.0851× (z -8.5) |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0968× (z -9.7) |
| [[A-427 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13874), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCWPW1]] | +0.72 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[DDX19A-DT]] | +0.71 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.71 | +0.71 / +0.51 | both halves | 1e-05 | same gene group |
| [[EYS]] | +0.70 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[NUTM2E]] | +0.70 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[SYNM-AS1]] | +0.70 | +0.70 / +0.66 | both halves | 7e-06 | same gene group |
| [[LINC02951]] | +0.70 | +0.68 / +0.41 | both halves | 4e-05 |  |
| [[HEATR4]] | +0.70 | +0.75 / +0.49 | both halves | 1e-05 |  |
| [[PPP1R9A-AS1]] | +0.70 | +0.60 / +0.59 | both halves | 7e-06 | same gene group |
| [[RNF32]] | +0.70 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[MAP3K20-AS1]] | +0.69 | +0.62 / +0.63 | both halves | 7e-06 | same gene group |
| [[ZC2HC1C]] | +0.69 | +0.70 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DLGAP4-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.752). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (14.6, 23.4); signed map (30.8, -2.9). **Vector** length 50.9, 5.89% of its response variance represented; |z| ≥ 3 in 902 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +0.9 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +1.1 | +1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | +0.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -0.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.3 | -3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -0.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -2.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.0 | +0.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | DLGAP4 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20q11.23 — chr20:36,507,702-36,573,391 (-) |
| Ensembl biotype | lncRNA |
| Also known as | CCAT7 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51223](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51223) · Entrez [101926987](https://www.ncbi.nlm.nih.gov/gene/101926987) · Ensembl [ENSG00000232907](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232907)

## Data

Gene col 13874: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13874); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13874, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13874]; `tensor/DDL_lfc|DDL_z.npy` [13874]; `embed/gene_vectors.npy` [13874]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13874 or target_col == 13874). Every well: [[DLGAP4-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLGAP4-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
