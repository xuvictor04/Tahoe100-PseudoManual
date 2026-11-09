---
symbol: "GPALPP1"
type: "gene"
col: 5420
ensembl_id: "ENSG00000133114"
name: "GPALPP motifs containing 1"
location: "13q14.12"
module: 15
arm: "+"
pooled_cpm: 33.78
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# GPALPP1

*GPALPP motifs containing 1* — 13q14.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.53× (z +14.3, q 1e-43, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.751× (z -9.7, q 2e-19, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS13B-DT]] (+0.74, fdr 7e-06), [[C8orf44-SGK3]] (+0.73, fdr 7e-06), [[PAAF1]] (+0.71, fdr 7e-06); moves opposite to [[GPRIN1]] (-0.58, fdr 3e-05), [[GTDC1]] (-0.57, fdr 5e-05), [[LMCD1]] (-0.56, fdr 2e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[N4BP2L2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5420.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +14.3 | 1e-43 | 37/48 (Panc 03.27, SW1417, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +11.5 | 3e-28 | 33/46 (NCI-H23, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +11.1 | 3e-26 | 36/48 (HT-29, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +10.6 | 5e-24 | 33/47 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +9.9 | 3e-21 | 34/48 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +9.7 | 5e-20 | 25/37 (LS 180, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +9.2 | 2e-18 | 35/48 (Panc 03.27, HT-29, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +8.7 | 2e-16 | 30/43 (A498, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +7.1 | 9e-11 | 30/48 (NCI-H23, RKO, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.28×** | +5.8 | 4e-07 | 21/48 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +5.5 | 2e-06 | 20/48 (SW1417, A-427, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +5.2 | 9e-06 | 19/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.22×** | +4.7 | 1e-04 | 19/48 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.21×** | +4.5 | 2e-04 | 18/47 (NCI-H1573, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +4.4 | 3e-04 | 14/48 (HEC-1-A, RKO, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.16× | +3.5 | 0.015 | 6/48 (LS 180, KATO III, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.16× | +3.4 | 0.017 | 12/47 (NCI-H23, NCI-H1792, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.14× | +3.1 | 0.050 | 4/48 (LOX-IMVI, SW1417, …) | rises with dose |  |
| [[Carbamazepine (drug)]] 0.5 µM |  | 1.13× | +2.9 | 0.081 | 8/48 (SW480, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5420.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.751×** | -9.7 | 2e-19 | 38/48 (SW480, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.733×** | -7.5 | 3e-11 | 26/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.686×** | -4.7 | 4e-04 | 22/48 (RKO, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.873× | -4.6 | 5e-04 | 8/48 (J82, SHP-77, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5420. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 45.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.245× (z -9.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 28.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.120× (z -11.6) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 40.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +10.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 45.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +8.7) | — |
| [[KATO III (line)]] | alt | 48.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 34.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.14× (z +10.3) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 34.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.00× (z +10.2) ⚠ toxic | — |
| [[NCI-H23 (line)]] | alt | 38.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +10.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 49.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +10.3) | — |
| [[PANC-1 (line)]] | alt | 28.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +9.2) | — |
| [[RKO (line)]] | wt | 33.2 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.62× (z +10.0) ⚠ toxic | — |
| [[SHP-77 (line)]] | alt | 28.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.56× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 24.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +10.2) | — |
| [[A-172 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 62.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5420), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS13B-DT]] | +0.74 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[C8orf44-SGK3]] | +0.73 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[PAAF1]] | +0.71 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[MCCC1]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[PNISR-AS1]] | +0.67 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[MAIP1]] | +0.66 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[ZBTB8OS]] | +0.66 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[URM1]] | +0.66 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[CAB39L]] | +0.65 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[TSTD3]] | +0.65 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ZNF460-AS1]] | +0.64 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[MED24]] | +0.63 | +0.45 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRIN1]] | -0.58 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[GTDC1]] | -0.57 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[LMCD1]] | -0.56 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[EHD4]] | -0.56 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[DUSP2]] | -0.56 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[FLNB]] | -0.56 | -0.52 / -0.37 | both halves | 9e-05 |  |
| [[SIPA1]] | -0.56 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[ADRB2]] | -0.56 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[LINC00540]] | -0.56 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[SCN1B]] | -0.55 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[EML4]] | -0.54 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[DUSP5]] | -0.54 | -0.47 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GPALPP1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[THBS4]] | B | THBS4 activity raises GPALPP1's level | lines that do not express THBS4 (6) vs lines expressing it (44) | 1.37× lower at baseline in the lines without THBS4 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[N4BP2L2]] | C | GPALPP1's natural level strengthens N4BP2L2's drug response | GPALPP1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.68, reverse -0.07; direction clear | 0.015 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.667). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-5.9, 24.0); signed map (-1.0, -3.7). **Vector** length 87.9, 17.7% of its response variance represented; |z| ≥ 3 in 902 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.8 | +9.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +11.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.8 | +5.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +9.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +7.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | +4.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.2 | +3.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.0 | -9.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.9 | -7.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.2 | -1.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -3.4 | +4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | +2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -4.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | +1.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -1.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | GPALPP motifs containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.12 — chr13:44,989,529-45,037,669 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA245H20.2, AD029, LSR7; previously KIAA1704 |
| Matched by | ensembl_id |

UniProt [Q8IXQ4](https://www.uniprot.org/uniprotkb/Q8IXQ4) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:20298](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20298) · Entrez [55425](https://www.ncbi.nlm.nih.gov/gene/55425) · UniProt [Q8IXQ4](https://www.uniprot.org/uniprotkb/Q8IXQ4) · Ensembl [ENSG00000133114](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133114)

## Data

Gene col 5420: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5420); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5420, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5420]; `tensor/DDL_lfc|DDL_z.npy` [5420]; `embed/gene_vectors.npy` [5420]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5420 or target_col == 5420). Every well: [[GPALPP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPALPP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
