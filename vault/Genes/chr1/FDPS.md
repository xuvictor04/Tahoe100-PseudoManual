---
symbol: "FDPS"
type: "gene"
col: 8376
ensembl_id: "ENSG00000160752"
name: "farnesyl diphosphate synthase"
location: "1q22"
module: 86
arm: "+"
pooled_cpm: 88.66
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 20
n_dd_up_clean: 21
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# FDPS

*farnesyl diphosphate synthase* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Cepharanthine (drug)]] 5 µM: 2.65× (z +17.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.413× (z -15.6, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MVD]] (+0.87, fdr 7e-06), [[MSMO1]] (+0.86, fdr 7e-06), [[HMGCR]] (+0.84, fdr 7e-06); moves opposite to [[KLF10]] (-0.50, fdr 2e-05), [[VEZF1]] (-0.48, fdr 3e-05), [[CSTF2T]] (-0.48, fdr 3e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8376.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cepharanthine (drug)]] 5 µM |  | **2.65×** | +17.2 | 0e+00 | 47/48 (NCI-H23, HT-29, …) | top dose only |  |
| [[Berbamine (drug)]] 5 µM |  | **2.59×** | +16.8 | 0e+00 | 47/49 (NCI-H23, HT-29, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.19×** | +9.4 | 1e-18 | 43/47 (LoVo, C-33 A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.75×** | +7.0 | 3e-10 | 43/48 (C32, AsPC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.74×** | +6.9 | 6e-10 | 35/49 (J82, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.71×** | +6.7 | 2e-09 | 39/48 (NCI-H2030, C-33 A, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.72×** | +6.5 | 5e-09 | 41/49 (AsPC-1, HOP62, …) | top dose only | plate-row cell shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.71×** | +6.3 | 2e-08 | 33/48 (MIA PaCa-2, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 5 µM |  | **1.65×** | +6.0 | 1e-07 | 33/48 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[Posaconazole (drug)]] 5 µM |  | **1.61×** | +5.7 | 7e-07 | 38/48 (HEC-1-A, AsPC-1, …) | rises with dose | plate-row cell shift |
| [[Terfenadine (drug)]] 5 µM |  | **1.35×** | +5.4 | 4e-06 | 34/48 (HT-29, SW 900, …) | top dose only | position effect removed |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +5.3 | 7e-06 | 35/48 (C-33 A, HEC-1-A, …) | top dose only | plate-row cell shift |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.54×** | +5.2 | 7e-06 | 34/48 (SW 900, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +5.0 | 3e-05 | 32/48 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.03×** | +4.6 | 1e-04 | 32/45 (HCT15, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +4.4 | 4e-04 | 23/48 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Ritonavir (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.001 | 26/48 (PANC-1, LS 180, …) | rises with dose |  |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.002 | 33/48 (SNU-423, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8376.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.413×** | -15.6 | 0e+00 | 45/48 (HT-29, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.449×** | -10.0 | 4e-21 | 46/48 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.446×** | -9.7 | 7e-20 | 44/48 (KATO III, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.586×** | -6.7 | 4e-09 | 36/48 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.617×** | -5.8 | 7e-07 | 35/48 (BT-474, COLO 205, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.629×** | -5.8 | 7e-07 | 37/48 (A-427, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.740×** | -5.3 | 9e-06 | 36/48 (SW 900, BT-474, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.706×** | -4.0 | 0.004 | 29/47 (SNU-1, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.719×** | -3.9 | 0.006 | 25/47 (LOX-IMVI, RKO, …) | inconsistent across doses |  |
| [[Quinestrol (drug)]] 5 µM |  | **0.808×** | -3.8 | 0.010 | 26/49 (KATO III, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.742×** | -3.7 | 0.010 | 25/48 (AsPC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.746×** | -3.7 | 0.012 | 28/48 (BT-474, LS 180, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.754×** | -3.5 | 0.019 | 29/48 (BT-474, KATO III, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Sapanisertib (drug)]] 0.05 µM |  | **0.744×** | -3.5 | 0.020 | 27/48 (CFPAC-1, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.768×** | -3.3 | 0.038 | 25/48 (KATO III, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8376. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 89.4 | 4 (1 ⚠) | 4 | [[Berbamine (drug)]] 5 µM 3.45× (z +15.4) | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -15.3) |
| [[LoVo (line)]] | wt | 63.5 | 7 (3 ⚠) | 1 | [[Berbamine (drug)]] 5 µM 3.99× (z +18.3) | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -10.5) |
| [[BT-474 (line)]] | alt | 161 | 2 | 5 | [[Cepharanthine (drug)]] 5 µM 2.82× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -13.3) |
| [[CFPAC-1 (line)]] | alt | 116 | 4 | 3 | [[Bortezomib (drug)]] 0.05 µM 5.61× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -13.3) |
| [[HCT15 (line)]] | alt | 236 | 3 | 4 | [[Berbamine (drug)]] 5 µM 3.31× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -13.2) |
| [[HT-29 (line)]] | alt | 91.1 | 4 | 2 | [[Cepharanthine (drug)]] 5 µM 4.89× (z +20.5) | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -18.3) |
| [[KATO III (line)]] | alt | 151 | 2 | 4 | [[Cepharanthine (drug)]] 5 µM 2.68× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -17.5) |
| [[LS 180 (line)]] | wt | 150 | 5 | 1 | [[Berbamine (drug)]] 5 µM 5.06× (z +16.6) | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 89.7 | 6 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.80× (z +13.3) | — |
| [[NCI-H460 (line)]] | wt | 82.7 | 4 (1 ⚠) | 2 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.84× (z +13.4) | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -13.4) |
| [[SW 900 (line)]] | alt | 117 | 3 | 3 | [[Berbamine (drug)]] 5 µM 3.74× (z +17.5) | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -17.1) |
| [[A498 (line)]] | wt | 95.1 | 2 | 3 | [[Berbamine (drug)]] 5 µM 2.41× (z +13.2) | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -18.0) |
| [[HEC-1-A (line)]] | alt | 84.3 | 4 (1 ⚠) | 1 | [[Berbamine (drug)]] 5 µM 3.19× (z +14.8) | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 140 | 3 (1 ⚠) | 2 | [[Cepharanthine (drug)]] 5 µM 4.94× (z +22.3) | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -14.5) |
| [[A-427 (line)]] | wt | 130 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -15.2) |
| [[C-33 A (line)]] | alt | 90.3 | 4 (1 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 4.44× (z +16.5) | — |
| [[COLO 205 (line)]] | alt | 142 | 2 | 2 | [[Berbamine (drug)]] 5 µM 3.48× (z +12.4) | [[Harringtonine (drug)]] 5 µM 0.154× (z -12.5) |
| [[HOP62 (line)]] | alt | 47.3 | 3 (1 ⚠) | 1 | [[Cepharanthine (drug)]] 5 µM 4.64× (z +18.0) | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 139 | 3 | 1 | [[Cepharanthine (drug)]] 5 µM 4.03× (z +16.5) | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 46.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.98× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Berbamine (drug)]] 5 µM 2.16× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 105 | 2 | 2 | [[Berbamine (drug)]] 5 µM 2.27× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.5) |
| [[C32 (line)]] | wt | 52.0 | 3 | 0 | [[Cepharanthine (drug)]] 5 µM 3.53× (z +12.1) | — |
| [[HS-578T (line)]] | alt | 53.6 | 2 | 1 | [[Cepharanthine (drug)]] 5 µM 3.98× (z +14.4) | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 56.7 | 3 | 0 | [[Cepharanthine (drug)]] 5 µM 4.10× (z +13.1) | — |
| [[J82 (line)]] | alt | 68.3 | 2 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Cepharanthine (drug)]] 5 µM 1.87× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 102 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -13.8) |
| [[SW480 (line)]] | alt | 89.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -16.6) |
| [[A549 (line)]] | wt | 39.7 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 6.80× (z +17.7) | — |
| [[H4 (line)]] | wt | 58.2 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.25× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 48.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.321× (z -8.6) |
| [[SNU-1 (line)]] | wt | 88.5 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.00× (z +10.3) | — |
| [[SNU-423 (line)]] | alt | 43.5 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 4.11× (z +14.0) | — |
| [[A-172 (line)]] | wt | 63.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +9.5) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 87.9 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 3.22× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 84.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 80.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 81.8 | 1 | 0 | [[Berbamine (drug)]] 5 µM 2.07× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 55.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -15.4) |
| [[SW1417 (line)]] | alt | 57.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -11.1) |
| [[SW48 (line)]] | wt | 96.1 | 1 | 0 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 4.20× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 98.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 80.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8376), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MVD]] | +0.87 | +0.88 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 995 |
| [[MSMO1]] | +0.86 | +0.87 / +0.85 | both halves | 7e-06 | pathway: Cholesterol biosynthesis; STRING 787 |
| [[HMGCR]] | +0.84 | +0.84 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 967 |
| [[FDFT1]] | +0.83 | +0.86 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 995 |
| [[ACSS2]] | +0.82 | +0.83 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 520 |
| [[SREBF2]] | +0.80 | +0.82 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 896 |
| [[IDI1]] | +0.78 | +0.75 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 994 |
| [[SCD]] | +0.77 | +0.81 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 559 |
| [[EBP]] | +0.77 | +0.80 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 675 |
| [[ACAT2]] | +0.76 | +0.69 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 829 |
| [[PCSK9]] | +0.75 | +0.73 / +0.70 | both halves | 7e-06 | STRING 404 |
| [[DHCR7]] | +0.75 | +0.79 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 816 |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF10]] | -0.50 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[VEZF1]] | -0.48 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[CSTF2T]] | -0.48 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[ENC1]] | -0.47 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[TIGD2]] | -0.47 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[ADO]] | -0.46 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[AMOTL2]] | -0.46 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[TRMT5]] | -0.45 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[ZNF260]] | -0.44 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ZBTB33]] | -0.43 | -0.37 / -0.48 | both halves | 7e-05 |  |
| [[ZNF502]] | -0.43 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[AASDHPPT]] | -0.43 | -0.42 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.886). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.4, -49.1); signed map (-53.0, 32.4). **Vector** length 152, 56.5% of its response variance represented; |z| ≥ 3 in 1,623 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mTORC1 signaling* (hallmark, mean cos +0.65 to 19); *Cholesterol biosynthesis via desmosterol (Bloch pathway)* (reactome, mean cos +0.71 to 8); *Zymostenol biosynthesis via lathosterol (Kandutsch-Russell pathway)* (reactome, mean cos +0.69 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +12.6 | +17.2 |
|  | [[Berbamine (drug)]] 5 µM |  | +10.9 | +16.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +8.4 | +9.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.3 | +6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.7 | +0.1 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +6.5 | +6.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +6.3 | +7.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +6.1 | +6.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -12.4 | -6.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.8 | -9.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -9.7 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.9 | -10.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -6.6 | -5.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.1 | -4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.4 | -3.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | farnesyl diphosphate synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:155,308,748-155,320,666 (+) |
| Ensembl biotype | protein_coding |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, PEROXISOME, MYOGENESIS |
| Reactome | 6 pathways, smallest: Lanosterol biosynthesis; Cholesterol biosynthesis; Activation of gene expression by SREBF (SREBP) |
| Matched by | ensembl_id |

**Function**, from UniProt [P14324](https://www.uniprot.org/uniprotkb/P14324) (Farnesyl pyrophosphate synthase):

> Key enzyme in isoprenoid biosynthesis which catalyzes the formation of farnesyl diphosphate (FPP), a precursor for several classes of essential metabolites including sterols, dolichols, carotenoids, and ubiquinones. FPP also serves as substrate for protein farnesylation and geranylgeranylation. Catalyzes the sequential condensation of isopentenyl pyrophosphate with the allylic pyrophosphates, dimethylallyl pyrophosphate, and then with the resultant geranylpyrophosphate to the ultimate product …

**Summary**, from NCBI Gene [2224](https://www.ncbi.nlm.nih.gov/gene/2224):

> This gene encodes an enzyme that catalyzes the production of geranyl pyrophosphate and farnesyl pyrophosphate from isopentenyl pyrophosphate and dimethylallyl pyrophosphate. The resulting product, farnesyl pyrophosphate, is a key intermediate in cholesterol and sterol biosynthesis, a substrate for protein farnesylation and geranylgeranylation, and a ligand or agonist for certain hormone receptors and growth receptors. Drugs that inhibit this enzyme prevent the post-translational modifications …

**Accessions** — [HGNC:3631](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3631) · Entrez [2224](https://www.ncbi.nlm.nih.gov/gene/2224) · UniProt [P14324](https://www.uniprot.org/uniprotkb/P14324) · Ensembl [ENSG00000160752](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160752)

## Data

Gene col 8376: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8376); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8376, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8376]; `tensor/DDL_lfc|DDL_z.npy` [8376]; `embed/gene_vectors.npy` [8376]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8376 or target_col == 8376). Every well: [[FDPS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FDPS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
