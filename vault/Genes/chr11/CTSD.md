---
symbol: "CTSD"
type: "gene"
col: 3958
ensembl_id: "ENSG00000117984"
name: "cathepsin D"
location: "11p15.5"
module: 50
arm: "+"
pooled_cpm: 103.89
n_lines_expressing: 46
n_dd_up: 6
n_dd_down: 7
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# CTSD

*cathepsin D* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.37× (z +16.9, q 0e+00, up in 42 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 1.64× (z +5.3, q 1e-05, up in 30 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (KATO III 5.32×, A498 4.16×, SW480 5.84×, A549 7.09×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 5.07×, A549 6.16×, KATO III 4.30×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.427× (z -13.8, q 2e-40, down in 41 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRN]] (+0.78, fdr 7e-06), [[PSAP]] (+0.78, fdr 7e-06), [[ATF6B]] (+0.71, fdr 7e-06); moves opposite to [[MPHOSPH6]] (-0.58, fdr 7e-06), [[BRIX1]] (-0.57, fdr 1e-05), [[C10orf88]] (-0.57, fdr 3e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[AGT]] → it (grade B ⚠); 5 go from it, the strongest it → [[IFITM10]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3958.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (KATO III 5.32×, A498 4.16×, SW480 5.84×, A549 7.09×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 5.07×, A549 6.16×, KATO III 4.30×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.37×** | +16.9 | 0e+00 | 42/43 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.30×** | +13.2 | 4e-37 | 37/37 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.62×** | +10.2 | 4e-22 | 38/39 (SW 900, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.60×** | +5.4 | 1e-05 | 37/43 (SW1417, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.64×** | +5.3 | 1e-05 | 30/44 (A-427, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +4.2 | 0.003 | 26/44 (H4, LoVo, …) | two highest doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.0 | 0.006 | 5/46 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.31× | +3.1 | 0.15 | 20/44 (HT-29, KATO III, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.63× | +3.0 | 0.16 | 24/44 (SNU-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3958.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.427×** | -13.8 | 2e-40 | 41/44 (HT-29, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.342×** | -12.3 | 3e-32 | 40/44 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.537×** | -6.9 | 1e-09 | 37/44 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.548×** | -6.6 | 4e-09 | 37/45 (SNU-423, C32, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.669×** | -4.6 | 4e-04 | 31/44 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.677×** | -4.5 | 7e-04 | 30/44 (RKO, H4, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.713×** | -3.9 | 0.008 | 29/44 (COLO 205, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3958. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 130 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +13.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -18.9) |
| [[C32 (line)]] | wt | 217 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 73.7 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -13.6) |
| [[H4 (line)]] | wt | 127 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -19.1) |
| [[HOP62 (line)]] | alt | 72.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.192× (z -13.9) |
| [[HS-578T (line)]] | alt | 101 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -10.6) |
| [[HT-29 (line)]] | alt | 110 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -21.3) |
| [[KATO III (line)]] | alt | 71.3 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.32× (z +14.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.213× (z -13.4) |
| [[LoVo (line)]] | wt | 32.2 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 7.53× (z +13.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -12.5) |
| [[LS 180 (line)]] | wt | 66.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 26.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 8.78× (z +13.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.127× (z -12.4) |
| [[PANC-1 (line)]] | alt | 276 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +13.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -15.0) |
| [[SW48 (line)]] | wt | 54.1 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 7.55× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.175× (z -10.8) |
| [[SW480 (line)]] | alt | 35.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.84× (z +14.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -10.4) |
| [[A498 (line)]] | wt | 306 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +14.4) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 36.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.09× (z +14.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 160 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -16.3) |
| [[NCI-H460 (line)]] | wt | 70.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +13.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.363× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 83.4 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -16.3) |
| [[SW1417 (line)]] | alt | 137 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -15.2) |
| [[A-172 (line)]] | wt | 133 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +11.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 39.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.67× (z +13.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -8.5) |
| [[AN3 CA (line)]] | alt | 58.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.93× (z +9.4) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 39.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -14.5) |
| [[CFPAC-1 (line)]] | alt | 96.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.246× (z -12.2) |
| [[COLO 205 (line)]] | alt | 125 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0626× (z -19.2) |
| [[HCT15 (line)]] | alt | 36.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.19× (z +11.1) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 83.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -14.9) |
| [[Hs 766T (line)]] | wt | 99.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.96× (z +11.0) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 79.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +8.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 287 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 65.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.32× (z +11.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 30.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +11.0) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 103 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -13.3) |
| [[CHP-212 (line)]] | wt | 54.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0602× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 42.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +12.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 46.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +10.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 30.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.221× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 161 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.316× (z -9.2) |
| [[SNU-1 (line)]] | wt | 30.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.27× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 289 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.190× (z -12.9) |
| [[SW 1271 (line)]] | alt | 48.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 21.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 23.6 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 25.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 94.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 178 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3958), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRN]] | +0.78 | +0.80 / +0.72 | both halves | 7e-06 | STRING 866 |
| [[PSAP]] | +0.78 | +0.81 / +0.67 | both halves | 7e-06 | STRING 799 |
| [[ATF6B]] | +0.71 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[ASAH1]] | +0.69 | +0.71 / +0.58 | both halves | 7e-06 | STRING 576 |
| [[GNPTG]] | +0.68 | +0.71 / +0.61 | both halves | 7e-06 | STRING 660 |
| [[PLBD2]] | +0.66 | +0.76 / +0.50 | both halves | 1e-05 |  |
| [[CTSA]] | +0.65 | +0.70 / +0.56 | both halves | 1e-05 | same gene group; pathway: Affinity selection of immunoglobulins; STRING 824 |
| [[DNASE2]] | +0.65 | +0.74 / +0.58 | both halves | 7e-06 | STRING 414 |
| [[SCPEP1]] | +0.63 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[GLB1]] | +0.63 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[LAPTM4A]] | +0.62 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[ATP6AP1]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 | pathway: Insulin receptor recycling |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPHOSPH6]] | -0.58 | -0.61 / -0.59 | both halves | 7e-06 | pathway: Affinity selection of immunoglobulins |
| [[BRIX1]] | -0.57 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[C10orf88]] | -0.57 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[TMA16]] | -0.56 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[FBXO45]] | -0.55 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[ZNF697]] | -0.55 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[CCDC137]] | -0.55 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[LINC00973]] | -0.55 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[MRPS17]] | -0.53 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[CAAP1]] | -0.53 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[MIS18A]] | -0.53 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[KIFBP]] | -0.53 | -0.51 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGT]] | B | AGT activity raises CTSD's level | lines that do not express AGT (33) vs lines expressing it (17) | 1.97× lower at baseline in the lines without AGT | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMBP, RIT2, SOX11 |
| [[GPX3]] | B | GPX3 activity raises CTSD's level | lines that do not express GPX3 (26) vs lines expressing it (24) | 1.77× lower at baseline in the lines without GPX3 | 0.024 | ⚠ within organs, on part of the lines; also absent: LINC02057, KYNU, C3 |
| [[PSMB5]] | B | PSMB5 activity lowers CTSD's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MMP2]] | B | MMP2 activity raises CTSD's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 1.80× lower at baseline in the lines without MMP2 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L |
| [[IFITM10]] | C | IFITM10 activity raises CTSD's level | lines that do not express IFITM10 (4) vs lines expressing it (46) | 3.11× lower at baseline in the lines without IFITM10 | 0.010 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CTSD, FLVCR2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFITM10]] | C | CTSD activity raises IFITM10's level | lines that do not express CTSD (4) vs lines expressing it (46) | 2.61× lower at baseline in the lines without CTSD | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFITM10, SQOR, ST6GALNAC2; maybe low, not absent; co-absent with the target; its own permutation p |
| [[DNASE2]] | C | CTSD activity raises DNASE2's level | lines that do not express CTSD (4) vs lines expressing it (46) | 2.06× lower at baseline in the lines without CTSD | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFITM10, SQOR, ST6GALNAC2; maybe low, not absent; its own permutation p |
| [[PSAP]] | C | CTSD activity raises PSAP's level | lines that do not express CTSD (4) vs lines expressing it (46) | 1.96× lower at baseline in the lines without CTSD | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFITM10, SQOR, ST6GALNAC2; maybe low, not absent; its own permutation p |
| [[KIFBP]] | C | CTSD activity raises KIFBP's level | lines that do not express CTSD (4) vs lines expressing it (46) | 1.29× lower at baseline in the lines without CTSD | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFITM10, SQOR, ST6GALNAC2; maybe low, not absent |
| [[ARF6]] | C | CTSD activity raises ARF6's level | lines that do not express CTSD (4) vs lines expressing it (46) | 1.60× lower at baseline in the lines without CTSD | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFITM10, SQOR, ST6GALNAC2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.595). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.7, -19.4); signed map (-50.6, -8.8). **Vector** length 112, 34.9% of its response variance represented; |z| ≥ 3 in 830 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glycosphingolipid catabolism* (reactome, mean cos +0.53 to 5); *Glycosphingolipid metabolism* (reactome, mean cos +0.53 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.7 | +4.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +1.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.4 | +5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +0.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.8 | +2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.7 | +2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.5 | +2.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.3 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.3 | -12.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.4 | -3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.4 | -13.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.4 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.2 | -6.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.1 | -2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -6.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.7 | -2.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.6 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | cathepsin D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:1,752,752-1,764,573 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CLN10; previously CPSD |
| Gene groups (HGNC) | Cathepsins; Peptidase family A1 |
| Hallmark sets | COMPLEMENT, P53_PATHWAY |
| Reactome | 18 pathways, smallest: Metabolism of Angiotensinogen to Angiotensins; Insulin receptor recycling; Collagen degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P07339](https://www.uniprot.org/uniprotkb/P07339) (Cathepsin D):

> Acid protease active in intracellular protein breakdown. Plays a role in APP processing following cleavage and activation by ADAM30 which leads to APP degradation. Involved in the pathogenesis of several diseases such as breast cancer and possibly Alzheimer disease.

**Summary**, from NCBI Gene [1509](https://www.ncbi.nlm.nih.gov/gene/1509):

> This gene encodes a member of the A1 family of peptidases. The encoded preproprotein is proteolytically processed to generate multiple protein products. These products include the cathepsin D light and heavy chains, which heterodimerize to form the mature enzyme. This enzyme exhibits pepsin-like activity and plays a role in protein turnover and in the proteolytic activation of hormones and growth factors. Mutations in this gene play a causal role in neuronal ceroid lipofuscinosis-10 and may be …

**Accessions** — [HGNC:2529](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2529) · Entrez [1509](https://www.ncbi.nlm.nih.gov/gene/1509) · UniProt [P07339](https://www.uniprot.org/uniprotkb/P07339) · Ensembl [ENSG00000117984](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117984)

## Data

Gene col 3958: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3958); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3958, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3958]; `tensor/DDL_lfc|DDL_z.npy` [3958]; `embed/gene_vectors.npy` [3958]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3958 or target_col == 3958). Every well: [[CTSD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTSD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
