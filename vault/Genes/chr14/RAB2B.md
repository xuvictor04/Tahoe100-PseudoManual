---
symbol: "RAB2B"
type: "gene"
col: 4975
ensembl_id: "ENSG00000129472"
name: "RAB2B, member RAS oncogene family"
location: "14q11.2"
module: 4
arm: "-"
pooled_cpm: 39.0
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 13
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# RAB2B

*RAB2B, member RAS oncogene family* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.65× (z +11.0, q 2e-25, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.716× (z -7.3, q 1e-10, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SIRT2]] (+0.68, fdr 7e-06), [[CRY2]] (+0.68, fdr 1e-05), [[SDF2]] (+0.62, fdr 3e-05); moves opposite to [[CYREN]] (-0.58, fdr 3e-05), [[TASOR]] (-0.58, fdr 1e-05), [[DPY19L1P2]] (-0.57, fdr 5e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4975.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +11.0 | 2e-25 | 31/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +9.8 | 3e-20 | 35/48 (MIA PaCa-2, LoVo, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.49×** | +8.8 | 2e-16 | 33/48 (LoVo, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +6.8 | 1e-09 | 26/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.27×** | +5.3 | 2e-05 | 19/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.24×** | +4.7 | 2e-04 | 21/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.20×** | +4.1 | 0.004 | 20/48 (LoVo, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.004 | 16/47 (RKO, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +4.0 | 0.004 | 15/48 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.8 | 0.009 | 18/48 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.19× | +3.7 | 0.012 | 17/48 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.11× | +3.3 | 0.050 | 18/48 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +3.2 | 0.069 | 12/48 (MIA PaCa-2, Panc 03.27, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4975.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.716×** | -7.3 | 1e-10 | 36/48 (SNU-423, C32, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.717×** | -7.0 | 4e-10 | 28/47 (SW480, SNU-423, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.718×** | -7.0 | 4e-10 | 24/40 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.728×** | -7.0 | 4e-10 | 27/47 (LoVo, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.753×** | -5.8 | 1e-06 | 22/43 (KATO III, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.778×** | -5.3 | 1e-05 | 24/48 (SNU-423, A549, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change | **0.801×** | -4.9 | 9e-05 | 21/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **0.802×** | -4.8 | 1e-04 | 26/46 (COLO 205, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **0.822×** | -4.3 | 0.001 | 19/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.825×** | -4.2 | 0.001 | 22/47 (MIA PaCa-2, COLO 205, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.828×** | -4.0 | 0.003 | 15/47 (hTERT-HPNE, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.837× | -3.9 | 0.005 | 19/48 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.890× | -3.6 | 0.013 | 12/48 (A-427, CFPAC-1, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.734×** | -3.6 | 0.015 | 13/48 (SHP-77, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | 0.849× | -3.4 | 0.021 | 9/47 (H4, NCI-H2347, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.864× | -3.2 | 0.049 | 19/48 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 5 µM |  | **0.761×** | -3.1 | 0.058 | 13/48 (MIA PaCa-2, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.870× | -3.0 | 0.074 | 13/48 (LoVo, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4975. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 33.6 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.12× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.335× (z -11.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 45.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[NCI-H1792 (line)]] | alt | 68.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 40.2 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +12.8) | — |
| [[PANC-1 (line)]] | alt | 28.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +18.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +12.3) | — |
| [[A-427 (line)]] | wt | 37.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[SNU-423 (line)]] | alt | 34.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.276× (z -11.0) |
| [[SW1417 (line)]] | alt | 32.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.51× (z +8.6) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[AsPC-1 (line)]] | alt | 27.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 54.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 49.2 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.161× (z -8.9) ⚠ toxic |
| [[H4 (line)]] | wt | 51.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -9.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 58.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -8.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 25.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -8.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 36.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -10.3) |
| [[KATO III (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -15.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 37.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -10.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 32.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 51.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.451× (z -9.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 64.6 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.101× (z -12.3) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 46.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4975), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRT2]] | +0.68 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[CRY2]] | +0.68 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[SDF2]] | +0.62 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[RANBP10]] | +0.62 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[CCS]] | +0.60 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[CBFA2T2]] | +0.59 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[PI4KAP1-1]] | +0.58 | +0.58 / +0.39 | both halves | 6e-05 |  |
| [[ALDOC]] | +0.56 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[KCTD7]] | +0.56 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[SEZ6L2]] | +0.56 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[HILPDA]] | +0.56 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[ABCB9]] | +0.56 | +0.55 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYREN]] | -0.58 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[TASOR]] | -0.58 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[DPY19L1P2]] | -0.57 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[ITPRIPL2]] | -0.56 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[MAPKAP1]] | -0.56 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[ATIC]] | -0.56 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[EIF4G1]] | -0.56 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[TMEM147-AS1]] | -0.55 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[RUVBL1]] | -0.54 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[UTP15]] | -0.54 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[DPH5-DT]] | -0.54 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[LINC01355]] | -0.54 | -0.50 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers RAB2B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CCDC9B]] | B | CCDC9B activity lowers RAB2B's level | lines that do not express CCDC9B (13) vs lines expressing it (37) | 1.24× higher at baseline in the lines without CCDC9B | 0.088 | ⚠ within organs, on part of the lines; also absent: LINC02220, COL16A1, CD22 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.442). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (3.1, -17.3); signed map (-27.4, 10.6). **Vector** length 100, 22.7% of its response variance represented; |z| ≥ 3 in 882 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +6.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.9 | +11.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +9.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.0 | +8.8 |
|  | [[NG25 (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.8 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +2.6 |
|  | [[Fumaric acid (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.7 | +2.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.1 | -7.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.3 | -7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -7.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.9 | -2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -4.4 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.6 | -3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | RAB2B, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:21,459,020-21,476,960 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14824 |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 1 pathways, smallest: RAB geranylgeranylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUD1](https://www.uniprot.org/uniprotkb/Q8WUD1) (Ras-related protein Rab-2B):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between active GTP-bound and inactive GDP-bound states. In their active state, drive transport of vesicular carriers from donor organelles to acceptor organelles to regulate the membrane traffic that maintains organelle identity and morphology. Regulates the compacted morphology of the Golgi (Probable). Promotes cytosolic DNA-induced …

**Summary**, from NCBI Gene [84932](https://www.ncbi.nlm.nih.gov/gene/84932):

> Members of the Rab protein family are nontransforming monomeric GTP-binding proteins of the Ras superfamily that contain 4 highly conserved regions involved in GTP binding and hydrolysis. Rab proteins are prenylated, membrane-bound proteins involved in vesicular fusion and trafficking; see MIM 179508.[supplied by OMIM, Apr 2006]

**Accessions** — [HGNC:20246](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20246) · Entrez [84932](https://www.ncbi.nlm.nih.gov/gene/84932) · UniProt [Q8WUD1](https://www.uniprot.org/uniprotkb/Q8WUD1) · Ensembl [ENSG00000129472](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129472)

## Data

Gene col 4975: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4975); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4975, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4975]; `tensor/DDL_lfc|DDL_z.npy` [4975]; `embed/gene_vectors.npy` [4975]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4975 or target_col == 4975). Every well: [[RAB2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
