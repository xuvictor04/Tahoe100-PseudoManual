---
symbol: "BBS2"
type: "gene"
col: 4588
ensembl_id: "ENSG00000125124"
name: "Bardet-Biedl syndrome 2"
location: "16q13"
module: 65
arm: "+"
pooled_cpm: 32.46
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 35
n_dd_up_clean: 4
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# BBS2

*Bardet-Biedl syndrome 2* — 16q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.42× (z +6.4, q 7e-08, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.329× (z -20.5, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LTA4H]] (+0.72, fdr 7e-06), [[TRAPPC11]] (+0.65, fdr 7e-06), [[ANAPC4]] (+0.64, fdr 7e-06); moves opposite to [[CLCF1]] (-0.60, fdr 1e-05), [[CDR2]] (-0.59, fdr 1e-05), [[KCNJ14]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CYB5A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4588.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +6.4 | 7e-08 | 34/48 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.24×** | +5.5 | 8e-06 | 23/48 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +4.2 | 0.005 | 14/48 (SHP-77, BT-474, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.25×** | +4.1 | 0.005 | 19/48 (LS 180, HCT15, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.005 | 20/48 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +3.7 | 0.021 | 18/48 (C32, Hs 766T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.035 | 18/48 (C32, Hs 766T, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.22×** | +3.5 | 0.035 | 14/36 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.20× | +3.3 | 0.050 | 9/48 (NCI-H2030, SW480, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.20× | +3.3 | 0.050 | 11/48 (NCI-H2030, KATO III, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.077 | 18/48 (C32, Hs 766T, …) | two highest doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 1.18× | +3.0 | 0.12 | 6/48 (C32, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4588.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.329×** | -20.5 | 0e+00 | 46/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.374×** | -18.2 | 0e+00 | 45/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.440×** | -15.1 | 0e+00 | 43/48 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.561×** | -15.1 | 0e+00 | 36/47 (NCI-H460, SK-MEL-2, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.444×** | -15.0 | 0e+00 | 45/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.476×** | -13.7 | 9e-41 | 44/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.482×** | -13.5 | 2e-39 | 46/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.492×** | -12.6 | 2e-34 | 36/48 (NCI-H1573, NCI-H460, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.509×** | -12.5 | 8e-34 | 40/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.594×** | -9.6 | 5e-20 | 34/48 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.600×** | -9.4 | 2e-19 | 37/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.647×** | -8.0 | 5e-14 | 30/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.656×** | -7.5 | 3e-12 | 32/47 (AN3 CA, Hs 766T, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.475×** | -7.2 | 3e-11 | 34/48 (MIA PaCa-2, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.478×** | -7.1 | 4e-11 | 32/48 (SNU-1, NCI-H2030, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.705×** | -6.1 | 3e-08 | 28/48 (CFPAC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.712×** | -6.0 | 5e-08 | 26/47 (H4, C32, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.723×** | -6.0 | 6e-08 | 29/48 (SW 1271, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.813×** | -5.4 | 2e-06 | 28/48 (CHP-212, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.601×** | -4.9 | 2e-05 | 22/48 (A498, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4588. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 36.6 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -22.8) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.240× (z -14.4) |
| [[PANC-1 (line)]] | alt | 27.4 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -15.4) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.331× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 29.3 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.214× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.245× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 52.8 | 0 | 7 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.239× (z -13.5) |
| [[SW480 (line)]] | alt | 38.2 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -18.2) |
| [[A498 (line)]] | wt | 33.5 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -12.4) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.381× (z -9.9) |
| [[C32 (line)]] | wt | 68.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -15.0) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.227× (z -11.4) |
| [[HOP62 (line)]] | alt | 32.2 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.171× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.200× (z -14.0) |
| [[LoVo (line)]] | wt | 26.3 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +10.1) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.251× (z -12.4) |
| [[A-172 (line)]] | wt | 42.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.317× (z -9.9) |
| [[A549 (line)]] | wt | 29.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -13.9) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.285× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 28.2 | 0 | 4 (2 ⚠) | — | [[Roxadustat (drug)]] 0.05 µM 0.0610× (z -15.3) |
| [[NCI-H1573 (line)]] | alt | 29.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -15.0) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.309× (z -9.9) |
| [[SNU-423 (line)]] | alt | 33.5 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.261× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.338× (z -9.4) |
| [[Hs 766T (line)]] | wt | 44.1 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.178× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -11.0) |
| [[KATO III (line)]] | alt | 31.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.263× (z -10.8) |
| [[LS 180 (line)]] | wt | 38.3 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.261× (z -12.4) |
| [[SW 900 (line)]] | alt | 29.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -15.9) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.173× (z -12.4) |
| [[CFPAC-1 (line)]] | alt | 29.2 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.330× (z -9.4) |
| [[HT-29 (line)]] | alt | 23.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -11.3) |
| [[J82 (line)]] | alt | 28.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.261× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.323× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 44.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -13.5) ⚠ cell-cycle shift, explains ~47% of this change |
| [[RKO (line)]] | wt | 25.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.240× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 25.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -16.5) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.287× (z -8.6) |
| [[AN3 CA (line)]] | alt | 33.3 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0793× (z -9.8) |
| [[CHP-212 (line)]] | wt | 36.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -9.6) |
| [[H4 (line)]] | wt | 26.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -9.6) |
| [[HCT15 (line)]] | alt | 35.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -12.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 38.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.382× (z -9.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 22.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.255× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 26.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.211× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -9.3) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SHP-77 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -14.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4588), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LTA4H]] | +0.72 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[TRAPPC11]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[ANAPC4]] | +0.64 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[PPP1CB]] | +0.63 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[TM7SF3]] | +0.63 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[IARS2]] | +0.63 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[FRG1BP]] | +0.62 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[LANCL1]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[COPS8]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ALDH7A1]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[EXD2]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[MRS2]] | +0.59 | +0.58 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLCF1]] | -0.60 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[CDR2]] | -0.59 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[KCNJ14]] | -0.58 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[EIF3J]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[TBILA]] | -0.53 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[DNTTIP2]] | -0.53 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[UCKL1-AS1]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[CRK]] | -0.52 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[WNT2B]] | -0.52 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[ORAI2]] | -0.52 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[LINC02798]] | -0.51 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[FBXO10]] | -0.51 | -0.46 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYB5A]] | B | CYB5A activity raises BBS2's level | lines that do not express CYB5A (6) vs lines expressing it (44) | 1.21× lower at baseline in the lines without CYB5A | 0.091 | ⚠ within organs, on part of the lines; also absent: FGF11 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.666). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-5.1, -8.5); signed map (-32.4, -15.1). **Vector** length 77.3, 17.6% of its response variance represented; |z| ≥ 3 in 1,372 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | +5.0 | +5.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.1 | +3.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +3.0 | +2.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.9 | +4.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.3 | +3.5 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.2 | +1.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +2.1 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.7 | -13.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.0 | -15.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -5.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.7 | -9.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.5 | -13.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -9.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.6 | -3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -6.0 |

