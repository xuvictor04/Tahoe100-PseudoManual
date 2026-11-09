---
symbol: "NOS1AP"
type: "gene"
col: 12742
ensembl_id: "ENSG00000198929"
name: "nitric oxide synthase 1 adaptor protein"
location: "1q23.3"
module: 83
arm: "-"
pooled_cpm: 91.68
n_lines_expressing: 41
n_dd_up: 17
n_dd_down: 13
n_dd_up_clean: 14
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 8
direction_downstream: 12
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# NOS1AP

*nitric oxide synthase 1 adaptor protein* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.39× (z +20.8, q 0e+00, up in 38 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.377× (z -16.6, q 0e+00, down in 34 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.781× (z -4.2, q 0.002, down in 18 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFD]] (+0.65, fdr 2e-05), [[ATP8A1]] (+0.64, fdr 9e-06), [[INPP5F]] (+0.63, fdr 2e-05); moves opposite to [[ZNF621]] (-0.64, fdr 1e-05), [[CLHC1]] (-0.62, fdr 3e-05), [[CSTF3]] (-0.60, fdr 2e-05).
> It sits in the **-** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[EEPD1]] → it (grade B ⚠); 12 go from it, the strongest it → [[INPP5F]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12742.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.39×** | +20.8 | 0e+00 | 38/39 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.81×** | +17.6 | 0e+00 | 39/39 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.80×** | +17.5 | 0e+00 | 38/39 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +12.8 | 1e-35 | 27/39 (NCI-H1792, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.06×** | +12.2 | 2e-32 | 38/39 (J82, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +10.9 | 9e-26 | 34/39 (CFPAC-1, RKO, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.66×** | +8.7 | 3e-16 | 38/40 (NCI-H23, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +7.7 | 7e-13 | 29/40 (RKO, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +7.4 | 1e-11 | 23/39 (LS 180, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +6.4 | 8e-09 | 28/39 (NCI-H23, RKO, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +5.5 | 2e-06 | 20/39 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +5.2 | 8e-06 | 27/37 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.68×** | +4.6 | 2e-04 | 22/39 (J82, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +4.5 | 2e-04 | 22/39 (LS 180, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.037 | 17/39 (BT-474, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.075 | 11/40 (SNU-423, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12742.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.377×** | -16.6 | 0e+00 | 34/38 (HCT15, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.420×** | -14.2 | 5e-43 | 29/33 (LS 180, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.519×** | -10.3 | 1e-22 | 29/35 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.687×** | -6.4 | 2e-08 | 29/38 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.754×** | -4.6 | 5e-04 | 23/38 (SW1417, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.781×** | -4.2 | 0.002 | 18/39 (HepG2/C3A, C32, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.624×** | -4.2 | 0.002 | 18/39 (SW1417, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.775×** | -4.2 | 0.002 | 20/39 (NCI-H2030, NCI-H1792, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.632×** | -4.1 | 0.003 | 21/37 (HCT15, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.858× | -3.7 | 0.013 | 11/39 (SNU-1, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.807×** | -3.6 | 0.014 | 17/39 (C32, PANC-1, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.674×** | -3.5 | 0.022 | 12/31 (HT-29, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.824×** | -3.3 | 0.044 | 13/39 (A498, LoVo, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.827×** | -3.2 | 0.050 | 18/39 (AsPC-1, Panc 03.27, …) | top dose only |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.881× | -3.0 | 0.092 | 7/39 (A498, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12742. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 245 | 5 | 6 (6 ⚠) | [[Belinostat (drug)]] 5 µM 2.30× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -18.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 355 | 4 (1 ⚠) | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 11.0× (z +13.3) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 3.17× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -23.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 139 | 4 | 5 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.96× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -17.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 65.4 | 5 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 5.00× (z +14.6) | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -11.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 122 | 6 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.194× (z -14.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 99.5 | 2 | 6 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.99× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.180× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.364× (z -9.0) |
| [[A-427 (line)]] | wt | 49.6 | 6 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.04× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 40.7 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 9.37× (z +16.7) | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -13.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 112 | 4 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.91× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -16.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 42.7 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.19× (z +14.0) | [[Dinaciclib (drug)]] 0.05 µM 0.319× (z -9.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 47.4 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.14× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -9.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 103 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.44× (z +12.2) | [[Lonafarnib (drug)]] 5 µM 0.0662× (z -14.0) ⚠ toxic |
| [[RKO (line)]] | wt | 27.3 | 6 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.86× (z +11.3) | — |
| [[SW 900 (line)]] | alt | 108 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -9.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 131 | 4 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.14× (z +9.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.97× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -9.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 81.7 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.08× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -14.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 52.3 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.39× (z +12.2) | — |
| [[A498 (line)]] | wt | 104 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.187× (z -13.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 248 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.344× (z -9.4) |
| [[HCT15 (line)]] | alt | 117 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.86× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0413× (z -28.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 167 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.0220× (z -39.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 47.0 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.03× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 97.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -14.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 27.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.79× (z +10.0) | — |
| [[BT-474 (line)]] | alt | 114 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.73× (z +10.7) | — |
| [[HepG2_C3A (line)]] | wt | 168 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.246× (z -12.8) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 116 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -15.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 29.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.64× (z +10.8) | — |
| [[LoVo (line)]] | wt | 339 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -17.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 99.8 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.331× (z -11.0) ⚠ transcription drop |
| [[NCI-H1792 (line)]] | alt | 27.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +14.5) | — |
| [[SNU-1 (line)]] | wt | 55.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 42.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.72× (z +10.4) | — |
| [[SW48 (line)]] | wt | 142 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 12.1× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.0487× (z -20.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -13.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.6 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 18.1 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.6 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 13.6 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 19.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 21.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.7 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 44.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12742), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFD]] | +0.65 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[ATP8A1]] | +0.64 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[INPP5F]] | +0.63 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[LRRC1]] | +0.61 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[FOXO6]] | +0.60 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[LGR4]] | +0.60 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[CXADR]] | +0.58 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[HMGN3]] | +0.58 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[PACSIN2]] | +0.58 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[CLMN]] | +0.58 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[FAM102B]] | +0.58 | +0.49 / +0.53 | both halves | 2e-05 |  |
| [[USP2]] | +0.58 | +0.44 / +0.60 | both halves | 3e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF621]] | -0.64 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[CLHC1]] | -0.62 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[CSTF3]] | -0.60 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[MAPKAPK5]] | -0.59 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[LTO1]] | -0.59 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[KRR1]] | -0.58 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[EXOSC3]] | -0.57 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[ACAD9]] | -0.57 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[ZNF577]] | -0.57 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[SMIM15-AS1]] | -0.57 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[METTL6]] | -0.56 | -0.37 / -0.44 | both halves | 7e-05 |  |
| [[DPH5-DT]] | -0.56 | -0.48 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EEPD1]] | B | EEPD1 activity raises NOS1AP's level | lines that do not express EEPD1 (14) vs lines expressing it (36) | 2.77× lower at baseline in the lines without EEPD1 | 0.028 | ⚠ within organs, on part of the lines; also absent: KCNK5, RHOD, LAMP3; maybe low, not absent |
| [[ZNF717]] | B | ZNF717 activity lowers NOS1AP's level | lines that do not express ZNF717 (7) vs lines expressing it (43) | 2.58× higher at baseline in the lines without ZNF717 | 0.057 | ⚠ within organs, on part of the lines; also absent: PTGR1, CCDC110, MYBL1 |
| [[BIK]] | B | BIK activity raises NOS1AP's level | lines that do not express BIK (15) vs lines expressing it (35) | 2.20× lower at baseline in the lines without BIK | 0.058 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3 |
| [[CDS1]] | B | CDS1 activity raises NOS1AP's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 2.13× lower at baseline in the lines without CDS1 | 0.059 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[NR3C2]] | B | NR3C2 activity raises NOS1AP's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.95× lower at baseline in the lines without NR3C2 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[ESPN]] | B | ESPN activity raises NOS1AP's level | lines that do not express ESPN (26) vs lines expressing it (24) | 1.83× lower at baseline in the lines without ESPN | 0.080 | ⚠ within organs, on part of the lines; also absent: B3GNT7, HSD17B2, FXYD3 |
| [[TSPAN15]] | B | TSPAN15 activity weakens NOS1AP's drug response | lines that do not express TSPAN15 (11) vs lines expressing it (29) | the lines without TSPAN15 respond 0.98× as strongly (z diff -0.20); strongest at Panobinostat 0.05 µM: 2.62x vs 1.91x (z diff -1.9) | 0.081 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[C1orf226]] | C | C1orf226 activity raises NOS1AP's level | lines that do not express C1orf226 (14) vs lines expressing it (36) | 4.12× lower at baseline in the lines without C1orf226 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, EPS8L2, EEPD1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[INPP5F]] | B | NOS1AP activity raises INPP5F's level | lines that do not express NOS1AP (9) vs lines expressing it (41) | 1.36× lower at baseline in the lines without NOS1AP | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, C1orf226, CMTM8; maybe low, not absent |
| [[ARRB1]] | B | NOS1AP activity raises ARRB1's level | lines that do not express NOS1AP (9) vs lines expressing it (41) | 1.68× lower at baseline in the lines without NOS1AP | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, C1orf226, CMTM8; maybe low, not absent |
| [[CARMIL1]] | B | NOS1AP activity raises CARMIL1's level | lines that do not express NOS1AP (9) vs lines expressing it (41) | 2.72× lower at baseline in the lines without NOS1AP | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, C1orf226, CMTM8; maybe low, not absent |
| [[DAB2IP]] | B | NOS1AP activity raises DAB2IP's level | lines that do not express NOS1AP (9) vs lines expressing it (41) | 1.98× lower at baseline in the lines without NOS1AP | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, C1orf226, CMTM8; maybe low, not absent |
| [[EEPD1]] | B | NOS1AP activity raises EEPD1's level | lines that do not express NOS1AP (9) vs lines expressing it (41) | 2.74× lower at baseline in the lines without NOS1AP | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, C1orf226, CMTM8; maybe low, not absent |
| [[EFNA3]] | B | NOS1AP activity raises EFNA3's level | lines that do not express NOS1AP (9) vs lines expressing it (41) | 1.43× lower at baseline in the lines without NOS1AP | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, C1orf226, CMTM8; maybe low, not absent |
| [[CLMN]] | B | NOS1AP activity raises CLMN's level | lines that do not express NOS1AP (9) vs lines expressing it (41) | 2.28× lower at baseline in the lines without NOS1AP | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, C1orf226, CMTM8; maybe low, not absent |
| [[CHKA]] | B | NOS1AP activity raises CHKA's level | lines that do not express NOS1AP (9) vs lines expressing it (41) | 2.20× lower at baseline in the lines without NOS1AP | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, C1orf226, CMTM8; maybe low, not absent |
| [[MAGI1]] | B | NOS1AP activity raises MAGI1's level | lines that do not express NOS1AP (9) vs lines expressing it (41) | 2.37× lower at baseline in the lines without NOS1AP | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, C1orf226, CMTM8; maybe low, not absent |
| [[PIK3C2B]] | B | NOS1AP activity raises PIK3C2B's level | lines that do not express NOS1AP (9) vs lines expressing it (41) | 2.39× lower at baseline in the lines without NOS1AP | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, C1orf226, CMTM8; maybe low, not absent |
| [[RHPN2]] | B | NOS1AP activity raises RHPN2's level | lines that do not express NOS1AP (9) vs lines expressing it (41) | 2.41× lower at baseline in the lines without NOS1AP | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, C1orf226, CMTM8; maybe low, not absent |
| [[C1orf226]] | C | NOS1AP activity raises C1orf226's level | lines that do not express NOS1AP (9) vs lines expressing it (41) | 2.37× lower at baseline in the lines without NOS1AP | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, C1orf226, CMTM8; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **-** arm (projection on the module's main direction -0.687). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (8.4, 5.6); signed map (-20.5, 20.2). **Vector** length 103, 29.6% of its response variance represented; |z| ≥ 3 in 1,212 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +10.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.3 | +12.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +7.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.8 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +8.7 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.8 | +2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.8 | +4.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | +2.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.4 | +0.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | -4.1 | -0.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.0 | -10.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.8 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | nitric oxide synthase 1 adaptor protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:162,069,691-162,370,475 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0464, CAPON |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O75052](https://www.uniprot.org/uniprotkb/O75052) (Carboxyl-terminal PDZ ligand of neuronal nitric oxide synthase protein):

> Adapter protein involved in neuronal nitric-oxide (NO) synthesis regulation via its association with nNOS/NOS1. The complex formed with NOS1 and synapsins is necessary for specific NO and synapsin functions at a presynaptic level. Mediates an indirect interaction between NOS1 and RASD1 leading to enhance the ability of NOS1 to activate RASD1. Competes with DLG4 for interaction with NOS1, possibly affecting NOS1 activity by regulating the interaction between NOS1 and DLG4 (By similarity). In …

**Summary**, from NCBI Gene [9722](https://www.ncbi.nlm.nih.gov/gene/9722):

> This gene encodes a cytosolic protein that binds to the signaling molecule, neuronal nitric oxide synthase (nNOS). This protein has a C-terminal PDZ-binding domain that mediates interactions with nNOS and an N-terminal phosphotyrosine binding (PTB) domain that binds to the small monomeric G protein, Dexras1. Studies of the related mouse and rat proteins have shown that this protein functions as an adapter protein linking nNOS to specific targets, such as Dexras1 and the synapsins. Alternative …

**Accessions** — [HGNC:16859](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16859) · Entrez [9722](https://www.ncbi.nlm.nih.gov/gene/9722) · UniProt [O75052](https://www.uniprot.org/uniprotkb/O75052) · Ensembl [ENSG00000198929](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198929)

## Data

Gene col 12742: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12742); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12742, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12742]; `tensor/DDL_lfc|DDL_z.npy` [12742]; `embed/gene_vectors.npy` [12742]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12742 or target_col == 12742). Every well: [[NOS1AP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOS1AP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
