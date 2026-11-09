---
symbol: "IGF2R"
type: "gene"
col: 12338
ensembl_id: "ENSG00000197081"
name: "insulin like growth factor 2 receptor"
location: "6q25.3"
module: 122
arm: "+"
pooled_cpm: 177.03
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 4
n_dd_up_clean: 17
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# IGF2R

*insulin like growth factor 2 receptor* — 6q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.13× (z +23.5, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.694× (z -7.8, q 5e-12, down in 37 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 0.795× (z -5.1, q 1e-04, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPP1]] (+0.74, fdr 7e-06), [[GBA1]] (+0.71, fdr 7e-06), [[ATP6V1C1]] (+0.70, fdr 7e-06); moves opposite to [[FBXO45]] (-0.56, fdr 6e-05), [[PDCD2L]] (-0.55, fdr 1e-05), [[MRPS26]] (-0.55, fdr 1e-04).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MMP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12338.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.13×** | +23.5 | 0e+00 | 46/48 (J82, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +12.5 | 3e-33 | 43/48 (KATO III, HT-29, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.70×** | +11.7 | 2e-29 | 39/48 (COLO 205, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +9.3 | 3e-18 | 33/49 (LoVo, AsPC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +8.1 | 8e-14 | 30/48 (COLO 205, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +7.7 | 1e-12 | 34/48 (COLO 205, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +6.9 | 6e-10 | 33/48 (HepG2/C3A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.24×** | +6.7 | 1e-09 | 27/48 (LoVo, HT-29, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +6.6 | 2e-09 | 37/48 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +6.6 | 2e-09 | 36/48 (SK-MEL-2, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.34×** | +6.5 | 5e-09 | 35/48 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +6.4 | 7e-09 | 36/48 (HT-29, RPMI-7951, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +6.2 | 3e-08 | 34/48 (A549, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +6.1 | 6e-08 | 32/48 (HepG2/C3A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +5.9 | 2e-07 | 28/48 (HT-29, SK-MEL-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.00×** | +5.3 | 3e-06 | 35/49 (NCI-H2347, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.27×** | +5.3 | 4e-06 | 31/48 (SHP-77, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +3.5 | 0.013 | 22/48 (C32, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12338.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.694×** | -7.8 | 5e-12 | 37/47 (COLO 205, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.795×** | -5.1 | 1e-04 | 28/48 (HT-29, LS 180, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.825×** | -4.3 | 0.004 | 22/48 (MIA PaCa-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.797×** | -3.6 | 0.044 | 25/48 (RPMI-7951, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.841× | -3.5 | 0.044 | 19/47 (SNU-1, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Verteporfin (drug)]] 5 µM |  | 0.849× | -3.5 | 0.047 | 18/49 (PANC-1, C32, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.864× | -3.2 | 0.095 | 18/48 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | 0.861× | -3.2 | 0.10 | 12/48 (AN3 CA, SW480, …) | top dose only | position effect removed |
| [[Vilanterol (drug)]] 5 µM |  | 0.905× | -3.1 | 0.11 | 4/49 (LOX-IMVI, HCT15, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12338. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 76.8 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +15.5) | — |
| [[BT-474 (line)]] | alt | 107 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +13.5) | — |
| [[HepG2_C3A (line)]] | wt | 283 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +18.9) | — |
| [[LoVo (line)]] | wt | 123 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +15.2) | — |
| [[NCI-H1792 (line)]] | alt | 169 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +11.9) | — |
| [[A498 (line)]] | wt | 187 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +12.1) | — |
| [[AsPC-1 (line)]] | alt | 108 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +29.6) | — |
| [[HOP62 (line)]] | alt | 107 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +13.0) | — |
| [[HT-29 (line)]] | alt | 203 | 4 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.61× (z +12.3) | [[Harringtonine (drug)]] 0.5 µM 0.411× (z -11.4) ⚠ cell-cycle shift, explains ~20% of this change |
| [[J82 (line)]] | alt | 199 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +30.8) | — |
| [[NCI-H1573 (line)]] | alt | 106 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +18.8) | — |
| [[NCI-H460 (line)]] | wt | 191 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +28.0) | — |
| [[C32 (line)]] | wt | 183 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 248 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +19.8) | — |
| [[Hs 766T (line)]] | wt | 109 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +26.8) | — |
| [[SW 900 (line)]] | alt | 191 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +17.4) | — |
| [[A-172 (line)]] | wt | 276 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +19.5) | — |
| [[CFPAC-1 (line)]] | alt | 88.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +19.7) | — |
| [[HS-578T (line)]] | alt | 164 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +16.4) | — |
| [[KATO III (line)]] | alt | 197 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +16.7) | — |
| [[NCI-H2347 (line)]] | alt | 124 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +26.7) | — |
| [[Panc 03.27 (line)]] | alt | 117 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +21.4) | — |
| [[PANC-1 (line)]] | alt | 232 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +14.7) | — |
| [[RKO (line)]] | wt | 167 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +18.1) | — |
| [[RPMI-7951 (line)]] | alt | 235 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +14.6) | — |
| [[SW48 (line)]] | wt | 138 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +16.7) | — |
| [[HEC-1-A (line)]] | alt | 107 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.62× (z +11.8) | — |
| [[hTERT-HPNE (line)]] | wt | 276 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +12.5) | — |
| [[SK-MEL-2 (line)]] | alt | 126 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +14.7) | — |
| [[SNU-423 (line)]] | alt | 459 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +14.7) | — |
| [[SW480 (line)]] | alt | 273 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +12.3) | — |
| [[A-427 (line)]] | wt | 160 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.8) | — |
| [[C-33 A (line)]] | alt | 99.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 168 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.38× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[LOX-IMVI (line)]] | wt | 158 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 176 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.54× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 228 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +21.7) | — |
| [[NCI-H23 (line)]] | alt | 96.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.7) | — |
| [[SHP-77 (line)]] | alt | 146 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 1.94× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 173 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.8) | — |
| [[SW1417 (line)]] | alt | 225 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.91× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 490 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 168 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 170 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12338), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPP1]] | +0.74 | +0.68 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[GBA1]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[ATP6V1C1]] | +0.70 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[GNS]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 | pathway: trans-Golgi Network Vesicle Budding |
| [[LAMP2]] | +0.65 | +0.59 / +0.67 | both halves | 7e-06 | same gene group; pathway: HALLMARK_PROTEIN_SECRETION; STRING 532 |
| [[APP]] | +0.63 | +0.38 / +0.69 | both halves | 6e-05 | pathway: HALLMARK_APOPTOSIS |
| [[M6PR]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 | same gene group; pathway: HALLMARK_PROTEIN_SECRETION; STRING 991 |
| [[HEXB]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 | STRING 550 |
| [[LAMP1]] | +0.57 | +0.58 / +0.54 | both halves | 1e-05 | same gene group; STRING 634 |
| [[WASHC2C]] | +0.56 | +0.54 / +0.50 | both halves | 1e-05 | STRING 780 |
| [[PEPD]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[WASHC2A]] | +0.55 | +0.52 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO45]] | -0.56 | -0.39 / -0.60 | both halves | 6e-05 |  |
| [[PDCD2L]] | -0.55 | -0.50 / -0.49 | both halves | 1e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[MRPS26]] | -0.55 | -0.34 / -0.60 | both halves | 1e-04 |  |
| [[TUBGCP5]] | -0.53 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[POP7]] | -0.52 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[TARS2]] | -0.51 | -0.32 / -0.54 | both halves | 1e-04 |  |
| [[EEF1AKMT4]] | -0.51 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[SNU13]] | -0.51 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[NSFP1]] | -0.50 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[SIVA1]] | -0.50 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[C16orf91]] | -0.49 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[SAC3D1]] | -0.49 | -0.31 / -0.52 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP2]] | B | MMP2 activity raises IGF2R's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 1.20× lower at baseline in the lines without MMP2 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.625). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-22.1, -20.3); signed map (-23.8, -35.8). **Vector** length 121, 40.1% of its response variance represented; |z| ≥ 3 in 1,200 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.9 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.1 | +2.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +8.0 | +3.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +7.7 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.6 | +2.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +4.3 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +2.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.5 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +5.9 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.2 | -7.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.4 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.5 | -5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -5.0 | -3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.8 | -3.5 |
|  | [[Vilanterol (drug)]] 5 µM |  | -2.9 | -3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.7 | -1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | insulin like growth factor 2 receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.3 — chr6:159,969,082-160,113,507 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD222, MPRI, MPR1, CIMPR, M6P-R, CI-M6PR, CI-MPR, MPR300 |
| Gene groups (HGNC) | CD molecules; MRH domain containing |
| Hallmark sets | PROTEIN_SECRETION, APOPTOSIS, IL2_STAT5_SIGNALING |
| Reactome | 10 pathways, smallest: Retrograde transport at the Trans-Golgi-Network; Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding |
| Matched by | ensembl_id |

