---
symbol: "PERP"
type: "gene"
col: 3365
ensembl_id: "ENSG00000112378"
name: "p53 apoptosis effector related to PMP22"
location: "6q23.3"
module: 7
arm: "-"
pooled_cpm: 176.36
n_lines_expressing: 46
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 8
direction_downstream: 2
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# PERP

*p53 apoptosis effector related to PMP22* — 6q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.38× (z +14.2, q 6e-43, up in 45 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.32× (z +5.2, q 2e-05, up in 31 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.585× (z -9.9, q 2e-20, down in 32 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DSG2]] (+0.61, fdr 7e-06), [[SERINC1]] (+0.57, fdr 5e-05), [[TMSB4X]] (+0.56, fdr 1e-05); moves opposite to [[DNAJA3]] (-0.58, fdr 1e-05), [[L3MBTL2]] (-0.55, fdr 1e-05), [[DOLPP1]] (-0.54, fdr 3e-05).
> It sits in the **-** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[GPRC5A]] → it (grade B ⚠); 2 go from it, the strongest it → [[GPRC5A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3365.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.38×** | +14.2 | 6e-43 | 45/45 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.16×** | +14.1 | 9e-43 | 39/39 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.48×** | +11.0 | 5e-26 | 40/41 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +5.6 | 3e-06 | 29/43 (J82, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +5.2 | 2e-05 | 31/44 (SW1417, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.1 | 3e-05 | 27/46 (HS-578T, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.8 | 1e-04 | 24/45 (A498, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.6 | 0.019 | 0/46 | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | **1.30×** | +3.5 | 0.030 | 27/44 (SW 1271, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +3.3 | 0.047 | 17/44 (HepG2/C3A, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3365.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.585×** | -9.9 | 2e-20 | 32/44 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.575×** | -7.2 | 1e-10 | 40/44 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.679×** | -5.1 | 8e-05 | 27/44 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.711×** | -4.5 | 9e-04 | 32/44 (HCT15, HepG2/C3A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.698×** | -4.4 | 9e-04 | 31/44 (SW48, HCT15, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.713×** | -4.4 | 9e-04 | 27/44 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.782×** | -3.2 | 0.100 | 24/44 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.770×** | -3.2 | 0.100 | 23/44 (AsPC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.790× | -3.1 | 0.13 | 25/43 (HCT15, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.792× | -3.0 | 0.13 | 22/44 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3365. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 395 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -12.2) |
| [[HEC-1-A (line)]] | alt | 186 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +11.5) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.422× (z -9.7) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 5 µM 0.422× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 147 | 4 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.82× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.62× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -13.0) |
| [[NCI-H460 (line)]] | wt | 182 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.19× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -17.0) |
| [[SW480 (line)]] | alt | 327 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.319× (z -13.2) |
| [[HS-578T (line)]] | alt | 137 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.44× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +10.8) | — |
| [[A498 (line)]] | wt | 95.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.54× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 170 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 69.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.65× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 193 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +12.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.381× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 160 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -16.1) |
| [[PANC-1 (line)]] | alt | 190 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.07× (z +18.1) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 94.0 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.79× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -9.3) |
| [[SW1417 (line)]] | alt | 369 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 1.95× (z +9.7) | — |
| [[A-172 (line)]] | wt | 134 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.41× (z +12.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 164 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +11.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -12.0) |
| [[C32 (line)]] | wt | 164 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +14.7) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 94.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.43× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -9.9) |
| [[HOP62 (line)]] | alt | 77.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.94× (z +12.0) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 263 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.16× (z +11.3) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 172 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -11.8) |
| [[SK-MEL-2 (line)]] | alt | 80.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.08× (z +11.6) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 159 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +10.6) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 382 | 0 | 3 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.341× (z -9.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.380× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 158 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -11.5) |
| [[HCT15 (line)]] | alt | 270 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -10.4) |
| [[HT-29 (line)]] | alt | 202 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +10.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 51.4 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.26× (z +9.6) | — |
| [[LoVo (line)]] | wt | 286 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -10.7) |
| [[LS 180 (line)]] | wt | 362 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -11.4) |
| [[MIA PaCa-2 (line)]] | alt | 84.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.90× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 87.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.75× (z +10.6) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 67.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +9.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 49.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 76.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.03× (z +10.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 96.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +9.3) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 743 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.414× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 369 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -17.0) |
| [[SNU-1 (line)]] | wt | 59.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.13× (z +11.5) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 119 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -8.5) |
| [[AN3 CA (line)]] | alt | 31.7 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 108 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3365), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DSG2]] | +0.61 | +0.59 / +0.60 | both halves | 7e-06 | pathway: Formation of the cornified envelope; STRING 717 |
| [[SERINC1]] | +0.57 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[TMSB4X]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[CD55]] | +0.54 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[MFSD6]] | +0.54 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[ITM2B]] | +0.53 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[CD9]] | +0.52 | +0.51 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[SDCBP]] | +0.52 | +0.37 / +0.52 | both halves | 9e-05 |  |
| [[S100A6]] | +0.50 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[LEPROT]] | +0.50 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[DSC2]] | +0.50 | +0.48 / +0.49 | both halves | 2e-05 | pathway: Formation of the cornified envelope; STRING 680 |
| [[GRN]] | +0.49 | +0.42 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJA3]] | -0.58 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[L3MBTL2]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[DOLPP1]] | -0.54 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[DPH7]] | -0.54 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[AARS2]] | -0.49 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[ATAD3B]] | -0.48 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[EP400]] | -0.48 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[FAN1]] | -0.48 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[SKIC8]] | -0.47 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[DDX51]] | -0.47 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[ZNF787]] | -0.47 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[POLRMT]] | -0.47 | -0.31 / -0.52 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPRC5A]] | B | GPRC5A activity raises PERP's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 2.48× lower at baseline in the lines without GPRC5A | 0.005 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[COL17A1]] | B | COL17A1 activity raises PERP's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 2.49× lower at baseline in the lines without COL17A1 | 0.013 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| [[S100A4]] | B | S100A4 activity raises PERP's level | lines that do not express S100A4 (24) vs lines expressing it (26) | 1.60× lower at baseline in the lines without S100A4 | 0.020 | ⚠ within organs, on part of the lines; also absent: FOXQ1, ALDH3A1, MAOB |
| [[GAREM1]] | B | GAREM1 activity raises PERP's level | lines that do not express GAREM1 (10) vs lines expressing it (40) | 1.86× lower at baseline in the lines without GAREM1 | 0.060 | ⚠ within organs, on part of the lines; also absent: TESMIN, GRTP1; maybe low, not absent |
| [[LMO7]] | B | LMO7 activity raises PERP's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 2.17× lower at baseline in the lines without LMO7 | 0.066 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[DSC2]] | B | DSC2 activity raises PERP's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 1.87× lower at baseline in the lines without DSC2 | 0.085 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |
| [[HDAC6]] | B | HDAC6 activity raises PERP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises PERP's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPRC5A]] | C | PERP activity raises GPRC5A's level | lines that do not express PERP (4) vs lines expressing it (46) | 5.08× lower at baseline in the lines without PERP | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CASP8, TRIM47, PMAIP1; maybe low, not absent; its own permutation p |
| [[S100A6]] | C | PERP activity raises S100A6's level | lines that do not express PERP (4) vs lines expressing it (46) | 3.49× lower at baseline in the lines without PERP | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CASP8, TRIM47, PMAIP1; maybe low, not absent; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **-** arm (projection on the module's main direction -0.220). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-34.0, -17.5); signed map (45.8, -6.0). **Vector** length 114, 39.1% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.7 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.3 | +1.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +5.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +1.8 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.8 | +0.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.3 | +1.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.3 | +0.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.7 | -7.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.8 | -2.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.7 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.4 | -2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.0 | -2.3 |
|  | [[EX229 (drug)]] 5 µM |  | -3.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | p53 apoptosis effector related to PMP22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.3 — chr6:138,088,505-138,107,419 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PIGPC1, dJ496H19.1, KCP1, THW, KRTCAP1 |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, P53_PATHWAY |
| Reactome | 5 pathways, smallest: TP53 regulates transcription of several additional cell death genes whose specific roles in p53-dependent apoptosis remain uncertain; Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FX8](https://www.uniprot.org/uniprotkb/Q96FX8) (p53 apoptosis effector related to PMP-22):

> Component of intercellular desmosome junctions (By similarity). Plays a role in stratified epithelial integrity and cell-cell adhesion by promoting desmosome assembly (By similarity). Thereby plays a role in barrier function of the skin against infection (By similarity). Plays a role in mammary epithelial tissue homeostasis and remodeling during and after pregnancy, potentially via its involvement in desmosome cell-cell junctions (By similarity). Required for tooth enamel development via …

**Summary**, from NCBI Gene [64065](https://www.ncbi.nlm.nih.gov/gene/64065):

> Involved in positive regulation of neutrophil chemotaxis and positive regulation of proteolysis. Predicted to be located in desmosome and plasma membrane. Predicted to be active in cell-cell junction. Implicated in erythrokeratodermia variabilis and mutilating palmoplantar keratoderma with periorificial keratotic plaques. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17637](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17637) · Entrez [64065](https://www.ncbi.nlm.nih.gov/gene/64065) · UniProt [Q96FX8](https://www.uniprot.org/uniprotkb/Q96FX8) · Ensembl [ENSG00000112378](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112378)

## Data

Gene col 3365: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3365); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3365, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3365]; `tensor/DDL_lfc|DDL_z.npy` [3365]; `embed/gene_vectors.npy` [3365]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3365 or target_col == 3365). Every well: [[PERP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PERP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
