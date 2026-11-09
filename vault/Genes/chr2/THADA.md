---
symbol: "THADA"
type: "gene"
col: 3745
ensembl_id: "ENSG00000115970"
name: "THADA armadillo repeat containing"
location: "2p21"
module: 1
arm: "+"
pooled_cpm: 85.24
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 14
n_dd_up_clean: 22
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# THADA

*THADA armadillo repeat containing* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.11× (z +9.4, q 3e-18, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.472× (z -9.4, q 2e-18, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INO80]] (+0.73, fdr 7e-06), [[COMMD10]] (+0.73, fdr 7e-06), [[WARS2]] (+0.71, fdr 7e-06); moves opposite to [[C20orf96]] (-0.61, fdr 2e-05), [[IFI27L1]] (-0.61, fdr 1e-05), [[GMCL1]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[WARS2-AS1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3745.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.11×** | +9.4 | 3e-18 | 42/47 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +6.6 | 1e-08 | 30/47 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +6.0 | 3e-07 | 32/47 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.59×** | +5.8 | 8e-07 | 37/47 (AsPC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.56×** | +5.4 | 8e-06 | 38/47 (NCI-H23, SW480, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.47×** | +4.9 | 1e-04 | 40/47 (HS-578T, HOP62, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +4.0 | 0.005 | 31/47 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.008 | 30/48 (NCI-H2347, KATO III, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.34×** | +3.7 | 0.013 | 33/47 (NCI-H1573, RKO, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.013 | 26/47 (SHP-77, NCI-H1573, …) | top dose only |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.020 | 29/47 (LOX-IMVI, LS 180, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.21×** | +3.4 | 0.038 | 21/47 (NCI-H2347, AsPC-1, …) | top dose only | low cells (technical?) |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.049 | 27/47 (SK-MEL-2, HOP62, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.055 | 24/47 (AsPC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.065 | 26/47 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.066 | 24/47 (SHP-77, LS 180, …) | inconsistent across doses |  |
| [[Dapagliflozin (drug)]] 0.05 µM |  | **1.27×** | +3.0 | 0.083 | 23/47 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3745.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.472×** | -9.4 | 2e-18 | 39/47 (SW480, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.512×** | -8.4 | 9e-15 | 44/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.549×** | -7.5 | 9e-12 | 39/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.636×** | -5.7 | 2e-06 | 40/47 (COLO 205, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.621×** | -5.5 | 3e-06 | 30/44 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.660×** | -5.2 | 2e-05 | 35/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.662×** | -5.0 | 5e-05 | 33/46 (NCI-H23, KATO III, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.657×** | -4.6 | 3e-04 | 29/48 (NCI-H1573, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.712×** | -4.3 | 0.001 | 33/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.547×** | -4.0 | 0.004 | 20/38 (Panc 03.27, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.574×** | -3.7 | 0.013 | 31/47 (KATO III, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.592×** | -3.4 | 0.025 | 25/48 (SW480, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.752×** | -3.4 | 0.025 | 22/42 (NCI-H23, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.747×** | -3.2 | 0.053 | 27/47 (PANC-1, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3745. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 129 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.273× (z -14.3) |
| [[NCI-H460 (line)]] | wt | 94.9 | 1 | 6 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.47× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.283× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.293× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 238 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0699× (z -27.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.411× (z -9.5) |
| [[KATO III (line)]] | alt | 122 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.331× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 70.2 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.66× (z +9.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.389× (z -8.9) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.411× (z -8.7) |
| [[PANC-1 (line)]] | alt | 116 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.217× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.235× (z -14.8) |
| [[AsPC-1 (line)]] | alt | 31.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.67× (z +11.5) | — |
| [[A-172 (line)]] | wt | 73.4 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.08× (z +9.3) | [[Auranofin (drug)]] 5 µM 0.322× (z -9.3) |
| [[A-427 (line)]] | wt | 149 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.428× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 71.8 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 4.45× (z +10.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.309× (z -8.5) |
| [[HT-29 (line)]] | alt | 76.0 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.323× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 109 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -10.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 131 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.369× (z -9.0) |
| [[SW 900 (line)]] | alt | 45.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.82× (z +10.4) | — |
| [[SW1417 (line)]] | alt | 85.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.301× (z -11.0) |
| [[A498 (line)]] | wt | 58.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.62× (z +11.0) | — |
| [[A549 (line)]] | wt | 112 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.71× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 62.8 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.295× (z -8.6) |
| [[C-33 A (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -8.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 97.8 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.200× (z -13.7) |
| [[HOP62 (line)]] | alt | 83.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.310× (z -10.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 46.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.274× (z -10.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 76.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 79.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 63.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.267× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 72.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.35× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 78.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.8) | — |
| [[NCI-H2347 (line)]] | alt | 30.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +11.1) | — |
| [[Panc 03.27 (line)]] | alt | 65.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.202× (z -11.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 90.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.206× (z -10.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 101 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.325× (z -9.1) |
| [[SHP-77 (line)]] | alt | 99.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.370× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 56.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.288× (z -9.0) |
| [[AN3 CA (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 63.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 78.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 63.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 67.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 61.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3745), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INO80]] | +0.73 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[COMMD10]] | +0.73 | +0.80 / +0.60 | both halves | 7e-06 |  |
| [[WARS2]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[DDX10]] | +0.71 | +0.71 / +0.78 | both halves | 7e-06 |  |
| [[TTC27]] | +0.71 | +0.75 / +0.63 | both halves | 7e-06 | STRING 458 |
| [[PHF14]] | +0.70 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[NOL11]] | +0.70 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[UTP20]] | +0.69 | +0.77 / +0.65 | both halves | 7e-06 | STRING 436 |
| [[GPATCH4]] | +0.67 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[LTV1]] | +0.65 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[NIP7]] | +0.65 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[UTP14A]] | +0.64 | +0.66 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C20orf96]] | -0.61 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[IFI27L1]] | -0.61 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.59 | -0.75 / -0.48 | both halves | 2e-05 |  |
| [[SRP54-AS1]] | -0.59 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[UBTD1]] | -0.58 | -0.70 / -0.40 | both halves | 5e-05 |  |
| [[LAPTM4A]] | -0.58 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[GTF2IP4]] | -0.56 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[CASTOR2]] | -0.56 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[DHRS1]] | -0.56 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[TLE2]] | -0.56 | -0.39 / -0.58 | both halves | 6e-05 |  |
| [[SAP30-DT]] | -0.56 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[TM9SF2]] | -0.55 | -0.64 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WARS2-AS1]] | C | WARS2-AS1 activity raises THADA's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 1.89× lower at baseline in the lines without WARS2-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.716). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-23.1, 13.3); signed map (6.1, -42.7). **Vector** length 119, 42.0% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.50 to 23); *MYC targets v2* (hallmark, mean cos +0.50 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.4 | +6.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +7.6 | +5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.5 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.9 | +2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.8 | +1.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.5 | +4.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.1 | +1.5 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -8.1 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.8 | -9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | -1.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.6 | -0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.9 | -1.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.6 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | +2.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | THADA armadillo repeat containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:43,230,851-43,596,038 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21877, KIAA1767, GITA, ARMC13, Trm732 |
| Gene groups (HGNC) | Armadillo repeat containing |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6YHU6](https://www.uniprot.org/uniprotkb/Q6YHU6) (tRNA):

> Together with methyltransferase FTSJ1, methylates the 2'-O-ribose of nucleotides at position 32 of the anticodon loop of substrate tRNAs.

**Summary**, from NCBI Gene [63892](https://www.ncbi.nlm.nih.gov/gene/63892):

> This gene is the target of 2p21 choromosomal aberrations in benign thyroid adenomas. Single nucleotide polymorphisms (SNPs) in this gene may be associated with type 2 diabetes and polycystic ovary syndrome. The encoded protein is likely involved in the death receptor pathway and apoptosis. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:19217](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19217) · Entrez [63892](https://www.ncbi.nlm.nih.gov/gene/63892) · UniProt [Q6YHU6](https://www.uniprot.org/uniprotkb/Q6YHU6) · Ensembl [ENSG00000115970](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115970)

## Data

Gene col 3745: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3745); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3745, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3745]; `tensor/DDL_lfc|DDL_z.npy` [3745]; `embed/gene_vectors.npy` [3745]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3745 or target_col == 3745). Every well: [[THADA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THADA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
