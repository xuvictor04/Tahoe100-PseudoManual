---
symbol: "SH3KBP1"
type: "gene"
col: 7138
ensembl_id: "ENSG00000147010"
name: "SH3 domain containing kinase binding protein 1"
location: "Xp22.12"
module: 136
arm: "+"
pooled_cpm: 240.46
n_lines_expressing: 48
n_dd_up: 18
n_dd_down: 20
n_dd_up_clean: 13
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# SH3KBP1

*SH3 domain containing kinase binding protein 1* — Xp22.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 1.49× (z +9.4, q 3e-18, up in 28 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.501× (z -23.0, q 0e+00, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP1B]] (+0.66, fdr 7e-06), [[GRB10]] (+0.65, fdr 7e-06), [[KIF21B]] (+0.62, fdr 1e-05); moves opposite to [[COQ9]] (-0.64, fdr 7e-06), [[YY1AP1]] (-0.58, fdr 2e-05), [[CSTF1]] (-0.56, fdr 1e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[S100A16]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7138.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.49×** | +9.4 | 3e-18 | 28/46 (KATO III, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.09×** | +9.0 | 4e-17 | 37/43 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +8.9 | 8e-17 | 29/46 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +7.6 | 6e-12 | 33/46 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.34×** | +6.9 | 6e-10 | 28/47 (RPMI-7951, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +6.8 | 1e-09 | 26/42 (C-33 A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Artesunate (drug)]] 5 µM |  | **1.22×** | +6.5 | 9e-09 | 23/46 (SW480, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +6.4 | 1e-08 | 27/46 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +6.3 | 2e-08 | 25/45 (COLO 205, HCT15, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.30×** | +5.6 | 1e-06 | 22/43 (SNU-423, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.27×** | +5.5 | 3e-06 | 21/46 (NCI-H2030, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.25×** | +5.2 | 1e-05 | 22/46 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.40×** | +5.0 | 2e-05 | 23/47 (LoVo, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +5.0 | 2e-05 | 15/46 (BT-474, LoVo, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.25×** | +5.0 | 2e-05 | 23/45 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.24×** | +4.9 | 4e-05 | 22/47 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +4.6 | 1e-04 | 24/46 (NCI-H1573, SW480, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.21×** | +4.4 | 4e-04 | 18/46 (SW480, KATO III, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | 1.19× | +4.1 | 0.001 | 19/46 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Thymol (drug)]] 5 µM |  | 1.13× | +3.9 | 0.002 | 6/46 (HS-578T, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7138.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.501×** | -23.0 | 0e+00 | 39/46 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.487×** | -16.7 | 0e+00 | 43/46 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.625×** | -15.7 | 0e+00 | 31/47 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.542×** | -13.8 | 2e-41 | 39/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.628×** | -10.9 | 8e-26 | 37/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.631×** | -10.4 | 2e-23 | 35/45 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.682×** | -9.0 | 1e-17 | 35/46 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.771×** | -8.7 | 3e-16 | 28/46 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.505×** | -8.4 | 3e-15 | 40/47 (KATO III, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.711×** | -8.0 | 5e-14 | 33/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.729×** | -7.5 | 4e-12 | 30/46 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.742×** | -7.0 | 1e-10 | 32/46 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.758×** | -6.3 | 2e-08 | 27/46 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.780×** | -5.9 | 2e-07 | 28/46 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.640×** | -5.5 | 2e-06 | 29/46 (NCI-H2347, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.821×** | -4.7 | 1e-04 | 22/45 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.810×** | -4.6 | 1e-04 | 20/46 (SK-MEL-2, NCI-H2347, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7138. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 718 | 2 (1 ⚠) | 16 (7 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.35× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.08× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -24.4) |
| [[SK-MEL-2 (line)]] | alt | 366 | 0 | 18 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -19.9) |
| [[PANC-1 (line)]] | alt | 243 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -26.7) |
| [[NCI-H2347 (line)]] | alt | 583 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -25.1) |
| [[KATO III (line)]] | alt | 249 | 4 (1 ⚠) | 5 | [[Ixazomib citrate (drug)]] 5 µM 3.16× (z +17.0) | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -21.9) |
| [[SW480 (line)]] | alt | 222 | 3 (1 ⚠) | 6 | [[Bortezomib (drug)]] 0.05 µM 2.08× (z +10.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.385× (z -14.8) |
| [[AsPC-1 (line)]] | alt | 160 | 4 | 3 | [[Bortezomib (drug)]] 0.05 µM 3.37× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -24.0) |
| [[HEC-1-A (line)]] | alt | 322 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -16.2) |
| [[HT-29 (line)]] | alt | 261 | 4 | 3 | [[Ixazomib citrate (drug)]] 5 µM 3.51× (z +15.5) | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -13.5) |
| [[A498 (line)]] | wt | 105 | 4 (1 ⚠) | 2 | [[Auranofin (drug)]] 5 µM 2.63× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 220 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -23.8) |
| [[A-172 (line)]] | wt | 430 | 1 | 4 | [[Ixazomib citrate (drug)]] 0.5 µM 2.28× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -17.5) |
| [[HOP62 (line)]] | alt | 205 | 3 | 2 | [[Auranofin (drug)]] 5 µM 3.01× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -12.4) |
| [[LoVo (line)]] | wt | 162 | 4 (1 ⚠) | 1 | [[Bortezomib (drug)]] 0.05 µM 2.99× (z +17.3) | [[Harringtonine (drug)]] 0.5 µM 0.602× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 139 | 1 | 4 | [[Auranofin (drug)]] 5 µM 2.91× (z +13.0) | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -13.5) |
| [[BT-474 (line)]] | alt | 64.7 | 2 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.57× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -12.2) |
| [[C32 (line)]] | wt | 209 | 2 | 2 | [[Auranofin (drug)]] 5 µM 2.07× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -13.7) |
| [[CFPAC-1 (line)]] | alt | 387 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -17.8) |
| [[HS-578T (line)]] | alt | 205 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -16.4) |
| [[LS 180 (line)]] | wt | 156 | 4 | 0 | [[Bortezomib (drug)]] 0.05 µM 1.97× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 421 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -18.4) |
| [[RKO (line)]] | wt | 102 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.291× (z -13.0) |
| [[SW1417 (line)]] | alt | 290 | 1 | 3 | [[Ixazomib citrate (drug)]] 5 µM 1.66× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -17.7) |
| [[A549 (line)]] | wt | 406 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -13.7) |
| [[H4 (line)]] | wt | 302 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -11.4) |
| [[HepG2_C3A (line)]] | wt | 217 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -17.6) |
| [[J82 (line)]] | alt | 116 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.40× (z +11.4) | — |
| [[NCI-H1573 (line)]] | alt | 99.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -12.8) |
| [[SW 1271 (line)]] | alt | 424 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -14.7) |
| [[SW 900 (line)]] | alt | 222 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -14.2) |
| [[COLO 205 (line)]] | alt | 141 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 3.08× (z +9.7) ⚠ toxic | [[Homoharringtonine (drug)]] 0.5 µM 0.292× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 84.4 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.371× (z -10.5) |
| [[SNU-423 (line)]] | alt | 140 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.17× (z +12.2) | — |
| [[A-427 (line)]] | wt | 151 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -17.1) |
| [[C-33 A (line)]] | alt | 81.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.73× (z +10.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 100 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 251 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.605× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 188 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.21× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 111 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.380× (z -8.7) |
| [[AN3 CA (line)]] | alt | 105 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 91.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.0 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 173 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 258 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 100 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 212 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7138), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP1B]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[GRB10]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[KIF21B]] | +0.62 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[PSME4]] | +0.61 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[HSP90AA1]] | +0.60 | +0.49 / +0.56 | both halves | 1e-05 | pathway: Bacterial Infection Pathways |
| [[EXOC6B]] | +0.60 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[LRRFIP1]] | +0.59 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[GPAT3]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[ASPH]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[RTN4]] | +0.58 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[AAK1]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 | pathway: Cargo recognition for clathrin-mediated endocytosis |
| [[ATP13A2]] | +0.58 | +0.60 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COQ9]] | -0.64 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[YY1AP1]] | -0.58 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[CSTF1]] | -0.56 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[LATS1]] | -0.56 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[RNF146]] | -0.54 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[TTC32]] | -0.53 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[SLC39A1]] | -0.53 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[NFYB]] | -0.52 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[UQCRFS1]] | -0.51 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[UBAP2L]] | -0.50 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[PHC3]] | -0.50 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[MIR181A2HG]] | -0.50 | -0.47 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[S100A16]] | B | S100A16 activity raises SH3KBP1's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 1.98× lower at baseline in the lines without S100A16 | 0.020 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[ADAM19]] | B | ADAM19 activity raises SH3KBP1's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 1.74× lower at baseline in the lines without ADAM19 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[CARD11]] | B | CARD11 activity raises SH3KBP1's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 1.58× lower at baseline in the lines without CARD11 | 0.098 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.580). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.8, 4.3); signed map (-5.7, 49.9). **Vector** length 136, 44.2% of its response variance represented; |z| ≥ 3 in 1,824 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.7 | +8.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.4 | +9.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.6 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.8 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.6 | +7.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.5 | +5.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.8 | +5.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.5 | -10.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.2 | -9.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.8 | -8.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.0 | -7.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.2 | -13.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.1 | -2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.0 | -2.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.8 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | SH3 domain containing kinase binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.12 — chrX:19,533,977-19,887,600 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CIN85 |
| Gene groups (HGNC) | SH3 domain containing |
| Reactome | 21 pathways, smallest: Reelin signalling pathway; InlB-mediated entry of Listeria monocytogenes into host cell; Listeria monocytogenes entry into host cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96B97](https://www.uniprot.org/uniprotkb/Q96B97) (SH3 domain-containing kinase-binding protein 1):

> Adapter protein involved in regulating diverse signal transduction pathways. Involved in the regulation of endocytosis and lysosomal degradation of ligand-induced receptor tyrosine kinases, including EGFR and MET/hepatocyte growth factor receptor, through an association with CBL and endophilins. The association with CBL, and thus the receptor internalization, may be inhibited by an interaction with PDCD6IP and/or SPRY2. Involved in regulation of ligand-dependent endocytosis of the IgE receptor. …

**Summary**, from NCBI Gene [30011](https://www.ncbi.nlm.nih.gov/gene/30011):

> This gene encodes an adapter protein that contains one or more N-terminal Src homology domains, a proline rich region and a C-terminal coiled-coil domain. The encoded protein facilitates protein-protein interactions and has been implicated in numerous cellular processes including apoptosis, cytoskeletal rearrangement, cell adhesion and in the regulation of clathrin-dependent endocytosis. Alternate splicing results in multiple transcript variants encoding distinct isoforms. [provided by RefSeq, …

**Accessions** — [HGNC:13867](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13867) · Entrez [30011](https://www.ncbi.nlm.nih.gov/gene/30011) · UniProt [Q96B97](https://www.uniprot.org/uniprotkb/Q96B97) · Ensembl [ENSG00000147010](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147010)

## Data

Gene col 7138: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7138); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7138, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7138]; `tensor/DDL_lfc|DDL_z.npy` [7138]; `embed/gene_vectors.npy` [7138]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7138 or target_col == 7138). Every well: [[SH3KBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3KBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
