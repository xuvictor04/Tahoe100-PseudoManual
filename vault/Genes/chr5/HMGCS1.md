---
symbol: "HMGCS1"
type: "gene"
col: 3420
ensembl_id: "ENSG00000112972"
name: "3-hydroxy-3-methylglutaryl-CoA synthase 1"
location: "5p12"
module: 86
arm: "+"
pooled_cpm: 111.4
n_lines_expressing: 49
n_dd_up: 44
n_dd_down: 10
n_dd_up_clean: 34
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# HMGCS1

*3-hydroxy-3-methylglutaryl-CoA synthase 1* — 5p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.31× (z +25.4, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 0.5 µM: 0.663× (z -5.1, q 2e-04, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IDI1]] (+0.86, fdr 7e-06), [[DHCR7]] (+0.79, fdr 7e-06), [[HMGCR]] (+0.79, fdr 7e-06); moves opposite to [[DTWD1]] (-0.42, fdr 5e-05), [[FBXL5]] (-0.42, fdr 6e-05), [[MTFMT]] (-0.39, fdr 6e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CDHR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3420.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.31×** | +25.4 | 0e+00 | 44/47 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Berbamine (drug)]] 5 µM |  | **2.76×** | +17.6 | 0e+00 | 46/48 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **2.65×** | +16.9 | 0e+00 | 46/47 (NCI-H23, HOP62, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.42×** | +10.9 | 2e-25 | 37/47 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.45×** | +10.6 | 4e-24 | 43/46 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.46×** | +10.5 | 1e-23 | 43/47 (NCI-H2347, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.32×** | +10.3 | 4e-23 | 43/47 (C32, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.07×** | +8.9 | 3e-17 | 41/47 (C32, HS-578T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.05×** | +8.5 | 2e-15 | 33/47 (NCI-H1573, AsPC-1, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.36×** | +7.8 | 4e-13 | 41/44 (NCI-H2347, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.79×** | +7.1 | 6e-11 | 34/47 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.87×** | +6.8 | 6e-10 | 38/48 (SNU-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.05×** | +6.3 | 1e-08 | 39/48 (NCI-H2347, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.70×** | +6.2 | 2e-08 | 34/47 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +6.0 | 8e-08 | 22/44 (J82, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +5.9 | 1e-07 | 30/47 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.64×** | +5.8 | 2e-07 | 33/47 (HOP62, HS-578T, …) | top dose only | plate-row cell shift |
| [[Posaconazole (drug)]] 5 µM |  | **1.64×** | +5.8 | 2e-07 | 34/47 (HEC-1-A, HS-578T, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3420.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 0.5 µM |  | **0.663×** | -5.1 | 2e-04 | 42/47 (KATO III, LoVo, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.673×** | -4.9 | 2e-04 | 31/47 (hTERT-HPNE, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.656×** | -4.8 | 2e-04 | 33/46 (HS-578T, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.686×** | -4.7 | 4e-04 | 36/48 (HEC-1-A, PANC-1, …) | inconsistent across doses |  |
| [[Quinestrol (drug)]] 5 µM |  | **0.806×** | -3.8 | 0.016 | 24/48 (KATO III, NCI-H1792, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.746×** | -3.6 | 0.025 | 23/47 (NCI-H2347, NCI-H1573, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.757×** | -3.5 | 0.044 | 24/47 (HS-578T, PANC-1, …) | inconsistent across doses |  |
| [[Asciminib (drug)]] 5 µM |  | **0.773×** | -3.2 | 0.091 | 21/47 (KATO III, PANC-1, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.837× | -3.2 | 0.091 | 18/47 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.778×** | -3.1 | 0.091 | 19/47 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.778×** | -3.1 | 0.091 | 18/46 (HepG2/C3A, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3420. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 50.2 | 18 (10 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.58× (z +22.5) | — |
| [[HS-578T (line)]] | alt | 135 | 7 | 2 | [[Cepharanthine (drug)]] 5 µM 5.37× (z +18.7) | [[Homoharringtonine (drug)]] 0.05 µM 0.306× (z -9.4) |
| [[LoVo (line)]] | wt | 111 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +31.0) | — |
| [[AsPC-1 (line)]] | alt | 157 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 24.5× (z +35.3) | — |
| [[C32 (line)]] | wt | 59.2 | 8 (1 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 6.78× (z +13.1) | — |
| [[LS 180 (line)]] | wt | 130 | 8 (1 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 4.08× (z +15.1) | — |
| [[HOP62 (line)]] | alt | 53.7 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.97× (z +22.9) | — |
| [[NCI-H2030 (line)]] | alt | 121 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +17.0) | — |
| [[NCI-H2347 (line)]] | alt | 96.9 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +20.4) | — |
| [[A549 (line)]] | wt | 108 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +25.6) | — |
| [[HEC-1-A (line)]] | alt | 98.8 | 6 (1 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 3.63× (z +14.7) | — |
| [[J82 (line)]] | alt | 129 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.47× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.88× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 162 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 31.9× (z +33.4) | — |
| [[A498 (line)]] | wt | 149 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +20.5) | — |
| [[HT-29 (line)]] | alt | 207 | 5 | 0 | [[Cepharanthine (drug)]] 5 µM 3.92× (z +14.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 70.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +16.1) | — |
| [[SW480 (line)]] | alt | 60.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +17.9) | — |
| [[COLO 205 (line)]] | alt | 176 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.1× (z +25.0) | — |
| [[HCT15 (line)]] | alt | 111 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.82× (z +11.2) | — |
| [[KATO III (line)]] | alt | 216 | 1 | 3 | [[Cepharanthine (drug)]] 5 µM 2.56× (z +9.2) | [[Quinestrol (drug)]] 5 µM 0.403× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 56.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.32× (z +24.3) | — |
| [[NCI-H23 (line)]] | alt | 85.5 | 4 (1 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 7.38× (z +22.1) | — |
| [[Panc 03.27 (line)]] | alt | 81.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.58× (z +20.3) | — |
| [[SW 900 (line)]] | alt | 89.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.80× (z +20.5) | — |
| [[C-33 A (line)]] | alt | 58.1 | 3 (1 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 6.65× (z +17.2) | — |
| [[CFPAC-1 (line)]] | alt | 147 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +25.5) | — |
| [[H4 (line)]] | wt | 88.1 | 3 | 0 | [[Berbamine (drug)]] 5 µM 3.91× (z +11.6) | — |
| [[hTERT-HPNE (line)]] | wt | 63.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.99× (z +18.3) | — |
| [[PANC-1 (line)]] | alt | 102 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +12.4) | — |
| [[SNU-423 (line)]] | alt | 64.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.63× (z +18.8) | — |
| [[SW48 (line)]] | wt | 90.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.90× (z +14.2) | — |
| [[A-172 (line)]] | wt | 56.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +18.4) | — |
| [[A-427 (line)]] | wt | 118 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +11.6) | — |
| [[AN3 CA (line)]] | alt | 142 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +10.7) | — |
| [[HepG2_C3A (line)]] | wt | 88.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +14.9) | — |
| [[Hs 766T (line)]] | wt | 92.5 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 2.94× (z +10.0) | — |
| [[SHP-77 (line)]] | alt | 101 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 8.90× (z +18.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 3.03× (z +9.6) | — |
| [[SNU-1 (line)]] | wt | 115 | 2 | 0 | [[Berbamine (drug)]] 5 µM 4.17× (z +11.8) | — |
| [[SW1417 (line)]] | alt | 101 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +14.8) | — |
| [[BT-474 (line)]] | alt | 686 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 93.7 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 6.42× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 141 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +16.4) | — |
| [[SW 1088 (line)]] | alt | 99.4 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0517× (z -9.7) |
| [[SW 1271 (line)]] | alt | 72.6 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0630× (z -9.7) |
| [[NCI-H2122 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 72.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3420), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDI1]] | +0.86 | +0.88 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 972 |
| [[DHCR7]] | +0.79 | +0.79 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 947 |
| [[HMGCR]] | +0.79 | +0.83 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 999 |
| [[CYP51A1]] | +0.77 | +0.76 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 984 |
| [[SCD]] | +0.77 | +0.77 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 794 |
| [[ACAT2]] | +0.77 | +0.80 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 998 |
| [[MSMO1]] | +0.76 | +0.74 / +0.72 | both halves | 7e-06 | pathway: Cholesterol biosynthesis; STRING 964 |
| [[INSIG1]] | +0.74 | +0.74 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 885 |
| [[FDPS]] | +0.73 | +0.74 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 997 |
| [[LPIN1]] | +0.72 | +0.81 / +0.61 | both halves | 7e-06 | STRING 513 |
| [[SC5D]] | +0.72 | +0.74 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 903 |
| [[FDFT1]] | +0.72 | +0.73 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 988 |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTWD1]] | -0.42 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[FBXL5]] | -0.42 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[MTFMT]] | -0.39 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[LIN9]] | -0.39 | -0.36 / -0.38 | both halves | 9e-05 |  |
| [[NCBP3]] | -0.39 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[TMEM168]] | -0.37 | -0.34 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDHR2]] | B | CDHR2 activity raises HMGCS1's level | lines that do not express CDHR2 (30) vs lines expressing it (20) | 1.29× lower at baseline in the lines without CDHR2 | 0.084 | ⚠ within organs, on part of the lines; also absent: VIL1, NPSR1-AS1, EPS8L3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.866). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.1, -49.2); signed map (-52.6, 32.4). **Vector** length 141, 53.8% of its response variance represented; |z| ≥ 3 in 1,795 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cholesterol biosynthesis via desmosterol (Bloch pathway)* (reactome, mean cos +0.67 to 8); *Zymostenol biosynthesis via lathosterol (Kandutsch-Russell pathway)* (reactome, mean cos +0.61 to 7); *SREBP1 lipogenesis* (control, mean cos +0.61 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +11.7 | +16.9 |
|  | [[Berbamine (drug)]] 5 µM |  | +10.4 | +17.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +7.3 | +5.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.0 | +10.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +6.9 | +0.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +6.7 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.4 | +3.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -7.0 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.6 | -3.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -6.1 | +4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | -1.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -5.7 | +4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.5 | -4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.4 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.1 | -2.9 |
|  | [[Quinestrol (drug)]] 5 µM |  | -3.3 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | 3-hydroxy-3-methylglutaryl-CoA synthase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p12 — chr5:43,287,470-43,313,512 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HMGCS |
| Gene groups (HGNC) | 3-hydroxy-3-methylglutaryl-CoA synthase family |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, ANDROGEN_RESPONSE, FATTY_ACID_METABOLISM, MTORC1_SIGNALING |
| Reactome | 8 pathways, smallest: Lanosterol biosynthesis; Cholesterol biosynthesis; Activation of gene expression by SREBF (SREBP) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01581](https://www.uniprot.org/uniprotkb/Q01581) (Hydroxymethylglutaryl-CoA synthase, cytoplasmic):

> Catalyzes the condensation of acetyl-CoA with acetoacetyl-CoA to form HMG-CoA, which is converted by HMG-CoA reductase (HMGCR) into mevalonate, a precursor for cholesterol synthesis.

**Summary**, from NCBI Gene [3157](https://www.ncbi.nlm.nih.gov/gene/3157):

> Enables hydroxymethylglutaryl-CoA synthase activity and protein homodimerization activity. Predicted to be involved in acetyl-CoA metabolic process and farnesyl diphosphate biosynthetic process, mevalonate pathway. Located in cytosol; nucleoplasm; and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:5007](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5007) · Entrez [3157](https://www.ncbi.nlm.nih.gov/gene/3157) · UniProt [Q01581](https://www.uniprot.org/uniprotkb/Q01581) · Ensembl [ENSG00000112972](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112972)

## Data

Gene col 3420: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3420); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3420, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3420]; `tensor/DDL_lfc|DDL_z.npy` [3420]; `embed/gene_vectors.npy` [3420]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3420 or target_col == 3420). Every well: [[HMGCS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMGCS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
