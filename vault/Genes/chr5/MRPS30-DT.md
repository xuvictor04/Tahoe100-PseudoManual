---
symbol: "MRPS30-DT"
type: "gene"
col: 14741
ensembl_id: "ENSG00000251141"
name: "MRPS30 divergent transcript"
location: "5p12"
module: 29
arm: "+"
pooled_cpm: 15.28
n_lines_expressing: 45
n_dd_up: 19
n_dd_down: 30
n_dd_up_clean: 15
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# MRPS30-DT

*MRPS30 divergent transcript* — 5p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.84× (z +11.0, q 2e-25, up in 37 of 43 measured lines) ⚠ cell-cycle shift, explains ~55% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.77× (z +10.3, q 3e-22, up in 26 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.390× (z -16.9, q 0e+00, down in 36 of 39 measured lines) ⚠ cell-cycle shift, explains ~56% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.507× (z -8.6, q 7e-16, down in 24 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC18B1]] (+0.61, fdr 2e-05), [[SUMO1]] (+0.54, fdr 3e-05), [[LINC01232]] (+0.53, fdr 4e-05); moves opposite to [[LCAT]] (-0.52, fdr 4e-05), [[CLEC16A]] (-0.51, fdr 1e-04), [[RASAL2]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HOTAIR]] → it (grade B ⚠); 2 go from it, the strongest it → [[SUMO1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14741.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.84×** | +11.0 | 2e-25 | 37/43 (LS 180, SW 900, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +10.3 | 3e-22 | 26/40 (HEC-1-A, SW1417, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.66×** | +6.5 | 2e-08 | 27/42 (SW 900, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.64×** | +6.3 | 5e-08 | 23/41 (LS 180, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.56×** | +5.7 | 2e-06 | 25/43 (A-172, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +4.8 | 2e-04 | 20/43 (SW 900, NCI-H1792, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.4 | 9e-04 | 15/38 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.005 | 17/43 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.36×** | +3.9 | 0.005 | 18/43 (NCI-H2347, SW 900, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.005 | 12/43 (A498, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.007 | 9/42 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +3.7 | 0.009 | 13/43 (NCI-H23, HEC-1-A, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +3.6 | 0.014 | 12/43 (NCI-H2347, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.35×** | +3.6 | 0.015 | 9/42 (NCI-H23, Hs 766T, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.30×** | +3.3 | 0.031 | 11/43 (HEC-1-A, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.031 | 5/43 (A498, HEC-1-A, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.053 | 13/42 (HEC-1-A, SK-MEL-2, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.081 | 8/41 (NCI-H1573, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 17 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14741.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.390×** | -16.9 | 0e+00 | 36/39 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.366×** | -12.8 | 8e-35 | 39/43 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.426×** | -10.8 | 5e-25 | 33/40 (A498, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.486×** | -9.1 | 8e-18 | 32/41 (COLO 205, LS 180, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.488×** | -9.1 | 1e-17 | 33/42 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.507×** | -8.6 | 7e-16 | 24/42 (HepG2/C3A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.541×** | -7.8 | 6e-13 | 26/41 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.500×** | -7.7 | 7e-13 | 29/38 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.559×** | -7.4 | 1e-11 | 26/42 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.669×** | -7.2 | 4e-11 | 27/43 (C32, COLO 205, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.536×** | -7.0 | 2e-10 | 27/41 (NCI-H1573, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.384×** | -6.3 | 1e-08 | 21/42 (LS 180, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.614×** | -6.2 | 3e-08 | 23/42 (NCI-H1573, A498, …) | rises with dose | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.630×** | -5.9 | 2e-07 | 26/42 (C32, A-427, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.643×** | -5.6 | 9e-07 | 21/42 (C32, NCI-H23, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.616×** | -5.4 | 2e-06 | 23/42 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.655×** | -5.3 | 3e-06 | 21/40 (Panc 03.27, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.654×** | -5.1 | 1e-05 | 20/42 (A498, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.550×** | -4.0 | 0.002 | 12/39 (C32, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.712×** | -3.8 | 0.003 | 11/43 (LOX-IMVI, AN3 CA, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.759×** | -3.5 | 0.011 | 13/42 (LOX-IMVI, NCI-H1573, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.620×** | -3.2 | 0.031 | 15/39 (NCI-H1573, A-427, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.838× | -3.1 | 0.032 | 12/43 (Hs 766T, J82, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **0.639×** | -3.0 | 0.057 | 5/36 (NCI-H23, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.651×** | -2.8 | 0.082 | 9/39 (HEC-1-A, SHP-77, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.76 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14741. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 16.6 | 0 | 10 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -23.1) ⚠ cell-cycle shift, explains ~56% of this change |
| [[COLO 205 (line)]] | alt | 45.1 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -17.3) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.257× (z -8.5) |
| [[A498 (line)]] | wt | 12.8 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0871× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.148× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 33.6 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -25.2) ⚠ cell-cycle shift, explains ~56% of this change |
| [[SW480 (line)]] | alt | 12.3 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.167× (z -11.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HepG2_C3A (line)]] | wt | 11.6 | 0 | 4 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0388× (z -11.6) |
| [[C32 (line)]] | wt | 45.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -16.2) ⚠ cell-cycle shift, explains ~56% of this change |
| [[NCI-H23 (line)]] | alt | 32.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -12.2) ⚠ cell-cycle shift, explains ~56% of this change |
| [[CFPAC-1 (line)]] | alt | 18.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -10.6) ⚠ cell-cycle shift, explains ~56% of this change |
| [[HCT15 (line)]] | alt | 15.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0762× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0802× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 17.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -11.5) ⚠ cell-cycle shift, explains ~56% of this change |
| [[LS 180 (line)]] | wt | 25.9 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.241× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 8.23 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -9.8) ⚠ cell-cycle shift, explains ~42% of this change |
| [[Panc 03.27 (line)]] | alt | 13.8 | 0 | 2 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.101× (z -12.1) |
| [[C-33 A (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -9.7) ⚠ cell-cycle shift, explains ~56% of this change |
| [[HS-578T (line)]] | alt | 5.55 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0824× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[MIA PaCa-2 (line)]] | alt | 23.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -9.2) ⚠ cell-cycle shift, explains ~56% of this change |
| [[NCI-H2347 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -8.6) ⚠ cell-cycle shift, explains ~56% of this change |
| [[NCI-H460 (line)]] | wt | 5.32 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -14.3) ⚠ cell-cycle shift, explains ~56% of this change |
| [[NCI-H661 (line)]] | alt | 628 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -10.0) ⚠ cell-cycle shift, explains ~56% of this change |
| [[RKO (line)]] | wt | 28.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -12.6) ⚠ cell-cycle shift, explains ~56% of this change |
| [[RPMI-7951 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0420× (z -11.8) ⚠ cell-cycle shift, explains ~70% of this change |
| [[SK-MEL-2 (line)]] | alt | 6.39 | 0 | 1 | — | [[NG25 (drug)]] 0.05 µM 0.0605× (z -10.0) |
| [[A-172 (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.36 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14741), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC18B1]] | +0.61 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[SUMO1]] | +0.54 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[LINC01232]] | +0.53 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[EEF1AKMT3]] | +0.53 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[LINC00115]] | +0.53 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[MINDY1]] | +0.52 | +0.52 / +0.37 | both halves | 8e-05 |  |
| [[SDHD]] | +0.52 | +0.33 / +0.49 | both halves | 1e-04 |  |
| [[ZBTB26]] | +0.52 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[HOXB6]] | +0.50 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[SMPDL3A]] | +0.50 | +0.39 / +0.45 | both halves | 6e-05 |  |
| [[ZNF738]] | +0.50 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[NDUFAF7]] | +0.50 | +0.45 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCAT]] | -0.52 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[CLEC16A]] | -0.51 | -0.32 / -0.48 | both halves | 1e-04 |  |
| [[RASAL2]] | -0.50 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[ARHGAP39]] | -0.49 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[CYFIP1]] | -0.48 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[SLC12A4]] | -0.48 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[SFSWAP]] | -0.47 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[ASAP1]] | -0.46 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[MICAL2]] | -0.45 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[MYO9A]] | -0.45 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[METRNL]] | -0.44 | -0.44 / -0.27 | both halves | 3e-04 |  |
| [[FER]] | -0.44 | -0.29 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOTAIR]] | B | HOTAIR activity raises MRPS30-DT's level | lines that do not express HOTAIR (27) vs lines expressing it (23) | 1.62× lower at baseline in the lines without HOTAIR | 0.069 | ⚠ within organs, on part of the lines; also absent: CES1, DOK5, ANKRD20A9P |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SUMO1]] | B | MRPS30-DT activity raises SUMO1's level | lines that do not express MRPS30-DT (5) vs lines expressing it (45) | 1.36× lower at baseline in the lines without MRPS30-DT | 0.093 | ⚠ within organs, on part of the lines; also absent: PIP4P2, ENSG00000277611 |
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | C | MRPS30-DT's natural level lowers the cells' numbers under Lapatinib ditosylate 0.5 µM (makes them more sensitive) | MRPS30-DT's natural level across 43 lines (lineage-adjusted; a glimpse) | r -0.66 | 0.417 over the table, 0.067 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.413). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-7.9, 22.4); signed map (-20.5, -29.8). **Vector** length 70.4, 13.2% of its response variance represented; |z| ≥ 3 in 1,098 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +7.5 | +11.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +10.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | +4.3 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.8 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +6.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +5.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.0 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | -0.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.9 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +4.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -4.8 | -16.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.0 | -5.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.8 | -5.9 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.6 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.5 | -7.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.2 | -5.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -7.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.8 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.7 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | MRPS30 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5p12 — chr5:44,742,420-44,808,777 (-) |
| Ensembl biotype | lncRNA |
| Also known as | BRCAT54, BRCAT107; previously LINC02224 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53420](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53420) · Entrez [100506674](https://www.ncbi.nlm.nih.gov/gene/100506674) · Ensembl [ENSG00000251141](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000251141)

## Data

Gene col 14741: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14741); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14741, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14741]; `tensor/DDL_lfc|DDL_z.npy` [14741]; `embed/gene_vectors.npy` [14741]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14741 or target_col == 14741). Every well: [[MRPS30-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS30-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
