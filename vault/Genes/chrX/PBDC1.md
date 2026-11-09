---
symbol: "PBDC1"
type: "gene"
col: 2244
ensembl_id: "ENSG00000102390"
name: "polysaccharide biosynthesis domain containing 1"
location: "Xq13.3"
module: 11
arm: "+"
pooled_cpm: 22.14
n_lines_expressing: 48
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# PBDC1

*polysaccharide biosynthesis domain containing 1* — Xq13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.38× (z +8.4, q 3e-14, up in 42 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.358× (z -9.9, q 2e-20, down in 44 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPP25L]] (+0.76, fdr 7e-06), [[TRIP11]] (+0.73, fdr 7e-06), [[ATF5]] (+0.72, fdr 3e-05); moves opposite to [[HDAC1]] (-0.69, fdr 1e-05), [[NOMO1]] (-0.69, fdr 3e-05), [[RPA1]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2244.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.38×** | +8.4 | 3e-14 | 42/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.21×** | +7.7 | 4e-12 | 43/46 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.25×** | +7.6 | 7e-12 | 42/46 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.18×** | +7.2 | 7e-11 | 39/42 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.63×** | +6.2 | 6e-08 | 33/45 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.67×** | +5.0 | 6e-05 | 32/46 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +4.3 | 0.001 | 29/45 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~63% of this change | **1.48×** | +3.8 | 0.010 | 22/44 (HT-29, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **1.48×** | +3.8 | 0.010 | 23/39 (A549, RPMI-7951, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.46×** | +3.7 | 0.013 | 22/44 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.043 | 21/46 (NCI-H2347, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.43×** | +3.2 | 0.061 | 17/45 (PANC-1, NCI-H460, …) | all doses, flat | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.061 | 22/45 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.061 | 23/45 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.091 | 16/45 (NCI-H460, HT-29, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2244.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.358×** | -9.9 | 2e-20 | 44/45 (KATO III, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.361×** | -9.8 | 2e-20 | 43/46 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.401×** | -8.8 | 2e-16 | 41/46 (KATO III, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.355×** | -5.2 | 2e-05 | 35/46 (KATO III, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.600×** | -4.9 | 1e-04 | 35/46 (KATO III, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.617×** | -4.7 | 3e-04 | 28/44 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.700×** | -3.4 | 0.048 | 25/46 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.545× | -3.1 | 0.16 | 17/46 (PANC-1, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2244. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +9.3) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.36× (z +9.2) | — |
| [[KATO III (line)]] | alt | 37.9 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.189× (z -12.2) |
| [[SW480 (line)]] | alt | 35.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.237× (z -10.4) |
| [[A-172 (line)]] | wt | 14.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +8.5) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[CHP-212 (line)]] | wt | 22.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0623× (z -9.1) |
| [[LS 180 (line)]] | wt | 21.3 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.206× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 23.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +12.0) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[NCI-H2347 (line)]] | alt | 33.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.275× (z -9.9) |
| [[RKO (line)]] | wt | 29.0 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.190× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 41.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +9.0) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[A-427 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.88 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2244), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP25L]] | +0.76 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[TRIP11]] | +0.73 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[ATF5]] | +0.72 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[FAM200A]] | +0.71 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[MED18]] | +0.71 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[ARL14EP]] | +0.71 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[LINC02307]] | +0.70 | +0.78 / +0.49 | both halves | 1e-05 |  |
| [[RPP38]] | +0.70 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[C14orf119]] | +0.70 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[ZNF830]] | +0.69 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[ZNF525]] | +0.69 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[TOPORS]] | +0.69 | +0.68 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC1]] | -0.69 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[NOMO1]] | -0.69 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[RPA1]] | -0.68 | -0.67 / -0.59 | both halves | 7e-06 |  |
| [[ABCA2]] | -0.68 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[TM9SF2]] | -0.67 | -0.72 / -0.59 | both halves | 7e-06 |  |
| [[PIK3R2]] | -0.67 | -0.69 / -0.47 | both halves | 2e-05 |  |
| [[CEP131]] | -0.67 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[NUDT21]] | -0.66 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[COL18A1]] | -0.65 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[KHDRBS1]] | -0.65 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[NOMO3]] | -0.65 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[GET1]] | -0.65 | -0.62 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PBDC1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.770). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-33.9, 6.3); signed map (3.7, -18.6). **Vector** length 89.6, 24.8% of its response variance represented; |z| ≥ 3 in 765 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.1 | +8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +8.0 | +6.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +6.1 | +7.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.8 | +3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.7 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +5.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +4.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.1 | +0.7 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.8 | -9.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.1 | -8.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.0 | -9.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.3 | -3.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.1 | -4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -5.2 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -1.3 | -2.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.0 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | polysaccharide biosynthesis domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.3 — chrX:76,173,040-76,178,314 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC874; previously CXorf26 |
| Matched by | ensembl_id |

UniProt [Q9BVG4](https://www.uniprot.org/uniprotkb/Q9BVG4) carries no function annotation.

**Summary**, from NCBI Gene [51260](https://www.ncbi.nlm.nih.gov/gene/51260):

> Predicted to enable protein folding chaperone. Predicted to be involved in 'de novo' cotranslational protein folding. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28790](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28790) · Entrez [51260](https://www.ncbi.nlm.nih.gov/gene/51260) · UniProt [Q9BVG4](https://www.uniprot.org/uniprotkb/Q9BVG4) · Ensembl [ENSG00000102390](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102390)

## Data

Gene col 2244: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2244); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2244, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2244]; `tensor/DDL_lfc|DDL_z.npy` [2244]; `embed/gene_vectors.npy` [2244]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2244 or target_col == 2244). Every well: [[PBDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PBDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
