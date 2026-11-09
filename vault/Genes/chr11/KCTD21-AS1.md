---
symbol: "KCTD21-AS1"
type: "gene"
col: 14454
ensembl_id: "ENSG00000246174"
name: "KCTD21 antisense RNA 1"
location: "11q14.1"
module: 35
arm: "+"
pooled_cpm: 2.55
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 6
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# KCTD21-AS1

*KCTD21 antisense RNA 1* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.62× (z +19.2, q 0e+00, up in 31 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.397× (z -8.2, q 1e-13, down in 26 of 40 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDNF]] (+0.72, fdr 7e-06), [[PJVK]] (+0.67, fdr 1e-05), [[MYL6B-AS1]] (+0.66, fdr 1e-05); moves opposite to [[LIFR]] (-0.55, fdr 2e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14454.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.62×** | +19.2 | 0e+00 | 31/31 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.78×** | +8.0 | 4e-13 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.87×** | +7.8 | 1e-12 | 20/42 (LS 180, RKO, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +7.7 | 3e-12 | 3/11 (Hs 766T, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.98×** | +6.0 | 2e-07 | 15/42 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +5.5 | 3e-06 | 6/33 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +5.1 | 2e-05 | 13/37 (LoVo, NCI-H23, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +4.9 | 8e-05 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +4.7 | 2e-04 | 11/26 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.4 | 6e-04 | 9/43 (A-172, HEC-1-A, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.64×** | +4.4 | 6e-04 | 13/38 (HEC-1-A, RPMI-7951, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.56×** | +3.9 | 0.004 | 8/45 (A-172, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.65×** | +3.9 | 0.004 | 2/12 (A-427, NCI-H23) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.53×** | +3.7 | 0.007 | 7/40 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.52×** | +3.7 | 0.008 | 7/34 (NCI-H2030, SHP-77, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.51×** | +3.6 | 0.010 | 4/43 (PANC-1, A-172, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.34×** | +3.5 | 0.013 | 6/43 (Hs 766T, NCI-H23, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.44×** | +3.2 | 0.040 | 2/24 (MIA PaCa-2, NCI-H2030) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14454.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.397×** | -8.2 | 1e-13 | 26/40 (PANC-1, A-172, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.436×** | -7.4 | 4e-11 | 24/45 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.528×** | -5.7 | 3e-06 | 20/36 (SHP-77, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.562×** | -5.1 | 4e-05 | 16/23 (NCI-H2030, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.416×** | -4.1 | 0.005 | 12/34 (NCI-H23, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.620×** | -3.8 | 0.016 | 12/38 (PANC-1, KATO III, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.776× | -3.2 | 0.11 | 12/31 (A-172, Hs 766T, …) | top dose only | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | 0.514× | -3.1 | 0.14 | 8/25 (HOP62, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.712× | -3.0 | 0.14 | 9/45 (LoVo, HepG2/C3A, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.713× | -3.0 | 0.14 | 4/35 (HepG2/C3A, LS 180, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14454. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 3.51 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.77× (z +10.1) | [[Digitoxin (drug)]] 0.5 µM 0.0605× (z -12.8) |
| [[A-172 (line)]] | wt | 2.79 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 1.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.1× (z +11.3) | — |
| [[KATO III (line)]] | alt | 3.66 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0664× (z -8.9) |
| [[LoVo (line)]] | wt | 1.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 3.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.66× (z +10.3) | — |
| [[SW480 (line)]] | alt | 1.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.82× (z +10.7) | — |
| [[A-427 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.561 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.703 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.830 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.934 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.679 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.691 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.782 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.907 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14454), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDNF]] | +0.72 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[PJVK]] | +0.67 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[MYL6B-AS1]] | +0.66 | +0.54 / +0.58 | both halves | 1e-05 | same gene group |
| [[CNPY2-AS1]] | +0.64 | +0.52 / +0.61 | both halves | 1e-05 | same gene group |
| [[ATP6V0D1-DT]] | +0.63 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[SUMO2P17]] | +0.62 | +0.63 / +0.36 | both halves | 1e-04 |  |
| [[ZNF236-DT]] | +0.62 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[LRIG2-DT]] | +0.62 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[RTCA-AS1]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 | same gene group |
| [[DNAJC30]] | +0.61 | +0.49 / +0.57 | both halves | 2e-05 |  |
| [[MYLK4]] | +0.60 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[SRRM2-AS1]] | +0.60 | +0.55 / +0.49 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIFR]] | -0.55 | -0.40 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KCTD21-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.649). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (7.1, 24.2); signed map (32.2, -3.3). **Vector** length 38.5, 4.04% of its response variance represented; |z| ≥ 3 in 1,027 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +19.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +2.8 | +7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +5.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +4.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.5 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.0 | -0.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.8 | +4.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | +2.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -1.2 | -3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | +1.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.9 | -3.0 |
|  | [[Malotilate (drug)]] 0.05 µM |  | -0.8 | -1.3 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -0.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | KCTD21 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q14.1 — chr11:78,139,756-78,175,323 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48674](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48674) · Entrez [100289388](https://www.ncbi.nlm.nih.gov/gene/100289388) · Ensembl [ENSG00000246174](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000246174)

## Data

Gene col 14454: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14454); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14454, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14454]; `tensor/DDL_lfc|DDL_z.npy` [14454]; `embed/gene_vectors.npy` [14454]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14454 or target_col == 14454). Every well: [[KCTD21-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCTD21-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
