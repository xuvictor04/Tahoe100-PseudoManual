---
symbol: "CAMKMT"
type: "gene"
col: 6822
ensembl_id: "ENSG00000143919"
name: "calmodulin-lysine N-methyltransferase"
location: "2p21"
module: 18
arm: "+"
pooled_cpm: 179.66
n_lines_expressing: 48
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# CAMKMT

*calmodulin-lysine N-methyltransferase* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.93× (z +13.6, q 3e-39, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.554× (z -11.7, q 4e-29, down in 29 of 42 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H23 0.196×, SNU-1 0.151×, A-427 0.222×, PANC-1 0.329×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (C-33 A 0.118×, NCI-H23 0.143×, PANC-1 0.282×, A-427 0.210×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (LoVo 0.303×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (SNU-1 0.378×); [[Harringtonine (drug)]] 0.05 µM in 1 line (SNU-1 0.381×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VWA8]] (+0.65, fdr 7e-06), [[CDIN1]] (+0.64, fdr 7e-06), [[MDN1]] (+0.62, fdr 1e-05); moves opposite to [[CHMP4B]] (-0.49, fdr 3e-05), [[FBXO48]] (-0.48, fdr 1e-04), [[AXL]] (-0.47, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NFIA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6822.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.93×** | +13.6 | 3e-39 | 42/46 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +12.6 | 5e-34 | 42/46 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.80×** | +12.2 | 7e-32 | 41/46 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.68×** | +10.7 | 9e-25 | 40/46 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.53×** | +8.8 | 1e-16 | 36/46 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.94×** | +7.1 | 8e-11 | 42/47 (AsPC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +6.9 | 3e-10 | 38/46 (NCI-H2347, SW 900, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.25×** | +6.5 | 6e-09 | 27/46 (A-427, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.31×** | +5.3 | 6e-06 | 27/46 (HS-578T, C32, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.29×** | +5.0 | 3e-05 | 26/46 (HS-578T, C32, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.26×** | +4.9 | 6e-05 | 26/46 (HS-578T, A549, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.4 | 5e-04 | 18/46 (HS-578T, hTERT-HPNE, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.48×** | +4.3 | 8e-04 | 24/46 (MIA PaCa-2, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.45×** | +4.0 | 0.002 | 27/46 (MIA PaCa-2, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.20×** | +3.8 | 0.005 | 18/46 (HS-578T, A549, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.009 | 20/46 (HS-578T, A498, …) | all doses, flat |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | 1.18× | +3.4 | 0.020 | 15/46 (CFPAC-1, HCT15, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +3.4 | 0.021 | 19/46 (A498, SW 900, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | 1.18× | +3.4 | 0.021 | 15/46 (HS-578T, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6822.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H23 0.196×, SNU-1 0.151×, A-427 0.222×, PANC-1 0.329×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (C-33 A 0.118×, NCI-H23 0.143×, PANC-1 0.282×, A-427 0.210×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (LoVo 0.303×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (SNU-1 0.378×); [[Harringtonine (drug)]] 0.05 µM in 1 line (SNU-1 0.381×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.554×** | -11.7 | 4e-29 | 29/42 (C-33 A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.568×** | -11.7 | 4e-29 | 36/47 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.576×** | -10.5 | 1e-23 | 34/43 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **0.662×** | -8.5 | 2e-15 | 33/46 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.775×** | -7.4 | 1e-11 | 24/46 (LoVo, LOX-IMVI, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.721×** | -6.5 | 8e-09 | 28/45 (MIA PaCa-2, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.722×** | -3.5 | 0.034 | 23/47 (LoVo, RPMI-7951, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.845× | -3.3 | 0.058 | 20/45 (HT-29, NCI-H1573, …) | all doses, flat |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.893× | -3.3 | 0.061 | 4/47 (C-33 A, RPMI-7951, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.896× | -3.2 | 0.076 | 12/47 (SNU-1, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6822. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 539 | 0 | 12 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.378× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 177 | 1 (1 ⚠) | 9 (9 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.08× (z +9.7) ⚠ unreliable plate only | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.356× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 98.0 | 4 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.28× (z +13.5) | [[Harringtonine (drug)]] 5 µM 0.304× (z -13.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 89.0 | 6 (2 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.09× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 179 | 4 (1 ⚠) | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.23× (z +10.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.276× (z -16.3) ⚠ toxic |
| [[LoVo (line)]] | wt | 169 | 3 (1 ⚠) | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.04× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -23.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 48.7 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.57× (z +13.9) | — |
| [[PANC-1 (line)]] | alt | 262 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -19.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 107 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.86× (z +13.8) | — |
| [[HEC-1-A (line)]] | alt | 189 | 5 (1 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.44× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.484× (z -10.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 113 | 4 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.51× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -12.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 129 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.58× (z +13.1) | [[Docetaxel (drug)]] 0.05 µM 0.414× (z -9.2) ⚠ transcription drop; cell-cycle shift, explains ~42% of this change |
| [[AsPC-1 (line)]] | alt | 73.5 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.25× (z +12.2) | — |
| [[KATO III (line)]] | alt | 290 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -16.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 350 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -18.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 290 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -14.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 222 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.371× (z -13.9) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 90.8 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.78× (z +14.5) | — |
| [[HT-29 (line)]] | alt | 259 | 0 | 4 (4 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.329× (z -14.7) ⚠ transcription drop; cell-cycle shift, explains ~42% of this change |
| [[hTERT-HPNE (line)]] | wt | 47.0 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +11.8) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 6.11× (z +10.8) | — |
| [[J82 (line)]] | alt | 46.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.84× (z +13.4) | — |
| [[LOX-IMVI (line)]] | wt | 214 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -16.3) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 127 | 3 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.52× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -13.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 236 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -12.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 135 | 2 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.32× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -10.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 52.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.35× (z +12.7) | — |
| [[SW480 (line)]] | alt | 269 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -18.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 387 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -19.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 310 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -26.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 141 | 1 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.27× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H661 (line)]] | alt | 293 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -9.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 258 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.377× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 473 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -26.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 223 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.245× (z -10.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 74.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.68× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 195 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -16.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 40.0 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 189 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 178 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 93.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 175 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 40.4 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 205 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 170 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6822), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VWA8]] | +0.65 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[CDIN1]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[MDN1]] | +0.62 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[UBE3D]] | +0.61 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[CMTM8]] | +0.60 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[CLASP2]] | +0.60 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[FAM135A]] | +0.60 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[LRRC8D]] | +0.59 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[PALS2]] | +0.59 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[STX18-AS1]] | +0.58 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[ADAT2]] | +0.58 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[TMEM147]] | +0.57 | +0.51 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHMP4B]] | -0.49 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[FBXO48]] | -0.48 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[AXL]] | -0.47 | -0.44 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFIA]] | B | NFIA activity raises CAMKMT's level | lines that do not express NFIA (11) vs lines expressing it (39) | 2.49× lower at baseline in the lines without NFIA | 0.003 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |
| [[CHD7]] | C | CHD7 activity raises CAMKMT's level | lines that do not express CHD7 (3) vs lines expressing it (47) | 2.90× lower at baseline in the lines without CHD7 | 0.058 | ⚠ few lines (3 vs 47); across organs; also absent: GDPD1, ENSG00000287975, PIM2 |
| [[LRRC8D]] | C | LRRC8D activity raises CAMKMT's level | lines that do not express LRRC8D (3) vs lines expressing it (47) | 2.83× lower at baseline in the lines without LRRC8D | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PPFIBP2, USP31, EID2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.640). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-8.5, -35.1); signed map (-13.3, -51.6). **Vector** length 117, 38.9% of its response variance represented; |z| ≥ 3 in 1,343 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.2 | +8.8 |
|  | [[EX229 (drug)]] 5 µM |  | +4.9 | +4.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.5 | +4.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.3 | +2.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.1 | +6.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.9 | +2.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.6 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -12.3 | -7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.5 | -10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.0 | -11.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | -5.7 | +2.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | -5.6 | -8.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.3 | -2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | +3.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | +1.2 |

## What is on record

|  |  |
|---|---|
| Name | calmodulin-lysine N-methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:44,361,947-44,772,592 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CLNMT; previously C2orf34 |
| Gene groups (HGNC) | 7BS protein lysine methyltransferases; Non-histone lysine methyltransferases |
| Reactome | 5 pathways, smallest: Protein methylation; Inactivation, recovery and regulation of the phototransduction cascade; The phototransduction cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z624](https://www.uniprot.org/uniprotkb/Q7Z624) (Calmodulin-lysine N-methyltransferase):

> Catalyzes the trimethylation of 'Lys-116' in calmodulin.

**Summary**, from NCBI Gene [79823](https://www.ncbi.nlm.nih.gov/gene/79823):

> This gene encodes a class I protein methyltransferase that acts in the formation of trimethyllysine in calmodulin. The protein contains a AdoMet-binding motif and may play a role in calcium-dependent signaling. [provided by RefSeq, Sep 2012]

**Accessions** — [HGNC:26276](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26276) · Entrez [79823](https://www.ncbi.nlm.nih.gov/gene/79823) · UniProt [Q7Z624](https://www.uniprot.org/uniprotkb/Q7Z624) · Ensembl [ENSG00000143919](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143919)

## Data

Gene col 6822: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6822); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6822, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6822]; `tensor/DDL_lfc|DDL_z.npy` [6822]; `embed/gene_vectors.npy` [6822]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6822 or target_col == 6822). Every well: [[CAMKMT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAMKMT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
