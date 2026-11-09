---
symbol: "FAM210A"
type: "gene"
col: 10796
ensembl_id: "ENSG00000177150"
name: "mitochondrial inner membrane structural 1"
location: "18p11.21"
module: 105
arm: "+"
pooled_cpm: 103.29
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 17
n_dd_up_clean: 21
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# FAM210A

*mitochondrial inner membrane structural 1* — 18p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.92× (z +12.7, q 5e-34, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.570× (z -10.0, q 1e-20, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HK2]] (+0.77, fdr 7e-06), [[INSIG2]] (+0.77, fdr 7e-06), [[RNMT]] (+0.73, fdr 7e-06, ⚠ same locus), [[POM121]] (+0.72, fdr 7e-06); moves opposite to [[SMARCB1]] (-0.57, fdr 2e-05), [[CPLANE1]] (-0.57, fdr 1e-05), [[ZNF644]] (-0.56, fdr 3e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10796.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.92×** | +12.7 | 5e-34 | 48/49 (NCI-H23, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.72×** | +12.5 | 2e-33 | 46/48 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.37×** | +10.8 | 8e-25 | 43/48 (SW480, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +10.1 | 9e-22 | 42/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.05×** | +9.0 | 3e-17 | 44/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.05×** | +9.0 | 3e-17 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.06×** | +7.3 | 2e-11 | 39/48 (HEC-1-A, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.77×** | +6.7 | 2e-09 | 31/37 (NCI-H2347, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **2.50×** | +6.0 | 1e-07 | 44/48 (BT-474, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.60×** | +5.9 | 2e-07 | 39/48 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.56×** | +5.6 | 1e-06 | 37/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.01×** | +4.6 | 2e-04 | 35/48 (HT-29, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.28×** | +4.4 | 4e-04 | 29/49 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +4.1 | 0.002 | 28/48 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.0 | 0.002 | 25/48 (LoVo, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Terfenadine (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.018 | 26/48 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.024 | 23/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.024 | 29/48 (HT-29, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10796.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.570×** | -10.0 | 1e-20 | 32/48 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.524×** | -7.8 | 2e-12 | 33/44 (C-33 A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.583×** | -6.5 | 1e-08 | 35/48 (RKO, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.629×** | -5.6 | 3e-06 | 37/47 (C-33 A, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.721×** | -4.1 | 0.004 | 27/49 (NCI-H23, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.724×** | -3.9 | 0.007 | 25/47 (C32, C-33 A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.733×** | -3.9 | 0.007 | 28/48 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.734×** | -3.9 | 0.007 | 33/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.815×** | -3.7 | 0.016 | 23/48 (HepG2/C3A, A-172, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.749×** | -3.6 | 0.016 | 29/49 (LOX-IMVI, HOP62, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.762×** | -3.4 | 0.031 | 32/48 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.767×** | -3.3 | 0.039 | 27/48 (LOX-IMVI, NCI-H1573, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.772×** | -3.3 | 0.048 | 29/49 (A-172, H4, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.830×** | -3.2 | 0.053 | 22/49 (C32, NCI-H2347, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.838× | -3.2 | 0.058 | 19/48 (RKO, hTERT-HPNE, …) | top dose only | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.807×** | -3.1 | 0.060 | 22/48 (C32, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.782×** | -3.1 | 0.063 | 23/48 (A-172, LS 180, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.787×** | -3.0 | 0.078 | 22/47 (C32, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10796. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 73.2 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.30× (z +20.3) | — |
| [[NCI-H460 (line)]] | wt | 88.1 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +19.2) | — |
| [[LoVo (line)]] | wt | 73.7 | 9 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.42× (z +19.2) | — |
| [[SW480 (line)]] | alt | 76.7 | 8 (2 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 5.15× (z +18.2) | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -11.2) |
| [[PANC-1 (line)]] | alt | 77.8 | 6 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.50× (z +16.3) | [[Harringtonine (drug)]] 5 µM 0.319× (z -10.5) |
| [[LS 180 (line)]] | wt | 89.6 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.02× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -9.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 114 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.12× (z +12.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.255× (z -10.0) ⚠ toxic |
| [[C32 (line)]] | wt | 242 | 1 | 5 (5 ⚠) | [[PH-797804 (drug)]] 5 µM 4.57× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -15.3) ⚠ cell-cycle shift, explains ~12% of this change |
| [[HEC-1-A (line)]] | alt | 103 | 3 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.60× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -13.3) |
| [[KATO III (line)]] | alt | 71.9 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.24× (z +11.1) | — |
| [[NCI-H1573 (line)]] | alt | 137 | 3 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.37× (z +11.0) | [[Harringtonine (drug)]] 5 µM 0.167× (z -12.9) |
| [[NCI-H2347 (line)]] | alt | 115 | 3 (1 ⚠) | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 15.1× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.166× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.452× (z -11.4) |
| [[A-172 (line)]] | wt | 178 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -8.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 75.3 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.49× (z +12.3) | — |
| [[A-427 (line)]] | wt | 109 | 2 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.23× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.208× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.554× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 88.0 | 2 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.21× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -10.1) |
| [[C-33 A (line)]] | alt | 186 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.07× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.0470× (z -25.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 264 | 3 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.66× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -17.3) |
| [[NCI-H1792 (line)]] | alt | 83.2 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.64× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.64× (z +12.2) | — |
| [[NCI-H23 (line)]] | alt | 105 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 14.0× (z +14.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0634× (z -29.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.429× (z -12.6) |
| [[RKO (line)]] | wt | 118 | 2 | 2 | [[TAK-901 (drug)]] 5 µM 7.57× (z +9.0) | [[Harringtonine (drug)]] 5 µM 0.171× (z -14.5) |
| [[RPMI-7951 (line)]] | alt | 154 | 2 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.75× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -9.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 88.1 | 1 | 2 | [[Auranofin (drug)]] 5 µM 2.99× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -12.4) |
| [[COLO 205 (line)]] | alt | 54.7 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 13.3× (z +16.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 140 | 1 | 2 | [[Auranofin (drug)]] 5 µM 4.78× (z +13.5) | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -12.8) |
| [[NCI-H2030 (line)]] | alt | 50.3 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.65× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.0880× (z -22.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.486× (z -9.7) |
| [[HS-578T (line)]] | alt | 115 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 10.1× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 175 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -14.7) |
| [[SHP-77 (line)]] | alt | 89.3 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 134 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.08× (z +12.2) | — |
| [[SNU-423 (line)]] | alt | 84.0 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.20× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -11.5) |
| [[H4 (line)]] | wt | 161 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.87× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 162 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -12.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 115 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -13.7) |
| [[hTERT-HPNE (line)]] | wt | 93.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.37× (z +9.7) | — |
| [[J82 (line)]] | alt | 107 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.90× (z +11.1) | — |
| [[Panc 03.27 (line)]] | alt | 49.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.24× (z +13.2) | — |
| [[SW 1088 (line)]] | alt | 112 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0896× (z -8.8) |
| [[SW 900 (line)]] | alt | 88.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.9× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 58.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.80× (z +9.4) | — |
| [[A498 (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 84.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 136 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 98.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 69.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10796), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HK2]] | +0.77 | +0.80 / +0.75 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.77 | +0.80 / +0.77 | both halves | 7e-06 |  |
| [[RNMT]] | +0.73 | +0.82 / +0.67 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[POM121]] | +0.72 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[POM121C]] | +0.72 | +0.81 / +0.64 | both halves | 7e-06 |  |
| [[AK2]] | +0.72 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[PDK1]] | +0.71 | +0.81 / +0.64 | both halves | 7e-06 |  |
| [[WDR45B]] | +0.71 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[DHRS13]] | +0.70 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[HDAC3]] | +0.69 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[ERO1A]] | +0.69 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.69 | +0.80 / +0.59 | both halves | 7e-06 |  |
| [[UBE2O]] | +0.69 | +0.79 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMARCB1]] | -0.57 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[CPLANE1]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[ZNF644]] | -0.56 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[FIZ1]] | -0.55 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[TACC2]] | -0.53 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[PMF1]] | -0.52 | -0.58 / -0.35 | both halves | 1e-04 |  |
| [[POGLUT1]] | -0.52 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[RNF115]] | -0.52 | -0.52 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises FAM210A's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.881). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.5, -19.1); signed map (-39.1, 24.7). **Vector** length 122, 45.3% of its response variance represented; |z| ≥ 3 in 1,348 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.0 | +10.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | +6.8 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +0.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.7 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | +5.2 | +3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.3 | +4.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.6 | +6.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +0.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -12.7 | -6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -11.2 | -10.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.1 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -1.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.7 | -3.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.5 | -1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -0.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.2 | -3.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial inner membrane structural 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.21 — chr18:13,663,347-13,726,663 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC24180, HsT2329; previously C18orf19, FAM210A |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96ND0](https://www.uniprot.org/uniprotkb/Q96ND0) (Mitochondrial inner membrane scaffold 1):

> Mitochondrial inner membrane protein essential for mitochondrial homeostasis, structural integrity, and cellular metabolism. Regulates mitochondrial translation by modulating protein synthesis of mitochondrial DNA-encoded genes. Plays a critical role in skeletal muscle mass and strength by regulating mitochondrial density, function, and protein synthesis. In brown adipose tissue, regulates mitochondrial cristae remodeling in response to cold stress by interacting with mitochondrial protease …

**Summary**, from NCBI Gene [125228](https://www.ncbi.nlm.nih.gov/gene/125228):

> Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28346](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28346) · Entrez [125228](https://www.ncbi.nlm.nih.gov/gene/125228) · UniProt [Q96ND0](https://www.uniprot.org/uniprotkb/Q96ND0) · Ensembl [ENSG00000177150](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177150)

## Data

Gene col 10796: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10796); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10796, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10796]; `tensor/DDL_lfc|DDL_z.npy` [10796]; `embed/gene_vectors.npy` [10796]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10796 or target_col == 10796). Every well: [[FAM210A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM210A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
