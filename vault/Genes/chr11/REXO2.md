---
symbol: "REXO2"
type: "gene"
col: 1141
ensembl_id: "ENSG00000076043"
name: "RNA exonuclease 2"
location: "11q23.2"
module: 169
arm: "+"
pooled_cpm: 42.05
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/169"]
generated_by: "tahoemap"
---

# REXO2

*RNA exonuclease 2* — 11q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.51× (z +10.1, q 5e-21, up in 40 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.58× (z +5.0, q 7e-05, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.610× (z -7.6, q 2e-11, down in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (KATO III 0.325×, Panc 03.27 0.271×, MIA PaCa-2 0.263×, HT-29 0.365×, …); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.0652×); [[Docetaxel (drug)]] 0.05 µM in 1 line (H4 0.213×; ⚠ transcription drop; cell-cycle shift, explains ~43% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.220×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFAF7]] (+0.61, fdr 1e-05), [[PPHLN1]] (+0.61, fdr 1e-05), [[ISCU]] (+0.59, fdr 4e-05); moves opposite to [[ZNF678]] (-0.60, fdr 1e-05), [[ZKSCAN2]] (-0.58, fdr 2e-05), [[SFR1]] (-0.55, fdr 2e-05).
> It is in [[Module 169]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1141.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.51×** | +10.1 | 5e-21 | 40/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +8.9 | 1e-16 | 34/39 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +7.2 | 1e-10 | 38/43 (AsPC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +5.3 | 2e-05 | 33/47 (NCI-H1792, HOP62, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.58×** | +5.0 | 7e-05 | 40/48 (SW480, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +4.6 | 4e-04 | 35/48 (COLO 205, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.5 | 6e-04 | 28/48 (LS 180, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +4.1 | 0.002 | 30/48 (C32, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.6 | 0.024 | 28/47 (C-33 A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.38×** | +3.5 | 0.024 | 25/47 (NCI-H460, NCI-H1573, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.042 | 27/48 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.047 | 23/47 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +3.2 | 0.055 | 25/48 (COLO 205, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.33×** | +3.1 | 0.076 | 22/46 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.085 | 23/48 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.096 | 20/48 (BT-474, J82, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1141.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (KATO III 0.325×, Panc 03.27 0.271×, MIA PaCa-2 0.263×, HT-29 0.365×, …); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.0652×); [[Docetaxel (drug)]] 0.05 µM in 1 line (H4 0.213×; ⚠ transcription drop; cell-cycle shift, explains ~43% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.220×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.610×** | -7.6 | 2e-11 | 35/48 (KATO III, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.691×** | -4.0 | 0.017 | 28/48 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | 0.724× | -3.4 | 0.14 | 22/48 (H4, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Folic acid (drug)]] 5 µM |  | 0.818× | -3.1 | 0.31 | 17/48 (A498, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1141. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 26.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.06× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 37.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.92× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -8.7) |
| [[HS-578T (line)]] | alt | 61.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +10.0) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 53.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 26.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -11.8) |
| [[NCI-H1792 (line)]] | alt | 35.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 38.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +8.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 54.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.00× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -13.5) |
| [[PANC-1 (line)]] | alt | 51.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +11.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 46.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -10.3) |
| [[A-172 (line)]] | wt | 32.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +10.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 59.4 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0652× (z -12.3) |
| [[AsPC-1 (line)]] | alt | 24.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.18× (z +9.6) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 25.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +9.8) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 37.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +8.8) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 59.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.213× (z -10.1) ⚠ transcription drop; cell-cycle shift, explains ~43% of this change |
| [[HOP62 (line)]] | alt | 25.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 63.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -10.7) |
| [[J82 (line)]] | alt | 42.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -8.9) |
| [[KATO III (line)]] | alt | 70.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -13.8) |
| [[LOX-IMVI (line)]] | wt | 53.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 34.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 25.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 34.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 39.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 46.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 71.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1141), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFAF7]] | +0.61 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[PPHLN1]] | +0.61 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[ISCU]] | +0.59 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[PCMTD1]] | +0.59 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[RNF13]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[SEC24B]] | +0.57 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[NENF]] | +0.56 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[MARCHF5]] | +0.56 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[KIZ-AS1]] ⚠ | +0.55 | +0.42 / +0.58 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LAPTM4A]] | +0.55 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[NADSYN1]] | +0.55 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[HINT1]] | +0.54 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[PFDN5]] | +0.54 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF678]] | -0.60 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[ZKSCAN2]] | -0.58 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[SFR1]] | -0.55 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[ARF6]] | -0.55 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[THOP1]] | -0.55 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[ZNF724]] | -0.54 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[HASPIN]] | -0.54 | -0.40 / -0.64 | both halves | 5e-05 |  |
| [[CHAMP1]] | -0.53 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[DNMT1]] | -0.53 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[MDC1]] | -0.53 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[PHLDA1]] | -0.53 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ZNF799]] | -0.52 | -0.42 / -0.54 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 169]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.645). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.4, -11.6); signed map (-35.9, -8.1). **Vector** length 85.3, 23.6% of its response variance represented; |z| ≥ 3 in 713 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +4.1 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.8 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.1 | -7.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.0 | -3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -0.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | +0.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | +0.1 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | RNA exonuclease 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.2 — chr11:114,439,435-114,450,279 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP566E144, SFN, CGI-114 |
| Gene groups (HGNC) | Exonucleases |
| Reactome | 2 pathways, smallest: Mitochondrial RNA degradation; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3B8](https://www.uniprot.org/uniprotkb/Q9Y3B8) (Oligoribonuclease, mitochondrial):

> 3'-to-5'exoribonuclease that preferentially degrades DNA and RNA oligonucleotides composed of only two nucleotides. Binds and degrades longer oligonucleotides with a lower affinity. Plays dual roles in mitochondria, scavenging nanoRNAs (small RNA oligonucleotides of <5 nucleotides) that are produced by the degradosome and clearing short RNAs that are generated by RNA processing. Essential for correct initiation of mitochondrial transcription, degrading mitochondrial RNA dinucleotides to prevent …

**Summary**, from NCBI Gene [25996](https://www.ncbi.nlm.nih.gov/gene/25996):

> This gene encodes a 3'-to-5' exonuclease specific for small (primarily 5 nucleotides or less in length) single-stranded RNA and DNA oligomers. This protein may have a role in DNA repair, replication, and recombination, and in RNA processing and degradation. It may also be involved in resistance of human cells to UV-C-induced cell death through its role in the DNA repair process. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:17851](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17851) · Entrez [25996](https://www.ncbi.nlm.nih.gov/gene/25996) · UniProt [Q9Y3B8](https://www.uniprot.org/uniprotkb/Q9Y3B8) · Ensembl [ENSG00000076043](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076043)

## Data

Gene col 1141: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1141); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1141, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1141]; `tensor/DDL_lfc|DDL_z.npy` [1141]; `embed/gene_vectors.npy` [1141]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1141 or target_col == 1141). Every well: [[REXO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/REXO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