## What is on record

|  |  |
|---|---|
| Name | Bardet-Biedl syndrome 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q13 — chr16:56,465,640-56,582,667 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously BBS |
| Gene groups (HGNC) | BBSome |
| Reactome | 5 pathways, smallest: BBSome-mediated cargo-targeting to cilium; Cargo trafficking to the periciliary membrane; Assembly of the 9+0 primary cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXC9](https://www.uniprot.org/uniprotkb/Q9BXC9) (BBSome complex member BBS2):

> The BBSome complex is thought to function as a coat complex required for sorting of specific membrane proteins to the primary cilia. The BBSome complex is required for ciliogenesis but is dispensable for centriolar satellite function. This ciliogenic function is mediated in part by the Rab8 GDP/GTP exchange factor, which localizes to the basal body and contacts the BBSome. Rab8(GTP) enters the primary cilium and promotes extension of the ciliary membrane. Firstly the BBSome associates with the …

**Summary**, from NCBI Gene [583](https://www.ncbi.nlm.nih.gov/gene/583):

> This gene is a member of the Bardet-Biedl syndrome (BBS) gene family. Bardet-Biedl syndrome is an autosomal recessive disorder characterized by severe pigmentary retinopathy, obesity, polydactyly, renal malformation and cognitive disability. The proteins encoded by BBS gene family members are structurally diverse and the similar phenotypes exhibited by mutations in BBS gene family members is likely due to their shared roles in cilia formation and function. Many BBS proteins localize to the …

**Accessions** — [HGNC:967](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:967) · Entrez [583](https://www.ncbi.nlm.nih.gov/gene/583) · UniProt [Q9BXC9](https://www.uniprot.org/uniprotkb/Q9BXC9) · Ensembl [ENSG00000125124](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125124)

## Data

Gene col 4588: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4588); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4588, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4588]; `tensor/DDL_lfc|DDL_z.npy` [4588]; `embed/gene_vectors.npy` [4588]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4588 or target_col == 4588). Every well: [[BBS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BBS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
