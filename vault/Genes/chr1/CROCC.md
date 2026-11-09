---
symbol: "CROCC"
type: "gene"
col: 662
ensembl_id: "ENSG00000058453"
name: "ciliary rootlet coiled-coil, rootletin"
location: "1p36.13"
module: 54
arm: "-"
pooled_cpm: 16.32
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 3
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# CROCC

*ciliary rootlet coiled-coil, rootletin* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.28× (z +29.3, q 0e+00, up in 41 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.20× (z +28.9, q 0e+00, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.780× (z -4.4, q 0.006, down in 19 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.631× (z -4.2, q 0.006, down in 15 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (J82 0.0390×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.164×; ⚠ toxic; transcription drop); [[Silodosin (drug)]] 5 µM in 1 line (C32 0.167×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-423 0.180×).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC200]] (+0.72, fdr 1e-05), [[RYR2]] (+0.72, fdr 1e-05), [[CYB5D2]] (+0.70, fdr 7e-06); moves opposite to [[POP7]] (-0.73, fdr 2e-05), [[SDHAF1]] (-0.67, fdr 2e-05), [[ISCA2]] (-0.65, fdr 1e-03, ⚠ one half only (not replicated)), [[PUSL1]] (-0.65, fdr 5e-04).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ATP2C2-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 662.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.28×** | +29.3 | 0e+00 | 41/41 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.20×** | +28.9 | 0e+00 | 44/46 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.44×** | +28.7 | 0e+00 | 30/31 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.79×** | +25.5 | 0e+00 | 43/47 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.24×** | +19.1 | 0e+00 | 29/35 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +11.9 | 1e-30 | 32/47 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +8.6 | 5e-16 | 26/46 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +8.5 | 1e-15 | 34/48 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +8.0 | 1e-13 | 26/48 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +7.9 | 2e-13 | 25/48 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +7.1 | 6e-11 | 21/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +6.9 | 3e-10 | 25/48 (A-427, A-172, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +6.5 | 5e-09 | 26/48 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +6.2 | 2e-08 | 22/47 (HepG2/C3A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +6.0 | 1e-07 | 21/47 (HS-578T, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.63×** | +4.5 | 3e-04 | 13/46 (HOP62, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.005 | 5/48 (KATO III, A-427, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.006 | 8/47 (CFPAC-1, A-427, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 662.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (J82 0.0390×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.164×; ⚠ toxic; transcription drop); [[Silodosin (drug)]] 5 µM in 1 line (C32 0.167×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-423 0.180×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.780×** | -4.4 | 0.006 | 19/47 (J82, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.631×** | -4.2 | 0.006 | 15/48 (NCI-H23, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **0.787×** | -4.1 | 0.009 | 15/44 (NCI-H23, J82, …) | top dose only | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.826× | -3.4 | 0.10 | 5/48 (SW1417, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 662. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 16.4 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 54.4× (z +23.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.87× (z +13.4) | — |
| [[LS 180 (line)]] | wt | 14.9 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.25× (z +14.8) | — |
| [[NCI-H460 (line)]] | wt | 8.95 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 41.5× (z +24.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 6.86× (z +18.3) | — |
| [[C32 (line)]] | wt | 15.6 | 4 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 12.7× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.23× (z +11.2) | [[Silodosin (drug)]] 5 µM 0.167× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 20.9 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.70× (z +13.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +12.1) | — |
| [[HOP62 (line)]] | alt | 26.1 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +16.7) | — |
| [[HT-29 (line)]] | alt | 15.1 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.16× (z +12.8) | — |
| [[KATO III (line)]] | alt | 12.9 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.5× (z +14.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.71× (z +12.8) | — |
| [[LoVo (line)]] | wt | 17.7 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.32× (z +17.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +15.6) | — |
| [[CFPAC-1 (line)]] | alt | 17.5 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.57× (z +15.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 22.2 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.24× (z +17.5) | — |
| [[NCI-H1573 (line)]] | alt | 15.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +15.6) | — |
| [[NCI-H1792 (line)]] | alt | 16.5 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +15.1) | — |
| [[RPMI-7951 (line)]] | alt | 15.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.6× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.05× (z +9.8) | — |
| [[SW480 (line)]] | alt | 15.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.87× (z +16.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +13.4) | — |
| [[A549 (line)]] | wt | 11.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.99× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 10.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.63× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.06× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 20.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +14.2) | — |
| [[PANC-1 (line)]] | alt | 14.4 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +13.5) | — |
| [[SK-MEL-2 (line)]] | alt | 30.6 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.75× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 13.7 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +10.3) | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.180× (z -8.9) |
| [[SW 900 (line)]] | alt | 15.4 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.77× (z +11.4) | — |
| [[SW48 (line)]] | wt | 35.6 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +10.0) | — |
| [[A-427 (line)]] | wt | 20.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.90× (z +9.3) | — |
| [[A498 (line)]] | wt | 7.89 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +12.7) | — |
| [[COLO 205 (line)]] | alt | 11.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 37.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 25.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -9.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 12.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.38× (z +9.8) | — |
| [[J82 (line)]] | alt | 15.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +10.1) | [[Digitoxin (drug)]] 5 µM 0.0390× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 48.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +17.0) | — |
| [[Panc 03.27 (line)]] | alt | 10.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.04× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.73× (z +9.4) | — |
| [[A-172 (line)]] | wt | 7.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +9.5) | — |
| [[AsPC-1 (line)]] | alt | 10.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +8.8) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 25.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.63× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 8.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +10.6) | — |
| [[RKO (line)]] | wt | 23.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +10.7) | — |
| [[SHP-77 (line)]] | alt | 11.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.2× (z +11.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 662), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC200]] | +0.72 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[RYR2]] | +0.72 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[CYB5D2]] | +0.70 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[LHFPL3]] | +0.68 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[PIEZO1]] | +0.67 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[MSTO1]] | +0.66 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[MUTYH]] | +0.64 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[LYRM1]] | +0.63 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[WDR74]] | +0.63 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[ATN1]] | +0.62 | +0.38 / +0.41 | both halves | 7e-05 |  |
| [[AP4S1]] | +0.62 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[AP1G2-AS1]] | +0.62 | +0.49 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 11 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POP7]] | -0.73 | -0.46 / -0.67 | both halves | 2e-05 |  |
| [[SDHAF1]] | -0.67 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[ISCA2]] | -0.65 | -0.18 / -0.58 | ⚠ one half (not replicated) | 1e-03 |  |
| [[PUSL1]] | -0.65 | -0.23 / -0.58 | both halves | 5e-04 |  |
| [[MRPL17]] | -0.64 | -0.37 / -0.57 | both halves | 8e-05 |  |
| [[PET117]] | -0.63 | -0.19 / -0.60 | ⚠ one half (not replicated) | 9e-04 |  |
| [[WRAP73]] | -0.63 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[MRPS34]] | -0.63 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[LSM2]] | -0.62 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[ZDHHC12]] | -0.62 | -0.39 / -0.60 | both halves | 6e-05 |  |
| [[MRPL55]] | -0.62 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[PDCD10]] | -0.61 | -0.66 / -0.40 | both halves | 5e-05 |  |
| [[MRPL14]] | -0.61 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[ANAPC11]] | -0.60 | -0.55 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CROCC's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP2C2-AS1]] | C | CROCC's natural level strengthens ATP2C2-AS1's drug response | CROCC's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.10; direction not clear | 0.066 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.730). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-0.2, 23.0); signed map (33.1, -19.5). **Vector** length 86.1, 17.6% of its response variance represented; |z| ≥ 3 in 1,022 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.2 | +29.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.1 | +28.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.2 | +19.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.0 | +25.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +28.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +7.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +1.5 | +1.3 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +1.4 | +0.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | +1.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.0 | +6.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.4 | +8.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.3 | +3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | +1.5 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Thymol (drug)]] 5 µM |  | -1.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ciliary rootlet coiled-coil, rootletin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:16,740,273-16,972,964 (+) |
| Ensembl biotype | protein_coding |
| Also known as | rootletin, ROLT, CROCC1 |
| Hallmark sets | APICAL_SURFACE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TZA2](https://www.uniprot.org/uniprotkb/Q5TZA2) (Rootletin):

> Major structural component of the ciliary rootlet, a cytoskeletal-like structure in ciliated cells which originates from the basal body at the proximal end of a cilium and extends proximally toward the cell nucleus (By similarity). Furthermore, is required for the correct positioning of the cilium basal body relative to the cell nucleus, to allow for ciliogenesis. Contributes to centrosome cohesion before mitosis.

**Summary**, from NCBI Gene [9696](https://www.ncbi.nlm.nih.gov/gene/9696):

> Predicted to enable kinesin binding activity and structural molecule activity. Involved in several processes, including centriole-centriole cohesion; positive regulation of cilium assembly; and positive regulation of protein localization to cilium. Located in centriole; centrosome; and ciliary basal body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21299](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21299) · Entrez [9696](https://www.ncbi.nlm.nih.gov/gene/9696) · UniProt [Q5TZA2](https://www.uniprot.org/uniprotkb/Q5TZA2) · Ensembl [ENSG00000058453](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000058453)

## Data

Gene col 662: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 662); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 662, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 662]; `tensor/DDL_lfc|DDL_z.npy` [662]; `embed/gene_vectors.npy` [662]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 662 or target_col == 662). Every well: [[CROCC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CROCC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
