---
symbol: "MED6"
type: "gene"
col: 5494
ensembl_id: "ENSG00000133997"
name: "mediator complex subunit 6"
location: "14q24.2"
module: 41
arm: "+"
pooled_cpm: 55.93
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 16
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# MED6

*mediator complex subunit 6* — 14q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.87× (z +13.4, q 2e-38, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.384× (z -15.0, q 0e+00, down in 41 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.752× (z -4.6, q 5e-04, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAM20]] (+0.79, fdr 7e-06, ⚠ same locus), [[COX16]] (+0.68, fdr 7e-06), [[SNIP1]] (+0.65, fdr 7e-06), [[VIRMA]] (+0.65, fdr 1e-05); moves opposite to [[NPIPB5]] (-0.59, fdr 1e-05), [[TTL]] (-0.56, fdr 2e-05), [[GATAD2A]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[SAP18]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5494.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.87×** | +13.4 | 2e-38 | 45/49 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **3.86×** | +11.5 | 5e-28 | 44/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +8.7 | 5e-16 | 8/49 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +8.1 | 6e-14 | 42/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +6.5 | 8e-09 | 37/48 (SW480, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +6.5 | 9e-09 | 32/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +5.8 | 6e-07 | 26/48 (SK-MEL-2, RKO, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.75×** | +4.8 | 1e-04 | 21/37 (SW480, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +4.3 | 1e-03 | 25/48 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.30×** | +4.2 | 0.001 | 27/48 (NCI-H1573, A-427, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.004 | 22/48 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.011 | 21/49 (C-33 A, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.033 | 16/48 (A-427, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.052 | 20/47 (SK-MEL-2, SHP-77, …) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.079 | 11/48 (NCI-H2347, A549, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.079 | 22/48 (SW480, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5494.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.384×** | -15.0 | 0e+00 | 41/42 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.404×** | -14.7 | 0e+00 | 47/49 (NCI-H2347, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.746×** | -4.8 | 3e-04 | 25/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.752×** | -4.6 | 5e-04 | 27/48 (CFPAC-1, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.858× | -3.5 | 0.055 | 21/49 (A498, RKO, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.810×** | -3.4 | 0.055 | 20/48 (hTERT-HPNE, HCT15, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.817×** | -3.3 | 0.058 | 20/48 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.817×** | -3.3 | 0.058 | 20/49 (hTERT-HPNE, C32, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.818×** | -3.3 | 0.058 | 18/48 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.818×** | -3.3 | 0.058 | 21/48 (CFPAC-1, SW 900, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.816×** | -3.2 | 0.063 | 19/48 (hTERT-HPNE, H4, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.822×** | -3.2 | 0.063 | 16/48 (NCI-H2030, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.868× | -3.2 | 0.063 | 15/48 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.825×** | -3.1 | 0.065 | 18/49 (LOX-IMVI, CFPAC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.825×** | -3.1 | 0.065 | 19/48 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.826×** | -3.1 | 0.065 | 19/48 (SW1417, SW 900, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.833×** | -3.0 | 0.088 | 11/48 (SW48, HT-29, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.834× | -3.0 | 0.091 | 16/48 (COLO 205, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5494. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 62.7 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -16.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 98.9 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.86× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 92.1 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -16.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 34.8 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.70× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 46.5 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.68× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.0506× (z -27.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 76.4 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.45× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.151× (z -17.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 72.4 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.98× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -15.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 36.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.418× (z -8.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 54.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -11.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 68.4 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.50× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -8.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 69.2 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.180× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 45.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.87× (z +10.2) | — |
| [[LS 180 (line)]] | wt | 56.2 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 7.84× (z +8.8) | — |
| [[NCI-H1573 (line)]] | alt | 92.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 62.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.357× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 91.7 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -13.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 67.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -9.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 70.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -14.4) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 73.3 | 0 | 2 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0807× (z -9.9) ⚠ toxic · without an alert: [[Allantoin (drug)]] 0.5 µM 0.0838× (z -9.8) |
| [[SW 900 (line)]] | alt | 89.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -11.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 67.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -13.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 54.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0599× (z -24.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 45.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0927× (z -16.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 81.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0457× (z -16.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 83.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -9.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 53.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -9.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 55.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -8.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 40.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -10.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 41.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.86× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 45.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.399× (z -10.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 46.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.08× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 57.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -12.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 66.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 58.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5494), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM20]] | +0.79 | +0.79 / +0.76 | both halves | 7e-06 | ⚠ same locus (46.2 kb, same strand: neighbours can correlate without regulation) |
| [[COX16]] | +0.68 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[SNIP1]] | +0.65 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[VIRMA]] | +0.65 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[ISY1]] | +0.65 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[TVP23B]] | +0.64 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[ADAM20P1]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ING4]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[CIR1]] | +0.62 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[AKAP10]] | +0.62 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[SCNM1]] | +0.62 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[PPIL4]] | +0.61 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[TFIP11]] | +0.61 | +0.62 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPIPB5]] | -0.59 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[TTL]] | -0.56 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[GATAD2A]] | -0.56 | -0.55 / -0.47 | both halves | 2e-05 | pathway: Adipogenesis |
| [[WWC2]] | -0.55 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[NPIPB4]] | -0.55 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[PKP4]] | -0.54 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[TJP1]] | -0.54 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[ANAPC7]] | -0.54 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[SRPK1]] | -0.54 | -0.52 / -0.49 | both halves | 2e-05 |  |
| [[PSEN2]] | -0.54 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[REEP3]] | -0.53 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[ACER3]] | -0.53 | -0.52 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAP18]] | C | MED6's natural level weakens SAP18's drug response | MED6's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.71, reverse -0.06; direction clear | 0.006 | ⚠ tissue can mimic it; precision caveat |
| [[BCAS2]] | C | MED6's natural level weakens BCAS2's drug response | MED6's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.16; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.606). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-2.7, -16.6); signed map (-4.9, -6.0). **Vector** length 84.1, 21.8% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.2 | +6.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +1.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +13.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +11.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | +2.9 | -3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | -1.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | -1.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.7 | -3.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -0.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.2 | +3.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.9 | -1.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.0 | -1.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.7 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | +1.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.9 | -0.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.2 — chr14:70,581,257-70,600,690 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NY-REN-28 |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 13 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Epigenetic regulation of adipogenesis genes by MLL3 and MLL4 complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [O75586](https://www.uniprot.org/uniprotkb/O75586) (Mediator of RNA polymerase II transcription subunit 6):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [10001](https://www.ncbi.nlm.nih.gov/gene/10001):

> Enables transcription coactivator activity and transcription coactivator binding activity. Acts upstream of or within positive regulation of transcription by RNA polymerase II. Located in nucleoplasm. Part of mediator complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19970](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19970) · Entrez [10001](https://www.ncbi.nlm.nih.gov/gene/10001) · UniProt [O75586](https://www.uniprot.org/uniprotkb/O75586) · Ensembl [ENSG00000133997](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133997)

## Data

Gene col 5494: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5494); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5494, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5494]; `tensor/DDL_lfc|DDL_z.npy` [5494]; `embed/gene_vectors.npy` [5494]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5494 or target_col == 5494). Every well: [[MED6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
