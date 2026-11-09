---
symbol: "ZBTB21"
type: "gene"
col: 10370
ensembl_id: "ENSG00000173276"
name: "zinc finger and BTB domain containing 21"
location: "21q22.3"
module: 68
arm: "+"
pooled_cpm: 43.41
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 8
n_dd_up_clean: 22
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# ZBTB21

*zinc finger and BTB domain containing 21* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.64× (z +29.9, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.663× (z -6.8, q 8e-09, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF543]] (+0.70, fdr 1e-05), [[SLFN5]] (+0.67, fdr 1e-05), [[THAP2]] (+0.66, fdr 1e-04); moves opposite to [[TTLL5]] (-0.64, fdr 1e-05), [[LPCAT4]] (-0.62, fdr 8e-05), [[SNX1]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF382]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10370.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.64×** | +29.9 | 0e+00 | 46/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.22×** | +19.1 | 0e+00 | 46/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.37×** | +19.1 | 0e+00 | 45/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **7.93×** | +17.7 | 0e+00 | 47/49 (NCI-H460, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.45×** | +14.6 | 0e+00 | 45/48 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +13.2 | 9e-38 | 43/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.04×** | +11.7 | 1e-29 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +8.2 | 2e-14 | 36/48 (BT-474, A-427, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +7.7 | 8e-13 | 38/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.43×** | +7.6 | 2e-12 | 29/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +5.3 | 7e-06 | 31/48 (SW 900, Hs 766T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +5.2 | 1e-05 | 28/48 (NCI-H460, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +5.1 | 2e-05 | 28/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.39×** | +5.0 | 2e-05 | 27/47 (NCI-H460, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.35×** | +4.9 | 4e-05 | 30/48 (HEC-1-A, C-33 A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +4.6 | 2e-04 | 24/48 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10370.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.663×** | -6.8 | 8e-09 | 29/48 (SK-MEL-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.701×** | -5.8 | 1e-06 | 25/48 (SK-MEL-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.723×** | -5.3 | 2e-05 | 26/48 (SK-MEL-2, RKO, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.679×** | -4.6 | 7e-04 | 26/47 (SHP-77, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -4.1 | 0.006 | 2/49 (NCI-H2122, SW 1088) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.810×** | -3.5 | 0.048 | 17/48 (SK-MEL-2, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.819×** | -3.3 | 0.073 | 21/48 (SW 1088, NCI-H1792, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.683×** | -3.3 | 0.073 | 17/47 (RKO, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.824×** | -3.2 | 0.088 | 12/48 (SW1417, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10370. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 44.7 | 12 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +22.5) | — |
| [[HEC-1-A (line)]] | alt | 48.8 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +21.4) | — |
| [[LoVo (line)]] | wt | 34.3 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +17.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 85.6 | 7 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.21× (z +13.5) | — |
| [[PANC-1 (line)]] | alt | 38.9 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +24.3) | — |
| [[A-172 (line)]] | wt | 87.7 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.03× (z +23.6) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[C32 (line)]] | wt | 64.8 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +17.7) | — |
| [[HOP62 (line)]] | alt | 46.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.25× (z +19.2) | — |
| [[LS 180 (line)]] | wt | 35.4 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +15.7) | — |
| [[NCI-H1792 (line)]] | alt | 54.5 | 5 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.69× (z +13.7) | [[Selinexor (drug)]] 5 µM 0.393× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 33.0 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +13.6) | [[Dinaciclib (drug)]] 0.05 µM 0.240× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 33.7 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +16.8) | — |
| [[A549 (line)]] | wt | 35.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +18.9) | — |
| [[BT-474 (line)]] | alt | 58.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +15.4) | — |
| [[CFPAC-1 (line)]] | alt | 32.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +18.3) | — |
| [[HS-578T (line)]] | alt | 56.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +18.7) | — |
| [[NCI-H1573 (line)]] | alt | 40.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.98× (z +25.5) | — |
| [[A498 (line)]] | wt | 64.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +22.4) | — |
| [[COLO 205 (line)]] | alt | 32.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.87× (z +17.9) | — |
| [[Hs 766T (line)]] | wt | 28.1 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.103× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change · without an alert: [[XRK3F2 (drug)]] 0.5 µM 0.199× (z -8.6) |
| [[HT-29 (line)]] | alt | 29.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +12.4) | — |
| [[J82 (line)]] | alt | 23.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.02× (z +18.8) | — |
| [[NCI-H2347 (line)]] | alt | 17.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +14.2) | — |
| [[SK-MEL-2 (line)]] | alt | 52.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +15.1) | [[Lonafarnib (drug)]] 5 µM 0.156× (z -8.6) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 19.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +15.0) | — |
| [[H4 (line)]] | wt | 76.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.168× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[HCT15 (line)]] | alt | 43.6 | 1 | 2 | [[Homoharringtonine (drug)]] 0.5 µM 4.22× (z +9.0) | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.221× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 33.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +13.0) | — |
| [[RKO (line)]] | wt | 91.0 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 7.42× (z +9.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -8.7) |
| [[SNU-1 (line)]] | wt | 72.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +12.3) | — |
| [[SNU-423 (line)]] | alt | 31.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +15.4) | — |
| [[A-427 (line)]] | wt | 28.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +11.6) | — |
| [[hTERT-HPNE (line)]] | wt | 53.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +13.2) | — |
| [[KATO III (line)]] | alt | 45.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +13.6) | — |
| [[RPMI-7951 (line)]] | alt | 56.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +12.6) | — |
| [[SHP-77 (line)]] | alt | 38.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[SW 900 (line)]] | alt | 40.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +16.3) | — |
| [[SW48 (line)]] | wt | 45.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[AN3 CA (line)]] | alt | 35.6 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.112× (z -9.2) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 24.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +12.1) | — |
| [[LOX-IMVI (line)]] | wt | 46.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.60× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 20.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 33.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +12.2) | — |
| [[C-33 A (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10370), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF543]] | +0.70 | +0.69 / +0.52 | both halves | 1e-05 | same gene group |
| [[SLFN5]] | +0.67 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[THAP2]] | +0.66 | +0.57 / +0.35 | both halves | 1e-04 |  |
| [[ZXDA]] | +0.65 | +0.57 / +0.39 | both halves | 5e-05 | same gene group |
| [[LIG4]] | +0.65 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[GGPS1]] | +0.64 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ZXDB]] | +0.64 | +0.58 / +0.46 | both halves | 3e-05 | same gene group |
| [[BCDIN3D]] | +0.63 | +0.54 / +0.34 | both halves | 1e-04 |  |
| [[ZNF181]] | +0.62 | +0.63 / +0.32 | both halves | 2e-04 | same gene group |
| [[RIPK2-DT]] | +0.62 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[C19orf54]] | +0.61 | +0.54 / +0.33 | both halves | 1e-04 |  |
| [[FAM200A]] | +0.61 | +0.60 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTLL5]] | -0.64 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[LPCAT4]] | -0.62 | -0.61 / -0.37 | both halves | 8e-05 |  |
| [[SNX1]] | -0.60 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[GUSBP18]] | -0.59 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[RTTN]] | -0.59 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[IGSF8]] | -0.59 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[PHKA2]] | -0.59 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[CEP131]] | -0.59 | -0.53 / -0.21 | both halves | 7e-04 |  |
| [[CKLF]] | -0.58 | -0.59 / -0.32 | both halves | 1e-04 |  |
| [[L2HGDH]] | -0.58 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[BCR]] | -0.57 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[SLC9A6]] | -0.57 | -0.48 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF382]] | B | ZNF382 activity raises ZBTB21's level | lines that do not express ZNF382 (18) vs lines expressing it (32) | 1.32× lower at baseline in the lines without ZNF382 | 0.059 | ⚠ within organs, on part of the lines; also absent: AFF3, DZIP1, MMP16 |
| [[HDAC6]] | B | HDAC6 activity raises ZBTB21's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.648). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (4.9, 11.5); signed map (21.4, -11.3). **Vector** length 112, 32.1% of its response variance represented; |z| ≥ 3 in 1,229 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +10.2 | +14.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +13.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.5 | +19.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +8.4 | +11.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.7 | +19.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +8.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.7 | +4.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.3 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | -0.7 |
| fall | [[Belinostat (drug)]] 5 µM |  | -6.1 | -6.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.5 | -5.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.6 | +1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -4.5 | -5.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -4.1 | -3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -1.3 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.9 | -2.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -0.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:41,986,831-42,010,387 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1227; previously ZNF295 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULJ3](https://www.uniprot.org/uniprotkb/Q9ULJ3) (Zinc finger and BTB domain-containing protein 21):

> Acts as a transcription repressor.

**Summary**, from NCBI Gene [49854](https://www.ncbi.nlm.nih.gov/gene/49854):

> Enables several functions, including DNA-binding transcription repressor activity, RNA polymerase II-specific; POZ domain binding activity; and methyl-CpG binding activity. Involved in negative regulation of transcription by RNA polymerase II. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13083](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13083) · Entrez [49854](https://www.ncbi.nlm.nih.gov/gene/49854) · UniProt [Q9ULJ3](https://www.uniprot.org/uniprotkb/Q9ULJ3) · Ensembl [ENSG00000173276](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173276)

## Data

Gene col 10370: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10370); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10370, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10370]; `tensor/DDL_lfc|DDL_z.npy` [10370]; `embed/gene_vectors.npy` [10370]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10370 or target_col == 10370). Every well: [[ZBTB21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
