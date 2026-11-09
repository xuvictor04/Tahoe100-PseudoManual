---
symbol: "PCMTD1-DT"
type: "gene"
col: 13676
ensembl_id: "ENSG00000228801"
name: "PCMTD1 divergent transcript"
location: "8q11.23"
module: 15
arm: "+"
pooled_cpm: 3.52
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 9
n_dd_up_clean: 25
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# PCMTD1-DT

*PCMTD1 divergent transcript* — 8q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.74× (z +20.6, q 0e+00, up in 32 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.542× (z -5.7, q 3e-06, down in 23 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DICER1-AS1]] (+0.74, fdr 7e-06), [[SPESP1]] (+0.71, fdr 1e-05), [[USP38-DT]] (+0.68, fdr 1e-05); moves opposite to [[DNAJB1]] (-0.57, fdr 6e-05), [[SLC45A4]] (-0.57, fdr 2e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13676.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.74×** | +20.6 | 0e+00 | 32/35 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.77×** | +9.0 | 6e-17 | 21/31 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.18×** | +7.3 | 6e-11 | 25/44 (KATO III, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.71×** | +7.1 | 2e-10 | 13/44 (KATO III, SHP-77, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.22×** | +7.1 | 2e-10 | 7/17 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +5.5 | 4e-06 | 2/4 (HOP62, HS-578T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +5.4 | 5e-06 | 6/17 (NCI-H2347, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +5.2 | 2e-05 | 14/35 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.9 | 6e-05 | 9/45 (A-172, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +4.6 | 2e-04 | 12/44 (A498, RPMI-7951, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +4.6 | 2e-04 | 3/6 (MIA PaCa-2, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.61×** | +4.5 | 4e-04 | 8/41 (NCI-H23, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.59×** | +4.3 | 6e-04 | 10/42 (A-427, SHP-77, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +4.3 | 8e-04 | 13/46 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +4.2 | 0.001 | 16/44 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **1.33×** | +3.7 | 0.007 | 10/44 (SW480, A498, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.50×** | +3.6 | 0.010 | 10/41 (SK-MEL-2, NCI-H1573, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.32×** | +3.6 | 0.010 | 6/44 (MIA PaCa-2, BT-474, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.45×** | +3.5 | 0.014 | 3/45 (A-427, CFPAC-1, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13676.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.542×** | -5.7 | 3e-06 | 23/45 (HS-578T, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.543×** | -5.7 | 3e-06 | 23/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.564×** | -5.4 | 1e-05 | 19/43 (BT-474, SW480, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.605×** | -4.7 | 3e-04 | 18/42 (A-427, J82, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.610×** | -4.4 | 0.001 | 16/41 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.658×** | -3.9 | 0.008 | 15/32 (PANC-1, NCI-H23, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.677×** | -3.7 | 0.021 | 16/42 (NCI-H2347, A-427, …) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **0.688×** | -3.5 | 0.030 | 8/43 (RKO, AsPC-1, …) | all doses, flat |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.769×** | -3.5 | 0.030 | 9/45 (SW 900, C-33 A, …) | all doses, flat |  |
| [[PF-06260933 (drug)]] 5 µM |  | 0.530× | -3.1 | 0.11 | 8/22 (PANC-1, SW480, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13676. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 2.95 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.69× (z +9.2) | [[Harringtonine (drug)]] 5 µM 0.0528× (z -10.4) ⚠ cell-cycle shift, explains ~84% of this change |
| [[A-172 (line)]] | wt | 5.09 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.105× (z -8.6) |
| [[A-427 (line)]] | wt | 4.70 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0775× (z -9.5) |
| [[A498 (line)]] | wt | 6.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.98× (z +10.8) | — |
| [[HOP62 (line)]] | alt | 4.10 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0860× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~86% of this change |
| [[LS 180 (line)]] | wt | 3.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.37× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 2.11 | 0 | 1 | — | [[Baicalin (drug)]] 0.05 µM 0.0506× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 2.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.45× (z +9.6) | — |
| [[A549 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13676), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DICER1-AS1]] | +0.74 | +0.75 / +0.58 | both halves | 7e-06 |  |
| [[SPESP1]] | +0.71 | +0.76 / +0.54 | both halves | 1e-05 |  |
| [[USP38-DT]] | +0.68 | +0.72 / +0.54 | both halves | 1e-05 | same gene group |
| [[CDNF]] | +0.66 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[APPBP2-DT]] | +0.66 | +0.67 / +0.57 | both halves | 9e-06 | same gene group |
| [[GAS2]] | +0.66 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[ZBED5-AS1]] | +0.66 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[BDNF-AS]] | +0.65 | +0.77 / +0.39 | both halves | 5e-05 |  |
| [[ZNF236-DT]] | +0.65 | +0.63 / +0.56 | both halves | 1e-05 | same gene group |
| [[SEC24B-AS1]] | +0.63 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[FKBP14-AS1]] | +0.63 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[AHI1-DT]] | +0.63 | +0.63 / +0.48 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJB1]] | -0.57 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[SLC45A4]] | -0.57 | -0.55 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PCMTD1-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises PCMTD1-DT's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TMCC1-DT]] | C | TMCC1-DT activity raises PCMTD1-DT's level | lines that do not express TMCC1-DT (3) vs lines expressing it (47) | 1.78× lower at baseline in the lines without TMCC1-DT | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, WWOX, DBNDD1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.624). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (3.2, 20.9); signed map (29.0, -7.9). **Vector** length 54.7, 7.91% of its response variance represented; |z| ≥ 3 in 934 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +20.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +4.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.6 | +3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +1.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.7 | -5.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.2 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | +2.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.3 | -1.7 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.2 | -2.7 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.2 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | PCMTD1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q11.23 — chr8:51,899,268-51,949,874 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55791](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55791) · Entrez [102724330](https://www.ncbi.nlm.nih.gov/gene/102724330) · Ensembl [ENSG00000228801](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228801)

## Data

Gene col 13676: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13676); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13676, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13676]; `tensor/DDL_lfc|DDL_z.npy` [13676]; `embed/gene_vectors.npy` [13676]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13676 or target_col == 13676). Every well: [[PCMTD1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCMTD1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
