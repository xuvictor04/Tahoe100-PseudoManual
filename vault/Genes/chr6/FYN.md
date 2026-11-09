---
symbol: "FYN"
type: "gene"
col: 216
ensembl_id: "ENSG00000010810"
name: "FYN proto-oncogene, Src family tyrosine kinase"
location: "6q21"
module: 134
arm: "+"
pooled_cpm: 121.36
n_lines_expressing: 42
n_dd_up: 16
n_dd_down: 14
n_dd_up_clean: 16
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 6
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# FYN

*FYN proto-oncogene, Src family tyrosine kinase* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.84× (z +19.0, q 0e+00, up in 35 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.414× (z -19.4, q 0e+00, down in 30 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.707× (z -7.6, q 3e-12, down in 22 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDFY2]] (+0.60, fdr 3e-05), [[STK32C]] (+0.60, fdr 1e-05), [[EIF4EBP1]] (+0.59, fdr 3e-05); moves opposite to [[CDK12]] (-0.55, fdr 3e-05), [[PPWD1]] (-0.54, fdr 3e-05), [[CARD8]] (-0.54, fdr 4e-05).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CAMK4]] → it (grade B ⚠); 6 go from it, the strongest it → [[OSBPL6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 216.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +19.0 | 0e+00 | 35/40 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.91×** | +14.3 | 5e-44 | 32/40 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.91×** | +14.3 | 8e-44 | 33/40 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.90×** | +14.2 | 2e-43 | 30/40 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.88×** | +13.9 | 8e-42 | 36/41 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.70×** | +11.7 | 2e-29 | 30/40 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +9.7 | 3e-20 | 28/40 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.98×** | +7.8 | 3e-13 | 29/41 (PANC-1, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +6.4 | 1e-08 | 19/41 (LoVo, RKO, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.20×** | +5.8 | 4e-07 | 19/40 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.56×** | +5.1 | 1e-05 | 22/40 (LoVo, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.24×** | +4.8 | 7e-05 | 16/40 (NCI-H2347, RKO, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +4.6 | 2e-04 | 14/41 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.6 | 2e-04 | 14/40 (SNU-1, PANC-1, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.001 | 17/41 (A-427, SHP-77, …) | top dose only |  |
| [[palbociclib (drug)]] 0.5 µM |  | **1.26×** | +3.7 | 0.008 | 18/40 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 216.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.414×** | -19.4 | 0e+00 | 30/41 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.413×** | -18.7 | 0e+00 | 26/35 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.486×** | -14.7 | 0e+00 | 31/37 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.657×** | -8.9 | 9e-17 | 27/39 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.707×** | -7.6 | 3e-12 | 22/40 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.736×** | -6.7 | 1e-09 | 25/40 (C32, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.767×** | -5.6 | 2e-06 | 19/40 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.792×** | -5.1 | 2e-05 | 20/40 (PANC-1, HOP62, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.857× | -4.8 | 1e-04 | 17/40 (SK-MEL-2, PANC-1, …) | top dose only | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.819×** | -4.4 | 6e-04 | 19/40 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.685×** | -4.3 | 7e-04 | 17/40 (A-172, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.823×** | -4.3 | 9e-04 | 12/41 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.874× | -4.2 | 0.001 | 11/40 (SK-MEL-2, RKO, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.698×** | -4.1 | 0.001 | 17/39 (SNU-1, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.831×** | -3.9 | 0.004 | 20/40 (C-33 A, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.838× | -3.6 | 0.011 | 17/39 (PANC-1, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.871× | -3.0 | 0.066 | 9/40 (HT-29, HOP62, …) | inconsistent across doses |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.908× | -3.0 | 0.074 | 4/41 (H4, SNU-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.911× | -2.9 | 0.090 | 14/40 (SW480, A-427, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.911× | -2.9 | 0.091 | 4/40 (NCI-H661, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 216. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 49.5 | 8 | 8 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.76× (z +17.2) | [[Harringtonine (drug)]] 0.5 µM 0.335× (z -13.1) |
| [[C32 (line)]] | wt | 763 | 0 | 13 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0685× (z -28.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -15.6) |
| [[SW480 (line)]] | alt | 579 | 0 | 12 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0887× (z -31.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -22.4) |
| [[NCI-H460 (line)]] | wt | 37.0 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.92× (z +18.2) | — |
| [[J82 (line)]] | alt | 115 | 6 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.06× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -15.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 35.3 | 8 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +18.8) | [[Harringtonine (drug)]] 5 µM 0.348× (z -9.5) |
| [[A-172 (line)]] | wt | 190 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.463× (z -13.2) |
| [[LS 180 (line)]] | wt | 67.5 | 6 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.93× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.137× (z -18.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 306 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.436× (z -14.3) |
| [[LOX-IMVI (line)]] | wt | 118 | 1 | 5 (5 ⚠) | [[Belinostat (drug)]] 5 µM 2.14× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.161× (z -20.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 38.2 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 5.44× (z +14.1) | — |
| [[Panc 03.27 (line)]] | alt | 42.3 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +11.1) | — |
| [[SW1417 (line)]] | alt | 63.8 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 2.55× (z +10.0) | — |
| [[A-427 (line)]] | wt | 51.5 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.05× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -15.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 118 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -12.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 294 | 1 | 4 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.56× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -12.1) |
| [[HT-29 (line)]] | alt | 97.4 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 96.3 | 1 | 4 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.28× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.347× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.395× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 307 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -16.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 46.4 | 4 | 0 | [[Belinostat (drug)]] 5 µM 3.16× (z +10.1) | — |
| [[SNU-423 (line)]] | alt | 244 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.94× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -17.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 191 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.265× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 61.7 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.28× (z +9.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.231× (z -12.0) ⚠ toxic |
| [[HCT15 (line)]] | alt | 160 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.486× (z -9.9) |
| [[RKO (line)]] | wt | 130 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.383× (z -9.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 153 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.83× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 93.6 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 1.88× (z +9.7) | — |
| [[SNU-1 (line)]] | wt | 96.0 | 1 | 1 (1 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.52× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.0917× (z -16.8) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 194 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0447× (z -15.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 55.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0907× (z -10.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 44.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +11.0) | — |
| [[H4 (line)]] | wt | 82.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -13.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 39.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.66× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -13.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 78.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.4) | — |
| [[A498 (line)]] | wt | 20.3 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 23.5 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 29.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 12.9 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.2 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 15.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 109 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 216), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDFY2]] | +0.60 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[STK32C]] | +0.60 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[EIF4EBP1]] | +0.59 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[MAPT]] | +0.59 | +0.50 / +0.47 | both halves | 2e-05 | STRING 994 |
| [[CARD19]] | +0.58 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[OSBPL6]] | +0.58 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[INPP5F]] | +0.58 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[ANKRD37]] | +0.58 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[SH3GL3]] | +0.57 | +0.47 / +0.49 | both halves | 2e-05 | same gene group; pathway: Signaling by NTRKs |
| [[GPR155]] | +0.57 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[ZFYVE28]] | +0.56 | +0.48 / +0.40 | both halves | 5e-05 |  |
| [[JARID2]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK12]] | -0.55 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[PPWD1]] | -0.54 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[CARD8]] | -0.54 | -0.40 / -0.43 | both halves | 4e-05 |  |
| [[DPP8]] | -0.53 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[EXOSC10]] | -0.53 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[MCPH1]] | -0.53 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[VPS52]] | -0.52 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[SRCAP]] | -0.52 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[ALG14]] | -0.51 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[TAF2]] | -0.51 | -0.43 / -0.44 | both halves | 3e-05 | pathway: HIV Infection |
| [[WDR33]] | -0.50 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[DNAJB12]] | -0.50 | -0.46 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAMK4]] | B | CAMK4 activity raises FYN's level | lines that do not express CAMK4 (21) vs lines expressing it (29) | 2.03× lower at baseline in the lines without CAMK4 | 0.086 | ⚠ within organs, on part of the lines; also absent: SNAP25, PRR16, ADAM12 |
| [[PMP22]] | B | PMP22 activity raises FYN's level | lines that do not express PMP22 (10) vs lines expressing it (40) | 2.80× lower at baseline in the lines without PMP22 | 0.094 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OSBPL6]] | B | FYN activity raises OSBPL6's level | lines that do not express FYN (8) vs lines expressing it (42) | 2.51× lower at baseline in the lines without FYN | 0.050 | ⚠ within organs, on part of the lines; also absent: RHOBTB3; maybe low, not absent |
| [[TSPAN5]] | B | FYN activity raises TSPAN5's level | lines that do not express FYN (8) vs lines expressing it (42) | 2.63× lower at baseline in the lines without FYN | 0.063 | ⚠ within organs, on part of the lines; also absent: RHOBTB3; maybe low, not absent |
| [[PDZD7]] | B | FYN activity raises PDZD7's level | lines that do not express FYN (8) vs lines expressing it (42) | 1.27× lower at baseline in the lines without FYN | 0.064 | ⚠ within organs, on part of the lines; also absent: RHOBTB3; maybe low, not absent |
| [[CAMK4]] | B | FYN activity raises CAMK4's level | lines that do not express FYN (8) vs lines expressing it (42) | 3.32× lower at baseline in the lines without FYN | 0.077 | ⚠ within organs, on part of the lines; also absent: RHOBTB3; maybe low, not absent |
| [[HACE1]] | B | FYN activity raises HACE1's level | lines that do not express FYN (8) vs lines expressing it (42) | 1.56× lower at baseline in the lines without FYN | 0.096 | ⚠ within organs, on part of the lines; also absent: RHOBTB3; maybe low, not absent |
| [[ETV5]] | C | FYN activity strengthens ETV5's drug response | lines that do not express FYN (8) vs lines expressing it (42) | the lines without FYN respond 1.08× as strongly (z diff +2.35); strongest at Binimetinib 0.5 µM: 0.35x vs 0.37x (z diff +3.2) | 0.069 | ⚠ within organs, on part of the lines; also absent: RHOBTB3; maybe low, not absent; rests on the correction |

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.617). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.3, -11.1); signed map (-27.7, 27.9). **Vector** length 121, 34.4% of its response variance represented; |z| ≥ 3 in 1,225 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.9 | +19.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.8 | +13.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.1 | +14.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.5 | +9.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.2 | +14.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.5 | +7.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.0 | +4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +4.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.3 | +5.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.6 | -8.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -5.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.9 | -0.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | -1.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.6 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | FYN proto-oncogene, Src family tyrosine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:111,660,332-111,873,452 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SYN, SLK, MGC45350 |
| Gene groups (HGNC) | SH2 domain containing; Src family tyrosine kinases; SH3 domain containing |
| Hallmark sets | COAGULATION, UV_RESPONSE_DN, COMPLEMENT |
| Reactome | 96 pathways, smallest: FLT3 signaling through SRC family kinases; NTRK2 activates RAC1; Reelin signalling pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P06241](https://www.uniprot.org/uniprotkb/P06241) (Tyrosine-protein kinase Fyn):

> Non-receptor tyrosine-protein kinase that plays a role in many biological processes including regulation of cell growth and survival, cell adhesion, integrin-mediated signaling, cytoskeletal remodeling, cell motility, immune response and axon guidance. Inactive FYN is phosphorylated on its C-terminal tail within the catalytic domain. Following activation by PKA, the protein subsequently associates with PTK2/FAK1, allowing PTK2/FAK1 phosphorylation, activation and targeting to focal adhesions. …

**Summary**, from NCBI Gene [2534](https://www.ncbi.nlm.nih.gov/gene/2534):

> This gene is a member of the protein-tyrosine kinase oncogene family. It encodes a membrane-associated tyrosine kinase that has been implicated in the control of cell growth. The protein associates with the p85 subunit of phosphatidylinositol 3-kinase and interacts with the fyn-binding protein. Alternatively spliced transcript variants encoding distinct isoforms exist. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4037](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4037) · Entrez [2534](https://www.ncbi.nlm.nih.gov/gene/2534) · UniProt [P06241](https://www.uniprot.org/uniprotkb/P06241) · Ensembl [ENSG00000010810](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000010810)

## Data

Gene col 216: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 216); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 216, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 216]; `tensor/DDL_lfc|DDL_z.npy` [216]; `embed/gene_vectors.npy` [216]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 216 or target_col == 216). Every well: [[FYN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FYN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
