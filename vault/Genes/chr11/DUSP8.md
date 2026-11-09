---
symbol: "DUSP8"
type: "gene"
col: 11549
ensembl_id: "ENSG00000184545"
name: "dual specificity phosphatase 8"
location: "11p15.5"
module: 123
arm: "+"
pooled_cpm: 8.36
n_lines_expressing: 46
n_dd_up: 47
n_dd_down: 12
n_dd_up_clean: 36
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 9
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# DUSP8

*dual specificity phosphatase 8* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 47 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 16.7× (z +38.7, q 0e+00, up in 37 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.658× (z -5.8, q 4e-06, down in 25 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KRTAP5-AS1]] (+0.90, fdr 7e-06, ⚠ same locus), [[JUND]] (+0.74, fdr 7e-06), [[RHOB]] (+0.69, fdr 7e-06), [[TFE3]] (+0.66, fdr 7e-06); moves opposite to [[TTI1]] (-0.57, fdr 1e-05), [[METTL9]] (-0.57, fdr 2e-05), [[SNHG30]] (-0.56, fdr 1e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 9 go from it, the strongest it → [[DDAH2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 47 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11549.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **16.7×** | +38.7 | 0e+00 | 37/39 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.15×** | +17.6 | 0e+00 | 34/36 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **6.47×** | +17.4 | 0e+00 | 38/41 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.61×** | +12.5 | 2e-33 | 37/43 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **2.06×** | +9.9 | 5e-21 | 38/43 (LoVo, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.37×** | +8.4 | 6e-15 | 27/42 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **2.30×** | +8.1 | 5e-14 | 33/41 (COLO 205, LoVo, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **2.31×** | +7.8 | 4e-13 | 29/39 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Peretinoin (drug)]] 5 µM |  | **2.25×** | +7.6 | 2e-12 | 28/40 (COLO 205, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +7.6 | 2e-12 | 25/39 (NCI-H460, SW48, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **2.17×** | +7.5 | 3e-12 | 28/43 (COLO 205, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **2.15×** | +7.4 | 5e-12 | 34/43 (PANC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.15×** | +7.4 | 5e-12 | 27/42 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **2.09×** | +7.1 | 4e-11 | 25/41 (SW480, RPMI-7951, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.08×** | +7.1 | 5e-11 | 26/43 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **2.03×** | +6.9 | 2e-10 | 25/38 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.02×** | +6.8 | 3e-10 | 24/40 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.83×** | +5.8 | 2e-07 | 22/43 (NCI-H1573, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11549.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.658×** | -5.8 | 4e-06 | 25/36 (HT-29, LoVo, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.667×** | -5.6 | 6e-06 | 26/42 (HT-29, COLO 205, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.589×** | -5.0 | 1e-04 | 19/37 (HT-29, SNU-1, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.629×** | -4.5 | 8e-04 | 19/40 (HT-29, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.658×** | -3.9 | 0.009 | 17/37 (SNU-423, HT-29, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.768×** | -3.7 | 0.024 | 16/44 (NCI-H1573, Panc 03.27, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.709×** | -3.4 | 0.061 | 15/42 (A549, NCI-H1792, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **0.714×** | -3.3 | 0.066 | 16/43 (SW 1271, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **0.716×** | -3.3 | 0.066 | 6/40 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM |  | **0.795×** | -3.2 | 0.078 | 14/42 (NCI-H2347, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.542×** | -3.1 | 0.091 | 16/36 (COLO 205, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.730×** | -3.1 | 0.094 | 11/43 (PANC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.734× | -3.0 | 0.10 | 11/43 (SW 900, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11549. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 7.42 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 38.5× (z +25.5) | — |
| [[HT-29 (line)]] | alt | 49.0 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -16.1) |
| [[LoVo (line)]] | wt | 15.8 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +22.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -8.9) |
| [[A-172 (line)]] | wt | 17.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.7× (z +22.2) | — |
| [[A498 (line)]] | wt | 15.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.0× (z +25.3) | — |
| [[NCI-H1573 (line)]] | alt | 6.62 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 24.1× (z +18.7) | [[Clobetasol propionate (drug)]] 0.05 µM 0.0286× (z -14.8) |
| [[A549 (line)]] | wt | 10.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +17.1) | — |
| [[COLO 205 (line)]] | alt | 16.3 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +16.2) | [[Naproxen (drug)]] 0.05 µM 0.0784× (z -10.0) |
| [[HOP62 (line)]] | alt | 3.59 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 65.0× (z +16.8) | — |
| [[LS 180 (line)]] | wt | 14.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +17.4) | — |
| [[PANC-1 (line)]] | alt | 4.33 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 59.8× (z +22.2) | — |
| [[AsPC-1 (line)]] | alt | 4.94 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.0× (z +16.2) | — |
| [[HEC-1-A (line)]] | alt | 3.18 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.1× (z +16.1) | — |
| [[HS-578T (line)]] | alt | 4.31 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.1× (z +14.3) | — |
| [[NCI-H1792 (line)]] | alt | 7.63 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 4.15 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.1× (z +12.1) | — |
| [[SNU-423 (line)]] | alt | 11.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 16.6× (z +18.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0927× (z -10.5) |
| [[SW48 (line)]] | wt | 13.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +14.5) | — |
| [[SW480 (line)]] | alt | 3.15 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.5× (z +16.9) | — |
| [[C-33 A (line)]] | alt | 9.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 5.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +15.0) | — |
| [[HepG2_C3A (line)]] | wt | 19.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +16.3) | — |
| [[J82 (line)]] | alt | 7.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.1× (z +16.5) | — |
| [[KATO III (line)]] | alt | 5.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.54× (z +11.4) | — |
| [[LOX-IMVI (line)]] | wt | 5.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.8× (z +13.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 7.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.2× (z +10.7) | — |
| [[NCI-H2030 (line)]] | alt | 6.30 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.84× (z +12.9) | — |
| [[NCI-H23 (line)]] | alt | 5.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.51× (z +10.7) | — |
| [[NCI-H2347 (line)]] | alt | 9.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +16.7) | — |
| [[RKO (line)]] | wt | 11.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +9.6) | — |
| [[SNU-1 (line)]] | wt | 13.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 5.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +11.2) | — |
| [[SW1417 (line)]] | alt | 7.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.71× (z +13.2) | — |
| [[A-427 (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.697 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11549), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRTAP5-AS1]] | +0.90 | +0.87 / +0.92 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[JUND]] | +0.74 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[RHOB]] | +0.69 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[TFE3]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[ARVCF]] | +0.65 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[ATF3]] | +0.63 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[CREB5]] | +0.61 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[TUBB2B]] | +0.61 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[JUN]] | +0.61 | +0.57 / +0.62 | both halves | 1e-05 | pathway: MAPK family signaling cascades; STRING 521 |
| [[TP53INP2]] | +0.61 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[SLC41A2]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[FAM50A]] | +0.61 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[DUSP16]] | +0.60 | +0.60 / +0.71 | both halves | 7e-06 | same gene group; pathway: MAPK family signaling cascades; STRING 454 |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTI1]] | -0.57 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[METTL9]] | -0.57 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[SNHG30]] | -0.56 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[IPO11]] | -0.56 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[DPY19L3]] | -0.55 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[RNF4]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[LAMB1]] | -0.53 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[NIF3L1]] | -0.53 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[RNGTT]] | -0.53 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[PHB2]] | -0.51 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[PARGP1]] | -0.50 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[GMPS]] | -0.50 | -0.57 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DUSP8's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KRTAP5-AS1]] | B | KRTAP5-AS1 activity raises DUSP8's level | lines that do not express KRTAP5-AS1 (12) vs lines expressing it (38) | 2.08× lower at baseline in the lines without KRTAP5-AS1 | 0.017 | ⚠ within organs, on part of the lines; also absent: LLGL2, TFR2, USP43; maybe low, not absent |
| [[SERPINB7]] | B | SERPINB7 activity raises DUSP8's level | lines that do not express SERPINB7 (24) vs lines expressing it (26) | 1.31× lower at baseline in the lines without SERPINB7 | 0.073 | ⚠ within organs, on part of the lines; also absent: BASP1, DNAH11, SLC16A7 |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDAH2]] | C | DUSP8 activity raises DDAH2's level | lines that do not express DUSP8 (4) vs lines expressing it (46) | 2.07× lower at baseline in the lines without DUSP8 | 0.013 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FAM241B, BTG3-AS1; maybe low, not absent; co-absent with the target |
| [[XKR4]] | C | DUSP8 activity lowers XKR4's level | lines that do not express DUSP8 (4) vs lines expressing it (46) | 1.90× higher at baseline in the lines without DUSP8 | 0.023 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FAM241B, BTG3-AS1; maybe low, not absent |
| [[DUSP16]] | C | DUSP8 activity raises DUSP16's level | lines that do not express DUSP8 (4) vs lines expressing it (46) | 2.81× lower at baseline in the lines without DUSP8 | 0.026 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FAM241B, BTG3-AS1; maybe low, not absent; co-absent with the target |
| [[TSHZ1]] | C | DUSP8 activity lowers TSHZ1's level | lines that do not express DUSP8 (4) vs lines expressing it (46) | 2.45× higher at baseline in the lines without DUSP8 | 0.029 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FAM241B, BTG3-AS1; maybe low, not absent |
| [[KLF6]] | C | DUSP8 activity raises KLF6's level | lines that do not express DUSP8 (4) vs lines expressing it (46) | 1.74× lower at baseline in the lines without DUSP8 | 0.044 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FAM241B, BTG3-AS1; maybe low, not absent |
| [[ITSN2]] | C | DUSP8 activity raises ITSN2's level | lines that do not express DUSP8 (4) vs lines expressing it (46) | 1.48× lower at baseline in the lines without DUSP8 | 0.057 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FAM241B, BTG3-AS1; maybe low, not absent |
| [[RAB30]] | C | DUSP8 activity lowers RAB30's level | lines that do not express DUSP8 (4) vs lines expressing it (46) | 1.84× higher at baseline in the lines without DUSP8 | 0.066 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FAM241B, BTG3-AS1; maybe low, not absent |
| [[KRTAP5-AS1]] | C | DUSP8 activity raises KRTAP5-AS1's level | lines that do not express DUSP8 (4) vs lines expressing it (46) | 2.91× lower at baseline in the lines without DUSP8 | 0.069 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FAM241B, BTG3-AS1; maybe low, not absent |
| cells under [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM | C | DUSP8 activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (protects the cells) | lines that do not express DUSP8 (4) vs lines expressing it (44) | the lines without DUSP8: 0.79× the cells of the other lines | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FAM241B, BTG3-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.689). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.0, -0.6); signed map (-0.7, 22.4). **Vector** length 103, 25.7% of its response variance represented; |z| ≥ 3 in 1,163 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.8 | +38.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.2 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.8 | +3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.3 | +2.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +17.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.1 | +3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.7 | +3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.1 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.9 | +9.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.6 | -5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.2 | +0.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.0 | -3.4 |
|  | [[NG25 (drug)]] 5 µM |  | -2.8 | -3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.7 | -3.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -1.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.6 | -2.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | dual specificity phosphatase 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:1,554,051-1,572,271 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HVH-5, HB5, FLJ42958; previously C11orf81 |
| Gene groups (HGNC) | MAP kinase phosphatases |
| Reactome | 8 pathways, smallest: Signaling by MAPK mutants; RAF-independent MAPK1/3 activation; Negative regulation of MAPK pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13202](https://www.uniprot.org/uniprotkb/Q13202) (Dual specificity protein phosphatase 8):

> Has phosphatase activity with synthetic phosphatase substrates and negatively regulates mitogen-activated protein kinase activity, presumably by catalysing their dephosphorylation. Expected to display protein phosphatase activity toward phosphotyrosine, phosphoserine and phosphothreonine residues.

**Summary**, from NCBI Gene [1850](https://www.ncbi.nlm.nih.gov/gene/1850):

> The protein encoded by this gene is a member of the dual specificity protein phosphatase subfamily. These phosphatases inactivate their target kinases by dephosphorylating both the phosphoserine/threonine and phosphotyrosine residues. They negatively regulate members of the mitogen-activated protein (MAP) kinase superfamily (MAPK/ERK, SAPK/JNK, p38), which is associated with cellular proliferation and differentiation. Different members of the family of dual specificity phosphatases show …

**Accessions** — [HGNC:3074](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3074) · Entrez [1850](https://www.ncbi.nlm.nih.gov/gene/1850) · UniProt [Q13202](https://www.uniprot.org/uniprotkb/Q13202) · Ensembl [ENSG00000184545](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184545)

## Data

Gene col 11549: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11549); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11549, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11549]; `tensor/DDL_lfc|DDL_z.npy` [11549]; `embed/gene_vectors.npy` [11549]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11549 or target_col == 11549). Every well: [[DUSP8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUSP8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
