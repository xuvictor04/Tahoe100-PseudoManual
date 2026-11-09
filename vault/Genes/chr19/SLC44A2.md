---
symbol: "SLC44A2"
type: "gene"
col: 4968
ensembl_id: "ENSG00000129353"
name: "solute carrier family 44 member 2 (CTL2 blood group)"
location: "19p13.2"
module: 94
arm: "+"
pooled_cpm: 22.94
n_lines_expressing: 46
n_dd_up: 19
n_dd_down: 20
n_dd_up_clean: 14
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 5
direction_downstream: 8
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# SLC44A2

*solute carrier family 44 member 2 (CTL2 blood group)* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 3.78× (z +29.3, q 0e+00, up in 39 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.599× (z -11.2, q 2e-26, down in 32 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP15]] (+0.68, fdr 1e-05), [[SLC2A4RG]] (+0.68, fdr 1e-05), [[TRPM4]] (+0.68, fdr 1e-05); moves opposite to [[ANKMY1]] (-0.57, fdr 3e-05), [[KCNJ14]] (-0.57, fdr 3e-05), [[FAM120B]] (-0.55, fdr 1e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ZNF433]] → it (grade B ⚠); 8 go from it, the strongest it → [[ZNF433]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4968.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **3.78×** | +29.3 | 0e+00 | 39/44 (LoVo, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **3.23×** | +18.3 | 0e+00 | 39/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **3.22×** | +18.3 | 0e+00 | 39/44 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **2.37×** | +13.5 | 2e-39 | 36/44 (LoVo, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.84×** | +9.2 | 6e-18 | 28/43 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +8.4 | 6e-15 | 21/36 (J82, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.5 | 5e-09 | 12/23 (J82, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +6.2 | 5e-08 | 19/32 (HEC-1-A, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.8 | 1e-04 | 18/44 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +4.7 | 1e-04 | 14/44 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adenine (drug)]] 5 µM |  | **1.21×** | +4.3 | 8e-04 | 15/44 (RPMI-7951, A-172, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.005 | 13/44 (SW480, SNU-423, …) | top dose only | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.020 | 13/44 (SW480, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.25×** | +3.5 | 0.020 | 13/41 (SNU-423, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.26×** | +3.5 | 0.020 | 14/44 (C32, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.025 | 10/43 (SW480, C32, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.25×** | +3.4 | 0.025 | 12/44 (SW480, C32, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.028 | 10/44 (SK-MEL-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.2 | 0.048 | 7/44 (A-172, HOP62, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.068 | 16/44 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4968.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.599×** | -11.2 | 2e-26 | 32/42 (MIA PaCa-2, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.596×** | -8.0 | 2e-13 | 35/44 (AN3 CA, HEC-1-A, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.596×** | -8.0 | 2e-13 | 31/44 (A-172, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.608×** | -7.7 | 1e-12 | 27/44 (SNU-423, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.608×** | -7.7 | 1e-12 | 24/42 (COLO 205, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.647×** | -6.7 | 2e-09 | 20/41 (RPMI-7951, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.654×** | -6.6 | 4e-09 | 25/44 (BT-474, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.653×** | -6.2 | 3e-08 | 30/44 (hTERT-HPNE, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.697×** | -5.6 | 1e-06 | 23/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.704×** | -5.4 | 3e-06 | 22/44 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.704×** | -5.2 | 9e-06 | 18/41 (RPMI-7951, SNU-423, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.723×** | -4.8 | 6e-05 | 24/42 (SK-MEL-2, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.779×** | -3.9 | 0.005 | 19/44 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.783×** | -3.6 | 0.012 | 13/43 (C-33 A, SW 900, …) | top dose only | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.797×** | -3.5 | 0.017 | 10/44 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[Gefitinib (drug)]] 5 µM |  | **0.811×** | -3.2 | 0.042 | 8/44 (NCI-H460, PANC-1, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.821×** | -3.0 | 0.075 | 12/43 (SNU-1, NCI-H460, …) | top dose only | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.816×** | -3.0 | 0.079 | 13/44 (MIA PaCa-2, NCI-H460, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.817×** | -3.0 | 0.080 | 7/43 (H4, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4968. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 32.0 | 3 | 3 (2 ⚠) | [[Selinexor (drug)]] 5 µM 4.64× (z +13.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.183× (z -10.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.207× (z -10.0) |
| [[SW480 (line)]] | alt | 14.6 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.26× (z +16.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Selinexor (drug)]] 5 µM 5.07× (z +15.9) | — |
| [[A-172 (line)]] | wt | 61.2 | 3 | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.60× (z +17.1) | [[Digitoxin (drug)]] 5 µM 0.382× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.391× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 31.0 | 3 | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 4.45× (z +14.3) | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -18.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -17.2) |
| [[COLO 205 (line)]] | alt | 14.7 | 1 | 3 (2 ⚠) | [[Selinexor (drug)]] 5 µM 4.46× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.102× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 41.5 | 4 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.28× (z +15.4) | — |
| [[LoVo (line)]] | wt | 9.02 | 4 | 0 | [[Selinexor (drug)]] 5 µM 8.31× (z +17.9) | — |
| [[SW1417 (line)]] | alt | 39.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.97× (z +19.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.20× (z +10.8) | — |
| [[BT-474 (line)]] | alt | 64.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -9.5) |
| [[HOP62 (line)]] | alt | 16.8 | 3 | 0 | [[Selinexor (drug)]] 5 µM 4.13× (z +12.7) | — |
| [[NCI-H460 (line)]] | wt | 7.14 | 3 | 0 | [[Selinexor (drug)]] 5 µM 7.64× (z +15.0) | — |
| [[PANC-1 (line)]] | alt | 14.1 | 3 | 0 | [[Selinexor (drug)]] 5 µM 4.91× (z +16.2) | — |
| [[SW 900 (line)]] | alt | 18.2 | 1 | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 3.75× (z +9.5) | [[Docetaxel (drug)]] 0.05 µM 0.112× (z -11.1) ⚠ transcription drop |
| [[C32 (line)]] | wt | 28.0 | 1 | 1 | [[Selinexor (drug)]] 5 µM 2.92× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 21.6 | 2 | 0 | [[Selinexor (drug)]] 5 µM 4.11× (z +12.8) | — |
| [[HT-29 (line)]] | alt | 16.3 | 2 | 0 | [[Selinexor (drug)]] 5 µM 4.52× (z +13.3) | — |
| [[J82 (line)]] | alt | 64.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +8.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 12.4 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 4.57× (z +11.9) | — |
| [[LS 180 (line)]] | wt | 13.9 | 1 | 1 | [[Selinexor (drug)]] 5 µM 4.17× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 14.2 | 1 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.06× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 62.5 | 2 | 0 | [[Selinexor (drug)]] 5 µM 2.25× (z +12.2) | — |
| [[Panc 03.27 (line)]] | alt | 72.4 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 15.2 | 1 | 1 | [[Selinexor (drug)]] 5 µM 3.74× (z +9.3) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0933× (z -11.3) |
| [[SNU-423 (line)]] | alt | 17.7 | 1 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.26× (z +10.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.215× (z -9.2) ⚠ toxic |
| [[A498 (line)]] | wt | 20.9 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.45× (z +12.0) | — |
| [[AN3 CA (line)]] | alt | 22.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0720× (z -9.2) |
| [[H4 (line)]] | wt | 14.1 | 1 | 0 | [[Selinexor (drug)]] 5 µM 7.60× (z +11.0) | — |
| [[HCT15 (line)]] | alt | 21.7 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.98× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 33.4 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.76× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 36.1 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.73× (z +12.3) | — |
| [[NCI-H1573 (line)]] | alt | 8.15 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.49× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 9.37 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.57× (z +9.0) | — |
| [[RKO (line)]] | wt | 9.55 | 1 | 0 | [[Selinexor (drug)]] 5 µM 5.47× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 16.5 | 1 | 0 | [[Selinexor (drug)]] 5 µM 4.15× (z +10.1) | — |
| [[SW48 (line)]] | wt | 24.9 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.52× (z +8.9) | — |
| [[A-427 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.04 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.63 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4968), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP15]] | +0.68 | +0.50 / +0.78 | both halves | 1e-05 |  |
| [[SLC2A4RG]] | +0.68 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[TRPM4]] | +0.68 | +0.50 / +0.74 | both halves | 1e-05 |  |
| [[XPO1]] | +0.64 | +0.61 / +0.76 | both halves | 7e-06 |  |
| [[TRAPPC11]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[STK32A]] | +0.61 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[NGFR]] | +0.61 | +0.31 / +0.71 | both halves | 2e-04 |  |
| [[CAPN5]] | +0.61 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[GSN]] | +0.61 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[GPCPD1]] | +0.60 | +0.41 / +0.69 | both halves | 4e-05 | pathway: Glycerophospholipid biosynthesis |
| [[GNG2]] | +0.60 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[ZNF44]] | +0.60 | +0.52 / +0.72 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKMY1]] | -0.57 | -0.43 / -0.64 | both halves | 3e-05 |  |
| [[KCNJ14]] | -0.57 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[FAM120B]] | -0.55 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[MIATNB]] | -0.53 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[GOSR2]] | -0.53 | -0.38 / -0.61 | both halves | 6e-05 |  |
| [[CA3]] | -0.53 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[TMEM11-DT]] | -0.52 | -0.36 / -0.62 | both halves | 1e-04 |  |
| [[PSMD6-AS2]] | -0.52 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[KLHL29]] | -0.50 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[WNT2B]] | -0.50 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[LRP2BP-AS1]] | -0.50 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[DNHD1]] | -0.49 | -0.31 / -0.55 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF433]] | B | ZNF433 activity raises SLC44A2's level | lines that do not express ZNF433 (8) vs lines expressing it (42) | 2.26× lower at baseline in the lines without ZNF433 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF563, ZNF442 |
| [[ZNF682]] | B | ZNF682 activity raises SLC44A2's level | lines that do not express ZNF682 (20) vs lines expressing it (30) | 1.96× lower at baseline in the lines without ZNF682 | 0.034 | ⚠ within organs, on part of the lines; also absent: ZNF93, ZNF90, SCUBE3 |
| [[NGFR]] | B | NGFR activity raises SLC44A2's level | lines that do not express NGFR (19) vs lines expressing it (31) | 2.02× lower at baseline in the lines without NGFR | 0.041 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, GNG11 |
| [[ZNF442]] | B | ZNF442 activity raises SLC44A2's level | lines that do not express ZNF442 (7) vs lines expressing it (43) | 1.80× lower at baseline in the lines without ZNF442 | 0.078 | ⚠ within organs, on part of the lines; also absent: ZNF563, ENSG00000286098, ENSG00000268870 |
| [[CNTNAP1]] | C | CNTNAP1 activity raises SLC44A2's level | lines that do not express CNTNAP1 (4) vs lines expressing it (46) | 2.25× lower at baseline in the lines without CNTNAP1 | 0.093 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZCCHC24, KIF17, SLC29A4 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF433]] | C | SLC44A2 activity raises ZNF433's level | lines that do not express SLC44A2 (4) vs lines expressing it (46) | 3.14× lower at baseline in the lines without SLC44A2 | 0.021 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC45, CLSPN, AURKB; maybe low, not absent |
| [[MRS2]] | C | SLC44A2 activity raises MRS2's level | lines that do not express SLC44A2 (4) vs lines expressing it (46) | 1.73× lower at baseline in the lines without SLC44A2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC45, CLSPN, AURKB; maybe low, not absent |
| [[TMEM14A]] | C | SLC44A2 activity raises TMEM14A's level | lines that do not express SLC44A2 (4) vs lines expressing it (46) | 2.35× lower at baseline in the lines without SLC44A2 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC45, CLSPN, AURKB; maybe low, not absent |
| [[MRPL40]] | C | SLC44A2 activity raises MRPL40's level | lines that do not express SLC44A2 (4) vs lines expressing it (46) | 1.49× lower at baseline in the lines without SLC44A2 | 0.068 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC45, CLSPN, AURKB; maybe low, not absent |
| [[ZMYM3]] | C | SLC44A2 activity raises ZMYM3's level | lines that do not express SLC44A2 (4) vs lines expressing it (46) | 1.59× lower at baseline in the lines without SLC44A2 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC45, CLSPN, AURKB; maybe low, not absent |
| [[ZNF442]] | C | SLC44A2 activity raises ZNF442's level | lines that do not express SLC44A2 (4) vs lines expressing it (46) | 2.15× lower at baseline in the lines without SLC44A2 | 0.075 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC45, CLSPN, AURKB; maybe low, not absent |
| [[EHMT2]] | C | SLC44A2 activity raises EHMT2's level | lines that do not express SLC44A2 (4) vs lines expressing it (46) | 1.96× lower at baseline in the lines without SLC44A2 | 0.083 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC45, CLSPN, AURKB; maybe low, not absent |
| [[NUDT16]] | C | SLC44A2 activity raises NUDT16's level | lines that do not express SLC44A2 (4) vs lines expressing it (46) | 1.70× lower at baseline in the lines without SLC44A2 | 0.097 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC45, CLSPN, AURKB; maybe low, not absent |

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.669). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.5, 24.8); signed map (14.6, -16.1). **Vector** length 114, 28.4% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +17.0 | +29.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +11.7 | +18.3 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +8.4 | +18.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.9 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +6.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +5.7 | +13.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +0.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.5 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -11.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -8.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.9 | -5.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.9 | -8.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -4.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -3.3 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -3.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 44 member 2 (CTL2 blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,602,457-10,644,557 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HNA-3, CTL2 |
| Gene groups (HGNC) | Blood group antigens; Solute carrier family 44; Human neutrophil antigens |
| Reactome | 12 pathways, smallest: SLC-mediated bile acid transport; Choline catabolism; SLC-mediated transport of organic anions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWA5](https://www.uniprot.org/uniprotkb/Q8IWA5) (Choline transporter-like protein 2):

> [Isoform 1]: Choline/H+ antiporter, mainly in mitochondria. Also acts as a low-affinity ethanolamine/H+ antiporter, regulating the supply of extracellular ethanolamine (Etn) for the CDP-Etn pathway, redistribute intracellular Etn and balance the CDP-Cho and CDP-Etn arms of the Kennedy pathway.; [Isoform 3]: Does not exhibit choline transporter activity.

**Summary**, from NCBI Gene [57153](https://www.ncbi.nlm.nih.gov/gene/57153):

> Enables choline transmembrane transporter activity and ethanolamine transmembrane transporter activity. Involved in choline transport; ethanolamine transport; and transmembrane transport. Located in mitochondrial outer membrane and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17292](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17292) · Entrez [57153](https://www.ncbi.nlm.nih.gov/gene/57153) · UniProt [Q8IWA5](https://www.uniprot.org/uniprotkb/Q8IWA5) · Ensembl [ENSG00000129353](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129353)

## Data

Gene col 4968: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4968); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4968, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4968]; `tensor/DDL_lfc|DDL_z.npy` [4968]; `embed/gene_vectors.npy` [4968]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4968 or target_col == 4968). Every well: [[SLC44A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC44A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
