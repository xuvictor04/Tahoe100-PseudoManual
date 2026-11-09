---
symbol: "L3MBTL1"
type: "gene"
col: 11691
ensembl_id: "ENSG00000185513"
name: "L3MBTL histone methyl-lysine binding protein 1"
location: "20q13.12"
module: 37
arm: "+"
pooled_cpm: 33.59
n_lines_expressing: 43
n_dd_up: 11
n_dd_down: 18
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# L3MBTL1

*L3MBTL histone methyl-lysine binding protein 1* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.30× (z +21.7, q 0e+00, up in 37 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (13 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.446× (z -14.1, q 1e-42, down in 35 of 40 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.649× (z -7.9, q 4e-13, down in 28 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGK2]] (+0.65, fdr 7e-06, ⚠ same locus), [[SNX31]] (+0.65, fdr 1e-05), [[ZNF529-AS1]] (+0.63, fdr 4e-05), [[C9orf153]] (+0.63, fdr 2e-05); moves opposite to [[AKAP11]] (-0.56, fdr 8e-05), [[SSX2IP]] (-0.54, fdr 1e-04), [[MDM1]] (-0.53, fdr 6e-04).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC02609]] → it (grade B ⚠); 3 go from it, the strongest it → [[LINC02609]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11691.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.30×** | +21.7 | 0e+00 | 37/41 (LoVo, HT-29, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +14.3 | 5e-44 | 32/41 (SNU-423, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.9 | 5e-07 | 21/41 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.22×** | +5.2 | 3e-05 | 20/41 (J82, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.69×** | +5.0 | 7e-05 | 19/39 (A498, RPMI-7951, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +4.7 | 2e-04 | 18/39 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.5 | 5e-04 | 14/41 (SW1417, NCI-H2030, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.25×** | +4.0 | 0.004 | 14/41 (A498, H4, …) | all doses, stronger at high dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.22×** | +3.6 | 0.018 | 11/40 (CFPAC-1, RKO, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.028 | 15/41 (SW1417, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.15× | +3.5 | 0.028 | 4/41 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.4 | 0.033 | 18/40 (LoVo, NCI-H1792, …) | top dose only | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | 1.20× | +3.3 | 0.039 | 8/41 (A498, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.3 | 0.039 | 13/41 (A549, NCI-H460, …) | rises with dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.045 | 7/41 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.20×** | +3.2 | 0.046 | 9/41 (SW480, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11691.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.446×** | -14.1 | 1e-42 | 35/40 (PANC-1, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.497×** | -12.7 | 2e-34 | 31/38 (HCT15, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.509×** | -11.8 | 6e-30 | 20/31 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.617×** | -8.1 | 7e-14 | 24/34 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.642×** | -8.1 | 9e-14 | 28/41 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.649×** | -7.9 | 4e-13 | 28/41 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.441×** | -7.8 | 6e-13 | 22/41 (PANC-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.657×** | -7.6 | 2e-12 | 26/40 (PANC-1, Hs 766T, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.745×** | -5.3 | 6e-06 | 22/41 (PANC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~62% of this change | **0.757×** | -4.8 | 7e-05 | 21/40 (NCI-H23, RKO, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.770×** | -4.7 | 1e-04 | 21/41 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.772×** | -4.7 | 1e-04 | 19/41 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.776×** | -4.6 | 2e-04 | 15/41 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.622×** | -4.5 | 3e-04 | 15/41 (NCI-H23, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.791×** | -4.3 | 8e-04 | 19/40 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.705×** | -3.3 | 0.030 | 15/40 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Sonidegib (drug)]] 0.5 µM |  | **0.791×** | -3.0 | 0.077 | 8/41 (HCT15, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Raltitrexed (drug)]] 0.5 µM |  | 0.850× | -2.9 | 0.099 | 10/41 (MIA PaCa-2, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11691. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 52.8 | 0 | 13 (11 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.156× (z -23.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.420× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 54.7 | 1 | 5 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.84× (z +12.9) | [[Dinaciclib (drug)]] 0.05 µM 0.366× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.470× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 75.2 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.353× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 33.0 | 2 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.273× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[A-172 (line)]] | wt | 35.4 | 1 | 4 (3 ⚠) | [[Auranofin (drug)]] 5 µM 3.69× (z +11.1) | [[Harringtonine (drug)]] 5 µM 0.240× (z -11.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.293× (z -10.4) |
| [[A-427 (line)]] | wt | 43.4 | 1 | 4 (3 ⚠) | [[Auranofin (drug)]] 5 µM 3.75× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -19.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.146× (z -9.0) |
| [[Hs 766T (line)]] | wt | 66.2 | 0 | 5 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.228× (z -12.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A498 (line)]] | wt | 32.9 | 1 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 3.30× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[HepG2_C3A (line)]] | wt | 50.5 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.221× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.245× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 116 | 1 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.15× (z +8.8) | [[Harringtonine (drug)]] 5 µM 0.335× (z -12.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[C32 (line)]] | wt | 18.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +11.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.81× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.183× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[HS-578T (line)]] | alt | 40.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[NCI-H460 (line)]] | wt | 22.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 6.00× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.137× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[RPMI-7951 (line)]] | alt | 28.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 5.37× (z +10.0) | — |
| [[SW 900 (line)]] | alt | 20.5 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 5.80× (z +11.1) | [[Harringtonine (drug)]] 5 µM 0.202× (z -9.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[CFPAC-1 (line)]] | alt | 38.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 24.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 12.5× (z +18.9) | — |
| [[J82 (line)]] | alt | 23.9 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.65× (z +9.9) | — |
| [[LoVo (line)]] | wt | 14.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.07× (z +21.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 17.1× (z +19.2) | — |
| [[NCI-H2347 (line)]] | alt | 24.2 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.71× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 42.4 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.190× (z -14.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RKO (line)]] | wt | 24.4 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 6.20× (z +10.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.207× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~62% of this change |
| [[SK-MEL-2 (line)]] | alt | 27.1 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 6.14× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[SNU-423 (line)]] | alt | 22.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 9.11× (z +15.0) | — |
| [[SW1417 (line)]] | alt | 64.4 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.27× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.410× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[SW480 (line)]] | alt | 38.3 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.34× (z +16.9) | [[Harringtonine (drug)]] 5 µM 0.345× (z -11.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A549 (line)]] | wt | 10.8 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.160× (z -9.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[AN3 CA (line)]] | alt | 23.4 | 0 | 1 | — | [[Benproperine (phosphate) (drug)]] 5 µM 0.0777× (z -8.9) |
| [[C-33 A (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[H4 (line)]] | wt | 34.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[HCT15 (line)]] | alt | 56.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0968× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[NCI-H1792 (line)]] | alt | 20.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.91× (z +15.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 49.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SHP-77 (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.171× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SW 1271 (line)]] | alt | 47.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0581× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 20.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +10.4) | — |
| [[AsPC-1 (line)]] | alt | 5.98 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.83 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.00 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.38 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.45 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.17 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 48.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11691), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGK2]] | +0.65 | +0.59 / +0.68 | both halves | 7e-06 | STRING 430; ⚠ same locus (8.0 kb, same strand: neighbours can correlate without regulation) |
| [[SNX31]] | +0.65 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[ZNF529-AS1]] | +0.63 | +0.41 / +0.69 | both halves | 4e-05 |  |
| [[C9orf153]] | +0.63 | +0.46 / +0.69 | both halves | 2e-05 |  |
| [[OOEP]] | +0.62 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[EXD3]] | +0.62 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[LINC02646]] | +0.61 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[PPP1R26-AS1]] | +0.61 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[CAPN10-DT]] | +0.60 | +0.22 / +0.69 | both halves | 6e-04 |  |
| [[TNXB]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[PHKG1]] | +0.60 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[NOXRED1]] | +0.60 | +0.42 / +0.67 | both halves | 4e-05 |  |
| [[SEPTIN1]] | +0.60 | +0.50 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP11]] | -0.56 | -0.37 / -0.60 | both halves | 8e-05 |  |
| [[SSX2IP]] | -0.54 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[MDM1]] | -0.53 | -0.22 / -0.50 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02609]] | B | LINC02609 activity raises L3MBTL1's level | lines that do not express LINC02609 (6) vs lines expressing it (44) | 2.31× lower at baseline in the lines without LINC02609 | 0.063 | ⚠ within organs, on part of the lines; also absent: TPST1, HLTF, FERMT2; maybe low, not absent |
| [[SGK2]] | C | SGK2 activity raises L3MBTL1's level | lines that do not express SGK2 (5) vs lines expressing it (45) | 3.38× lower at baseline in the lines without SGK2 | 0.080 | ⚠ within organs, on part of the lines; also absent: IGF2BP2, ADORA2B, ARSD; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02609]] | B | L3MBTL1 activity raises LINC02609's level | lines that do not express L3MBTL1 (7) vs lines expressing it (43) | 2.01× lower at baseline in the lines without L3MBTL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000277611, DNAJC18, COPZ2; maybe low, not absent |
| [[CDKL3]] | B | L3MBTL1 activity raises CDKL3's level | lines that do not express L3MBTL1 (7) vs lines expressing it (43) | 1.75× lower at baseline in the lines without L3MBTL1 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000277611, DNAJC18, COPZ2; maybe low, not absent |
| [[SGK2]] | C | L3MBTL1 activity raises SGK2's level | lines that do not express L3MBTL1 (7) vs lines expressing it (43) | 2.09× lower at baseline in the lines without L3MBTL1 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000277611, DNAJC18, COPZ2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.666). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.7, -16.8); signed map (6.7, 9.3). **Vector** length 96.2, 22.4% of its response variance represented; |z| ≥ 3 in 941 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +12.0 | +21.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +14.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.3 | +5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.5 | +4.7 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +2.8 | +3.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.6 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +3.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.0 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -6.4 | -14.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.3 | -7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | -3.1 | -12.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -5.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.9 | -7.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | +0.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | -1.9 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.7 | -0.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | L3MBTL histone methyl-lysine binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:43,489,442-43,550,954 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZC2HC3, dJ138B7.3, DKFZp586P1522, KIAA0681; previously L3MBTL |
| Gene groups (HGNC) | Sterile alpha motif domain containing; Zinc fingers C2H2C-type; MBT domain containing |
| Reactome | 3 pathways, smallest: Regulation of TP53 Activity through Methylation; Regulation of TP53 Activity; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y468](https://www.uniprot.org/uniprotkb/Q9Y468) (Lethal(3)malignant brain tumor-like protein 1):

> Polycomb group (PcG) protein that specifically recognizes and binds mono- and dimethyllysine residues on target proteins, thereby acting as a 'reader' of a network of post-translational modifications. PcG proteins maintain the transcriptionally repressive state of genes: acts as a chromatin compaction factor by recognizing and binding mono- and dimethylated histone H1b/H1-4 at 'Lys-26' (H1bK26me1 and H1bK26me2) and histone H4 at 'Lys-20' (H4K20me1 and H4K20me2), leading to condense chromatin …

**Summary**, from NCBI Gene [26013](https://www.ncbi.nlm.nih.gov/gene/26013):

> This gene represents a polycomb group gene. The encoded protein functions to regulate gene activity, likely via chromatin modification. The encoded protein may also be necessary for mitosis. Alternatively spliced transcript variants encoding different isoforms have been identified.[provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:15905](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15905) · Entrez [26013](https://www.ncbi.nlm.nih.gov/gene/26013) · UniProt [Q9Y468](https://www.uniprot.org/uniprotkb/Q9Y468) · Ensembl [ENSG00000185513](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185513)

## Data

Gene col 11691: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11691); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11691, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11691]; `tensor/DDL_lfc|DDL_z.npy` [11691]; `embed/gene_vectors.npy` [11691]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11691 or target_col == 11691). Every well: [[L3MBTL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/L3MBTL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
