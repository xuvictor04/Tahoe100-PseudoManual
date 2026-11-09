---
symbol: "PHKA1"
type: "gene"
col: 853
ensembl_id: "ENSG00000067177"
name: "phosphorylase kinase regulatory subunit alpha 1"
location: "Xq13.1"
module: 18
arm: "+"
pooled_cpm: 40.7
n_lines_expressing: 43
n_dd_up: 21
n_dd_down: 18
n_dd_up_clean: 17
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# PHKA1

*phosphorylase kinase regulatory subunit alpha 1* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.30× (z +6.0, q 1e-06, up in 25 of 40 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Betamethasone dipropionate (drug)]] 5 µM: 1.31× (z +5.8, q 2e-06, up in 18 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.546× (z -19.4, q 0e+00, down in 34 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLMN]] (+0.61, fdr 7e-06), [[LDLRAD3]] (+0.61, fdr 7e-06), [[FAM135A]] (+0.59, fdr 1e-05); moves opposite to [[NR3C1]] (-0.55, fdr 1e-05), [[KLF7]] (-0.55, fdr 1e-05), [[HMGN2P46]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ADAM8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 853.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +6.0 | 1e-06 | 25/40 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.31×** | +5.8 | 2e-06 | 18/40 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.28×** | +5.7 | 3e-06 | 20/40 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | **1.28×** | +5.6 | 3e-06 | 18/41 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.29×** | +5.6 | 3e-06 | 18/40 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.28×** | +5.5 | 3e-06 | 17/40 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.27×** | +5.3 | 8e-06 | 19/40 (HOP62, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.25×** | +5.0 | 4e-05 | 18/40 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.23×** | +4.8 | 1e-04 | 20/40 (H4, HOP62, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.6 | 2e-04 | 15/40 (HOP62, Hs 766T, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.22×** | +4.5 | 3e-04 | 18/40 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +4.5 | 3e-04 | 16/40 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Econazole (drug)]] 5 µM |  | **1.22×** | +4.5 | 4e-04 | 15/40 (Hs 766T, HOP62, …) | rises with dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.21×** | +4.4 | 5e-04 | 14/40 (HT-29, LS 180, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +4.3 | 6e-04 | 13/40 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.21×** | +4.3 | 6e-04 | 10/40 (HOP62, H4, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.22×** | +4.3 | 6e-04 | 10/40 (A-427, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 853.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.546×** | -19.4 | 0e+00 | 34/40 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.469×** | -17.2 | 0e+00 | 34/41 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.484×** | -16.1 | 0e+00 | 36/41 (SW48, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.506×** | -15.5 | 0e+00 | 36/40 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.546×** | -13.2 | 5e-38 | 32/40 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.757×** | -8.9 | 7e-17 | 24/41 (SW1417, A-427, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.771×** | -8.3 | 7e-15 | 21/41 (SNU-1, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.695×** | -8.3 | 9e-15 | 27/40 (SW480, C32, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.527×** | -7.6 | 2e-12 | 30/41 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.700×** | -7.5 | 4e-12 | 22/38 (RKO, LoVo, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.721×** | -7.4 | 5e-12 | 24/40 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **0.729×** | -7.2 | 3e-11 | 24/39 (J82, NCI-H2030, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.732×** | -7.1 | 6e-11 | 21/40 (A498, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.749×** | -6.4 | 6e-09 | 24/40 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.816×** | -4.6 | 1e-04 | 14/40 (A498, C32, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.896× | -3.5 | 0.012 | 10/41 (NCI-H2347, PANC-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.851× | -3.4 | 0.020 | 14/39 (A549, H4, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 853. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 27.1 | 12 | 0 | [[Budesonide (drug)]] 0.05 µM 3.80× (z +10.7) | — |
| [[RKO (line)]] | wt | 74.3 | 0 | 9 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.305× (z -11.3) |
| [[SW48 (line)]] | wt | 102 | 0 | 8 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0806× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.146× (z -15.1) |
| [[SW480 (line)]] | alt | 57.1 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -19.7) |
| [[MIA PaCa-2 (line)]] | alt | 58.4 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -18.4) |
| [[PANC-1 (line)]] | alt | 73.1 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -22.0) |
| [[A549 (line)]] | wt | 69.9 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -15.6) |
| [[LoVo (line)]] | wt | 62.1 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.309× (z -14.8) |
| [[C32 (line)]] | wt | 60.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -17.5) |
| [[HEC-1-A (line)]] | alt | 28.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 81.6 | 0 | 5 | — | [[Harringtonine (drug)]] 5 µM 0.341× (z -12.6) |
| [[A498 (line)]] | wt | 40.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -19.4) |
| [[SW1417 (line)]] | alt | 40.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -13.4) |
| [[A-427 (line)]] | wt | 42.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.447× (z -10.6) |
| [[LS 180 (line)]] | wt | 44.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.247× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 30.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.284× (z -9.9) |
| [[SHP-77 (line)]] | alt | 45.6 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.307× (z -9.6) |
| [[SNU-1 (line)]] | wt | 73.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -13.3) |
| [[C-33 A (line)]] | alt | 51.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.311× (z -9.9) |
| [[HCT15 (line)]] | alt | 49.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.462× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 45.7 | 1 | 1 | [[Clobetasol propionate (drug)]] 5 µM 2.75× (z +8.5) | [[Harringtonine (drug)]] 5 µM 0.283× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 36.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -12.5) |
| [[NCI-H2347 (line)]] | alt | 26.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -10.6) |
| [[CHP-212 (line)]] | wt | 57.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0849× (z -11.4) |
| [[H4 (line)]] | wt | 25.7 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0992× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 15.1 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0765× (z -11.8) |
| [[Hs 766T (line)]] | wt | 41.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -9.0) |
| [[J82 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0662× (z -16.5) ⚠ transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 52.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.359× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 41.9 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0724× (z -9.5) |
| [[SNU-423 (line)]] | alt | 42.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.345× (z -9.4) |
| [[A-172 (line)]] | wt | 10.0 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.93 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.89 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.67 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.15 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 853), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLMN]] | +0.61 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[LDLRAD3]] | +0.61 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[FAM135A]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[TMEM164]] | +0.59 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[SFXN4]] | +0.59 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[EBPL]] | +0.59 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[CHPT1]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[NFIA]] | +0.58 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[PON2]] | +0.56 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[TUBGCP4]] | +0.55 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ANAPC1]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[ABCC4]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR3C1]] | -0.55 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[KLF7]] | -0.55 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[HMGN2P46]] | -0.54 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[VEGFC]] | -0.53 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[IFT22]] | -0.52 | -0.57 / -0.38 | both halves | 6e-05 |  |
| [[DDAH2]] | -0.51 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[CHMP4B]] | -0.51 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[APCDD1L-DT]] | -0.51 | -0.49 / -0.50 | both halves | 2e-05 |  |
| [[DNTTIP1]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ZNF267]] | -0.50 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[DAPK3]] | -0.49 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[KIAA1217]] | -0.49 | -0.50 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM8]] | B | ADAM8 activity weakens PHKA1's drug response | lines that do not express ADAM8 (23) vs lines expressing it (18) | the lines without ADAM8 respond 1.57× as strongly (z diff -2.11); strongest at Idarubicin (hydrochloride) 5 µM: 0.68x vs 0.92x (z diff -3.9) | 0.039 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[NR3C1]] | B | NR3C1 activity raises PHKA1's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[NFIA]] | B | NFIA activity raises PHKA1's level | lines that do not express NFIA (11) vs lines expressing it (39) | 2.01× lower at baseline in the lines without NFIA | 0.090 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.620). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (28.6, -2.4); signed map (-4.0, -54.4). **Vector** length 108, 26.8% of its response variance represented; |z| ≥ 3 in 1,159 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.9 | +6.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.5 | +4.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +4.2 | +5.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +4.1 | +3.5 |
|  | [[Budesonide (drug)]] 5 µM |  | +4.1 | +5.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +4.0 | +5.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.2 | -7.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -13.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.8 | -7.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -8.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -3.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | phosphorylase kinase regulatory subunit alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:72,578,814-72,714,319 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PHKA |
| Gene groups (HGNC) | Phosphorylase kinase subunits |
| Reactome | 3 pathways, smallest: Glycogen breakdown (glycogenolysis); Glycogen metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P46020](https://www.uniprot.org/uniprotkb/P46020) (Phosphorylase b kinase regulatory subunit alpha, skeletal muscle isoform):

> Phosphorylase b kinase catalyzes the phosphorylation of serine in certain substrates, including troponin I. The alpha chain may bind calmodulin.

**Summary**, from NCBI Gene [5255](https://www.ncbi.nlm.nih.gov/gene/5255):

> Phosphorylase kinase is a polymer of 16 subunits, four each of alpha, beta, gamma and delta. The alpha subunit includes the skeletal muscle and hepatic isoforms, and the skeletal muscle isoform is encoded by this gene. The beta subunit is the same in both the muscle and hepatic isoforms, and encoded by one gene. The gamma subunit also includes the skeletal muscle and hepatic isoforms, which are encoded by two different genes. The delta subunit is a calmodulin and can be encoded by three …

**Accessions** — [HGNC:8925](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8925) · Entrez [5255](https://www.ncbi.nlm.nih.gov/gene/5255) · UniProt [P46020](https://www.uniprot.org/uniprotkb/P46020) · Ensembl [ENSG00000067177](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067177)

## Data

Gene col 853: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 853); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 853, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 853]; `tensor/DDL_lfc|DDL_z.npy` [853]; `embed/gene_vectors.npy` [853]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 853 or target_col == 853). Every well: [[PHKA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHKA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
