---
symbol: "MT-RNR2"
type: "gene"
col: 13058
ensembl_id: "ENSG00000210082"
name: "mitochondrially encoded 16S rRNA"
location: "mitochondria"
module: null
arm: null
pooled_cpm: 26432.88
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# MT-RNR2

*mitochondrially encoded 16S rRNA* — mitochondria

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.79× (z +12.0, q 2e-30, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.41× (z +3.9, q 0.013, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.223× (z -13.5, q 8e-39, down in 48 of 48 measured lines) ⚠ transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 15 lines (C-33 A 0.198×, Hs 766T 0.158×, PANC-1 0.183×, MIA PaCa-2 0.180×, …; ⚠ transcription drop).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13058.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.79×** | +12.0 | 2e-30 | 49/49 (LoVo, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.55×** | +11.0 | 1e-25 | 44/44 (LoVo, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.90×** | +8.1 | 1e-13 | 45/45 (C-33 A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.013 | 45/49 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.14×** | +3.6 | 0.038 | 47/49 (C32, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.5 | 0.039 | 35/48 (SNU-423, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.32×** | +3.3 | 0.080 | 43/48 (NCI-H2347, J82, …) | top dose only | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | 1.96× | +3.2 | 0.11 | 42/48 (C32, SW48, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13058.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 15 lines (C-33 A 0.198×, Hs 766T 0.158×, PANC-1 0.183×, MIA PaCa-2 0.180×, …; ⚠ transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.223×** | -13.5 | 8e-39 | 48/48 (C-33 A, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.613× | -3.2 | 0.46 | 49/49 (A549, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13058. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 24,919 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +12.3) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.273× (z -11.9) ⚠ transcription drop |
| [[A549 (line)]] | wt | 30,006 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +13.7) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.240× (z -13.1) ⚠ transcription drop |
| [[AN3 CA (line)]] | alt | 23,844 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +13.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.204× (z -14.5) ⚠ transcription drop |
| [[C-33 A (line)]] | alt | 19,230 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +16.2) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.198× (z -16.0) ⚠ transcription drop |
| [[C32 (line)]] | wt | 19,656 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +13.2) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.281× (z -11.8) ⚠ transcription drop |
| [[HEC-1-A (line)]] | alt | 24,519 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +12.4) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.273× (z -11.1) ⚠ transcription drop |
| [[HOP62 (line)]] | alt | 23,678 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.35× (z +12.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.280× (z -10.8) ⚠ transcription drop |
| [[KATO III (line)]] | alt | 30,584 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +12.9) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.212× (z -14.7) ⚠ transcription drop |
| [[LoVo (line)]] | wt | 18,241 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +17.1) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.278× (z -13.0) ⚠ transcription drop |
| [[LOX-IMVI (line)]] | wt | 24,138 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +12.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.220× (z -12.9) ⚠ transcription drop |
| [[LS 180 (line)]] | wt | 30,049 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +13.0) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.204× (z -14.1) ⚠ transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 24,929 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.70× (z +13.3) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.180× (z -15.4) ⚠ transcription drop |
| [[NCI-H460 (line)]] | wt | 24,977 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +13.6) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.223× (z -13.6) ⚠ transcription drop |
| [[SK-MEL-2 (line)]] | alt | 17,439 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +12.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.242× (z -13.5) ⚠ transcription drop |
| [[SNU-423 (line)]] | alt | 15,549 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +12.6) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.397× (z -8.8) ⚠ transcription drop |
| [[SW48 (line)]] | wt | 21,737 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +12.0) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.263× (z -11.4) ⚠ transcription drop |
| [[SW480 (line)]] | alt | 22,513 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +15.0) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.204× (z -15.2) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 23,978 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +11.2) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.261× (z -12.1) ⚠ transcription drop |
| [[A-427 (line)]] | wt | 23,319 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +10.1) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.189× (z -14.4) ⚠ transcription drop |
| [[AsPC-1 (line)]] | alt | 31,180 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +9.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.194× (z -12.7) ⚠ transcription drop |
| [[H4 (line)]] | wt | 23,486 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +13.4) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.224× (z -13.9) ⚠ transcription drop |
| [[HCT15 (line)]] | alt | 15,150 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +15.3) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.337× (z -10.0) ⚠ transcription drop |
| [[HepG2_C3A (line)]] | wt | 34,069 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +9.2) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.231× (z -13.0) ⚠ transcription drop |
| [[HS-578T (line)]] | alt | 26,081 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +12.0) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.279× (z -10.6) ⚠ transcription drop |
| [[HT-29 (line)]] | alt | 28,494 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +11.9) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.236× (z -12.8) ⚠ transcription drop |
| [[hTERT-HPNE (line)]] | wt | 29,960 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +10.3) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.234× (z -12.3) ⚠ transcription drop |
| [[J82 (line)]] | alt | 24,061 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.64× (z +10.9) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.223× (z -13.2) ⚠ transcription drop |
| [[NCI-H1792 (line)]] | alt | 30,564 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +12.1) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.223× (z -12.8) ⚠ transcription drop |
| [[NCI-H2030 (line)]] | alt | 32,671 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +10.0) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.224× (z -12.4) ⚠ transcription drop |
| [[NCI-H23 (line)]] | alt | 20,875 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +11.9) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.256× (z -13.3) ⚠ transcription drop |
| [[Panc 03.27 (line)]] | alt | 24,400 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +11.6) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.214× (z -13.3) ⚠ transcription drop |
| [[PANC-1 (line)]] | alt | 30,023 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +12.2) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.183× (z -15.5) ⚠ transcription drop |
| [[RPMI-7951 (line)]] | alt | 18,392 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +11.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.360× (z -9.5) ⚠ transcription drop |
| [[SHP-77 (line)]] | alt | 31,388 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +10.3) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.188× (z -14.5) ⚠ transcription drop |
| [[SW 900 (line)]] | alt | 31,976 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +11.8) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.210× (z -13.7) ⚠ transcription drop |
| [[SW1417 (line)]] | alt | 31,697 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +9.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.193× (z -14.6) ⚠ transcription drop |
| [[CFPAC-1 (line)]] | alt | 23,017 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +8.6) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.240× (z -11.8) ⚠ transcription drop |
| [[CHP-212 (line)]] | wt | 29,230 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +9.8) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.199× (z -12.7) ⚠ transcription drop |
| [[COLO 205 (line)]] | alt | 34,917 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +10.1) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.160× (z -15.1) ⚠ transcription drop |
| [[Hs 766T (line)]] | wt | 40,014 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +9.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.158× (z -15.7) ⚠ transcription drop |
| [[NCI-H1573 (line)]] | alt | 36,685 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +10.3) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.180× (z -13.5) ⚠ transcription drop |
| [[RKO (line)]] | wt | 19,343 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.73× (z +14.0) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.299× (z -10.9) ⚠ transcription drop |
| [[SNU-1 (line)]] | wt | 30,455 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +10.8) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.191× (z -14.1) ⚠ transcription drop |
| [[SW 1088 (line)]] | alt | 23,863 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +10.8) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.270× (z -9.9) ⚠ transcription drop |
| [[SW 1271 (line)]] | alt | 20,989 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +9.3) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.249× (z -11.6) ⚠ transcription drop |
| [[BT-474 (line)]] | alt | 33,714 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.186× (z -14.2) ⚠ transcription drop |
| [[NCI-H2347 (line)]] | alt | 31,256 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.176× (z -15.2) ⚠ transcription drop |
| [[NCI-H661 (line)]] | alt | 27,356 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.212× (z -13.0) ⚠ transcription drop |
| [[NCI-H2122 (line)]] | alt | 30,736 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29,872 | 0 | 0 | — | — |

