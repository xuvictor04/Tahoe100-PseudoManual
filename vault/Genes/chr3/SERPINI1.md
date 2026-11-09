---
symbol: "SERPINI1"
type: "gene"
col: 8713
ensembl_id: "ENSG00000163536"
name: "serpin family I member 1"
location: "3q26.1"
module: 27
arm: "+"
pooled_cpm: 11.84
n_lines_expressing: 46
n_dd_up: 32
n_dd_down: 11
n_dd_up_clean: 27
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# SERPINI1

*serpin family I member 1* — 3q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 8.29× (z +30.4, q 0e+00, up in 42 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.628× (z -6.7, q 1e-08, down in 20 of 42 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPE]] (+0.58, fdr 1e-05), [[CALCA]] (+0.55, fdr 3e-04), [[RIMBP2]] (+0.53, fdr 4e-05); moves opposite to [[MTOR]] (-0.53, fdr 3e-05), [[C1orf159]] (-0.47, fdr 7e-05), [[TMEM33]] (-0.43, fdr 2e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[FGF9]] → it (grade B ⚠); 1 goes from it, the strongest it → [[GTF2B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8713.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **8.29×** | +30.4 | 0e+00 | 42/43 (A498, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **7.88×** | +29.7 | 0e+00 | 41/42 (A498, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **6.35×** | +26.6 | 0e+00 | 42/43 (SK-MEL-2, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.45×** | +25.2 | 0e+00 | 37/41 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.59×** | +18.4 | 0e+00 | 38/43 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.20×** | +16.0 | 0e+00 | 38/44 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.05×** | +14.6 | 0e+00 | 25/40 (CFPAC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.85×** | +14.5 | 1e-45 | 32/37 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.65×** | +13.5 | 2e-39 | 25/32 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.59×** | +13.2 | 8e-38 | 30/37 (Panc 03.27, A-172, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.87×** | +12.7 | 2e-35 | 32/44 (NCI-H2347, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.36×** | +11.9 | 1e-30 | 8/15 (HT-29, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **3.99×** | +10.4 | 9e-24 | 32/43 (SK-MEL-2, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.89×** | +9.1 | 3e-18 | 28/43 (NCI-H2347, PANC-1, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.01×** | +8.4 | 2e-15 | 21/43 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.77×** | +8.2 | 6e-15 | 21/39 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +6.8 | 3e-10 | 17/44 (HEC-1-A, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8713.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.628×** | -6.7 | 1e-08 | 20/42 (HCT15, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.681×** | -5.5 | 8e-06 | 17/43 (NCI-H1573, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.743×** | -4.3 | 0.003 | 15/43 (SHP-77, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.820×** | -4.1 | 0.006 | 12/44 (SHP-77, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.756×** | -4.0 | 0.006 | 18/40 (SHP-77, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.761×** | -3.9 | 0.007 | 8/43 (SW480, SHP-77, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.594×** | -3.9 | 0.007 | 7/41 (SW480, HCT15, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.766×** | -3.8 | 0.009 | 6/42 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.771×** | -3.7 | 0.011 | 11/41 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.768×** | -3.6 | 0.021 | 10/42 (A-172, C-33 A, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.789×** | -3.4 | 0.033 | 9/42 (SW480, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Rapamycin (drug)]] 5 µM |  | 0.860× | -3.1 | 0.098 | 8/44 (RKO, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8713. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 21.3 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 5.68× (z +12.2) | — |
| [[SHP-77 (line)]] | alt | 93.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0909× (z -25.2) |
| [[SW480 (line)]] | alt | 58.4 | 0 | 6 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.174× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 9.41 | 4 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 8.10× (z +11.0) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0467× (z -16.1) |
| [[SK-MEL-2 (line)]] | alt | 14.1 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 14.9× (z +13.6) | — |
| [[A-172 (line)]] | wt | 4.09 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 18.1× (z +10.2) | [[Daptomycin (drug)]] 0.5 µM 0.0537× (z -9.6) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 4.09 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 10.6× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 6.71 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.35× (z +9.2) | — |
| [[NCI-H2347 (line)]] | alt | 14.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.40× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 6.23 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 10.3× (z +12.6) | — |
| [[SW1417 (line)]] | alt | 16.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.54× (z +11.3) | — |
| [[A-427 (line)]] | wt | 19.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.99× (z +13.1) | — |
| [[A498 (line)]] | wt | 4.39 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 25.0× (z +14.6) | — |
| [[KATO III (line)]] | alt | 14.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.08× (z +10.8) | — |
| [[LOX-IMVI (line)]] | wt | 7.02 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.01× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 12.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.03× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.14 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 6.05 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 9.59× (z +9.6) | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.120× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 10.3 | 2 | 0 | [[Selinexor (drug)]] 5 µM 3.37× (z +9.0) | — |
| [[LoVo (line)]] | wt | 3.86 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 11.7× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 15.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 9.54 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 9.20× (z +9.6) | — |
| [[C32 (line)]] | wt | 6.51 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 13.3× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 5.29 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0625× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 13.1 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0693× (z -9.5) |
| [[RKO (line)]] | wt | 4.36 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 5 µM 0.0426× (z -9.0) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8713), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPE]] | +0.58 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[CALCA]] | +0.55 | +0.53 / +0.29 | both halves | 3e-04 |  |
| [[RIMBP2]] | +0.53 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[PCSK1]] | +0.50 | +0.55 / +0.33 | both halves | 1e-04 |  |
| [[MYLIP]] | +0.50 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[PWWP3B]] | +0.50 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[TENT5C]] | +0.50 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[ACADSB]] | +0.49 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[VASN]] | +0.48 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[ARG2]] | +0.48 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[WDR47]] | +0.48 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[PROX1]] | +0.48 | +0.50 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTOR]] | -0.53 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[C1orf159]] | -0.47 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[TMEM33]] | -0.43 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[GFM1]] | -0.43 | -0.29 / -0.36 | both halves | 2e-04 |  |
| [[L3MBTL2]] | -0.43 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[LRRK1]] | -0.42 | -0.30 / -0.57 | both halves | 2e-04 |  |
| [[ACSF3]] | -0.42 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[CNDP2]] | -0.42 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[PIGQ]] | -0.42 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[EMC8]] | -0.42 | -0.28 / -0.41 | both halves | 3e-04 |  |
| [[MFSD14CP-1]] | -0.41 | -0.29 / -0.40 | both halves | 2e-04 |  |
| [[RASAL2]] | -0.41 | -0.22 / -0.48 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGF9]] | B | FGF9 activity raises SERPINI1's level | lines that do not express FGF9 (31) vs lines expressing it (19) | 2.14× lower at baseline in the lines without FGF9 | 0.012 | ⚠ within organs, on part of the lines; also absent: VWA2, LINC02253, PRR15L |
| [[TOP2A]] | B | TOP2A activity lowers SERPINI1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EPHB3]] | B | EPHB3 activity raises SERPINI1's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 2.01× lower at baseline in the lines without EPHB3 | 0.062 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| [[MPZL3]] | B | MPZL3 activity raises SERPINI1's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.60× lower at baseline in the lines without MPZL3 | 0.088 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GTF2B]] | C | SERPINI1 activity raises GTF2B's level | lines that do not express SERPINI1 (4) vs lines expressing it (46) | 1.31× lower at baseline in the lines without SERPINI1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.313). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.1, 39.7); signed map (46.1, 36.3). **Vector** length 69.4, 12.7% of its response variance represented; |z| ≥ 3 in 1,196 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +16.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.1 | +12.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +8.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +13.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +25.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +6.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +9.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +3.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.6 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -6.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | +0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.8 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | serpin family I member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.1 — chr3:167,735,243-167,825,569 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PI12 |
| Gene groups (HGNC) | Serpin peptidase inhibitors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99574](https://www.uniprot.org/uniprotkb/Q99574) (Neuroserpin):

> Serine protease inhibitor that inhibits plasminogen activators and plasmin but not thrombin. May be involved in the formation or reorganization of synaptic connections as well as for synaptic plasticity in the adult nervous system. May protect neurons from cell damage by tissue-type plasminogen activator (Probable).

**Summary**, from NCBI Gene [5274](https://www.ncbi.nlm.nih.gov/gene/5274):

> This gene encodes a member of the serpin superfamily of serine proteinase inhibitors. The protein is primarily secreted by axons in the brain, and preferentially reacts with and inhibits tissue-type plasminogen activator. It is thought to play a role in the regulation of axonal growth and the development of synaptic plasticity. Mutations in this gene result in familial encephalopathy with neuroserpin inclusion bodies (FENIB), which is a dominantly inherited form of familial encephalopathy and …

**Accessions** — [HGNC:8943](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8943) · Entrez [5274](https://www.ncbi.nlm.nih.gov/gene/5274) · UniProt [Q99574](https://www.uniprot.org/uniprotkb/Q99574) · Ensembl [ENSG00000163536](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163536)

## Data

Gene col 8713: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8713); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8713, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8713]; `tensor/DDL_lfc|DDL_z.npy` [8713]; `embed/gene_vectors.npy` [8713]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8713 or target_col == 8713). Every well: [[SERPINI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERPINI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
