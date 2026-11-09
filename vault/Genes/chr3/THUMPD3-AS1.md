---
symbol: "THUMPD3-AS1"
type: "gene"
col: 13053
ensembl_id: "ENSG00000206573"
name: "THUMPD3 antisense RNA 1"
location: "3p25.3"
module: 38
arm: "+"
pooled_cpm: 104.48
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 28
n_dd_up_clean: 9
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# THUMPD3-AS1

*THUMPD3 antisense RNA 1* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.04× (z +16.3, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.590× (z -8.6, q 6e-15, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C21orf91-OT1]] (+0.79, fdr 7e-06), [[ADAMTSL4-AS2]] (+0.78, fdr 7e-06), [[UBE2D3-AS1]] (+0.75, fdr 7e-06); moves opposite to [[FYCO1]] (-0.68, fdr 7e-06), [[ATP5F1C]] (-0.63, fdr 1e-05), [[SLC23A2]] (-0.63, fdr 3e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13053.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +16.3 | 0e+00 | 47/49 (AsPC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.42×** | +14.2 | 1e-43 | 48/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +11.5 | 2e-28 | 40/47 (NCI-H1792, C32, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.52×** | +6.7 | 2e-09 | 44/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +6.0 | 2e-07 | 31/48 (A-172, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.4 | 0.001 | 28/50 (RKO, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.3 | 0.001 | 28/48 (HS-578T, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.0 | 0.005 | 0/50 | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.025 | 28/48 (HOP62, Panc 03.27, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.074 | 22/48 (CFPAC-1, HOP62, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13053.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.590×** | -8.6 | 6e-15 | 45/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.624×** | -7.7 | 6e-12 | 45/48 (BT-474, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.640×** | -7.2 | 8e-11 | 35/48 (NCI-H1573, PANC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.646×** | -7.1 | 2e-10 | 41/48 (NCI-H1573, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.682×** | -6.2 | 6e-08 | 40/48 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.693×** | -6.0 | 2e-07 | 32/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.697×** | -5.9 | 4e-07 | 37/48 (NCI-H23, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.693×** | -5.7 | 7e-07 | 36/47 (HOP62, LS 180, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.705×** | -5.5 | 3e-06 | 31/48 (SNU-423, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.717×** | -5.4 | 3e-06 | 28/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.712×** | -5.3 | 6e-06 | 31/47 (AsPC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.546×** | -5.1 | 1e-05 | 41/49 (NCI-H1573, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.736×** | -5.0 | 3e-05 | 32/48 (SW 1271, SW480, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.741×** | -4.9 | 5e-05 | 27/48 (NCI-H1573, H4, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.751×** | -4.6 | 1e-04 | 28/47 (SW480, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | **0.779×** | -3.9 | 0.003 | 29/48 (NCI-H2030, Panc 03.27, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.801×** | -3.6 | 0.009 | 26/48 (PANC-1, C32, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.859× | -3.5 | 0.014 | 20/48 (CHP-212, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13053. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 97.3 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.231× (z -14.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.320× (z -11.4) |
| [[HOP62 (line)]] | alt | 209 | 3 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +11.0) | [[Ixazomib citrate (drug)]] 0.5 µM 0.424× (z -9.5) |
| [[SW480 (line)]] | alt | 116 | 2 | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.96× (z +15.8) | [[Harringtonine (drug)]] 0.5 µM 0.537× (z -9.0) |
| [[A-172 (line)]] | wt | 134 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.417× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[C32 (line)]] | wt | 66.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +18.2) | — |
| [[HEC-1-A (line)]] | alt | 200 | 3 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.36× (z +15.7) | [[Lonafarnib (drug)]] 5 µM 0.247× (z -9.5) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 81.1 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.434× (z -8.6) |
| [[PANC-1 (line)]] | alt | 76.1 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.455× (z -9.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.456× (z -9.2) |
| [[HCT15 (line)]] | alt | 118 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.322× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[HS-578T (line)]] | alt | 100 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +12.9) | — |
| [[hTERT-HPNE (line)]] | wt | 100 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.7) | — |
| [[KATO III (line)]] | alt | 137 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.329× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 104 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +15.6) | — |
| [[NCI-H460 (line)]] | wt | 79.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +10.7) | — |
| [[RKO (line)]] | wt | 79.6 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.94× (z +13.5) | — |
| [[SK-MEL-2 (line)]] | alt | 112 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +15.3) | — |
| [[SNU-423 (line)]] | alt | 112 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +10.1) | [[Belumosudil (drug)]] 5 µM 0.398× (z -8.7) |
| [[SW 900 (line)]] | alt | 98.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +12.1) | — |
| [[A498 (line)]] | wt | 53.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +15.1) | — |
| [[A549 (line)]] | wt | 100 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.240× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 99.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +19.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.395× (z -9.6) ⚠ toxic |
| [[BT-474 (line)]] | alt | 118 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0853× (z -10.3) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 63.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +13.1) | — |
| [[HT-29 (line)]] | alt | 119 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.57× (z +14.5) | — |
| [[LS 180 (line)]] | wt | 73.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.82× (z +11.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 85.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +12.4) | — |
| [[NCI-H1792 (line)]] | alt | 103 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +18.3) | — |
| [[NCI-H2347 (line)]] | alt | 96.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +13.1) | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 2 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.220× (z -12.6) |
| [[Panc 03.27 (line)]] | alt | 103 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +15.2) | — |
| [[RPMI-7951 (line)]] | alt | 177 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 180 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +13.5) | — |
| [[SW48 (line)]] | wt | 74.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +10.6) | — |
| [[C-33 A (line)]] | alt | 91.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +8.9) | — |
| [[CHP-212 (line)]] | wt | 90.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 122 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.408× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 102 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +10.1) | — |
| [[Hs 766T (line)]] | wt | 107 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +11.2) | — |
| [[J82 (line)]] | alt | 124 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 87.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.2) | — |
| [[SHP-77 (line)]] | alt | 63.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.17× (z +9.4) | — |
| [[SW 1088 (line)]] | alt | 151 | 0 | 1 | — | [[Fumaric acid (drug)]] 0.05 µM 0.106× (z -9.2) |
| [[SW 1271 (line)]] | alt | 205 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -12.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 92.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 88.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13053), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C21orf91-OT1]] | +0.79 | +0.79 / +0.69 | both halves | 7e-06 |  |
| [[ADAMTSL4-AS2]] | +0.78 | +0.77 / +0.72 | both halves | 7e-06 | same gene group |
| [[UBE2D3-AS1]] | +0.75 | +0.71 / +0.60 | both halves | 7e-06 | same gene group |
| [[SLC9A5]] | +0.74 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[LRP2BP]] | +0.74 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[NUP210L]] | +0.74 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[GSK3B-DT]] | +0.73 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[IDI2-AS1]] | +0.73 | +0.69 / +0.66 | both halves | 7e-06 | same gene group |
| [[ACTR3-AS1]] | +0.73 | +0.72 / +0.59 | both halves | 7e-06 | same gene group |
| [[AVIL]] | +0.72 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[FAM151B]] | +0.72 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[PILRA]] | +0.72 | +0.74 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FYCO1]] | -0.68 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[ATP5F1C]] | -0.63 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[SLC23A2]] | -0.63 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[BLMH]] | -0.62 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[SERAC1]] | -0.62 | -0.66 / -0.40 | both halves | 5e-05 |  |
| [[ACTR5]] | -0.62 | -0.54 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers THUMPD3-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.778). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.2, -17.7); signed map (10.9, 13.4). **Vector** length 148, 48.7% of its response variance represented; |z| ≥ 3 in 1,263 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +13.1 | +14.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.8 | +16.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +10.6 | +11.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +6.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.6 | +6.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +2.9 |
| fall | [[Belinostat (drug)]] 5 µM |  | -7.3 | -8.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.6 | -5.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.3 | -7.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -6.2 | -5.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.1 | -5.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.7 | -5.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.3 | -3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.3 | -3.0 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -3.9 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | THUMPD3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p25.3 — chr3:9,349,689-9,398,579 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously SETD5-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44478](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44478) · Entrez [440944](https://www.ncbi.nlm.nih.gov/gene/440944) · Ensembl [ENSG00000206573](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206573)

## Data

Gene col 13053: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13053); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13053, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13053]; `tensor/DDL_lfc|DDL_z.npy` [13053]; `embed/gene_vectors.npy` [13053]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13053 or target_col == 13053). Every well: [[THUMPD3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THUMPD3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
