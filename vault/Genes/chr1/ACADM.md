---
symbol: "ACADM"
type: "gene"
col: 3871
ensembl_id: "ENSG00000117054"
name: "acyl-CoA dehydrogenase medium chain"
location: "1p31.1"
module: 3
arm: "-"
pooled_cpm: 33.3
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 8
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# ACADM

*acyl-CoA dehydrogenase medium chain* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.76× (z +25.5, q 0e+00, up in 45 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.78× (z +15.6, q 0e+00, up in 37 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.898× (z -6.9, q 2e-09, down in 5 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.700× (z -6.8, q 2e-09, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OXCT1]] (+0.71, fdr 7e-06), [[HNRNPH3]] (+0.66, fdr 1e-05), [[DECR1]] (+0.66, fdr 3e-05); moves opposite to [[MPG]] (-0.72, fdr 7e-06), [[MRPL55]] (-0.65, fdr 5e-05), [[PUSL1]] (-0.65, fdr 6e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3871.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.76×** | +25.5 | 0e+00 | 45/45 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.92×** | +25.3 | 0e+00 | 36/36 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.20×** | +20.7 | 0e+00 | 39/40 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +15.6 | 0e+00 | 37/46 (HEC-1-A, J82, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +12.5 | 5e-34 | 37/44 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +8.8 | 2e-16 | 30/46 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +8.7 | 3e-16 | 36/47 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +8.3 | 7e-15 | 26/46 (HT-29, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +7.2 | 3e-11 | 29/46 (HEC-1-A, SW 900, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +6.7 | 1e-09 | 27/47 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +6.4 | 9e-09 | 26/46 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +6.1 | 4e-08 | 29/47 (NCI-H2347, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +6.1 | 5e-08 | 24/45 (C32, LoVo, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +5.3 | 4e-06 | 21/47 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +5.1 | 1e-05 | 20/47 (HepG2/C3A, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.8 | 5e-05 | 21/47 (NCI-H2347, A498, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +4.4 | 3e-04 | 19/47 (NCI-H1792, C32, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.008 | 10/47 (J82, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.033 | 12/47 (HS-578T, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.18× | +3.1 | 0.037 | 6/47 (LoVo, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3871.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.898× | -6.9 | 2e-09 | 5/47 (NCI-H2030, NCI-H2347, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.700×** | -6.8 | 2e-09 | 25/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.690×** | -6.7 | 3e-09 | 28/47 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.721×** | -6.3 | 5e-08 | 25/46 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.760×** | -5.3 | 1e-05 | 25/47 (NCI-H2030, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.800×** | -4.3 | 0.002 | 19/47 (PANC-1, Hs 766T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.802×** | -4.2 | 0.002 | 16/47 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.814×** | -4.0 | 0.005 | 14/47 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.709×** | -3.5 | 0.035 | 14/40 (SNU-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | 0.737× | -3.1 | 0.12 | 10/46 (SHP-77, Panc 03.27, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3871. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 39.6 | 9 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +15.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.7 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.8) | — |
| [[SW480 (line)]] | alt | 51.4 | 4 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +8.6) | [[Bortezomib (drug)]] 0.05 µM 0.489× (z -8.8) |
| [[A498 (line)]] | wt | 31.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +9.5) | — |
| [[C32 (line)]] | wt | 30.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.87× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.81× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 17.5 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +9.8) | — |
| [[J82 (line)]] | alt | 39.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.92× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +12.1) | — |
| [[LOX-IMVI (line)]] | wt | 36.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.96× (z +13.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 16.2 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +11.7) | — |
| [[PANC-1 (line)]] | alt | 65.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +16.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +10.9) | — |
| [[SW 900 (line)]] | alt | 29.7 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.60× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +9.4) | — |
| [[A-427 (line)]] | wt | 61.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.85× (z +15.1) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 17.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +9.1) | — |
| [[HepG2_C3A (line)]] | wt | 29.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.00× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 24.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 23.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +11.5) | — |
| [[LoVo (line)]] | wt | 27.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.5× (z +17.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 25.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.75× (z +15.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 36.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +13.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 47.5 | 3 (3 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.71× (z +10.8) ⚠ toxic | — |
| [[SHP-77 (line)]] | alt | 60.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.58× (z +13.4) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 25.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +10.2) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 56.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.30× (z +10.9) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -12.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 42.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.15× (z +9.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 26.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.84× (z +13.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 50.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 27.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.83× (z +17.0) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 38.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 26.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +10.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 19.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +9.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 20.6 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.0647× (z -9.6) |
| [[HCT15 (line)]] | alt | 53.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.44× (z +9.3) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 34.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.68× (z +12.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 23.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.70× (z +12.2) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 21.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +9.3) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.274× (z -8.8) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 22.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3871), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OXCT1]] | +0.71 | +0.65 / +0.61 | both halves | 7e-06 | STRING 546 |
| [[HNRNPH3]] | +0.66 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[DECR1]] | +0.66 | +0.58 / +0.43 | both halves | 3e-05 | pathway: HALLMARK_ADIPOGENESIS; STRING 755 |
| [[TMX4]] | +0.65 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[HMGN1]] | +0.64 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[BMI1]] | +0.64 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[GALC]] | +0.64 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[BCLAF1]] | +0.64 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[ZMYND11]] | +0.63 | +0.57 / +0.37 | both halves | 7e-05 |  |
| [[CYB5D2]] | +0.63 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[DDX39B]] | +0.63 | +0.43 / +0.52 | both halves | 3e-05 | STRING 435 |
| [[CGGBP1]] | +0.62 | +0.64 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPG]] | -0.72 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[MRPL55]] | -0.65 | -0.39 / -0.59 | both halves | 5e-05 |  |
| [[PUSL1]] | -0.65 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[RALGDS]] | -0.64 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[CIAO2B]] | -0.63 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[RASSF7]] | -0.62 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[TMEM184B]] | -0.62 | -0.66 / -0.40 | both halves | 5e-05 |  |
| [[POLR2J4]] | -0.62 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[CDC34]] | -0.61 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[MRPL41]] ⚠ | -0.61 | -0.43 / -0.38 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SDHAF1]] | -0.61 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[DNAJC5]] | -0.61 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[TMEM120B]] | -0.61 | -0.64 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ACADM's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PRSS8]] | B | PRSS8 activity lowers ACADM's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 1.59× higher at baseline in the lines without PRSS8 | 0.037 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[PSMB5]] | B | PSMB5 activity raises ACADM's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[OGFRL1]] | B | OGFRL1 activity raises ACADM's level | lines that do not express OGFRL1 (10) vs lines expressing it (40) | 1.60× lower at baseline in the lines without OGFRL1 | 0.088 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, HDGFL3, CYP46A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.706). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-3.7, 4.4); signed map (16.2, -36.6). **Vector** length 88.7, 20.2% of its response variance represented; |z| ≥ 3 in 1,007 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +25.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +25.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +20.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.5 | +6.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.9 | +6.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | -0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.9 | +2.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.9 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +8.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | +1.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -5.4 | +3.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -4.2 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -4.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.4 | -6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | +0.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | -0.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.9 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA dehydrogenase medium chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:75,724,431-75,787,575 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MCAD, MCADH, ACAD1 |
| Gene groups (HGNC) | Acyl-CoA dehydrogenase family; Flavoproteins |
| Hallmark sets | FATTY_ACID_METABOLISM, ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 9 pathways, smallest: Beta oxidation of octanoyl-CoA to hexanoyl-CoA; mitochondrial fatty acid beta-oxidation of unsaturated fatty acids; Beta oxidation of decanoyl-CoA to octanoyl-CoA-CoA |
| Matched by | ensembl_id |

