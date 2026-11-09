---
symbol: "GCNT2"
type: "gene"
col: 3292
ensembl_id: "ENSG00000111846"
name: "glucosaminyl (N-acetyl) transferase 2 (I blood group)"
location: "6p24.3-p24.2"
module: 117
arm: "+"
pooled_cpm: 93.87
n_lines_expressing: 34
n_dd_up: 17
n_dd_down: 18
n_dd_up_clean: 16
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# GCNT2

*glucosaminyl (N-acetyl) transferase 2 (I blood group)* — 6p24.3-p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 2.98× (z +22.9, q 0e+00, up in 29 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.548× (z -18.8, q 0e+00, down in 26 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAPS2]] (+0.63, fdr 7e-06), [[TLR6]] (+0.59, fdr 1e-05), [[EGF]] (+0.57, fdr 1e-05); moves opposite to [[TBCCD1]] (-0.57, fdr 2e-05), [[CRYGS]] (-0.55, fdr 3e-05), [[ZBED4]] (-0.50, fdr 3e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[AKR1C3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3292.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **2.98×** | +22.9 | 0e+00 | 29/32 (HOP62, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.57×** | +21.0 | 0e+00 | 28/32 (HepG2/C3A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.84×** | +19.1 | 0e+00 | 20/32 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.15×** | +17.0 | 0e+00 | 26/32 (HOP62, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.74×** | +8.8 | 2e-16 | 23/33 (HOP62, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +8.4 | 3e-15 | 22/32 (NCI-H1573, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +7.6 | 2e-12 | 18/32 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +6.8 | 7e-10 | 18/32 (J82, HOP62, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.33×** | +5.8 | 4e-07 | 16/33 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.18× | +5.3 | 6e-06 | 12/32 (NCI-H1792, SW 900, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.21×** | +5.3 | 6e-06 | 13/32 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.24×** | +4.8 | 6e-05 | 13/32 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +4.2 | 0.001 | 13/32 (A-172, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.22×** | +4.1 | 0.001 | 10/32 (AsPC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.54×** | +4.0 | 0.002 | 10/32 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.003 | 14/33 (NCI-H1573, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3292.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.548×** | -18.8 | 0e+00 | 26/32 (MIA PaCa-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.511×** | -14.3 | 8e-44 | 25/32 (MIA PaCa-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.590×** | -11.7 | 3e-29 | 25/32 (PANC-1, NCI-H2347, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.635×** | -9.7 | 6e-20 | 24/33 (MIA PaCa-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.670×** | -8.9 | 1e-16 | 20/32 (PANC-1, NCI-H1792, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.815×** | -6.4 | 2e-08 | 18/32 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.769×** | -5.8 | 5e-07 | 18/32 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | **0.770×** | -5.8 | 5e-07 | 18/32 (NCI-H661, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Mebendazole (drug)]] 5 µM |  | **0.774×** | -5.4 | 4e-06 | 13/32 (CFPAC-1, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.798×** | -5.0 | 4e-05 | 17/32 (SHP-77, NCI-H2030, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.802×** | -4.9 | 6e-05 | 17/32 (COLO 205, SW480, …) | rises with dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.798×** | -4.8 | 7e-05 | 18/32 (NCI-H2030, A498, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.810×** | -4.7 | 1e-04 | 16/32 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.817×** | -4.5 | 3e-04 | 14/32 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.823×** | -4.3 | 6e-04 | 15/32 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.829×** | -4.0 | 0.002 | 13/32 (HS-578T, A498, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.840× | -3.8 | 0.004 | 14/32 (CFPAC-1, Panc 03.27, …) | two highest doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.674×** | -3.6 | 0.008 | 12/32 (CFPAC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.892× | -3.5 | 0.011 | 7/32 (A498, NCI-H2347, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.856× | -3.4 | 0.015 | 8/32 (PANC-1, A-172, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.693×** | -3.4 | 0.016 | 9/32 (C32, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | 0.865× | -3.2 | 0.031 | 10/32 (NCI-H2347, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3292. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 466 | 1 (1 ⚠) | 9 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 6.17× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -22.1) |
| [[COLO 205 (line)]] | alt | 79.8 | 3 | 6 (5 ⚠) | [[Bortezomib (drug)]] 0.05 µM 5.82× (z +13.9) | [[Harringtonine (drug)]] 5 µM 0.148× (z -15.3) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.313× (z -13.7) |
| [[LOX-IMVI (line)]] | wt | 132 | 5 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +15.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -15.4) |
| [[SW 900 (line)]] | alt | 116 | 2 | 7 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.69× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -17.2) |
| [[HOP62 (line)]] | alt | 61.8 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +17.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 496 | 1 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -29.4) |
| [[NCI-H2030 (line)]] | alt | 219 | 1 (1 ⚠) | 6 (3 ⚠) | [[Selinexor (drug)]] 5 µM 1.70× (z +8.7) ⚠ cell-cycle shift, explains ~58% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -25.3) |
| [[SW480 (line)]] | alt | 32.1 | 5 (2 ⚠) | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 5.29× (z +14.3) | [[Digitoxin (drug)]] 0.5 µM 0.377× (z -8.9) ⚠ cell-cycle shift, explains ~55% of this change |
| [[NCI-H1792 (line)]] | alt | 112 | 2 | 4 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.82× (z +15.3) | [[Panobinostat (drug)]] 5 µM 0.280× (z -13.1) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -13.1) |
| [[Panc 03.27 (line)]] | alt | 136 | 4 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +16.6) | [[Panobinostat (drug)]] 0.5 µM 0.359× (z -10.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 274 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +23.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -20.4) |
| [[HepG2_C3A (line)]] | wt | 93.5 | 3 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 7.36× (z +16.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -16.0) |
| [[J82 (line)]] | alt | 37.8 | 5 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 4.87× (z +12.8) | — |
| [[NCI-H2347 (line)]] | alt | 87.6 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -15.8) |
| [[A-172 (line)]] | wt | 35.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +11.8) | — |
| [[A498 (line)]] | wt | 87.1 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -14.2) |
| [[C32 (line)]] | wt | 93.1 | 1 | 3 | [[Ixazomib citrate (drug)]] 5 µM 2.51× (z +8.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -11.4) |
| [[Hs 766T (line)]] | wt | 126 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -16.6) |
| [[hTERT-HPNE (line)]] | wt | 28.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.44× (z +17.0) | — |
| [[NCI-H460 (line)]] | wt | 38.0 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +16.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -8.9) |
| [[SHP-77 (line)]] | alt | 31.0 | 2 | 2 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 5.93× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -13.2) |
| [[SNU-423 (line)]] | alt | 64.9 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -15.6) |
| [[BT-474 (line)]] | alt | 27.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.34× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 34.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +12.0) | — |
| [[AN3 CA (line)]] | alt | 70.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 33.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +15.2) | — |
| [[AsPC-1 (line)]] | alt | 42.5 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 4.74× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 34.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 51.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.14× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H661 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.129× (z -9.0) ⚠ transcription drop; cell-cycle shift, explains ~23% of this change |
| [[A-427 (line)]] | wt | 7.05 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 64.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.29 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 19.5 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.73 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 16.4 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.92 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 12.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.43 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.10 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.06 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.87 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 7.84 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.92 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3292), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPS2]] | +0.63 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[TLR6]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[EGF]] | +0.57 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[TLR1]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[EFCAB7]] | +0.56 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[GNGT1]] | +0.55 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[JAKMIP3]] | +0.53 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[PSMA4]] | +0.53 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[SPART]] | +0.53 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[ADAMTS1]] | +0.52 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[ZSCAN31]] | +0.52 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[PTGR1]] | +0.50 | +0.50 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCCD1]] | -0.57 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[CRYGS]] | -0.55 | -0.43 / -0.47 | both halves | 3e-05 | STRING 473 |
| [[ZBED4]] | -0.50 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[WDR27]] | -0.49 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[MCRIP1]] | -0.48 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[FBH1]] | -0.48 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[LINC01128]] | -0.47 | -0.54 / -0.37 | both halves | 9e-05 |  |
| [[FCHO2]] | -0.47 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[CLMP]] | -0.47 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[MAPK1]] | -0.47 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[PLP2]] | -0.47 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[RNF170]] | -0.47 | -0.38 / -0.53 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GCNT2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KIAA1549L]] | B | KIAA1549L activity lowers GCNT2's level | lines that do not express KIAA1549L (20) vs lines expressing it (30) | 1.38× higher at baseline in the lines without KIAA1549L | 0.056 | ⚠ within organs, on part of the lines; also absent: NLRP3, PLPP4, PHACTR1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers GCNT2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CAPRIN2]] | C | CAPRIN2 activity lowers GCNT2's level | lines that do not express CAPRIN2 (3) vs lines expressing it (47) | 2.13× higher at baseline in the lines without CAPRIN2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PALS2, STX2, POLR3G; maybe low, not absent; its own permutation p |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKR1C3]] | B | GCNT2 activity raises AKR1C3's level | lines that do not express GCNT2 (16) vs lines expressing it (34) | 2.57× lower at baseline in the lines without GCNT2 | 0.024 | ⚠ within organs, on part of the lines; also absent: WBP2NL, LOXL2, CSF3 |
| [[TYW3]] | B | GCNT2 activity lowers TYW3's level | lines that do not express GCNT2 (16) vs lines expressing it (34) | 1.34× higher at baseline in the lines without GCNT2 | 0.045 | ⚠ within organs, on part of the lines; also absent: WBP2NL, LOXL2, CSF3 |
| [[AR]] | B | GCNT2 activity raises AR's level | lines that do not express GCNT2 (16) vs lines expressing it (34) | 2.04× lower at baseline in the lines without GCNT2 | 0.073 | ⚠ within organs, on part of the lines; also absent: WBP2NL, LOXL2, CSF3 |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.581). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-6.0, 47.9); signed map (50.1, -8.1). **Vector** length 119, 32.0% of its response variance represented; |z| ≥ 3 in 1,102 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +8.6 | +22.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.1 | +21.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.7 | +17.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +19.1 |
|  | [[NG25 (drug)]] 5 µM |  | +4.3 | +4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.2 | +8.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.1 | +8.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +6.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +3.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -14.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -18.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -9.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.0 | -11.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -3.9 | -8.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.4 | -3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | glucosaminyl (N-acetyl) transferase 2 (I blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.3-p24.2 — chr6:10,492,223-10,629,368 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IGNT, NAGCT1, bA421M1.1, bA360O19.2, ULG3; previously NACGT1, II, GCNT5, CCAT |
| Gene groups (HGNC) | Glucosaminyl (N-acetyl) transferases/xylosyltransferases; Blood group antigens |
| Hallmark sets | XENOBIOTIC_METABOLISM, HYPOXIA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N0V5](https://www.uniprot.org/uniprotkb/Q8N0V5) (N-acetyllactosaminide beta-1,6-N-acetylglucosaminyl-transferase):

> Branching enzyme that converts linear into branched poly-N-acetyllactosaminoglycans. Introduces the blood group I antigen during embryonic development. It is closely associated with the development and maturation of erythroid cells.; [Isoform C]: Determines the expression of the blood group I antigen in erythrocytes.

**Summary**, from NCBI Gene [2651](https://www.ncbi.nlm.nih.gov/gene/2651):

> This gene encodes the enzyme responsible for formation of the blood group I antigen. The i and I antigens are distinguished by linear and branched poly-N-acetyllactosaminoglycans, respectively. The encoded protein is the I-branching enzyme, a beta-1,6-N-acetylglucosaminyltransferase responsible for the conversion of fetal i antigen to adult I antigen in erythrocytes during embryonic development. Mutations in this gene have been associated with adult i blood group phenotype. Alternatively …

**Accessions** — [HGNC:4204](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4204) · Entrez [2651](https://www.ncbi.nlm.nih.gov/gene/2651) · UniProt [Q8N0V5](https://www.uniprot.org/uniprotkb/Q8N0V5) · Ensembl [ENSG00000111846](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111846)

## Data

Gene col 3292: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3292); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3292, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3292]; `tensor/DDL_lfc|DDL_z.npy` [3292]; `embed/gene_vectors.npy` [3292]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3292 or target_col == 3292). Every well: [[GCNT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GCNT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
