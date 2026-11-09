---
symbol: "GDPD5"
type: "gene"
col: 8173
ensembl_id: "ENSG00000158555"
name: "glycerophosphodiester phosphodiesterase domain containing 5"
location: "11q13.4-q13.5"
module: 34
arm: "+"
pooled_cpm: 10.41
n_lines_expressing: 48
n_dd_up: 17
n_dd_down: 13
n_dd_up_clean: 14
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 8
direction_downstream: 1
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# GDPD5

*glycerophosphodiester phosphodiesterase domain containing 5* — 11q13.4-q13.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.89× (z +18.7, q 0e+00, up in 42 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.624× (z -6.3, q 2e-07, down in 22 of 37 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.667× (z -5.6, q 7e-06, down in 15 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLC3]] (+0.69, fdr 1e-05), [[BAIAP3]] (+0.68, fdr 1e-05), [[FCHO1]] (+0.67, fdr 1e-05); moves opposite to [[TDRD3]] (-0.62, fdr 1e-05), [[PNISR-AS1]] (-0.58, fdr 1e-04), [[QRSL1]] (-0.57, fdr 9e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[MYO1D]] → it (grade B ⚠); 1 goes from it, the strongest it → [[TDRD3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8173.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.89×** | +18.7 | 0e+00 | 42/45 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **3.62×** | +17.7 | 0e+00 | 43/45 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.03×** | +15.2 | 0e+00 | 41/45 (HT-29, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.72×** | +13.7 | 1e-40 | 42/45 (HT-29, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.00×** | +13.5 | 2e-39 | 39/45 (LS 180, HT-29, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **2.07×** | +10.0 | 2e-21 | 30/41 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +8.5 | 2e-15 | 29/44 (BT-474, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.06×** | +8.0 | 6e-14 | 31/45 (SK-MEL-2, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +5.1 | 3e-05 | 17/40 (CFPAC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.35×** | +4.1 | 0.002 | 11/45 (A-172, SK-MEL-2, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.32×** | +3.6 | 0.015 | 10/44 (SW480, HEC-1-A, …) | top dose only |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.44×** | +3.6 | 0.016 | 2/44 (A-172, CFPAC-1) | rises with dose | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.59×** | +3.3 | 0.038 | 5/39 (SW480, NCI-H2347, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.039 | 6/45 (BT-474, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.55×** | +3.1 | 0.063 | 3/39 (NCI-H2347, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.091 | 9/43 (A-172, LoVo, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8173.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.624×** | -6.3 | 2e-07 | 22/37 (KATO III, AsPC-1, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.667×** | -5.6 | 7e-06 | 15/44 (A-172, H4, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.523×** | -4.7 | 6e-04 | 17/44 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.730×** | -4.3 | 0.002 | 17/46 (KATO III, H4, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.750×** | -4.0 | 0.008 | 15/44 (CFPAC-1, NCI-H2347, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.743×** | -3.9 | 0.008 | 19/42 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 5 µM |  | **0.761×** | -3.6 | 0.024 | 5/42 (NCI-H2030, A-172, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.774×** | -3.5 | 0.028 | 9/44 (A-172, A498, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.835× | -3.5 | 0.028 | 7/44 (Panc 03.27, RPMI-7951, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.779×** | -3.4 | 0.033 | 17/31 (SW480, J82, …) | inconsistent across doses | composition shift |
| [[Terfenadine (drug)]] 0.5 µM |  | **0.786×** | -3.3 | 0.046 | 8/44 (HCT15, AsPC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.780×** | -3.3 | 0.046 | 14/39 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.802×** | -3.0 | 0.099 | 11/43 (LOX-IMVI, SW 900, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.803×** | -3.0 | 0.099 | 14/44 (H4, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8173. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 42.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +8.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -9.2) |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 2 | — | [[Neratinib (drug)]] 0.05 µM 0.0592× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 20.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -12.6) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 21.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0728× (z -10.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0957× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 15.2 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -12.9) |
| [[HT-29 (line)]] | alt | 3.49 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 7.08× (z +8.8) | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM 0.0530× (z -9.4) |
| [[KATO III (line)]] | alt | 14.3 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 19.0 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 18.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 7.91 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.11× (z +8.5) | — |
| [[A549 (line)]] | wt | 7.03 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0950× (z -8.9) |
| [[HOP62 (line)]] | alt | 9.62 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -10.1) |
| [[J82 (line)]] | alt | 6.84 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0679× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LOX-IMVI (line)]] | wt | 5.08 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0871× (z -9.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LS 180 (line)]] | wt | 5.39 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.60× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 5.81 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0950× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW 900 (line)]] | alt | 6.92 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0879× (z -8.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A-427 (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8173), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLC3]] | +0.69 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[BAIAP3]] | +0.68 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[FCHO1]] | +0.67 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[KRT15]] | +0.67 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[RAC2]] | +0.66 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[PIK3CD]] | +0.66 | +0.60 / +0.60 | both halves | 7e-06 | pathway: PI Metabolism |
| [[GIPR]] | +0.64 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[SEMA7A]] | +0.64 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[ARVCF]] | +0.64 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[ESAM]] | +0.63 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[DLGAP4]] | +0.63 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[EPN2]] | +0.62 | +0.57 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TDRD3]] | -0.62 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[PNISR-AS1]] | -0.58 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[QRSL1]] | -0.57 | -0.51 / -0.37 | both halves | 9e-05 |  |
| [[EFCAB2]] | -0.57 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[NAF1]] | -0.57 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[ANGEL2]] | -0.57 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[ARID1B]] | -0.57 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[PUS10]] | -0.56 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[SUPV3L1]] | -0.56 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[NNT]] | -0.56 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[GAS2]] | -0.56 | -0.40 / -0.25 | both halves | 4e-04 |  |
| [[KIAA0825]] | -0.55 | -0.43 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO1D]] | B | MYO1D activity raises GDPD5's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 1.20× lower at baseline in the lines without MYO1D | 0.022 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[PGBD5]] | B | PGBD5 activity raises GDPD5's level | lines that do not express PGBD5 (28) vs lines expressing it (22) | 1.72× lower at baseline in the lines without PGBD5 | 0.046 | ⚠ within organs, on part of the lines; also absent: TMEM163, LRRN1, ELAVL2 |
| [[TMEM40]] | B | TMEM40 activity raises GDPD5's level | lines that do not express TMEM40 (24) vs lines expressing it (26) | 1.57× lower at baseline in the lines without TMEM40 | 0.048 | ⚠ within organs, on part of the lines; also absent: LRG1, LRRN1, WNT7A; maybe low, not absent |
| [[SEMA3B]] | B | SEMA3B activity raises GDPD5's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 1.65× lower at baseline in the lines without SEMA3B | 0.069 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[WNT7A]] | B | WNT7A activity raises GDPD5's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 1.29× lower at baseline in the lines without WNT7A | 0.080 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6 |
| [[ZNF385A]] | B | ZNF385A activity raises GDPD5's level | lines that do not express ZNF385A (7) vs lines expressing it (43) | 1.78× lower at baseline in the lines without ZNF385A | 0.092 | ⚠ within organs, on part of the lines; also absent: PDP1, AGBL2; maybe low, not absent |
| [[TINAGL1]] | B | TINAGL1 activity raises GDPD5's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 1.36× lower at baseline in the lines without TINAGL1 | 0.094 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[SPNS2]] | B | SPNS2 activity raises GDPD5's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 1.39× lower at baseline in the lines without SPNS2 | 0.096 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TDRD3]] | C | GDPD5's natural level weakens TDRD3's drug response | GDPD5's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.63, reverse +0.27; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.688). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.9, -0.6); signed map (-1.6, 45.4). **Vector** length 81.5, 15.4% of its response variance represented; |z| ≥ 3 in 1,233 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +13.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +8.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.5 | +13.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.2 | +17.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.1 | +15.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +8.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +3.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.8 | +0.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -3.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.6 | -6.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.6 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -0.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.8 | -2.0 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | glycerophosphodiester phosphodiesterase domain containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4-q13.5 — chr11:75,434,640-75,525,941 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PP1665, GDE2 |
| Reactome | 4 pathways, smallest: Glycerophospholipid catabolism; PI Metabolism; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WTR4](https://www.uniprot.org/uniprotkb/Q8WTR4) (Glycerophosphodiester phosphodiesterase 2):

> Ecto-phospholipase that cleaves the phosphodiester bond in the glycosylphosphatidylinositol (GPI) anchor of various proteins, releasing them from the plasma membrane into the extracellular space. Cleaves the GPI-anchor of glypican-6/GPC6, thereby positively regulating neuron differentiation in a cell-autonomous manner. May also hydrolyze the GPI-anchor of glypican-3/GPC3. Cleaves the GPI-anchor of the serine protease inhibitor RECK, leading to its inactivation. RECK inactivation inhibits NOTCH …

**Summary**, from NCBI Gene [81544](https://www.ncbi.nlm.nih.gov/gene/81544):

> Predicted to enable glycerophosphodiester phosphodiesterase activity and glycerophospholipase activity. Predicted to be involved in several processes, including negative regulation of Notch signaling pathway; negative regulation of amyloid precursor protein biosynthetic process; and positive regulation of neuron differentiation. Predicted to act upstream of or within neuron differentiation and regulation of timing of cell differentiation. Predicted to be located in axon; neuronal cell body; and …

**Accessions** — [HGNC:28804](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28804) · Entrez [81544](https://www.ncbi.nlm.nih.gov/gene/81544) · UniProt [Q8WTR4](https://www.uniprot.org/uniprotkb/Q8WTR4) · Ensembl [ENSG00000158555](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158555)

## Data

Gene col 8173: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8173); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8173, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8173]; `tensor/DDL_lfc|DDL_z.npy` [8173]; `embed/gene_vectors.npy` [8173]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8173 or target_col == 8173). Every well: [[GDPD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GDPD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
