---
symbol: "AMBRA1"
type: "gene"
col: 3145
ensembl_id: "ENSG00000110497"
name: "autophagy and beclin 1 regulator 1"
location: "11p11.2"
module: 24
arm: "+"
pooled_cpm: 138.93
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 8
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# AMBRA1

*autophagy and beclin 1 regulator 1* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.08× (z +14.1, q 2e-42, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.331× (z -19.3, q 0e+00, down in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.710× (z -6.0, q 3e-07, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MARCHF5]] (+0.71, fdr 7e-06), [[PIAS1]] (+0.71, fdr 7e-06), [[PPP2R5E]] (+0.66, fdr 7e-06); moves opposite to [[SOWAHC]] (-0.56, fdr 1e-05), [[HUS1]] (-0.54, fdr 6e-05), [[THOC6]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PFKP]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3145.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.08×** | +14.1 | 2e-42 | 48/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.84×** | +11.7 | 4e-29 | 47/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.77×** | +9.9 | 9e-21 | 45/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +7.5 | 1e-11 | 36/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +7.3 | 3e-11 | 30/48 (A-172, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +6.4 | 1e-08 | 39/48 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +6.4 | 1e-08 | 37/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +6.3 | 2e-08 | 34/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +4.8 | 9e-05 | 34/48 (H4, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.27×** | +4.2 | 0.002 | 28/48 (H4, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.023 | 22/48 (NCI-H460, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.045 | 22/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.049 | 21/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.094 | 18/48 (SNU-423, LoVo, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3145.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.331×** | -19.3 | 0e+00 | 48/49 (COLO 205, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.347×** | -17.7 | 0e+00 | 44/44 (HepG2/C3A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.381×** | -15.5 | 0e+00 | 43/45 (SW1417, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.710×** | -6.0 | 3e-07 | 40/48 (MIA PaCa-2, HT-29, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.844× | -4.2 | 0.003 | 17/48 (SW 1088, MIA PaCa-2, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.789×** | -4.2 | 0.003 | 32/48 (LoVo, J82, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **0.790×** | -4.1 | 0.003 | 27/48 (SW1417, SW 1271, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.798×** | -3.8 | 0.010 | 23/47 (MIA PaCa-2, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.816×** | -3.6 | 0.022 | 24/48 (J82, HEC-1-A, …) | all doses, flat |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.837× | -3.1 | 0.097 | 19/47 (A-172, C32, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.751× | -3.1 | 0.10 | 22/48 (A549, MIA PaCa-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.842× | -3.0 | 0.12 | 19/48 (C32, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3145. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 114 | 6 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -13.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 130 | 5 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.60× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 144 | 3 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.196× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.492× (z -11.6) |
| [[SW1417 (line)]] | alt | 198 | 3 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.63× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.194× (z -18.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 147 | 3 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.91× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -14.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 291 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.08× (z +9.5) | [[Auranofin (drug)]] 5 µM 0.210× (z -18.2) |
| [[SW480 (line)]] | alt | 129 | 3 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 9.22× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.398× (z -12.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 153 | 4 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.3× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.327× (z -11.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 134 | 2 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 5.80× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -12.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 149 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.10× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.419× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 123 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.64× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.369× (z -11.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 130 | 3 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 8.92× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 96.9 | 3 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.13× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.400× (z -11.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 224 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.40× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.150× (z -21.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 156 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.83× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -17.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 186 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.24× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -16.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 172 | 1 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 7.48× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.210× (z -13.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 135 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.51× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -12.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 172 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.66× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.0779× (z -26.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 101 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.78× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.381× (z -10.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 163 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.79× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.0790× (z -23.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 96.1 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.68× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.342× (z -12.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 159 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.15× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -13.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 118 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.120× (z -24.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 134 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.03× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -25.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 179 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -15.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 144 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.96× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -15.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 105 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.7× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.311× (z -9.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 133 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.35× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -14.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 135 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -20.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 113 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 102 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +9.6) | — |
| [[NCI-H2347 (line)]] | alt | 157 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -19.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 118 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.80× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.256× (z -14.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 151 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.50× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -10.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 200 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -13.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 133 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.58× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -12.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 179 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.3× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0470× (z -29.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 95.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.288× (z -12.4) ⚠ transcription drop |
| [[NCI-H661 (line)]] | alt | 156 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -10.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 116 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.80× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 148 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.18× (z +9.4) | — |
| [[CHP-212 (line)]] | wt | 154 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 85.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 91.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 75.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3145), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARCHF5]] | +0.71 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[PIAS1]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[PPP2R5E]] | +0.66 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[STRN3]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 | same gene group |
| [[NPEPPS]] | +0.64 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[SEC24B]] | +0.63 | +0.58 / +0.66 | both halves | 7e-06 | same gene group |
| [[PAN3]] | +0.61 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[COX14]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ELF2]] | +0.61 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[SPPL3]] | +0.61 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[ZNF358]] | +0.61 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[LAMTOR2]] | +0.60 | +0.54 / +0.45 | both halves | 3e-05 | pathway: Autophagy |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOWAHC]] | -0.56 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[HUS1]] | -0.54 | -0.58 / -0.39 | both halves | 6e-05 |  |
| [[THOC6]] | -0.53 | -0.54 / -0.42 | both halves | 4e-05 | same gene group |
| [[PHLDA1]] | -0.52 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[MYSM1]] | -0.52 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[TNFRSF12A]] | -0.51 | -0.62 / -0.40 | both halves | 4e-05 |  |
| [[ETS1]] | -0.51 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[ZNF121]] | -0.50 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[FAM83G]] | -0.49 | -0.54 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PFKP]] | C | PFKP activity lowers AMBRA1's level | lines that do not express PFKP (3) vs lines expressing it (47) | 1.37× higher at baseline in the lines without PFKP | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ASPH, MAP3K5, CFAP45; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.469). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (0.2, -40.9); signed map (-15.1, 12.6). **Vector** length 81.8, 27.1% of its response variance represented; |z| ≥ 3 in 1,045 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +1.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.7 | +14.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +11.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.8 | +0.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +0.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.7 | +2.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.6 | +0.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.5 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | +0.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.9 | -1.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.6 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -0.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | autophagy and beclin 1 regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:46,396,414-46,594,125 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20294, KIAA1736, WDR94, DCAF3 |
| Gene groups (HGNC) | WD repeat domain containing; DDB1 and CUL4 associated factors; MicroRNA protein coding host genes |
| Reactome | 2 pathways, smallest: Macroautophagy; Autophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0C7](https://www.uniprot.org/uniprotkb/Q9C0C7) (Activating molecule in BECN1-regulated autophagy protein 1):

> Substrate-recognition component of a DCX (DDB1-CUL4-X-box) E3 ubiquitin-protein ligase complex involved in cell cycle control and autophagy. The DCX(AMBRA1) complex specifically mediates the polyubiquitination of target proteins such as BECN1, CCND1, CCND2, CCND3, ELOC and ULK1. Acts as an upstream master regulator of the transition from G1 to S cell phase: AMBRA1 specifically recognizes and binds phosphorylated cyclin-D (CCND1, CCND2 and CCND3), leading to cyclin-D ubiquitination by the …

**Summary**, from NCBI Gene [55626](https://www.ncbi.nlm.nih.gov/gene/55626):

> Enables enzyme binding activity; protein phosphatase activator activity; and ubiquitin-like ligase-substrate adaptor activity. Involved in several processes, including macroautophagy; positive regulation of free ubiquitin chain polymerization; and positive regulation of phosphatidylinositol 3-kinase/protein kinase B signal transduction. Located in cytosol. Part of Cul4-RING E3 ubiquitin ligase complex. Is active in cytoskeleton; mitochondrion; and nucleus. Biomarker of multiple system atrophy. …

**Accessions** — [HGNC:25990](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25990) · Entrez [55626](https://www.ncbi.nlm.nih.gov/gene/55626) · UniProt [Q9C0C7](https://www.uniprot.org/uniprotkb/Q9C0C7) · Ensembl [ENSG00000110497](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110497)

## Data

Gene col 3145: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3145); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3145, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3145]; `tensor/DDL_lfc|DDL_z.npy` [3145]; `embed/gene_vectors.npy` [3145]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3145 or target_col == 3145). Every well: [[AMBRA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AMBRA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
