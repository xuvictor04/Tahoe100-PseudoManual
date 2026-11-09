---
symbol: "CYP51A1"
type: "gene"
col: 15
ensembl_id: "ENSG00000001630"
name: "cytochrome P450 family 51 subfamily A member 1"
location: "7q21.2"
module: 86
arm: "+"
pooled_cpm: 107.17
n_lines_expressing: 49
n_dd_up: 27
n_dd_down: 13
n_dd_up_clean: 20
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# CYP51A1

*cytochrome P450 family 51 subfamily A member 1* — 7q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Berbamine (drug)]] 5 µM: 2.27× (z +18.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.902× (z -5.6, q 2e-05, down in 1 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.791× (z -5.2, q 5e-05, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SC5D]] (+0.85, fdr 7e-06), [[MSMO1]] (+0.80, fdr 7e-06), [[DHCR7]] (+0.80, fdr 7e-06); moves opposite to [[ZC3H18]] (-0.45, fdr 6e-05), [[KIFC3]] (-0.41, fdr 6e-05), [[DHRS7B]] (-0.41, fdr 8e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Berbamine (drug)]] 5 µM |  | **2.27×** | +18.2 | 0e+00 | 47/48 (LoVo, HOP62, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **2.21×** | +17.5 | 0e+00 | 45/47 (HOP62, LoVo, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.28×** | +12.9 | 8e-36 | 42/48 (A549, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +10.9 | 2e-25 | 43/46 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +9.9 | 6e-21 | 39/43 (A549, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 5 µM |  | **1.59×** | +7.0 | 2e-10 | 37/47 (HOP62, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +6.8 | 8e-10 | 31/44 (J82, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.52×** | +6.5 | 5e-09 | 36/47 (HOP62, A498, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | **1.33×** | +6.4 | 1e-08 | 39/47 (HEC-1-A, LS 180, …) | rises with dose |  |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +5.7 | 6e-07 | 35/47 (HOP62, A498, …) | top dose only | plate-row cell shift |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.42×** | +5.3 | 7e-06 | 31/48 (C32, HOP62, …) | top dose only | plate-row cell shift |
| [[Posaconazole (drug)]] 5 µM |  | **1.38×** | +4.9 | 5e-05 | 29/47 (HEC-1-A, AsPC-1, …) | rises with dose | plate-row cell shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +4.3 | 7e-04 | 22/47 (HEC-1-A, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.31×** | +4.2 | 9e-04 | 31/47 (C32, hTERT-HPNE, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.004 | 27/47 (HT-29, A498, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +3.8 | 0.004 | 20/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Ritonavir (drug)]] 5 µM |  | 1.18× | +3.6 | 0.009 | 18/47 (PANC-1, LS 180, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.013 | 23/47 (C32, Panc 03.27, …) | rises with dose |  |
| [[Cyclosporin A (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.014 | 22/47 (SW48, NCI-H1573, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.902× | -5.6 | 2e-05 | 1/49 (NCI-H23) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.791×** | -5.2 | 5e-05 | 30/47 (RKO, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.727×** | -5.0 | 1e-04 | 28/47 (AsPC-1, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.745×** | -4.6 | 6e-04 | 30/47 (BT-474, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Quinestrol (drug)]] 5 µM |  | **0.824×** | -4.3 | 0.002 | 25/48 (RKO, NCI-H1792, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.826×** | -4.3 | 0.002 | 23/47 (RPMI-7951, CFPAC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.771×** | -4.1 | 0.003 | 28/47 (LoVo, NCI-H23, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.783×** | -3.7 | 0.016 | 24/48 (NCI-H2347, AsPC-1, …) | top dose only | plate-row cell shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.785×** | -3.7 | 0.016 | 24/47 (LoVo, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.794×** | -3.6 | 0.016 | 23/47 (BT-474, AsPC-1, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.726×** | -3.6 | 0.017 | 22/47 (HT-29, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.785×** | -3.5 | 0.021 | 26/46 (RKO, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Asciminib (drug)]] 5 µM |  | **0.807×** | -3.4 | 0.034 | 23/47 (LS 180, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.806×** | -3.3 | 0.047 | 21/47 (CFPAC-1, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 73.1 | 6 (3 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 3.79× (z +19.8) | — |
| [[J82 (line)]] | alt | 93.1 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Berbamine (drug)]] 5 µM 1.99× (z +9.5) | — |
| [[NCI-H460 (line)]] | wt | 92.3 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.98× (z +10.4) | — |
| [[C32 (line)]] | wt | 148 | 5 (3 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 2.98× (z +13.7) | — |
| [[Panc 03.27 (line)]] | alt | 87.1 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Berbamine (drug)]] 5 µM 2.59× (z +10.7) | — |
| [[RKO (line)]] | wt | 207 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -19.2) |
| [[A498 (line)]] | wt | 86.9 | 4 (2 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 2.57× (z +15.1) | — |
| [[A549 (line)]] | wt | 79.9 | 4 (2 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 3.19× (z +16.6) | — |
| [[AsPC-1 (line)]] | alt | 185 | 3 (1 ⚠) | 1 (1 ⚠) | [[Berbamine (drug)]] 5 µM 3.15× (z +16.0) | [[Panobinostat (drug)]] 0.5 µM 0.370× (z -9.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[BT-474 (line)]] | alt | 171 | 2 | 2 (2 ⚠) | [[Berbamine (drug)]] 5 µM 2.16× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.325× (z -10.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[LoVo (line)]] | wt | 149 | 4 (2 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 4.38× (z +20.4) | — |
| [[LOX-IMVI (line)]] | wt | 70.9 | 4 (2 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 2.18× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 80.3 | 4 (2 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 2.98× (z +14.6) | — |
| [[PANC-1 (line)]] | alt | 116 | 4 (2 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 1.90× (z +10.1) | — |
| [[CFPAC-1 (line)]] | alt | 156 | 2 | 1 | [[Berbamine (drug)]] 5 µM 2.21× (z +11.1) | [[Harringtonine (drug)]] 5 µM 0.385× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 119 | 3 (1 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 2.75× (z +15.4) | — |
| [[LS 180 (line)]] | wt | 146 | 3 | 0 | [[Berbamine (drug)]] 5 µM 3.73× (z +16.7) | — |
| [[SNU-1 (line)]] | wt | 185 | 2 | 1 | [[Berbamine (drug)]] 5 µM 2.86× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -10.0) |
| [[SNU-423 (line)]] | alt | 90.6 | 3 (1 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 2.73× (z +12.3) | — |
| [[SW 900 (line)]] | alt | 74.9 | 3 (1 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 2.88× (z +12.5) | — |
| [[SW480 (line)]] | alt | 79.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Berbamine (drug)]] 5 µM 1.98× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 103 | 2 | 0 | [[Berbamine (drug)]] 5 µM 2.68× (z +12.1) | — |
| [[COLO 205 (line)]] | alt | 51.9 | 2 | 0 | [[Berbamine (drug)]] 5 µM 3.74× (z +11.0) | — |
| [[H4 (line)]] | wt | 90.4 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.37× (z +13.4) | — |
| [[Hs 766T (line)]] | wt | 94.9 | 2 | 0 | [[Berbamine (drug)]] 5 µM 2.09× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 137 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.21× (z +16.3) | — |
| [[HT-29 (line)]] | alt | 138 | 2 | 0 | [[Berbamine (drug)]] 5 µM 3.07× (z +16.2) | — |
| [[hTERT-HPNE (line)]] | wt | 78.2 | 2 | 0 | [[Berbamine (drug)]] 5 µM 2.33× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 132 | 2 | 0 | [[Berbamine (drug)]] 5 µM 2.22× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 80.3 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.23× (z +9.6) ⚠ toxic · without an alert: [[Berbamine (drug)]] 5 µM 2.21× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 169 | 1 | 1 | [[Cepharanthine (drug)]] 5 µM 1.99× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 108 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.00× (z +14.3) | — |
| [[RPMI-7951 (line)]] | alt | 96.7 | 2 | 0 | [[Berbamine (drug)]] 5 µM 1.90× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 67.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 63.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.424× (z -8.5) |
| [[A-427 (line)]] | wt | 109 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +8.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 151 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 126 | 1 | 0 | [[Berbamine (drug)]] 5 µM 2.29× (z +10.2) | — |
| [[HepG2_C3A (line)]] | wt | 124 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 90.2 | 1 | 0 | [[Berbamine (drug)]] 5 µM 2.11× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 83.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 215 | 1 | 0 | [[Berbamine (drug)]] 5 µM 2.14× (z +10.0) | — |
| [[CHP-212 (line)]] | wt | 90.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SC5D]] | +0.85 | +0.79 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 987 |
| [[MSMO1]] | +0.80 | +0.85 / +0.77 | both halves | 7e-06 | pathway: Cholesterol biosynthesis; STRING 996 |
| [[DHCR7]] | +0.80 | +0.82 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 978 |
| [[SCD]] | +0.78 | +0.77 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 580 |
| [[HMGCS1]] | +0.77 | +0.76 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 984 |
| [[HMGCR]] | +0.77 | +0.87 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 948 |
| [[IDI1]] | +0.76 | +0.76 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 942 |
| [[ACAT2]] | +0.72 | +0.71 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 732 |
| [[FDPS]] | +0.72 | +0.77 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 886 |
| [[FDFT1]] | +0.70 | +0.80 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 997 |
| [[ACSS2]] | +0.68 | +0.72 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 511 |
| [[STARD4]] | +0.67 | +0.70 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 484 |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H18]] | -0.45 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[KIFC3]] | -0.41 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[DHRS7B]] | -0.41 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[GGA3]] | -0.40 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[DCAF15]] | -0.39 | -0.28 / -0.39 | both halves | 3e-04 |  |
| [[MTG2]] | -0.39 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[MECR]] | -0.37 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[ALKBH1]] | -0.37 | -0.34 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.834). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.2, -49.3); signed map (-52.6, 32.3). **Vector** length 141, 48.8% of its response variance represented; |z| ≥ 3 in 1,402 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Lanosterol biosynthesis* (reactome, mean cos +0.68 to 10); *SREBP1 lipogenesis* (control, mean cos +0.60 to 6); *androgen response* (hallmark, mean cos +0.65 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +11.6 | +9.9 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +11.4 | +17.5 |
|  | [[Berbamine (drug)]] 5 µM |  | +10.4 | +18.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.9 | +12.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +8.8 | +10.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +6.7 | +6.5 |
|  | [[Adagrasib (drug)]] 5 µM |  | +6.1 | +7.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | +5.8 | +6.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.2 | -1.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.8 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | +0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.5 | -2.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.3 | +0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.1 | -3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.2 | -1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.1 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome P450 family 51 subfamily A member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.2 — chr7:92,084,987-92,134,803 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CP51, CYPL1, P450L1, LDM, P450-14DM; previously CYP51 |
| Gene groups (HGNC) | Cytochrome P450 family 51 |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, MTORC1_SIGNALING |
| Reactome | 13 pathways, smallest: Zymostenol biosynthesis via lathosterol (Kandutsch-Russell pathway); Cholesterol biosynthesis via desmosterol (Bloch pathway); Endogenous sterols |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16850](https://www.uniprot.org/uniprotkb/Q16850) (Lanosterol 14-alpha demethylase):

> Sterol 14alpha-demethylase that plays a critical role in the cholesterol biosynthesis pathway, being cholesterol the major sterol component in mammalian membranes as well as a precursor for bile acid and steroid hormone synthesis. Cytochrome P450 monooxygenase that catalyzes the three-step oxidative removal of the 14alpha-methyl group (C-32) of sterols such as lanosterol (lanosta-8,24-dien-3beta-ol) and 24,25-dihydrolanosterol (DHL) in the form of formate, and converts the sterols to …

**Summary**, from NCBI Gene [1595](https://www.ncbi.nlm.nih.gov/gene/1595):

> This gene encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. This endoplasmic reticulum protein participates in the synthesis of cholesterol by catalyzing the removal of the 14alpha-methyl group from lanosterol. Homologous genes are found in all three eukaryotic phyla, fungi, plants, and animals, suggesting that this is …

**Accessions** — [HGNC:2649](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2649) · Entrez [1595](https://www.ncbi.nlm.nih.gov/gene/1595) · UniProt [Q16850](https://www.uniprot.org/uniprotkb/Q16850) · Ensembl [ENSG00000001630](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000001630)

## Data

Gene col 15: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15]; `tensor/DDL_lfc|DDL_z.npy` [15]; `embed/gene_vectors.npy` [15]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15 or target_col == 15). Every well: [[CYP51A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYP51A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
