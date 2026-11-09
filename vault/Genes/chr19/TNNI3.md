---
symbol: "TNNI3"
type: "gene"
col: 5012
ensembl_id: "ENSG00000129991"
name: "troponin I3, cardiac type"
location: "19q13.42"
module: 85
arm: "+"
pooled_cpm: 2.67
n_lines_expressing: 39
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 6
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# TNNI3

*troponin I3, cardiac type* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.93× (z +11.0, q 3e-25, up in 32 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.0853×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAAF3]] (+0.74, fdr 7e-06, ⚠ same locus), [[TSTD1]] (+0.74, fdr 7e-06), [[CCDC88B]] (+0.72, fdr 7e-06), [[CARHSP1]] (+0.70, fdr 3e-05); moves opposite to [[ZMYND11]] (-0.71, fdr 3e-05), [[DNAJC11]] (-0.69, fdr 8e-06), [[PSME3IP1]] (-0.69, fdr 1e-05).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TNNT1]] → it (grade B ⚠); 6 go from it, the strongest it → [[DNAAF3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5012.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.93×** | +11.0 | 3e-25 | 32/33 (KATO III, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.78×** | +9.5 | 7e-19 | 27/30 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.00×** | +8.5 | 3e-15 | 27/30 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.59×** | +8.3 | 2e-14 | 25/32 (PANC-1, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.90×** | +8.0 | 9e-14 | 3/4 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.80×** | +6.3 | 2e-08 | 7/11 (SW480, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.56×** | +5.8 | 6e-07 | 21/32 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.51×** | +5.7 | 1e-06 | 20/28 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +5.5 | 3e-06 | 7/21 (A-172, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.39×** | +5.3 | 8e-06 | 11/21 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.28×** | +4.7 | 2e-04 | 2/4 (SW480, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.09×** | +4.5 | 3e-04 | 6/14 (NCI-H2030, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.43×** | +3.1 | 0.081 | 9/30 (NCI-H1573, KATO III, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.0 | 0.095 | 5/23 (PANC-1, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5012.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.0853×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.546× | -3.7 | 0.12 | 13/27 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | 0.576× | -3.3 | 0.28 | 16/29 (SK-MEL-2, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.607× | -3.1 | 0.36 | 8/33 (RKO, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5012. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 3.97 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0853× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.482 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.635 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.686 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.279 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.509 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.357 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.585 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.868 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.805 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.943 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.906 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.749 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.709 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.971 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.770 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.547 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.928 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5012), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF3]] | +0.74 | +0.67 / +0.62 | both halves | 7e-06 | STRING 432; ⚠ same locus (0.9 kb, same strand: neighbours can correlate without regulation) |
| [[TSTD1]] | +0.74 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[CCDC88B]] | +0.72 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[CARHSP1]] | +0.70 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[LMTK3]] | +0.70 | +0.69 / +0.46 | both halves | 2e-05 |  |
| [[PLEKHH3]] | +0.70 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[SLC27A1]] | +0.69 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[CFD]] | +0.68 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[AHDC1]] | +0.68 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[SLC17A7]] | +0.68 | +0.43 / +0.74 | both halves | 3e-05 |  |
| [[FCHO1]] | +0.68 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[TMEM256]] | +0.68 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[TSPAN33]] | +0.67 | +0.45 / +0.66 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND11]] | -0.71 | -0.45 / -0.75 | both halves | 3e-05 |  |
| [[DNAJC11]] | -0.69 | -0.60 / -0.58 | both halves | 8e-06 |  |
| [[PSME3IP1]] | -0.69 | -0.49 / -0.70 | both halves | 1e-05 |  |
| [[MCM3AP]] | -0.68 | -0.57 / -0.64 | both halves | 8e-06 |  |
| [[MAPKAPK5]] | -0.66 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[MTHFSD]] | -0.65 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[ZNF507]] | -0.65 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[PSME3]] | -0.64 | -0.48 / -0.74 | both halves | 2e-05 |  |
| [[ZXDB]] | -0.64 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.63 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[UTP20]] | -0.63 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[CPSF2]] | -0.63 | -0.49 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNNT1]] | B | TNNT1 activity raises TNNI3's level | lines that do not express TNNT1 (9) vs lines expressing it (41) | 1.68× lower at baseline in the lines without TNNT1 | 0.081 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, HDAC9; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAAF3]] | B | TNNI3 activity raises DNAAF3's level | lines that do not express TNNI3 (11) vs lines expressing it (39) | 1.67× lower at baseline in the lines without TNNI3 | 0.009 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CCT7]] | B | TNNI3 activity raises CCT7's level | lines that do not express TNNI3 (11) vs lines expressing it (39) | 1.28× lower at baseline in the lines without TNNI3 | 0.048 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FCHO1]] | B | TNNI3 activity raises FCHO1's level | lines that do not express TNNI3 (11) vs lines expressing it (39) | 1.61× lower at baseline in the lines without TNNI3 | 0.067 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[RNASEH1]] | B | TNNI3 activity raises RNASEH1's level | lines that do not express TNNI3 (11) vs lines expressing it (39) | 1.27× lower at baseline in the lines without TNNI3 | 0.068 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PSME3]] | B | TNNI3 activity raises PSME3's level | lines that do not express TNNI3 (11) vs lines expressing it (39) | 1.08× lower at baseline in the lines without TNNI3 | 0.087 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CHRNB1]] | B | TNNI3 activity raises CHRNB1's level | lines that do not express TNNI3 (11) vs lines expressing it (39) | 1.79× lower at baseline in the lines without TNNI3 | 0.092 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.723). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (7.3, -3.3); signed map (-29.7, 20.0). **Vector** length 50.5, 10.5% of its response variance represented; |z| ≥ 3 in 608 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +5.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.0 | +9.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.0 | +11.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.5 | +8.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +2.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.9 | -3.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.9 | -3.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -2.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | troponin I3, cardiac type |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:55,151,767-55,157,773 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TNNC1, CMH7, cTNI; previously CMD2A |
| Gene groups (HGNC) | Troponin complex subunits |
| Hallmark sets | SPERMATOGENESIS, KRAS_SIGNALING_DN |
| Reactome | 4 pathways, smallest: Striated Muscle Contraction; Ion homeostasis; Cardiac conduction |
| Matched by | ensembl_id |

