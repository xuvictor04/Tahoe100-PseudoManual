---
symbol: "FAM174A-DT"
type: "gene"
col: 14509
ensembl_id: "ENSG00000247877"
name: "FAM174A divergent transcript"
location: "5q21.1"
module: 10
arm: "+"
pooled_cpm: 5.32
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 23
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# FAM174A-DT

*FAM174A divergent transcript* — 5q21.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.246× (z -10.0, q 1e-20, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CARF]] (+0.69, fdr 7e-06), [[CASC2]] (+0.68, fdr 7e-06), [[ZRANB2-DT]] (+0.67, fdr 7e-06); moves opposite to [[ABHD3]] (-0.57, fdr 2e-05), [[TMEM184B]] (-0.56, fdr 2e-05), [[CARD19]] (-0.53, fdr 7e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[THBS4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14509.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 0.5 µM |  | 1.61× | +3.4 | 0.26 | 11/45 (MIA PaCa-2, KATO III, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.65× | +3.3 | 0.26 | 11/45 (SW480, HepG2/C3A, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.36× | +3.1 | 0.42 | 9/47 (SW480, SK-MEL-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14509.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.246×** | -10.0 | 1e-20 | 41/46 (SHP-77, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.330×** | -7.9 | 9e-13 | 36/46 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.362×** | -7.2 | 1e-10 | 33/44 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.364×** | -7.2 | 1e-10 | 24/37 (SW480, SHP-77, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.409×** | -6.3 | 3e-08 | 27/45 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.435×** | -5.9 | 3e-07 | 28/44 (PANC-1, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.423×** | -5.8 | 7e-07 | 26/43 (MIA PaCa-2, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.566×** | -5.7 | 9e-07 | 23/41 (A-172, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.481×** | -5.2 | 1e-05 | 20/40 (NCI-H460, A549, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.475×** | -5.1 | 2e-05 | 24/44 (PANC-1, C32, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.472×** | -4.9 | 5e-05 | 27/46 (AN3 CA, SNU-423, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.533×** | -4.5 | 4e-04 | 19/47 (SW480, A-427, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.560×** | -4.0 | 0.003 | 18/30 (LS 180, SK-MEL-2, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.602×** | -3.6 | 0.013 | 16/46 (CFPAC-1, LoVo, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.703×** | -3.5 | 0.016 | 18/46 (SNU-1, AN3 CA, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.425×** | -3.2 | 0.050 | 11/43 (SW480, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Aprepitant (drug)]] 0.05 µM |  | **0.649×** | -3.1 | 0.066 | 16/45 (COLO 205, A-172, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.640×** | -3.0 | 0.066 | 14/46 (NCI-H23, NCI-H1792, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.558×** | -3.0 | 0.085 | 9/45 (A-427, SW 1271, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.662×** | -2.9 | 0.089 | 12/39 (CFPAC-1, SW 900, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.63 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14509. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.44 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0474× (z -13.6) |
| [[LS 180 (line)]] | wt | 9.64 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.107× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~36% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.124× (z -8.6) |
| [[SHP-77 (line)]] | alt | 15.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0576× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0777× (z -10.9) |
| [[SW480 (line)]] | alt | 5.75 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0403× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -8.9) |
| [[A-172 (line)]] | wt | 7.30 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -9.0) ⚠ cell-cycle shift, explains ~82% of this change |
| [[CFPAC-1 (line)]] | alt | 3.76 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0441× (z -9.4) |
| [[J82 (line)]] | alt | 4.71 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0495× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 12.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.103× (z -8.5) |
| [[RKO (line)]] | wt | 7.32 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0724× (z -9.0) |
| [[A-427 (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14509), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CARF]] | +0.69 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[CASC2]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[ZRANB2-DT]] | +0.67 | +0.68 / +0.66 | both halves | 7e-06 | same gene group |
| [[SPATA17]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[FRG1-DT]] | +0.62 | +0.59 / +0.58 | both halves | 8e-06 | same gene group |
| [[CRB1]] | +0.61 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[TTC30A]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[TAPT1-AS1]] | +0.60 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[ZFX]] | +0.60 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[B3GALT9]] | +0.59 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[BDNF-AS]] | +0.59 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[LINC00667]] | +0.59 | +0.56 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABHD3]] | -0.57 | -0.49 / -0.49 | both halves | 2e-05 |  |
| [[TMEM184B]] | -0.56 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[CARD19]] | -0.53 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[CIAO2B]] | -0.52 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[POR]] | -0.52 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[SLC17A5]] | -0.52 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[SLC37A3]] | -0.51 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[RAB11FIP1]] | -0.50 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[F11R]] | -0.50 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[ARFGAP3]] | -0.49 | -0.52 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THBS4]] | B | THBS4 activity raises FAM174A-DT's level | lines that do not express THBS4 (6) vs lines expressing it (44) | 1.85× lower at baseline in the lines without THBS4 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.642). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-28.5, 27.7); signed map (3.2, 5.0). **Vector** length 56.3, 8.39% of its response variance represented; |z| ≥ 3 in 1,094 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +1.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | -1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +1.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.3 | +2.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.0 | -7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.7 | -5.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.1 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -6.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | FAM174A divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q21.1 — chr5:100,428,124-100,535,262 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55584](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55584) · Entrez [121232371](https://www.ncbi.nlm.nih.gov/gene/121232371) · Ensembl [ENSG00000247877](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247877)

## Data

Gene col 14509: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14509); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14509, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14509]; `tensor/DDL_lfc|DDL_z.npy` [14509]; `embed/gene_vectors.npy` [14509]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14509 or target_col == 14509). Every well: [[FAM174A-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM174A-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
