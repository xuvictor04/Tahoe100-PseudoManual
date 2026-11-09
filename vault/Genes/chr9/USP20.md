---
symbol: "USP20"
type: "gene"
col: 5930
ensembl_id: "ENSG00000136878"
name: "ubiquitin specific peptidase 20"
location: "9q34.11"
module: 52
arm: "+"
pooled_cpm: 17.39
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 15
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# USP20

*ubiquitin specific peptidase 20* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 4.87× (z +23.8, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.494× (z -10.6, q 2e-23, down in 33 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.743× (z -4.4, q 6e-04, down in 21 of 47 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZER1]] (+0.68, fdr 1e-05), [[PITPNA]] (+0.67, fdr 3e-05), [[ZBTB49]] (+0.64, fdr 1e-05); moves opposite to [[SMG7]] (-0.57, fdr 3e-05), [[SYNJ2BP]] (-0.55, fdr 1e-04), [[CLIC2]] (-0.54, fdr 5e-04).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5930.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.87×** | +23.8 | 0e+00 | 47/48 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.22×** | +21.6 | 0e+00 | 47/48 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.69×** | +21.1 | 0e+00 | 42/44 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.27×** | +17.8 | 0e+00 | 47/47 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.72×** | +11.5 | 2e-28 | 33/47 (NCI-H460, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +7.0 | 2e-10 | 33/48 (HOP62, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.5 | 3e-06 | 24/47 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.98×** | +5.4 | 6e-06 | 23/48 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.4 | 8e-04 | 16/47 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +4.3 | 0.001 | 20/46 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.64×** | +3.9 | 0.005 | 11/46 (NCI-H2347, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.015 | 12/48 (HEC-1-A, NCI-H2347, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.060 | 8/47 (Panc 03.27, NCI-H460, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 12 with an alert ⚠; shown: the 15 strongest. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5930.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.494×** | -10.6 | 2e-23 | 33/42 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.563×** | -8.3 | 3e-14 | 28/43 (LoVo, RKO, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.564×** | -8.3 | 3e-14 | 21/29 (HEC-1-A, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.576×** | -7.7 | 3e-12 | 23/33 (Hs 766T, HOP62, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.666×** | -6.1 | 1e-07 | 25/47 (NCI-H1792, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.691×** | -5.5 | 3e-06 | 25/48 (SW480, J82, …) | inconsistent across doses | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.730×** | -4.7 | 2e-04 | 21/47 (RKO, HOP62, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.740×** | -4.5 | 5e-04 | 21/48 (A498, A549, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.743×** | -4.4 | 6e-04 | 21/47 (A-427, SW 1271, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.742×** | -4.2 | 0.001 | 12/47 (SHP-77, RKO, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.791×** | -3.5 | 0.023 | 14/47 (NCI-H460, SW480, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.646×** | -3.4 | 0.028 | 7/25 (NCI-H1792, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.647×** | -3.4 | 0.028 | 12/47 (HEC-1-A, A498, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.805×** | -3.2 | 0.045 | 19/47 (SW48, LoVo, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.858× | -3.2 | 0.045 | 16/48 (A-172, J82, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5930. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 18.3 | 4 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 9.28× (z +13.9) | [[Dinaciclib (drug)]] 0.05 µM 0.0876× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Sulfisoxazole (drug)]] 0.5 µM 0.216× (z -9.6) |
| [[LoVo (line)]] | wt | 15.5 | 4 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -15.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 12.6 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.98× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.186× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 15.9 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.16× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0483× (z -23.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 13.7 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 6.54× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0842× (z -14.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 20.3 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.165× (z -13.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 20.0 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.23× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -10.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 19.8 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.57× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.183× (z -10.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 18.8 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.45× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.206× (z -9.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 19.1 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.02× (z +11.8) | [[AZD2858 (drug)]] 5 µM 0.0729× (z -9.0) ⚠ toxic |
| [[SW480 (line)]] | alt | 19.1 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.76× (z +15.7) | — |
| [[LS 180 (line)]] | wt | 12.1 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.98× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -12.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 12.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.60× (z +12.0) | — |
| [[RKO (line)]] | wt | 57.6 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.24× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -12.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 16.2 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.202× (z -10.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 25.2 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.95× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -11.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 29.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.27× (z +13.9) | — |
| [[COLO 205 (line)]] | alt | 30.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.25× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 17.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +10.9) | — |
| [[hTERT-HPNE (line)]] | wt | 14.7 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.78× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0820× (z -12.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 20.6 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -15.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 21.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.87× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -9.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 11.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.50× (z +9.3) | — |
| [[SW1417 (line)]] | alt | 23.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.97× (z +11.9) | — |
| [[AsPC-1 (line)]] | alt | 8.15 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 8.24× (z +9.4) | — |
| [[C32 (line)]] | wt | 19.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +8.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.174× (z -8.7) ⚠ toxic |
| [[HS-578T (line)]] | alt | 16.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.29× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 16.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.197× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H2347 (line)]] | alt | 16.5 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.56× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -10.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 15.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.06× (z +10.0) | [[Bosentan (hydrate) (drug)]] 5 µM 0.0873× (z -9.3) |
| [[A-427 (line)]] | wt | 11.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.38× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 8.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +9.2) | — |
| [[CHP-212 (line)]] | wt | 17.0 | 0 | 1 | — | [[Busulfan (drug)]] 5 µM 0.132× (z -8.8) |
| [[HCT15 (line)]] | alt | 15.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 13.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.06× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 17.7 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.99× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 19.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.43× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5930), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 9 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZER1]] | +0.68 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[PITPNA]] | +0.67 | +0.44 / +0.72 | both halves | 3e-05 |  |
| [[ZBTB49]] | +0.64 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[MIGA2]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[FBH1]] | +0.62 | +0.38 / +0.66 | both halves | 6e-05 |  |
| [[ARHGAP1]] | +0.62 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[ZBTB48]] | +0.58 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[PMM1]] | +0.58 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[ANKS3]] | +0.57 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[SRGAP2D]] | +0.57 | +0.25 / +0.70 | both halves | 4e-04 |  |
| [[MAP3K3]] | +0.57 | +0.26 / +0.68 | both halves | 3e-04 |  |
| [[ZNF333]] | +0.57 | +0.50 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMG7]] | -0.57 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[SYNJ2BP]] | -0.55 | -0.34 / -0.64 | both halves | 1e-04 |  |
| [[CLIC2]] | -0.54 | -0.23 / -0.48 | both halves | 5e-04 |  |
| [[FAM171B]] | -0.54 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[ATF7IP]] | -0.54 | -0.19 / -0.55 | ⚠ one half (not replicated) | 8e-04 |  |
| [[PRTFDC1]] | -0.52 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[AGPS]] | -0.52 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[COMMD8]] | -0.51 | -0.26 / -0.56 | both halves | 4e-04 |  |
| [[GMFB]] | -0.51 | -0.16 / -0.62 | ⚠ one half (not replicated) | 0.001 |  |
| [[ARPP19]] | -0.51 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[ZNF260]] | -0.51 | -0.07 / -0.63 | ⚠ one half (not replicated) | 0.004 |  |
| [[TSPAN6]] | -0.51 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[GNGT1]] | -0.51 | -0.24 / -0.53 | both halves | 5e-04 |  |
| [[MANEA]] | -0.51 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[ABLIM1]] | -0.50 | -0.35 / -0.51 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers USP20's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.557). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-15.2, -0.1); signed map (-45.8, 0.4). **Vector** length 75.3, 15.4% of its response variance represented; |z| ≥ 3 in 1,055 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +21.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.9 | +21.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.4 | +23.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +1.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.3 | +17.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +3.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | -0.6 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +1.6 | +3.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.2 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -1.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.3 | -7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | +0.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | +0.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:129,834,698-129,881,828 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1003 |
| Gene groups (HGNC) | Ubiquitin specific peptidases; MicroRNA protein coding host genes |
| Reactome | 2 pathways, smallest: Ub-specific processing proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2K6](https://www.uniprot.org/uniprotkb/Q9Y2K6) (Ubiquitin carboxyl-terminal hydrolase 20):

> Deubiquitinating enzyme that plays a role in many cellular processes including autophagy, cellular antiviral response or membrane protein biogenesis. Attenuates TLR4-mediated NF-kappa-B signaling by cooperating with beta-arrestin-2/ARRB2 and inhibiting TRAF6 autoubiquitination. Promotes cellular antiviral responses by deconjugating 'Lys-33' and 'Lys-48'-linked ubiquitination of STING1 leading to its stabilization. Plays an essential role in autophagy induction by regulating the ULK1 stability …

**Summary**, from NCBI Gene [10868](https://www.ncbi.nlm.nih.gov/gene/10868):

> This gene encodes a ubiquitin specific processing protease that was first identified as a substrate of the VHL (von Hippel-Lindau disease) protein E3 ubiquitin ligase complex. In addition to being ubiquitinated by the VHL-E3 ligase complex, this enzyme deubiquitinates hypoxia-inducible factor (HIF)-1 alpha and thereby causes increased expression of HIF-1alpha targeted genes which play a role in angiogenesis, glucose metabolism, cell proliferation and metastasis. The enzyme encoded by this gene …

**Accessions** — [HGNC:12619](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12619) · Entrez [10868](https://www.ncbi.nlm.nih.gov/gene/10868) · UniProt [Q9Y2K6](https://www.uniprot.org/uniprotkb/Q9Y2K6) · Ensembl [ENSG00000136878](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136878)

## Data

Gene col 5930: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5930); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5930, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5930]; `tensor/DDL_lfc|DDL_z.npy` [5930]; `embed/gene_vectors.npy` [5930]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5930 or target_col == 5930). Every well: [[USP20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
