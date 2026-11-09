---
symbol: "IKBKB"
type: "gene"
col: 2449
ensembl_id: "ENSG00000104365"
name: "inhibitor of nuclear factor kappa B kinase subunit beta"
location: "8p11.21"
module: 14
arm: "+"
pooled_cpm: 56.38
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 17
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# IKBKB

*inhibitor of nuclear factor kappa B kinase subunit beta* — 8p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.25× (z +5.7, q 5e-06, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.391× (z -17.0, q 0e+00, down in 43 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.599× (z -13.1, q 7e-37, down in 43 of 49 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSF3]] (+0.57, fdr 3e-05), [[WDR75]] (+0.55, fdr 6e-05), [[SMG9]] (+0.53, fdr 5e-05); moves opposite to [[SAR1A]] (-0.55, fdr 9e-05), [[BTAF1]] (-0.53, fdr 1e-04), [[PDIA3]] (-0.52, fdr 1e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2449.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +5.7 | 5e-06 | 25/48 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +5.4 | 2e-05 | 26/48 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.3 | 0.004 | 0/49 | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.24×** | +3.7 | 0.036 | 22/47 (RPMI-7951, HOP62, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.039 | 16/49 (AsPC-1, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 12 with an alert ⚠; shown: the 15 strongest. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2449.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.391×** | -17.0 | 0e+00 | 43/48 (NCI-H23, CHP-212, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.439×** | -13.7 | 2e-40 | 38/45 (SW48, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.599×** | -13.1 | 7e-37 | 43/49 (AsPC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.483×** | -12.6 | 2e-34 | 33/42 (A549, A-427, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.573×** | -10.1 | 1e-21 | 40/48 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.613×** | -8.8 | 9e-17 | 39/48 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.636×** | -8.2 | 2e-14 | 34/48 (SK-MEL-2, J82, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.642×** | -8.0 | 8e-14 | 32/48 (SK-MEL-2, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.767×** | -4.6 | 3e-04 | 25/47 (HOP62, A-172, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.784×** | -4.4 | 6e-04 | 25/48 (Panc 03.27, SW480, …) | two highest doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.631×** | -4.4 | 7e-04 | 28/43 (NCI-H1792, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **0.816×** | -3.7 | 0.011 | 21/46 (NCI-H661, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.813×** | -3.5 | 0.017 | 21/48 (CFPAC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.823×** | -3.5 | 0.017 | 21/48 (HEC-1-A, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.823×** | -3.4 | 0.027 | 22/46 (RKO, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2449. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 62.6 | 2 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.364× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 78.7 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.190× (z -15.6) |
| [[J82 (line)]] | alt | 93.5 | 1 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -9.0) |
| [[SW480 (line)]] | alt | 57.4 | 0 | 7 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.253× (z -17.9) |
| [[MIA PaCa-2 (line)]] | alt | 63.3 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.262× (z -13.0) ⚠ toxic; cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.374× (z -9.9) |
| [[A-172 (line)]] | wt | 91.3 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +14.6) | [[Auranofin (drug)]] 5 µM 0.288× (z -13.1) |
| [[A498 (line)]] | wt | 50.1 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -8.5) |
| [[HS-578T (line)]] | alt | 65.2 | 3 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 4.94× (z +16.6) | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A549 (line)]] | wt | 75.2 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.153× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SNU-423 (line)]] | alt | 32.4 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +14.6) | [[Auranofin (drug)]] 5 µM 0.300× (z -10.1) |
| [[SW48 (line)]] | wt | 74.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0901× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.309× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 49.8 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -11.8) |
| [[CHP-212 (line)]] | wt | 76.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0594× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H2030 (line)]] | alt | 42.9 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.365× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 49.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.352× (z -11.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 72.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -13.5) |
| [[SHP-77 (line)]] | alt | 80.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -9.8) |
| [[A-427 (line)]] | wt | 57.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[AsPC-1 (line)]] | alt | 63.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -15.7) |
| [[COLO 205 (line)]] | alt | 65.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -10.1) |
| [[H4 (line)]] | wt | 52.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 58.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -9.4) |
| [[Hs 766T (line)]] | wt | 98.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[hTERT-HPNE (line)]] | wt | 36.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +11.6) | — |
| [[KATO III (line)]] | alt | 66.8 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.380× (z -9.3) |
| [[LoVo (line)]] | wt | 61.6 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.324× (z -12.7) |
| [[LOX-IMVI (line)]] | wt | 58.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 54.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[PANC-1 (line)]] | alt | 24.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +19.9) | — |
| [[RKO (line)]] | wt | 90.4 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.193× (z -15.5) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[RPMI-7951 (line)]] | alt | 52.8 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.11× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.189× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[AN3 CA (line)]] | alt | 67.8 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.173× (z -9.4) |
| [[BT-474 (line)]] | alt | 57.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.307× (z -10.2) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HCT15 (line)]] | alt | 53.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[LS 180 (line)]] | wt | 64.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H1792 (line)]] | alt | 57.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 43.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.406× (z -8.5) |
| [[SNU-1 (line)]] | wt | 65.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -10.6) |
| [[SW1417 (line)]] | alt | 52.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -10.7) |
| [[C-33 A (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2449), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSF3]] | +0.57 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[WDR75]] | +0.55 | +0.38 / +0.54 | both halves | 6e-05 |  |
| [[SMG9]] | +0.53 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[ZC3H7B]] | +0.53 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[ANO9]] | +0.52 | +0.52 / +0.49 | both halves | 1e-05 | pathway: SARS-CoV-2 Infection |
| [[EBI3]] | +0.51 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[STAT5A]] | +0.51 | +0.38 / +0.47 | both halves | 7e-05 |  |
| [[LIME1]] | +0.51 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[UBE2J2]] | +0.50 | +0.38 / +0.49 | both halves | 7e-05 |  |
| [[TIMM9]] | +0.50 | +0.33 / +0.51 | both halves | 1e-04 |  |
| [[SPG11]] | +0.50 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[TRAF4]] | +0.49 | +0.39 / +0.48 | both halves | 6e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAR1A]] | -0.55 | -0.37 / -0.57 | both halves | 9e-05 |  |
| [[BTAF1]] | -0.53 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[PDIA3]] | -0.52 | -0.34 / -0.58 | both halves | 1e-04 | pathway: Antigen processing-Cross presentation |
| [[SKP1]] | -0.51 | -0.40 / -0.50 | both halves | 5e-05 | pathway: Activation of NF-kappaB in B cells; STRING 672 |
| [[SERPINH1]] | -0.51 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[SNX3]] | -0.50 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[PPME1]] | -0.50 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[TMED7]] | -0.50 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[ALKBH5]] | -0.50 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[TMEM167A]] | -0.50 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[NUCB1]] | -0.49 | -0.29 / -0.54 | both halves | 2e-04 |  |
| [[NID2]] | -0.49 | -0.39 / -0.46 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises IKBKB's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.394). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.1, -24.2); signed map (-0.2, -8.7). **Vector** length 84.7, 19.7% of its response variance represented; |z| ≥ 3 in 982 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.6 | +5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +5.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | -1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +0.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | +3.2 | -3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | -0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.0 | +0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +0.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +0.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.3 | -10.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.8 | -3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.7 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -0.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.6 | +0.3 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.3 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | inhibitor of nuclear factor kappa B kinase subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.21 — chr8:42,271,302-42,332,460 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IKK2, NFKBIKB, IKK-beta, IKKB |
| Gene groups (HGNC) | I kappa B kinase family; IKK complex |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 78 pathways, smallest: IKBKB deficiency causes SCID; IKBKG deficiency causes anhidrotic ectodermal dysplasia with immunodeficiency (EDA-ID) (via TLR); SLC15A4:TASL-dependent IRF5 activation |
| Matched by | ensembl_id |

