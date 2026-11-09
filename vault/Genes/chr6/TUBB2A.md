---
symbol: "TUBB2A"
type: "gene"
col: 5993
ensembl_id: "ENSG00000137267"
name: "tubulin beta 2A class IIa"
location: "6p25.2"
module: 123
arm: "+"
pooled_cpm: 17.87
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# TUBB2A

*tubulin beta 2A class IIa* — 6p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.11× (z +19.9, q 0e+00, up in 45 of 47 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 6.17× (z +15.1, q 0e+00, up in 45 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (A-172 0.202×, AsPC-1 0.152×, NCI-H2347 0.231×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Afatinib (drug)]] 5 µM in 1 line (BT-474 0.127×); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (NCI-H23 0.0757×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF223]] (+0.70, fdr 7e-06), [[DYNLL1]] (+0.65, fdr 7e-06), [[MARCKS]] (+0.65, fdr 7e-06); moves opposite to [[RBBP4]] (-0.62, fdr 1e-05), [[ELAVL1]] (-0.61, fdr 1e-05), [[MTRR]] (-0.58, fdr 1e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ARL14]] → it (grade B ⚠); 4 go from it, the strongest it → [[SGSH]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5993.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **5.11×** | +19.9 | 0e+00 | 45/47 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **6.17×** | +15.1 | 0e+00 | 45/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.09×** | +14.0 | 2e-42 | 44/45 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.21×** | +10.0 | 2e-21 | 44/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **3.01×** | +9.5 | 3e-19 | 41/48 (SW480, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.88×** | +9.1 | 9e-18 | 44/48 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.86×** | +9.0 | 1e-17 | 40/45 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.67×** | +8.1 | 3e-14 | 34/42 (KATO III, J82, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **2.34×** | +7.3 | 2e-11 | 37/48 (NCI-H460, SW480, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.27×** | +7.1 | 9e-11 | 42/47 (LS 180, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.21×** | +6.8 | 5e-10 | 39/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **2.15×** | +6.6 | 2e-09 | 39/48 (PANC-1, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +6.4 | 8e-09 | 37/48 (LS 180, SW1417, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.05×** | +6.2 | 3e-08 | 35/48 (SW480, KATO III, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **1.88×** | +5.2 | 7e-06 | 28/41 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.80×** | +5.1 | 1e-05 | 27/48 (SW480, HT-29, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.05 µM |  | **1.88×** | +5.0 | 2e-05 | 31/46 (A-172, NCI-H460, …) | all doses, flat | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.77×** | +4.9 | 3e-05 | 27/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 5 µM |  | **1.64×** | +4.1 | 0.001 | 29/48 (PANC-1, SNU-423, …) | all doses, flat | position effect removed |
| [[Docetaxel (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.013 | 18/48 (NCI-H2030, SNU-423, …) | all doses, flat | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.47×** | +3.2 | 0.032 | 19/46 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +3.1 | 0.041 | 15/47 (LS 180, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5993.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (A-172 0.202×, AsPC-1 0.152×, NCI-H2347 0.231×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Afatinib (drug)]] 5 µM in 1 line (BT-474 0.127×); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (NCI-H23 0.0757×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 0.664× | -3.5 | 0.16 | 20/48 (hTERT-HPNE, AN3 CA, …) | all doses, flat | position effect removed |
| [[Citalopram (hydrobromide) (drug)]] 0.5 µM |  | 0.676× | -3.4 | 0.16 | 18/46 (AN3 CA, KATO III, …) | all doses, flat | position effect removed |
| [[Citalopram (hydrobromide) (drug)]] 5 µM |  | 0.680× | -3.3 | 0.16 | 14/48 (SW 1088, SK-MEL-2, …) | all doses, flat | position effect removed |
| [[Levobupivacaine (hydrochloride) (drug)]] 0.05 µM |  | 0.672× | -3.2 | 0.22 | 18/47 (NCI-H1573, CFPAC-1, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5993. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.00 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.14× (z +13.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 16.3× (z +13.1) | — |
| [[NCI-H2347 (line)]] | alt | 24.8 | 6 (3 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 9.06× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 6.92 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 41.1× (z +17.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 57.1× (z +13.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 42.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 14.8× (z +13.6) | — |
| [[SW48 (line)]] | wt | 25.4 | 5 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 15.6× (z +11.2) | — |
| [[SW480 (line)]] | alt | 12.4 | 5 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.49× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 5.60× (z +9.4) | — |
| [[A549 (line)]] | wt | 12.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.33× (z +12.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 9.30× (z +9.7) | — |
| [[AsPC-1 (line)]] | alt | 16.8 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 21.3× (z +21.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 13.0× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.152× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 19.4 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 8.13× (z +13.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 15.2× (z +11.6) | [[Afatinib (drug)]] 5 µM 0.127× (z -10.9) |
| [[PANC-1 (line)]] | alt | 5.55 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +16.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 31.2× (z +14.5) | — |
| [[C32 (line)]] | wt | 7.61 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.3× (z +13.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 30.4× (z +10.8) | — |
| [[HOP62 (line)]] | alt | 30.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.33× (z +17.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 12.0× (z +13.5) | — |
| [[HS-578T (line)]] | alt | 52.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +12.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.81× (z +10.4) | — |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +12.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 10.6× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 15.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +16.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 11.5× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 35.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +17.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 9.70× (z +11.4) | — |
| [[SW 900 (line)]] | alt | 8.16 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +14.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 15.5× (z +10.3) | — |
| [[A498 (line)]] | wt | 11.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +11.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.17× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 10.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +9.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 7.20× (z +9.1) | — |
| [[J82 (line)]] | alt | 30.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +12.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.02× (z +9.0) | — |
| [[KATO III (line)]] | alt | 14.2 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.66× (z +8.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LoVo (line)]] | wt | 20.2 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 9.00× (z +10.7) | — |
| [[NCI-H1792 (line)]] | alt | 9.32 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.6× (z +10.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 11.3× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 10.4 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 12.2× (z +10.9) | — |
| [[RPMI-7951 (line)]] | alt | 23.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +10.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.01× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 26.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +12.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A-172 (line)]] | wt | 86.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 24.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +16.4) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[COLO 205 (line)]] | alt | 6.72 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.41× (z +9.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HepG2_C3A (line)]] | wt | 21.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.29× (z +11.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[Hs 766T (line)]] | wt | 9.10 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.11× (z +10.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HT-29 (line)]] | alt | 14.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +10.2) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[LOX-IMVI (line)]] | wt | 7.95 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +10.1) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H23 (line)]] | alt | 5.20 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0757× (z -8.6) |
| [[SNU-1 (line)]] | wt | 10.2 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 19.9× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 11.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +12.2) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A-427 (line)]] | wt | 9.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5993), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF223]] | +0.70 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[DYNLL1]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 | pathway: Affinity selection of immunoglobulins; STRING 626 |
| [[MARCKS]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[TUBB2B]] | +0.65 | +0.56 / +0.68 | both halves | 1e-05 | same gene group; pathway: Activation of AMPK downstream of NMDARs; STRING 933 |
| [[LRRC8E]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[TUBA1A]] | +0.63 | +0.45 / +0.65 | both halves | 3e-05 | pathway: Activation of AMPK downstream of NMDARs; STRING 999 |
| [[RHOB]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[DLGAP4]] | +0.62 | +0.51 / +0.61 | both halves | 1e-05 | pathway: Neuronal System |
| [[KLF2]] | +0.61 | +0.54 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CDKN2B]] | +0.60 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[MAP1S]] | +0.60 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[H3-3B]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBBP4]] | -0.62 | -0.54 / -0.62 | both halves | 1e-05 | pathway: G2/M Transition |
| [[ELAVL1]] | -0.61 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[MTRR]] | -0.58 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[TM9SF3]] | -0.57 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[METTL9]] | -0.57 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[ARIH2]] | -0.56 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[MRE11]] | -0.56 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[TMEM248]] | -0.55 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[PHB2]] | -0.54 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[POLR2B]] | -0.54 | -0.56 / -0.55 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins |
| [[HSPA14]] | -0.53 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[SENP3]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARL14]] | B | ARL14 activity lowers TUBB2A's level | lines that do not express ARL14 (23) vs lines expressing it (27) | 1.29× higher at baseline in the lines without ARL14 | 0.087 | ⚠ within organs, on part of the lines; also absent: TMEM92, LIPH, AFAP1L2; maybe low, not absent |
| [[ARMCX2]] | B | ARMCX2 activity raises TUBB2A's level | lines that do not express ARMCX2 (28) vs lines expressing it (22) | 1.48× lower at baseline in the lines without ARMCX2 | 0.095 | ⚠ within organs, on part of the lines; also absent: EDNRA, ARMCX1, GPR173 |
| [[ZMIZ1]] | C | ZMIZ1 activity strengthens TUBB2A's drug response | lines that do not express ZMIZ1 (4) vs lines expressing it (44) | the lines without ZMIZ1 respond 0.76× as strongly (z diff +1.30); strongest at Homoharringtonine 5 µM: 2.77x vs 6.00x (z diff +3.9) | 0.068 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WWC3, PYROXD2, NINJ1; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SGSH]] | B | TUBB1, TUBB2A, [[TUBB3]], TUBB4A, [[TUBB4B]] activity raises SGSH's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 lower it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets |
| [[MZT1]] | B | TUBB1, TUBB2A, [[TUBB3]], TUBB4A, [[TUBB4B]] activity lowers MZT1's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 raise it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[ENSG00000287352]] | B | TUBB1, TUBB2A, [[TUBB3]], TUBB4A, [[TUBB4B]] activity lowers ENSG00000287352's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 raise it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[RAB28]] | B | TUBB1, TUBB2A, [[TUBB3]], TUBB4A, [[TUBB4B]] activity raises RAB28's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 lower it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.598). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.3, -0.0); signed map (-0.0, 22.3). **Vector** length 99.4, 28.5% of its response variance represented; |z| ≥ 3 in 1,180 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +6.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +15.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.5 | +19.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.5 | +10.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +4.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.7 | +2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +0.7 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.5 | -1.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +0.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -0.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | -0.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | tubulin beta 2A class IIa |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.2 — chr6:3,153,497-3,157,544 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ40E16.7; previously TUBB, TUBB2 |
| Gene groups (HGNC) | Tubulin beta family |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 83 pathways, smallest: Microtubule-dependent trafficking of connexons from Golgi to the plasma membrane; Transport of connexons to the plasma membrane; Gap junction assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13885](https://www.uniprot.org/uniprotkb/Q13885) (Tubulin beta-2A chain):

> Tubulin is the major constituent of microtubules, a cylinder consisting of laterally associated linear protofilaments composed of alpha- and beta-tubulin heterodimers. Microtubules grow by the addition of GTP-tubulin dimers to the microtubule end, where a stabilizing cap forms. Below the cap, tubulin dimers are in GDP-bound state, owing to GTPase activity of alpha-tubulin.

**Summary**, from NCBI Gene [7280](https://www.ncbi.nlm.nih.gov/gene/7280):

> Microtubules, key participants in processes such as mitosis and intracellular transport, are composed of heterodimers of alpha- and beta-tubulins. The protein encoded by this gene is a beta-tubulin. Defects in this gene are associated with complex cortical dysplasia with other brain malformations-5. Two transcript variants encoding distinct isoforms have been found for this gene. [provided by RefSeq, Jul 2015]

**Accessions** — [HGNC:12412](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12412) · Entrez [7280](https://www.ncbi.nlm.nih.gov/gene/7280) · UniProt [Q13885](https://www.uniprot.org/uniprotkb/Q13885) · Ensembl [ENSG00000137267](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137267)

## Data

Gene col 5993: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5993); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5993, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5993]; `tensor/DDL_lfc|DDL_z.npy` [5993]; `embed/gene_vectors.npy` [5993]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5993 or target_col == 5993). Every well: [[TUBB2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUBB2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