**Function**, from UniProt [P19429](https://www.uniprot.org/uniprotkb/P19429) (Troponin I, cardiac muscle):

> Troponin I is the inhibitory subunit of troponin, the thin filament regulatory complex which confers calcium-sensitivity to striated muscle actomyosin ATPase activity.

**Summary**, from NCBI Gene [7137](https://www.ncbi.nlm.nih.gov/gene/7137):

> Troponin I (TnI), along with troponin T (TnT) and troponin C (TnC), is one of 3 subunits that form the troponin complex of the thin filaments of striated muscle. TnI is the inhibitory subunit; blocking actin-myosin interactions and thereby mediating striated muscle relaxation. The TnI subfamily contains three genes: TnI-skeletal-fast-twitch, TnI-skeletal-slow-twitch, and TnI-cardiac. This gene encodes the TnI-cardiac protein and is exclusively expressed in cardiac muscle tissues. Mutations in …

**Accessions** — [HGNC:11947](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11947) · Entrez [7137](https://www.ncbi.nlm.nih.gov/gene/7137) · UniProt [P19429](https://www.uniprot.org/uniprotkb/P19429) · Ensembl [ENSG00000129991](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129991)

## Data

Gene col 5012: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5012); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5012, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5012]; `tensor/DDL_lfc|DDL_z.npy` [5012]; `embed/gene_vectors.npy` [5012]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5012 or target_col == 5012). Every well: [[TNNI3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNNI3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