**Function**, from UniProt [P11717](https://www.uniprot.org/uniprotkb/P11717) (Cation-independent mannose-6-phosphate receptor):

> Mediates the transport of phosphorylated lysosomal enzymes from the Golgi complex and the cell surface to lysosomes. Lysosomal enzymes bearing phosphomannosyl residues bind specifically to mannose-6-phosphate receptors in the Golgi apparatus and the resulting receptor-ligand complex is transported to an acidic prelysosomal compartment where the low pH mediates the dissociation of the complex. The receptor is then recycled back to the Golgi for another round of trafficking through its binding to …

**Summary**, from NCBI Gene [3482](https://www.ncbi.nlm.nih.gov/gene/3482):

> This gene encodes a receptor for both insulin-like growth factor 2 and mannose 6-phosphate. The binding sites for each ligand are located on different segments of the protein. This receptor has various functions, including in the intracellular trafficking of lysosomal enzymes, the activation of transforming growth factor beta, and the degradation of insulin-like growth factor 2. Mutation or loss of heterozygosity of this gene has been association with risk of hepatocellular carcinoma. The …

**Accessions** — [HGNC:5467](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5467) · Entrez [3482](https://www.ncbi.nlm.nih.gov/gene/3482) · UniProt [P11717](https://www.uniprot.org/uniprotkb/P11717) · Ensembl [ENSG00000197081](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197081)

## Data

Gene col 12338: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12338); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12338, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12338]; `tensor/DDL_lfc|DDL_z.npy` [12338]; `embed/gene_vectors.npy` [12338]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12338 or target_col == 12338). Every well: [[IGF2R — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGF2R.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
