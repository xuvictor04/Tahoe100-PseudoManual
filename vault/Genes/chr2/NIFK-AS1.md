---
symbol: "NIFK-AS1"
type: "gene"
col: 14106
ensembl_id: "ENSG00000236859"
name: "NIFK antisense RNA 1"
location: "2q14.3"
module: 15
arm: "+"
pooled_cpm: 20.83
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 15
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# NIFK-AS1

*NIFK antisense RNA 1* — 2q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.61× (z +15.6, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.499× (z -8.0, q 6e-13, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAI4]] (+0.78, fdr 7e-06), [[DICER1-AS1]] (+0.77, fdr 7e-06), [[ENTPD3-AS1]] (+0.77, fdr 7e-06); moves opposite to [[GPRIN1]] (-0.65, fdr 7e-05), [[APMAP]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14106.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.61×** | +15.6 | 0e+00 | 43/47 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +8.6 | 2e-15 | 32/46 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +7.4 | 3e-11 | 33/47 (SW480, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.67×** | +5.9 | 6e-07 | 35/47 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.1 | 5e-05 | 24/47 (SW1417, HOP62, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.29×** | +4.1 | 0.004 | 22/47 (SW480, HepG2/C3A, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.43×** | +4.1 | 0.004 | 23/47 (PANC-1, SNU-423, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +4.1 | 0.004 | 16/46 (SW480, NCI-H23, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.5 | 0.032 | 19/44 (SW1417, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.043 | 11/47 (LS 180, J82, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.043 | 13/47 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.35×** | +3.3 | 0.044 | 14/47 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.064 | 10/47 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.070 | 12/47 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.21×** | +3.1 | 0.077 | 16/47 (NCI-H460, J82, …) | all doses, flat | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14106.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.499×** | -8.0 | 6e-13 | 34/47 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.511×** | -7.7 | 3e-12 | 38/47 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.513×** | -7.6 | 5e-12 | 34/47 (PANC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.570×** | -6.5 | 1e-08 | 34/46 (PANC-1, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.600×** | -5.6 | 2e-06 | 27/45 (SHP-77, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.627×** | -5.4 | 8e-06 | 29/45 (PANC-1, NCI-H460, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.638×** | -5.1 | 2e-05 | 27/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.684×** | -4.1 | 0.003 | 26/47 (PANC-1, SW 1271, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.699×** | -4.1 | 0.003 | 23/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.645×** | -3.6 | 0.018 | 17/47 (NCI-H460, C-33 A, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.551×** | -3.6 | 0.018 | 20/45 (A-427, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.561×** | -3.5 | 0.024 | 16/47 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.744×** | -3.4 | 0.029 | 17/47 (AN3 CA, NCI-H2030, …) | rises with dose |  |
| [[Aprepitant (drug)]] 0.05 µM |  | **0.757×** | -3.2 | 0.055 | 15/47 (AN3 CA, NCI-H2030, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.600×** | -3.1 | 0.080 | 15/39 (PANC-1, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14106. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 27.9 | 1 | 12 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +15.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.193× (z -15.5) |
| [[SW480 (line)]] | alt | 24.5 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +11.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.339× (z -8.5) |
| [[AN3 CA (line)]] | alt | 19.9 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0602× (z -9.4) |
| [[HOP62 (line)]] | alt | 24.9 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.88× (z +10.8) | — |
| [[HS-578T (line)]] | alt | 11.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.82× (z +12.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 38.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +8.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.285× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 28.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 33.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 20.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +11.8) | — |
| [[A-172 (line)]] | wt | 19.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +9.2) | — |
| [[A549 (line)]] | wt | 15.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +8.6) | — |
| [[C32 (line)]] | wt | 15.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +8.8) | — |
| [[H4 (line)]] | wt | 38.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 40.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 28.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 14.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.94× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.110× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 12.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 21.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 13.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.68× (z +10.9) | — |
| [[NCI-H460 (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.210× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[RKO (line)]] | wt | 11.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.09× (z +11.2) | — |
| [[RPMI-7951 (line)]] | alt | 29.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.199× (z -9.8) ⚠ toxic |
| [[SW1417 (line)]] | alt | 13.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.74× (z +13.5) | — |
| [[A-427 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.08 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14106), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAI4]] | +0.78 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[DICER1-AS1]] | +0.77 | +0.73 / +0.62 | both halves | 7e-06 | same gene group |
| [[ENTPD3-AS1]] | +0.77 | +0.73 / +0.61 | both halves | 7e-06 | same gene group |
| [[ANKRD17-DT]] | +0.77 | +0.77 / +0.58 | both halves | 7e-06 |  |
| [[SPESP1]] | +0.75 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[CFAP43]] | +0.74 | +0.80 / +0.55 | both halves | 1e-05 |  |
| [[POLR1HASP]] | +0.73 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[CASS4]] | +0.73 | +0.74 / +0.51 | both halves | 1e-05 |  |
| [[DARS1-AS1]] | +0.73 | +0.64 / +0.63 | both halves | 7e-06 | same gene group |
| [[ASH1L]] | +0.73 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[DDX59-AS1]] | +0.72 | +0.67 / +0.65 | both halves | 7e-06 | same gene group |
| [[CHD1-DT]] | +0.72 | +0.72 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRIN1]] | -0.65 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[APMAP]] | -0.63 | -0.52 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NIFK-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FSD1]] | B | FSD1 activity raises NIFK-AS1's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 1.64× lower at baseline in the lines without FSD1 | 0.039 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[INHA]] | B | INHA activity raises NIFK-AS1's level | lines that do not express INHA (11) vs lines expressing it (39) | 1.70× lower at baseline in the lines without INHA | 0.045 | ⚠ within organs, on part of the lines; also absent: OBSL1, KCNK13 |
| [[MAP2K1]] | B | MAP2K1 activity lowers NIFK-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[CATSPER2P1]] | C | CATSPER2P1 activity raises NIFK-AS1's level | lines that do not express CATSPER2P1 (3) vs lines expressing it (47) | 1.99× lower at baseline in the lines without CATSPER2P1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FAM182B, SLFNL1-AS1, ENSG00000287400; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.679). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (3.0, 19.8); signed map (27.9, -7.5). **Vector** length 93.7, 23.2% of its response variance represented; |z| ≥ 3 in 982 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +15.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +8.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +7.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +0.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.1 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +4.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.1 | -1.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | -2.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -1.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.9 | -7.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -3.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.2 | -2.8 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | NIFK antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q14.3 — chr2:121,649,320-121,728,563 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [254128](https://www.ncbi.nlm.nih.gov/gene/254128):

> Predicted to be involved in RNA processing. Predicted to be located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27385](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27385) · Entrez [254128](https://www.ncbi.nlm.nih.gov/gene/254128) · Ensembl [ENSG00000236859](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236859)

## Data

Gene col 14106: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14106); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14106, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14106]; `tensor/DDL_lfc|DDL_z.npy` [14106]; `embed/gene_vectors.npy` [14106]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14106 or target_col == 14106). Every well: [[NIFK-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NIFK-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
