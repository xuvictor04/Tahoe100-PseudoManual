---
symbol: "COCH"
type: "gene"
col: 1968
ensembl_id: "ENSG00000100473"
name: "cochlin"
location: "14q12"
module: 21
arm: "+"
pooled_cpm: 8.83
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# COCH

*cochlin* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.92× (z +13.2, q 8e-37, up in 26 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.42× (z +4.3, q 0.002, up in 11 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.654× (z -5.2, q 1e-04, down in 17 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (J82 0.243×, LoVo 0.306×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 0.176×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H23 0.0900×; ⚠ cell-cycle shift, explains ~0% of this change); [[Diphenhydramine (drug)]] 5 µM in 1 line (AsPC-1 0.0524×); [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM in 1 line (NCI-H23 0.1000×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCDH15]] (+0.60, fdr 1e-05), [[PDE8B]] (+0.56, fdr 2e-05), [[OMG]] (+0.54, fdr 5e-05); moves opposite to [[ILVBL]] (-0.46, fdr 6e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1968.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.92×** | +13.2 | 8e-37 | 26/27 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.67×** | +11.6 | 2e-28 | 15/16 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +7.3 | 7e-11 | 12/21 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +4.3 | 0.002 | 11/46 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.005 | 13/47 (BT-474, NCI-H1573, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.005 | 10/40 (NCI-H2347, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.006 | 8/39 (LOX-IMVI, SNU-423, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Allantoin (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.006 | 10/46 (LoVo, A549, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.35×** | +3.7 | 0.015 | 12/34 (CFPAC-1, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.019 | 6/45 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.31×** | +3.3 | 0.043 | 10/39 (Hs 766T, A-172, …) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.46×** | +3.3 | 0.045 | 4/45 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +3.3 | 0.045 | 11/45 (KATO III, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.3 | 0.045 | 6/43 (A498, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1968.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (J82 0.243×, LoVo 0.306×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 0.176×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H23 0.0900×; ⚠ cell-cycle shift, explains ~0% of this change); [[Diphenhydramine (drug)]] 5 µM in 1 line (AsPC-1 0.0524×); [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM in 1 line (NCI-H23 0.1000×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.654×** | -5.2 | 1e-04 | 17/47 (BT-474, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.692×** | -4.5 | 0.002 | 14/47 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.755× | -3.4 | 0.11 | 10/46 (J82, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.745× | -3.2 | 0.22 | 2/47 (AN3 CA, HCT15) | inconsistent across doses | position effect removed |
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | 0.776× | -3.1 | 0.22 | 4/46 (A498, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1968. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 5.29 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0900× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM 0.1000× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 3.70 | 0 | 1 | — | [[Diphenhydramine (drug)]] 5 µM 0.0524× (z -8.8) |
| [[J82 (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 20.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 33.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.67× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -9.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1968), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 7 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCDH15]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[PDE8B]] | +0.56 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[OMG]] | +0.54 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[LINC02755]] | +0.53 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[IQCM]] | +0.52 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[KCNMB2]] | +0.52 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[SPTBN1-AS2]] | +0.52 | +0.39 / +0.52 | both halves | 6e-05 |  |
| [[C1orf56]] | +0.51 | +0.37 / +0.45 | both halves | 8e-05 |  |
| [[C12orf40]] | +0.51 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[PPP1R9A-AS1]] | +0.50 | +0.37 / +0.44 | both halves | 8e-05 |  |
| [[GALNT17]] | +0.49 | +0.29 / +0.46 | both halves | 2e-04 |  |
| [[C3orf49]] | +0.49 | +0.42 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ILVBL]] | -0.46 | -0.39 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises COCH's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.466). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.4, 24.7); signed map (36.1, 10.6). **Vector** length 39.4, 4.01% of its response variance represented; |z| ≥ 3 in 691 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +13.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +11.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +7.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.4 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +0.7 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -2.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.0 | -0.3 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.0 | -2.2 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.9 | -1.8 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | cochlin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:30,874,514-30,895,065 (+) |
| Ensembl biotype | protein_coding |
| Also known as | COCH-5B2; previously DFNA31, DFNA9 |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [O43405](https://www.uniprot.org/uniprotkb/O43405) (Cochlin):

> Plays a role in the control of cell shape and motility in the trabecular meshwork.

**Summary**, from NCBI Gene [1690](https://www.ncbi.nlm.nih.gov/gene/1690):

> The protein encoded by this gene is highly conserved in human, mouse, and chicken, showing 94% and 79% amino acid identity of human to mouse and chicken sequences, respectively. Hybridization to this gene was detected in spindle-shaped cells located along nerve fibers between the auditory ganglion and sensory epithelium. These cells accompany neurites at the habenula perforata, the opening through which neurites extend to innervate hair cells. This and the pattern of expression of this gene in …

**Accessions** — [HGNC:2180](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2180) · Entrez [1690](https://www.ncbi.nlm.nih.gov/gene/1690) · UniProt [O43405](https://www.uniprot.org/uniprotkb/O43405) · Ensembl [ENSG00000100473](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100473)

## Data

Gene col 1968: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1968); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1968, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1968]; `tensor/DDL_lfc|DDL_z.npy` [1968]; `embed/gene_vectors.npy` [1968]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1968 or target_col == 1968). Every well: [[COCH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COCH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
