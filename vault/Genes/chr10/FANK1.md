---
symbol: "FANK1"
type: "gene"
col: 12788
ensembl_id: "ENSG00000203780"
name: "fibronectin type III and ankyrin repeat domains 1"
location: "10q26.2"
module: 26
arm: "+"
pooled_cpm: 35.15
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 30
n_dd_up_clean: 12
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# FANK1

*fibronectin type III and ankyrin repeat domains 1* — 10q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.55× (z +16.3, q 0e+00, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (13 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.368× (z -12.3, q 7e-32, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM4C]] (+0.64, fdr 7e-06), [[KIAA0753]] (+0.61, fdr 2e-05), [[PRPF18]] (+0.56, fdr 3e-05); moves opposite to [[GNPTAB]] (-0.56, fdr 2e-05), [[NEK3]] (-0.56, fdr 3e-05), [[GRB14]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12788.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.55×** | +16.3 | 0e+00 | 43/46 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +6.6 | 1e-08 | 31/45 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.66×** | +6.0 | 4e-07 | 30/45 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.7 | 3e-04 | 22/46 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.6 | 6e-04 | 20/47 (BT-474, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +4.4 | 0.001 | 22/47 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.35×** | +3.7 | 0.018 | 17/46 (SW480, LOX-IMVI, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.021 | 18/46 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.027 | 19/45 (Panc 03.27, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.044 | 16/47 (NCI-H1573, SW 900, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.052 | 19/46 (A-172, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.092 | 10/46 (CFPAC-1, SW48, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.29×** | +3.1 | 0.092 | 14/48 (NCI-H1573, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 1.60× | +3.0 | 0.11 | 11/47 (LS 180, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12788.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.368×** | -12.3 | 7e-32 | 41/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.374×** | -11.6 | 1e-28 | 41/45 (NCI-H1792, COLO 205, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.417×** | -10.7 | 1e-24 | 38/45 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.442×** | -10.0 | 2e-21 | 36/46 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.565×** | -9.9 | 5e-21 | 42/47 (HT-29, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.489×** | -8.8 | 1e-16 | 39/47 (PANC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.563×** | -6.8 | 9e-10 | 31/47 (SNU-423, C32, …) | two highest doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.596×** | -6.4 | 1e-08 | 29/45 (PANC-1, C-33 A, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.619×** | -5.9 | 2e-07 | 27/46 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.640×** | -5.5 | 2e-06 | 31/46 (HT-29, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.633×** | -5.2 | 1e-05 | 23/40 (SW 900, NCI-H1792, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.659×** | -5.1 | 1e-05 | 23/45 (SNU-423, CFPAC-1, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.682×** | -4.5 | 3e-04 | 24/47 (CFPAC-1, NCI-H1792, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.697×** | -4.4 | 4e-04 | 23/47 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.692×** | -4.4 | 5e-04 | 23/43 (PANC-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.705×** | -4.3 | 6e-04 | 22/46 (PANC-1, RPMI-7951, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.721×** | -4.0 | 0.002 | 23/46 (CFPAC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.745×** | -3.6 | 0.008 | 22/47 (A-427, PANC-1, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.747×** | -3.6 | 0.009 | 22/46 (CFPAC-1, C32, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.814×** | -3.6 | 0.009 | 17/47 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.760×** | -3.4 | 0.018 | 15/46 (HEC-1-A, SHP-77, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.756×** | -3.2 | 0.033 | 14/45 (SNU-423, Panc 03.27, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.702×** | -3.1 | 0.040 | 13/47 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12788. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 180 | 0 | 15 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.198× (z -14.4) |
| [[NCI-H1792 (line)]] | alt | 92.0 | 0 | 6 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0667× (z -17.7) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 21.0 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +14.7) | [[Digitoxin (drug)]] 0.05 µM 0.244× (z -10.5) ⚠ cell-cycle shift, explains ~82% of this change · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.240× (z -9.9) |
| [[SW 900 (line)]] | alt | 61.1 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0431× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.204× (z -9.6) |
| [[C32 (line)]] | wt | 46.1 | 0 | 5 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0916× (z -14.3) ⚠ toxic · without an alert: [[Ponatinib (drug)]] 5 µM 0.252× (z -8.6) |
| [[COLO 205 (line)]] | alt | 56.2 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.117× (z -15.4) ⚠ toxic |
| [[LoVo (line)]] | wt | 15.9 | 2 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.35× (z +16.7) | [[Digitoxin (drug)]] 5 µM 0.213× (z -10.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 27.1 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.127× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.255× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 19.7 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.00× (z +11.1) | [[Harringtonine (drug)]] 0.5 µM 0.210× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 96.6 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +8.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.283× (z -9.6) ⚠ toxic · without an alert: [[Tucidinostat (drug)]] 5 µM 0.429× (z -9.4) |
| [[SNU-423 (line)]] | alt | 50.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -11.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[AN3 CA (line)]] | alt | 33.4 | 0 | 2 | — | [[Bexarotene (drug)]] 0.5 µM 0.0539× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 9.48 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.21× (z +10.5) | [[Digitoxin (drug)]] 5 µM 0.0760× (z -11.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 38.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.124× (z -11.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 74.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0952× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HCT15 (line)]] | alt | 44.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change · without an alert: [[SBI-0640756 (drug)]] 5 µM 0.0482× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 25.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +8.8) | [[Harringtonine (drug)]] 0.5 µM 0.217× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 15.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.91× (z +9.7) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0994× (z -9.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HOP62 (line)]] | alt | 25.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +14.2) | — |
| [[HT-29 (line)]] | alt | 45.0 | 0 | 2 (1 ⚠) | — | [[Tucidinostat (drug)]] 5 µM 0.377× (z -11.4) |
| [[KATO III (line)]] | alt | 17.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +9.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.255× (z -8.6) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 24.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +10.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.193× (z -8.9) ⚠ toxic |
| [[RKO (line)]] | wt | 11.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.07× (z +13.2) | [[Digitoxin (drug)]] 0.5 µM 0.125× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 25.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 14.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +13.3) | — |
| [[A-172 (line)]] | wt | 20.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +8.5) | — |
| [[A-427 (line)]] | wt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0823× (z -14.1) |
| [[A498 (line)]] | wt | 13.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.21× (z +13.6) | — |
| [[A549 (line)]] | wt | 17.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.30× (z +12.1) | — |
| [[CFPAC-1 (line)]] | alt | 46.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -10.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Hs 766T (line)]] | wt | 11.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +9.5) | — |
| [[HS-578T (line)]] | alt | 14.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +10.4) | — |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.19× (z +10.2) | — |
| [[J82 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LOX-IMVI (line)]] | wt | 12.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 30.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 32.5 | 0 | 1 | — | [[venetoclax (drug)]] 5 µM 0.0467× (z -9.5) |
| [[SNU-1 (line)]] | wt | 17.0 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.111× (z -9.1) |
| [[SW1417 (line)]] | alt | 11.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.46× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.65 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12788), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM4C]] | +0.64 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[KIAA0753]] | +0.61 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[PRPF18]] | +0.56 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[DNASE1]] | +0.56 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[CFAP43]] | +0.55 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[LMLN]] | +0.55 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[IFT140]] | +0.55 | +0.37 / +0.60 | both halves | 9e-05 |  |
| [[PIPOX]] | +0.54 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[SYNRG]] | +0.53 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[TTC41P]] | +0.53 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[EFCAB6]] | +0.52 | +0.40 / +0.54 | both halves | 4e-05 |  |
| [[ZCWPW2]] | +0.52 | +0.49 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNPTAB]] | -0.56 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[NEK3]] | -0.56 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[GRB14]] | -0.56 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[C1orf115]] | -0.56 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[ZFAND4]] | -0.54 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[RSAD1]] | -0.54 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[SLC5A4-AS1]] | -0.53 | -0.29 / -0.52 | both halves | 2e-04 |  |
| [[LRRC8B]] | -0.53 | -0.40 / -0.63 | both halves | 5e-05 |  |
| [[ZNF30]] | -0.52 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[CHST10]] | -0.52 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[PPP5C]] | -0.52 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[FDX1]] | -0.52 | -0.38 / -0.59 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FANK1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.442). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-5.1, 18.3); signed map (7.5, 1.4). **Vector** length 95.7, 25.7% of its response variance represented; |z| ≥ 3 in 1,339 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +16.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +6.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +4.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.0 | -4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | -0.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | -2.8 |
|  | [[Sulfatinib (drug)]] 5 µM |  | +1.9 | +1.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -12.2 | -9.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -9.7 | -5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | -5.1 | -3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -1.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | -4.6 | -4.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.5 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | +1.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.3 | -2.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.3 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | fibronectin type III and ankyrin repeat domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.2 — chr10:125,896,564-126,009,592 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Fibronectin type III domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TC84](https://www.uniprot.org/uniprotkb/Q8TC84) (Fibronectin type 3 and ankyrin repeat domains protein 1):

> Through the activation of JUN and AP-1-mediated transcription, may regulate apoptosis.

**Summary**, from NCBI Gene [92565](https://www.ncbi.nlm.nih.gov/gene/92565):

> Involved in negative regulation of apoptotic process; positive regulation of DNA-templated transcription; and positive regulation of apoptotic process. Located in chromatin; cytosol; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23527](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23527) · Entrez [92565](https://www.ncbi.nlm.nih.gov/gene/92565) · UniProt [Q8TC84](https://www.uniprot.org/uniprotkb/Q8TC84) · Ensembl [ENSG00000203780](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203780)

## Data

Gene col 12788: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12788); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12788, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12788]; `tensor/DDL_lfc|DDL_z.npy` [12788]; `embed/gene_vectors.npy` [12788]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12788 or target_col == 12788). Every well: [[FANK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FANK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
