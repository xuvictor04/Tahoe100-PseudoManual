---
symbol: "PRPF4"
type: "gene"
col: 5928
ensembl_id: "ENSG00000136875"
name: "pre-mRNA splicing tri-snRNP complex factor PRPF4"
location: "9q32"
module: 11
arm: "+"
pooled_cpm: 34.6
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 2
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# PRPF4

*pre-mRNA splicing tri-snRNP complex factor PRPF4* — 9q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.00× (z +22.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.713× (z -6.4, q 8e-08, down in 23 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Posaconazole (drug)]] 5 µM: 0.831× (z -3.7, q 0.046, down in 8 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H460 0.265×, H4 0.136×, BT-474 0.140×, LOX-IMVI 0.263×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HEC-1-A 0.159×, SHP-77 0.295×, C32 0.146×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 0.184×, RKO 0.220×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Belumosudil (mesylate) (drug)]] 5 µM in 1 line (H4 0.0745×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRMT10C]] (+0.66, fdr 7e-06), [[CEBPZ]] (+0.66, fdr 7e-06), [[ZNF146]] (+0.66, fdr 7e-06); moves opposite to [[NAP1L1]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GAS6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[NUP214]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5928.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.00×** | +22.3 | 0e+00 | 48/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.66×** | +19.9 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.11×** | +15.1 | 0e+00 | 45/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.62×** | +13.7 | 3e-40 | 43/48 (COLO 205, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.25×** | +12.5 | 7e-34 | 39/48 (SK-MEL-2, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.80×** | +11.9 | 7e-31 | 41/48 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +11.2 | 2e-27 | 36/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.67×** | +10.4 | 2e-23 | 41/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.62×** | +9.4 | 4e-19 | 35/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.48×** | +7.6 | 2e-12 | 31/47 (PANC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +7.0 | 2e-10 | 31/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.27×** | +6.7 | 9e-10 | 23/48 (NCI-H1792, Hs 766T, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.41×** | +6.6 | 2e-09 | 26/47 (SW1417, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +6.3 | 1e-08 | 23/48 (HEC-1-A, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.36×** | +6.3 | 1e-08 | 30/47 (J82, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +5.7 | 4e-07 | 21/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +5.1 | 1e-05 | 22/48 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.5 | 2e-04 | 15/48 (Panc 03.27, MIA PaCa-2, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.001 | 15/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.005 | 14/47 (MIA PaCa-2, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.22×** | +3.7 | 0.005 | 9/48 (NCI-H460, RKO, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.011 | 14/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5928.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H460 0.265×, H4 0.136×, BT-474 0.140×, LOX-IMVI 0.263×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HEC-1-A 0.159×, SHP-77 0.295×, C32 0.146×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 0.184×, RKO 0.220×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Belumosudil (mesylate) (drug)]] 5 µM in 1 line (H4 0.0745×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.713×** | -6.4 | 8e-08 | 23/43 (HEC-1-A, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Posaconazole (drug)]] 5 µM |  | **0.831×** | -3.7 | 0.046 | 8/48 (PANC-1, AN3 CA, …) | top dose only | plate-row cell shift |
| [[Cobimetinib (drug)]] 5 µM |  | 0.834× | -3.6 | 0.046 | 14/47 (RPMI-7951, RKO, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.885× | -3.6 | 0.046 | 11/49 (PANC-1, A549, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.858× | -3.2 | 0.17 | 11/48 (NCI-H460, Panc 03.27, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.884× | -3.1 | 0.17 | 12/48 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.901× | -3.1 | 0.17 | 7/48 (RKO, NCI-H23, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.863× | -3.0 | 0.17 | 16/47 (NCI-H23, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5928. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.8 | 6 (4 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.08× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 40.8 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.96× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -17.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 43.7 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.38× (z +14.6) | — |
| [[A549 (line)]] | wt | 35.8 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.88× (z +12.2) | — |
| [[COLO 205 (line)]] | alt | 30.9 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.23× (z +9.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.01× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 31.4 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.10× (z +11.1) | — |
| [[KATO III (line)]] | alt | 53.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.86× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.291× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 42.3 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.27× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 21.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.59× (z +10.5) | — |
| [[RKO (line)]] | wt | 60.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.08× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 25.7 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.33× (z +11.6) | — |
| [[A498 (line)]] | wt | 60.0 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.58× (z +11.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.452× (z -9.1) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 40.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Belumosudil (mesylate) (drug)]] 5 µM 0.0745× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 24.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.31× (z +8.5) ⚠ cell-cycle shift, explains ~31% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.214× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[LoVo (line)]] | wt | 33.1 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.17× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 28.1 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.27× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.263× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 22.7 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.95× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 30.3 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.14× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 90.9 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.40× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -12.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 52.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 21.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.146× (z -11.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 30.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.99× (z +10.0) | — |
| [[HS-578T (line)]] | alt | 22.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.48× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 23.2 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.37× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 19.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.02× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 35.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.35× (z +10.3) | — |
| [[SNU-423 (line)]] | alt | 26.7 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.35× (z +8.6) | — |
| [[SW 1271 (line)]] | alt | 50.3 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0589× (z -10.0) ⚠ cell-cycle shift, explains ~93% of this change |
| [[SW1417 (line)]] | alt | 43.4 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.84× (z +10.7) | — |
| [[A-427 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5928), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT10C]] | +0.66 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[CEBPZ]] | +0.66 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[ZNF146]] | +0.66 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[INTS5]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[GEMIN4]] | +0.64 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[TBRG4]] | +0.64 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[NOL11]] | +0.64 | +0.66 / +0.66 | both halves | 7e-06 | STRING 433 |
| [[SNRPE]] | +0.64 | +0.64 / +0.60 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 999 |
| [[TTI1]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[EXOSC2]] | +0.63 | +0.62 / +0.65 | both halves | 7e-06 | STRING 551 |
| [[YRDC]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[ISG20L2]] | +0.63 | +0.54 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAP1L1]] | -0.56 | -0.52 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GAS6]] | B | GAS6 activity raises PRPF4's level | lines that do not express GAS6 (8) vs lines expressing it (42) | 1.37× lower at baseline in the lines without GAS6 | 0.068 | ⚠ within organs, on part of the lines |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUP214]] | C | PRPF4's natural level strengthens NUP214's drug response | PRPF4's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.50; direction not clear | 0.064 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.416). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-43.1, -0.1); signed map (-3.4, -21.5). **Vector** length 97.5, 24.6% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +6.8 | +12.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.6 | +13.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +11.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.1 | +22.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.1 | +10.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +5.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.5 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +4.5 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -1.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.0 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.9 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | pre-mRNA splicing tri-snRNP complex factor PRPF4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q32 — chr9:113,275,642-113,294,009 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Prp4p, HPRP4, HPRP4P, PRP4, SNRNP60 |
| Gene groups (HGNC) | WD repeat domain containing; U4/U6 small nuclear ribonucleoprotein particle |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [O43172](https://www.uniprot.org/uniprotkb/O43172) (U4/U6 small nuclear ribonucleoprotein Prp4):

> Plays a role in pre-mRNA splicing as component of the U4/U6-U5 tri-snRNP complex that is involved in spliceosome assembly, and as component of the precatalytic spliceosome (spliceosome B complex).

**Summary**, from NCBI Gene [9128](https://www.ncbi.nlm.nih.gov/gene/9128):

> The protein encoded by this gene is part of a heteromeric complex that binds U4, U5, and U6 small nuclear RNAs and is involved in pre-mRNA splicing. The encoded protein also is a mitotic checkpoint protein and a regulator of chemoresistance in human ovarian cancer. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2016]

**Accessions** — [HGNC:17349](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17349) · Entrez [9128](https://www.ncbi.nlm.nih.gov/gene/9128) · UniProt [O43172](https://www.uniprot.org/uniprotkb/O43172) · Ensembl [ENSG00000136875](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136875)

## Data

Gene col 5928: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5928); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5928, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5928]; `tensor/DDL_lfc|DDL_z.npy` [5928]; `embed/gene_vectors.npy` [5928]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5928 or target_col == 5928). Every well: [[PRPF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRPF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
