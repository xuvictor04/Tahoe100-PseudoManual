---
symbol: "TM9SF5P"
type: "gene"
col: 13936
ensembl_id: "ENSG00000234062"
name: "transmembrane 9 superfamily member 5, pseudogene"
location: "Xq26.3"
module: 26
arm: "+"
pooled_cpm: 14.61
n_lines_expressing: 48
n_dd_up: 20
n_dd_down: 29
n_dd_up_clean: 19
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# TM9SF5P

*transmembrane 9 superfamily member 5, pseudogene* — Xq26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.38× (z +12.8, q 1e-34, up in 38 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.449× (z -8.3, q 4e-14, down in 28 of 45 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GALNT7-DT]] (+0.71, fdr 1e-05), [[NEK11]] (+0.70, fdr 1e-05), [[CCDC90B-AS1]] (+0.67, fdr 4e-05); moves opposite to [[WASF3]] (-0.62, fdr 1e-04), [[MINK1]] (-0.61, fdr 6e-05), [[HDAC11]] (-0.58, fdr 1e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13936.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.38×** | +12.8 | 1e-34 | 38/44 (LoVo, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.93×** | +6.8 | 2e-09 | 22/45 (NCI-H460, SK-MEL-2, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.74×** | +5.5 | 6e-06 | 28/44 (HS-578T, A549, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.64×** | +5.2 | 4e-05 | 25/45 (J82, AsPC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.51×** | +4.3 | 0.002 | 22/45 (A549, NCI-H23, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.38×** | +4.1 | 0.005 | 18/46 (NCI-H23, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.47×** | +4.0 | 0.005 | 21/44 (SK-MEL-2, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.44×** | +3.7 | 0.015 | 14/46 (NCI-H23, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.29×** | +3.7 | 0.015 | 16/46 (AsPC-1, NCI-H460, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.29×** | +3.6 | 0.015 | 16/46 (A549, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.015 | 17/44 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Meloxicam (drug)]] 0.05 µM |  | **1.41×** | +3.6 | 0.015 | 13/45 (HEC-1-A, SW48, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.018 | 16/46 (AsPC-1, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.43×** | +3.5 | 0.021 | 13/45 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.046 | 11/46 (NCI-H23, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.047 | 9/46 (HOP62, SW1417, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13936.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.449×** | -8.3 | 4e-14 | 28/45 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.451×** | -8.3 | 4e-14 | 32/45 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.464×** | -8.0 | 3e-13 | 32/45 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.245×** | -7.6 | 3e-12 | 30/44 (PANC-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.518×** | -6.8 | 1e-09 | 27/45 (PANC-1, NCI-H1573, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.557×** | -6.1 | 1e-07 | 25/45 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.560×** | -6.0 | 2e-07 | 27/45 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.579×** | -5.7 | 1e-06 | 26/43 (PANC-1, NCI-H1573, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.364×** | -5.5 | 2e-06 | 24/41 (HS-578T, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.589×** | -5.5 | 2e-06 | 21/44 (A498, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~25% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.607×** | -5.0 | 3e-05 | 22/38 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.711×** | -5.0 | 3e-05 | 26/46 (RPMI-7951, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.625×** | -4.9 | 5e-05 | 23/45 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.739×** | -4.4 | 4e-04 | 24/46 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.653×** | -4.2 | 0.001 | 20/44 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.702×** | -3.5 | 0.013 | 18/46 (SW 1271, HEC-1-A, …) | top dose only | position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **0.712×** | -3.5 | 0.013 | 17/45 (Hs 766T, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.718×** | -3.4 | 0.017 | 16/45 (SW48, SK-MEL-2, …) | rises with dose |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.735×** | -3.2 | 0.039 | 6/45 (HS-578T, RKO, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.738×** | -3.1 | 0.042 | 14/45 (HT-29, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13936. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 42.5 | 0 | 14 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0872× (z -22.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.293× (z -11.1) |
| [[A498 (line)]] | wt | 30.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -12.1) |
| [[SW480 (line)]] | alt | 17.3 | 1 (1 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.64× (z +11.3) ⚠ cell-cycle shift, explains ~57% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.217× (z -11.4) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HEC-1-A (line)]] | alt | 11.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.87× (z +12.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.168× (z -8.8) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 47.4 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.404× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 14.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0702× (z -13.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A-427 (line)]] | wt | 16.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.213× (z -9.7) |
| [[A549 (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.169× (z -8.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[CFPAC-1 (line)]] | alt | 6.21 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.192× (z -8.5) |
| [[H4 (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0706× (z -10.5) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 9.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 13.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 14.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.158× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0963× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[KATO III (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[LoVo (line)]] | wt | 5.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.90× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -9.1) ⚠ cell-cycle shift, explains ~39% of this change |
| [[LS 180 (line)]] | wt | 8.14 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0884× (z -9.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H1792 (line)]] | alt | 5.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.89× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 13.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.46× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.105× (z -10.2) ⚠ transcription drop; cell-cycle shift, explains ~73% of this change |
| [[SW48 (line)]] | wt | 11.3 | 0 | 1 | — | [[Rutin (trihydrate) (drug)]] 5 µM 0.0625× (z -8.6) |
| [[A-172 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.59 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13936), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNT7-DT]] | +0.71 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[NEK11]] | +0.70 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | +0.67 | +0.67 / +0.43 | both halves | 4e-05 |  |
| [[EFCAB2]] | +0.66 | +0.63 / +0.36 | both halves | 9e-05 |  |
| [[PKN2-AS1]] | +0.66 | +0.62 / +0.35 | both halves | 1e-04 |  |
| [[DNAI4]] | +0.62 | +0.64 / +0.26 | both halves | 4e-04 |  |
| [[CFAP418-AS1]] | +0.62 | +0.59 / +0.37 | both halves | 7e-05 |  |
| [[EIF1B-AS1]] | +0.62 | +0.61 / +0.37 | both halves | 8e-05 |  |
| [[ALOX12-AS1]] | +0.62 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[WARS2-AS1]] | +0.62 | +0.67 / +0.31 | both halves | 2e-04 |  |
| [[CCDC30]] | +0.62 | +0.56 / +0.37 | both halves | 8e-05 |  |
| [[RFX3-DT]] | +0.61 | +0.60 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASF3]] | -0.62 | -0.63 / -0.33 | both halves | 1e-04 |  |
| [[MINK1]] | -0.61 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[HDAC11]] | -0.58 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[NDUFA12]] | -0.57 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[DPY30]] | -0.57 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[SDHAF3]] | -0.56 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[HMOX2]] | -0.55 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[GRAMD4]] | -0.55 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[RSAD1]] | -0.55 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[SMARCD3]] | -0.55 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[NR2C1]] | -0.55 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[STN1]] | -0.54 | -0.51 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers TM9SF5P's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[ANKRD18B]] | B | ANKRD18B activity raises TM9SF5P's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 1.48× lower at baseline in the lines without ANKRD18B | 0.071 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.649). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.3, 13.3); signed map (24.6, -4.7). **Vector** length 88.0, 19.9% of its response variance represented; |z| ≥ 3 in 1,161 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +12.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.0 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +5.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.7 | +4.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.3 | +3.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.3 | -5.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.6 | -8.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.3 | -6.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.2 | -2.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.2 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.1 | -2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane 9 superfamily member 5, pseudogene |
| Locus type | pseudogene |
| Location | Xq26.3 — chrX:136,958,883-137,021,479 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Gene groups (HGNC) | Unitary pseudogenes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55623](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55623) · Entrez [100420958](https://www.ncbi.nlm.nih.gov/gene/100420958) · Ensembl [ENSG00000234062](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234062)

## Data

Gene col 13936: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13936); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13936, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13936]; `tensor/DDL_lfc|DDL_z.npy` [13936]; `embed/gene_vectors.npy` [13936]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13936 or target_col == 13936). Every well: [[TM9SF5P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TM9SF5P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
