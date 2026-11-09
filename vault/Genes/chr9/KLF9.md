---
symbol: "KLF9"
type: "gene"
col: 4041
ensembl_id: "ENSG00000119138"
name: "KLF transcription factor 9"
location: "9q21.12"
module: 98
arm: "+"
pooled_cpm: 37.18
n_lines_expressing: 45
n_dd_up: 43
n_dd_down: 27
n_dd_up_clean: 37
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 7
direction_downstream: 2
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# KLF9

*KLF transcription factor 9* — 9q21.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (6 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 0.05 µM: 2.79× (z +17.3, q 0e+00, up in 33 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.413× (z -14.9, q 0e+00, down in 39 of 43 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.345× (z -9.4, q 2e-18, down in 37 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSC22D3]] (+0.75, fdr 7e-06), [[BCL6]] (+0.73, fdr 7e-06), [[MAOA]] (+0.72, fdr 7e-06); moves opposite to [[ADAMTS16]] (-0.58, fdr 1e-05), [[PKIA]] (-0.56, fdr 2e-05), [[ANXA10]] (-0.54, fdr 1e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ATOH8]] → it (grade B ⚠); 2 go from it, the strongest it → [[PHF21A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 6 with an alert ⚠; shown: the 15 strongest. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4041.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.79×** | +17.3 | 0e+00 | 33/43 (SNU-423, Hs 766T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **2.76×** | +17.0 | 0e+00 | 33/43 (SNU-423, NCI-H460, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **2.75×** | +17.0 | 0e+00 | 34/43 (NCI-H460, SNU-423, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **2.00×** | +16.4 | 0e+00 | 31/43 (A498, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **2.64×** | +16.3 | 0e+00 | 32/43 (Hs 766T, SNU-423, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.53×** | +15.6 | 0e+00 | 31/42 (NCI-H460, Hs 766T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **2.52×** | +15.5 | 0e+00 | 32/43 (Hs 766T, HS-578T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.58×** | +15.3 | 0e+00 | 33/43 (NCI-H460, Hs 766T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **2.59×** | +14.8 | 0e+00 | 31/42 (NCI-H460, Hs 766T, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **2.37×** | +14.5 | 0e+00 | 31/43 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **2.37×** | +14.5 | 0e+00 | 33/43 (A498, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **2.35×** | +14.3 | 6e-45 | 30/43 (Hs 766T, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **2.26×** | +13.7 | 6e-41 | 29/43 (Hs 766T, SNU-423, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **2.24×** | +13.6 | 2e-40 | 31/43 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +12.7 | 1e-35 | 31/43 (Hs 766T, NCI-H460, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4041.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.413×** | -14.9 | 0e+00 | 39/43 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.345×** | -9.4 | 2e-18 | 37/43 (Hs 766T, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.392×** | -8.2 | 3e-14 | 31/43 (RPMI-7951, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.398×** | -8.1 | 7e-14 | 34/43 (MIA PaCa-2, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.407×** | -7.9 | 3e-13 | 31/43 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.443×** | -7.2 | 7e-11 | 32/43 (C32, SW 1271, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Clotrimazole (drug)]] 5 µM |  | **0.753×** | -6.8 | 1e-09 | 27/44 (NCI-H460, SNU-423, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.675×** | -6.4 | 1e-08 | 23/43 (A498, LOX-IMVI, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.773×** | -6.2 | 5e-08 | 23/43 (NCI-H2030, SW48, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.689×** | -6.0 | 8e-08 | 20/34 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.608×** | -6.0 | 1e-07 | 31/43 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.704×** | -5.7 | 6e-07 | 21/41 (LOX-IMVI, hTERT-HPNE, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.753×** | -4.8 | 7e-05 | 22/43 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.600×** | -4.5 | 3e-04 | 17/31 (LOX-IMVI, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.604×** | -4.4 | 3e-04 | 17/41 (MIA PaCa-2, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.694×** | -4.4 | 4e-04 | 18/43 (LOX-IMVI, C32, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.782×** | -3.9 | 0.003 | 13/43 (RPMI-7951, LoVo, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.803×** | -3.7 | 0.006 | 16/43 (C32, RKO, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.737×** | -3.7 | 0.006 | 15/43 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Rimonabant (drug)]] 5 µM |  | 0.863× | -3.5 | 0.010 | 15/43 (A498, SW1417, …) | rises with dose | position effect removed |
| [[Folic acid (drug)]] 5 µM |  | 0.868× | -3.4 | 0.017 | 9/43 (Hs 766T, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4041. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 97.0 | 18 | 4 (4 ⚠) | [[Budesonide (drug)]] 0.05 µM 4.28× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.236× (z -13.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 51.9 | 19 (1 ⚠) | 2 (2 ⚠) | [[Triamcinolone (drug)]] 5 µM 3.10× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[Hs 766T (line)]] | wt | 29.1 | 19 | 1 | [[Triamcinolone (drug)]] 5 µM 5.40× (z +14.0) | [[TAK-733 (drug)]] 5 µM 0.0584× (z -8.7) |
| [[HS-578T (line)]] | alt | 53.0 | 20 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +13.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 4.50× (z +12.5) | — |
| [[LOX-IMVI (line)]] | wt | 72.4 | 14 | 5 (5 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 2.92× (z +10.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.233× (z -13.7) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 32.5 | 19 | 0 | [[Triamcinolone (drug)]] 5 µM 2.89× (z +12.8) | — |
| [[NCI-H460 (line)]] | wt | 16.9 | 19 (1 ⚠) | 0 | [[Budesonide (drug)]] 0.05 µM 7.90× (z +13.3) | — |
| [[SW 900 (line)]] | alt | 28.6 | 16 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 5.48× (z +11.5) | — |
| [[HOP62 (line)]] | alt | 54.8 | 13 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 4.91× (z +11.4) | — |
| [[Panc 03.27 (line)]] | alt | 26.7 | 11 | 0 | [[Triamcinolone (drug)]] 5 µM 3.54× (z +11.2) | — |
| [[A549 (line)]] | wt | 16.0 | 10 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 6.17× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 16.4 | 8 | 0 | [[Budesonide (drug)]] 0.05 µM 5.37× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 54.5 | 8 | 0 | [[Budesonide (drug)]] 0.5 µM 2.90× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 46.0 | 7 | 0 | [[Triamcinolone (drug)]] 0.5 µM 4.48× (z +9.9) | — |
| [[J82 (line)]] | alt | 86.0 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +12.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 3.18× (z +9.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.353× (z -8.8) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 131 | 3 (2 ⚠) | 2 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.21× (z +10.5) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 2.89× (z +9.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.250× (z -13.1) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 124 | 1 | 4 (3 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 2.83× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.267× (z -11.6) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.0858× (z -11.3) |
| [[KATO III (line)]] | alt | 28.5 | 3 (2 ⚠) | 1 (1 ⚠) | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 3.38× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.145× (z -13.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 136 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[SW480 (line)]] | alt | 21.9 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.118× (z -16.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 47.9 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.121× (z -15.7) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.0989× (z -9.0) |
| [[PANC-1 (line)]] | alt | 21.4 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +9.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.303× (z -10.1) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 28.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +11.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +9.5) | — |
| [[A-427 (line)]] | wt | 26.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +10.4) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[C-33 A (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.172× (z -8.9) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 28.8 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0608× (z -15.9) |
| [[HT-29 (line)]] | alt | 18.4 | 1 (1 ⚠) | 0 | [[Carbidopa (monohydrate) (drug)]] 0.5 µM 4.82× (z +8.5) ⚠ unreliable plate only | — |
| [[SNU-1 (line)]] | wt | 64.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +12.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SW 1271 (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[SW1417 (line)]] | alt | 26.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +9.4) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[AN3 CA (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.01 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.97 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 84.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 62.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.52 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.25 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 91.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.28 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4041), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D3]] | +0.75 | +0.76 / +0.73 | both halves | 7e-06 | STRING 539 |
| [[BCL6]] | +0.73 | +0.67 / +0.73 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[MAOA]] | +0.72 | +0.78 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[IRX3]] | +0.72 | +0.71 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[MT1M]] | +0.71 | +0.69 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[CCND3]] | +0.71 | +0.75 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[MT1E]] | +0.71 | +0.72 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[ZMYND8]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[TLR2]] | +0.70 | +0.71 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[NNMT]] | +0.70 | +0.68 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[SAA1]] | +0.70 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[TNS2]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTS16]] | -0.58 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[PKIA]] | -0.56 | -0.67 / -0.47 | both halves | 2e-05 |  |
| [[ANXA10]] | -0.54 | -0.55 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATOH8]] | B | ATOH8 activity raises KLF9's level | lines that do not express ATOH8 (23) vs lines expressing it (27) | 2.19× lower at baseline in the lines without ATOH8 | 0.011 | ⚠ within organs, on part of the lines; also absent: DZIP1, LINC00839, KCNQ5; maybe low, not absent |
| [[GYPC]] | B | GYPC activity raises KLF9's level | lines that do not express GYPC (35) vs lines expressing it (15) | 2.77× lower at baseline in the lines without GYPC | 0.014 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |
| [[CCL20]] | B | CCL20 activity lowers KLF9's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 1.52× higher at baseline in the lines without CCL20 | 0.092 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[NR3C1]] | B | NR3C1 activity raises KLF9's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 7.0% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[ANXA10]] | C | ANXA10 activity weakens KLF9's drug response | lines that do not express ANXA10 (32) vs lines expressing it (11) | the lines without ANXA10 respond 0.71× as strongly (z diff -1.63); strongest at Betamethasone dipropionate 5 µM: 2.24x vs 3.07x (z diff -2.1) | 0.039 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP; target measured in part of the lines; rests on the correction; artifact flags |
| [[ADAMTSL4]] | C | ADAMTSL4 activity raises KLF9's level | lines that do not express ADAMTSL4 (3) vs lines expressing it (47) | 4.02× lower at baseline in the lines without ADAMTSL4 | 0.058 | ⚠ few lines (3 vs 47); across organs; also absent: BLVRA, ITGA2B, SOAT1; maybe low, not absent |
| [[FOXC2]] | C | FOXC2 activity weakens KLF9's drug response | lines that do not express FOXC2 (30) vs lines expressing it (13) | the lines without FOXC2 respond 0.61× as strongly (z diff -1.20); strongest at Budesonide 0.5 µM: 2.20x vs 3.26x (z diff -1.9) | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT; target measured in part of the lines; rests on the correction |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PHF21A]] | B | KLF9 activity raises PHF21A's level | lines that do not express KLF9 (5) vs lines expressing it (45) | 1.52× lower at baseline in the lines without KLF9 | 0.060 | ⚠ within organs, on part of the lines; also absent: NDC80, WDR54, ADGRB2; maybe low, not absent; its own permutation p |
| [[UGP2]] | B | KLF9 activity lowers UGP2's level | lines that do not express KLF9 (5) vs lines expressing it (45) | 1.41× higher at baseline in the lines without KLF9 | 0.089 | ⚠ within organs, on part of the lines; also absent: NDC80, WDR54, ADGRB2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.819). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.9, 15.1); signed map (16.5, 30.6). **Vector** length 143, 44.4% of its response variance represented; |z| ≥ 3 in 1,692 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Clobetasol propionate (drug)]] 0.05 µM |  | +8.9 | +17.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +8.8 | +16.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +8.7 | +15.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +8.7 | +17.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +8.6 | +14.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.0 | -14.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.7 | -9.4 |
|  | [[EX229 (drug)]] 5 µM |  | -5.8 | -7.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.6 | -8.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.8 | -8.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.7 | -7.2 |

## What is on record

|  |  |
|---|---|
| Name | KLF transcription factor 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.12 — chr9:70,384,604-70,414,657 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously BTEB1 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KLF transcription factors |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 9 pathways, smallest: Positive Regulation of CDH1 Gene Transcription; Regulation of CDH1 Gene Transcription; Regulation of CDH1 Expression and Function |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13886](https://www.uniprot.org/uniprotkb/Q13886) (Krueppel-like factor 9):

> Transcription factor that binds to GC box promoter elements. Selectively activates mRNA synthesis from genes containing tandem repeats of GC boxes but represses genes with a single GC box. Acts as an epidermal circadian transcription factor regulating keratinocyte proliferation.

**Summary**, from NCBI Gene [687](https://www.ncbi.nlm.nih.gov/gene/687):

> The protein encoded by this gene is a transcription factor that binds to GC box elements located in the promoter. Binding of the encoded protein to a single GC box inhibits mRNA expression while binding to tandemly repeated GC box elements activates transcription. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1123](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1123) · Entrez [687](https://www.ncbi.nlm.nih.gov/gene/687) · UniProt [Q13886](https://www.uniprot.org/uniprotkb/Q13886) · Ensembl [ENSG00000119138](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119138)

## Data

Gene col 4041: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4041); `tables/drug_effects.parquet` (86 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4041, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4041]; `tensor/DDL_lfc|DDL_z.npy` [4041]; `embed/gene_vectors.npy` [4041]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4041 or target_col == 4041). Every well: [[KLF9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLF9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
