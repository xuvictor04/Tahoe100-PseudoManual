---
symbol: "HNRNPK-AS1"
type: "gene"
col: 14010
ensembl_id: "ENSG00000235298"
name: "HNRNPK antisense RNA 1"
location: "9q21.32"
module: 21
arm: "+"
pooled_cpm: 3.22
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# HNRNPK-AS1

*HNRNPK antisense RNA 1* — 9q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.76× (z +10.4, q 2e-22, up in 22 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.70× (z +7.0, q 3e-10, up in 21 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.588× (z -5.5, q 3e-05, down in 12 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GEMIN7-AS1]] (+0.74, fdr 7e-06), [[NAPA-AS1]] (+0.68, fdr 1e-05), [[ATP1A1-AS1]] (+0.66, fdr 3e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14010.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.76×** | +10.4 | 2e-22 | 22/34 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.67×** | +10.1 | 2e-21 | 16/20 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.33×** | +8.4 | 1e-14 | 3/5 (HOP62, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.28×** | +7.8 | 8e-13 | 4/6 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.70×** | +7.0 | 3e-10 | 21/39 (SW480, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.89×** | +6.5 | 8e-09 | 15/46 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +6.1 | 7e-08 | 10/27 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.41×** | +4.9 | 6e-05 | 11/35 (A498, A-172, …) | rises with dose | composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.48×** | +4.9 | 7e-05 | 10/36 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.58×** | +4.7 | 2e-04 | 12/44 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.87×** | +4.6 | 3e-04 | 11/35 (NCI-H460, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.73×** | +4.0 | 0.003 | 2/6 (HEC-1-A, PANC-1) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +3.9 | 0.004 | 8/45 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[9-ING-41 (drug)]] 0.05 µM |  | **1.47×** | +3.7 | 0.008 | 6/44 (PANC-1, J82, …) | inconsistent across doses | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.039 | 3/43 (LoVo, PANC-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.054 | 4/36 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14010.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.588×** | -5.5 | 3e-05 | 12/47 (H4, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.599×** | -5.3 | 4e-05 | 15/46 (LOX-IMVI, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.638×** | -4.6 | 7e-04 | 8/44 (HCT15, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.648×** | -4.5 | 0.001 | 13/38 (A-427, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.909× | -3.6 | 0.037 | 11/48 (SHP-77, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.718×** | -3.4 | 0.062 | 10/46 (SW 900, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14010. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 3.09 | 0 | 1 | — | [[Norepinephrine (hydrochloride) (drug)]] 5 µM 0.189× (z -8.6) |
| [[HT-29 (line)]] | alt | 3.02 | 0 | 1 | — | [[Esmolol (hydrochloride) (drug)]] 0.5 µM 0.0667× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 3.40 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 9.57× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14010), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GEMIN7-AS1]] | +0.74 | +0.68 / +0.60 | both halves | 7e-06 | same gene group |
| [[NAPA-AS1]] | +0.68 | +0.55 / +0.50 | both halves | 1e-05 | same gene group |
| [[ATP1A1-AS1]] | +0.66 | +0.44 / +0.54 | both halves | 3e-05 | same gene group |
| [[PAXBP1-AS1]] | +0.65 | +0.41 / +0.52 | both halves | 4e-05 | same gene group |
| [[PXN-AS1]] | +0.65 | +0.55 / +0.59 | both halves | 1e-05 | same gene group |
| [[ADNP-AS1]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 | same gene group |
| [[C2CD5-AS1]] | +0.63 | +0.47 / +0.46 | both halves | 2e-05 | same gene group |
| [[SPATA21]] | +0.63 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[RTCA-AS1]] | +0.63 | +0.51 / +0.33 | both halves | 1e-04 | same gene group |
| [[CYB5D2]] | +0.63 | +0.44 / +0.40 | both halves | 4e-05 |  |
| [[ZNF451-AS1]] | +0.63 | +0.49 / +0.48 | both halves | 2e-05 | same gene group |
| [[TSPOAP1-AS1]] | +0.62 | +0.50 / +0.55 | both halves | 1e-05 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises HNRNPK-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.598). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.9, 25.2); signed map (33.7, -1.7). **Vector** length 30.2, 2.36% of its response variance represented; |z| ≥ 3 in 834 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +8.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | -1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | +1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.0 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +1.5 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -1.2 | -4.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -0.9 | -0.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -0.9 | -5.3 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -0.9 | +0.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | -0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.7 | +1.2 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -0.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | HNRNPK antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 9q21.32 — chr9:83,972,233-83,975,777 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56061](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56061) · Entrez [123706516](https://www.ncbi.nlm.nih.gov/gene/123706516) · Ensembl [ENSG00000235298](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235298)

## Data

Gene col 14010: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14010); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14010, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14010]; `tensor/DDL_lfc|DDL_z.npy` [14010]; `embed/gene_vectors.npy` [14010]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14010 or target_col == 14010). Every well: [[HNRNPK-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNRNPK-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