**Function**, from UniProt [P11310](https://www.uniprot.org/uniprotkb/P11310) (Medium-chain specific acyl-CoA dehydrogenase, mitochondrial):

> Medium-chain specific acyl-CoA dehydrogenase is one of the acyl-CoA dehydrogenases that catalyze the first step of mitochondrial fatty acid beta-oxidation (FAO), breaking down fatty acids into acetyl-CoA and allowing the production of energy from fats. The first step of FAO consists in the proR-proR stereospecific alpha, beta-dehydrogenation of fatty acyl-CoA thioesters using the electron transfer flavoprotein (ETF) as their physiologic electron acceptor, resulting in the formation of …

**Summary**, from NCBI Gene [34](https://www.ncbi.nlm.nih.gov/gene/34):

> This gene encodes the medium-chain specific (C4 to C12 straight chain) acyl-Coenzyme A dehydrogenase. The homotetramer enzyme catalyzes the initial step of the mitochondrial fatty acid beta-oxidation pathway. Defects in this gene cause medium-chain acyl-CoA dehydrogenase deficiency, a disease characterized by hepatic dysfunction, fasting hypoglycemia, and encephalopathy, which can result in infantile death. Alternatively spliced transcript variants encoding different isoforms have been found …

**Accessions** — [HGNC:89](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:89) · Entrez [34](https://www.ncbi.nlm.nih.gov/gene/34) · UniProt [P11310](https://www.uniprot.org/uniprotkb/P11310) · Ensembl [ENSG00000117054](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117054)

## Data

Gene col 3871: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3871); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3871, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3871]; `tensor/DDL_lfc|DDL_z.npy` [3871]; `embed/gene_vectors.npy` [3871]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3871 or target_col == 3871). Every well: [[ACADM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACADM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
