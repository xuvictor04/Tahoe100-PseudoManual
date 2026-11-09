---
symbol: "ATP9A"
type: "gene"
col: 615
ensembl_id: "ENSG00000054793"
name: "ATPase phospholipid transporting 9A"
location: "20q13.2"
module: 232
arm: "+"
pooled_cpm: 100.38
n_lines_expressing: 46
n_dd_up: 9
n_dd_down: 29
n_dd_up_clean: 6
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/232"]
generated_by: "tahoemap"
---

# ATP9A

*ATPase phospholipid transporting 9A* — 20q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.40× (z +6.2, q 2e-07, up in 31 of 43 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.26× (z +4.5, q 0.002, up in 25 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.205× (z -30.4, q 0e+00, down in 43 of 44 measured lines).
> Its strongest partners by |cos| (76 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RMND5A]] (+0.57, fdr 2e-04), [[GABARAPL1]] (+0.52, fdr 2e-04), [[IQCE]] (+0.50, fdr 1e-04); moves opposite to [[ZNF215]] (-0.51, fdr 4e-04), [[ELP3]] (-0.50, fdr 1e-04), [[PIBF1]] (-0.47, fdr 1e-04).
> It is in [[Module 232]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MYO5B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 615.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.40×** | +6.2 | 2e-07 | 31/43 (LoVo, HT-29, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +4.5 | 0.002 | 25/43 (NCI-H2030, LoVo, …) | rises with dose | low cells (technical?) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.61×** | +4.3 | 0.003 | 22/46 (A-427, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.56×** | +4.1 | 0.007 | 21/44 (LoVo, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.16× | +4.0 | 0.009 | 10/44 (HOP62, AsPC-1, …) | rises with dose |  |
| [[AZD-8055 (drug)]] 5 µM |  | **1.51×** | +3.8 | 0.016 | 16/45 (LoVo, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.26×** | +3.4 | 0.047 | 18/46 (HepG2/C3A, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.048 | 19/45 (LoVo, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.25×** | +3.3 | 0.051 | 14/44 (LoVo, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.2 | 0.068 | 14/44 (A-427, HepG2/C3A, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +3.2 | 0.080 | 10/44 (KATO III, Hs 766T, …) | top dose only |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.090 | 12/44 (LoVo, Hs 766T, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 18 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 615.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.205×** | -30.4 | 0e+00 | 43/44 (AsPC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.235×** | -27.7 | 0e+00 | 42/44 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.238×** | -27.5 | 0e+00 | 43/44 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.369×** | -19.1 | 0e+00 | 43/44 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.468×** | -14.5 | 1e-45 | 41/44 (Panc 03.27, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.623×** | -12.8 | 2e-35 | 30/44 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.523×** | -11.9 | 7e-31 | 35/43 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.679×** | -10.4 | 1e-23 | 30/45 (C-33 A, HT-29, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.631×** | -8.5 | 2e-15 | 36/44 (C-33 A, NCI-H460, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.408×** | -8.2 | 2e-14 | 36/45 (CFPAC-1, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.654×** | -7.8 | 3e-13 | 32/46 (C-33 A, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.694×** | -7.0 | 1e-10 | 26/44 (RPMI-7951, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.726×** | -6.1 | 4e-08 | 23/44 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.799×** | -6.0 | 7e-08 | 25/44 (NCI-H2347, HT-29, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.801×** | -6.0 | 9e-08 | 23/44 (Hs 766T, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.528×** | -5.8 | 2e-07 | 32/44 (Panc 03.27, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.831×** | -5.0 | 2e-05 | 23/44 (BT-474, C-33 A, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.806×** | -4.1 | 0.001 | 23/45 (HOP62, C-33 A, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.659×** | -3.8 | 0.003 | 18/44 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.677×** | -3.5 | 0.009 | 19/44 (NCI-H460, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.697×** | -3.3 | 0.022 | 19/43 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.796×** | -3.1 | 0.039 | 13/44 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.850× | -3.1 | 0.040 | 18/44 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.65 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 615. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 355 | 0 | 11 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.127× (z -21.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.167× (z -18.5) |
| [[CFPAC-1 (line)]] | alt | 151 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.121× (z -24.1) |
| [[HT-29 (line)]] | alt | 180 | 0 | 11 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0959× (z -24.7) |
| [[NCI-H460 (line)]] | wt | 132 | 0 | 11 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -24.8) |
| [[NCI-H1573 (line)]] | alt | 106 | 0 | 10 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.128× (z -24.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.148× (z -22.9) |
| [[NCI-H2347 (line)]] | alt | 128 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -20.6) |
| [[Panc 03.27 (line)]] | alt | 92.9 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.116× (z -21.2) |
| [[HepG2_C3A (line)]] | wt | 161 | 0 | 9 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -17.0) |
| [[NCI-H1792 (line)]] | alt | 176 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0950× (z -26.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.140× (z -21.7) |
| [[SW480 (line)]] | alt | 77.4 | 0 | 9 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.198× (z -17.2) |
| [[Hs 766T (line)]] | wt | 184 | 1 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.8) ⚠ cell-cycle shift, explains ~43% of this change | [[Panobinostat (drug)]] 0.5 µM 0.199× (z -16.5) |
| [[SW 900 (line)]] | alt | 178 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -19.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.157× (z -17.4) |
| [[A-172 (line)]] | wt | 76.1 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -17.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.187× (z -16.6) |
| [[AsPC-1 (line)]] | alt | 208 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.102× (z -26.9) |
| [[BT-474 (line)]] | alt | 323 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.149× (z -25.0) |
| [[COLO 205 (line)]] | alt | 225 | 0 | 7 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.110× (z -21.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.143× (z -18.8) |
| [[HS-578T (line)]] | alt | 71.8 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -16.9) |
| [[MIA PaCa-2 (line)]] | alt | 29.3 | 0 | 7 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.158× (z -14.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.215× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 111 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -19.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -15.0) |
| [[SNU-423 (line)]] | alt | 98.3 | 0 | 7 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.112× (z -22.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.204× (z -16.2) |
| [[SW1417 (line)]] | alt | 255 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.160× (z -24.4) |
| [[KATO III (line)]] | alt | 140 | 1 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +11.6) ⚠ cell-cycle shift, explains ~43% of this change | [[Panobinostat (drug)]] 0.5 µM 0.145× (z -21.7) |
| [[J82 (line)]] | alt | 61.4 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -10.3) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.325× (z -9.8) |
| [[LS 180 (line)]] | wt | 69.6 | 0 | 5 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.150× (z -17.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.186× (z -15.2) |
| [[SW48 (line)]] | wt | 70.3 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.148× (z -13.8) |
| [[A-427 (line)]] | wt | 201 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.231× (z -17.0) |
| [[C32 (line)]] | wt | 98.5 | 0 | 4 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.188× (z -16.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.205× (z -16.0) |
| [[HEC-1-A (line)]] | alt | 43.9 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -16.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.214× (z -15.2) |
| [[LoVo (line)]] | wt | 72.3 | 0 | 4 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.123× (z -24.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.143× (z -22.5) |
| [[NCI-H2030 (line)]] | alt | 114 | 0 | 4 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.259× (z -15.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.307× (z -13.1) |
| [[A549 (line)]] | wt | 60.1 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.244× (z -13.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.297× (z -11.8) |
| [[AN3 CA (line)]] | alt | 141 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.257× (z -9.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.271× (z -8.8) |
| [[HOP62 (line)]] | alt | 55.1 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.296× (z -11.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.375× (z -9.5) |
| [[RKO (line)]] | wt | 38.3 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.288× (z -9.5) |
| [[SHP-77 (line)]] | alt | 42.4 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.258× (z -10.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A498 (line)]] | wt | 22.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.5 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.2 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.78 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 615), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RMND5A]] | +0.57 | +0.31 / +0.49 | both halves | 2e-04 |  |
| [[GABARAPL1]] | +0.52 | +0.32 / +0.51 | both halves | 2e-04 |  |
| [[IQCE]] | +0.50 | +0.33 / +0.48 | both halves | 1e-04 |  |
| [[SQSTM1]] | +0.50 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[DSC2]] | +0.48 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[OCLN]] | +0.47 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[VSIG10]] | +0.47 | +0.34 / +0.35 | both halves | 1e-04 |  |
| [[BAG1]] | +0.47 | +0.36 / +0.50 | both halves | 9e-05 |  |
| [[YPEL5]] | +0.47 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[RC3H1]] | +0.47 | +0.44 / +0.38 | both halves | 6e-05 |  |
| [[RNF103]] | +0.46 | +0.33 / +0.41 | both halves | 1e-04 |  |
| [[CASTOR3P-1]] | +0.46 | +0.22 / +0.45 | both halves | 6e-04 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF215]] | -0.51 | -0.26 / -0.49 | both halves | 4e-04 |  |
| [[ELP3]] | -0.50 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[PIBF1]] | -0.47 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[RARS1]] | -0.46 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[PDSS1]] | -0.46 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[CUZD1]] | -0.46 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[MRPL17]] | -0.45 | -0.23 / -0.48 | both halves | 5e-04 |  |
| [[XPO6]] | -0.45 | -0.19 / -0.49 | ⚠ not reproduced | 8e-04 |  |
| [[SLC25A32]] | -0.45 | -0.22 / -0.40 | both halves | 6e-04 |  |
| [[SRBD1]] | -0.45 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[AASDH]] | -0.44 | -0.33 / -0.58 | both halves | 1e-04 |  |
| [[POLR3A]] | -0.44 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[WDR89]] | -0.44 | -0.29 / -0.50 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO5B]] | B | MYO5B activity raises ATP9A's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 1.84× lower at baseline in the lines without MYO5B | 0.012 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[DSC2]] | B | DSC2 activity raises ATP9A's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 2.03× lower at baseline in the lines without DSC2 | 0.023 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |
| [[MTUS1-DT]] | B | MTUS1-DT activity raises ATP9A's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 2.12× lower at baseline in the lines without MTUS1-DT | 0.026 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[TOP2A]] | B | TOP2A activity raises ATP9A's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MTOR]] | B | MTOR activity lowers ATP9A's level | compounds that target MTOR: 3 of 8 raise it (AZD-8055, Bimiralisib, Sapanisertib) | 38% of the class's compounds vs 1.7% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[GUCY1A2]] | B | GUCY1A2 activity lowers ATP9A's level | lines that do not express GUCY1A2 (8) vs lines expressing it (42) | 1.33× higher at baseline in the lines without GUCY1A2 | 0.092 | ⚠ within organs, on part of the lines; also absent: ZNF559, ENSG00000229195, LINC02456; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 232]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-14.2, -50.1); signed map (-0.5, 14.7). **Vector** length 89.1, 23.7% of its response variance represented; |z| ≥ 3 in 1,414 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.5 | -2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +8.3 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.6 | -1.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.4 | -2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +5.4 | -10.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +0.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +4.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.7 | +4.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -2.9 | -6.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.6 | -3.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -2.4 | -3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -3.8 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.9 | -2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ATPase phospholipid transporting 9A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.2 — chr20:51,596,514-51,768,390 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0611, ATPIIA |
| Gene groups (HGNC) | ATPase phospholipid transporting |
| Reactome | 3 pathways, smallest: Ion transport by P-type ATPases; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [O75110](https://www.uniprot.org/uniprotkb/O75110) (Probable phospholipid-transporting ATPase IIA):

> Plays a role in regulating membrane trafficking of cargo proteins, namely endosome to plasma membrane recycling, probably acting through RAB5 and RAB11 activation. Also involved in endosome to trans-Golgi network retrograde transport. In complex with MON2 and DOP1B, regulates SNX3 retromer-mediated endosomal sorting of WLS, a transporter of Wnt morphogens in developing tissues. Participates in the formation of endosomal carriers that direct WLS trafficking back to Golgi, away from lysosomal …

**Summary**, from NCBI Gene [10079](https://www.ncbi.nlm.nih.gov/gene/10079):

> Enables protease binding activity. Involved in negative regulation of exosomal secretion; regulation of endocytic recycling; and regulation of retrograde transport, endosome to Golgi. Located in several cellular components, including endosome; perinuclear region of cytoplasm; and trans-Golgi network membrane. Implicated in neurodevelopmental disorder with poor growth and behavioral abnormalities. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13540](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13540) · Entrez [10079](https://www.ncbi.nlm.nih.gov/gene/10079) · UniProt [O75110](https://www.uniprot.org/uniprotkb/O75110) · Ensembl [ENSG00000054793](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000054793)

## Data

Gene col 615: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 615); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 615, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 615]; `tensor/DDL_lfc|DDL_z.npy` [615]; `embed/gene_vectors.npy` [615]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 615 or target_col == 615). Every well: [[ATP9A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP9A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
