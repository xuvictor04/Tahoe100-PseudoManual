---
symbol: "SYDE2"
type: "gene"
col: 1778
ensembl_id: "ENSG00000097096"
name: "synapse defective Rho GTPase homolog 2"
location: "1p22.3"
module: 123
arm: "+"
pooled_cpm: 20.87
n_lines_expressing: 46
n_dd_up: 26
n_dd_down: 7
n_dd_up_clean: 21
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# SYDE2

*synapse defective Rho GTPase homolog 2* — 1p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.09× (z +39.8, q 0e+00, up in 39 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 0.727× (z -6.2, q 2e-07, down in 21 of 43 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AJUBA]] (+0.69, fdr 7e-06), [[BMI1]] (+0.61, fdr 3e-05), [[AMOTL2]] (+0.59, fdr 1e-05); moves opposite to [[UFD1]] (-0.55, fdr 3e-05), [[SAP130]] (-0.54, fdr 3e-05), [[SAMD4B]] (-0.54, fdr 3e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[NFYB]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1778.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.09×** | +39.8 | 0e+00 | 39/41 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.81×** | +26.7 | 0e+00 | 39/42 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.14×** | +22.0 | 0e+00 | 38/42 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.36×** | +17.2 | 0e+00 | 38/43 (C-33 A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.99×** | +13.7 | 1e-40 | 34/43 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +12.4 | 2e-33 | 28/43 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +10.9 | 2e-25 | 30/42 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.63×** | +9.8 | 9e-21 | 26/43 (C-33 A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.63×** | +9.7 | 1e-20 | 26/43 (A-427, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +9.1 | 4e-18 | 28/43 (C-33 A, A-427, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.58×** | +9.1 | 4e-18 | 25/43 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +8.9 | 4e-17 | 22/42 (J82, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +8.0 | 4e-14 | 24/39 (J82, C32, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +6.8 | 5e-10 | 18/43 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +6.1 | 5e-08 | 15/44 (PANC-1, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +6.0 | 5e-08 | 17/43 (J82, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.78×** | +6.0 | 6e-08 | 16/43 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.75×** | +5.9 | 1e-07 | 18/41 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1778.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.727×** | -6.2 | 2e-07 | 21/43 (C-33 A, RKO, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.737×** | -6.2 | 2e-07 | 18/43 (BT-474, HT-29, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.812×** | -4.2 | 0.005 | 15/43 (A-427, NCI-H23, …) | rises with dose | low cells (technical?) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.823×** | -3.9 | 0.011 | 15/41 (C-33 A, NCI-H460, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.780×** | -3.6 | 0.039 | 13/41 (AN3 CA, A-172, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.715×** | -3.5 | 0.040 | 6/37 (SW480, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.795×** | -3.3 | 0.076 | 10/40 (PANC-1, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Furosemide (drug)]] 5 µM |  | 0.892× | -3.3 | 0.076 | 9/44 (SW 1088, A549, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1778. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 59.0 | 9 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 37.6 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +17.7) | — |
| [[NCI-H460 (line)]] | wt | 15.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +26.4) | — |
| [[HEC-1-A (line)]] | alt | 34.9 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +13.8) | [[Lonafarnib (drug)]] 5 µM 0.128× (z -10.6) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 63.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.30× (z +27.1) | — |
| [[A-172 (line)]] | wt | 10.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +12.9) | — |
| [[LoVo (line)]] | wt | 20.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.176× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 42.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.0477× (z -24.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 14.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +14.6) | — |
| [[NCI-H23 (line)]] | alt | 30.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.41× (z +23.5) | — |
| [[RKO (line)]] | wt | 71.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[SK-MEL-2 (line)]] | alt | 22.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.85× (z +17.6) | — |
| [[SW480 (line)]] | alt | 11.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +15.1) | — |
| [[A498 (line)]] | wt | 16.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +15.2) | — |
| [[A549 (line)]] | wt | 12.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.54× (z +16.2) | — |
| [[CFPAC-1 (line)]] | alt | 8.78 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +15.9) | — |
| [[HT-29 (line)]] | alt | 19.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +16.4) | — |
| [[J82 (line)]] | alt | 28.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +14.6) | — |
| [[NCI-H1573 (line)]] | alt | 8.85 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.28× (z +16.0) | — |
| [[NCI-H2030 (line)]] | alt | 32.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +16.6) | — |
| [[NCI-H2347 (line)]] | alt | 14.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +11.9) | — |
| [[Panc 03.27 (line)]] | alt | 16.8 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.78× (z +9.3) | — |
| [[SNU-1 (line)]] | wt | 18.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +10.0) | [[Thymol (drug)]] 0.5 µM 0.116× (z -9.7) |
| [[SW 900 (line)]] | alt | 11.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +12.0) | [[XRK3F2 (drug)]] 0.5 µM 0.0770× (z -8.7) |
| [[SW1417 (line)]] | alt | 26.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +14.8) | — |
| [[C32 (line)]] | wt | 7.30 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0492× (z -12.0) |
| [[HCT15 (line)]] | alt | 19.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +9.5) | — |
| [[HepG2_C3A (line)]] | wt | 14.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +8.7) | — |
| [[KATO III (line)]] | alt | 15.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.82× (z +17.3) | — |
| [[RPMI-7951 (line)]] | alt | 5.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.75× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 8.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.45× (z +12.7) | — |
| [[AN3 CA (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.18 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.99 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 94.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1778), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AJUBA]] | +0.69 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[BMI1]] | +0.61 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[AMOTL2]] | +0.59 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[LGALSL-DT]] | +0.59 | +0.62 / +0.34 | both halves | 1e-04 |  |
| [[NFYB]] | +0.58 | +0.69 / +0.36 | both halves | 9e-05 |  |
| [[REST]] | +0.57 | +0.65 / +0.41 | both halves | 4e-05 |  |
| [[DNAAF2]] | +0.57 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[SFTA1P]] | +0.56 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[LINC01186]] | +0.56 | +0.56 / +0.37 | both halves | 8e-05 |  |
| [[LATS2]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[ZFP30]] | +0.56 | +0.62 / +0.33 | both halves | 1e-04 |  |
| [[MARVELD2]] | +0.55 | +0.57 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UFD1]] | -0.55 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[SAP130]] | -0.54 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[SAMD4B]] | -0.54 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[ZCCHC17]] | -0.52 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[PSMD13]] | -0.52 | -0.58 / -0.39 | both halves | 6e-05 |  |
| [[ASB16-AS1]] | -0.52 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[CTNNBL1]] | -0.51 | -0.56 / -0.24 | both halves | 4e-04 |  |
| [[VRK3]] | -0.51 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[YIPF1]] | -0.51 | -0.55 / -0.28 | both halves | 3e-04 |  |
| [[SNX1]] | -0.51 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[MLF2]] | -0.50 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[ADAM17]] | -0.50 | -0.56 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFYB]] | C | SYDE2 activity raises NFYB's level | lines that do not express SYDE2 (4) vs lines expressing it (46) | 1.59× lower at baseline in the lines without SYDE2 | 0.058 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MATN2, TLCD5; maybe low, not absent |

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.434). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.6, 12.5); signed map (27.8, -33.2). **Vector** length 91.9, 20.1% of its response variance represented; |z| ≥ 3 in 1,126 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.5 | +26.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +39.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.8 | +22.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.1 | +13.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +12.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.5 | +4.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.3 | -6.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -1.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.0 | -0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -0.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -4.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.0 | -1.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -2.8 |
|  | [[Docetaxel (drug)]] 5 µM |  | -1.4 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | synapse defective Rho GTPase homolog 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.3 — chr1:85,156,889-85,201,724 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13815 |
| Gene groups (HGNC) | C2 domain containing |
| Reactome | 4 pathways, smallest: RAC1 GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VT97](https://www.uniprot.org/uniprotkb/Q5VT97) (Rho GTPase-activating protein SYDE2):

> GTPase activator for the Rho-type GTPases by converting them to an inactive GDP-bound state.

**Summary**, from NCBI Gene [84144](https://www.ncbi.nlm.nih.gov/gene/84144):

> Predicted to enable GTPase activator activity. Acts upstream of or within cell migration. Predicted to be located in cytosol. Predicted to be active in synaptic membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25841](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25841) · Entrez [84144](https://www.ncbi.nlm.nih.gov/gene/84144) · UniProt [Q5VT97](https://www.uniprot.org/uniprotkb/Q5VT97) · Ensembl [ENSG00000097096](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000097096)

## Data

Gene col 1778: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1778); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1778, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1778]; `tensor/DDL_lfc|DDL_z.npy` [1778]; `embed/gene_vectors.npy` [1778]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1778 or target_col == 1778). Every well: [[SYDE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYDE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
