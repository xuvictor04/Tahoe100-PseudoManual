---
symbol: "BAHCC1"
type: "gene"
col: 15478
ensembl_id: "ENSG00000266074"
name: "BAH domain and coiled-coil containing 1"
location: "17q25.3"
module: 14
arm: "+"
pooled_cpm: 17.43
n_lines_expressing: 48
n_dd_up: 9
n_dd_down: 23
n_dd_up_clean: 6
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# BAHCC1

*BAH domain and coiled-coil containing 1* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.58× (z +19.5, q 0e+00, up in 30 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.528× (z -8.7, q 8e-16, down in 34 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GSE1]] (+0.72, fdr 7e-06), [[BCL3]] (+0.66, fdr 7e-06), [[PHF19]] (+0.65, fdr 9e-06); moves opposite to [[TM2D1]] (-0.59, fdr 8e-06), [[GPR89A]] (-0.58, fdr 1e-05), [[NDUFAF7]] (-0.58, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15478.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.58×** | +19.5 | 0e+00 | 30/45 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.66×** | +18.1 | 0e+00 | 30/45 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.13×** | +11.0 | 7e-26 | 29/44 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +9.1 | 1e-17 | 28/45 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +6.6 | 4e-09 | 22/39 (PANC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +6.1 | 8e-08 | 20/34 (LoVo, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +6.0 | 2e-07 | 22/46 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +4.0 | 0.005 | 11/28 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Demeclocycline (drug)]] 5 µM |  | 1.18× | +3.5 | 0.032 | 7/45 (Hs 766T, PANC-1, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.054 | 13/45 (NCI-H460, HS-578T, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~10% of this change | 1.23× | +3.0 | 0.13 | 12/42 (COLO 205, LS 180, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15478.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.528×** | -8.7 | 8e-16 | 34/45 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.548×** | -8.7 | 8e-16 | 32/45 (A-427, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.553×** | -8.6 | 2e-15 | 31/45 (LS 180, A-427, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.700×** | -7.3 | 4e-11 | 26/45 (LoVo, HT-29, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.709×** | -7.0 | 2e-10 | 28/46 (HT-29, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.651×** | -6.2 | 5e-08 | 26/45 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.677×** | -5.6 | 1e-06 | 24/44 (LoVo, C32, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.509×** | -5.1 | 2e-05 | 18/45 (PANC-1, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.551×** | -4.5 | 4e-04 | 18/38 (A-427, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.567×** | -4.3 | 1e-03 | 14/44 (HT-29, LoVo, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.576×** | -4.2 | 0.002 | 17/45 (LoVo, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.756×** | -4.0 | 0.002 | 14/46 (PANC-1, LoVo, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.757×** | -3.9 | 0.005 | 18/44 (H4, C32, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.691×** | -3.8 | 0.005 | 15/45 (MIA PaCa-2, PANC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.770×** | -3.8 | 0.006 | 16/44 (PANC-1, A-172, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.613×** | -3.7 | 0.008 | 7/43 (HT-29, PANC-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.794×** | -3.3 | 0.028 | 17/45 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Retinoic acid (drug)]] 5 µM |  | 0.852× | -3.3 | 0.035 | 10/46 (SW 900, SHP-77, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.799×** | -3.2 | 0.035 | 14/46 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15478. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 44.5 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +21.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.350× (z -9.9) ⚠ unreliable plate only · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.350× (z -9.4) |
| [[A-427 (line)]] | wt | 29.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -11.9) |
| [[HS-578T (line)]] | alt | 22.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +23.4) | — |
| [[NCI-H460 (line)]] | wt | 11.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.21× (z +19.7) | — |
| [[A-172 (line)]] | wt | 18.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +21.5) | — |
| [[A498 (line)]] | wt | 12.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.30× (z +17.7) | — |
| [[A549 (line)]] | wt | 16.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +18.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 13.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +12.6) | — |
| [[SNU-1 (line)]] | wt | 28.4 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.116× (z -10.5) |
| [[SNU-423 (line)]] | alt | 12.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.9× (z +23.0) | — |
| [[C32 (line)]] | wt | 23.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.142× (z -10.8) |
| [[HOP62 (line)]] | alt | 21.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +19.8) | — |
| [[hTERT-HPNE (line)]] | wt | 31.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 15.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -9.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 19.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +15.4) | — |
| [[BT-474 (line)]] | alt | 6.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.18× (z +10.7) | — |
| [[CFPAC-1 (line)]] | alt | 8.91 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +16.9) | — |
| [[COLO 205 (line)]] | alt | 12.6 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0717× (z -12.2) |
| [[H4 (line)]] | wt | 13.6 | 0 | 1 | — | [[Rapamycin (drug)]] 0.5 µM 0.0705× (z -9.2) |
| [[Hs 766T (line)]] | wt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +12.1) | — |
| [[HT-29 (line)]] | alt | 13.4 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.350× (z -8.7) |
| [[J82 (line)]] | alt | 14.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +15.3) | — |
| [[LOX-IMVI (line)]] | wt | 10.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +12.0) | — |
| [[LS 180 (line)]] | wt | 14.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.232× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 9.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +10.2) | — |
| [[RKO (line)]] | wt | 15.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -9.6) ⚠ cell-cycle shift, explains ~12% of this change |
| [[RPMI-7951 (line)]] | alt | 5.91 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +11.3) | — |
| [[SW 900 (line)]] | alt | 24.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.60× (z +8.9) | — |
| [[SW48 (line)]] | wt | 49.7 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 5.87× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15478), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSE1]] | +0.72 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[BCL3]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[PHF19]] | +0.65 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[NAB1]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[SIX5]] | +0.63 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[SYNPO]] | +0.63 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[HIVEP1]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[STAT5A]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[NFIX]] | +0.60 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[ZNF318]] | +0.60 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[SKIL]] | +0.59 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[PTP4A3]] | +0.59 | +0.50 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TM2D1]] | -0.59 | -0.58 / -0.62 | both halves | 8e-06 |  |
| [[GPR89A]] | -0.58 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[NDUFAF7]] | -0.58 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[RPS5]] | -0.56 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[GPR89B]] | -0.56 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[MED31]] | -0.56 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[PPHLN1]] | -0.56 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[PPIL2]] | -0.55 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[ZNF235]] | -0.55 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[IGBP1]] | -0.55 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[PDCD10]] | -0.55 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[MGST3]] | -0.54 | -0.56 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.584). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.1, 4.7); signed map (44.6, 5.1). **Vector** length 106, 24.7% of its response variance represented; |z| ≥ 3 in 1,051 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.2 | +19.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.0 | +18.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +11.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.2 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +6.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +1.8 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | +1.5 | +1.0 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +1.5 | +1.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -5.6 | -8.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.5 | -7.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.7 | -8.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -8.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.6 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -7.3 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -3.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.5 | -3.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | BAH domain and coiled-coil containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,395,457-81,466,331 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1447, BAHD2 |
| Matched by | ensembl_id |

UniProt [Q9P281](https://www.uniprot.org/uniprotkb/Q9P281) carries no function annotation.

**Summary**, from NCBI Gene [57597](https://www.ncbi.nlm.nih.gov/gene/57597):

> Predicted to enable chromatin binding activity. Predicted to act upstream of or within chromatin organization; locomotory behavior; and neuron differentiation. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29279](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29279) · Entrez [57597](https://www.ncbi.nlm.nih.gov/gene/57597) · UniProt [Q9P281](https://www.uniprot.org/uniprotkb/Q9P281) · Ensembl [ENSG00000266074](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000266074)

## Data

Gene col 15478: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15478); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15478, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15478]; `tensor/DDL_lfc|DDL_z.npy` [15478]; `embed/gene_vectors.npy` [15478]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15478 or target_col == 15478). Every well: [[BAHCC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BAHCC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