**Function**, from UniProt [O14920](https://www.uniprot.org/uniprotkb/O14920) (Inhibitor of nuclear factor kappa-B kinase subunit beta):

> Serine kinase that plays an essential role in the NF-kappa-B signaling pathway which is activated by multiple stimuli such as inflammatory cytokines, bacterial or viral products, DNA damages or other cellular stresses. Acts as a part of the canonical IKK complex in the conventional pathway of NF-kappa-B activation. Phosphorylates inhibitors of NF-kappa-B on 2 critical serine residues. These modifications allow polyubiquitination of the inhibitors and subsequent degradation by the proteasome. In …

**Summary**, from NCBI Gene [3551](https://www.ncbi.nlm.nih.gov/gene/3551):

> The protein encoded by this gene phosphorylates the inhibitor in the inhibitor/NF-kappa-B complex, causing dissociation of the inhibitor and activation of NF-kappa-B. The encoded protein itself is found in a complex of proteins. Several transcript variants, some protein-coding and some not, have been found for this gene. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:5960](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5960) · Entrez [3551](https://www.ncbi.nlm.nih.gov/gene/3551) · UniProt [O14920](https://www.uniprot.org/uniprotkb/O14920) · Ensembl [ENSG00000104365](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104365)

## Data

Gene col 2449: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2449); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2449, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2449]; `tensor/DDL_lfc|DDL_z.npy` [2449]; `embed/gene_vectors.npy` [2449]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2449 or target_col == 2449). Every well: [[IKBKB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IKBKB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
