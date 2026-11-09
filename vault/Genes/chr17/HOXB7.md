---
symbol: "HOXB7"
type: "gene"
col: 15256
ensembl_id: "ENSG00000260027"
name: "homeobox B7"
location: "17q21.32"
module: 46
arm: "+"
pooled_cpm: 19.83
n_lines_expressing: 43
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# HOXB7

*homeobox B7* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.46× (z +13.3, q 1e-37, up in 37 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.325× (z -11.7, q 7e-29, down in 38 of 41 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOTAIR]] (+0.74, fdr 1e-05), [[EFCAB5]] (+0.69, fdr 5e-04), [[AHI1-DT]] (+0.68, fdr 1e-04); moves opposite to [[GPRIN1]] (-0.65, fdr 2e-04), [[DGKD]] (-0.61, fdr 2e-04), [[FLNB]] (-0.60, fdr 0.001, ⚠ one half only (not replicated)).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HOXB8]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CMIP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15256.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +13.3 | 1e-37 | 37/40 (A498, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.78×** | +10.6 | 5e-24 | 28/33 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.85×** | +10.5 | 2e-23 | 27/30 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.98×** | +6.9 | 9e-10 | 29/36 (A-427, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +5.6 | 3e-06 | 22/32 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +4.4 | 1e-03 | 25/38 (LOX-IMVI, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.008 | 19/38 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +3.7 | 0.014 | 19/39 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.018 | 22/41 (NCI-H1792, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15256.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.325×** | -11.7 | 7e-29 | 38/41 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.360×** | -10.6 | 6e-24 | 39/41 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.408×** | -9.3 | 2e-18 | 38/41 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.557×** | -8.6 | 1e-15 | 31/39 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.602×** | -5.3 | 1e-05 | 29/41 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.651×** | -4.5 | 8e-04 | 22/38 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.667×** | -4.2 | 0.002 | 24/41 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.656×** | -4.1 | 0.003 | 23/39 (HT-29, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.680×** | -4.0 | 0.004 | 23/41 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.485×** | -3.9 | 0.005 | 18/40 (KATO III, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.700×** | -3.7 | 0.011 | 20/40 (NCI-H23, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.716×** | -3.5 | 0.025 | 16/40 (HT-29, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.538×** | -3.4 | 0.032 | 17/37 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.540×** | -3.3 | 0.033 | 17/40 (SW480, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15256. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 43.7 | 3 (2 ⚠) | 8 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -15.7) |
| [[HT-29 (line)]] | alt | 45.0 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.170× (z -14.2) |
| [[SW480 (line)]] | alt | 33.2 | 2 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.186× (z -15.1) |
| [[LoVo (line)]] | wt | 28.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -10.7) |
| [[SW1417 (line)]] | alt | 45.8 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +10.1) | [[Panobinostat (drug)]] 0.5 µM 0.158× (z -14.1) |
| [[A498 (line)]] | wt | 19.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +14.7) | — |
| [[HCT15 (line)]] | alt | 59.2 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.202× (z -9.1) |
| [[KATO III (line)]] | alt | 35.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.206× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 13.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.188× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 11.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +12.6) | [[Belinostat (drug)]] 5 µM 0.249× (z -8.8) |
| [[SW48 (line)]] | wt | 48.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.111× (z -11.6) |
| [[A-172 (line)]] | wt | 14.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +9.6) | — |
| [[A549 (line)]] | wt | 13.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +13.2) | — |
| [[BT-474 (line)]] | alt | 19.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +8.7) | — |
| [[C32 (line)]] | wt | 19.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 16.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -9.8) |
| [[COLO 205 (line)]] | alt | 20.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0759× (z -16.6) |
| [[HOP62 (line)]] | alt | 27.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -13.7) |
| [[NCI-H1573 (line)]] | alt | 12.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -12.3) |
| [[Panc 03.27 (line)]] | alt | 23.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.211× (z -10.4) |
| [[RKO (line)]] | wt | 13.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 21.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.225× (z -8.9) |
| [[A-427 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.17 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.49 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15256), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 17 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOTAIR]] | +0.74 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[EFCAB5]] | +0.69 | +0.47 / +0.23 | both halves | 5e-04 |  |
| [[AHI1-DT]] | +0.68 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[DICER1-AS1]] | +0.68 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[HOXC9]] | +0.68 | +0.28 / +0.62 | both halves | 3e-04 | same gene group; STRING 688 |
| [[SEC24B-AS1]] | +0.68 | +0.45 / +0.37 | both halves | 9e-05 |  |
| [[SPEN-AS1]] | +0.68 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[GALNT7-DT]] | +0.67 | +0.48 / +0.30 | both halves | 2e-04 |  |
| [[NCOA2]] | +0.67 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[KLF3-AS1]] | +0.67 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[HOXB-AS1]] | +0.67 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[GAS2]] | +0.66 | +0.54 / +0.23 | both halves | 5e-04 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRIN1]] | -0.65 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[DGKD]] | -0.61 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[FLNB]] | -0.60 | -0.52 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXB8]] | B | HOXB8 activity raises HOXB7's level | lines that do not express HOXB8 (19) vs lines expressing it (31) | 2.38× lower at baseline in the lines without HOXB8 | 0.029 | ⚠ within organs, on part of the lines; also absent: FAM83F, LINC02086, ZBTB7C |
| [[TOP2A]] | B | TOP2A activity lowers HOXB7's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CMIP]] | B | HOXB7 activity lowers CMIP's level | lines that do not express HOXB7 (7) vs lines expressing it (43) | 1.33× higher at baseline in the lines without HOXB7 | 0.050 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.821). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (0.6, 24.5); signed map (26.2, -15.1). **Vector** length 73.2, 17.2% of its response variance represented; |z| ≥ 3 in 738 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +13.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +3.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.7 | +3.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +2.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.0 | +1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +1.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.2 | -9.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.8 | -11.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.7 | -10.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | -2.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -3.9 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -0.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | homeobox B7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:48,607,232-48,633,572 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX2, HOX2C |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Matched by | ensembl_id |

**Function**, from UniProt [P09629](https://www.uniprot.org/uniprotkb/P09629) (Homeobox protein Hox-B7):

> Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis.

**Summary**, from NCBI Gene [3217](https://www.ncbi.nlm.nih.gov/gene/3217):

> This gene is a member of the Antp homeobox family and encodes a protein with a homeobox DNA-binding domain. It is included in a cluster of homeobox B genes located on chromosome 17. The encoded nuclear protein functions as a sequence-specific transcription factor that is involved in cell proliferation and differentiation. Increased expression of this gene is associated with some cases of melanoma and ovarian carcinoma. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5118](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5118) · Entrez [3217](https://www.ncbi.nlm.nih.gov/gene/3217) · UniProt [P09629](https://www.uniprot.org/uniprotkb/P09629) · Ensembl [ENSG00000260027](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000260027)

## Data

Gene col 15256: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15256); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15256, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15256]; `tensor/DDL_lfc|DDL_z.npy` [15256]; `embed/gene_vectors.npy` [15256]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15256 or target_col == 15256). Every well: [[HOXB7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXB7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