## Genes that move with it

Not in the vector space, so no gene relations.

## Genes that move opposite

Not in the vector space, so no gene relations.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

Not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). Its drug and cell-line tables above are complete all the same.

## What is on record

|  |  |
|---|---|
| Name | mitochondrially encoded 16S rRNA |
| Locus type | RNA, ribosomal (non-coding RNA) |
| Location | mitochondria — chrMT:1,671-3,229 (+) |
| Ensembl biotype | Mt_rRNA |
| Also known as | HN, 16S; previously MTRNR2 |
| Gene groups (HGNC) | Receptor ligands; Mitochondrially encoded ribosomal RNAs |
| Reactome | 22 pathways, smallest: Formyl peptide receptors bind formyl peptides and many other ligands; rRNA modification in the mitochondrion; FASTK family proteins regulate processing and stability of mitochondrial RNAs |
| Matched by | ensembl_id |

**Function**, from UniProt [A0A3G1DIU6](https://www.uniprot.org/uniprotkb/A0A3G1DIU6) (Small humanin-like peptide 2):

> Binds to and activates chemokine receptor ACKR3/CXCR7 which results in activation of proopiomelanocortin neurons in the arcuate nucleus of the hypothalamus, leading to suppression of food intake and increased energy expenditure. Displays chaperone-like activity, inhibiting misfolding of IAPP and preventing IAPP amyloid formation. Significantly reduces apoptosis and the generation of reactive oxygen species and improves mitochondrial metabolism in vitro.

**Summary**, from NCBI Gene [4550](https://www.ncbi.nlm.nih.gov/gene/4550):

> Enables several functions, including identical protein binding activity; receptor antagonist activity; and receptor ligand activity. Involved in several processes, including cellular response to amyloid-beta; negative regulation of cellular component organization; and negative regulation of cytokine production. Acts upstream of with a positive effect on cell surface receptor signaling pathway via STAT. Located in several cellular components, including mitochondrion; perinuclear region of …

**Accessions** — [HGNC:7471](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7471) · Entrez [4550](https://www.ncbi.nlm.nih.gov/gene/4550) · UniProt [A0A3G1DIU6](https://www.uniprot.org/uniprotkb/A0A3G1DIU6) · Ensembl [ENSG00000210082](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000210082)

## Data

Gene col 13058: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13058); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13058, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13058]; `tensor/DDL_lfc|DDL_z.npy` [13058]; `embed/gene_vectors.npy` [13058]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13058 or target_col == 13058). Every well: [[MT-RNR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MT-RNR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
