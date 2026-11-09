---
symbol: "PRKAR1B"
type: "gene"
col: 11986
ensembl_id: "ENSG00000188191"
name: "protein kinase cAMP-dependent type I regulatory subunit beta"
location: "7p22.3"
module: 1
arm: "+"
pooled_cpm: 51.0
n_lines_expressing: 44
n_dd_up: 8
n_dd_down: 20
n_dd_up_clean: 5
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 6
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PRKAR1B

*protein kinase cAMP-dependent type I regulatory subunit beta* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.74× (z +9.4, q 5e-18, up in 17 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.25× (z +5.5, q 4e-06, up in 17 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.365× (z -17.7, q 0e+00, down in 41 of 41 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC6A11]] (+0.60, fdr 4e-04), [[ST7L]] (+0.60, fdr 2e-05), [[DNAJC11]] (+0.58, fdr 2e-05); moves opposite to [[ARL3]] (-0.55, fdr 3e-05), [[ECI2]] (-0.55, fdr 4e-05), [[HEBP1]] (-0.54, fdr 8e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TSPAN33]] → it (grade B ⚠); 6 go from it, the strongest it → [[ZNF337-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11986.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +9.4 | 5e-18 | 17/34 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.52×** | +7.3 | 6e-11 | 18/38 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +6.4 | 4e-08 | 16/36 (Panc 03.27, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +5.6 | 3e-06 | 3/42 (KATO III, LS 180, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.5 | 4e-06 | 17/42 (AsPC-1, A498, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.35×** | +5.1 | 4e-05 | 18/41 (NCI-H2347, NCI-H460, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.035 | 9/41 (A498, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.046 | 12/41 (RPMI-7951, J82, …) | two highest doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.055 | 12/41 (AsPC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.20× | +3.2 | 0.067 | 7/42 (KATO III, RKO, …) | inconsistent across doses |  |
| [[Brimonidine (drug)]] 5 µM |  | 1.20× | +3.2 | 0.067 | 2/42 (MIA PaCa-2, HEC-1-A) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.067 | 15/41 (SHP-77, NCI-H2030, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11986.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.365×** | -17.7 | 0e+00 | 41/41 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.397×** | -16.2 | 0e+00 | 40/42 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.427×** | -14.9 | 0e+00 | 37/42 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.492×** | -12.5 | 2e-33 | 34/42 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.542×** | -10.7 | 8e-25 | 31/41 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.586×** | -9.0 | 2e-17 | 31/42 (SW48, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.616×** | -8.5 | 1e-15 | 26/41 (NCI-H1792, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.730×** | -7.8 | 4e-13 | 28/42 (SW48, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.649×** | -7.6 | 2e-12 | 23/41 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.670×** | -7.0 | 1e-10 | 28/42 (LS 180, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.693×** | -6.4 | 7e-09 | 23/42 (PANC-1, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.501×** | -6.3 | 1e-08 | 23/35 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.709×** | -6.0 | 7e-08 | 20/41 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.520×** | -6.0 | 7e-08 | 23/42 (SW48, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.713×** | -5.9 | 1e-07 | 20/41 (SW 1271, RKO, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.775×** | -4.2 | 8e-04 | 21/42 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.791×** | -2.9 | 0.092 | 12/42 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11986. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 139 | 0 | 15 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0725× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -12.7) |
| [[NCI-H1792 (line)]] | alt | 198 | 1 (1 ⚠) | 13 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +13.0) ⚠ cell-cycle shift, would explain all of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.214× (z -14.8) ⚠ toxic; cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.233× (z -14.6) |
| [[NCI-H23 (line)]] | alt | 142 | 0 | 14 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.215× (z -17.1) |
| [[NCI-H1573 (line)]] | alt | 44.3 | 0 | 13 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.126× (z -16.2) |
| [[PANC-1 (line)]] | alt | 93.2 | 0 | 13 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.215× (z -18.3) |
| [[SW480 (line)]] | alt | 134 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -18.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.282× (z -16.3) |
| [[C32 (line)]] | wt | 62.5 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.193× (z -11.9) |
| [[A-427 (line)]] | wt | 56.4 | 0 | 8 (8 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.120× (z -19.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 68.5 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -16.5) |
| [[NCI-H460 (line)]] | wt | 61.7 | 0 | 6 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.304× (z -12.4) |
| [[RKO (line)]] | wt | 31.9 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -11.0) |
| [[BT-474 (line)]] | alt | 50.4 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.245× (z -10.5) |
| [[SW48 (line)]] | wt | 71.6 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -11.6) |
| [[HCT15 (line)]] | alt | 112 | 0 | 4 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.278× (z -10.7) |
| [[LoVo (line)]] | wt | 23.2 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.60× (z +8.7) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.122× (z -14.9) |
| [[SW 1271 (line)]] | alt | 99.8 | 0 | 4 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0483× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.130× (z -8.7) |
| [[KATO III (line)]] | alt | 65.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -12.9) |
| [[A498 (line)]] | wt | 33.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +11.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 59.4 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.279× (z -12.2) |
| [[HS-578T (line)]] | alt | 34.3 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.178× (z -13.3) |
| [[NCI-H2030 (line)]] | alt | 48.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.303× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 15.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +14.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 13.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.39× (z +14.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SHP-77 (line)]] | alt | 104 | 1 | 1 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.46× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -12.1) ⚠ cell-cycle shift, explains ~2% of this change |
| [[A-172 (line)]] | wt | 22.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +11.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 58.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.322× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 36.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +11.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Hs 766T (line)]] | wt | 22.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HT-29 (line)]] | alt | 20.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.246× (z -8.5) |
| [[J82 (line)]] | alt | 16.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.234× (z -9.1) |
| [[LS 180 (line)]] | wt | 33.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.274× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0787× (z -11.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 19.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +20.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.82 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.41 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.77 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 31.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11986), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC6A11]] | +0.60 | +0.52 / +0.26 | both halves | 4e-04 | pathway: Neuronal System |
| [[ST7L]] | +0.60 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[DNAJC11]] | +0.58 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[PCSK6]] | +0.58 | +0.60 / +0.34 | both halves | 1e-04 |  |
| [[NCR3LG1]] | +0.57 | +0.58 / +0.34 | both halves | 1e-04 |  |
| [[P2RY11]] | +0.57 | +0.59 / +0.41 | both halves | 4e-05 | pathway: G alpha (s) signalling events |
| [[PCBP1-AS1]] | +0.57 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[TASOR]] | +0.55 | +0.52 / +0.38 | both halves | 6e-05 |  |
| [[TRAF3]] | +0.55 | +0.59 / +0.38 | both halves | 7e-05 |  |
| [[ZC3H4]] | +0.55 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[EXOSC6]] | +0.54 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[GPATCH4]] | +0.54 | +0.52 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL3]] | -0.55 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[ECI2]] | -0.55 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[HEBP1]] | -0.54 | -0.50 / -0.37 | both halves | 8e-05 | pathway: G alpha (i) signalling events |
| [[PCTP]] | -0.54 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[TSPAN33]] | -0.54 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[NR3C2]] | -0.53 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[RAB2A]] | -0.53 | -0.50 / -0.36 | both halves | 9e-05 |  |
| [[PPP1R12B]] | -0.52 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[MGST3]] | -0.52 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[MPC2]] | -0.51 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[STRN]] | -0.51 | -0.47 / -0.32 | both halves | 2e-04 | pathway: Intracellular signaling by second messengers |
| [[MED30]] | -0.51 | -0.53 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN33]] | B | TSPAN33 activity raises PRKAR1B's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 2.70× lower at baseline in the lines without TSPAN33 | 0.005 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[PCSK6]] | B | PCSK6 activity raises PRKAR1B's level | lines that do not express PCSK6 (21) vs lines expressing it (29) | 1.83× lower at baseline in the lines without PCSK6 | 0.048 | ⚠ within organs, on part of the lines; also absent: BTNL9, CYP4F12, LINC02964 |
| [[TOP2B]] | B | TOP2B activity lowers PRKAR1B's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF337-AS1]] | B | PRKAR1B activity raises ZNF337-AS1's level | lines that do not express PRKAR1B (6) vs lines expressing it (44) | 1.81× lower at baseline in the lines without PRKAR1B | 0.056 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[DENND1A]] | B | PRKAR1B activity raises DENND1A's level | lines that do not express PRKAR1B (6) vs lines expressing it (44) | 1.80× lower at baseline in the lines without PRKAR1B | 0.068 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FAM83H]] | B | PRKAR1B activity raises FAM83H's level | lines that do not express PRKAR1B (6) vs lines expressing it (44) | 2.91× lower at baseline in the lines without PRKAR1B | 0.070 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TSPAN33]] | B | PRKAR1B activity raises TSPAN33's level | lines that do not express PRKAR1B (6) vs lines expressing it (44) | 2.45× lower at baseline in the lines without PRKAR1B | 0.090 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ADCK1]] | B | PRKAR1B activity raises ADCK1's level | lines that do not express PRKAR1B (6) vs lines expressing it (44) | 1.76× lower at baseline in the lines without PRKAR1B | 0.094 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PLAG1]] | B | PRKAR1B activity lowers PLAG1's level | lines that do not express PRKAR1B (6) vs lines expressing it (44) | 3.28× higher at baseline in the lines without PRKAR1B | 0.098 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.496). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (2.9, -4.8); signed map (26.1, -32.1). **Vector** length 102, 26.1% of its response variance represented; |z| ≥ 3 in 1,149 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.7 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.7 | -1.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +1.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +5.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +2.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -7.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.9 | -7.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.8 | -9.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.5 | -17.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -6.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -1.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase cAMP-dependent type I regulatory subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:549,197-727,650 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Protein kinase A subunits |
| Reactome | 44 pathways, smallest: CREB1 phosphorylation through the activation of Adenylate Cyclase; PKA activation in glucagon signalling; PKA activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P31321](https://www.uniprot.org/uniprotkb/P31321) (cAMP-dependent protein kinase type I-beta regulatory subunit):

> Regulatory subunit of the cAMP-dependent protein kinases involved in cAMP signaling in cells.

**Summary**, from NCBI Gene [5575](https://www.ncbi.nlm.nih.gov/gene/5575):

> The protein encoded by this gene is a regulatory subunit of cyclic AMP-dependent protein kinase A (PKA), which is involved in the signaling pathway of the second messenger cAMP. Two regulatory and two catalytic subunits form the PKA holoenzyme, disbands after cAMP binding. The holoenzyme is involved in many cellular events, including ion transport, metabolism, and transcription. Several transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Aug 2015]

**Accessions** — [HGNC:9390](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9390) · Entrez [5575](https://www.ncbi.nlm.nih.gov/gene/5575) · UniProt [P31321](https://www.uniprot.org/uniprotkb/P31321) · Ensembl [ENSG00000188191](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188191)

## Data

Gene col 11986: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11986); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11986, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11986]; `tensor/DDL_lfc|DDL_z.npy` [11986]; `embed/gene_vectors.npy` [11986]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11986 or target_col == 11986). Every well: [[PRKAR1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKAR1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
