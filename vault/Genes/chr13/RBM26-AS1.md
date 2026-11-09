---
symbol: "RBM26-AS1"
type: "gene"
col: 13584
ensembl_id: "ENSG00000227354"
name: "RBM26 antisense RNA 1"
location: "13q31.1"
module: 10
arm: "+"
pooled_cpm: 3.16
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 7
n_dd_up_clean: 18
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# RBM26-AS1

*RBM26 antisense RNA 1* — 13q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.24× (z +18.6, q 0e+00, up in 28 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.543× (z -5.6, q 1e-05, down in 22 of 44 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCDIN3D]] (+0.84, fdr 7e-06), [[LINC02340]] (+0.80, fdr 7e-06), [[PCNX4-DT]] (+0.80, fdr 2e-05); moves opposite to [[IGSF8]] (-0.70, fdr 1e-04), [[ANKRD27]] (-0.69, fdr 4e-04), [[GNB2]] (-0.67, fdr 3e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13584.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.24×** | +18.6 | 0e+00 | 28/33 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.55×** | +16.3 | 0e+00 | 30/31 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.55×** | +11.6 | 1e-28 | 28/34 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.80×** | +9.0 | 2e-17 | 26/42 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.79×** | +9.0 | 2e-17 | 18/26 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +7.6 | 2e-12 | 1/4 (SW480) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.34×** | +7.4 | 7e-12 | 6/12 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.26×** | +7.4 | 7e-12 | 24/42 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.26×** | +6.9 | 4e-10 | 2/4 (A498, HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.12×** | +6.9 | 4e-10 | 4/13 (HEC-1-A, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.09×** | +6.7 | 8e-10 | 19/44 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +5.2 | 8e-06 | 10/32 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +5.0 | 2e-05 | 8/44 (SW480, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.71×** | +4.9 | 5e-05 | 11/45 (KATO III, LS 180, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.4 | 4e-04 | 8/46 (HEC-1-A, NCI-H2347, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +3.4 | 0.021 | 9/41 (HEC-1-A, SHP-77, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.022 | 3/46 (KATO III, SW480, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.024 | 1/43 (AN3 CA) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.047 | 4/47 (COLO 205, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13584.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.543×** | -5.6 | 1e-05 | 22/44 (SW480, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.591×** | -4.5 | 0.002 | 15/37 (A498, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.633×** | -4.2 | 0.006 | 19/42 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.680×** | -3.5 | 0.060 | 8/46 (A-172, NCI-H661, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.499×** | -3.3 | 0.077 | 10/37 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.696×** | -3.3 | 0.077 | 7/46 (SNU-1, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.501×** | -3.3 | 0.077 | 7/31 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13584. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.1 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +9.9) | [[Ixazomib citrate (drug)]] 5 µM 0.237× (z -9.3) |
| [[LoVo (line)]] | wt | 4.46 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +14.4) | — |
| [[A498 (line)]] | wt | 4.32 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0618× (z -9.3) |
| [[HCT15 (line)]] | alt | 3.75 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 4.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.61× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 4.11 | 0 | 1 | — | [[Sulfisoxazole (drug)]] 0.05 µM 0.0597× (z -9.4) |
| [[A-172 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.822 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.961 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13584), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCDIN3D]] | +0.84 | +0.85 / +0.71 | both halves | 7e-06 |  |
| [[LINC02340]] | +0.80 | +0.86 / +0.60 | both halves | 7e-06 |  |
| [[PCNX4-DT]] | +0.80 | +0.83 / +0.47 | both halves | 2e-05 |  |
| [[LINC00240]] | +0.79 | +0.83 / +0.55 | both halves | 1e-05 |  |
| [[PPP3CB-AS1]] | +0.79 | +0.78 / +0.46 | both halves | 3e-05 | same gene group |
| [[WARS2-AS1]] | +0.78 | +0.79 / +0.38 | both halves | 6e-05 | same gene group |
| [[PPP1R3F]] | +0.78 | +0.76 / +0.46 | both halves | 3e-05 |  |
| [[RFX3-DT]] | +0.77 | +0.79 / +0.45 | both halves | 3e-05 |  |
| [[OXA1L-DT]] | +0.77 | +0.79 / +0.44 | both halves | 3e-05 |  |
| [[GUCY2C-AS1]] | +0.77 | +0.81 / +0.45 | both halves | 3e-05 | same gene group |
| [[KRCC1]] | +0.77 | +0.78 / +0.49 | both halves | 1e-05 |  |
| [[SEPTIN7-DT]] | +0.76 | +0.77 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGSF8]] | -0.70 | -0.70 / -0.35 | both halves | 1e-04 |  |
| [[ANKRD27]] | -0.69 | -0.70 / -0.26 | both halves | 4e-04 |  |
| [[GNB2]] | -0.67 | -0.64 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RBM26-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises RBM26-AS1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.785). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (5.6, 14.8); signed map (27.1, -11.0). **Vector** length 63.3, 9.64% of its response variance represented; |z| ≥ 3 in 1,175 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.2 | +11.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +18.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.1 | +9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +16.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.1 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +3.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.2 | -5.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +1.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | +0.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | +0.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.8 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +0.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.9 | -3.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -1.9 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | RBM26 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 13q31.1 — chr13:79,406,293-79,427,317 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:39805](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:39805) · Entrez [100505538](https://www.ncbi.nlm.nih.gov/gene/100505538) · Ensembl [ENSG00000227354](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227354)

## Data

Gene col 13584: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13584); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13584, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13584]; `tensor/DDL_lfc|DDL_z.npy` [13584]; `embed/gene_vectors.npy` [13584]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13584 or target_col == 13584). Every well: [[RBM26-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM26-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
