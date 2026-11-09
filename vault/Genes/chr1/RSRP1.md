---
symbol: "RSRP1"
type: "gene"
col: 3933
ensembl_id: "ENSG00000117616"
name: "arginine and serine rich protein 1"
location: "1p36.11"
module: 4
arm: "-"
pooled_cpm: 130.68
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 16
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# RSRP1

*arginine and serine rich protein 1* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.10× (z +21.3, q 0e+00, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.514× (z -13.0, q 1e-35, down in 37 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.736× (z -5.9, q 3e-07, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AAMDC]] (+0.78, fdr 7e-06), [[TERF2IP]] (+0.72, fdr 7e-06), [[CD27-AS1]] (+0.72, fdr 7e-06); moves opposite to [[TMEM33]] (-0.72, fdr 7e-06), [[AGPS]] (-0.72, fdr 7e-06), [[FARSB]] (-0.71, fdr 1e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3933.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +21.3 | 0e+00 | 46/49 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +15.1 | 0e+00 | 40/48 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +14.7 | 0e+00 | 43/50 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +12.2 | 8e-32 | 42/48 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +9.4 | 4e-19 | 39/47 (RKO, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.13× | +3.5 | 0.041 | 9/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Terfenadine (drug)]] 5 µM |  | 1.13× | +3.4 | 0.048 | 5/48 (H4, NCI-H2030, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.18× | +3.3 | 0.050 | 16/48 (Panc 03.27, H4, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.18× | +3.3 | 0.050 | 20/48 (C32, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.3 | 0.050 | 22/48 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.065 | 17/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.078 | 17/48 (CFPAC-1, A-427, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3933.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.514×** | -13.0 | 1e-35 | 37/44 (SNU-423, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.549×** | -12.1 | 2e-31 | 35/49 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.676×** | -7.9 | 5e-13 | 43/48 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.692×** | -6.9 | 7e-10 | 33/45 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.736×** | -5.9 | 3e-07 | 36/48 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.751×** | -5.8 | 7e-07 | 31/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.587×** | -5.6 | 1e-06 | 37/48 (PANC-1, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.634×** | -4.8 | 1e-04 | 31/48 (Panc 03.27, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.779×** | -4.7 | 2e-04 | 31/48 (SW480, NCI-H1573, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.652×** | -4.5 | 3e-04 | 27/48 (PANC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.788×** | -4.5 | 4e-04 | 30/48 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.806×** | -4.4 | 6e-04 | 25/48 (COLO 205, A549, …) | two highest doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.794×** | -4.3 | 8e-04 | 26/48 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.675×** | -4.2 | 0.001 | 24/48 (HEC-1-A, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.688×** | -4.0 | 0.003 | 25/48 (HEC-1-A, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.820×** | -3.8 | 0.005 | 24/48 (hTERT-HPNE, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 0.836× | -3.3 | 0.027 | 19/48 (CFPAC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.840× | -3.3 | 0.034 | 16/49 (HT-29, NCI-H2030, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.843× | -3.2 | 0.039 | 20/49 (NCI-H1573, LS 180, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.851× | -3.1 | 0.052 | 18/48 (SW1417, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3933. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 85.4 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +15.7) | — |
| [[HS-578T (line)]] | alt | 199 | 4 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -11.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 103 | 5 (1 ⚠) | 2 (2 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -10.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 140 | 5 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.491× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 125 | 1 | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.302× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.436× (z -9.8) |
| [[C32 (line)]] | wt | 89.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +21.4) | — |
| [[CFPAC-1 (line)]] | alt | 170 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +13.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.486× (z -10.3) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 117 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +15.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.523× (z -8.6) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 220 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -22.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 126 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +17.5) | — |
| [[NCI-H1792 (line)]] | alt | 162 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +19.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.409× (z -12.1) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.522× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 135 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +12.4) | — |
| [[SNU-423 (line)]] | alt | 141 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.212× (z -19.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 85.3 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.465× (z -8.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 166 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +19.8) | — |
| [[HT-29 (line)]] | alt | 127 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +12.5) | — |
| [[Panc 03.27 (line)]] | alt | 121 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +14.4) | [[Dinaciclib (drug)]] 0.5 µM 0.479× (z -8.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 94.3 | 4 (1 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 4.44× (z +12.9) | — |
| [[SK-MEL-2 (line)]] | alt | 132 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +17.5) | — |
| [[SW 900 (line)]] | alt | 136 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -12.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 102 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +15.7) | — |
| [[NCI-H2030 (line)]] | alt | 153 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +13.4) | — |
| [[NCI-H23 (line)]] | alt | 175 | 1 | 2 (2 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -13.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 172 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +18.9) | [[Dinaciclib (drug)]] 0.5 µM 0.491× (z -11.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 104 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.133× (z -16.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 94.8 | 1 | 1 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.273× (z -16.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 112 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +15.5) | — |
| [[A549 (line)]] | wt | 86.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.61× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.498× (z -8.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 86.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +8.8) | [[AZD2858 (drug)]] 0.5 µM 0.0859× (z -10.6) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 123 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.78× (z +26.5) | — |
| [[BT-474 (line)]] | alt | 63.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +16.3) | — |
| [[C-33 A (line)]] | alt | 139 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +9.5) | — |
| [[HepG2_C3A (line)]] | wt | 166 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +16.4) | — |
| [[hTERT-HPNE (line)]] | wt | 243 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -11.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 97.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +11.5) | — |
| [[LoVo (line)]] | wt | 101 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +17.6) | — |
| [[LS 180 (line)]] | wt | 119 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.3) | — |
| [[NCI-H1573 (line)]] | alt | 154 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -20.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 127 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +16.4) | — |
| [[COLO 205 (line)]] | alt | 122 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +10.7) | — |
| [[H4 (line)]] | wt | 136 | 1 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +8.6) | — |
| [[J82 (line)]] | alt | 126 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +16.9) | — |
| [[SHP-77 (line)]] | alt | 86.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +13.5) | — |
| [[SW 1088 (line)]] | alt | 191 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0692× (z -12.4) |
| [[CHP-212 (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 148 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3933), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AAMDC]] | +0.78 | +0.76 / +0.84 | both halves | 7e-06 |  |
| [[TERF2IP]] | +0.72 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[CD27-AS1]] | +0.72 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[POLR2A]] | +0.70 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[FAM117A]] | +0.70 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[CCDC115]] | +0.70 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[PIK3CA]] | +0.69 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[ADCY10]] | +0.69 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[KLC4]] | +0.69 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[ZNF490]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[OSER1-DT]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[IST1]] | +0.67 | +0.55 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM33]] | -0.72 | -0.64 / -0.77 | both halves | 7e-06 |  |
| [[AGPS]] | -0.72 | -0.62 / -0.76 | both halves | 7e-06 |  |
| [[FARSB]] | -0.71 | -0.55 / -0.71 | both halves | 1e-05 |  |
| [[RUVBL1]] | -0.71 | -0.57 / -0.70 | both halves | 8e-06 |  |
| [[GFM1]] | -0.69 | -0.57 / -0.70 | both halves | 8e-06 |  |
| [[NAA15]] | -0.69 | -0.62 / -0.73 | both halves | 7e-06 |  |
| [[EIPR1]] | -0.69 | -0.70 / -0.67 | both halves | 7e-06 |  |
| [[PTPN11]] | -0.69 | -0.54 / -0.78 | both halves | 1e-05 |  |
| [[HERC2]] | -0.69 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[EFTUD2]] | -0.68 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[POLR1A]] | -0.68 | -0.64 / -0.71 | both halves | 7e-06 |  |
| [[PRKDC]] | -0.68 | -0.61 / -0.66 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RSRP1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HOXA5]] | B | HOXA5 activity raises RSRP1's level | lines that do not express HOXA5 (9) vs lines expressing it (41) | 1.35× lower at baseline in the lines without HOXA5 | 0.046 | ⚠ within organs, on part of the lines; also absent: HOXA3, HOXA6, HOTAIRM1 |
| [[SRPX2]] | B | SRPX2 activity raises RSRP1's level | lines that do not express SRPX2 (24) vs lines expressing it (26) | 1.31× lower at baseline in the lines without SRPX2 | 0.070 | ⚠ within organs, on part of the lines; also absent: TGFBI, GBP5, FN1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.809). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-3.5, -40.7); signed map (-10.9, 8.6). **Vector** length 145, 46.7% of its response variance represented; |z| ≥ 3 in 1,116 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +21.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +12.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +14.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.3 | +9.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.7 | +3.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.7 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +3.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.1 | +1.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.1 | +2.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.6 | -7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -9.6 | -12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.6 | -13.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.1 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.9 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.3 | -1.8 |
|  | [[EX229 (drug)]] 5 µM |  | -6.3 | -4.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.3 | -5.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.1 | -4.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.3 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | arginine and serine rich protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:25,242,249-25,338,213 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DJ465N24.2.1; previously C1orf63 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUV0](https://www.uniprot.org/uniprotkb/Q9BUV0) (Arginine/serine-rich protein 1):

> Probably acts as a spliceosomal factor that contributes to spliceosome assembly and regulates the isoform switching of proteins such as PARP6.

**Summary**, from NCBI Gene [57035](https://www.ncbi.nlm.nih.gov/gene/57035):

> Involved in spliceosomal complex assembly. Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25234](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25234) · Entrez [57035](https://www.ncbi.nlm.nih.gov/gene/57035) · UniProt [Q9BUV0](https://www.uniprot.org/uniprotkb/Q9BUV0) · Ensembl [ENSG00000117616](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117616)

## Data

Gene col 3933: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3933); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3933, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3933]; `tensor/DDL_lfc|DDL_z.npy` [3933]; `embed/gene_vectors.npy` [3933]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3933 or target_col == 3933). Every well: [[RSRP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RSRP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
