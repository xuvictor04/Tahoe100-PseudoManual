---
symbol: "CITED2"
type: "gene"
col: 8948
ensembl_id: "ENSG00000164442"
name: "Cbp/p300 interacting transactivator with ED-rich tail 2"
location: "6q24.1"
module: 123
arm: "+"
pooled_cpm: 64.31
n_lines_expressing: 47
n_dd_up: 9
n_dd_down: 23
n_dd_up_clean: 7
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 5
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# CITED2

*Cbp/p300 interacting transactivator with ED-rich tail 2* — 6q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.10× (z +11.6, q 2e-28, up in 32 of 44 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 2.21× (z +8.8, q 5e-16, up in 33 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.492× (z -7.9, q 2e-12, down in 37 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 0.534× (z -6.6, q 1e-08, down in 31 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGK1]] (+0.61, fdr 1e-05), [[SIRT1]] (+0.61, fdr 1e-05), [[OTUD1]] (+0.59, fdr 1e-05); moves opposite to [[IQCB1]] (-0.51, fdr 3e-05), [[COP1]] (-0.50, fdr 2e-05), [[LINC03006-1]] (-0.49, fdr 4e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 5 go from it, the strongest it → [[ZBTB10]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8948.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.10×** | +11.6 | 2e-28 | 32/44 (C32, LS 180, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.21×** | +8.8 | 5e-16 | 33/45 (A-427, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.15×** | +8.5 | 4e-15 | 33/44 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +7.3 | 6e-11 | 37/45 (HS-578T, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +6.2 | 5e-08 | 26/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.66×** | +5.6 | 2e-06 | 32/45 (A-427, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.69×** | +5.6 | 2e-06 | 28/45 (A-427, LS 180, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +4.3 | 0.002 | 26/46 (RPMI-7951, HS-578T, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.39×** | +3.4 | 0.049 | 20/44 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.32× | +3.1 | 0.12 | 15/46 (A-172, SNU-423, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.28× | +3.1 | 0.12 | 15/46 (HEC-1-A, HOP62, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8948.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.492×** | -7.9 | 2e-12 | 37/45 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.515×** | -7.3 | 6e-11 | 34/45 (BT-474, RPMI-7951, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.534×** | -6.6 | 1e-08 | 31/45 (NCI-H2030, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.575×** | -6.1 | 1e-07 | 40/45 (SW 1088, C-33 A, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.593×** | -5.8 | 9e-07 | 30/45 (A498, NCI-H2030, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.592×** | -5.6 | 2e-06 | 25/43 (C-33 A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.429×** | -4.9 | 8e-05 | 29/45 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.443×** | -4.7 | 2e-04 | 31/45 (SNU-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.654×** | -4.5 | 4e-04 | 27/44 (NCI-H23, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.459×** | -4.5 | 4e-04 | 25/45 (NCI-H2030, MIA PaCa-2, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.464×** | -4.4 | 5e-04 | 34/45 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.705×** | -3.9 | 0.005 | 24/46 (SNU-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.701×** | -3.6 | 0.012 | 23/43 (C-33 A, C32, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.809×** | -3.3 | 0.037 | 22/45 (NCI-H1573, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.734×** | -3.3 | 0.037 | 21/45 (NCI-H23, SNU-1, …) | top dose only | position effect removed |
| [[Trimetrexate (drug)]] 5 µM |  | **0.811×** | -3.3 | 0.037 | 20/46 (HCT15, RPMI-7951, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.582×** | -3.1 | 0.053 | 19/45 (AsPC-1, SNU-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Pimozide (drug)]] 5 µM |  | **0.754×** | -3.1 | 0.053 | 12/45 (HCT15, SNU-1, …) | top dose only | position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.754×** | -3.1 | 0.053 | 19/44 (HT-29, C32, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.755×** | -3.1 | 0.054 | 15/45 (NCI-H1573, AN3 CA, …) | inconsistent across doses | position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.691×** | -2.9 | 0.089 | 15/45 (A498, SNU-1, …) | rises with dose | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8948. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 543 | 3 (1 ⚠) | 7 (6 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.53× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0722× (z -21.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -13.6) |
| [[A-427 (line)]] | wt | 89.3 | 5 (2 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 6.30× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.150× (z -14.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 43.1 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.27× (z +17.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.76× (z +13.1) | — |
| [[NCI-H2030 (line)]] | alt | 197 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.269× (z -9.2) |
| [[C32 (line)]] | wt | 31.7 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +21.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 9.66× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 30.8 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.62× (z +17.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.71× (z +13.0) | — |
| [[SNU-423 (line)]] | alt | 175 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.252× (z -8.7) |
| [[LoVo (line)]] | wt | 20.4 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.44× (z +13.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 98.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 7.60× (z +13.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.180× (z -11.4) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 143 | 2 | 2 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.57× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -9.0) |
| [[SW480 (line)]] | alt | 16.9 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.78× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.216× (z -9.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 53.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +9.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.64× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 38.7 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +8.9) ⚠ cell-cycle shift, explains ~35% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.245× (z -9.6) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.256× (z -9.3) |
| [[C-33 A (line)]] | alt | 136 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0873× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HOP62 (line)]] | alt | 36.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +12.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +10.3) | — |
| [[hTERT-HPNE (line)]] | wt | 60.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.39× (z +15.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.95× (z +13.3) | — |
| [[J82 (line)]] | alt | 47.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +13.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.52× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 68.4 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0605× (z -16.8) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 43.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +10.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.64× (z +8.8) | [[Ixazomib citrate (drug)]] 5 µM 0.182× (z -9.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW1417 (line)]] | alt | 35.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +14.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.04× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 29.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -11.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 41.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +15.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 3.37× (z +11.0) | — |
| [[NCI-H1573 (line)]] | alt | 63.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -10.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 65.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.253× (z -9.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 38.7 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0791× (z -9.2) ⚠ cell-cycle shift, explains ~18% of this change |
| [[AsPC-1 (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -8.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 42.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -10.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 37.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.142× (z -8.7) ⚠ toxic |
| [[HCT15 (line)]] | alt | 36.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 24.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +10.4) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1792 (line)]] | alt | 62.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +14.7) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2347 (line)]] | alt | 46.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.280× (z -8.9) ⚠ unreliable plate only |
| [[NCI-H661 (line)]] | alt | 213 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -9.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 69.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -10.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 47.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +11.6) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[A549 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 65.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.08 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 77.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 51.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8948), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGK1]] | +0.61 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[SIRT1]] | +0.61 | +0.57 / +0.61 | both halves | 1e-05 | pathway: FOXO-mediated transcription |
| [[OTUD1]] | +0.59 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[BCL6]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 | pathway: FOXO-mediated transcription |
| [[AHR]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[MEX3B]] | +0.56 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[ARID5B]] | +0.55 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[BHLHE41]] | +0.55 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[C21orf91]] | +0.55 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[PNRC1]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[KLF4]] | +0.54 | +0.54 / +0.54 | both halves | 1e-05 | pathway: FOXO-mediated transcription |
| [[TCIM]] | +0.54 | +0.50 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQCB1]] | -0.51 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[COP1]] | -0.50 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[LINC03006-1]] | -0.49 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[TIMM23B]] | -0.48 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[UBE2K]] | -0.48 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[NAP1L4]] | -0.47 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[HERC2P9]] | -0.46 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[HERC2P2]] | -0.45 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[VKORC1L1]] | -0.45 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[HERC2P3]] | -0.45 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[PPIH]] | -0.45 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[TRAPPC10]] | -0.45 | -0.55 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZBTB10]] | C | CITED2 activity raises ZBTB10's level | lines that do not express CITED2 (3) vs lines expressing it (47) | 5.25× lower at baseline in the lines without CITED2 | 0.015 | ⚠ few lines (3 vs 47); across organs; also absent: RDX, FNBP1, BMS1P23; maybe low, not absent |
| cells under [[Lonafarnib (drug)]] 5 µM | C | CITED2 activity raises the cells' numbers under Lonafarnib 5 µM (protects the cells) | lines that do not express CITED2 (3) vs lines expressing it (45) | the lines without CITED2: 0.09× the cells of the other lines | 0.021 | ⚠ few lines (3 vs 47); across organs; also absent: RDX, FNBP1, BMS1P23; maybe low, not absent |
| [[NR3C1]] | C | CITED2 activity raises NR3C1's level | lines that do not express CITED2 (3) vs lines expressing it (47) | 10.28× lower at baseline in the lines without CITED2 | 0.030 | ⚠ few lines (3 vs 47); across organs; also absent: RDX, FNBP1, BMS1P23; maybe low, not absent |
| cells under [[Dinaciclib (drug)]] 0.05 µM | C | CITED2 activity raises the cells' numbers under Dinaciclib 0.05 µM (protects the cells) | lines that do not express CITED2 (3) vs lines expressing it (45) | the lines without CITED2: 0.28× the cells of the other lines | 0.043 | ⚠ few lines (3 vs 47); across organs; also absent: RDX, FNBP1, BMS1P23; maybe low, not absent |
| cells under [[Dinaciclib (drug)]] 5 µM | C | CITED2 activity raises the cells' numbers under Dinaciclib 5 µM (protects the cells) | lines that do not express CITED2 (3) vs lines expressing it (45) | the lines without CITED2: 0.22× the cells of the other lines | 0.061 | ⚠ few lines (3 vs 47); across organs; also absent: RDX, FNBP1, BMS1P23; maybe low, not absent |

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.572). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.3, -31.2); signed map (-0.7, 16.0). **Vector** length 137, 40.7% of its response variance represented; |z| ≥ 3 in 1,261 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +7.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.7 | +8.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.6 | +8.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +7.6 | +11.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.3 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.3 | +1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.3 | +3.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -7.1 | -7.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.3 | -6.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.9 | -7.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.7 | -5.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.6 | -4.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.5 | -4.9 |
|  | [[EX229 (drug)]] 5 µM |  | -4.3 | -4.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.1 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | Cbp/p300 interacting transactivator with ED-rich tail 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.1 — chr6:139,371,807-139,374,648 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MRG1 |
| Gene groups (HGNC) | CBP/p300-interacting transactivator with ED-rich tail family |
| Hallmark sets | UV_RESPONSE_DN, GLYCOLYSIS, HYPOXIA |
| Reactome | 9 pathways, smallest: TFAP2 (AP-2) family regulates transcription of other transcription factors; Activation of the TFAP2 (AP-2) family of transcription factors; Regulation of gene expression by Hypoxia-inducible Factor |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99967](https://www.uniprot.org/uniprotkb/Q99967) (Cbp/p300-interacting transactivator 2):

> Transcriptional coactivator of the p300/CBP-mediated transcription complex. Acts as a bridge, linking TFAP2 transcription factors and the p300/CBP transcriptional coactivator complex in order to stimulate TFAP2-mediated transcriptional activation. Positively regulates TGF-beta signaling through its association with the SMAD/p300/CBP-mediated transcriptional coactivator complex. Stimulates the peroxisome proliferator-activated receptors PPARA transcriptional activity. Enhances estrogen-dependent …

**Summary**, from NCBI Gene [10370](https://www.ncbi.nlm.nih.gov/gene/10370):

> The protein encoded by this gene inhibits transactivation of HIF1A-induced genes by competing with binding of hypoxia-inducible factor 1-alpha to p300-CH1. Mutations in this gene are a cause of cardiac septal defects. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, May 2012]

**Accessions** — [HGNC:1987](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1987) · Entrez [10370](https://www.ncbi.nlm.nih.gov/gene/10370) · UniProt [Q99967](https://www.uniprot.org/uniprotkb/Q99967) · Ensembl [ENSG00000164442](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164442)

## Data

Gene col 8948: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8948); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8948, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8948]; `tensor/DDL_lfc|DDL_z.npy` [8948]; `embed/gene_vectors.npy` [8948]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8948 or target_col == 8948). Every well: [[CITED2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CITED2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
