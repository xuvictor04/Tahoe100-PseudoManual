---
symbol: "PRKCA"
type: "gene"
col: 7786
ensembl_id: "ENSG00000154229"
name: "protein kinase C alpha"
location: "17q24.2"
module: 141
arm: "+"
pooled_cpm: 504.71
n_lines_expressing: 45
n_dd_up: 14
n_dd_down: 16
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 11
direction_downstream: 25
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# PRKCA

*protein kinase C alpha* — 17q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.96× (z +16.5, q 0e+00, up in 35 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.567× (z -9.4, q 3e-18, down in 35 of 42 measured lines) ⚠ toxic. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.542× (z -5.5, q 4e-06, down in 32 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZSWIM6]] (+0.57, fdr 1e-05), [[ARHGAP26]] (+0.56, fdr 2e-05), [[EPHB2]] (+0.55, fdr 2e-05); moves opposite to [[ZNF133]] (-0.60, fdr 1e-05), [[RWDD3]] (-0.53, fdr 2e-05), [[ZNF383]] (-0.53, fdr 3e-05).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[ABCC3]] → it (grade B ⚠); 25 go from it, the strongest it → [[ATXN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7786.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +16.5 | 0e+00 | 35/43 (hTERT-HPNE, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +8.3 | 3e-14 | 33/43 (C32, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.32×** | +6.8 | 2e-09 | 24/44 (LoVo, SNU-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.46×** | +6.5 | 9e-09 | 28/43 (hTERT-HPNE, A-427, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.38×** | +5.6 | 2e-06 | 31/43 (A-427, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +5.5 | 4e-06 | 33/43 (hTERT-HPNE, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.2 | 1e-05 | 24/45 (C32, C-33 A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.74×** | +5.0 | 4e-05 | 31/43 (SW480, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.9 | 5e-05 | 19/43 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.30×** | +4.6 | 2e-04 | 23/43 (LoVo, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +4.4 | 6e-04 | 26/43 (C32, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +4.2 | 0.001 | 27/43 (NCI-H23, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.014 | 22/43 (Hs 766T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.036 | 24/44 (hTERT-HPNE, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.049 | 14/43 (SNU-1, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7786.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.567×** | -9.4 | 3e-18 | 35/42 (HepG2/C3A, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.577×** | -9.2 | 2e-17 | 34/44 (COLO 205, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.579×** | -8.7 | 6e-16 | 27/40 (CFPAC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.659×** | -6.9 | 7e-10 | 31/40 (SW480, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.542×** | -5.5 | 4e-06 | 32/44 (H4, Panc 03.27, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.763×** | -4.7 | 3e-04 | 32/43 (SW 1271, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.765×** | -4.6 | 3e-04 | 24/43 (A-172, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.601×** | -4.6 | 3e-04 | 27/35 (Panc 03.27, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.774×** | -4.4 | 6e-04 | 26/43 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.783×** | -4.2 | 0.001 | 24/43 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.843× | -4.1 | 0.002 | 23/44 (HOP62, CHP-212, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.787×** | -4.0 | 0.003 | 27/43 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.795×** | -4.0 | 0.003 | 28/43 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.795×** | -3.9 | 0.003 | 28/43 (LS 180, Panc 03.27, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.804×** | -3.6 | 0.011 | 27/42 (HOP62, AsPC-1, …) | two highest doses |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.885× | -3.0 | 0.081 | 4/44 (SW 1271, AsPC-1, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.839× | -2.9 | 0.094 | 21/43 (SNU-423, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7786. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 335 | 12 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.06× (z +37.1) | — |
| [[C32 (line)]] | wt | 234 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.19× (z +34.6) | — |
| [[SNU-1 (line)]] | wt | 212 | 9 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +20.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.435× (z -8.5) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 549 | 5 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +13.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.431× (z -11.0) ⚠ toxic |
| [[A-172 (line)]] | wt | 279 | 8 (4 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +13.5) | — |
| [[CFPAC-1 (line)]] | alt | 1,001 | 1 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.460× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 843 | 0 | 7 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.198× (z -16.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.424× (z -13.1) |
| [[HOP62 (line)]] | alt | 972 | 2 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.352× (z -10.7) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.394× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 415 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +26.0) | — |
| [[LoVo (line)]] | wt | 194 | 6 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +21.7) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.29× (z +14.3) | — |
| [[LOX-IMVI (line)]] | wt | 403 | 5 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +23.9) | [[Dinaciclib (drug)]] 0.05 µM 0.446× (z -10.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 419 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +17.9) | [[Lonafarnib (drug)]] 5 µM 0.115× (z -13.4) ⚠ toxic |
| [[SW480 (line)]] | alt | 608 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +20.6) | [[Dinaciclib (drug)]] 0.05 µM 0.432× (z -12.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 394 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +17.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.437× (z -9.4) ⚠ toxic |
| [[LS 180 (line)]] | wt | 344 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.409× (z -10.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 2,137 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -18.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 605 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +16.9) | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -10.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 375 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.485× (z -10.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 872 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 708 | 0 | 4 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.405× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 1,033 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -12.8) ⚠ cell-cycle shift, explains ~18% of this change |
| [[NCI-H2030 (line)]] | alt | 418 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.318× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 249 | 3 (1 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.12× (z +9.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.10× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.405× (z -11.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 248 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.18× (z +11.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[A498 (line)]] | wt | 673 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +17.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.454× (z -8.6) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 399 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +19.4) | — |
| [[C-33 A (line)]] | alt | 216 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +17.2) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +12.8) | — |
| [[H4 (line)]] | wt | 482 | 3 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +11.4) | — |
| [[HCT15 (line)]] | alt | 224 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +15.6) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[SW 900 (line)]] | alt | 738 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.385× (z -10.9) ⚠ toxic |
| [[SW1417 (line)]] | alt | 296 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +19.2) | — |
| [[CHP-212 (line)]] | wt | 1,436 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.319× (z -8.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 269 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +16.8) | — |
| [[A549 (line)]] | wt | 835 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -9.1) ⚠ cell-cycle shift, explains ~18% of this change |
| [[AN3 CA (line)]] | alt | 286 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +13.3) | — |
| [[HS-578T (line)]] | alt | 535 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 440 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.387× (z -8.9) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 551 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +11.1) | — |
| [[SW 1088 (line)]] | alt | 526 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +9.8) | — |
| [[SW 1271 (line)]] | alt | 823 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.275× (z -9.0) ⚠ transcription drop |
| [[SW48 (line)]] | wt | 286 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.5) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[BT-474 (line)]] | alt | 589 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 113 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 447 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 512 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.8 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 473 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 113 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 76.1 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7786), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSWIM6]] | +0.57 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[ARHGAP26]] | +0.56 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[EPHB2]] | +0.55 | +0.54 / +0.47 | both halves | 2e-05 | same gene group |
| [[TIAM1]] | +0.53 | +0.54 / +0.47 | both halves | 2e-05 | STRING 452 |
| [[KLF12]] | +0.53 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[PFN1]] | +0.52 | +0.54 / +0.42 | both halves | 4e-05 | pathway: Beta-catenin independent WNT signaling |
| [[ITGA6]] | +0.52 | +0.46 / +0.52 | both halves | 3e-05 | pathway: Extracellular matrix organization; STRING 565 |
| [[HOMER1]] | +0.52 | +0.46 / +0.54 | both halves | 2e-05 | pathway: Neuronal System; STRING 465 |
| [[ATXN1]] | +0.51 | +0.48 / +0.43 | both halves | 4e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[CCNYL1]] | +0.51 | +0.54 / +0.48 | both halves | 2e-05 | same gene group |
| [[FRYL]] | +0.51 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[STIM2]] | +0.51 | +0.47 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF133]] | -0.60 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[RWDD3]] | -0.53 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[ZNF383]] | -0.53 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[METTL22]] | -0.53 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[FOXO3B]] | -0.52 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[SNX4]] | -0.52 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[TMLHE]] | -0.52 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[ZW10]] | -0.51 | -0.56 / -0.46 | both halves | 3e-05 | pathway: RHO GTPase Effectors |
| [[FPGT]] | -0.51 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[ZNF329]] | -0.51 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[RTCA]] | -0.51 | -0.53 / -0.42 | both halves | 4e-05 | same gene group |
| [[ZNF112]] | -0.50 | -0.52 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCC3]] | B | ABCC3 activity raises PRKCA's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 2.44× lower at baseline in the lines without ABCC3 | 0.004 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[ATXN1]] | B | ATXN1 activity raises PRKCA's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 2.85× lower at baseline in the lines without ATXN1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |
| [[ATP1B1]] | B | ATP1B1 activity raises PRKCA's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 2.44× lower at baseline in the lines without ATP1B1 | 0.008 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[SMAD3]] | B | SMAD3 activity raises PRKCA's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 2.72× lower at baseline in the lines without SMAD3 | 0.013 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[IL1RAP]] | B | IL1RAP activity raises PRKCA's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 2.43× lower at baseline in the lines without IL1RAP | 0.028 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[ITGA6]] | B | ITGA6 activity raises PRKCA's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 1.59× lower at baseline in the lines without ITGA6 | 0.058 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ABCC3]] | B | ABCC3 activity strengthens PRKCA's drug response | lines that do not express ABCC3 (11) vs lines expressing it (33) | the lines without ABCC3 respond 0.96× as strongly (z diff +0.01); strongest at Dinaciclib 5 µM: 1.01x vs 0.56x (z diff +5.9) | 0.068 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL; target measured in part of the lines; both ways; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers PRKCA's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FRG1DP]] | B | FRG1DP activity raises PRKCA's level | lines that do not express FRG1DP (17) vs lines expressing it (33) | 1.65× lower at baseline in the lines without FRG1DP | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000237596, C9, GLIPR1 |
| [[SYNJ2]] | C | SYNJ2 activity raises PRKCA's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 2.38× lower at baseline in the lines without SYNJ2 | 0.050 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |
| [[SLC4A7]] | C | SLC4A7 activity lowers PRKCA's level | lines that do not express SLC4A7 (3) vs lines expressing it (47) | 2.56× higher at baseline in the lines without SLC4A7 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: USP31, CSPG5, NR4A3; maybe low, not absent; its own permutation p |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 25, C 0. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATXN1]] | B | PRKCA activity raises ATXN1's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 4.79× lower at baseline in the lines without PRKCA | 7e-04 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[ITGA6]] | B | PRKCA activity raises ITGA6's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 3.78× lower at baseline in the lines without PRKCA | 0.006 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[SYNJ2]] | B | PRKCA activity raises SYNJ2's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 3.11× lower at baseline in the lines without PRKCA | 0.008 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[FOXO3B]] | B | PRKCA activity lowers FOXO3B's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 1.82× higher at baseline in the lines without PRKCA | 0.011 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[IRAK1BP1]] | B | PRKCA activity lowers IRAK1BP1's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 2.57× higher at baseline in the lines without PRKCA | 0.014 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[ABCC3]] | B | PRKCA activity raises ABCC3's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 5.35× lower at baseline in the lines without PRKCA | 0.018 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[TSPAN5]] | B | PRKCA activity raises TSPAN5's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 3.85× lower at baseline in the lines without PRKCA | 0.020 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[PDLIM5]] | B | PRKCA activity raises PDLIM5's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 2.44× lower at baseline in the lines without PRKCA | 0.021 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[ITPRID2]] | B | PRKCA activity raises ITPRID2's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 1.89× lower at baseline in the lines without PRKCA | 0.025 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[SMAD3]] | B | PRKCA activity raises SMAD3's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 2.73× lower at baseline in the lines without PRKCA | 0.025 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[SHB]] | B | PRKCA activity raises SHB's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 2.26× lower at baseline in the lines without PRKCA | 0.039 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[ZNF383]] | B | PRKCA activity lowers ZNF383's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 1.91× higher at baseline in the lines without PRKCA | 0.068 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.464). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-14.7, 27.8); signed map (2.0, 42.5). **Vector** length 122, 39.6% of its response variance represented; |z| ≥ 3 in 1,530 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.9 | +3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +5.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.5 | +3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +16.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +4.9 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | +2.6 | +1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +2.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -10.3 | -9.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.6 | -3.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -6.3 | -4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.2 | -4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.4 | -8.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.3 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.0 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.9 | -4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase C alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q24.2 — chr17:66,302,613-66,810,743 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PKCα; previously PKCA |
| Gene groups (HGNC) | C2 domain containing protein kinases; MicroRNA protein coding host genes; Protein kinase C family |
| Hallmark sets | NOTCH_SIGNALING, UV_RESPONSE_DN, HYPOXIA |
| Reactome | 66 pathways, smallest: Disinhibition of SNARE formation; ROBO receptors bind AKAP5; EGFR Transactivation by Gastrin |
| Matched by | ensembl_id |

