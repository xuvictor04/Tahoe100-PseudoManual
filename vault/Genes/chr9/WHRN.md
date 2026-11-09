---
symbol: "WHRN"
type: "gene"
col: 1745
ensembl_id: "ENSG00000095397"
name: "whirlin"
location: "9q32"
module: 161
arm: "+"
pooled_cpm: 35.83
n_lines_expressing: 46
n_dd_up: 10
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 9
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# WHRN

*whirlin* — 9q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.89× (z +13.6, q 3e-39, up in 43 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.770× (z -4.8, q 1e-03, down in 26 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFAP210]] (+0.53, fdr 1e-05), [[MAPRE2]] (+0.52, fdr 3e-05), [[IDS]] (+0.51, fdr 3e-05); moves opposite to [[SCO1]] (-0.52, fdr 4e-05), [[CIAPIN1]] (-0.50, fdr 3e-05), [[RRP36]] (-0.49, fdr 4e-05).
> It is in [[Module 161]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 9 go from it, the strongest it → [[DEDD2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1745.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.89×** | +13.6 | 3e-39 | 43/44 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.31×** | +10.8 | 1e-24 | 39/44 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.25×** | +10.3 | 8e-23 | 41/44 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +7.3 | 3e-11 | 33/44 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +6.7 | 3e-09 | 25/43 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.2 | 2e-05 | 22/43 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.01×** | +4.7 | 2e-04 | 26/44 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.012 | 19/44 (A-172, A549, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.39×** | +3.5 | 0.026 | 18/44 (A498, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.061 | 15/43 (SK-MEL-2, NCI-H1573, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1745.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.770×** | -4.8 | 1e-03 | 26/44 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.737×** | -3.9 | 0.022 | 19/44 (PANC-1, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **0.660×** | -3.8 | 0.024 | 22/44 (H4, Hs 766T, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.755×** | -3.6 | 0.029 | 22/43 (RKO, LoVo, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.756×** | -3.6 | 0.029 | 20/44 (Hs 766T, RPMI-7951, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.757×** | -3.6 | 0.029 | 21/44 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.759×** | -3.6 | 0.030 | 19/43 (Hs 766T, SNU-423, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.742×** | -3.5 | 0.037 | 18/44 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.762×** | -3.4 | 0.047 | 17/34 (SHP-77, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.779×** | -3.2 | 0.071 | 18/43 (NCI-H1573, SNU-423, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change | **0.787×** | -3.1 | 0.099 | 22/42 (Panc 03.27, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[vincristine (drug)]] 0.05 µM |  | 0.756× | -3.0 | 0.12 | 15/44 (A-427, LS 180, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1745. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 41.0 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +13.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.46× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -12.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 16.4 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.27× (z +11.8) | — |
| [[NCI-H460 (line)]] | wt | 69.7 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.371× (z -9.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 18.2 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.25× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.0889× (z -13.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 51.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +12.6) | — |
| [[C32 (line)]] | wt | 46.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +12.8) | — |
| [[NCI-H1573 (line)]] | alt | 41.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.289× (z -8.5) |
| [[SNU-423 (line)]] | alt | 41.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.95× (z +10.0) | — |
| [[A549 (line)]] | wt | 22.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.80× (z +13.1) | — |
| [[AsPC-1 (line)]] | alt | 27.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.53× (z +8.8) | — |
| [[H4 (line)]] | wt | 31.8 | 0 | 1 | — | [[TAK-733 (drug)]] 5 µM 0.0350× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 35.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -8.7) |
| [[HOP62 (line)]] | alt | 22.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.85× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 55.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[NCI-H2347 (line)]] | alt | 11.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.38× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[PANC-1 (line)]] | alt | 24.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.11× (z +10.8) | — |
| [[RKO (line)]] | wt | 52.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +14.2) | — |
| [[SHP-77 (line)]] | alt | 75.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -15.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 58.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW480 (line)]] | alt | 32.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -14.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.14 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.69 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.83 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 83.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 84.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1745), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP210]] | +0.53 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[MAPRE2]] | +0.52 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[IDS]] | +0.51 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[TENT5C]] | +0.50 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[FOSB]] | +0.49 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[MLF1]] | +0.49 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[FAM102A]] | +0.48 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[DNAH7]] | +0.47 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[PLTP]] | +0.47 | +0.34 / +0.47 | both halves | 1e-04 |  |
| [[ZMIZ1]] | +0.47 | +0.36 / +0.44 | both halves | 9e-05 |  |
| [[PHF1]] | +0.47 | +0.36 / +0.44 | both halves | 1e-04 |  |
| [[TKT]] | +0.46 | +0.38 / +0.45 | both halves | 7e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCO1]] | -0.52 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[CIAPIN1]] | -0.50 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[RRP36]] | -0.49 | -0.50 / -0.40 | both halves | 4e-05 |  |
| [[ARMC8]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[MIOS]] | -0.46 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[LSM6]] | -0.46 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[MRPL58]] | -0.45 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[UMPS]] | -0.45 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[VPS54]] | -0.45 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[CNOT11]] | -0.45 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[KDM4D]] | -0.44 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[PYM1]] | -0.44 | -0.29 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers WHRN's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DEDD2]] | C | WHRN activity lowers DEDD2's level | lines that do not express WHRN (4) vs lines expressing it (46) | 2.06× higher at baseline in the lines without WHRN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLTCL1, NKAIN1, KIAA1549; maybe low, not absent; its own permutation p |
| [[UBLCP1]] | C | WHRN activity raises UBLCP1's level | lines that do not express WHRN (4) vs lines expressing it (46) | 2.02× lower at baseline in the lines without WHRN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLTCL1, NKAIN1, KIAA1549; maybe low, not absent; its own permutation p |
| [[WDR75]] | C | WHRN activity raises WDR75's level | lines that do not express WHRN (4) vs lines expressing it (46) | 1.60× lower at baseline in the lines without WHRN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLTCL1, NKAIN1, KIAA1549; maybe low, not absent; its own permutation p |
| [[PPP4R2]] | C | WHRN activity raises PPP4R2's level | lines that do not express WHRN (4) vs lines expressing it (46) | 1.41× lower at baseline in the lines without WHRN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLTCL1, NKAIN1, KIAA1549; maybe low, not absent; its own permutation p |
| [[RPP14]] | C | WHRN activity raises RPP14's level | lines that do not express WHRN (4) vs lines expressing it (46) | 1.15× lower at baseline in the lines without WHRN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLTCL1, NKAIN1, KIAA1549; maybe low, not absent; its own permutation p |
| [[BRIX1]] | C | WHRN activity raises BRIX1's level | lines that do not express WHRN (4) vs lines expressing it (46) | 1.59× lower at baseline in the lines without WHRN | 0.061 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLTCL1, NKAIN1, KIAA1549; maybe low, not absent |
| [[CHAMP1]] | C | WHRN activity raises CHAMP1's level | lines that do not express WHRN (4) vs lines expressing it (46) | 1.44× lower at baseline in the lines without WHRN | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLTCL1, NKAIN1, KIAA1549; maybe low, not absent |
| [[DNAH7]] | C | WHRN activity lowers DNAH7's level | lines that do not express WHRN (4) vs lines expressing it (46) | 1.42× higher at baseline in the lines without WHRN | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLTCL1, NKAIN1, KIAA1549; maybe low, not absent |
| [[ELAC1]] | C | WHRN activity raises ELAC1's level | lines that do not express WHRN (4) vs lines expressing it (46) | 1.41× lower at baseline in the lines without WHRN | 0.0999 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLTCL1, NKAIN1, KIAA1549; maybe low, not absent |

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.343). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.5, -30.7); signed map (-1.7, 18.4). **Vector** length 90.4, 20.7% of its response variance represented; |z| ≥ 3 in 985 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +1.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | -2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | +2.5 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +2.9 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | +1.9 | +1.7 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.8 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -3.8 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -3.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.0 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.8 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.7 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | whirlin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q32 — chr9:114,402,080-114,505,473 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CIP98, USH2D, PDZD7B; previously DFNB31 |
| Gene groups (HGNC) | PDZ domain containing; USH2 complex |
| Reactome | 4 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound by inner hair cells of the cochlea; Sensory processing of sound |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P202](https://www.uniprot.org/uniprotkb/Q9P202) (Whirlin):

> Involved in hearing and vision as member of the USH2 complex. Necessary for elongation and maintenance of inner and outer hair cell stereocilia in the organ of Corti in the inner ear. Involved in the maintenance of the hair bundle ankle region, which connects stereocilia in cochlear hair cells of the inner ear. In retina photoreceptors, required for the maintenance of periciliary membrane complex that seems to play a role in regulating intracellular protein transport.

**Summary**, from NCBI Gene [25861](https://www.ncbi.nlm.nih.gov/gene/25861):

> This gene is thought to function in the organization and stabilization of sterocilia elongation and actin cystoskeletal assembly, based on studies of the related mouse gene. Mutations in this gene have been associated with autosomal recessive non-syndromic deafness and Usher Syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2016]

**Accessions** — [HGNC:16361](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16361) · Entrez [25861](https://www.ncbi.nlm.nih.gov/gene/25861) · UniProt [Q9P202](https://www.uniprot.org/uniprotkb/Q9P202) · Ensembl [ENSG00000095397](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095397)

## Data

Gene col 1745: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1745); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1745, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1745]; `tensor/DDL_lfc|DDL_z.npy` [1745]; `embed/gene_vectors.npy` [1745]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1745 or target_col == 1745). Every well: [[WHRN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WHRN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