**Function**, from UniProt [P17252](https://www.uniprot.org/uniprotkb/P17252) (Protein kinase C alpha type):

> Calcium-activated, phospholipid- and diacylglycerol (DAG)-dependent serine/threonine-protein kinase that is involved in positive and negative regulation of cell proliferation, apoptosis, differentiation, migration and adhesion, tumorigenesis, cardiac hypertrophy, angiogenesis, platelet function and inflammation, by directly phosphorylating targets such as RAF1, BCL2, CSPG4, TNNT2/CTNT, or activating signaling cascade involving MAPK1/3 (ERK1/2) and RAP1GAP. Involved in cell proliferation and …

**Summary**, from NCBI Gene [5578](https://www.ncbi.nlm.nih.gov/gene/5578):

> Protein kinase C (PKC) is a family of serine- and threonine-specific protein kinases that can be activated by calcium and the second messenger diacylglycerol. PKC family members phosphorylate a wide variety of protein targets and are known to be involved in diverse cellular signaling pathways. PKC family members also serve as major receptors for phorbol esters, a class of tumor promoters. Each member of the PKC family has a specific expression profile and is believed to play a distinct role in …

**Accessions** — [HGNC:9393](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9393) · Entrez [5578](https://www.ncbi.nlm.nih.gov/gene/5578) · UniProt [P17252](https://www.uniprot.org/uniprotkb/P17252) · Ensembl [ENSG00000154229](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154229)

## Data

Gene col 7786: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7786); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7786, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7786]; `tensor/DDL_lfc|DDL_z.npy` [7786]; `embed/gene_vectors.npy` [7786]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7786 or target_col == 7786). Every well: [[PRKCA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKCA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
